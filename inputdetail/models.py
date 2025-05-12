from multiprocessing.pool import INIT
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

# Create your models here.

# Hii ni model inayohifadhi taarifa za idara
class Department(models.Model):
    department_id = models.AutoField(primary_key=True, default="D100")
    department_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.department_name


# Hii ni model inayohifadhi taarifa za programu zinazotolewa na idara
class Program(models.Model):
    program_code = models.CharField(primary_key=True, max_length=50, unique=True,default="P100",)
    program_name = models.CharField(max_length=255, unique=True)
    duration = models.IntegerField()
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs")  # ✅ Added related_name

    def __str__(self):
        return f"{self.program_code} - {self.program_name} ({self.duration} years)"


# Hii ni model inayohifadhi taarifa za kozi zinazohusiana na programu mbalimbali
class Course(models.Model):
    course_code = models.CharField(primary_key=True, max_length=20, unique=True,default="C100")
    course_name = models.CharField(max_length=150, unique=True)
    program_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="courses")  # ✅ Added related_name
    course_credit = models.IntegerField(default=9) 
    # Department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="courses")  # ✅ Added related_name  
    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


# Custom Manager for User Authentication
class UserManager(BaseUserManager):
    def create_user(self, registration_no, email, password=None, **extra_fields):
        if not registration_no:
            raise ValueError("Registration number is required")
        if not email:
            raise ValueError("Email address is required")
        
        email = self.normalize_email(email)
        user = self.model(registration_no=registration_no, email=email, **extra_fields)
        
        if not password:
            password = user.last_name  # Default password is last name
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, registration_no, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(registration_no, email, password, **extra_fields)


# User Model (Custom User Model)
class User(AbstractBaseUser, PermissionsMixin):
    registration_no = models.CharField(max_length=20, unique=True,default="NIT/BIT/1898")
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40, blank=True, null=True)
    phone_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=60, unique=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="users", null =True, blank =True)
    course_code = models.ManyToManyField(Course, related_name="users")  # ✅ Added related_name

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'registration_no'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    groups = models.ManyToManyField(Group, related_name="user_groups")  # ✅ Fixed conflict
    user_permissions = models.ManyToManyField(Permission, related_name="user_permissions")  # ✅ Fixed conflict

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.is_superuser and self.department_id is None:
            raise ValueError("Department is required for non-superuser accounts")
        if not self.pk and not self.password:
            self.set_password(self.last_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.registration_no})"


class Venue(models.Model):
    venue_name = models.CharField(max_length=100, unique=True)
    venue_number = models.CharField(primary_key=True, max_length=10, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.venue_name} ({self.venue_number}) - Capacity: {self.capacity}"


class Group(models.Model):
    group_id = models.AutoField(primary_key=True,default="12")
    academic_year = models.IntegerField()
    group_name = models.CharField(unique=True, max_length=100)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")  # ✅ Added related_name
    students_No = models.IntegerField()
    Program_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="groups")  # ✅ Added related_name
    Department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="groups")  # ✅ Added related_name

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True,)
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="schedules")  # ✅ Merged course_code and course_name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedules")  # ✅ Added related_name
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="schedules")  # ✅ Added related_name
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="schedules")  # ✅ Added related_name
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    updated_at = models.DateTimeField()
    program_code = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="schedules")  # ✅ Added related_name
    program_name = models.ForeignKey(Program, on_delete=models.CASCADE,related_name="Schedule")

    def __str__(self):
        return f"{self.program.program_name}, {self.course.course_name} - {self.day_of_week} {self.start_time} - {self.end_time} at {self.venue.venue_name}"


class Conflict(models.Model):
    CONFLICT_TYPES = [
        ('VENUE_OVERLAP', 'Venue Overlap'),
        ('USER_CLASH', 'User Clash'),
        ('COURSE_OVERLAP', 'Course Overlap'),
    ]
    RESOLUTION_STATUSES = [
        ('PENDING', 'Pending'),
        ('RESOLVED', 'Resolved'),
    ]

    conflict_id = models.AutoField(primary_key=True)
    schedule_1 = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="conflict_schedule_1")
    schedule_2 = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name="conflict_schedule_2", null=True, blank=True)
    conflict_type = models.CharField(max_length=50, choices=CONFLICT_TYPES)
    detected_at = models.DateTimeField(default=now)
    resolution_status = models.CharField(max_length=20, choices=RESOLUTION_STATUSES, default="PENDING")
    resolved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="resolved_conflicts")  # ✅ Added related_name
    resolution_comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_conflict_type_display()} - {self.resolution_status}"

from django.db import models

# Create your models here.
class ClockIn(models.Model):
    user = models.CharField(max_length=50)
    clock_in = models.DateTimeField(auto_now_add=True)
    clock_out = models.DateTimeField(auto_now_add=True)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Clock In'
        verbose_name_plural = 'Clock Ins'
        ordering = ['date']
    
class ClockOut(models.Model):
    user = models.CharField(max_length=50)
    clock_in = models.DateTimeField(auto_now_add=True)
    clock_out = models.DateTimeField(auto_now_add=True)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Clock Out'
        verbose_name_plural = 'Clock Outs'
        ordering = ['date']  
        
class Employee(models.Model):
    user = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    date_of_hire = models.DateField()
    date_of_termination = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['last_name']
        
class Payroll(models.Model):
    user = models.CharField(max_length=50)
    employee = models.CharField(max_length=50)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Payroll'
        verbose_name_plural = 'Payrolls'
        ordering = ['date']    
        
class Schedule(models.Model):
    user = models.CharField(max_length=50)
    employee = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        ordering = ['date']
        
class Task(models.Model):
    user = models.CharField(max_length=50)
    employee = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    task = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['date']
                                          
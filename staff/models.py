from django.db import models

# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True,null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class CheckInTime(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='check_in_times')
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class CheckOutTime(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='check_out_times')
    time = models.TimeField()

    def __str__(self):
        return str(self.time)

class CheckInDate(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='check_in_dates')
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class CheckOutDate(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='check_out_dates')
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class OvertimePayment(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='overtime_payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.amount} on {self.date}'


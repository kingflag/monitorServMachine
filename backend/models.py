from django.db import models


class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    ip_address = models.CharField(max_length=20, unique=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    active_statu = models.BooleanField(default=False)
    create_time = models.TimeField(auto_now_add=True)
    update_time = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'machine_table'

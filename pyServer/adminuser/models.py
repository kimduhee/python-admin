from django.db import models

class AdminUser(models.Model):
    admin_seq = models.IntegerField(primary_key=True)
    admin_id = models.CharField(max_length=20, blank=True, null=False)
    admin_name = models.CharField(max_length=10, blank=True, null=False)
    admin_password = models.CharField(max_length=100, blank=True, null=False)
    reg_dt = models.DateTimeField(null=False)
    upd_dt = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = "admin_user"

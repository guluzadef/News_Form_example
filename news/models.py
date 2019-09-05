from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_time=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        verbose_name ="News"
        verbose_name_plural="News"
        ordering=["-id"]


class Notification(models.Model):
    info = models.ForeignKey(News, on_delete=models.CASCADE)
    types = {
        ('bazaya_melumat_daxil_olundu', 'xeber sayta elave olundu')
    }
    options = models.CharField(max_length=250, choices=types)

    def __str__(self):
        return f"{self.info.title}"

    def get_info(self):
        result = ""
        if self.options == "bazaya_melumat_daxil_olundu":
            result = f"{self.info.title} elave olundu "

        return result
    class Meta:
        verbose_name ="Notifications"
        verbose_name_plural="Notifications"
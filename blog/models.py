from django.db import models

class blogProject(models.Model):
    blogtitle = models.CharField(max_length=200)
    blogdate = models.DateField(auto_now_add=True)
    blogdesc = models.TextField()

    def __str__(self):
        return self.blogtitle

from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=100, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
    
    def __str__(self) -> str:
        return self.name
    
    
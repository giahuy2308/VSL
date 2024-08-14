import os
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Community(models.Model):
    name = models.CharField(max_length=100,default="")
    introduction = models.TextField()
    group_avatar = models.ImageField(upload_to="static/image/", blank=True, null=True)
    p_password = models.CharField(max_length=200,default="",blank=True,null=True)
    is_public = models.BooleanField(default=True)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self):
        remove = super().delete()
        os.remove(self.group_avatar.path)        
        return remove

    def __str__(self):
        return f"{self.id}"

class Participant(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('member', 'Member'),
        ('guest', 'Guest'),
    ]

    user = models.ForeignKey(get_user_model(), related_name="members", on_delete=models.CASCADE)
    community = models.ForeignKey(Community, related_name="participants", on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="guest")

    def __str__(self) -> str:
        return f'{self.user.username} | {self.community.name} | {self.role} | {self.id}'


class Reaction(models.Model):
    TYPE_CHOICES = (
        ("Like", 'like'),
        ("Haha", 'haha'),
    )
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type',"object_id")
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    author = models.ForeignKey(get_user_model(), related_name="reactions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class Page(models.Model):
    community = models.ForeignKey(Community,related_name="pages",on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(),related_name="pages",on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="static/image/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reactions = GenericRelation(Reaction, related_query_name='page')
    
    def delete(self, using=None, keep_parents=False):
        remove = super().delete(using=using, keep_parents=keep_parents)
        os.remove(self.image.path)        
        return remove

    def __str__(self):
        return f"{self.id}"
    

class Comment(models.Model):
    page = models.ForeignKey(Page,related_name="comments",on_delete=models.CASCADE) 
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),related_name="comments",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    reactions = GenericRelation(Reaction, related_query_name='comment')

    def __str__(self):
        return f"{self.id}"
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

# class line is standard just change the name to something appropriate.
# always starts with a capital letter
# here it's Post because we're describing a blog post.
class Post(models.Model):
    # ForeignKey means a link to another model.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # means a field with a fixed or limited number of characters
    title = models.CharField(max_length=200)
    # means a field without a limit.
    text = models.TextField()
    # date and time - has a default of the current time.
    created_date = models.DateTimeField(default=timezone.now)
    # data and time - but without a default.
    published_date = models.DateTimeField(blank=True, null=True)

    # publish method to save the entry in our database.
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # Method to return the title of the post in a string.
    def __str__(self):
        return self.title
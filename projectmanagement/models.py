from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.dispatch import receiver



# Project object(s)
PROJECT_VISIBILITY = ( 
    ("PRIVATE", "Private"), 
    ("PUBLIC", "Public"), 
)

class Project(models.Model):
    user = models.ForeignKey(
        User,
        related_name="projects",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    instructions = models.CharField(max_length=4000)
    visibility = models.CharField( 
        max_length = 10, 
        choices = PROJECT_VISIBILITY, 
        default = 'PRIVATE'
    ) 
    time_created = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.id}: {self.title} by {self.user.username} created {self.time_created:%Y-%m-%d %H:%M}"

# Materials Associated with a Project Object
class ProjectMaterial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=150)
    approx_price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    approx_number_of_units = models.IntegerField()

    def __str__(self):
        return(f"{self.approx_number_of_units} {self.material_name}'s @ ${self.approx_price_per_unit} (each)")
    
    def total_price(self):
        return self.approx_price_per_unit * self.approx_number_of_units


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", 
        related_name="followed_by", 
        symmetrical=False, 
        blank=True
    )
    # starred = models.ManyToManyField()

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        # user_profile.save()
post_save.connect(create_profile, sender=User)


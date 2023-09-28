from django.contrib import admin
from .models import UserProfile, Skill, ContactProfile, Testimonial, Media, Portfolio, Blog, Certificate

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "timestamp")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "score", "image")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "name", "role", "quote")

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "name", "is_active", "body")
    readonly_fields = ("slug", )

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "timestamp", "author", "name", "body")
    readonly_fields = ("slug", )

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    # readonly_fields = ("slug", )

#21:04 pasitikrinti ir kazka pakeisti jei reikia

# from .models import ToDoList, Item
# # Register your models here.
# admin.site.register(ToDoList)
# admin.site.register(Item)

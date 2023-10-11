from django.contrib import admin
from .models import Skill, ContactProfile, Certificate

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "subject")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "score", "image")


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    # readonly_fields = ("slug", )



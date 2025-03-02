from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "member_fname", "member_lname", "member_role")

admin.site.register(Member, MemberAdmin)

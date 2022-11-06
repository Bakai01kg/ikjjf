from django.contrib import admin

from main.models import User,Profile,Club, Country

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    list_display_links = list_display

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name','surname','birthday','gender']
    list_display_links = list_display


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = list_display

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display

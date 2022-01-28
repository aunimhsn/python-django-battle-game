from django.contrib import admin

from .models import Armor, Character, Spell, TypeCharacter, Weapon

# Register your models here.
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Spell)
admin.site.register(Character)
admin.site.register(TypeCharacter)
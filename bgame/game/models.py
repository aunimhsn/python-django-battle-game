from django.db import models
from django.forms import CharField


# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=200)
    damage = models.IntegerField()
    icon_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Armor(models.Model):
    name = models.CharField(max_length=200)
    defense = models.IntegerField()
    icon_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Spell(models.Model):
    name = models.CharField(max_length=200)
    mana = models.IntegerField()
    damage = models.IntegerField()
    icon_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TypeCharacter(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=200)
    hp = models.IntegerField()
    mana = models.IntegerField()
    type_character = models.ForeignKey(TypeCharacter, on_delete=models.CASCADE, default=1)
    weapon = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True)
    armor = models.ForeignKey(Armor, on_delete=models.SET_NULL, null=True) 
    spell = models.ForeignKey(Spell, on_delete=models.SET_NULL, blank=True, null=True) 

    def __str__(self):
        return self.name



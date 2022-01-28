from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from game.models import Character, Weapon, Armor, Spell, TypeCharacter

# Create your views here.
def index(request):
    characters = Character.objects.all()
    return render(request, 'index.html', {'characters': characters})

def weapons(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/index.html', {'weapons': weapons})

def weapons_create(request):
    return render(request, 'weapons/create.html')

# POST 
def weapons_store(request):
    Weapon.objects.create(name=request.POST["name"], damage=request.POST["damage"], icon_path=request.POST["icon_path"])
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('game:weapons-index'))

def armors(request):
    armors = Armor.objects.all()
    return render(request, 'armors/index.html', {'armors': armors})

def armors_create(request):
    return render(request, 'armors/create.html')

# POST 
def armors_store(request):
    Armor.objects.create(name=request.POST["name"], defense=request.POST["defense"], icon_path=request.POST["icon_path"])
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('game:armors-index'))

def characters(request):
    characters = Character.objects.all()
    return render(request, 'characters/index.html', {'characters': characters})

def characters_create(request):
    context = {"armors": Armor.objects.all(), "weapons": Weapon.objects.all(), "spells": Spell.objects.all(), "types_character": TypeCharacter.objects.all()}
    return render(request, 'characters/create.html', context)

# POST 
def characters_store(request):
    Character.objects.create(
        name=request.POST["name"],
        hp=request.POST["hp"],
        mana=request.POST["mana"],
        type_character=TypeCharacter.objects.get(pk=request.POST["type_character"]),
        weapon=Weapon.objects.get(pk=request.POST["weapon"]), 
        armor=Armor.objects.get(pk=request.POST["armor"]),
        spell=Spell.objects.get(pk=request.POST["spell"])
    )
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('game:characters-index'))
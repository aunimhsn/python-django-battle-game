# Generated by Django 4.0.1 on 2022-01-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('defense', models.IntegerField()),
                ('icon_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mana', models.IntegerField()),
                ('damage', models.IntegerField()),
                ('icon_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('damage', models.IntegerField()),
                ('icon_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mana', models.IntegerField()),
                ('damage', models.IntegerField()),
                ('icon_path', models.CharField(max_length=255)),
                ('armor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.armor')),
                ('spell', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.spell')),
                ('weapon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.weapon')),
            ],
        ),
    ]
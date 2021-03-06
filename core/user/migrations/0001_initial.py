# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-15 22:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('member_list', models.TextField(blank=True, null=True)),
                ('group_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('tax_code', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(db_index=True, max_length=255)),
                ('date_creation', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False)),
                ('object_id', models.PositiveIntegerField()),
                ('public', models.BooleanField(db_index=True, default=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=255)),
                ('push_token', models.CharField(blank=True, max_length=255, null=True)),
                ('device_type', models.CharField(db_index=True, max_length=20)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('api_version', models.PositiveSmallIntegerField(blank=True, default=1, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroupChat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('groupchat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to='user.GroupChat')),
                ('invited_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_invited_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
                ('modified_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPrivacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('A', 'Allow'), ('D', 'Deny')], default='D', max_length=1)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privacy_target', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='privacy_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceToken', models.CharField(blank=True, max_length=100, null=True)),
                ('middle_name', models.TextField(blank=True, max_length=20, null=True)),
                ('display_name', models.TextField(blank=True, max_length=50, null=True)),
                ('first_name', models.TextField(blank=True, max_length=50, null=True)),
                ('last_name', models.TextField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('A', 'Another')], default='M', max_length=1)),
                ('address', models.TextField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('job_title', models.TextField(blank=True, max_length=140, null=True)),
                ('company_name', models.TextField(blank=True, max_length=140, null=True)),
                ('business_area', models.CharField(blank=True, max_length=100, null=True)),
                ('university1', models.TextField(blank=True, max_length=140, null=True)),
                ('university2', models.TextField(blank=True, max_length=140, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('year_experience', models.FloatField(blank=True, null=True)),
                ('profile_picture', models.CharField(blank=True, max_length=500, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
                ('personality', models.TextField(blank=True, null=True)),
                ('fav_pros', models.TextField(blank=True, null=True)),
                ('date_pass_change', models.DateField(blank=True, null=True)),
                ('favor_quotation', models.TextField(blank=True, max_length=99999, null=True)),
                ('is_member', models.BooleanField(default=False)),
                ('version', models.IntegerField(blank=True, default=1, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_email_notification', models.BooleanField(default=True)),
                ('public_profile', models.BooleanField(default=True)),
                ('visible_search', models.BooleanField(default=True)),
                ('receive_push_notification', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usersettings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='UserVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.FloatField(default=1.0)),
                ('source', models.CharField(default='ios', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userversion', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

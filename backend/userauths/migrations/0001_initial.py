# Generated by Django 4.2 on 2023-10-25 22:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('addon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(max_length=500)),
                ('otp', models.CharField(blank=True, max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default/default-user.jpg', null=True, upload_to='accounts/users')),
                ('full_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
                ('state', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('newsletter', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=500, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvxyz', length=10, max_length=20, prefix='', unique=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='addon.tax')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]

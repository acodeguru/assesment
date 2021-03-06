# Generated by Django 3.0 on 2019-12-15 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performance', '0002_auto_20191215_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performancescore',
            name='id',
        ),
        migrations.AlterField(
            model_name='performance',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='performance',
            name='event_date',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='performancescore',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='performancescore',
            name='performance',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='performance.Performance'),
        ),
    ]

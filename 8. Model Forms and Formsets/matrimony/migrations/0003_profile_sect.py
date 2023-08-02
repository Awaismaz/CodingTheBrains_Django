# Generated by Django 4.2.3 on 2023-07-21 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("matrimony", "0002_caste_fatherprofile_hobby_religion_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="sect",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profiles",
                to="matrimony.sect",
            ),
        ),
    ]

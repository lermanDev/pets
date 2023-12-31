# Generated by Django 4.2.6 on 2023-10-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shelter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Shelter Name")),
                ("address", models.TextField(verbose_name="Address")),
                ("city", models.CharField(max_length=100, verbose_name="City")),
                ("state", models.CharField(max_length=100, verbose_name="State")),
                ("zip_code", models.CharField(max_length=10, verbose_name="Zip Code")),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Email Address",
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="Website"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="shelters/",
                        verbose_name="Principal Image",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
            options={
                "verbose_name": "Shelter",
                "verbose_name_plural": "Shelters",
                "ordering": ["name"],
            },
        ),
    ]

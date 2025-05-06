from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'SiteSetting',
                'verbose_name_plural': 'SiteSetting',
                'db_table': 'sitesettings',
            },
        ),
    ]
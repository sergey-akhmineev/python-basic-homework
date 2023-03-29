# Generated by Django 4.1.3 on 2022-11-10 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0003_lpgenre'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='lp',
            name='record_label',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='lp.recordlabel'),
            preserve_default=False,
        ),
    ]

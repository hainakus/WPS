# Generated by Django 2.2.3 on 2019-07-16 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0003_auto_20190710_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('number_guest', models.PositiveIntegerField(default=0)),
                ('nights', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='favorite_counter',
        ),
        migrations.RemoveField(
            model_name='room',
            name='files',
        ),
        migrations.AddField(
            model_name='room',
            name='total_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='accuracy_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='checkin_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='clean_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='communication_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='location_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='space',
            field=models.SmallIntegerField(choices=[(1, 'Entire room'), (2, 'Private Room'), (3, 'Shared Room')], default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='value_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='RoomReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('rating_1', models.SmallIntegerField()),
                ('rating_2', models.SmallIntegerField()),
                ('total_rating', models.SmallIntegerField(blank=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_review', to='rooms.Booking')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='rooms.Room')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='room_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReservedDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserveds', to='rooms.Room')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='rooms.ReservedDates'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='rooms.Room'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

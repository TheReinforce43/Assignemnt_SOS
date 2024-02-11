# Generated by Django 5.0.1 on 2024-02-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_teacherrequest_approved_as_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherrequest',
            name='current_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='current_education_year',
            field=models.CharField(blank=True, choices=[('1st_year', '1st Year'), ('2nd_year', '2nd Year'), ('3rd_year', '3rd Year'), ('4th_year', '4th Year'), ('graduated', 'Graduated'), ('post_graduation_running', 'Enrolled In Postgraduation studies')], max_length=50, null=True, verbose_name='Current Education Year:'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='current_location',
            field=models.TextField(blank=True, choices=[('in_dhaka', 'Inside Dhaka'), ('in_gazipur', 'Inside Gazipur'), ('others', 'Others')], null=True, verbose_name='Current Location'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='cv',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to='teacher_cv'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='describe_your_experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='fb_link',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Facebook Link'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='interested_subjects',
            field=models.CharField(blank=True, choices=[('non_department', 'Non Department'), ('department', 'Department')], max_length=50, null=True, verbose_name='Interested Subjects'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='interested_teaching_area',
            field=models.CharField(blank=True, choices=[('polytechnic', 'Polytechnic'), ('class_6_to_12', 'Class 6-12'), ('duet_admission', 'DUET Admission')], max_length=50, null=True, verbose_name='Interested Teaching Segments'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='link_previous_class',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Previous Class Link Live or Recorded'),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone Number: '),
        ),
        migrations.AlterField(
            model_name='teacherrequest',
            name='university_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='University'),
        ),
    ]

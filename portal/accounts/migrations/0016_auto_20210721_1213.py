# Generated by Django 3.2.4 on 2021-07-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_regdeadline_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsareaofinterests',
            name='fifth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Fifth Choice'),
        ),
        migrations.AlterField(
            model_name='studentsareaofinterests',
            name='first_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='First Choice'),
        ),
        migrations.AlterField(
            model_name='studentsareaofinterests',
            name='fourth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Fourth Choice'),
        ),
        migrations.AlterField(
            model_name='studentsareaofinterests',
            name='second_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Second Choice'),
        ),
        migrations.AlterField(
            model_name='studentsareaofinterests',
            name='third_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Third Choice'),
        ),
        migrations.AlterField(
            model_name='supervisorsareaofinterests',
            name='fifth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Fifth Choice'),
        ),
        migrations.AlterField(
            model_name='supervisorsareaofinterests',
            name='first_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='First Choice'),
        ),
        migrations.AlterField(
            model_name='supervisorsareaofinterests',
            name='fourth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Fourth Choice'),
        ),
        migrations.AlterField(
            model_name='supervisorsareaofinterests',
            name='second_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Second Choice'),
        ),
        migrations.AlterField(
            model_name='supervisorsareaofinterests',
            name='third_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], max_length=200, verbose_name='Third Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedstudents',
            name='fifth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Fifth Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedstudents',
            name='first_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='First Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedstudents',
            name='fourth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Fourth Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedstudents',
            name='second_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Second Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedstudents',
            name='third_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Third Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedsupervisors',
            name='fifth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Fifth Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedsupervisors',
            name='first_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='First Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedsupervisors',
            name='fourth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Fourth Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedsupervisors',
            name='second_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Second Choice'),
        ),
        migrations.AlterField(
            model_name='unallocatedsupervisors',
            name='third_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Robotics', 'Robotics'), ('Data Science', 'Data Science'), ('Algorithm Design', 'Algorithm Design'), ('Machine Learning', 'Machine Learning'), ('Software Development', 'Software Development'), ('Information Systems', 'Information Systems'), ('Web Development', 'Web Development'), ('Database Management', 'Database Management'), ('Networking and Communication', 'Networking and Communication'), ('Cloud Computing', 'Cloud Computing'), ('Design and Animation', 'Design and Animation'), ('Cyber Security', 'Cyber Security')], default=None, max_length=200, verbose_name='Third Choice'),
        ),
    ]
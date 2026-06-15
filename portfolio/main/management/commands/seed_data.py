import os
from django.core.management.base import BaseCommand
from main.models import Profile, Skill, Project, Experience
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed database with initial data for Dmytro Oleksiienko'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Create Superuser if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            self.stdout.write(self.style.SUCCESS('Superuser created (admin:admin)'))

        # Create or update Profile
        profile = Profile.objects.first()
        if not profile:
            profile = Profile.objects.create(
                name='Dmytro Oleksiienko',
                bio='Junior Python developer actively building pet projects to sharpen my skills in FastAPI, Django, and PostgreSQL. Open to new opportunities and eager to grow in a team',
                role='Software Developer',
                email='dmytro.oleksiienko@icloud.com',
                github='https://github.com/Dmytro-Oleksiienko',
                linkedin='https://linkedin.com/in/dmytro-oleksiienko/',
                location='Kharkiv, Ukraine',
                is_available=True,
                photo_url='https://avatars.githubusercontent.com/u/146471958?v=4',
            )
            self.stdout.write(self.style.SUCCESS('Profile created'))
        else:
            if not profile.photo_url:
                profile.photo_url = 'https://avatars.githubusercontent.com/u/146471958?v=4'
                profile.save()
                self.stdout.write(self.style.SUCCESS('Profile updated with photo_url'))

        # Create Skills
        skills = [
            'Python', 'Django', 'FastAPI', 'JavaScript', 
            'React', 'HTML/CSS', 'PostgreSQL', 'Docker', 'Git'
        ]
        if not Skill.objects.exists():
            for i, skill_name in enumerate(skills):
                Skill.objects.create(name=skill_name, order=i)
            self.stdout.write(self.style.SUCCESS('Skills created'))

        # Create Projects
        if not Project.objects.exists():
            Project.objects.create(
                name='portfolio-site',
                description='Personal portfolio website built with Django for the main frontend and admin panel, and FastAPI for handling contact form submissions asynchronously.',
                tagline='Modern web portfolio',
                gitlink='https://github.com/Dmytro-Oleksiienko/portfolio-site',
                order=0
            )
            self.stdout.write(self.style.SUCCESS('Projects created'))

        # Create Experience
        if not Experience.objects.exists():
            Experience.objects.create(
                name='Taras Shevchenko National University of Kyiv',
                faculty='Faculty of Computer Science and Cybernetics',
                department='Software Engineering',
                start_year=2022,
                end_year=2026,
                order=0
            )
            self.stdout.write(self.style.SUCCESS('Experience created'))

        self.stdout.write(self.style.SUCCESS('Data seeding complete!'))

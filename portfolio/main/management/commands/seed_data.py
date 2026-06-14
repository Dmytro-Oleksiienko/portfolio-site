import os
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
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

        # Create Profile
        if not Profile.objects.exists():
            profile = Profile(
                name='Dmytro Oleksiienko',
                bio='Software Engineer passionate about web development, backend engineering, and creating reliable scalable systems. Always eager to learn new technologies and build cool things.',
                role='Software Developer',
                email='dmytro@example.com',
                github='https://github.com/Dmytro-Oleksiienko',
                linkedin='https://linkedin.com/in/dmytro-oleksiienko',
                location='Ukraine',
                is_available=True
            )
            
            # Download avatar
            avatar_url = 'https://avatars.githubusercontent.com/u/146471958?v=4'
            response = requests.get(avatar_url)
            if response.status_code == 200:
                profile.photo.save('avatar.jpg', ContentFile(response.content), save=False)
                
            profile.save()
            self.stdout.write(self.style.SUCCESS('Profile created'))

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

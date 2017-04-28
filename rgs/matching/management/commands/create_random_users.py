from django.core.management.base import BaseCommand
from matching.models import RGSUser, Interest
from random import randint, sample


class Command(BaseCommand):
    interests_data = ['Books', 'Films', 'Sports', 'Videogames', 'Fashion', 'Music', 'Food', 'Technology']
    male_names_data = ['Jordan', 'James', 'Max', 'David', 'Eliot']
    female_names_data = ['Victoria', 'April', 'Kate', 'Alison', 'Susan']
    lastnames_data = ['Johnson', 'Maxwell', 'Fell', 'Willeman', 'Mullen', 'Brown', 'Duffy', 'Casey', 'Mcshane', 'Fletcher']
    gender_data = ['M', 'F']
    
    def generate_interests(self):
        for interest in self.interests_data:
            if Interest.objects.filter(desc=interest).count() == 0:
                i = Interest(desc=interest)
                i.save()

    def add_arguments(self, parser):
        parser.add_argument('users', type=int)

    def handle(self, *args, **options):
        users = options['users']
        self.generate_interests()
        for u in range(users):
            gender = self.gender_data[randint(0,len(self.gender_data) - 1)]
            if gender == 'M':
                name = self.male_names_data[randint(0,len(self.male_names_data) - 1)]
            else:
                name = self.female_names_data[randint(0,len(self.female_names_data) - 1)]
            lastname = self.lastnames_data[randint(0,len(self.lastnames_data) - 1)]
            age = randint(18,80)

            interests = sample(self.interests_data, randint(0,len(self.interests_data) - 1))

            new_user = RGSUser(name=name, lastname=lastname, gender=gender, age=age)
            new_user.save()
            
            for i in interests:
                interest = Interest.objects.get(desc=i)
                new_user.interests.add(interest)

            new_user.save()
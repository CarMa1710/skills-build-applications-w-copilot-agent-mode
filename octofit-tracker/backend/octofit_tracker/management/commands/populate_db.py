from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Activities
        Activity.objects.create(user=tony, activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='yoga', duration=20, date=timezone.now().date())

        # Workouts
        w1 = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        w2 = Workout.objects.create(name='Sprints', description='Sprint intervals', difficulty='hard')

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=2)
        Leaderboard.objects.create(user=bruce, score=80, rank=3)
        Leaderboard.objects.create(user=clark, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

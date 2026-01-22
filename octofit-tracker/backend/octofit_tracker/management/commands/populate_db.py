from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})
        
        # Create unique index on email field
        self.stdout.write('Creating unique index on email field...')
        db.users.create_index([('email', 1)], unique=True)
        
        # Create Teams
        self.stdout.write('Creating teams...')
        teams = [
            {
                '_id': 'marvel',
                'name': 'Team Marvel',
                'description': 'Earth\'s Mightiest Heroes',
                'created_at': datetime.now(),
                'members': []
            },
            {
                '_id': 'dc',
                'name': 'Team DC',
                'description': 'Justice League Members',
                'created_at': datetime.now(),
                'members': []
            }
        ]
        db.teams.insert_many(teams)
        
        # Create Users (Superheroes)
        self.stdout.write('Creating superhero users...')
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com', 'alias': 'Iron Man', 'team': 'marvel'},
            {'name': 'Steve Rogers', 'email': 'captain@marvel.com', 'alias': 'Captain America', 'team': 'marvel'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com', 'alias': 'Thor', 'team': 'marvel'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com', 'alias': 'Black Widow', 'team': 'marvel'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com', 'alias': 'Hulk', 'team': 'marvel'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com', 'alias': 'Spider-Man', 'team': 'marvel'},
            {'name': 'Wanda Maximoff', 'email': 'scarletwitch@marvel.com', 'alias': 'Scarlet Witch', 'team': 'marvel'},
        ]
        
        dc_heroes = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com', 'alias': 'Superman', 'team': 'dc'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com', 'alias': 'Batman', 'team': 'dc'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com', 'alias': 'Wonder Woman', 'team': 'dc'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com', 'alias': 'The Flash', 'team': 'dc'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com', 'alias': 'Aquaman', 'team': 'dc'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com', 'alias': 'Green Lantern', 'team': 'dc'},
            {'name': 'Victor Stone', 'email': 'cyborg@dc.com', 'alias': 'Cyborg', 'team': 'dc'},
        ]
        
        all_heroes = marvel_heroes + dc_heroes
        users = []
        
        for hero in all_heroes:
            user = {
                'name': hero['name'],
                'email': hero['email'],
                'alias': hero['alias'],
                'team': hero['team'],
                'fitness_level': random.choice(['beginner', 'intermediate', 'advanced', 'super-hero']),
                'total_points': 0,
                'created_at': datetime.now(),
                'last_active': datetime.now()
            }
            users.append(user)
        
        result = db.users.insert_many(users)
        user_ids = result.inserted_ids
        
        # Update teams with member IDs
        marvel_user_ids = [uid for uid, hero in zip(user_ids, all_heroes) if hero['team'] == 'marvel']
        dc_user_ids = [uid for uid, hero in zip(user_ids, all_heroes) if hero['team'] == 'dc']
        
        db.teams.update_one({'_id': 'marvel'}, {'$set': {'members': marvel_user_ids}})
        db.teams.update_one({'_id': 'dc'}, {'$set': {'members': dc_user_ids}})
        
        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Superhero Strength Training',
                'description': 'Build strength like your favorite superhero',
                'difficulty': 'intermediate',
                'duration_minutes': 45,
                'exercises': [
                    {'name': 'Push-ups', 'sets': 3, 'reps': 15},
                    {'name': 'Pull-ups', 'sets': 3, 'reps': 10},
                    {'name': 'Squats', 'sets': 4, 'reps': 20},
                    {'name': 'Deadlifts', 'sets': 3, 'reps': 12}
                ],
                'category': 'strength',
                'created_at': datetime.now()
            },
            {
                'name': 'Speed Force Cardio',
                'description': 'Run fast like The Flash',
                'difficulty': 'advanced',
                'duration_minutes': 30,
                'exercises': [
                    {'name': 'Sprint intervals', 'sets': 8, 'duration': '30 seconds'},
                    {'name': 'High knees', 'sets': 3, 'reps': 50},
                    {'name': 'Burpees', 'sets': 4, 'reps': 15}
                ],
                'category': 'cardio',
                'created_at': datetime.now()
            },
            {
                'name': 'Spider-Man Agility Training',
                'description': 'Enhance your agility and flexibility',
                'difficulty': 'intermediate',
                'duration_minutes': 40,
                'exercises': [
                    {'name': 'Box jumps', 'sets': 3, 'reps': 15},
                    {'name': 'Ladder drills', 'sets': 4, 'duration': '2 minutes'},
                    {'name': 'Mountain climbers', 'sets': 4, 'reps': 30}
                ],
                'category': 'agility',
                'created_at': datetime.now()
            },
            {
                'name': 'Hulk Smash Power Workout',
                'description': 'Build explosive power',
                'difficulty': 'advanced',
                'duration_minutes': 50,
                'exercises': [
                    {'name': 'Power cleans', 'sets': 5, 'reps': 5},
                    {'name': 'Box jumps', 'sets': 4, 'reps': 10},
                    {'name': 'Medicine ball slams', 'sets': 4, 'reps': 15}
                ],
                'category': 'power',
                'created_at': datetime.now()
            },
            {
                'name': 'Black Widow Flexibility',
                'description': 'Master flexibility and balance',
                'difficulty': 'beginner',
                'duration_minutes': 35,
                'exercises': [
                    {'name': 'Yoga flow', 'duration': '15 minutes'},
                    {'name': 'Stretching routine', 'duration': '15 minutes'},
                    {'name': 'Balance poses', 'sets': 3, 'duration': '1 minute each'}
                ],
                'category': 'flexibility',
                'created_at': datetime.now()
            }
        ]
        
        db.workouts.insert_many(workouts)
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['running', 'cycling', 'swimming', 'weightlifting', 'yoga', 'martial arts', 'flying', 'web-slinging']
        activities = []
        
        for i, user_id in enumerate(user_ids):
            # Create 5-10 activities per user
            num_activities = random.randint(5, 10)
            for _ in range(num_activities):
                days_ago = random.randint(1, 30)
                activity = {
                    'user_id': user_id,
                    'user_name': all_heroes[i]['name'],
                    'user_alias': all_heroes[i]['alias'],
                    'activity_type': random.choice(activity_types),
                    'duration_minutes': random.randint(20, 120),
                    'distance_km': round(random.uniform(1.0, 20.0), 2) if random.choice([True, False]) else None,
                    'calories_burned': random.randint(100, 800),
                    'points_earned': random.randint(10, 100),
                    'date': datetime.now() - timedelta(days=days_ago),
                    'notes': f'Training session for {all_heroes[i]["alias"]}'
                }
                activities.append(activity)
        
        db.activities.insert_many(activities)
        
        # Calculate and update user total points
        self.stdout.write('Calculating user points...')
        for user_id in user_ids:
            user_activities = db.activities.find({'user_id': user_id})
            total_points = sum(activity['points_earned'] for activity in user_activities)
            db.users.update_one({'_id': user_id}, {'$set': {'total_points': total_points}})
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        leaderboard_entries = []
        
        # Individual leaderboard
        all_users = list(db.users.find())
        all_users.sort(key=lambda x: x['total_points'], reverse=True)
        
        for rank, user in enumerate(all_users, start=1):
            leaderboard_entries.append({
                'user_id': user['_id'],
                'user_name': user['name'],
                'user_alias': user['alias'],
                'team': user['team'],
                'total_points': user['total_points'],
                'rank': rank,
                'type': 'individual',
                'updated_at': datetime.now()
            })
        
        # Team leaderboard
        marvel_points = sum(u['total_points'] for u in all_users if u['team'] == 'marvel')
        dc_points = sum(u['total_points'] for u in all_users if u['team'] == 'dc')
        
        team_scores = [
            {'team': 'marvel', 'points': marvel_points},
            {'team': 'dc', 'points': dc_points}
        ]
        team_scores.sort(key=lambda x: x['points'], reverse=True)
        
        for rank, team_data in enumerate(team_scores, start=1):
            team = db.teams.find_one({'_id': team_data['team']})
            leaderboard_entries.append({
                'team_id': team_data['team'],
                'team_name': team['name'],
                'total_points': team_data['points'],
                'rank': rank,
                'type': 'team',
                'member_count': len(team['members']),
                'updated_at': datetime.now()
            })
        
        db.leaderboard.insert_many(leaderboard_entries)
        
        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(self.style.SUCCESS(f'Teams created: {db.teams.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Users created: {db.users.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Activities created: {db.activities.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts created: {db.workouts.count_documents({})}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard entries: {db.leaderboard.count_documents({})}'))
        
        # Display top 3 heroes
        self.stdout.write('\n=== Top 3 Heroes ===')
        top_heroes = list(db.users.find().sort('total_points', -1).limit(3))
        for i, hero in enumerate(top_heroes, start=1):
            self.stdout.write(f'{i}. {hero["alias"]} ({hero["name"]}) - {hero["total_points"]} points')
        
        # Display team standings
        self.stdout.write('\n=== Team Standings ===')
        self.stdout.write(f'1. Team Marvel: {marvel_points} points')
        self.stdout.write(f'2. Team DC: {dc_points} points')
        
        client.close()

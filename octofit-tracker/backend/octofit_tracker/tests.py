from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime


class UserModelTest(TestCase):
    """Test cases for User model"""
    
    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@example.com',
            alias='Test Man',
            team='marvel',
            fitness_level='beginner'
        )
    
    def test_user_creation(self):
        """Test that a user can be created"""
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.total_points, 0)
    
    def test_user_string_representation(self):
        """Test the string representation of a user"""
        self.assertEqual(str(self.user), 'Test Hero (Test Man)')


class TeamModelTest(TestCase):
    """Test cases for Team model"""
    
    def setUp(self):
        self.team = Team.objects.create(
            _id='test_team',
            name='Test Team',
            description='A test team'
        )
    
    def test_team_creation(self):
        """Test that a team can be created"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team._id, 'test_team')
    
    def test_team_string_representation(self):
        """Test the string representation of a team"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='test_user_id',
            user_name='Test Hero',
            user_alias='Test Man',
            activity_type='running',
            duration_minutes=30,
            calories_burned=300,
            points_earned=50
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created"""
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.duration_minutes, 30)
        self.assertEqual(self.activity.points_earned, 50)


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""
    
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            difficulty='beginner',
            duration_minutes=45,
            category='strength'
        )
    
    def test_workout_creation(self):
        """Test that a workout can be created"""
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 'beginner')


class APIEndpointTests(APITestCase):
    """Test cases for API endpoints"""
    
    def setUp(self):
        self.client = APIClient()
        
        # Create test data
        self.user = User.objects.create(
            name='API Test Hero',
            email='apitest@example.com',
            alias='API Man',
            team='marvel',
            fitness_level='intermediate',
            total_points=100
        )
        
        self.team = Team.objects.create(
            _id='api_team',
            name='API Team',
            description='API test team'
        )
    
    def test_api_root(self):
        """Test that the API root endpoint works"""
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
    
    def test_user_list(self):
        """Test that the user list endpoint works"""
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_user_detail(self):
        """Test that the user detail endpoint works"""
        response = self.client.get(reverse('user-detail', args=[str(self.user._id)]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Hero')
    
    def test_team_list(self):
        """Test that the team list endpoint works"""
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_team_detail(self):
        """Test that the team detail endpoint works"""
        response = self.client.get(reverse('team-detail', args=['api_team']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Team')
    
    def test_activity_list(self):
        """Test that the activity list endpoint works"""
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_leaderboard_list(self):
        """Test that the leaderboard list endpoint works"""
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_workout_list(self):
        """Test that the workout list endpoint works"""
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_user(self):
        """Test creating a new user via API"""
        data = {
            'name': 'New Hero',
            'email': 'newhero@example.com',
            'alias': 'New Man',
            'team': 'dc',
            'fitness_level': 'advanced'
        }
        response = self.client.post(reverse('user-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # Original user + new user
    
    def test_create_activity(self):
        """Test creating a new activity via API"""
        data = {
            'user_id': str(self.user._id),
            'user_name': 'API Test Hero',
            'user_alias': 'API Man',
            'activity_type': 'cycling',
            'duration_minutes': 60,
            'calories_burned': 500,
            'points_earned': 75
        }
        response = self.client.post(reverse('activity-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardTests(APITestCase):
    """Test cases for Leaderboard functionality"""
    
    def setUp(self):
        self.client = APIClient()
        
        # Create leaderboard entries
        Leaderboard.objects.create(
            user_id='user1',
            user_name='Hero One',
            user_alias='Hero 1',
            team='marvel',
            total_points=100,
            rank=1,
            type='individual'
        )
        
        Leaderboard.objects.create(
            team_id='marvel',
            team_name='Team Marvel',
            total_points=500,
            rank=1,
            type='team'
        )
    
    def test_leaderboard_individual(self):
        """Test the individual leaderboard endpoint"""
        response = self.client.get(reverse('leaderboard-individual'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['type'], 'individual')
    
    def test_leaderboard_teams(self):
        """Test the team leaderboard endpoint"""
        response = self.client.get(reverse('leaderboard-teams'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['type'], 'team')

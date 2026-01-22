from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'alias', 'team', 'fitness_level', 
                  'total_points', 'created_at', 'last_active']
        read_only_fields = ['id', 'created_at']


class TeamSerializer(serializers.ModelSerializer):
    """Serializer for Team model"""
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'members']
        read_only_fields = ['created_at']


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for Activity model"""
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user_id', 'user_name', 'user_alias', 'activity_type', 
                  'duration_minutes', 'distance_km', 'calories_burned', 
                  'points_earned', 'date', 'notes']
        read_only_fields = ['id']


class LeaderboardSerializer(serializers.ModelSerializer):
    """Serializer for Leaderboard model"""
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'user_name', 'user_alias', 'team_id', 
                  'team_name', 'team', 'total_points', 'rank', 'type', 
                  'member_count', 'updated_at']
        read_only_fields = ['id', 'updated_at']


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout model"""
    id = serializers.CharField(source='_id', read_only=True)
    
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'difficulty', 'duration_minutes', 
                  'exercises', 'category', 'created_at']
        read_only_fields = ['id', 'created_at']

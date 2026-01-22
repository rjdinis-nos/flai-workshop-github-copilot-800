from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer, TeamSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['team', 'fitness_level']
    search_fields = ['name', 'email', 'alias']
    ordering_fields = ['total_points', 'created_at', 'name']
    ordering = ['-total_points']

    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific user"""
        user = self.get_object()
        activities = Activity.objects.filter(user_id=str(user._id))
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        """Get all members of a specific team"""
        team = self.get_object()
        users = User.objects.filter(team=pk)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get all activities for a specific team"""
        team = self.get_object()
        users = User.objects.filter(team=pk)
        user_ids = [str(user._id) for user in users]
        activities = Activity.objects.filter(user_id__in=user_ids)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing activities
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user_id', 'activity_type', 'user_alias']
    search_fields = ['user_name', 'user_alias', 'activity_type', 'notes']
    ordering_fields = ['date', 'points_earned', 'duration_minutes', 'calories_burned']
    ordering = ['-date']

    @action(detail=False, methods=['get'])
    def recent(self, request):
        """Get recent activities (last 30 days)"""
        from django.utils import timezone
        from datetime import timedelta
        thirty_days_ago = timezone.now() - timedelta(days=30)
        activities = Activity.objects.filter(date__gte=thirty_days_ago)
        serializer = self.get_serializer(activities, many=True)
        return Response(serializer.data)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for viewing leaderboard (read-only)
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['type', 'team']
    ordering_fields = ['rank', 'total_points']
    ordering = ['rank']

    @action(detail=False, methods=['get'])
    def individual(self, request):
        """Get individual leaderboard only"""
        leaderboard = Leaderboard.objects.filter(type='individual')
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def teams(self, request):
        """Get team leaderboard only"""
        leaderboard = Leaderboard.objects.filter(type='team')
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def top_ten(self, request):
        """Get top 10 individual rankings"""
        leaderboard = Leaderboard.objects.filter(type='individual')[:10]
        serializer = self.get_serializer(leaderboard, many=True)
        return Response(serializer.data)


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing workouts
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['difficulty', 'category']
    search_fields = ['name', 'description', 'category']
    ordering_fields = ['name', 'difficulty', 'duration_minutes', 'created_at']
    ordering = ['difficulty', 'name']

    @action(detail=False, methods=['get'])
    def by_difficulty(self, request):
        """Get workouts grouped by difficulty"""
        difficulties = ['beginner', 'intermediate', 'advanced', 'super-hero']
        result = {}
        for difficulty in difficulties:
            workouts = Workout.objects.filter(difficulty=difficulty)
            serializer = self.get_serializer(workouts, many=True)
            result[difficulty] = serializer.data
        return Response(result)

    @action(detail=False, methods=['get'])
    def recommend(self, request):
        """Get workout recommendations based on fitness level"""
        fitness_level = request.query_params.get('fitness_level', 'beginner')
        workouts = Workout.objects.filter(difficulty=fitness_level)[:5]
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)

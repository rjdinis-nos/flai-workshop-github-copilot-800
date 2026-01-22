from djongo import models
from django.utils import timezone


class User(models.Model):
    """User model for fitness app users"""
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    alias = models.CharField(max_length=200, blank=True)
    team = models.CharField(max_length=100, blank=True)
    fitness_level = models.CharField(max_length=50, default='beginner')
    total_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    last_active = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'users'
        ordering = ['-total_points']

    def __str__(self):
        return f"{self.name} ({self.alias})"


class Team(models.Model):
    """Team model for group competitions"""
    _id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    members = models.JSONField(default=list)

    class Meta:
        db_table = 'teams'
        ordering = ['name']

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activity model for tracking user exercises"""
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    user_alias = models.CharField(max_length=200, blank=True)
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories_burned = models.IntegerField()
    points_earned = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-date']
        verbose_name_plural = 'activities'

    def __str__(self):
        return f"{self.user_alias} - {self.activity_type} ({self.date.strftime('%Y-%m-%d')})"


class Leaderboard(models.Model):
    """Leaderboard model for rankings"""
    _id = models.ObjectIdField(primary_key=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=200, blank=True)
    user_alias = models.CharField(max_length=200, blank=True)
    team_id = models.CharField(max_length=100, null=True, blank=True)
    team_name = models.CharField(max_length=200, blank=True)
    team = models.CharField(max_length=100, blank=True)
    total_points = models.IntegerField(default=0)
    rank = models.IntegerField()
    type = models.CharField(max_length=20)  # 'individual' or 'team'
    member_count = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'leaderboard'
        ordering = ['rank']

    def __str__(self):
        if self.type == 'team':
            return f"{self.team_name} - Rank {self.rank}"
        return f"{self.user_alias} - Rank {self.rank}"


class Workout(models.Model):
    """Workout model for suggested exercises"""
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    duration_minutes = models.IntegerField()
    exercises = models.JSONField(default=list)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'workouts'
        ordering = ['difficulty', 'name']

    def __str__(self):
        return f"{self.name} ({self.difficulty})"

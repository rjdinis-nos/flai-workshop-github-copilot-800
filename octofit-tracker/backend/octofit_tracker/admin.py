from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ('name', 'alias', 'email', 'team', 'fitness_level', 'total_points', 'created_at')
    list_filter = ('team', 'fitness_level', 'created_at')
    search_fields = ('name', 'email', 'alias')
    ordering = ('-total_points',)
    readonly_fields = ('_id', 'created_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('_id', 'name', 'email', 'alias')
        }),
        ('Team & Fitness', {
            'fields': ('team', 'fitness_level', 'total_points')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_active')
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ('name', 'description', 'created_at', 'member_count')
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('_id', 'created_at')
    
    def member_count(self, obj):
        """Display the number of members in the team"""
        return len(obj.members) if obj.members else 0
    member_count.short_description = 'Members'


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ('user_alias', 'activity_type', 'duration_minutes', 'points_earned', 'date')
    list_filter = ('activity_type', 'date', 'user_alias')
    search_fields = ('user_name', 'user_alias', 'activity_type', 'notes')
    ordering = ('-date',)
    readonly_fields = ('_id', 'date')
    
    fieldsets = (
        ('User Information', {
            'fields': ('_id', 'user_id', 'user_name', 'user_alias')
        }),
        ('Activity Details', {
            'fields': ('activity_type', 'duration_minutes', 'distance_km', 'calories_burned', 'points_earned')
        }),
        ('Additional Information', {
            'fields': ('date', 'notes')
        }),
    )


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ('rank', 'display_name', 'type', 'total_points', 'updated_at')
    list_filter = ('type', 'team', 'updated_at')
    search_fields = ('user_name', 'user_alias', 'team_name')
    ordering = ('rank',)
    readonly_fields = ('_id', 'updated_at')
    
    def display_name(self, obj):
        """Display either user alias or team name based on type"""
        if obj.type == 'team':
            return obj.team_name
        return obj.user_alias or obj.user_name
    display_name.short_description = 'Name'
    
    fieldsets = (
        ('Ranking Information', {
            'fields': ('_id', 'rank', 'type', 'total_points')
        }),
        ('User Information', {
            'fields': ('user_id', 'user_name', 'user_alias', 'team'),
            'classes': ('collapse',)
        }),
        ('Team Information', {
            'fields': ('team_id', 'team_name', 'member_count'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('updated_at',)
        }),
    )


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ('name', 'difficulty', 'category', 'duration_minutes', 'created_at')
    list_filter = ('difficulty', 'category', 'created_at')
    search_fields = ('name', 'description', 'category')
    ordering = ('difficulty', 'name')
    readonly_fields = ('_id', 'created_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('_id', 'name', 'description')
        }),
        ('Workout Details', {
            'fields': ('difficulty', 'category', 'duration_minutes', 'exercises')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )


# Customize admin site headers
admin.site.site_header = 'OctoFit Tracker Administration'
admin.site.site_title = 'OctoFit Admin'
admin.site.index_title = 'Welcome to OctoFit Tracker Admin Portal'

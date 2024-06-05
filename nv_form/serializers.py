from rest_framework import serializers, validators




class UserSerializer(serializers.Serializer):
    
    # fields = ['first_name', 'last_name', 'email', 'phone_number', 'location', 'university', 'age_range', 'sdg_interest', 'attendance_type', 'academic_level', 'academic_major', 'how_hear_about_ysf', 'contact_preference', 'employment_status', 'expectations', 'shirt_size']
    fields = '__all__'




    
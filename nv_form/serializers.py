from rest_framework import serializers, validators
from .models import User





class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['fullname', 'email_address', 'phone_number', 'gender', 'age', 'volunteering_experience', 'member_of_aiesec', 'travel_from', 'prefer_location', 'preferred_project', 'health_issues', 'please_specify','who_do_we_contact','emergency_contact','anything_else_to_know']
        # fields = '__all__'




    
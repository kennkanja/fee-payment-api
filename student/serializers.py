from  rest_framework import serializers
from student.models import Student, Pay

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('reg_no', 'name','course','year','fee','time')


class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay
        fields = ('student', 'amount','time')
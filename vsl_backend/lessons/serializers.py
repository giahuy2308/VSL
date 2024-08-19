from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if self.context.get("include_lessons"):
            lessons = LessonSerializer(instance.lessons, many=True).data

            for obj in lessons:
                obj.pop("course")

            representation["lessons"] = lessons
            

        return representation


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if self.context.get('include_sections'):
            sections = SectionSerializer(instance.sections, many=True).data

            for obj in sections:
                obj.pop("lesson")

            representation['sections'] = sections

        return representation


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if self.context.get('include_contents'):
            contents = ContentSerializer(instance.contents, many=True).data
            images = ImageSerializer(instance.images, many=True).data
            animations = AnimationSerializer(instance.animations, many=True).data
            li = sorted(contents + images + animations, key=lambda obj: obj["no"])

            for obj in li:
                obj.pop("section")

            representation["contents"] = li

        return representation


class ContentSerializer(serializers.ModelSerializer):
    no = serializers.ReadOnlyField()

    class Meta:
        model = Content
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    no = serializers.ReadOnlyField()

    class Meta:
        model = Image
        fields = "__all__"


class AnimationSerializer(serializers.ModelSerializer):
    no = serializers.ReadOnlyField()

    class Meta:
        model = Animation
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"

class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if self.context.get('include_questions'):
            questions = QuestionSerializer(instance.questions, context={"include_choices":True} , many=True).data

            for obj in questions:
                obj.pop("examination")
                obj.pop("answer")

            representation['questions'] = questions
        
        return representation


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if self.context.get('include_choices'):
            choices = ChoiceSerializer(instance.choices, many=True).data

            for obj in choices:
                obj.pop("question")

            representation['choices'] = choices
        
        return representation


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Assignment
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if self.context.get('include_questions'):
            questions = QuestionSerializer(instance.examination.questions, many=True).data

            for question in questions:
                question.pop("examination")

                userchoice = UserChoice.objects.filter(assignment=instance, question=question["id"])[0].choice

                question["choice"] = ChoiceSerializer(userchoice).data
                question["choice"].pop("question")

            representation['questions'] = questions
        
        return representation


class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = '__all__'


class UserQuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = UserQuestion
        fields = "__all__"


class AnswerForUQSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = AnswerForUQ
        fields = "__all__"


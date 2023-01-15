from .models import Candidate
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from django.db.utils import IntegrityError

# Create your views here.


@permission_classes(
    [
        AllowAny,
    ]
)
class register(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        try:
            Candidate.objects.create(
                email=request.data.get('email'),
                name=request.data.get('name'),
                number=request.data.get('number'),
                section=request.data.get('section', ''),
                hallno=request.data.get('hallno'),
                rollno=request.data.get('rollno'),
                club_preference=request.data.get('club_preference'),
                roles_preference=request.data.get('roles_preference'),
                answer_1_text=request.data.get('answer_1_text', ''),
                answer_2_text=request.data.get('answer_2_text', ''),
                answer_3_text=request.data.get('answer_3_text', ''),
                answer_4_text=request.data.get('answer_4_text', ''),
                answer_5_text=request.data.get('answer_5_text', ''),
                answer_6_text=request.data.get('answer_6_text', ''),
                answer_7_text=request.data.get('answer_7_text', ''),
                answer_8_text=request.data.get('answer_8_text', ''),
                answer_9_text=request.data.get('answer_9_text', ''),
            )
            return Response({"success": True})
        except IntegrityError as e:
            print(e)
            return Response({"success": False, "message": "Not all fields were provided"})


@permission_classes(
    [
        AllowAny,
    ]
)
class register_check_email(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        registered = False
        try:
            email = request.GET.get('email', None)
            registration = Candidate.objects.get(email=email)
            if registration:
                registered = True
        except:
            pass

        return Response({"registered": registered})

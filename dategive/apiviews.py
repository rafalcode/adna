from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response # leaving this oneout (easy, as it's not explicit) cuases problem  Related object does not exist
# from .models import Crec

class DgiveShow(APIView):
    def post(self, request):
        return Response({"token": user.auth_token.key})

from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from . serializers import AdvocateSerializer, CompanySerializer
from . models import Advocate, Company

# Create your views here.

@api_view(['GET'])
def endpoint(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)


@api_view(['GET', 'POST'])
def advocate_list(request):
    # data = ['Dennis', 'Tadas', 'Max']

    # Handles GET requests
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
            # Alternatively
            # username = request.data.get('username'),
            # bio = request.data.get('bio')
        )

    serializer = AdvocateSerializer(advocate, many=False)

    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
    advocates = Advocate.objects.get(username=username)
    # advocates_list = Advocate.objects.all()
    # serializer = AdvocateSerializer(advocates_list, many=True)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocates, many=False)
        return Response(serializer.data)

    if request.method  == 'PUT':
        advocates.username = request.data['username']
        advocates.bio = request.data['bio']
        advocates.save()

        serializer = AdvocateSerializer(advocates, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        advocates.delete()
        return Response(serializer.data)
      


class AdvocateDetail(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise Advocate

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def put(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('Object Deleted!')


@api_view(['GET'])
def company_list(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)
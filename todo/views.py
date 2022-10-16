from functools import partial
from re import L
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from todo.models import Todo
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.serializer import TodoSerializer
from rest_framework import status
from django.template.defaultfilters import slugify


class ShowTodosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        srz_data = TodoSerializer(instance=todos, many=True).data
        return Response(data=srz_data, status=status.HTTP_200_OK)


class CreateTodoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        de_srz = TodoSerializer(data=request.data)
        if de_srz.is_valid():
            de_srz.validated_data["user"] = request.user
            todo = de_srz.create(de_srz.validated_data)
            srz = TodoSerializer(instance=todo)
            return Response(data=srz.data)
        return Response(data=de_srz.errors)


class TodoRetriveView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk, user=request.user)
            srz = TodoSerializer(instance=todo).data
            return Response(data=srz)
        except Todo.DoesNotExist:
            return Response(data={"error": "does not Exist !!"})


class TodoUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        todo = Todo.objects.get(user=request.user, pk=pk)
        de_srz = TodoSerializer(instance=todo, data=request.data, partial=True)
        if de_srz.is_valid():
            de_srz.validated_data["slug"] = slugify(de_srz.validated_data["title"])
            de_srz.save()
            return Response(data=de_srz.data,status=status.HTTP_200_OK)
        return Response(data=de_srz.errors,status=status.HTTP_400_BAD_REQUEST)


class TodoDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk, user=request.user)
            todo.delete()
            return Response(data={"status": "deleted"})
        except Todo.DoesNotExist:
            return Response(data={"status": "does not exist !!"})


class TodoCreateListView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# class UpdateTodoView(APIView):
    # def put(self ,request,pk):


# Create your views here.

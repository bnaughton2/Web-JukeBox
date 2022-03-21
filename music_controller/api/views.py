from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GetRoom(APIView):
    serializer_class = RoomSerializer
    #Kwarg == keyword argument
    lookup_url_kwarg = 'code'
    
    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                data['isHost'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({"Room Not Found": "Invalid Room Code"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"Bad Request": "Room code paramter not found in request"}, status=status.HTTP_400_BAD_REQUEST)

class JoinRoom(APIView):
    lookup_url_kwarg = 'code'

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        code = request.data.get(self.lookup_url_kwarg)
        if code != None:
            roomResult = Room.objects.filter(code=code)
            if len(roomResult) > 0:
                room = roomResult[0]
                self.request.session['roomCode'] = code
                return Response({'message': 'Room Joined!'}, status=status.HTTP_200_OK)
            
            return Response({'Bad Request': 'Invalid Room Code'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'Bad Request': 'Invalid post data, did not find a code key'}, status=status.HTTP_400_BAD_REQUEST)

class CreateRoomView(APIView):
    serializerClass = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializerClass(data=request.data)
        if serializer.is_valid():
            guestCanPause = serializer.data.get('guestCanPause')
            votesToSkip = serializer.data.get('votesToSkip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guestCanPause = guestCanPause
                room.votesToSkip = votesToSkip
                room.save(update_fields=['guestCanPause', 'votesToSkip'])
                self.request.session['roomCode'] = room.code
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guestCanPause=guestCanPause, votesToSkip=votesToSkip)
                room.save()
                self.request.session['roomCode'] = room.code
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
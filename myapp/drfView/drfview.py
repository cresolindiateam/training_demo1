from rest_framework.views import APIView
from rest_framework.response import Response

class ProfileAPI(APIView):
    def get(self, request):
        return Response({"user": request.user.username})



class Aboutus(APIView):
      
      def get(self, request):
        user = request.user

        if user.username=="admin": 
            return Response({
                "about":"old user",
                "role": "admin",
                "username": user.username,
                "email": user.email,
                "all_users_count": user.__class__.objects.count()
            })

        if user.username=="admin1":
            return Response({
                "about":"new user",
                "role": "admin",
                "username": user.username,
                "email": user.email,
                "all_users_count": user.__class__.objects.count()
            })    

        # 👤 normal user
        return Response({
            "role": "user",
            "username": user.username
        })

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from places.models import Place
import os

'''
class SavePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        name = request.data.get('name')
        address = request.data.get('address')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        photo_reference = request.data.get('photo_reference')

        # Save place in Neo4j
        place = Place(name=name, address=address, latitude=latitude, longitude=longitude, photo_reference=photo_reference).save()
        place.saved_by.connect(user)

        return Response({"message": "Place saved successfully", "place_id": place.id}, status=201)
'''

class SavePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        name = request.data.get('name')
        address = request.data.get('address')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        photo_reference = request.data.get('photo_reference')

        place = Place.objects.create(
            name=name, 
            address=address, 
            latitude=latitude, 
            longitude=longitude, 
            photo_reference=photo_reference,
            saved_by=user
        )

        return Response({"message": "Place saved successfully", "place_id": place.id}, status=201)
    
class SearchPlacesView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get("query")
        location = request.query_params.get("location")  
        radius = request.query_params.get("radius", 1000)  

        google_api_key = os.getenv("GOOGLE_API_KEY")
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&location={location}&radius={radius}&key={google_api_key}"

        response = requests.get(url)
        places_data = response.json()

        places = []
        for result in places_data.get("results", []):
            place = {
                "name": result.get("name"),
                "address": result.get("formatted_address"),
                "latitude": result["geometry"]["location"]["lat"],
                "longitude": result["geometry"]["location"]["lng"],
                "photo": result.get("photos", [{}])[0].get("photo_reference"),
            }
            places.append(place)

        return Response({"places": places})

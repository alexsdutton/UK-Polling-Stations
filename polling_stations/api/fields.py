from django.utils.encoding import smart_str
from rest_framework import serializers


class PointField(serializers.Field):
    type_name = 'PointField'
    type_label = 'point'

    def to_representation(self, value):
        """
        Transform POINT object to json.
        """
        if value is None:
            return value

        value = {
            "latitude": smart_str(value.y),
            "longitude": smart_str(value.x)
        }
        return value


class GeoJsonPointField(serializers.Field):
    type_name = 'PointField'
    type_label = 'point'

    def to_representation(self, value):
        """
        Transform POINT object to a geojson feature.
        """
        if value is None:
            return value

        value = {
            "type": "Feature",
            "geometry": {
                "point": {
                    "type": "Point",
                    "coordinates": [
                        value.x,
                        value.y
                    ],
                },
            },
        }
        return value

# How to calculate a service area based on ranges of distance

The CalculateIsolines API allows you to determine reachable service areas within specified ranges of time or distance, factoring in road networks and traffic conditions. This capability supports applications in defining service areas for restaurants, grocery stores, or other service providers which can assist in planning fuel efficiency and defining accessible areas for service coverage.

## Potential use cases

- **Plan service areas:** Use this API to plan accessible areas for services like restaurants or grocery delivery based on travel time or distance.

## Examples

Sample request

```
{
    "Origin": [
        -123.11679620827039,
        49.28147612192166
    ],
    "DepartureTime": "2024-10-28T21:27:56Z",
    "Thresholds": {
        "Distance": [
            1000,
            2000,
            3000
        ]
    },
    "TravelMode": "Car"
}
```

Sample response

```
{
    "DepartureTime": "2024-10-28T14:27:56-07:00",
    "IsolineGeometryFormat": "FlexiblePolyline",
    "Isolines": [
        {
            "Connections": [],
            "DistanceThreshold": 1000,
            "Geometries": [
                {
                    "PolylinePolygon": [
                        "Redacted"
                    ]
                }
            ]
        },
        {
            "Connections": [],
            "DistanceThreshold": 2000,
            "Geometries": [
                {
                    "PolylinePolygon": [
                        "Redacted"
                    ]
                }
            ]
        },
        {
            "Connections": [],
            "DistanceThreshold": 3000,
            "Geometries": [
                {
                    "PolylinePolygon": [
                        "Redacted"
                    ]
                }
            ]
        }
    ],
    "SnappedOrigin": [
        -123.11687,
        49.2813999
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/isolines?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origin": [
        -123.11679620827039,
        49.28147612192166
    ],
    "DepartureTime": "2024-10-28T21:27:56Z",
    "Thresholds": {
        "Distance": [
            1000,
            2000,
            3000
        ]
    },
    "TravelMode": "Car"
}'
```

AWS CLI

```
aws geo-routes calculate-isolines --key ${YourKey} \
--origin -123.11679620827039 49.28147612192166 \
--departure-time "2024-10-28T21:27:56Z" \
--thresholds '{"Distance": [1000, 2000, 3000]}' \
--travel-mode "Car"
```

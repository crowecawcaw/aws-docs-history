# How to find the shortest routes

The CalculateRoutes API helps you to find the shortest routes between origin and destination.

## Potential use cases

- **Optimize routes for time efficiency:** Improve delivery operations by calculating the shortest route. This is useful for reducing travel distance in logistics and delivery services.

## Examples

Sample request

```
{
    "Origin": [
        -123.118105,
        49.282423
    ],
    "Destination": [
        -123.020098,
        49.232872
    ],
    "TravelMode": "Car",
    "OptimizeRoutingFor": "ShortestRoute"
}
```

Sample response

```
{
    "LegGeometryFormat": "FlexiblePolyline",
    "Notices": [],
    "Routes": [
        {
            "Legs": [
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "TravelMode": "Car",
                    "Type": "Vehicle",
                    "VehicleLegDetails": {
                        "AfterTravelSteps": [],
                        "Arrival": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.020098,
                                    49.232872
                                ],
                                "Position": [
                                    -123.0203051,
                                    49.2328499
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.1181051,
                                    49.282423
                                ],
                                "Position": [
                                    -123.1180883,
                                    49.2824349
                                ]
                            }
                        },
                        "Incidents": [],
                        "Notices": [],
                        "PassThroughWaypoints": [],
                        "Spans": [],
                        "Tolls": [],
                        "TollSystems": [],
                        "TravelSteps": [
                            {
                                "Distance": 1288,
                                "Duration": 102,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "ExitNumber": [],
                                "GeometryOffset": 37,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 1356,
                                "Duration": 134,
                                "ExitNumber": [],
                                "GeometryOffset": 42,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 7092,
                                "Duration": 568,
                                "ExitNumber": [],
                                "GeometryOffset": 92,
                                "KeepStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left"
                                },
                                "Type": "Keep"
                            },
                            {
                                "Distance": 65,
                                "Duration": 26,
                                "ExitNumber": [],
                                "GeometryOffset": 337,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 50,
                                "Duration": 18,
                                "ExitNumber": [],
                                "GeometryOffset": 339,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 343,
                                "Type": "Arrive"
                            }
                        ],
                        "TruckRoadTypes": [],
                        "Zones": []
                    }
                }
            ],
            "MajorRoadLabels": [
                {
                    "RouteNumber": {
                        "Language": "en",
                        "Value": "HWY-1A"
                    }
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/routes?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origin": [
        -123.118105,
        49.282423
    ],
    "Destination": [
        -123.020098,
        49.232872
    ],
    "TravelMode": "Car",
    "OptimizeRoutingFor": "ShortestRoute"
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.118105 49.282423 \
--destination -123.020098 49.232872 \
--travel-mode "Scooter" \
--optimize-routing-for "ShortestRoute"

```

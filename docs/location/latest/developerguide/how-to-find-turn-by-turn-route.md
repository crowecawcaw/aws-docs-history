# How to find routes with turn-by-turn directions

The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as car, truck, pedestrian and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination, with only a few constraints.

## Potential use cases

- **Create a navigation mobile app:** Use the API to get turn-by-turn navigation instructions.
- **Display directions on a web platform:** Show detailed route guidance for web applications to assist you with navigation.

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
    "TravelStepType": "TurnByTurn",
    "TravelMode": "Car"
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
                        "Arrival": {
                            "Place": {
                                "Position": [-123.0203051, 49.2328499]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "Position": [-123.1180883, 49.2824349]
                            }
                        },
                        "TravelSteps": [
                            {
                                "Distance": 1288,
                                "Duration": 102,
                                "Type": "Depart",
                                "NextRoad": {
                                    "RoadName": "W Georgia St",
                                    "RouteNumber": "HWY-1A"
                                }
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "Type": "Keep",
                                "NextRoad": {
                                    "RoadName": "Main St",
                                    "RouteNumber": "HWY-1A"
                                }
                            },
                            {
                                "Distance": 1356,
                                "Duration": 134,
                                "Type": "Turn",
                                "NextRoad": {
                                    "RoadName": "Main St",
                                    "RouteNumber": "HWY-1A"
                                }
                            },
                            {
                                "Distance": 7092,
                                "Duration": 568,
                                "Type": "Keep",
                                "NextRoad": {
                                    "RoadName": "Kingsway",
                                    "RouteNumber": "HWY-1A"
                                }
                            },
                            {
                                "Distance": 65,
                                "Duration": 26,
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "Type": "Arrive"
                            }
                        ]
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
  "TravelStepType": "TurnByTurn",
  "TravelMode": "Car"
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.118105 49.282423 \
--destination -123.020098 49.232872 \
--travel-step-type "TurnByTurn" \
--travel-mode "Car"
```

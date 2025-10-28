# How to create routes with custom avoidance of several potential items

The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as car, truck, pedestrian and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination, with only a few constraints.

## Potential use cases

- **Calculate routes with custom avoidance:** Customize routes with avoidance for better routes and commute planning.

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
    "Avoid": {
        "TollRoads": true,
        "UTurns": true,
        "Ferries": true,
        "ControlledAccessHighways": true,
        "Tunnels": true
    }
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
  "Avoid": {
    "TollRoads": true,
    "UTurns": true,
    "Ferries": true,
    "ControlledAccessHighways": true,
    "Tunnels": true
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.118105 49.282423 \
--destination -123.020098 49.232872 \
--travel-mode "Car" \
--avoid '{"TollRoads": true, "UTurns": true, "Ferries": true, "ControlledAccessHighways": true, "Tunnels": true}'

```

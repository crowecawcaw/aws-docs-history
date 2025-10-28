# How to find a speed limit for a road span

The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as car, truck, pedestrian and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination, with only a few constraints.

## Potential use cases

- **Audit speed limit compliance:** Stays aware of speed limits and compliance to them.
- **Inform the driver of the speed limit:** Notifies the driver of the speed limit when it might not be clear otherwise.

## Examples

Sample request

```
{
    "Origin": [
        13.055211,
        52.704802
    ],
    "Destination": [
        13.551910,
        52.282705
    ],
    "TravelMode": "Car",
    "SpanAdditionalFeatures": ["SpeedLimit"]
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
                                    13.55191,
                                    52.282705
                                ],
                                "Position": [
                                    13.5507836,
                                    52.2859121
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    13.055211,
                                    52.704802
                                ],
                                "Position": [
                                    13.0555036,
                                    52.7056073
                                ]
                            }
                        },
                        "Incidents": [],
                        "Notices": [],
                        "PassThroughWaypoints": [],
                        "Spans": [
                            {
                                "GeometryOffset": 0,
                                "SpeedLimit": {
                                    "Unlimited": true
                                }
                            },
                            {
                                "GeometryOffset": 151,
                                "SpeedLimit": {
                                    "MaxSpeed": 120.00000762939453
                                }
                            },
                            {
                                "GeometryOffset": 167,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 195,
                                "SpeedLimit": {
                                    "MaxSpeed": 120.00000762939453
                                }
                            },
                            {
                                "GeometryOffset": 220,
                                "SpeedLimit": {
                                    "Unlimited": true
                                }
                            },
                            {
                                "GeometryOffset": 356,
                                "SpeedLimit": {
                                    "MaxSpeed": 120.00000762939453
                                }
                            },
                            {
                                "GeometryOffset": 358,
                                "SpeedLimit": {
                                    "MaxSpeed": 100
                                }
                            },
                            {
                                "GeometryOffset": 368,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 384,
                                "SpeedLimit": {
                                    "MaxSpeed": 60.000003814697266
                                }
                            },
                            {
                                "GeometryOffset": 639,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 701,
                                "SpeedLimit": {
                                    "MaxSpeed": 60.000003814697266
                                }
                            },
                            {
                                "GeometryOffset": 726,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 805,
                                "SpeedLimit": {
                                    "MaxSpeed": 60.000003814697266
                                }
                            },
                            {
                                "GeometryOffset": 839,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 1384,
                                "SpeedLimit": {
                                    "MaxSpeed": 60.000003814697266
                                }
                            },
                            {
                                "GeometryOffset": 1393,
                                "SpeedLimit": {
                                    "MaxSpeed": 50
                                }
                            },
                            {
                                "GeometryOffset": 1443,
                                "SpeedLimit": {
                                    "MaxSpeed": 30.000001907348633
                                }
                            },
                            {
                                "GeometryOffset": 1454,
                                "SpeedLimit": {
                                    "MaxSpeed": 50
                                }
                            },
                            {
                                "GeometryOffset": 1504,
                                "SpeedLimit": {
                                    "MaxSpeed": 60.000003814697266
                                }
                            },
                            {
                                "GeometryOffset": 1513,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 1516,
                                "SpeedLimit": {
                                    "MaxSpeed": 60.000003814697266
                                }
                            },
                            {
                                "GeometryOffset": 1555,
                                "SpeedLimit": {
                                    "MaxSpeed": 80
                                }
                            },
                            {
                                "GeometryOffset": 1748,
                                "SpeedLimit": {
                                    "MaxSpeed": 120.00000762939453
                                }
                            },
                            {
                                "GeometryOffset": 1904,
                                "SpeedLimit": {
                                    "MaxSpeed": 100
                                }
                            },
                            {
                                "GeometryOffset": 1945,
                                "SpeedLimit": {
                                    "Unlimited": true
                                }
                            },
                            {
                                "GeometryOffset": 2006,
                                "SpeedLimit": {
                                    "MaxSpeed": 70
                                }
                            },
                            {
                                "GeometryOffset": 2017,
                                "SpeedLimit": {
                                    "MaxSpeed": 50
                                }
                            },
                            {
                                "GeometryOffset": 2033,
                                "SpeedLimit": {
                                    "MaxSpeed": 30.000001907348633
                                }
                            }
                        ],
                        "Tolls": [],
                        "TollSystems": [],
                        "TravelSteps": [
                            {
                                "Distance": 9099,
                                "Duration": 262,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 18849,
                                "Duration": 800,
                                "ExitNumber": [],
                                "GeometryOffset": 162,
                                "KeepStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Keep"
                            },
                            {
                                "Distance": 4290,
                                "Duration": 212,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 701,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 14418,
                                "Duration": 651,
                                "ExitNumber": [],
                                "GeometryOffset": 828,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 1255,
                                "Duration": 62,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 1359,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 1607,
                                "Duration": 139,
                                "ExitNumber": [],
                                "GeometryOffset": 1393,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 934,
                                "Duration": 92,
                                "ExitNumber": [],
                                "GeometryOffset": 1442,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 320,
                                "Duration": 27,
                                "ExitNumber": [],
                                "GeometryOffset": 1473,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 320,
                                "Duration": 33,
                                "ExitNumber": [],
                                "GeometryOffset": 1491,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 17863,
                                "Duration": 680,
                                "ExitNumber": [],
                                "GeometryOffset": 1504,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 2888,
                                "Duration": 95,
                                "ExitNumber": [],
                                "GeometryOffset": 1917,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 321,
                                "Duration": 28,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 1977,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 549,
                                "Duration": 41,
                                "ExitNumber": [],
                                "GeometryOffset": 2006,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 386,
                                "Duration": 51,
                                "ExitNumber": [],
                                "GeometryOffset": 2023,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 98,
                                "Duration": 15,
                                "ExitNumber": [],
                                "GeometryOffset": 2033,
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
                                "GeometryOffset": 2036,
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
                        "Language": "de",
                        "Value": "A111"
                    }
                },
                {
                    "RouteNumber": {
                        "Language": "de",
                        "Value": "A113"
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
    13.055211,
    52.704802
  ],
  "Destination": [
    13.551910,
    52.282705
  ],
  "TravelMode": "Car",
  "SpanAdditionalFeatures": ["SpeedLimit"]
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin 13.055211 52.704802 \
--destination 13.551910 52.282705 \
--travel-mode "Car" \
--span-additional-features "SpeedLimit"
```

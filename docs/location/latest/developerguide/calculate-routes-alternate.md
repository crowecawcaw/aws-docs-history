# How to find alternate routes

The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as car, truck, pedestrian and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination, with only a few constraints.

## Potential use cases

- **Identify alternate routes:** Be able to pick the best route to suit your business needs.

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
    "MaxAlternatives": 2
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
                        "Spans": [],
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
        },
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
                        "Spans": [],
                        "Tolls": [],
                        "TollSystems": [],
                        "TravelSteps": [
                            {
                                "Distance": 91047,
                                "Duration": 2880,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 3496,
                                "Duration": 119,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 1473,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 321,
                                "Duration": 28,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 1565,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 549,
                                "Duration": 41,
                                "ExitNumber": [],
                                "GeometryOffset": 1594,
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
                                "GeometryOffset": 1611,
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
                                "GeometryOffset": 1621,
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
                                "GeometryOffset": 1624,
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
                        "Value": "A10"
                    }
                }
            ]
        },
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
                        "Spans": [],
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
                                "Distance": 12258,
                                "Duration": 554,
                                "ExitNumber": [],
                                "GeometryOffset": 828,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 18567,
                                "Duration": 1218,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 1282,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 250,
                                "Duration": 28,
                                "ExitNumber": [],
                                "GeometryOffset": 1760,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 4856,
                                "Duration": 245,
                                "ExitNumber": [],
                                "GeometryOffset": 1793,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 3202,
                                "Duration": 165,
                                "ExitNumber": [],
                                "GeometryOffset": 1970,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 386,
                                "Duration": 51,
                                "ExitNumber": [],
                                "GeometryOffset": 2072,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 98,
                                "Duration": 15,
                                "ExitNumber": [],
                                "GeometryOffset": 2082,
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
                                "GeometryOffset": 2085,
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
                        "Value": "B96"
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
  "MaxAlternatives": 2
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin 13.055211 52.704802 \
--destination 13.551910 52.282705 \
--travel-mode "Car" \
--max-alternatives 2
```

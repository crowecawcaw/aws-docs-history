# How to create routes with custom avoidance

The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as car, truck, pedestrian and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination, with only a few constraints.

## Potential use cases

- **Calculate routes with custom avoidance:** Customize routes with avoidance for better routes and commute planning.

## Examples

Sample request

```
{
    "Origin": [
        -123.116655,
        49.281538
    ],
    "Destination": [
        -123.01791785749363,
        49.22782762759908
    ],
    "TravelMode": "Car",
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "BoundingBox": [
                        -123.078693,
                        49.238987,
                        -123.054638,
                        49.251694
                    ]
                }
            }
        ]
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
                                    -123.0179179,
                                    49.2278276
                                ],
                                "Position": [
                                    -123.0229001,
                                    49.22883
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.116655,
                                    49.281538
                                ],
                                "Position": [
                                    -123.1166332,
                                    49.2815528
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
                                "Distance": 1144,
                                "Duration": 85,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "ExitNumber": [],
                                "GeometryOffset": 35,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 433,
                                "Duration": 47,
                                "ExitNumber": [],
                                "GeometryOffset": 40,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1131,
                                "Duration": 81,
                                "ExitNumber": [],
                                "GeometryOffset": 54,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 54,
                                "Duration": 4,
                                "ExitNumber": [],
                                "GeometryOffset": 79,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 520,
                                "Duration": 39,
                                "ExitNumber": [],
                                "GeometryOffset": 83,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 1123,
                                "Duration": 111,
                                "ExitNumber": [],
                                "GeometryOffset": 101,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1131,
                                "Duration": 81,
                                "ExitNumber": [],
                                "GeometryOffset": 141,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 2843,
                                "Duration": 209,
                                "ExitNumber": [],
                                "GeometryOffset": 167,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 3219,
                                "Duration": 246,
                                "ExitNumber": [],
                                "GeometryOffset": 255,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 64,
                                "Duration": 23,
                                "ExitNumber": [],
                                "GeometryOffset": 332,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 334,
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
                    "RoadName": {
                        "Language": "en",
                        "Value": "Boundary Rd"
                    }
                },
                {
                    "RoadName": {
                        "Language": "en",
                        "Value": "Grandview Hwy"
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
    -123.116655,
    49.281538
  ],
  "Destination": [
    -123.01791785749363,
    49.22782762759908
  ],
  "TravelMode": "Car",
  "Avoid": {
    "Areas": [
      {
        "Geometry": {
          "BoundingBox": [
            -123.078693,
            49.238987,
            -123.054638,
            49.251694
          ]
        }
      }
    ]
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.13277 49.281538 \
--destination -123.01791785749363 49.22782762759908 \
--travel-mode "Car" \
--avoid '{"Areas":[{"Geometry":{"BoundingBox":[-123.054638,49.238987,-123.054638,49.251694]}}]}'

```

Sample request

```
{
    "Origin": [
        -123.116655,
        49.281538
    ],
    "Destination": [
        -123.01791785749363,
        49.22782762759908
    ],
    "TravelMode": "Car",
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "polygon": [
                        [
                            [
                                -123.06953,
                                49.256419
                            ],
                            [
                                -123.080486,
                                49.242115
                            ],
                            [
                                -123.058573,
                                49.242115
                            ],
                            [
                                -123.06953,
                                49.256419
                            ]
                        ]
                    ]
                }
            }
        ]
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
                                    -123.0179179,
                                    49.2278276
                                ],
                                "Position": [
                                    -123.0229001,
                                    49.22883
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.116655,
                                    49.281538
                                ],
                                "Position": [
                                    -123.1166332,
                                    49.2815528
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
                                "Distance": 1144,
                                "Duration": 85,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "ExitNumber": [],
                                "GeometryOffset": 35,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 433,
                                "Duration": 47,
                                "ExitNumber": [],
                                "GeometryOffset": 40,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1131,
                                "Duration": 81,
                                "ExitNumber": [],
                                "GeometryOffset": 54,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 54,
                                "Duration": 4,
                                "ExitNumber": [],
                                "GeometryOffset": 79,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 520,
                                "Duration": 39,
                                "ExitNumber": [],
                                "GeometryOffset": 83,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 1123,
                                "Duration": 111,
                                "ExitNumber": [],
                                "GeometryOffset": 101,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1131,
                                "Duration": 81,
                                "ExitNumber": [],
                                "GeometryOffset": 141,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 448,
                                "Duration": 34,
                                "ExitNumber": [],
                                "GeometryOffset": 167,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 1797,
                                "Duration": 151,
                                "ExitNumber": [],
                                "GeometryOffset": 182,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 2836,
                                "Duration": 224,
                                "ExitNumber": [],
                                "GeometryOffset": 222,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 339,
                                "Duration": 30,
                                "ExitNumber": [],
                                "GeometryOffset": 326,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 64,
                                "Duration": 23,
                                "ExitNumber": [],
                                "GeometryOffset": 335,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 337,
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
                },
                {
                    "RoadName": {
                        "Language": "en",
                        "Value": "Nanaimo St"
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
    -123.116655,
    49.281538
  ],
  "Destination": [
    -123.01791785749363,
    49.22782762759908
  ],
  "TravelMode": "Car",
  "Avoid": {
    "Areas": [
      {
        "Geometry": {
          "polygon": [
            [
              [
                -123.06953,
                49.256419
              ],
              [
                -123.080486,
                49.242115
              ],
              [
                -123.058573,
                49.242115
              ],
              [
                -123.06953,
                49.256419
              ]
            ]
          ]
        }
      }
    ]
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.13277 49.281538 \
--destination -123.01791785749363 49.22782762759908 \
--travel-mode "Car" \
--avoid '{"Areas":[{"Geometry":{"Polygon":[[[-123.06953,49.256419],[-123.05167,49.242115],[-123.02381,49.242115],[-123.06953,49.256419]]]}}]}'

```

Sample request

```
{
    "Origin": [
        -123.116655,
        49.281538
    ],
    "Destination": [
        -123.01791785749363,
        49.22782762759908
    ],
    "TravelMode": "Car",
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "PolylinePolygon": [
                        "BF0s0sJxglvXr5CvkCAgpEs5CvkC"
                    ]
                }
            }
        ]
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
                                    -123.0179179,
                                    49.2278276
                                ],
                                "Position": [
                                    -123.0229001,
                                    49.22883
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.116655,
                                    49.281538
                                ],
                                "Position": [
                                    -123.1166332,
                                    49.2815528
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
                                "Distance": 1144,
                                "Duration": 85,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "ExitNumber": [],
                                "GeometryOffset": 35,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 433,
                                "Duration": 47,
                                "ExitNumber": [],
                                "GeometryOffset": 40,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1131,
                                "Duration": 81,
                                "ExitNumber": [],
                                "GeometryOffset": 54,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 54,
                                "Duration": 4,
                                "ExitNumber": [],
                                "GeometryOffset": 79,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 520,
                                "Duration": 39,
                                "ExitNumber": [],
                                "GeometryOffset": 83,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 1123,
                                "Duration": 111,
                                "ExitNumber": [],
                                "GeometryOffset": 101,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1131,
                                "Duration": 81,
                                "ExitNumber": [],
                                "GeometryOffset": 141,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 448,
                                "Duration": 34,
                                "ExitNumber": [],
                                "GeometryOffset": 167,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 1797,
                                "Duration": 151,
                                "ExitNumber": [],
                                "GeometryOffset": 182,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 2836,
                                "Duration": 224,
                                "ExitNumber": [],
                                "GeometryOffset": 222,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 339,
                                "Duration": 30,
                                "ExitNumber": [],
                                "GeometryOffset": 326,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 64,
                                "Duration": 23,
                                "ExitNumber": [],
                                "GeometryOffset": 335,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 337,
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
                },
                {
                    "RoadName": {
                        "Language": "en",
                        "Value": "Nanaimo St"
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
    -123.116655,
    49.281538
  ],
  "Destination": [
    -123.01791785749363,
    49.22782762759908
  ],
  "TravelMode": "Car",
  "Avoid": {
    "Areas": [
      {
        "Geometry": {
          "PolylinePolygon": [
            "BF0s0sJxglvXr5CvkCAgpEs5CvkC"
          ]
        }
      }
    ]
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.13277 49.281538 \
--destination -123.01791785749363 49.22782762759908 \
--travel-mode "Car" \
--avoid '{"Areas":[{"Geometry":{"PolylinePolygon":["BF0s0sJxglvXr5CvkCAgpEs5CvkC"]}}]}'

```

Sample request

```
{
    "Origin": [
        -123.116655,
        49.281538
    ],
    "Destination": [
        -123.01791785749363,
        49.22782762759908
    ],
    "TravelMode": "Car",
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "PolylineCorridor": {
                        "Polyline": "Redacted",
                        "Radius": 10
                    }
                }
            }
        ]
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
                                    -123.0179179,
                                    49.2278276
                                ],
                                "Position": [
                                    -123.0229001,
                                    49.22883
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.116655,
                                    49.281538
                                ],
                                "Position": [
                                    -123.1166332,
                                    49.2815528
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
                                "Distance": 1144,
                                "Duration": 85,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "ExitNumber": [],
                                "GeometryOffset": 35,
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
                                "GeometryOffset": 40,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 2468,
                                "Duration": 204,
                                "ExitNumber": [],
                                "GeometryOffset": 90,
                                "KeepStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left"
                                },
                                "Type": "Keep"
                            },
                            {
                                "Distance": 1100,
                                "Duration": 88,
                                "ExitNumber": [],
                                "GeometryOffset": 170,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1588,
                                "Duration": 133,
                                "ExitNumber": [],
                                "GeometryOffset": 214,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 47,
                                "Duration": 14,
                                "ExitNumber": [],
                                "GeometryOffset": 260,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 2478,
                                "Duration": 196,
                                "ExitNumber": [],
                                "GeometryOffset": 265,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 339,
                                "Duration": 30,
                                "ExitNumber": [],
                                "GeometryOffset": 357,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 64,
                                "Duration": 23,
                                "ExitNumber": [],
                                "GeometryOffset": 366,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 368,
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
    -123.116655,
    49.281538
  ],
  "Destination": [
    -123.01791785749363,
    49.22782762759908
  ],
  "TravelMode": "Car",
  "Avoid": {
    "Areas": [
      {
        "Geometry": {
          "PolylineCorridor": {
            "Polyline": "Redacted",
            "Radius": 10
          }
        }
      }
    ]
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.116655 49.281538 \
--destination -123.01791785749363 49.22782762759908 \
--travel-mode "Car" \
--avoid '{"Areas": [{"Geometry": {"PolylineCorridor": {"Polyline": "BF2mysJnmkvX5ekiC", "Radius": 10}}}]}'

```

Sample request

```
{
    "Origin": [
        -123.116655,
        49.281538
    ],
    "Destination": [
        -123.01791785749363,
        49.22782762759908
    ],
    "TravelMode": "Car",
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "Corridor": {
                        "LineString": [
                            [
                                -123.06532243038754,
                                49.245226301868776
                            ],
                            [
                                -123.0547357660333,
                                49.24030469850804
                            ]
                        ],
                        "Radius": 10
                    }
                }
            }
        ]
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
                                    -123.0179179,
                                    49.2278276
                                ],
                                "Position": [
                                    -123.0229001,
                                    49.22883
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    -123.116655,
                                    49.281538
                                ],
                                "Position": [
                                    -123.1166332,
                                    49.2815528
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
                                "Distance": 1144,
                                "Duration": 85,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "ExitNumber": [],
                                "GeometryOffset": 35,
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
                                "GeometryOffset": 40,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 2468,
                                "Duration": 204,
                                "ExitNumber": [],
                                "GeometryOffset": 90,
                                "KeepStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left"
                                },
                                "Type": "Keep"
                            },
                            {
                                "Distance": 1100,
                                "Duration": 88,
                                "ExitNumber": [],
                                "GeometryOffset": 170,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1588,
                                "Duration": 133,
                                "ExitNumber": [],
                                "GeometryOffset": 214,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 47,
                                "Duration": 14,
                                "ExitNumber": [],
                                "GeometryOffset": 260,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 2478,
                                "Duration": 196,
                                "ExitNumber": [],
                                "GeometryOffset": 265,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 339,
                                "Duration": 30,
                                "ExitNumber": [],
                                "GeometryOffset": 357,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 64,
                                "Duration": 23,
                                "ExitNumber": [],
                                "GeometryOffset": 366,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 368,
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
    -123.116655,
    49.281538
  ],
  "Destination": [
    -123.01791785749363,
    49.22782762759908
  ],
  "TravelMode": "Car",
  "Avoid": {
    "Areas": [
      {
        "Geometry": {
          "Corridor": {
            "LineString": [
              [
                -123.06532243038754,
                49.245226301868776
              ],
              [
                -123.0547357660333,
                49.24030469850804
              ]
            ],
            "Radius": 10
          }
        }
      }
    ]
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.13277 49.281538 \
--destination -123.01791785749363 49.22782762759908 \
--travel-mode "Car" \
--avoid '{"Areas":[{"Geometry":{"Corridor":{"LineString":[[-123.06532243038754,49.245226301868776],[-123.0547357660333,49.24030469850804]],"Radius":10}}}]}'

```

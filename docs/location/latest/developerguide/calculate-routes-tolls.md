# How to calculate the tolls for a route

The CalculateRoutes API helps you to find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as car, truck, pedestrian and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination, with only a few constraints.

## Potential use cases

- **Calculate tolls:** Be able to calculate toll costs during route planning.
- **Audit tolls:** Be able to audit toll costs after traveling.

## Examples

Sample request

```
{
    "Origin": [
        2.234491,
        48.815704
    ],
    "Destination": [
        5.11412,
        47.260723
    ],
    "TravelMode": "Car",
    "Tolls": {
        "AllTransponders": true,
        "AllVignettes": true
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
                                    5.11412,
                                    47.2607229
                                ],
                                "Position": [
                                    5.1128203,
                                    47.2596356
                                ]
                            }
                        },
                        "Departure": {
                            "Place": {
                                "ChargingStation": false,
                                "OriginalPosition": [
                                    2.234491,
                                    48.8157039
                                ],
                                "Position": [
                                    2.2346482,
                                    48.815674
                                ]
                            }
                        },
                        "Incidents": [],
                        "Notices": [],
                        "PassThroughWaypoints": [],
                        "Spans": [],
                        "Tolls": [
                            {
                                "Country": "FRA",
                                "PaymentSites": [
                                    {
                                        "Name": "FLEURY-EN-BIERE",
                                        "Position": [
                                            2.53988,
                                            48.42578
                                        ]
                                    },
                                    {
                                        "Name": "POUILLY-EN-AUXOIS",
                                        "Position": [
                                            4.56112,
                                            47.25244
                                        ]
                                    }
                                ],
                                "Rates": [
                                    {
                                        "Id": "2d680295-fb0f-45aa-a8ed-79d9f0f9ff9f",
                                        "LocalPrice": {
                                            "Currency": "EUR",
                                            "Estimate": false,
                                            "Range": false,
                                            "Value": 21.700000762939453
                                        },
                                        "Name": "APRR",
                                        "PaymentMethods": [
                                            "Cash",
                                            "BankCard",
                                            "CreditCard",
                                            "Transponder",
                                            "TravelCard"
                                        ],
                                        "Transponders": [
                                            {
                                                "SystemName": "BipandGo"
                                            },
                                            {
                                                "SystemName": "BipandGo"
                                            },
                                            {
                                                "SystemName": "BipandGo IDVROOM carpoorling"
                                            },
                                            {
                                                "SystemName": "Cito30"
                                            },
                                            {
                                                "SystemName": "Easytrip pass"
                                            },
                                            {
                                                "SystemName": "Liane 30"
                                            },
                                            {
                                                "SystemName": "Liber-t"
                                            },
                                            {
                                                "SystemName": "Liber-t mobilitis"
                                            },
                                            {
                                                "SystemName": "Pass Pont-Pont"
                                            },
                                            {
                                                "SystemName": "Progressivi'T Maurienne"
                                            },
                                            {
                                                "SystemName": "TopEurop"
                                            },
                                            {
                                                "SystemName": "Tunnel Pass+"
                                            },
                                            {
                                                "SystemName": "Ulys"
                                            },
                                            {
                                                "SystemName": "Ulys Europe"
                                            },
                                            {
                                                "SystemName": "Viaduc-t 30"
                                            }
                                        ]
                                    }
                                ],
                                "Systems": [
                                    0
                                ]
                            }
                        ],
                        "TollSystems": [
                            {
                                "Name": "APRR"
                            }
                        ],
                        "TravelSteps": [
                            {
                                "Distance": 122,
                                "Duration": 21,
                                "ExitNumber": [],
                                "GeometryOffset": 0,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 32,
                                "Duration": 7,
                                "ExitNumber": [],
                                "GeometryOffset": 7,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 74,
                                "Duration": 14,
                                "ExitNumber": [],
                                "GeometryOffset": 8,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 199,
                                "Duration": 33,
                                "ExitNumber": [],
                                "GeometryOffset": 9,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 21,
                                "Duration": 10,
                                "ExitNumber": [],
                                "GeometryOffset": 17,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 461,
                                "Duration": 63,
                                "ExitNumber": [],
                                "GeometryOffset": 20,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1557,
                                "Duration": 145,
                                "ExitNumber": [],
                                "GeometryOffset": 41,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 3471,
                                "Duration": 151,
                                "ExitNumber": [],
                                "GeometryOffset": 135,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 9796,
                                "Duration": 430,
                                "ExitNumber": [],
                                "GeometryOffset": 242,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 2473,
                                "Duration": 112,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 582,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 674,
                                "Duration": 25,
                                "ExitNumber": [],
                                "GeometryOffset": 669,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 253953,
                                "Duration": 7468,
                                "ExitNumber": [],
                                "GeometryOffset": 679,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 37379,
                                "Duration": 1192,
                                "ExitNumber": [],
                                "ExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "GeometryOffset": 5701,
                                "Type": "Exit"
                            },
                            {
                                "Distance": 2021,
                                "Duration": 110,
                                "ExitNumber": [],
                                "GeometryOffset": 6695,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 7380,
                                "Duration": 316,
                                "ExitNumber": [],
                                "GeometryOffset": 6776,
                                "RoundaboutPassStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutPass"
                            },
                            {
                                "Distance": 4253,
                                "Duration": 156,
                                "ExitNumber": [],
                                "GeometryOffset": 6987,
                                "KeepStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left"
                                },
                                "Type": "Keep"
                            },
                            {
                                "Distance": 813,
                                "Duration": 54,
                                "ExitNumber": [],
                                "GeometryOffset": 7081,
                                "RampStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 1909,
                                "Duration": 109,
                                "ExitNumber": [],
                                "GeometryOffset": 7133,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Left",
                                    "TurnIntensity": "Sharp"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 827,
                                "Duration": 47,
                                "ExitNumber": [],
                                "GeometryOffset": 7182,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 680,
                                "Duration": 41,
                                "ExitNumber": [],
                                "GeometryOffset": 7216,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 224,
                                "Duration": 12,
                                "ExitNumber": [],
                                "GeometryOffset": 7258,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 25,
                                "Duration": 2,
                                "ExitNumber": [],
                                "GeometryOffset": 7265,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 748,
                                "Duration": 51,
                                "ExitNumber": [],
                                "GeometryOffset": 7267,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 656,
                                "Duration": 46,
                                "ExitNumber": [],
                                "GeometryOffset": 7299,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 1119,
                                "Duration": 78,
                                "ExitNumber": [],
                                "GeometryOffset": 7329,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 432,
                                "Duration": 26,
                                "ExitNumber": [],
                                "GeometryOffset": 7383,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 1864,
                                "Duration": 100,
                                "ExitNumber": [],
                                "GeometryOffset": 7402,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 1110,
                                "Duration": 93,
                                "ExitNumber": [],
                                "GeometryOffset": 7470,
                                "RoundaboutExitStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right"
                                },
                                "Type": "RoundaboutExit"
                            },
                            {
                                "Distance": 232,
                                "Duration": 10,
                                "ExitNumber": [],
                                "GeometryOffset": 7563,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 642,
                                "Duration": 29,
                                "ExitNumber": [],
                                "GeometryOffset": 7572,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 357,
                                "Duration": 25,
                                "ExitNumber": [],
                                "GeometryOffset": 7580,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 63,
                                "Duration": 10,
                                "ExitNumber": [],
                                "GeometryOffset": 7600,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 2626,
                                "Duration": 411,
                                "ExitNumber": [],
                                "GeometryOffset": 7602,
                                "TurnStepDetails": {
                                    "Intersection": [],
                                    "SteeringDirection": "Right",
                                    "TurnIntensity": "Typical"
                                },
                                "Type": "Turn"
                            },
                            {
                                "Distance": 234,
                                "Duration": 37,
                                "ExitNumber": [],
                                "GeometryOffset": 7627,
                                "Type": "Continue"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "ExitNumber": [],
                                "GeometryOffset": 7632,
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
                        "Language": "fr",
                        "Value": "A6"
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
    2.234491,
    48.815704
  ],
  "Destination": [
    5.11412,
    47.260723
  ],
  "TravelMode": "Car",
  "Tolls": {
    "AllTransponders": true,
    "AllVignettes": true
  }
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin 13.055211 52.704802 \
--destination 13.551910 52.282705 \
--travel-mode "Car" \
--tolls '{"AllTransponders": true, "AllVignettes": true}'
```

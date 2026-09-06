

# How to find an intermodal route
<a name="calculate-routes-intermodal-route"></a>

The CalculateRoutes API supports the `Intermodal` travel mode to calculate routes that combine multiple transport types in a single journey, such as driving to a park-and-ride location and then taking public transit to your destination. Pedestrian legs are always enabled to connect between other transport types.

## Potential use cases
<a name="intermodal-potential-use-cases"></a>
+ **Park and ride:** Drive to a transit station, park, and take public transit to avoid congestion and parking costs in city centers. Use `Vehicle` enabled for `FirstLeg` with `Taxi` and `Rental` disabled.
+ **Taxi and ride:** Take a taxi from your starting point to a well-connected transit station, then switch to public transit for the remainder of the journey. This is useful for areas not well connected by public transportation or when you want to avoid parking entirely. Use `Taxi` enabled for `FirstLeg` with `Vehicle` and `Rental` disabled.
+ **Last-mile transit:** Take public transit for the majority of the journey and use a taxi or rental for the last leg to reach the final destination.

## Examples
<a name="calculate-routes-intermodal-examples"></a>

### Calculate a park and ride intermodal route
<a name="calculate-routes-intermodal-park-and-ride"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -122.3088,
        47.4502
    ],
    "Destination": [
        -122.3331,
        47.6097
    ],
    "TravelMode": "Intermodal",
    "TravelModeOptions": {
        "Intermodal": {
            "Vehicle": {
                "EnabledFor": ["FirstLeg"]
            },
            "Taxi": {
                "EnabledFor": ["None"]
            },
            "Rental": {
                "EnabledFor": ["None"]
            }
        }
    },
    "DepartNow": true
}
```

------
#### [ Sample response ]

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
                        "AfterTravelSteps": [
                            {
                                "Duration": 300,
                                "Type": "Park"
                            }
                        ],
                        "Arrival": {
                            "Place": {
                                "Name": "Ipm Lot",
                                "Position": [
                                    -122.3264,
                                    47.58003
                                ],
                                "Type": "ParkingLot"
                            },
                            "Time": "2026-05-19T15:32:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Position": [
                                    -122.3088,
                                    47.4502
                                ]
                            },
                            "Time": "2026-05-19T15:12:00-07:00"
                        },
                        "Summary": {
                            "Overview": {
                                "Distance": 20493,
                                "Duration": 1500
                            },
                            "TravelOnly": {
                                "Duration": 1200
                            }
                        }
                    }
                },
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "PedestrianLegDetails": {
                        "Arrival": {
                            "Place": {
                                "Name": "Sodo Station Northeast Entrance",
                                "Position": [
                                    -122.327329,
                                    47.580637
                                ],
                                "Type": "AccessPoint"
                            },
                            "Time": "2026-05-19T15:39:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Name": "Ipm Lot",
                                "Position": [
                                    -122.3264,
                                    47.58003
                                ],
                                "Type": "ParkingLot"
                            },
                            "Time": "2026-05-19T15:37:00-07:00"
                        }
                    },
                    "TravelMode": "Pedestrian",
                    "Type": "Pedestrian"
                },
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "TravelMode": "LightRail",
                    "Type": "Transit",
                    "TransitLegDetails": {
                        "Agency": {
                            "Name": "Sound Transit",
                            "Url": "https://www.soundtransit.org"
                        },
                        "Arrival": {
                            "Place": {
                                "Name": "Symphony",
                                "Position": [
                                    -122.33602,
                                    47.60781
                                ],
                                "Type": "Station"
                            },
                            "Time": "2026-05-19T15:48:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Name": "Sodo",
                                "Position": [
                                    -122.32739,
                                    47.581074
                                ],
                                "Type": "Station"
                            },
                            "Time": "2026-05-19T15:40:00-07:00"
                        },
                        "Summary": {
                            "Overview": {
                                "Distance": 3174,
                                "Duration": 480
                            },
                            "TravelOnly": {
                                "Duration": 480
                            }
                        },
                        "Transport": {
                            "Color": "#28813F",
                            "Headsign": "Lynnwood City Center",
                            "Mode": "LightRail",
                            "RouteName": "1 Line",
                            "ShortRouteName": "1 Line",
                            "TextColor": "#FFFFFF"
                        }
                    }
                },
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "PedestrianLegDetails": {
                        "Arrival": {
                            "Place": {
                                "Position": [
                                    -122.3331,
                                    47.6097
                                ]
                            },
                            "Time": "2026-05-19T15:55:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Name": "Symphony Station Entrance A1",
                                "Position": [
                                    -122.335875,
                                    47.607929
                                ],
                                "Type": "AccessPoint"
                            },
                            "Time": "2026-05-19T15:49:00-07:00"
                        }
                    },
                    "TravelMode": "Pedestrian",
                    "Type": "Pedestrian"
                }
            ],
            "Summary": {
                "Distance": 24183,
                "Duration": 2280
            }
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://routes.geo.us-east-1.amazonaws.com/v2/routes?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
  "Origin": [
    -122.3088,
    47.4502
  ],
  "Destination": [
    -122.3331,
    47.6097
  ],
  "TravelMode": "Intermodal",
  "TravelModeOptions": {
    "Intermodal": {
      "Vehicle": {
        "EnabledFor": ["FirstLeg"]
      },
      "Taxi": {
        "EnabledFor": ["None"]
      },
      "Rental": {
        "EnabledFor": ["None"]
      }
    }
  },
  "DepartNow": true
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-routes \
--origin -122.3088 47.4502 \
--destination -122.3331 47.6097 \
--travel-mode "Intermodal" \
--travel-mode-options '{"Intermodal": {"Vehicle": {"EnabledFor": ["FirstLeg"]}, "Taxi": {"EnabledFor": ["None"]}, "Rental": {"EnabledFor": ["None"]}}}' \
--depart-now
```

------
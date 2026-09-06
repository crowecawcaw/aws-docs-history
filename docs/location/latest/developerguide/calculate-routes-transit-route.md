

# How to find a transit route
<a name="calculate-routes-transit-route"></a>

The CalculateRoutes API supports the `Transit` travel mode to calculate routes using public transportation such as buses, subways, trains, and monorails. Transit routes include pedestrian legs for walking to and from transit stops.

## Potential use cases
<a name="transit-potential-use-cases"></a>
+ **Plan public transit journeys:** Find the best public transit route between two locations, including walking directions to and from stops.
+ **Filter transit modes:** Use `AllowedModes` to restrict routes to specific transit types (for example, only subways and buses), or use `ExcludedModes` to remove unwanted modes (for example, exclude ferries).

## Examples
<a name="calculate-routes-transit-examples"></a>

### Calculate a route using public transit
<a name="calculate-routes-transit-mode"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -122.3331,
        47.6097
    ],
    "Destination": [
        -122.3493,
        47.6205
    ],
    "TravelMode": "Transit",
    "DepartNow": true
}
```

------
#### [ Sample response ]

```
{
    "PricingBucket": "Core",
    "LegGeometryFormat": "FlexiblePolyline",
    "Notices": [],
    "Routes": [
        {
            "Legs": [
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "PedestrianLegDetails": {
                        "Arrival": {
                            "Place": {
                                "Name": "Westlake Center",
                                "Position": [
                                    -122.33696,
                                    47.612046
                                ]
                            },
                            "Time": "2026-05-15T12:55:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Position": [
                                    -122.3331,
                                    47.6097
                                ]
                            },
                            "Time": "2026-05-15T12:47:00-07:00"
                        },
                        "PassThroughWaypoints": [],
                        "Spans": [],
                        "TravelSteps": [
                            {
                                "Distance": 61,
                                "Duration": 70,
                                "GeometryOffset": 0,
                                "Instruction": "Head northwest on 6th Ave. Go for 61 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 96,
                                "Duration": 106,
                                "GeometryOffset": 3,
                                "Instruction": "Turn left onto Union St. Go for 96 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 315,
                                "Duration": 315,
                                "GeometryOffset": 5,
                                "Instruction": "Turn right onto 5th Ave. Go for 315 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "GeometryOffset": 10,
                                "Instruction": "Arrive at 5th Ave. Your destination is on the left.",
                                "Type": "Depart"
                            }
                        ]
                    },
                    "TravelMode": "Pedestrian",
                    "Type": "Pedestrian"
                },
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "TravelMode": "Monorail",
                    "Type": "Transit"
                },
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "PedestrianLegDetails": {
                        "Arrival": {
                            "Place": {
                                "Position": [
                                    -122.3493,
                                    47.6205
                                ]
                            },
                            "Time": "2026-05-15T13:00:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Name": "Seattle Center",
                                "Position": [
                                    -122.349955,
                                    47.621263
                                ]
                            },
                            "Time": "2026-05-15T12:58:00-07:00"
                        },
                        "PassThroughWaypoints": [],
                        "Spans": [],
                        "TravelSteps": [
                            {
                                "Distance": 37,
                                "Duration": 37,
                                "GeometryOffset": 0,
                                "Instruction": "Head south. Go for 37 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 33,
                                "Duration": 33,
                                "GeometryOffset": 1,
                                "Instruction": "Turn left onto Lenny Wilkens Way. Go for 33 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 49,
                                "Duration": 49,
                                "GeometryOffset": 2,
                                "Instruction": "Turn right. Go for 49 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 0,
                                "Duration": 0,
                                "GeometryOffset": 6,
                                "Instruction": "Arrive at your destination on the left.",
                                "Type": "Depart"
                            }
                        ]
                    },
                    "TravelMode": "Pedestrian",
                    "Type": "Pedestrian"
                }
            ],
            "Summary": {
                "Distance": 0,
                "Duration": 0
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
    -122.3331,
    47.6097
  ],
  "Destination": [
    -122.3493,
    47.6205
  ],
  "TravelMode": "Transit",
  "DepartNow": true
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-routes \
--origin -122.3331 47.6097 \
--destination -122.3493 47.6205 \
--travel-mode "Transit" \
--depart-now
```

------

### Calculate a route using public transit excluding certain transport modes
<a name="calculate-routes-transit-excluded-modes"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -122.3331,
        47.6097
    ],
    "Destination": [
        -122.3493,
        47.6205
    ],
    "TravelMode": "Transit",
    "TravelModeOptions": {
        "Transit": {
            "ExcludedModes": ["Monorail"]
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
                    "PedestrianLegDetails": {
                        "Arrival": {
                            "Place": {
                                "Name": "3rd Ave & Pike St",
                                "Position": [
                                    -122.337585,
                                    47.609642
                                ]
                            },
                            "Time": "2026-05-15T12:58:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Position": [
                                    -122.3331,
                                    47.6097
                                ]
                            },
                            "Time": "2026-05-15T12:50:00-07:00"
                        },
                        "TravelSteps": [
                            {
                                "Distance": 61,
                                "Duration": 70,
                                "Instruction": "Head northwest on 6th Ave. Go for 61 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 294,
                                "Duration": 304,
                                "Instruction": "Turn left onto Union St. Go for 294 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 112,
                                "Duration": 112,
                                "Instruction": "Turn right onto 3rd Ave. Go for 112 m.",
                                "Type": "Depart"
                            }
                        ]
                    },
                    "TravelMode": "Pedestrian",
                    "Type": "Pedestrian"
                },
                {
                    "Geometry": {
                        "Polyline": "Redacted"
                    },
                    "TravelMode": "Bus",
                    "Type": "Transit",
                    "TransitLegDetails": {
                        "Agency": {
                            "Name": "Metro Transit"
                        },
                        "Arrival": {
                            "Place": {
                                "Name": "7th Ave N & Denny Way",
                                "Position": [
                                    -122.343445,
                                    47.619087
                                ]
                            },
                            "Time": "2026-05-15T13:00:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Name": "3rd Ave & Pike St",
                                "Position": [
                                    -122.337585,
                                    47.609642
                                ]
                            },
                            "Time": "2026-05-15T12:58:00-07:00"
                        },
                        "Transport": {
                            "Color": "#9C182F",
                            "Headsign": "Aurora Village Transit Center",
                            "Mode": "Bus",
                            "RouteName": "E Line",
                            "ShortRouteName": "E Line",
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
                                    -122.3493,
                                    47.6205
                                ]
                            },
                            "Time": "2026-05-15T13:10:00-07:00"
                        },
                        "Departure": {
                            "Place": {
                                "Name": "7th Ave N & Denny Way",
                                "Position": [
                                    -122.343445,
                                    47.619087
                                ]
                            },
                            "Time": "2026-05-15T13:00:00-07:00"
                        },
                        "TravelSteps": [
                            {
                                "Distance": 71,
                                "Duration": 80,
                                "Instruction": "Head north on 7th Ave N. Go for 71 m.",
                                "Type": "Depart"
                            },
                            {
                                "Distance": 436,
                                "Duration": 440,
                                "Instruction": "Turn left onto John St. Go for 436 m.",
                                "Type": "Depart"
                            }
                        ]
                    },
                    "TravelMode": "Pedestrian",
                    "Type": "Pedestrian"
                }
            ],
            "Summary": {
                "Distance": 0,
                "Duration": 0
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
    -122.3331,
    47.6097
  ],
  "Destination": [
    -122.3493,
    47.6205
  ],
  "TravelMode": "Transit",
  "TravelModeOptions": {
    "Transit": {
      "ExcludedModes": ["Monorail"]
    }
  },
  "DepartNow": true
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-routes \
--origin -122.3331 47.6097 \
--destination -122.3493 47.6205 \
--travel-mode "Transit" \
--travel-mode-options '{"Transit": {"ExcludedModes": ["Monorail"]}}' \
--depart-now
```

------
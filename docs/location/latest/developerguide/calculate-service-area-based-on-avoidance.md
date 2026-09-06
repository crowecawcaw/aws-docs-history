

# How to calculate a service area based on avoidance
<a name="calculate-service-area-based-on-avoidance"></a>

The CalculateIsolines API allows you to determine reachable service areas within specified ranges of time or distance, factoring in road networks and traffic conditions to avoid. This capability supports applications in defining service areas for restaurants, grocery stores, or other service providers which can assist in planning fuel efficiency and defining accessible areas for service coverage.

## Potential use cases
<a name="calculate-service-area-avoidance-potential-use"></a>
+ **Plan service areas:** Use this API to plan accessible areas for services like restaurants or grocery delivery based on avoidance.

## Examples
<a name="calculate-service-area-avoidance-examples"></a>

### Calculate a service area based on avoidance with Car TravelMode
<a name="calculate-service-area-avoidance-car"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -123.11679620827039,
        49.28147612192166
    ],
    "DepartureTime": "2024-10-28T21:27:56Z",
    "Thresholds": {
        "Distance": [
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "UTurns": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Car"
}
```

------
#### [ Sample response ]

```
{
    "DepartureTime": "2024-10-28T14:27:56-07:00",
    "IsolineGeometryFormat": "FlexiblePolyline",
    "Isolines": [
        {
            "Connections": [],
            "DistanceThreshold": 4000,
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

------
#### [ cURL ]

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
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "UTurns": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Car"
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-isolines --key ${YourKey} \
--origin -123.11679620827039 49.28147612192166 \
--departure-time "2024-10-28T21:27:56Z" \
--thresholds '{"Distance": [4000]}' \
--avoid '{"TollRoads": true, "UTurns": true, "ControlledAccessHighways": true, "Ferries": true, "DirtRoads": true, "SeasonalClosure": true, "CarShuttleTrains": true, "TollTransponders": true, "ZoneCategories": [{"Category": "Environmental"}]}' \
--travel-mode "Car"
```

------

### Calculate a service area based on avoidance with Truck TravelMode
<a name="calculate-service-area-avoidance-truck"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -123.11679620827039,
        49.28147612192166
    ],
    "DepartureTime": "2024-10-28T21:27:56Z",
    "Thresholds": {
        "Distance": [
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "UTurns": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Truck"
}
```

------
#### [ Sample response ]

```
{
    "DepartureTime": "2024-10-28T14:27:56-07:00",
    "IsolineGeometryFormat": "FlexiblePolyline",
    "Isolines": [
        {
            "Connections": [],
            "DistanceThreshold": 4000,
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

------
#### [ cURL ]

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
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "UTurns": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Truck"
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-isolines --key ${YourKey} \
--origin -123.11679620827039 49.28147612192166 \
--departure-time "2024-10-28T21:27:56Z" \
--thresholds '{"Distance": [4000]}' \
--avoid '{"TollRoads": true, "UTurns": true, "ControlledAccessHighways": true, "Ferries": true, "DirtRoads": true, "SeasonalClosure": true, "CarShuttleTrains": true, "TollTransponders": true, "ZoneCategories": [{"Category": "Environmental"}]}' \
--travel-mode "Truck"
```

------

### Calculate a service area based on avoidance for pedestrians
<a name="calculate-service-area-avoidance-truck"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -123.11679620827039,
        49.28147612192166
    ],
    "DepartureTime": "2024-10-28T21:27:56Z",
    "Thresholds": {
        "Distance": [
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Pedestrian"
}
```

------
#### [ Sample response ]

```
{
    "DepartureTime": "2024-10-28T14:27:56-07:00",
    "IsolineGeometryFormat": "FlexiblePolyline",
    "Isolines": [
        {
            "Connections": [],
            "DistanceThreshold": 4000,
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

------
#### [ cURL ]

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
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Pedestrian"
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-isolines --key ${YourKey} \
--origin -123.11679620827039 49.28147612192166 \
--departure-time "2024-10-28T21:27:56Z" \
--thresholds '{"Distance": [4000]}' \
--avoid '{"TollRoads": true, "ControlledAccessHighways": true, "Ferries": true, "DirtRoads": true, "SeasonalClosure": true, "CarShuttleTrains": true, "TollTransponders": true, "ZoneCategories": [{"Category": "Environmental"}]}' \
--travel-mode "Pedestrian"
```

------

### Calculate a service area based on avoidance with Scooter TravelMode
<a name="calculate-service-area-avoidance-scooter"></a>

------
#### [ Sample request ]

```
{
    "Origin": [
        -123.11679620827039,
        49.28147612192166
    ],
    "DepartureTime": "2024-10-28T21:27:56Z",
    "Thresholds": {
        "Distance": [
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "ControlledAccessHighways": true,
        "DifficultTurns": false,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Scooter"
}
```

------
#### [ Sample response ]

```
{
    "DepartureTime": "2024-10-28T14:27:56-07:00",
    "IsolineGeometryFormat": "FlexiblePolyline",
    "Isolines": [
        {
            "Connections": [],
            "DistanceThreshold": 4000,
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

------
#### [ cURL ]

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
            4000
        ]
    },
    "Avoid": {
        "TollRoads": true,
        "ControlledAccessHighways": true,
        "Ferries": true,
        "DirtRoads": true,
        "SeasonalClosure": true,
        "CarShuttleTrains": true,
        "TollTransponders": true,
        "ZoneCategories": [
            {
                "Category": "Environmental"
            }
        ]
    },
    "TravelMode": "Scooter"
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-isolines --key ${YourKey} \
--origin -123.11679620827039 49.28147612192166 \
--departure-time "2024-10-28T21:27:56Z" \
--thresholds '{"Distance": [4000]}' \
--avoid '{"TollRoads": true, "ControlledAccessHighways": true, "Ferries": true, "DirtRoads": true, "SeasonalClosure": true, "CarShuttleTrains": true, "TollTransponders": true, "ZoneCategories": [{"Category": "Environmental"}]}' \
--travel-mode "Scooter"
```

------
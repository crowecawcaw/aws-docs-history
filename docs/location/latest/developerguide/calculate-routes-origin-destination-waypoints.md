# How to find a route for an origin and destination

The CalculateRoutes API helps you find the best routes between origin and destination, as well as the best opportunities for driver resting. It supports travel modes such as truck, pedestrian, car and scooter. It also supports up to 25 waypoints (stopovers) including the origin and destination with only a few constraints.

## Potential use cases

- **Find point-to-point routes:** Determine the best route between two locations based on various travel modes and additional options.

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
    ]
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
                        "TravelSteps": [
                            {
                                "Distance": 1288,
                                "Duration": 102,
                                "Type": "Depart"
                            },
                            {
                                "Distance": 262,
                                "Duration": 24,
                                "Type": "Ramp"
                            },
                            {
                                "Distance": 1356,
                                "Duration": 134,
                                "Type": "Turn"
                            },
                            {
                                "Distance": 7092,
                                "Duration": 568,
                                "Type": "Keep"
                            },
                            {
                                "Distance": 65,
                                "Duration": 26,
                                "Type": "Turn"
                            },
                            {
                                "Distance": 50,
                                "Duration": 18,
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
  ]
}'
```

AWS CLI

```
aws geo-routes calculate-routes --key ${YourKey} \
--origin -123.118105 49.282423 \
--destination -123.020098 49.232872
```

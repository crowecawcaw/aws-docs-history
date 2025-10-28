# How to calculate a route matrix of distance and time for multiple origins and destinations

The CalculateRouteMatrix API calculates routes and provides travel time and travel distance for each combination of origins and destinations. This capability is useful for applications requiring route planning and optimization across multiple locations.

## Potential use cases

- **Optimize route planning:** Use the route matrix as input for route optimization software to enhance service efficiency and reduce travel time.

## Examples

Sample request

```
{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        },
        {
            "Position": [-123.11179620827039, 49.3014761219]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "DepartureTime": "2024-05-28T21:27:56Z",
    "RoutingBoundary": {
        "Unbounded": true
    }
}
```

Sample response

```
{
    "ErrorCount": 0,
    "RouteMatrix": [
        [
            {
                "Distance": 1907,
                "Duration": 343
            }
        ],
        [
            {
                "Distance": 5629,
                "Duration": 954
            }
        ]
    ],
    "RoutingBoundary": {
        "Unbounded": true
    }
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/route-matrix?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        },
        {
            "Position": [-123.11179620827039, 49.3014761219]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "DepartureTime": "2024-05-28T21:27:56Z",
    "RoutingBoundary": {
        "Unbounded": true
    }
}'
```

AWS CLI

```
aws geo-routes calculate-route-matrix --key ${YourKey} \
--origins '[{"Position": [-123.11679620827039, 49.28147612192166]}, {"Position": [-123.11179620827039, 49.3014761219]}]' \
--destinations '[{"Position": [-123.11179620827039, 49.28897192166]}]' \
--departure-time "2024-05-28T21:27:56Z" \
--routing-boundary '{"Unbounded": true}'
```

Sample request

```
{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        },
        {
            "Position": [-123.11179620827039, 49.3014761219]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "DepartureTime": "2024-05-28T21:27:56Z",
    "RoutingBoundary": {
        "Geometry": {
            "AutoCircle": {
                "Margin": 10000,
                "MaxRadius": 30000
            }
        }
    }
}
```

Sample response

```
{
    "ErrorCount": 0,
    "RouteMatrix": [
        [
            {
                "Distance": 1907,
                "Duration": 344
            }
        ],
        [
            {
                "Distance": 5629,
                "Duration": 950
            }
        ]
    ],
    "RoutingBoundary": {
        "Geometry": {
            "Circle": {
                "Center": [
                    -123.1142962082704,
                    49.29147612191083
                ],
                "Radius": 11127
            }
        },
        "Unbounded": false
    }
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/route-matrix?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        },
        {
            "Position": [-123.11179620827039, 49.3014761219]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "DepartureTime": "2024-05-28T21:27:56Z",
    "RoutingBoundary": {
        "Geometry": {
            "AutoCircle": {
                "Margin": 10000,
                "MaxRadius": 30000
            }
        }
    }
}'
```

AWS CLI

```
aws geo-routes calculate-route-matrix --key ${YourKey} \
--origins '[{"Position": [-123.11679620827039, 49.28147612192166]}, {"Position": [-123.11179620827039, 49.3014761219]}]' \
--destinations '[{"Position": [-123.11179620827039, 49.28897192166]}]' \
--departure-time "2024-05-28T21:27:56Z" \
--routing-boundary '{"Geometry": {"AutoCircle": {"Margin": 10000, "MaxRadius": 30000}}}'
```

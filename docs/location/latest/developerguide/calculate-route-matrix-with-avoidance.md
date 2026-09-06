

# How to calculate route matrix with avoidance
<a name="calculate-route-matrix-with-avoidance"></a>

The CalculateRouteMatrix API computes routes and returns travel time and distance from each origin to each destination in the specified lists. The response includes `Distance` in meters and `Duration` in seconds. The API can be used to set avoidance options for specific areas or road features, ensuring routes avoid specified zones or conditions. If an alternative route is not feasible, the avoidance preference may be bypassed.

## Potential use cases
<a name="calculate-route-matrix-potential-use"></a>
+ **Route planning and optimization:** Use route matrix as input for software that requires optimized travel routes while avoiding certain areas or road features.

## Examples
<a name="calculate-route-matrix-examples"></a>

### CalculateRouteMatrix with an avoidance area
<a name="calculate-route-matrix-avoidance-area"></a>

------
#### [ Sample request ]

```
{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "BoundingBox": [
                         -123.116561,
                         49.281517,
                         -123.110165,
                         49.285689
                    ]
                }
            }
        ]
    },
    "RoutingBoundary": {
        "Unbounded": true
    }
}
```

------
#### [ Sample response ]

```
{
    "ErrorCount": 0,
    "RouteMatrix": [
        [
            {
                "Distance": 1855,
                "Duration": 295
            }
        ]
    ],
    "RoutingBoundary": {
        "Unbounded": true
    }
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/route-matrix?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "Avoid": {
        "Areas": [
            {
                "Geometry": {
                    "BoundingBox": [
                         -123.116561,
                         49.281517,
                         -123.110165,
                         49.285689
                    ]
                }
            }
        ]
    },
    "RoutingBoundary": {
        "Unbounded": true
    }
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-route-matrix --key ${YourKey} \
--origins '[{"Position": [-123.11679620827039, 49.28147612192166]}]' \
--destinations '[{"Position": [-123.112317039, 49.28897192166]}]' \
--avoid '{"Areas": [{"Geometry": {"BoundingBox": [-123.116561, 49.281517, -123.110165, 49.285689]}}]}' \
--routing-boundary '{"Unbounded": true}'
```

------

### CalculateRouteMatrix avoiding toll roads, highways, and ferries
<a name="calculate-route-matrix-avoidance-features"></a>

------
#### [ Sample request ]

```
{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "Avoid": {
        "TollRoads": true,
        "ControlledAccessHighways": true,
        "Ferries": true    
    },
    "RoutingBoundary": {
        "Unbounded": true
    }
}
```

------
#### [ Sample response ]

```
{
    "ErrorCount": 0,
    "RouteMatrix": [
        [
            {
                "Distance": 1855,
                "Duration": 295
            }
        ]
    ],
    "RoutingBoundary": {
        "Unbounded": true
    }
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/route-matrix?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origins": [
        {
            "Position": [-123.11679620827039, 49.28147612192166]
        }
    ],
    "Destinations": [
        {
            "Position": [-123.112317039, 49.28897192166]
        }
    ],
    "Avoid": {
        "TollRoads": true,
        "ControlledAccessHighways": true,
        "Ferries": true    
    },
    "RoutingBoundary": {
        "Unbounded": true
    }
}'
```

------
#### [ AWS CLI ]

```
aws geo-routes calculate-route-matrix --key ${YourKey} \
--origins '[{"Position": [-123.11679620827039, 49.28147612192166]}]' \
--destinations '[{"Position": [-123.112317039, 49.28897192166]}]' \
--avoid '{"TollRoads": true, "ControlledAccessHighways": true, "Ferries": true}' \
--routing-boundary '{"Unbounded": true}'
```

------
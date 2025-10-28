# How to optimize waypoints for a route

The OptimizeWaypoints API calculates the most efficient route between a series of waypoints, minimizing either travel time or total distance. This API solves the Traveling Salesman Problem by considering road networks and traffic conditions to determine the optimal path.

## Potential use cases

- **Analyze service area patterns:** Use waypoint optimization to make informed decisions about business service areas and improve logistics efficiency.

## Examples

Sample Request

```
{
    "Origin": [
        -123.095740,
        49.274426
    ],
    "Waypoints": [
        {
            "Position": [
                -123.115193,
                49.280596
            ]
        },
        {
            "Position": [
                -123.089557,
                49.271774
            ]
        }
    ],
    "DepartureTime": "2024-10-25T18:13:42Z",
    "Destination": [
        -123.095185,
        49.263728
    ],
    "TravelMode": "Car"
}
```

Sample Response

```
{
    "Connections": [
        {
            "Distance": 1989,
            "From": "Origin",
            "RestDuration": 0,
            "To": "Waypoint0",
            "TravelDuration": 258,
            "WaitDuration": 0
        },
        {
            "Distance": 3010,
            "From": "Waypoint0",
            "RestDuration": 0,
            "To": "Waypoint1",
            "TravelDuration": 298,
            "WaitDuration": 0
        },
        {
            "Distance": 2371,
            "From": "Waypoint1",
            "RestDuration": 0,
            "To": "Destination",
            "TravelDuration": 311,
            "WaitDuration": 0
        }
    ],
    "Distance": 7370,
    "Duration": 867,
    "ImpedingWaypoints": [],
    "OptimizedWaypoints": [
        {
            "DepartureTime": "2024-10-25T18:13:42Z",
            "Id": "Origin",
            "Position": [
                -123.09574,
                49.274426
            ]
        },
        {
            "DepartureTime": "2024-10-25T18:18:00Z",
            "Id": "Waypoint0",
            "Position": [
                -123.115193,
                49.280596
            ]
        },
        {
            "DepartureTime": "2024-10-25T18:22:58Z",
            "Id": "Waypoint1",
            "Position": [
                -123.089557,
                49.271774
            ]
        },
        {
            "ArrivalTime": "2024-10-25T18:28:09Z",
            "Id": "Destination",
            "Position": [
                -123.095185,
                49.263728
            ]
        }
    ],
    "TimeBreakdown": {
        "RestDuration": 0,
        "ServiceDuration": 0,
        "TravelDuration": 867,
        "WaitDuration": 0
    }
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/optimize-waypoints?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
    "Origin": [
        -123.095740,
        49.274426
    ],
    "Waypoints": [
        {
            "Position": [
                -123.115193,
                49.280596
            ]
        },
        {
            "Position": [
                -123.089557,
                49.271774
            ]
        }
    ],
    "DepartureTime": "2024-10-25T18:13:42Z",
    "Destination": [
        -123.095185,
        49.263728
    ],
    "TravelMode": "Car"
}'
```

AWS CLI

```
aws geo-routes optimize-waypoints --key ${YourKey} \
--origin -123.095740 49.274426 \
--waypoints '[{"Position": [-123.115193 , 49.280596]}, {"Position": [-123.089557 , 49.271774]}]' \
--destination -123.095185 49.263728 \
--departure-time "2024-10-25T18:13:42Z" \
--travel-mode "Car"
```

# How to optimize waypoints for a route with traffic awareness

The OptimizeWaypoints API calculates the optimal route between multiple waypoints to minimize travel time or total distance. It utilizes advanced algorithms to solve the Traveling Salesman Problem, determining the most efficient path while accounting for factors such as road networks and real-time traffic conditions.

## Potential use cases

- **Optimize multi-stop routes for delivery efficiency:** Improve delivery operations by calculating the shortest or fastest route among several stops. This is useful for reducing operational costs, fuel consumption, and travel time in logistics and delivery services.

## Examples

Sample request

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
    "TravelMode": "Car",
    "Traffic": {
        "Usage": "UseTrafficData"
    }
}
```

Sample response

```
{
    "Connections": [
        {
            "Distance": 1989,
            "From": "Origin",
            "RestDuration": 0,
            "To": "Waypoint0",
            "TravelDuration": 324,
            "WaitDuration": 0
        },
        {
            "Distance": 2692,
            "From": "Waypoint0",
            "RestDuration": 0,
            "To": "Waypoint1",
            "TravelDuration": 338,
            "WaitDuration": 0
        },
        {
            "Distance": 2371,
            "From": "Waypoint1",
            "RestDuration": 0,
            "To": "Destination",
            "TravelDuration": 395,
            "WaitDuration": 0
        }
    ],
    "Distance": 7052,
    "Duration": 1057,
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
            "ArrivalTime": "2024-10-25T18:19:06Z",
            "DepartureTime": "2024-10-25T18:19:06Z",
            "Id": "Waypoint0",
            "Position": [
                -123.115193,
                49.280596
            ]
        },
        {
            "ArrivalTime": "2024-10-25T18:24:44Z",
            "DepartureTime": "2024-10-25T18:24:44Z",
            "Id": "Waypoint1",
            "Position": [
                -123.089557,
                49.271774
            ]
        },
        {
            "ArrivalTime": "2024-10-25T18:31:19Z",
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
        "TravelDuration": 1057,
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
    "TravelMode": "Car",
    "Traffic": {
        "Usage": "UseTrafficData"
    }
}'
```

AWS CLI

```
aws geo-routes optimize-waypoints --key ${YourKey} \
--origin -123.095740 49.274426 \
--waypoints '[{"Position": [-123.115193 , 49.280596]}, {"Position": [-123.089557 , 49.271774]}]' \
--destination -123.095185 49.263728 \
--departure-time "2024-10-25T18:13:42Z" \
--travel-mode "Car" \
--traffic '{"Usage": "UseTrafficData"}'
```

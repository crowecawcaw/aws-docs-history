# How to optimize waypoints for a route with access hours awareness

The OptimizeWaypoints API also calculates the optimal route between a set of waypoints, with the goal of minimizing either the travel time or the total distance covered. It solves the Traveling Salesman Problem of determining the most efficient path, taking into account factors such as the road network and traffic conditions.

## Potential use cases

- **Analyze customer access hours:** Plan for efficiency around your customer’s access hours.

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
            ],
            "SideOfStreet": {
                "Position": [
                    -123.089557,
                    49.271774
                ],
                "UseWith": "AnyStreet"
            },
            "AccessHours": {
                "From": {
                    "DayOfWeek": "Saturday",
                    "TimeOfDay": "00:02:42Z"
                },
                "To": {
                    "DayOfWeek": "Friday",
                    "TimeOfDay": "1:33:36+02:50"
                }
            },
            "Heading": "250",
            "ServiceDuration": "200"
        },
        {
            "Position": [
                -123.089557,
                49.271774
            ],
            "AccessHours": {
                "From": {
                    "DayOfWeek": "Monday",
                    "TimeOfDay": "00:02:42Z"
                },
                "To": {
                    "DayOfWeek": "Tuesday",
                    "TimeOfDay": "1:33:36+02:50"
                }
            },
            "ServiceDuration": "200"
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
            "WaitDuration": 20682
        },
        {
            "Distance": 3360,
            "From": "Waypoint0",
            "RestDuration": 0,
            "To": "Waypoint1",
            "TravelDuration": 378,
            "WaitDuration": 172222
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
    "Distance": 7720,
    "Duration": 194251,
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
            "ArrivalTime": "2024-10-25T18:18:00Z",
            "DepartureTime": "2024-10-26T00:06:02Z",
            "Id": "Waypoint0",
            "Position": [
                -123.115193,
                49.280596
            ]
        },
        {
            "ArrivalTime": "2024-10-26T00:12:20Z",
            "DepartureTime": "2024-10-28T00:06:02Z",
            "Id": "Waypoint1",
            "Position": [
                -123.089557,
                49.271774
            ]
        },
        {
            "ArrivalTime": "2024-10-28T00:11:13Z",
            "Id": "Destination",
            "Position": [
                -123.095185,
                49.263728
            ]
        }
    ],
    "TimeBreakdown": {
        "RestDuration": 0,
        "ServiceDuration": 400,
        "TravelDuration": 947,
        "WaitDuration": 192904
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
            ],
            "SideOfStreet": {
                "Position": [
                    -123.089557,
                    49.271774
                ],
                "UseWith": "AnyStreet"
            },
            "AccessHours": {
                "From": {
                    "DayOfWeek": "Saturday",
                    "TimeOfDay": "00:02:42Z"
                },
                "To": {
                    "DayOfWeek": "Friday",
                    "TimeOfDay": "1:33:36+02:50"
                }
            },
            "Heading": "250",
            "ServiceDuration": "200"
        },
        {
            "Position": [
                -123.089557,
                49.271774
            ],
            "AccessHours": {
                "From": {
                    "DayOfWeek": "Monday",
                    "TimeOfDay": "00:02:42Z"
                },
                "To": {
                    "DayOfWeek": "Tuesday",
                    "TimeOfDay": "1:33:36+02:50"
                }
            },
            "ServiceDuration": "200"
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
--waypoints '[{"Position": [-123.115193 , 49.280596], "SideOfStreet": {"Position": [-123.089557, 49.271774], "UseWith": "AnyStreet"}, "AccessHours": {"From": {"DayOfWeek": "Saturday", "TimeOfDay": "00:02:42Z"}, "To": {"DayOfWeek": "Friday", "TimeOfDay": "1:33:36+02:50"}}, "Heading": 250, "ServiceDuration": 200}, {"Position": [-123.089557, 49.271774], "AccessHours": {"From": {"DayOfWeek": "Monday", "TimeOfDay": "00:02:42Z"}, "To": {"DayOfWeek": "Tuesday", "TimeOfDay": "1:33:36+02:50"}}, "ServiceDuration": 200}]' \
--destination -123.095185 49.263728 \
--departure-time "2024-10-25T18:13:42Z" \
--travel-mode "Car"
```

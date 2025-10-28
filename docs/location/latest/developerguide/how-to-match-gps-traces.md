# How to match GPS traces to a road network

The SnapToRoads API allows you to match GPS traces onto the road network. A GPS trace includes positions and metadata like timestamp, speed, and heading that are recorded using a GPS device. These traces often have a margin of error, making them challenging to use for analysis and visualization directly.

SnapToRoads considers legal and time restrictions for the specified travel mode while matching traces. If the trace strongly suggests a restriction violation, the actual route taken is maintained.

## Potential use cases

- **Overlay GPS traces onto the most likely driven roads:** This feature helps align GPS data to the most accurate path on the road network, supporting clearer data visualization.
- **Interpolate gaps in GPS traces:** SnapToRoads can fill in gaps by snapping coordinates to road segments, creating a more continuous and useful dataset for applications.
- **Filter noise and outliers:** By snapping to the nearest road, this API can help remove outliers and reduce GPS noise, improving data reliability for analysis.

## Examples

Sample request

```
{
  "TracePoints": [
    {
      "Position": [8.53404,50.16364],
      "Timestamp": "2024-05-22T18:13:42Z"
    },
    {
      "Position": [8.53379056,50.16352417],
      "Speed": 20,
      "Timestamp": "2024-05-22T18:13:59Z"
    }
  ],
  "TravelMode": "Car"
}
```

Sample response

```
{
    "Notices": [],
    "SnappedGeometry": {
        "Polyline": "Redacted"
    },
    "SnappedGeometryFormat": "FlexiblePolyline",
    "SnappedTracePoints": [
        {
            "Confidence": 1,
            "OriginalPosition": [8.53404, 50.16364],
            "SnappedPosition": [8.53402, 50.16367]
        },
        {
            "Confidence": 0.86,
            "OriginalPosition": [8.53379056, 50.16352417],
            "SnappedPosition": [8.53375, 50.16356]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/snap-to-roads?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
  "TracePoints": [
    {
      "Position": [8.53404,50.16364],
      "Timestamp": "2024-05-22T18:13:42Z"
    },
    {
      "Position": [8.53379056,50.16352417],
      "Speed": 20,
      "Timestamp": "2024-05-22T18:13:59Z"
    }
  ],
  "TravelMode": "Car"
}'
```

AWS CLI

```
aws geo-routes snap-to-roads --key ${YourKey} \
--trace-points '[{"Position": [8.53404, 50.16364], "Timestamp": "2024-05-22T18:13:42Z"}, {"Position": [8.53379056, 50.16352417], "Speed": 20, "Timestamp": "2024-05-22T18:13:59Z"}]' \
--travel-mode "Car"
```

Sample request

```
{
  "TracePoints": [
    {
      "Position": [8.53404,50.16364],
      "Timestamp": "2024-05-22T18:13:42Z"
    },
    {
      "Position": [8.53379056,50.16352417],
      "Speed": 20,
      "Timestamp": "2024-05-22T18:13:59Z"
    }
  ],
  "TravelMode": "Truck",
  "TravelModeOptions": {
    "Truck": {
      "GrossWeight": 10000
    }
  }
}
```

Sample response

```
{
    "Notices": [],
    "SnappedGeometry": {
        "Polyline": "Redacted"
    },
    "SnappedGeometryFormat": "FlexiblePolyline",
    "SnappedTracePoints": [
        {
            "Confidence": 1,
            "OriginalPosition": [8.53404, 50.16364],
            "SnappedPosition": [8.53402, 50.16367]
        },
        {
            "Confidence": 0.86,
            "OriginalPosition": [8.53379056, 50.16352417],
            "SnappedPosition": [8.53375, 50.16356]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://routes.geo.eu-central-1.amazonaws.com/v2/snap-to-roads?key=Your_key' \
  --header 'Content-Type: application/json' \
  --data '{
  "TracePoints": [
    {
      "Position": [8.53404,50.16364],
      "Timestamp": "2024-05-22T18:13:42Z"
    },
    {
      "Position": [8.53379056,50.16352417],
      "Speed": 20,
      "Timestamp": "2024-05-22T18:13:59Z"
    }
  ],
  "TravelMode": "Truck",
  "TravelModeOptions": {
    "Truck": {
      "GrossWeight": 10000
    }
  }
}'
```

AWS CLI

```
aws geo-routes snap-to-roads --key ${YourKey} \
--trace-points '[{"Position": [8.53404, 50.16364], "Timestamp": "2024-05-22T18:13:42Z"}, {"Position": [8.53379056, 50.16352417], "Speed": 20, "Timestamp": "2024-05-22T18:13:59Z"}]' \
--travel-mode "Truck" \
--travel-mode-options '{"Truck": {"GrossWeight": 10000}}'
```

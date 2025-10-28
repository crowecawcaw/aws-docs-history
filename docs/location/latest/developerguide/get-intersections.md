# How to get intersections

`Intersections` allows you to retrieve all nearby intersections. This can
potentially be used by emergency services and delivery couriers.

## Potential use cases

- **Emergency response:** Emergency response
  vehicles often need to identify nearby intersections for optimal positioning
  when responding to calls. This allows them to maintain clear access routes
  and faster response times, while ensuring visibility from multiple
  approaches.
- **Delivery couriers:** Delivery couriers can
  utilize intersection data to find more efficient parking spots, especially
  in dense urban areas where door-to-door parking may be limited or
  restricted.

## Example

Sample request

```
{
    "QueryText":"910 Beach Avenue, Vancouver",
    "AdditionalFeatures": ["Intersections"]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
            "Address": {
                "Label": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                "Country": {
                    "Code2": "CA",
                    "Code3": "CAN",
                    "Name": "Canada"
                },
                "Region": {
                    "Code": "BC",
                    "Name": "British Columbia"
                },
                "SubRegion": {
                    "Name": "Metro Vancouver"
                },
                "Locality": "Vancouver",
                "District": "Downtown Vancouver",
                "PostalCode": "V6Z 2W7",
                "Street": "Beach Ave",
                "StreetComponents": [
                    {
                        "BaseName": "Beach",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "910"
            },
            "Position": [
                -123.13325,
                49.27542
            ],
            "MapView": [
                -123.13463,
                49.27452,
                -123.13187,
                49.27632
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Locality": 1,
                        "Intersection": [
                            1
                        ],
                        "AddressNumber": 1
                    }
                }
            },
            "ParsedQuery": {
                "Address": {
                    "Locality": [
                        {
                            "StartIndex": 18,
                            "EndIndex": 27,
                            "Value": "Vancouver",
                            "QueryComponent": "Query"
                        }
                    ],
                    "Street": [
                        {
                            "StartIndex": 4,
                            "EndIndex": 16,
                            "Value": "Beach Avenue",
                            "QueryComponent": "Query"
                        }
                    ],
                    "AddressNumber": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 3,
                            "Value": "910",
                            "QueryComponent": "Query"
                        }
                    ]
                }
            },
            "Intersections": [
                {
                    "PlaceId": "<Redacted>",
                    "Title": "Beach Ave & Hornby St, Vancouver, BC V6Z, Canada",
                    "Address": {
                        "Label": "Beach Ave & Hornby St, Vancouver, BC V6Z, Canada",
                        "PostalCode": "V6Z",
                        "Intersection": [
                            "Beach Ave",
                            "Hornby St"
                        ]
                    },
                    "Position": [
                        -123.1328,
                        49.27536
                    ]
                },
                {
                    "PlaceId": "<Redacted>",
                    "Title": "Beach Ave & Burrard St, Vancouver, BC, Canada",
                    "Address": {
                        "Label": "Beach Ave & Burrard St, Vancouver, BC, Canada",
                        "Intersection": [
                            "Beach Ave",
                            "Burrard St"
                        ]
                    },
                    "Position": [
                        -123.13377,
                        49.27599
                    ]
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText":"910 Beach Avenue, Vancouver",
    "AdditionalFeatures": ["Intersections"]
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "910 Beach Avenue, Vancouver" --additional-features "Intersections"
```

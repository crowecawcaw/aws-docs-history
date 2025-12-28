# How to get intersections

ReverseGeocode API can retrieve nearby intersections to the specified location.

## Potential use case

**Retrieve all nearby intersections.** This can be
used by emergency services and delivery couriers. Emergency response vehicles often
need to identify nearby intersections for optimal positioning when responding to
calls. This allows them to maintain clear access routes and faster response times
while ensuring visibility from multiple approaches. Similarly, delivery couriers can
utilize intersection data to find more efficient parking spots, especially in dense
urban areas where door-to-door parking may be limited or restricted.

## Get nearby intersections

Intersections are returned when the result type is Street, PointAddress, or InterpolatedAddress. To ensure you get nearby intersections, set the `Heading` parameter or filter for Street, PointAddress, or InterpolatedAddress types.

Sample request

```
{
   "QueryPosition": [-123.11694, 49.28126],
   "AdditionalFeatures": ["Intersections"],
   "Heading": 45
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
            "Address": {
                "Label": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
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
                "PostalCode": "V6B 0M3",
                "Street": "W Georgia St",
                "StreetComponents": [
                    {
                        "BaseName": "Georgia",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "510"
            },
            "Position": [
                -123.11694,
                49.28126
            ],
            "Distance": 0,
            "MapView": [
                -123.11813,
                49.27786,
                -123.11076,
                49.28246
            ],
            "Intersections": [
                {
                    "PlaceId": "<Redacted>",
                    "Title": "W Georgia St & Richards St, Vancouver, BC V6B, Canada",
                    "Address": {
                        "Label": "W Georgia St & Richards St, Vancouver, BC V6B, Canada",
                        "PostalCode": "V6B",
                        "Intersection": [
                            "W Georgia St",
                            "Richards St"
                        ]
                    },
                    "Position": [
                        -123.11614,
                        49.28124
                    ],
                    "Distance": 58
                },
                {
                    "PlaceId": "<Redacted>",
                    "Title": "W Georgia St & Seymour St, Vancouver, BC V6B, Canada",
                    "Address": {
                        "Label": "W Georgia St & Seymour St, Vancouver, BC V6B, Canada",
                        "PostalCode": "V6B",
                        "Intersection": [
                            "W Georgia St",
                            "W Georgia St",
                            "Seymour St",
                            "Seymour St"
                        ]
                    },
                    "Position": [
                        -123.11712,
                        49.28186
                    ],
                    "Distance": 68
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
   --url 'https://places.geo.eu-central-1.amazonaws.com/v2/reverse-geocode?key=Your_Key' \
   --header 'Content-Type: application/json' \
   --data '{
      "QueryPosition": [
         -123.11694, 49.28126
      ],
      "AdditionalFeatures": ["Intersections"],
      "Heading": 45
}
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position -123.11694, 49.28126 --additional-features "Intersections" --heading 45
```

Sample request

```
{
   "QueryPosition": [-123.11694, 49.28126],
   "AdditionalFeatures": ["Intersections"],
   "Filter": {
       "IncludePlaceTypes": ["Street"]
   }
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Street",
            "Title": "W Georgia St, Vancouver, BC V6B, Canada",
            "Address": {
                "Label": "W Georgia St, Vancouver, BC V6B, Canada",
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
                "PostalCode": "V6B",
                "Street": "W Georgia St",
                "StreetComponents": [
                    {
                        "BaseName": "Georgia",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ]
            },
            "Position": [
                -123.11694,
                49.28126
            ],
            "Distance": 0,
            "MapView": [
                -123.11813,
                49.27786,
                -123.11076,
                49.28246
            ],
            "Intersections": [
                {
                    "PlaceId": "<Redacted>",
                    "Title": "W Georgia St & Richards St, Vancouver, BC V6B, Canada",
                    "Address": {
                        "Label": "W Georgia St & Richards St, Vancouver, BC V6B, Canada",
                        "PostalCode": "V6B",
                        "Intersection": [
                            "W Georgia St",
                            "Richards St"
                        ]
                    },
                    "Position": [
                        -123.11614,
                        49.28124
                    ],
                    "Distance": 58
                },
                {
                    "PlaceId": "<Redacted>",
                    "Title": "W Georgia St & Seymour St, Vancouver, BC V6B, Canada",
                    "Address": {
                        "Label": "W Georgia St & Seymour St, Vancouver, BC V6B, Canada",
                        "PostalCode": "V6B",
                        "Intersection": [
                            "W Georgia St",
                            "W Georgia St",
                            "Seymour St",
                            "Seymour St"
                        ]
                    },
                    "Position": [
                        -123.11712,
                        49.28186
                    ],
                    "Distance": 68
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
   --url 'https://places.geo.eu-central-1.amazonaws.com/v2/reverse-geocode?key=Your_Key' \
   --header 'Content-Type: application/json' \
   --data '{
      "QueryPosition": [
         -123.11694, 49.28126
      ],
      "AdditionalFeatures": ["Intersections"],
      "Filter": {
          "IncludePlaceTypes": ["Street"]
      }
}'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position -123.11694, 49.28126 --additional-features "Intersections" --filter '{"IncludePlaceTypes": ["Street"]}'
```

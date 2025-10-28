# How to reverse geocode for correct

result

This guide provides methods to refine reverse geocoding results, ensuring that the
returned data aligns closely with specific business needs. Using filters, users can
narrow down results to more precisely match types like address points, streets, or
localities.

## Potential Use Cases

- **Restrict results for specific needs:** Use
  filters to retrieve only the most relevant information, such as exact
  addresses or broader locality data, based on business requirements.

## Examples

By filtering for `PointAddress`, you can retrieve specific
street addresses, enhancing location accuracy.

Sample Request

```
{
    "QueryPosition": [
        -97.721, 30.404
    ],
    "Filter": {
        "IncludePlaceTypes": [
            "PointAddress"
        ]
    }
}
```

Sample Response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "11721 Domain Blvd, Austin, TX 78758-0051, United States",
            "Address": {
                "Label": "11721 Domain Blvd, Austin, TX 78758-0051, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "TX",
                    "Name": "Texas"
                },
                "SubRegion": {
                    "Name": "Travis"
                },
                "Locality": "Austin",
                "District": "North Burnet",
                "PostalCode": "78758-0051",
                "Street": "Domain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Domain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "11721"
            },
            "Position": [
                -97.72087,
                30.404
            ],
            "Distance": 5,
            "MapView": [
                -97.72219,
                30.40273,
                -97.72057,
                30.40649
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
  "{
    "QueryPosition": [
        -97.721,  30.404
    ],
    "Filter": {
        "IncludePlaceTypes": [
            "PointAddress"
        ]
    }'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position -97.721 30.404 --filter '{"IncludePlaceTypes": ["PointAddress"]}'
```

By filtering for `Street`, the API returns street-level data
without specific address numbers.

Sample Request

```
{
    "QueryPosition": [
        -97.721, 30.404
    ],
    "Filter": {
        "IncludePlaceTypes": [
            "Street"
        ]
    }
}
```

Sample Response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Street",
            "Title": "Domain Blvd, Austin, TX 78758, United States",
            "Address": {
                "Label": "Domain Blvd, Austin, TX 78758, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "TX",
                    "Name": "Texas"
                },
                "SubRegion": {
                    "Name": "Travis"
                },
                "Locality": "Austin",
                "District": "North Burnet",
                "PostalCode": "78758",
                "Street": "Domain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Domain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ]
            },
            "Position": [
                -97.72103,
                30.40399
            ],
            "Distance": 3,
            "MapView": [
                -97.72219,
                30.40273,
                -97.72057,
                30.40649
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
  "{
    "QueryPosition": [
        -97.721,  30.404
    ],
    "Filter": {
        "IncludePlaceTypes": [
            "Street"
        ]
    }'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position -97.721 30.404 --filter '{"IncludePlaceTypes": ["Street"]}'
```

By filtering for `Locality`, you can retrieve broader location
data, including city names.

Sample Request

```
{
    "QueryPosition": [
        -97.721, 30.404
    ],
    "Filter": {
        "IncludePlaceTypes": [
            "Locality"
        ]
    }
}
```

Sample Response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "Austin, TX, United States",
            "Address": {
                "Label": "Austin, TX, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "TX",
                    "Name": "Texas"
                },
                "SubRegion": {
                    "Name": "Travis"
                },
                "Locality": "Austin",
                "PostalCode": "78701"
            },
            "Position": [
                -97.74299,
                30.26759
            ],
            "Distance": 0,
            "MapView": [
                -98.06484,
                30.06592,
                -97.55914,
                30.51965
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
  "{
    "QueryPosition": [
        -97.721,  30.404
    ],
    "Filter": {
        "IncludePlaceTypes": [
            "Locality"
        ]
    }'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position -97.721 30.404 --filter '{"IncludePlaceTypes": ["Locality"]}'
```

# How to search for a place, POI,

or business using a name

The SearchText API allows users to search for a place, POI, or business by name, using
free text input. Results can be refined by setting a bias position, which may be based
on device location, IP position, or map viewport center. Alternatively, users can
provide a specific city or place, with results biased based on the provided
geocoordinates.

## Potential use cases

- **Locate a place by name:** Retrieve
  locations based on place names, such as "Gas Town".
- **Find points of interest (POIs):** Search
  for places of interest by name, such as "Stanley Park".
- **Search by business name:** Locate
  businesses by name, like "Starbucks".

## Examples

Sample request

```
{
    "QueryText": "Gas Town",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "District",
            "Title": "Gastown, Vancouver, BC, Canada",
            "Address": {
                "Label": "Gastown, Vancouver, BC, Canada",
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
                "District": "Gastown",
                "PostalCode": "V6B"
            },
            "Position": [
                -123.10647,
                49.28363
            ],
            "Distance": 2633,
            "MapView": [
                -123.11193,
                49.28141,
                -123.10217,
                49.28648
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Gas Town",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${`YourKey`} --query-text "Gas Town" --bias-position -123.11336 49.26038
```

Sample request

```
{
    "QueryText": "Stanley Park",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Stanley Park",
            "Address": {
                "Label": "Stanley Park, Stanley Park Dr, Vancouver, BC V6G, Canada",
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
                "District": "Stanley Park",
                "PostalCode": "V6G",
                "Street": "Stanley Park Dr",
                "StreetComponents": [
                    {
                        "BaseName": "Stanley Park",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ]
            },
            "Position": [
                -123.13593,
                49.29716
            ],
            "Distance": 4405,
            "Categories": [
                {
                    "Id": "park-recreation_area",
                    "Name": "Park-Recreation Area",
                    "LocalizedName": "Park-Recreation Area",
                    "Primary": true
                },
                {
                    "Id": "tourist_attraction",
                    "Name": "Tourist Attraction",
                    "LocalizedName": "Tourist Attraction",
                    "Primary": false
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Stanley Park",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${`YourKey`} --query-text "Stanley Park" --bias-position -123.11336 49.26038
```

Sample request

```
{
    "QueryText": "Amazon YVR11",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Amazon YVR11",
            "Address": {
                "Label": "Amazon YVR11, 510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
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
            "Distance": 2336,
            "Categories": [
                {
                    "Id": "business_facility",
                    "Name": "Business Facility",
                    "LocalizedName": "Business Facility",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.11656,
                        49.28151
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
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Amazon YVR11",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${`YourKey`} --query-text "Amazon YVR11" --bias-position -123.11336 49.26038
```

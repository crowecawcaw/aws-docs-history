# How to search nearby from a position

The SearchNearby API enables querying for all nearby places and points of interest
(POI) without entering any specific text. Users can explore neighborhoods, discover
POIs, and more using this API. It requires a `QueryPosition`, which can
represent a device's location, IP-based position, or the map viewport center.
Alternatively, users can specify a city or place to bias results based on the
geocoordinates of that location.

## Potential use cases

- **Explore nearby POIs:** View all points of
  interest near the current position.
- **Explore nearby places:** View all locations
  or places near a given position.

## Examples

In this example, the search is conducted from a position in Dubai with
latitude 25.26951 and longitude 55.30884.

Sample request

```
{
    "QueryPosition": [
        55.30884,
        25.26951
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
            "Title": "هما",
            "Address": {
                "Label": "هما, شارع مستشفى آل مكتوم, نايف دبي, الإمارات العربية المتحدة",
                "Country": {
                    "Code2": "AE",
                    "Code3": "ARE",
                    "Name": "الإمارات العربية المتحدة"
                },
                "SubRegion": {
                    "Name": "دبي"
                },
                "Locality": "دبي",
                "District": "نايف",
                "Street": "شارع مستشفى آل مكتوم",
                "StreetComponents": [
                    {
                        "BaseName": "مستشفى آل مكتوم",
                        "Type": "شارع",
                        "TypePlacement": "BeforeBaseName",
                        "TypeSeparator": " ",
                        "Language": "ar"
                    }
                ]
            },
            "Position": [
                55.30884,
                25.26951
            ],
            "Distance": 0,
            "Categories": [
                {
                    "Id": "department_store",
                    "Name": "Department Store",
                    "LocalizedName": "مول تجاري",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "HEMA",
                    "Id": "HEMA"
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "دبي, الإمارات العربية المتحدة",
            "Address": {
                "Label": "دبي, الإمارات العربية المتحدة",
                "Country": {
                    "Code2": "AE",
                    "Code3": "ARE",
                    "Name": "الإمارات العربية المتحدة"
                },
                "SubRegion": {
                    "Name": "دبي"
                },
                "Locality": "دبي"
            },
            "Position": [
                55.30884,
                25.26951
            ],
            "Distance": 0,
            "MapView": [
                54.64906,
                24.62308,
                55.7371,
                25.36995
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-nearby?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [
        55.30884,
        25.26951
    ],
    "MaxResults": 2
}'
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position 55.30884 25.26951 \
--max-results 2
```

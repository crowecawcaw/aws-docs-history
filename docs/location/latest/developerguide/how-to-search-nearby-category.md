# How to search nearby places based on

category

The SearchNearby API enables querying for points of interest (POI) with the inclusion
or exclusion of specified categories. This can help users explore neighborhoods,
discover local POIs, and more. The API requires a `QueryPosition`, which can
be based on a device's location, IP position, or the center of the map viewport.
Alternatively, users can specify a city or place, and the application will bias results
based on that location’s coordinates.

To learn more about supported categories, see [Categories filters](places-filtering.md#place-categories "places-filtering.md#place-categories").

## Potential use cases

- **Explore local facilities:** Find available
  facilities within a neighborhood.
- **Discover tourist attractions:** Identify
  tourist spots within a city.
- **Plan travel in a city:** Organize travel
  around different POIs within a chosen city.

## Examples

Sample request

```
{
    "QueryPosition": [
        4.35609,
        50.84439
    ],
    "Filter": {
        "IncludeCategories": ["airport"]
    }
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Brussels Airport",
            "Address": {
                "Label": "Brussels Airport, A201, 1930 Zaventem, België",
                "Country": {
                    "Code2": "BE",
                    "Code3": "BEL",
                    "Name": "België"
                },
                "Region": {
                    "Code": "VLG",
                    "Name": "Vlaanderen"
                },
                "SubRegion": {
                    "Name": "Vlaams Brabant"
                },
                "Locality": "Zaventem",
                "PostalCode": "1930",
                "Street": "A201",
                "StreetComponents": [
                    {
                        "BaseName": "A201",
                        "Language": "nl"
                    }
                ]
            },
            "Position": [
                4.47767,
                50.89452
            ],
            "Distance": 10191,
            "Categories": [
                {
                    "Id": "airport",
                    "Name": "Airport",
                    "LocalizedName": "Luchthaven",
                    "Primary": true
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Internationale Luchthaven Antwerpen",
            "Address": {
                "Label": "Internationale Luchthaven Antwerpen, Luchthavenlei 1, 2100 Antwerpen, België",
                "Country": {
                    "Code2": "BE",
                    "Code3": "BEL",
                    "Name": "België"
                },
                "Region": {
                    "Code": "VLG",
                    "Name": "Vlaanderen"
                },
                "SubRegion": {
                    "Name": "Antwerpen"
                },
                "Locality": "Antwerpen",
                "District": "Deurne",
                "PostalCode": "2100",
                "Street": "Luchthavenlei",
                "StreetComponents": [
                    {
                        "BaseName": "Luchthaven",
                        "Type": "lei",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": "",
                        "Language": "nl"
                    }
                ],
                "AddressNumber": "1"
            },
            "Position": [
                4.45083,
                51.18867
            ],
            "Distance": 38852,
            "Categories": [
                {
                    "Id": "airport",
                    "Name": "Airport",
                    "LocalizedName": "Luchthaven",
                    "Primary": true
                }
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
        4.35609,
        50.84439
    ],
    "Filter": {
        "IncludeCategories": ["airport"]
    },
    "MaxResults": 2
}
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position 4.35609 50.84439 \
--filter '{"IncludeCategories": ["airport"]}' \
--max-results 2
```

Sample request

```
{
    "QueryPosition": [
        4.35609,
        50.84439
    ],
    "Filter": {
        "ExcludeCategories": ["airport"]
    }
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Socialbrands Module 2",
            "Address": {
                "Label": "Socialbrands Module 2, Albertinaplein, 1000 Brussel, België",
                "Country": {
                    "Code2": "BE",
                    "Code3": "BEL",
                    "Name": "België"
                },
                "Region": {
                    "Code": "BRU",
                    "Name": "Brussel"
                },
                "SubRegion": {
                    "Name": "Brussel"
                },
                "Locality": "Brussel",
                "District": "Koningswijk",
                "PostalCode": "1000",
                "Street": "Albertinaplein",
                "StreetComponents": [
                    {
                        "BaseName": "Albertina",
                        "Type": "plein",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": "",
                        "Language": "nl"
                    }
                ]
            },
            "Position": [
                4.35609,
                50.84439
            ],
            "Distance": 0,
            "Categories": [
                {
                    "Id": "commercial_services",
                    "Name": "Commercial Services",
                    "LocalizedName": "Commerciële diensten",
                    "Primary": true
                }
            ],
            "Contacts": {
                "Websites": [
                    {
                        "Value": "https://oneread.net"
                    }
                ]
            },
            "AccessPoints": [
                {
                    "Position": [
                        4.35609,
                        50.84439
                    ]
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Barman Privé",
            "Address": {
                "Label": "Barman Privé, Albertinaplein, 1000 Brussel, België",
                "Country": {
                    "Code2": "BE",
                    "Code3": "BEL",
                    "Name": "België"
                },
                "Region": {
                    "Code": "BRU",
                    "Name": "Brussel"
                },
                "SubRegion": {
                    "Name": "Brussel"
                },
                "Locality": "Brussel",
                "District": "Koningswijk",
                "PostalCode": "1000",
                "Street": "Albertinaplein",
                "StreetComponents": [
                    {
                        "BaseName": "Albertina",
                        "Type": "plein",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": "",
                        "Language": "nl"
                    }
                ]
            },
            "Position": [
                4.35609,
                50.84439
            ],
            "Distance": 0,
            "Categories": [
                {
                    "Id": "catering_and_other_food_services",
                    "Name": "Catering and Other Food Services",
                    "LocalizedName": "Catering- en horecadiensten",
                    "Primary": true
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+32476891634"
                    }
                ]
            },
            "OpeningHours": [
                {
                    "Display": [
                        "ma-zo: 00:00 - 24:00"
                    ],
                    "OpenNow": true,
                    "Components": [
                        {
                            "OpenTime": "T000000",
                            "OpenDuration": "PT24H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA,SU"
                        }
                    ]
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        4.35609,
                        50.84439
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
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-nearby?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [
        4.35609,
        50.84439
    ],
    "Filter": {
        "ExcludeCategories": ["airport"]
    }
}
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position 4.35609 50.84439 \
--filter '{"ExcludeCategories": ["airport"]}' \
--max-results 2
```

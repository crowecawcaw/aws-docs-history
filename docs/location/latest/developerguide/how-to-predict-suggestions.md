# How to predict suggestions based on

input

The Suggest API enables applications to complete user queries for places or categories
of results. These suggestions can be used directly or refined further with the
SearchText API to retrieve additional details and results.

## Potential use cases

- **Restaurant or park lookup:** Locate
  restaurants, parks, or other places near a specific position.

## Examples

Sample request

```
{
  "QueryText": "restaura",
  "BiasPosition": [-124.81035775620968, 49.234628873773985],
  "AdditionalFeatures": ["Core"]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "Title": "Restaurant",
            "SuggestResultItemType": "Query",
            "Query": {
                "QueryId": "AQAAAHgAw1x7...",
                "QueryType": "Category"
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 0,
                        "EndIndex": 8,
                        "Value": "Restaura"
                    }
                ]
            }
        }
    ],
    "QueryRefinements": []
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/suggest?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "restaura",
  "BiasPosition": [-124.81035775620968, 49.234628873773985],
  "AdditionalFeatures": ["Core"]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} \
--query-text "restaura" \
--bias-position -124.81035775620968 49.234628873773985 \
--additional-features "Core"
```

Sample request

```
{
  "QueryText": "Domin",
  "BiasPosition": [-124.81035775620968, 49.234628873773985],
  "AdditionalFeatures": ["Core"]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "Title": "Domino's",
            "SuggestResultItemType": "Query",
            "Query": {
                "QueryId": "AQAAAHUA4UNp...",
                "QueryType": "BusinessChain"
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 0,
                        "EndIndex": 5,
                        "Value": "Domin"
                    }
                ]
            }
        }
    ],
    "QueryRefinements": []
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/suggest?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "Domin",
  "BiasPosition": [-124.81035775620968, 49.234628873773985],
  "AdditionalFeatures": ["Core"]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} \
--query-text "Domin" \
--bias-position -124.81035775620968 49.234628873773985 \
--additional-features "Core"
```

Sample request (SearchText)

```
{
  "QueryId": "<QueryId from Suggest API>",
  "AdditionalFeatures": ["Core"]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Domino's",
            "Address": {
                "Label": "Domino's, 233 Shelly Rd, Parksville, BC V9P, Canada",
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
                    "Name": "Nanaimo"
                },
                "Locality": "Parksville",
                "PostalCode": "V9P",
                "Street": "Shelly Rd",
                "StreetComponents": [
                    {
                        "BaseName": "Shelly",
                        "Type": "Rd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "233"
            },
            "Position": [
                -124.29334,
                49.31669
            ],
            "Distance": 38602,
            "Categories": [
                {
                    "Id": "fast_food",
                    "Name": "Fast Food",
                    "LocalizedName": "Fast Food",
                    "Primary": true
                },
                {
                    "Id": "take_out_and_delivery_only",
                    "Name": "Take Out and Delivery Only",
                    "LocalizedName": "Take Out & Delivery Only",
                    "Primary": false
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Pizza",
                    "Id": "pizza",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "Domino's",
                    "Id": "Domino's"
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+12502489296"
                    }
                ],
                "Websites": [
                    {
                        "Value": "http://pizza.dominos.ca/Parksville-British-Columbia-10039"
                    }
                ]
            },
            "OpeningHours": [
                {
                    "Display": [
                        "Mon-Fri: 11:00 - 24:00",
                        "Sat, Sun: 00:00 - 01:00, 11:00 - 24:00"
                    ],
                    "OpenNow": true,
                    "Components": [
                        {
                            "OpenTime": "T110000",
                            "OpenDuration": "PT13H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH,SU"
                        },
                        {
                            "OpenTime": "T110000",
                            "OpenDuration": "PT14H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:FR,SA"
                        }
                    ]
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -124.29319,
                        49.31669
                    ]
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Domino's",
            "Address": {
                "Label": "Domino's, 215 Port Augusta St, Comox, BC V9M, Canada",
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
                    "Name": "Comox Valley"
                },
                "Locality": "Comox",
                "PostalCode": "V9M",
                "Street": "Port Augusta St",
                "StreetComponents": [
                    {
                        "BaseName": "Port Augusta",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "215"
            },
            "Position": [
                -124.92492,
                49.67378
            ],
            "Distance": 49528,
            "Categories": [
                {
                    "Id": "fast_food",
                    "Name": "Fast Food",
                    "LocalizedName": "Fast Food",
                    "Primary": true
                },
                {
                    "Id": "take_out_and_delivery_only",
                    "Name": "Take Out and Delivery Only",
                    "LocalizedName": "Take Out & Delivery Only",
                    "Primary": false
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Pizza",
                    "Id": "pizza",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "Domino's",
                    "Id": "Domino's"
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+17784310222"
                    }
                ],
                "Websites": [
                    {
                        "Value": "http://pizza.dominos.ca/comox-british-columbia-39035"
                    }
                ]
            },
            "OpeningHours": [
                {
                    "Display": [
                        "Mon-Thu: 10:30 - 23:00",
                        "Fri: 10:30 - 24:00",
                        "Sat: 00:00 - 01:00, 10:30 - 24:00",
                        "Sun: 00:00 - 01:00, 10:30 - 23:00"
                    ],
                    "OpenNow": true,
                    "Components": [
                        {
                            "OpenTime": "T103000",
                            "OpenDuration": "PT12H30M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH,SU"
                        },
                        {
                            "OpenTime": "T103000",
                            "OpenDuration": "PT14H30M",
                            "Recurrence": "FREQ:DAILY;BYDAY:FR,SA"
                        }
                    ]
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -124.92518,
                        49.67387
                    ]
                }
            ]
        },
        ...
    ],
    "QueryRefinements": []
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryId": "<QueryId from Suggest API>",
  "AdditionalFeatures": ["Core"]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} \
--query-id "<QueryId from Suggest API>" \
--additional-features "Core"
```

## Developer tips

Use filters such as `Filter.IncludeCountries` or
`Filter.BoundingBox` with `BiasPosition`. These filters
apply to subsequent queries using the `QueryId`.

```
{
  "QueryText": "Domin",
  "BiasPosition": [-124.81035775620968, 49.234628873773985],
  "Filter": {
    "IncludeCountries": ["CAN"]
  }
}
```

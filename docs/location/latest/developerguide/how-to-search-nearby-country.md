# How to search nearby within a

country

The SearchNearby API enables you to search for nearby places within a specific
country. To use the API, you need to provide a QueryPosition, which can be:

- A device position
- An IP-based position
- A map's viewport center
  Alternatively, users can provide a city name or place, and the application can bias
  results based on the geocoordinates of that location.

## Potential use cases

- Explore businesses within a country
- Find nearby B2B customers within a country
- Explore tourist places within a country

## Examples

The following example demonstrates how to search for golf courses within
Canada near specified coordinates.

Sample request
This request searches for golf courses in Canada near the
specified location.

```
{
    "QueryPosition": [
            -122.741803,
            49.002478
    ],
    "Filter" : {
        "IncludeCategories": ["golf_course"],
        "IncludeCountries": ["CAN"]
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
            "Title": "Peace Portal Golf Course",
            "Address": {
                "Label": "Peace Portal Golf Course, 16900 * Ave, Surrey, BC V*Z *P*, Canada",
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
                "Locality": "Surrey",
                "District": "South Surrey",
                "PostalCode": "V*Z *P*",
                "Street": "* Ave",
                "StreetComponents": [
                    {
                        "BaseName": "4",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "16900"
            },
            "Position": [
                -122.75086,
                49.00921
            ],
            "Distance": 998,
            "Categories": [
                {
                    "Id": "golf_course",
                    "Name": "Golf Course",
                    "LocalizedName": "Golf Course",
                    "Primary": true
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+16045384818"                    }
                ],
                "Websites": [
                    {
                        "Value": "http://www.peaceportalgolf.com"
                    }
                ]
            },
            "AccessPoints": [
                {
                    "Position": [
                        -122.75087,
                        49.00935
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
         -122.741803,
         49.002478
        ],
        "Filter" : {
        "IncludeCategories": ["golf_course"],
              "IncludeCountries": ["CAN"]
    }

}'
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position -122.741803 49.002478 \
--filter '{"IncludeCategories": ["golf_course"], "IncludeCountries": ["CAN"]}'
```

# How to search for a place within a

country

The `SearchText` API enables you limit search results to within one or more
countries. This feature useful for searching in border areas or smaller countries that
neighbour each other.

One way to use the SearchText API is to let end users do a free-text search and an
application set's bias position. These bias positions can be a device position, IP
position, or a map‘s view port center. Additionally, end users can provide the city name
or place and the application can bias results based on geo-coordinates.

## Potential use cases

- Limit the search results to within a country for an area that has a nearby
  international border.
- Filter results to withing multiple countries.

## Examples

In this example, the bias position is near the USA and Canada border.
Without specifying `IncludeCountries": ["CAN"]`, the API would
return results from both Canada and the USA.

Sample request

```
{
    "QueryText": "Starbucks",
    "BiasPosition": [
                -122.741803,
                 49.002478
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
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 16010 24 Ave, Surrey, BC V3Z 0R5, Canada",
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
                "PostalCode": "V3Z 0R5",
                "Street": "24 Ave",
                "StreetComponents": [
                    {
                        "BaseName": "24",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "16010"
            },
            "Position": [
                -122.77867,
                49.04482
            ],
            "Distance": 5422,
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 1730 152 St, Surrey, BC V4A 4N4, Canada",
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
                "PostalCode": "V4A 4N4",
                "Street": "152 St",
                "StreetComponents": [
                    {
                        "BaseName": "152",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "1730"
            },
            "Position": [
                -122.80096,
                49.03341
            ],
            "Distance": 5517,
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "Starbucks",
                    "Id": "Starbucks"
                }
            ]
        },
        ...
        ...
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Starbucks",
    "BiasPosition": [
                -122.741803,
                49.002478
            ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-text "Starbucks" --bias-position -122.741803 49.002478
```

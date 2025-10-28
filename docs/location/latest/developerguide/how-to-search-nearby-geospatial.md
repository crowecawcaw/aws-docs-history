# How to search nearby using geospatial

context

The SearchNearby API enables you to explore nearby, while restricting results within
geospatial context (such as a circle or bounding box).

The SearchNearby API lets you filter results using geospatial contexts such as circles
and bounding boxes. By defining these geographic boundaries, you can limit search
results to specific areas.

## Potential use cases

- Limit search results to a specific geographic area
- Search within custom-defined boundaries
- Focus results on targeted neighborhoods or districts

## Examples

The following example demonstrates how to search for schools within a
1000-meter radius of the specified coordinates.

Sample request
This request searches for schools within a 1000-meter
(1-kilometer) radius.

```
{
    "QueryPosition": [
                 -122.741803,
         49.002478
        ],
        "QueryRadius":1000,
        "Filter" : {
            "IncludeCategories": ["school"]
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
            "Title": "Grace Lutheran Church",
            "Address": {
                "Label": "Grace Lutheran Church, 702 G St, Blaine, WA 98230-5125, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "WA",
                    "Name": "Washington"
                },
                "SubRegion": {
                    "Name": "Whatcom"
                },
                "Locality": "Blaine",
                "PostalCode": "98230-5125",
                "Street": "G St",
                "StreetComponents": [
                    {
                        "BaseName": "G",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "702"
            },
            "Position": [
                -122.74157,
                48.99533
            ],
            "Distance": 795,
            "Categories": [
                {
                    "Id": "church",
                    "Name": "Church",
                    "LocalizedName": "Church",
                    "Primary": true
                },
                {
                    "Id": "kindergarten_and_childcare",
                    "Name": "Kindergarten and Childcare",
                    "LocalizedName": "Kindergarten & Childcare",
                    "Primary": false
                },
                {
                    "Id": "school",
                    "Name": "School",
                    "LocalizedName": "School",
                    "Primary": false
                }
            ]
        }
        ...
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/searearch-nearby?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [
         -122.741803,
         49.002478
    ],
    "QueryRadius": 1000,
    "Filter": {
        "IncludeCategories": ["school"]
    }
}'
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position -122.741803 49.002478 \
--query-radius 1000 \
--filter '{"IncludeCategories": ["school"]}'
```

## Developer Tips

- Alternatively, you can use a bounding box filter.

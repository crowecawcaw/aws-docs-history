# How to search using category name or food

type

The `SearchText` API enables you to search by name of category such as
restaurants, schools and more. You can also search by food type.

One way to use the SearchText API is to let end users search by name (category and
food type) and an application set's bias position. These bias positions can be a device
position, IP position, or a map‘s view port center. Additionally, end users can provide
the city name or place and the application can bias results based on
geo-coordinates.

For more information, see [Categories filters](places-filtering.md#place-categories "places-filtering.md#place-categories") and [Food Type filters](places-filtering.md#food-type "places-filtering.md#food-type").

## Potential use cases

- Search for specific POI or place as a part of exploring a neighborhood.
- Search for specific tourist spot for travel planning.
- Search for restaurants that serve a specific food.

## Examples

Sample request

```
{
    "QueryText": "Nursing Home",
    "BiasPosition": [
                -123.11336,
                49.26038
            ],
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Diamond Geriatrics Inc",
            "Address": {
                "Label": "Diamond Geriatrics Inc, 288 W 8th Ave, Vancouver, BC V5Y 1N5, Canada",
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
                "District": "Mt Pleasant",
                "PostalCode": "V5Y 1N5",
                "Street": "W 8th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "8th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "288"
            },
            "Position": [
                -123.11061,
                49.2636
            ],
            "Distance": 410,
            "Categories": [
                {
                    "Id": "nursing_home",
                    "Name": "Nursing Home",
                    "LocalizedName": "Nursing Home",
                    "Primary": true
                },
                {
                    "Id": "social_service",
                    "Name": "Social Service",
                    "LocalizedName": "Social Services",
                    "Primary": false
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Para Med Home Health Care",
            "Address": {
                "Label": "Para Med Home Health Care, 601 W Broadway, Vancouver, BC V5Z 4C2, Canada",
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
                "District": "Fairview",
                "PostalCode": "V5Z 4C2",
                "Street": "W Broadway",
                "StreetComponents": [
                    {
                        "BaseName": "Broadway",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "601"
            },
            "Position": [
                -123.11772,
                49.26343
            ],
            "Distance": 464,
            "Categories": [
                {
                    "Id": "nursing_home",
                    "Name": "Nursing Home",
                    "LocalizedName": "Nursing Home",
                    "Primary": true
                },
                {
                    "Id": "hospital_or_health_care_facility",
                    "Name": "Hospital or Health Care Facility",
                    "LocalizedName": "Hospital or Health Care Facility",
                    "Primary": false
                }
            ]
        }
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
    "QueryText": "Nursing Home",
    "BiasPosition": [
                -123.11336,
                49.26038
            ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-text "Nursing Home" --bias-position -123.11336 49.26038
```

Specify a food type for `QueryText` to select restaurants by
food type. Filtering by food type enables restaurants to be indexed,
queried, and displayed by food type.

Sample request

```
{
    "QueryText": "Sushi",
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
            "Title": "Sushi Tomy",
            "Address": {
                "Label": "Sushi Tomy, 555 W 12th Ave, Vancouver, BC V5Z 3X7, Canada",
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
                "District": "Fairview",
                "PostalCode": "V5Z 3X7",
                "Street": "W 12th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "12th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "555"
            },
            "Position": [
                -123.11629,
                49.26086
            ],
            "Distance": 219,
            "Categories": [
                {
                    "Id": "deli",
                    "Name": "Deli",
                    "LocalizedName": "Deli",
                    "Primary": true
                },
                {
                    "Id": "restaurant",
                    "Name": "Restaurant",
                    "LocalizedName": "Restaurant",
                    "Primary": false
                },
                {
                    "Id": "casual_dining",
                    "Name": "Casual Dining",
                    "LocalizedName": "Casual Dining",
                    "Primary": false
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Japanese - Sushi",
                    "Id": "japanese-sushi",
                    "Primary": true
                },
                {
                    "LocalizedName": "Canadian",
                    "Id": "canadian",
                    "Primary": false
                },
                {
                    "LocalizedName": "Japanese",
                    "Id": "japanese",
                    "Primary": false
                }
            ]
        },
        {
            "PlaceId": "<Redacted>"
            "PlaceType": "PointOfInterest",
            "Title": "Shiro Japanese Restaurant",
            "Address": {
                "Label": "Shiro Japanese Restaurant, 3096 Cambie St, Vancouver, BC V5Z 2V9, Canada",
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
                "District": "Mt Pleasant",
                "PostalCode": "V5Z 2V9",
                "Street": "Cambie St",
                "StreetComponents": [
                    {
                        "BaseName": "Cambie",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "3096"
            },
            "Position": [
                -123.11461,
                49.25797
            ],
            "Distance": 283,
            "Categories": [
                {
                    "Id": "casual_dining",
                    "Name": "Casual Dining",
                    "LocalizedName": "Casual Dining",
                    "Primary": true
                },
                {
                    "Id": "restaurant",
                    "Name": "Restaurant",
                    "LocalizedName": "Restaurant",
                    "Primary": false
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Japanese - Sushi",
                    "Id": "japanese-sushi",
                    "Primary": true
                },
                {
                    "LocalizedName": "Asian",
                    "Id": "asian",
                    "Primary": false
                },
                {
                    "LocalizedName": "Japanese",
                    "Id": "japanese",
                    "Primary": false
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
    "QueryText": "Sushi",
    "BiasPosition": [
                -123.11336,
                49.26038
            ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-text "Sushi" --bias-position -123.11336 49.26038
```

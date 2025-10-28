# How to search in a specific

language

This feature allows the selection of a preferred response language from
BCP47-compliant codes. It detects the query language based on name variants and uses the
preferred language for unmatched tokens and ambiguous cases. If there is no requested
language, the **Places** API provides results in the official country
language, but prioritizes the regional language in regions where it differs. As a
fallback strategy, if any address elements are unavailable in the requested language,
**Places** APIs return addresses in the default language.

## Potential use cases

One potential use case is to localize the query and/or the result.

## Examples

Without the `"Language": "EN"` line in the request, results
would be returned in Hebrew.

Sample request

```

{
    "QueryText": "Vegan",
        "BiasPosition":[
                34.78953,
                32.08556
        ],
    "Language": "EN"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Rainbow",
            "Address": {
                "Label": "Rainbow, Ibn Gabirol 88, 6404612 Tel Aviv-Yafo, Israel",
                "Country": {
                    "Code2": "IL",
                    "Code3": "ISR",
                    "Name": "Israel"
                },
                "Region": {
                    "Code": "TA",
                    "Name": "TA"
                },
                "SubRegion": {
                    "Name": "Tel Aviv"
                },
                "Locality": "Tel Aviv-Yafo",
                "District": "The New North-Southern Area",
                "PostalCode": "6404612",
                "Street": "Ibn Gabirol",
                "StreetComponents": [
                    {
                        "BaseName": "Ibn Gabirol",
                        "Language": "he-Latn"
                    }
                ],
                "AddressNumber": "88"
            },
            "Position": [
                34.78149,
                32.08252
            ],
            "Distance": 829,
            "Categories": [
                {
                    "Id": "restaurant",
                    "Name": "Restaurant",
                    "LocalizedName": "Restaurant",
                    "Primary": true
                },
                {
                    "Id": "fast_food",
                    "Name": "Fast Food",
                    "LocalizedName": "Fast Food",
                    "Primary": false
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Vegan",
                    "Id": "vegan",
                    "Primary": true
                },
                {
                    "LocalizedName": "Fast Food",
                    "Id": "fast_food",
                    "Primary": false
                },
                {
                    "LocalizedName": "Burgers",
                    "Id": "burgers",
                    "Primary": false
                },
                {
                    "LocalizedName": "Jewish/Kosher",
                    "Id": "jewish/kosher",
                    "Primary": false
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Alegria",
            "Address": {
                "Label": "Alegria, Ibn Gabirol 165, 6203305 Tel Aviv-Yafo, Israel",
                "Country": {
                    "Code2": "IL",
                    "Code3": "ISR",
                    "Name": "Israel"
                },
                "Region": {
                    "Code": "TA",
                    "Name": "TA"
                },
                "SubRegion": {
                    "Name": "Tel Aviv"
                },
                "Locality": "Tel Aviv-Yafo",
                "District": "The Old North-Northern Area",
                "PostalCode": "6203305",
                "Street": "Ibn Gabirol",
                "StreetComponents": [
                    {
                        "BaseName": "Ibn Gabirol",
                        "Language": "he-Latn"
                    }
                ],
                "AddressNumber": "165"
            },
            "Position": [
                34.78295,
                32.0923
            ],
            "Distance": 973,
            "Categories": [
                {
                    "Id": "restaurant",
                    "Name": "Restaurant",
                    "LocalizedName": "Restaurant",
                    "Primary": true
                },
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": false
                },
                {
                    "Id": "specialty_food_store",
                    "Name": "Specialty Food Store",
                    "LocalizedName": "Specialty Food Store",
                    "Primary": false
                },
                {
                    "Id": "bakery_and_baked_goods_store",
                    "Name": "Bakery and Baked Goods Store",
                    "LocalizedName": "Bakery & Baked Goods Store",
                    "Primary": false
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Vegan",
                    "Id": "vegan",
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
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '
        {
            "QueryText": "Vegan",
                "BiasPosition":[
                        34.78953,
                        32.08556
                ],
            "Language": "EN"
        }'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-text "Vegan" \
--bias-position 34.78953 32.08556 \
--language "EN"
```

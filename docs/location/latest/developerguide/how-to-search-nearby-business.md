# How to search nearby based on business

chain

The SearchNearby API enables you to query nearby business chains. You can include or
exclude specific business chains in your search. This feature allows end users to
explore neighborhoods, discover points of interest, and more.

To use the SearchNearby API, you need to provide a QueryPosition, which can be:

- A device position
- An IP-based position
- A map's viewport center
  Alternatively, users can provide a city name or place, and the application can bias
  results based on the geo-coordinates of that location.

For more information about supported business chains, see [Business Chains filter](places-filtering.md#business-chains "places-filtering.md#business-chains").

## Potential use cases

- Explore businesses in the vicinity
- Expand your business by finding nearby B2B customers

## Examples

The following example demonstrates how to search for nearby Starbucks
locations.

Sample request
This request searches for Starbucks locations near the
specified coordinates.

```
{
    "QueryPosition": [
        12.49563,
        41.90325
    ],
    "Filter" : {
        "IncludeBusinessChains": ["Starbucks"]
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
            "Title": "Starbucks",
            "Address": {
                "Label": "Starbucks, Via Giovanni Giolitti, 2, 00185 Roma RM, Italia",
                "Country": {
                    "Code2": "IT",
                    "Code3": "ITA",
                    "Name": "Italia"
                },
                "Region": {
                    "Name": "Lazio"
                },
                "SubRegion": {
                    "Code": "RM",
                    "Name": "Roma"
                },
                "Locality": "Roma",
                "District": "Esquilino",
                 "PostalCode": "00185",
                "Street": "Via Giovanni Giolitti",
                "StreetComponents": [
                    {
                        "BaseName": "Giovanni Giolitti",
                        "Type": "Via",
                        "TypePlacement": "BeforeBaseName",
                        "TypeSeparator": " ",
                        "Language": "it"
                    }
                ],
                "AddressNumber": "2"
            },
            "Position": [
                12.50102,
                41.90093
            ],
            "Distance": 515,
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Bar",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "Starbucks",
                    "Id": "Starbucks"
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
                12.49563,
                41.90325
        ],
        "Filter" : {
        "IncludeBusinessChains": ["Starbucks"]
    }
}'
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position 12.49563 41.90325 \
--filter '{"IncludeBusinessChains": ["Starbucks"]}'
```

## Developer Tips

- You can use `ExcludeBusinessChains` to exclude certain business
  chains from your results.
- You can exclude or include multiple business chains.

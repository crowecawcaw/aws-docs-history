# How to search for a place

using contact information

The SearchText API allows users to search for a place using a phone number, supporting
both international and local formats. Users can bias results by setting a position based
on device location, IP address, or map viewport center, or by specifying a city or place
to refine results based on geocoordinates.

## Potential use cases

- **Locate a place with a phone number:** Find
  a POI by using its contact number to retrieve its address.

## Examples

In this example, the Vancouver Aquarium is searched using its phone number
"+1 778-655-9554" from a bias position in Vancouver, BC.

Sample request

```
{
    "QueryText": "+1 778-655-9554",
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
            "Title": "Vancouver Aquarium",
            "Address": {
                "Label": "Vancouver Aquarium, 834 Avison Way, Vancouver, BC V6G, Canada",
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
                "Street": "Avison Way",
                "StreetComponents": [
                    {
                        "BaseName": "Avison",
                        "Type": "Way",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "834"
            },
            "Position": [
                -123.13049,
                49.30013
            ],
            "Distance": 4591,
            "Categories": [
                {
                    "Id": "aquarium",
                    "Name": "Aquarium",
                    "LocalizedName": "Aquarium",
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
    "QueryText": "+1 778-655-9554",
    "BiasPosition": [
        -123.11336,
        49.26038
    ]
}'
```

AWS CLI

```
aws geo-places search-text --key ${`YourKey`} --query-text "+1 778-655-9554" --bias-position -123.11336 49.26038
```

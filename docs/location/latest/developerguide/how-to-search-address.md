# How to search for an address

The `SearchText` API enables you to search for an address.

One way to use the SearchText API is to let end users search for an address and an
application set's bias position. These bias positions can be a device position, IP
position, or a map‘s view port center. Additionally, end users can provide the city name
or place and the application can bias results based on geo-coordinates.

## Potential use cases

- Search for an address based on a bias position.
- Filter results to include or remove specific addresses.

## Examples

Sample request

```
{
    "QueryText":"1368 E 8 Ave Vancouver",
        "BiasPosition":[
                -123.18544,
                49.24643
        ],
     "MaxResults":1
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "1368 E 8th Ave, Vancouver, BC V5N 1T2, Canada",
            "Address": {
                "Label": "1368 E 8th Ave, Vancouver, BC V5N 1T2, Canada",
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
                "District": "Grandview-Woodland",
                "PostalCode": "V5N 1T2",
                "Street": "E 8th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "8th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "E",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "1368"
            },
            "Position": [
                -123.07612,
                49.26306
            ],
            "Distance": 8147,
            "MapView": [
                -123.07752,
                49.26299,
                -123.05661,
                49.26334
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
    "QueryText": "1368 E 8 Ave Vancouver",
    "BiasPosition": [
                -123.18544,
                49.24643
            ],
    "MaxResults": 1
}'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-text "1368 E 8 Ave Vancouver" --bias-position -123.18544 49.24643 --max-results 1
```

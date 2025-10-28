# How to reverse geocode in a

specific language

The feature allows the selection of a preferred response language from
BCP47-compliant codes. It detects the query language based on name variants and uses the
preferred language for unmatched tokens and ambiguous cases. If no requested language,
the **Places** API provides results in the official country language,
but prioritizes the regional language in regions where it differs. As a fallback
strategy, if any address elements are unavailable in the requested language,
**Places** APIs return addresses in the default language.

## Potential use cases

One potential use case is to localize the query and/or the result.

## Examples

Sample request

```
{
    "QueryPosition": [
                139.69172,
                35.6895
            ],
    "Language": "JA"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "2-8-1 Nishishinjuku, Shinjuku-ku, Tokyo 160-0023, Japan",
            "Address": {
                "Label": "2-8-1 Nishishinjuku, Shinjuku-ku, Tokyo 160-0023, Japan",
                "Country": {
                    "Code2": "JP",
                    "Code3": "JPN",
                    "Name": "Japan"
                },
                "Region": {
                    "Name": "Tokyo"
                },
                "SubRegion": {},
                "Locality": "Shinjuku-ku",
                "SubDistrict": "Nishishinjuku",
                "PostalCode": "160-0023",
                "Block": "2 Chome",
                "SubBlock": "8",
                "AddressNumber": "1"
            },
            "Position": [
                139.69171,
                35.68949
            ],
            "Distance": 1,
            "MapView": [
                139.69071,
                35.68861,
                139.69251,
                35.69048
            ],
            "AccessPoints": [
                {
                    "Position": [
                        139.69206,
                        35.68954
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
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/reverse-geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [
                139.69172,
                35.6895
            ],
    "Language": "JA"
}'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position 139.69172 35.6895 --language "JA"
```

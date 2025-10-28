# How to geocode for the time zone of a

city

You can use the Geocode API to provide time zone information such as UTC offset and
time zone name.

## Potential use

Possible uses for geocode time zones:

- Create a world clock
- Schedule meetings in different geographies

## Examples

Geocode in Brussels, with time zone request.

Sample request

```
{
  "QueryText": "Brussels",
  "Filter" : {
        "IncludePlaceTypes": ["Locality"]
    },
    "AdditionalFeatures": [
    "TimeZone"
  ]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "Brussel, België",
            "Address": {
                "Label": "Brussel, België",
                "Country": {
                    "Code2": "BE",
                    "Code3": "BEL",
                    "Name": "België"
                },
                "Region": {
                    "Code": "BRU",
                    "Name": "Brussel"
                },
                "SubRegion": {
                    "Name": "Brussel"
                },
                "Locality": "Brussel",
                "PostalCode": "1000"
            },
            "Position": [
                4.35609,
                50.84439
            ],
            "MapView": [
                4.3139,
                50.79628,
                4.43709,
                50.91397
            ],
            "TimeZone": {
                "Name": "Europe/Brussels",
                "Offset": "+02:00",
                "OffsetSeconds": 7200
            },
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "Brussels",
  "Filter" : {
        "IncludePlaceTypes": ["Locality"]
    },
    "AdditionalFeatures": [
    "TimeZone"
  ]
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "Brussels" \
--filter '{"IncludePlaceTypes": ["Locality"]}' \
--additional-features "TimeZone"
```

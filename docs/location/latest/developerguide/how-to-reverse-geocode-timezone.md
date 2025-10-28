# How to reverse geocode for the time

zone of a city

You can use the Reverse Geocode API to request for time zone information such as UTC
offset and time zone name

## Potential use

Possible uses for geocode time zones:

- Create a world clock
- Schedule meetings in different geographies

## Examples

Reverse geocode a location in Tokyo, with time zone request.

Sample request

```
{
    "QueryPosition": [
        139.69172,
        35.6895
    ],
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
            "PlaceType": "PointAddress",
            "Title": "〒160-0023 東京都新宿区西新宿2丁目8-1",
            "Address": {
                "Label": "〒160-0023 東京都新宿区西新宿2丁目8-1",
                "Country": {
                    "Code2": "JP",
                    "Code3": "JPN",
                    "Name": "日本"
                },
                "Region": {
                    "Name": "東京都"
                },
                "SubRegion": {},
                "Locality": "新宿区",
                "SubDistrict": "西新宿",
                "PostalCode": "160-0023",
                "Block": "2丁目",
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
            ],
            "TimeZone": {
                "Name": "Asia/Tokyo",
                "Offset": "+09:00",
                "OffsetSeconds": 32400
            }
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
    "AdditionalFeatures": [
                "TimeZone"
              ]
}'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position 139.69172 35.6895 --additional-features "TimeZone"
```

# How to reverse geocode with a political

view

The Amazon Location Service allows you to specify a political view to ensure your application aligns
with local regulations. This feature is useful when geocoding locations in disputed
areas where place names or borders may vary depending on the political view.

## Potential Use Cases

**Adhere to local policies:** Ensure that place names
and borders comply with legal requirements of the selected political view.

## Examples

Sample Request

```
{
    "QueryPosition": [
        33.95876,
        45.46824
    ],
    "PoliticalView": "RUS"
}
```

Sample Response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "Первомайский район, Южный федеральный округ, Россия",
            "Address": {
                "Label": "Первомайский район, Южный федеральный округ, Россия",
                "Country": {
                    "Code2": "RU",
                    "Code3": "RUS",
                    "Name": "Россия"
                },
                "Region": {
                    "Name": "Южный федеральный округ"
                },
                "SubRegion": {
                    "Name": "Республика Крым"
                },
                "Locality": "Первомайский район"
            },
            "Position": [
                33.85939,
                45.7142
            ],
            "Distance": 0,
            "MapView": [
                33.52692,
                45.34303,
                34.12277,
                45.80953
            ],
            "PoliticalView": "RUS"
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
        33.95876,
        45.46824
    ],
    "PoliticalView": "RUS"
}'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position 33.95876 45.46824 --political-view "RUS"
```

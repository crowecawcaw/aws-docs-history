# How to reverse geocode for a

position

The Reverse Geocode API allows you to convert a geocode to a geographic area based on
a position query. The API response includes place details, providing information about
the location associated with specific coordinates.

## Potential use cases

- **Store place information:** Add place
  details to a datastore containing geocoordinates.
- **Map visualization:** Use place information
  to display data on a map.
- **User location detection:** Identify the
  user's location based on their device position.

Sample request

```
{
  "QueryPosition": [
    -123.11694,
    49.28126
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
            "Title": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
            "Address": {
                "Label": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
                "Country": { "Code2": "CA", "Code3": "CAN", "Name": "Canada" },
                "Region": { "Code": "BC", "Name": "British Columbia" },
                "SubRegion": { "Name": "Metro Vancouver" },
                "Locality": "Vancouver",
                "District": "Downtown Vancouver",
                "PostalCode": "V6B 0M3",
                "Street": "W Georgia St",
                "StreetComponents": [
                    { "BaseName": "Georgia", "Type": "St", "TypePlacement": "AfterBaseName", "TypeSeparator": " ", "Prefix": "W", "Language": "en" }
                ],
                "AddressNumber": "510"
            },
            "Position": [-123.11694, 49.28126],
            "Distance": 0,
            "MapView": [-123.11813, 49.27786, -123.11076, 49.28246],
            "AccessPoints": [
                { "Position": [-123.11656, 49.28151] }
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
            -123.11694,
            49.28126
        ]
}'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position "-123.11694,49.28126"
```

Sample request

```
{
  "QueryPosition": [
    -123.11694,
    49.28126
  ],
  "MaxResults": "3"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
            "Address": { /* Address details */ },
            "Position": [-123.11694, 49.28126],
            "Distance": 0,
            "MapView": [/* Map view details */],
            "AccessPoints": [/* Access point details */]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "ChargePoint",
            "Address": { /* Address details */ },
            "Position": [-123.11663, 49.28116],
            "Distance": 25,
            "Categories": [/* Category details */],
            "AccessPoints": [/* Access point details */]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Zipcar",
            "Address": { /* Address details */ },
            "Position": [-123.11715, 49.28094],
            "Distance": 29,
            "Categories": [/* Category details */],
            "AccessPoints": [/* Access point details */]
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
            -123.11694,
            49.28126
        ],
        "MaxResults": "3"
}'
```

AWS CLI

```
aws geo-places reverse-geocode --key ${YourKey} --query-position "-123.11694,49.28126" --max-results "3"
```

## Developer tips

For targeted results, use `IncludePlaceTypes` in the filter.

```
{
  "QueryPosition": [
    -123.11694,
    49.28126
  ],
  "Filter": { "IncludePlaceTypes": ["PointAddress"] }
}
```



# How to get administrative address names
<a name="how-to-reverse-geocode-address-names-mode"></a>

Use `AddressNamesMode` set to `Administrative` to return the official administrative names for address components such as the city name. `Administrative` currently applies only to addresses in the United States.

## Potential use cases
<a name="reverse-geocode-address-names-mode-use"></a>
+ **Address standardization:** Normalize city names to their official administrative form for data quality.

## Examples
<a name="reverse-geocode-address-names-mode-example"></a>

### Use Administrative mode
<a name="reverse-geocode-address-names-mode-admin"></a>

------
#### [ Sample request ]

```
{
    "QueryPosition": [-73.985, 40.748],
    "AddressNamesMode": "Administrative"
}
```

------
#### [ Sample response ]

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "350 5th Ave, New York, NY 10118, United States",
            "Address": {
                "Label": "350 5th Ave, New York, NY 10118, United States",
                "Locality": "New York"
            }
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/reverse-geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [-73.985, 40.748],
    "AddressNamesMode": "Administrative"
}'
```

------
#### [ AWS CLI ]

```
aws geo-places reverse-geocode --key ${YourKey} --query-position -73.985 40.748 --address-names-mode Administrative
```

------
# How to control address name variants

`AddressNamesMode` specifies how address names are returned. If not set,
the service returns normalized (official) names by default. When set to
`Matched`, address names in the response are based on the input query
rather than official names. When set to `Administrative`, the service
returns the official administrative names for address components.
`Administrative` currently applies only to addresses in the United
States.

## Potential use cases

- **Address form completion:** Use
  `Matched` to return names consistent with what the user
  typed, reducing confusion in autocomplete workflows.
- **Address standardization:** Use
  `Administrative` to normalize city names to their official
  administrative form for data quality and deduplication.

## Examples

Sample request

```
{
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Matched"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "100 Universal City Plz, Universal City, CA 91608, United States",
            "Address": {
                "Label": "100 Universal City Plz, Universal City, CA 91608, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "CA",
                    "Name": "California"
                },
                "Locality": "Universal City",
                "PostalCode": "91608",
                "Street": "Universal City Plz",
                "AddressNumber": "100"
            },
            "Position": [
                -118.36054,
                34.13857
            ]
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
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Matched"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "100 Universal City Plaza, Hollywood, CA" --address-names-mode Matched
```

Sample request

```
{
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Administrative"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "100 Universal Terrace Pkwy, Los Angeles, CA 91608, United States",
            "Address": {
                "Label": "100 Universal Terrace Pkwy, Los Angeles, CA 91608, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "CA",
                    "Name": "California"
                },
                "Locality": "Los Angeles",
                "PostalCode": "91608",
                "Street": "Universal Terrace Pkwy",
                "AddressNumber": "100"
            },
            "Position": [
                -118.36054,
                34.13857
            ]
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
    "QueryText": "100 Universal City Plaza, Hollywood, CA",
    "AddressNamesMode": "Administrative"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "100 Universal City Plaza, Hollywood, CA" --address-names-mode Administrative
```

## Developer tips

- If not set, the service returns normalized (official) names by
  default.
- `Administrative` currently applies only to addresses in
  the United States.

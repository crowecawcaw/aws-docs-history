# How to get administrative address names

Use the `address-names-mode` query parameter set to
`Administrative` to return official administrative names for address
components. `Administrative` currently applies only to addresses in the
United States.

## Potential use cases

- **Address standardization:** Normalize
  city names to their official administrative form when displaying place
  details.

## Examples

Sample request

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?address-names-mode=Administrative&key=Your_Key
```

Sample response

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointOfInterest",
    "Title": "Empire State Building, New York, NY, United States",
    "Address": {
        "Label": "Empire State Building, 350 5th Ave, New York, NY 10118, United States",
        "Locality": "New York"
    }
}
```

cURL

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?address-names-mode=Administrative&key=Your_Key'
```

AWS CLI

```
aws geo-places get-place --key ${YourKey} --place-id "YourPlaceId" --address-names-mode Administrative
```

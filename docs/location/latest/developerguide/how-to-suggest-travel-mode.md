

# How to get suggestions with travel mode
<a name="how-to-suggest-travel-mode"></a>

Use `TravelMode` in Suggest requests to improve the relevance of place suggestions based on the user's mode of transportation.

## Potential use cases
<a name="suggest-travel-mode-use"></a>
+ **Fleet apps:** Suggest truck-friendly stops and services as drivers type their query.
+ **Ride-sharing:** Prioritize relevant pickup and drop-off locations based on vehicle type.

## Examples
<a name="suggest-travel-mode-example"></a>

### Suggest places for scooter users
<a name="suggest-travel-mode-scooter"></a>

------
#### [ Sample request ]

```
{
    "QueryText": "parking",
    "BiasPosition": [-122.3321, 47.6062],
    "TravelMode": "Scooter"
}
```

------
#### [ Sample response ]

```
{
    "ResultItems": [
        {
            "Title": "Pacific Place Parking, Seattle, WA",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "<Redacted>",
                "PlaceType": "PointOfInterest",
                "Distance": 830
            }
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/suggest?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "parking",
    "BiasPosition": [-122.3321, 47.6062],
    "TravelMode": "Scooter"
}'
```

------
#### [ AWS CLI ]

```
aws geo-places suggest --key ${YourKey} --query-text "parking" --bias-position -122.3321 47.6062 --travel-mode Scooter
```

------

## Developer tips
<a name="suggest-travel-mode-dev-tips"></a>
+ Valid values are `Car`, `Scooter`, and `Truck`.
+ `TravelMode` improves relevance but does not filter results.
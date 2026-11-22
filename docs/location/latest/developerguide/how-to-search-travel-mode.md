

# How to search with travel mode

`TravelMode` indicates your mode of mobility. This improves the relevance of search results. For example, a search for "EV charging station" returns charging stations suitable for trucks when `TravelMode` is set to `Truck`.

## Potential use cases
<a name="search-text-travel-mode-use"></a>
+ **Fleet management:** Find fuel stations or rest stops that accommodate trucks or commercial vehicles.
+ **Navigation apps:** Provide more relevant results based on whether the user is driving a car, riding a scooter, or operating a truck.

## Examples
<a name="search-text-travel-mode-example"></a>

### Search for truck-friendly fuel stations
<a name="search-text-travel-mode-truck"></a>

------
#### [ Sample request ]

```json
{
    "QueryText": "fuel station",
    "BiasPosition": [-122.3321, 47.6062],
    "TravelMode": "Truck"
}
```

------
#### [ Sample response ]

```json
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Pilot Travel Center, Seattle, WA",
            "Distance": 1520
        }
    ]
}
```

------
#### [ cURL ]

```bash
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "fuel station",
    "BiasPosition": [-122.3321, 47.6062],
    "TravelMode": "Truck"
}'
```

------
#### [ AWS CLI ]

```bash
aws geo-places search-text --key ${YourKey} --query-text "fuel station" --bias-position -122.3321 47.6062 --travel-mode Truck
```

------

## Developer tips
<a name="search-text-travel-mode-dev-tips"></a>
+ Valid values are `Car`, `Scooter`, and `Truck`.
+ `TravelMode` improves relevance but does not filter results. Results may still include places that are not specific to the travel mode.
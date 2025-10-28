# How to search nearby places based on food

type

The `SearchNearby` API enables you query nearby restaurants that serve a
specific type of food. You can also exclude food types from your results.

You can use the SearchNearby API to let end users explore neighborhoods and discover
places of interest. The API requires QueryPosition, which can be a device position, IP
position, or a map‘s view port center. Another way is to let end users provide the city
name or place name and the application can bias results based on the
geo-coordinates.

For more information on food types, see [Food Type filters](places-filtering.md#food-type "places-filtering.md#food-type").

## Potential use cases

- Explore types of food available in the vicinity.
- Exclude restaurant options that serve food types to which you're
  allergic.

## Example

The following example demonstrates how to search for nearby places based
on food type.

Sample request
This request searches for restaurants that serve Chinese food
near the specified coordinates.

```
{
    "QueryPosition": [
        12.49563,
        41.90325
    ],
    "Filter": {
        "IncludeFoodTypes": ["chinese"]
    }
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Bufala e Pachino",
            "Address": {
                "Label": "Bufala e Pachino, Via Firenze, 53, 00184 Roma RM, Italia",
                "Country": {
                    "Code2": "IT",
                    "Code3": "ITA",
                    "Name": "Italia"
                }
            },
            "Position": [
                12.49409,
                41.90237
            ],
            "Distance": 161,
            "Categories": [
                {
                    "Id": "restaurant",
                    "Name": "Restaurant",
                    "LocalizedName": "Ristorante",
                    "Primary": true
                }
            ],
            "FoodTypes": [
                {
                    "LocalizedName": "Pizza",
                    "Id": "pizza",
                    "Primary": true
                },
                {
                    "LocalizedName": "Cinese",
                    "Id": "chinese",
                    "Primary": false
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-nearby?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [12.49563, 41.90325],
    "Filter": {
        "IncludeFoodTypes": ["chinese"]
    }
}'
```

AWS CLI

```
aws geo-places search-nearby --key ${YourKey} \
--query-position 12.49563 41.90325 \
--filter '{"IncludeFoodTypes": ["chinese"]}'
```

### Developer Tips

- You can use `ExludeFoodTypes` to exclude certain business
  chains from your results.
- You can exclude or include multiple food types.

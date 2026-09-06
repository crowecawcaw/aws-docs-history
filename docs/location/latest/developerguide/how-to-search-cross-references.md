

# How to get cross-references for places
<a name="how-to-search-cross-references"></a>

`CrossReferences` allows you to retrieve third-party supplier identifiers for places, enabling correlation of places across external systems such as Yelp and TripAdvisor. You must include `CrossReferences` in the `AdditionalFeatures` request parameter.

## Potential use cases
<a name="search-text-cross-references-use"></a>
+ **Data enrichment:** Match places from your database with third-party review platforms to display ratings and reviews.
+ **Cross-platform correlation:** Link place records across multiple systems using shared supplier identifiers.

## Examples
<a name="search-text-cross-references-example"></a>

### Get cross-references for a restaurant
<a name="search-text-cross-references-restaurant"></a>

------
#### [ Sample request ]

```
{
    "QueryText": "Canlis Seattle",
    "BiasPosition": [-122.3321, 47.6062],
    "AdditionalFeatures": ["CrossReferences"]
}
```

------
#### [ Sample response ]

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Canlis, Seattle, WA, United States",
            "CrossReferences": [
                {
                    "Source": "Yelp",
                    "SourcePlaceId": "canlis-seattle",
                    "SourceCategories": [
                        {
                            "Id": "100-1000-0000",
                            "Name": "Restaurant"
                        }
                    ]
                },
                {
                    "Source": "TripAdvisor",
                    "SourcePlaceId": "d590427",
                    "SourceCategories": [
                        {
                            "Id": "100-1000-0000",
                            "Name": "Restaurant"
                        }
                    ]
                }
            ]
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Canlis Seattle",
    "BiasPosition": [-122.3321, 47.6062],
    "AdditionalFeatures": ["CrossReferences"]
}'
```

------
#### [ AWS CLI ]

```
aws geo-places search-text --key ${YourKey} --query-text "Canlis Seattle" --bias-position -122.3321 47.6062 --additional-features CrossReferences
```

------

## Developer tips
<a name="search-text-cross-references-dev-tips"></a>
+ Cross-references are only available for point of interest (POI) results.
+ Not all places have cross-references. The field is omitted when no supplier references are available.
+ The `Source` field contains the name of the third-party supplier, and `SourcePlaceId` contains the identifier used by that supplier.
+ To use the returned identifiers, refer to the supplier's API documentation. For example, see the [Yelp Places API](https://docs.developer.yelp.com/docs/places-intro) on the Yelp website or the [Tripadvisor Content API](https://docs.terra.tripadvisor.com/docs/overview) on the Tripadvisor website.
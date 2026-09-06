

# How to get cross-references for nearby places
<a name="how-to-search-nearby-cross-references"></a>

Include `CrossReferences` in the `AdditionalFeatures` parameter to retrieve third-party supplier identifiers for each nearby place result.

## Potential use cases
<a name="search-nearby-cross-references-use"></a>
+ **Review integration:** Display third-party ratings alongside nearby search results.
+ **Data matching:** Correlate nearby places with records in external databases.

## Examples
<a name="search-nearby-cross-references-example"></a>

### Get cross-references for nearby restaurants
<a name="search-nearby-cross-references"></a>

------
#### [ Sample request ]

```
{
    "QueryPosition": [-122.3321, 47.6062],
    "QueryRadius": 1000,
    "Filter": {
        "IncludeCategories": ["100-1000-0000"]
    },
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
            "Title": "Pike Place Chowder, Seattle, WA",
            "CrossReferences": [
                {
                    "Source": "Yelp",
                    "SourcePlaceId": "pike-place-chowder-seattle"
                }
            ],
            "Distance": 245
        }
    ]
}
```

------
#### [ cURL ]

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-nearby?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryPosition": [-122.3321, 47.6062],
    "QueryRadius": 1000,
    "Filter": {
        "IncludeCategories": ["100-1000-0000"]
    },
    "AdditionalFeatures": ["CrossReferences"]
}'
```

------
#### [ AWS CLI ]

```
aws geo-places search-nearby --key ${YourKey} --query-position -122.3321 47.6062 --query-radius 1000 --filter '{"IncludeCategories": ["100-1000-0000"]}' --additional-features CrossReferences
```

------

## Developer tips
<a name="search-nearby-cross-references-dev-tips"></a>
+ To use the returned identifiers, refer to the supplier's API documentation. For example, see the [Yelp Places API](https://docs.developer.yelp.com/docs/places-intro) on the Yelp website or the [Tripadvisor Content API](https://docs.terra.tripadvisor.com/docs/overview) on the Tripadvisor website.
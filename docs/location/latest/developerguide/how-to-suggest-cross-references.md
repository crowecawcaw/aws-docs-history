# How to get cross-references from suggestions

Include `CrossReferences` in the `AdditionalFeatures` parameter
to retrieve third-party supplier identifiers for place suggestions.

## Potential use cases

- **Preview integration:** Show third-party
  identifiers alongside suggestions before the user selects a place.
- **Pre-fetch reviews:** Use supplier IDs
  to pre-load review data as the user browses suggestions.

## Examples

Sample request

```
{
    "QueryText": "Starbucks downtown",
    "BiasPosition": [-122.3321, 47.6062],
    "AdditionalFeatures": ["CrossReferences"]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "Title": "Starbucks, Seattle, WA",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "<Redacted>",
                "PlaceType": "PointOfInterest",
                "CrossReferences": [
                    {
                        "Source": "Yelp",
                        "SourcePlaceId": "starbucks-seattle-12"
                    }
                ]
            }
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/suggest?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Starbucks downtown",
    "BiasPosition": [-122.3321, 47.6062],
    "AdditionalFeatures": ["CrossReferences"]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} --query-text "Starbucks downtown" --bias-position -122.3321 47.6062 --additional-features CrossReferences
```

## Developer tips

- To use the returned identifiers, refer to the supplier's API
  documentation. For example, see the
  [Yelp
  Places API](https://docs.developer.yelp.com/docs/places-intro "https://docs.developer.yelp.com/docs/places-intro") on the Yelp website or the
  [Tripadvisor
  Content API](https://docs.terra.tripadvisor.com/docs/overview "https://docs.terra.tripadvisor.com/docs/overview") on the Tripadvisor website.

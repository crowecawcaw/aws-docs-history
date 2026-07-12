# How to get cross-references for a place

Use `CrossReferences` in the `AdditionalFeatures` parameter to
retrieve third-party supplier identifiers for a place. This enables you to correlate
the place with entries in external systems such as Yelp and TripAdvisor.

## Potential use cases

- **Review aggregation:** Link a place to its
  profile on review platforms to display user ratings.
- **Data reconciliation:** Match place records
  across your internal systems and third-party databases.

## Examples

Sample request

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?additional-features=CrossReferences&key=Your_Key
```

Sample response

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointOfInterest",
    "Title": "Space Needle, Seattle, WA, United States",
    "CrossReferences": [
        {
            "Source": "TripAdvisor",
            "SourcePlaceId": "d104410",
            "SourceCategories": [
                {
                    "Id": "400-4000-4580",
                    "Name": "Landmark-Attraction"
                }
            ]
        },
        {
            "Source": "Yelp",
            "SourcePlaceId": "space-needle-seattle",
            "SourceCategories": [
                {
                    "Id": "400-4000-4580",
                    "Name": "Landmark-Attraction"
                }
            ]
        }
    ]
}
```

cURL

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/YourPlaceId?key=Your_Key&additional-features=CrossReferences'
```

AWS CLI

```
aws geo-places get-place --key ${YourKey} --place-id "YourPlaceId" --additional-features CrossReferences
```

## Developer tips

- To use the returned identifiers, refer to the supplier's API
  documentation. For example, see the
  [Yelp
  Places API](https://docs.developer.yelp.com/docs/places-intro "https://docs.developer.yelp.com/docs/places-intro") on the Yelp website or the
  [Tripadvisor
  Content API](https://docs.terra.tripadvisor.com/docs/overview "https://docs.terra.tripadvisor.com/docs/overview") on the Tripadvisor website.

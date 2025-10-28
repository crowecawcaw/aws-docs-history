# How to geocode using geospatial

context

The Geocode API enables you to use geospatial context (such as bias position) to get
desired results.

###### Note

"Bias position" refers to a mechanism that prioritizes search results based on a
user's specified location or a defined area. It essentially shifts the focus of
search results towards locations that are geographically closer to a designated bias
point, without necessarily excluding other results.

## Potential use

Use geospatial context to get the correct results based on your business
needs.

## Examples

By biasing to a position, you can change the rankings of your results. Try
the following example, with— and then without—the
`BiasPosition` value and compare the results.

Sample request

```
{
    "QueryText": "George Street",
    "BiasPosition": [
                151.2059,
                -33.8691
            ]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Street",
            "Title": "George St, Sydney NSW, Australia",
            "Address": {
                "Label": "George St, Sydney NSW, Australia",
                "Country": {
                    "Code2": "AU",
                    "Code3": "AUS",
                    "Name": "Australia"
                },
                "Region": {
                    "Code": "NSW",
                    "Name": "New South Wales"
                },
                "Locality": "Sydney",
                "Street": "George St",
                "StreetComponents": [
                    {
                        "BaseName": "George",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ]
            },
            "Position": [
                151.20691,
                -33.86974
            ],
            "Distance": 117,
            "MapView": [
                151.20225,
                -33.88406,
                151.20912,
                -33.85635
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Intersection": [
                            1
                        ]
                    }
                }
            }
        },
        ...
        ...
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/geocode?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "George Street",
    "BiasPosition": [
                151.2059,
                -33.8691
            ]
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "George Street" --bias-position 151.2059 -33.8691
```

## Developer tips

For address geocoding, try to use complete addresses or a query component with a
combination of bias position, including country and place. To learn more, see [How to geocode an address](how-to-geocode-address.md "how-to-geocode-address.md").

# How to geocode using filters

The Geocode API enables you to use filters to get desired results.

## Potential use

Use filters to restrict results based on your business needs.

## Examples

Specify a value for `IncludeCountries` to return values for
that country in the results.

Sample request
Without `IncludeCountries": ["USA"]`, the Geocode
API will return Vancouver, BC, Canada.

```
{
  "QueryText": "Vancouver",
    "Filter" : {
        "IncludeCountries": ["USA"]
    }
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "Vancouver, WA, United States",
            "Address": {
                "Label": "Vancouver, WA, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "WA",
                    "Name": "Washington"
                },
                "SubRegion": {
                    "Name": "Clark"
                },
                "Locality": "Vancouver",
                "PostalCode": "98660"
            },
            "Position": [
                -122.67156,
                45.63248
            ],
            "MapView": [
                -122.77466,
                45.57714,
                -122.46451,
                45.69803
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Locality": 1
                    }
                }
            }
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
  "QueryText": "Vancouver",
    "Filter" : {
        "IncludeCountries": ["USA"]
    }
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "Vancouver" --filter '{"IncludeCountries": ["USA"]}'
```

Specify a value for `IncludePlaceTypes` to return values for
that place in the results.

Sample request
Without `IncludePlaceTypes": ["Street"]`, the
Geocode API will return Georgia, a country. You can further
refine the results by adding `"IncludeCountries"`
with values of **CAN** and
**USA** and compare the results.

```
{
  "QueryText": "Georgia",
    "Filter" : {
        "IncludePlaceTypes": ["Street"]
    }

}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Street",
            "Title": "Georgia, Benito Juárez, CDMX, México",
            "Address": {
                "Label": "Georgia, Benito Juárez, CDMX, México",
                "Country": {
                    "Code2": "MX",
                    "Code3": "MEX",
                    "Name": "México"
                },
                "Region": {
                    "Code": "CDMX",
                    "Name": "Ciudad de México"
                },
                "SubRegion": {
                    "Name": "Ciudad de México"
                },
                "Locality": "Benito Juárez",
                "Street": "Georgia",
                "StreetComponents": [
                    {
                        "BaseName": "Georgia",
                        "Language": "es"
                    }
                ]
            },
            "Position": [
                -99.17754,
                19.38887
            ],
            "MapView": [
                -99.18133,
                19.38755,
                -99.17374,
                19.39016
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
  "QueryText": "Georgia",
    "Filter" : {
        "IncludePlaceTypes": ["Street"]
    }

}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "Georgia" --filter '{"IncludePlaceTypes": ["Street"]}'
```

## Developer tips

For address geocoding, try to use complete addresses or a query component with a
combination of bias position, including country and place. To learn more, see [How to geocode an address](how-to-geocode-address.md "how-to-geocode-address.md").

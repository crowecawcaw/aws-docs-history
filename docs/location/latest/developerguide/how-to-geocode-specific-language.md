# How to geocode in a specific

language

This feature allows the selection of a preferred response language from
BCP47-compliant codes. It detects the query language based on name variants and uses the
preferred language for unmatched tokens and ambiguous cases. If there is no requested
language, the **Places** API provides results in the official country
language, but prioritizes the regional language in regions where it differs. As a
fallback strategy, if any address elements are unavailable in the requested language,
**Places** APIs return addresses in the default language.

## Potential use cases

One potential use case is to localize the query and/or the result.

## Examples

Sample request

```
{
    "QueryText":"Patna, Bihar, Bharat",
    "Language": "HI"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "पटना, बिहार, भारत",
            "Address": {
                "Label": "पटना, बिहार, भारत",
                "Country": {
                    "Code2": "IN",
                    "Code3": "IND",
                    "Name": "भारत"
                },
                "Region": {
                    "Code": "BR",
                    "Name": "बिहार"
                },
                "SubRegion": {
                    "Name": "पटना"
                },
                "Locality": "पटना",
                "PostalCode": "800001"
            },
            "Position": [
                85.13752,
                25.60134
            ],
            "MapView": [
                85.03222,
                25.55157,
                85.27107,
                25.65917
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Country": 1,
                        "Region": 1,
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
    "QueryText":"Patna, Bihar, Bharat",
    "Language": "HI"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "पटना, बिहार, भारत" --language "HI"
```

Sample request

```
{
    "QueryText":"पटना, बिहार, भारत"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "Patana, Bihar, Bharat",
            "Address": {
                "Label": "Patana, Bihar, Bharat",
                "Country": {
                    "Code2": "IN",
                    "Code3": "IND",
                    "Name": "Bharat"
                },
                "Region": {
                    "Code": "BR",
                    "Name": "Bihar"
                },
                "SubRegion": {
                    "Name": "Patana"
                },
                "Locality": "Patana",
                "PostalCode": "800001"
            },
            "Position": [
                85.13752,
                25.60134
            ],
            "MapView": [
                85.03222,
                25.55157,
                85.27107,
                25.65917
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Country": 1,
                        "Region": 1,
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
    "QueryText":"पटना, बिहार, भारत"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "पटना, बिहार, भारत"
```

Sample request

```
{
    "QueryText":"पटना, बिहार, भारत",
    "Language": "HI"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "पटना, बिहार, भारत",
            "Address": {
                "Label": "पटना, बिहार, भारत",
                "Country": {
                    "Code2": "IN",
                    "Code3": "IND",
                    "Name": "भारत"
                },
                "Region": {
                    "Code": "BR",
                    "Name": "बिहार"
                },
                "SubRegion": {
                    "Name": "पटना"
                },
                "Locality": "पटना",
                "PostalCode": "800001"
            },
            "Position": [
                85.13752,
                25.60134
            ],
            "MapView": [
                85.03222,
                25.55157,
                85.27107,
                25.65917
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Country": 1,
                        "Region": 1,
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
    "QueryText":"पटना, बिहार, भारत",
    "Language": "HI"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "पटना, बिहार, भारत" --language "HI"
```

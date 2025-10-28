# How to complete an address

The Autocomplete API enables you to complete partially typed addresses, providing
standardized input for end users and improving efficiency during data entry.

## Potential use cases

- **Complete an address during checkout:**
  Facilitate accurate and fast address input as customers type into a checkout
  form.
- **Country-specific address completion:**
  Restrict suggestions to a specific country for compliance or relevance to
  the user’s location.

## Examples

In this example, minimal data is returned to keep the response concise and
cost-effective. Complete place details can be retrieved later using the
PlaceId with the GetPlace API.

Sample request

```
{
  "QueryText": "100 McCullum Rd"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "United Kingdom, E3 5JB, London, 100 McCullum Road"
        }
    ],
    "QueryRefinements": []
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/autocomplete?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "100 McCullum Rd"
}'
```

AWS CLI

```
aws geo-places autocomplete --key ${YourKey} --query-text "100 McCullum Rd"
```

This example returns multiple address suggestions, allowing users to
select a standardized address format for populating form fields
accurately.

Sample request

```
{
  "QueryText": "100 McCullum Rd",
  "AdditionalFeatures": [
    "Core"
  ]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "United Kingdom, E3 5JB, London, 100 McCullum Road",
            "Address": {
                "Label": "100 McCullum Road, London, E3 5JB, United Kingdom",
                "Country": {
                    "Code2": "GB",
                    "Code3": "GBR",
                    "Name": "United Kingdom"
                },
                "Region": {
                    "Name": "England"
                },
                "SubRegion": {
                    "Code": "LDN",
                    "Name": "London"
                },
                "Locality": "London",
                "District": "Bow",
                "PostalCode": "E3 5JB",
                "Street": "McCullum Road",
                "StreetComponents": [
                    {
                        "BaseName": "McCullum",
                        "Type": "Road",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "100"
            },
            "Language": "en",
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 32,
                        "EndIndex": 35,
                        "Value": "100"
                    },
                    {
                        "StartIndex": 36,
                        "EndIndex": 49,
                        "Value": "McCullum Road"
                    }
                ],
                "Address": {
                    "Label": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 3,
                            "Value": "100"
                        },
                        {
                            "StartIndex": 4,
                            "EndIndex": 17,
                            "Value": "McCullum Road"
                        }
                    ],
                    "Street": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 13,
                            "Value": "McCullum Road"
                        }
                    ],
                    "AddressNumber": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 3,
                            "Value": "100"
                        }
                    ]
                }
            }
        },
        ...
    ],
    "QueryRefinements": []
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/autocomplete?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "100 McCullum Rd",
  "AdditionalFeatures": [
    "Core"
  ]
}'
```

AWS CLI

```
aws geo-places autocomplete --key ${YourKey} --query-text "100 McCullum Rd" --additional-features "Core"
```

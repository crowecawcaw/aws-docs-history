# How to complete an address with

filters

The Autocomplete API enables you to complete partially typed addresses, facilitating
quick and standardized address input for end users. By using the
`AdditionalFeatures` parameter, you can customize the information
provided in the response to meet specific requirements.

## Potential use cases

- **Minimize data for cost efficiency:** Reduce
  response size and data transfer costs by requesting only essential address
  components when a follow-up query is anticipated.
- **Include necessary details for direct use:**
  Retrieve comprehensive address information to eliminate the need for
  additional queries.

## Examples

This example applies a country filter to refine results, enabling a
standardized form of the user-inputted address to populate form fields
accurately.

Sample request

```
{
  "QueryText": "100 McCullum Rd",
  "Filter": {
    "IncludeCountries": [
      "GBR"
    ]
  }
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
  "QueryText": "100 McCullum Rd",
  "Filter": {
    "IncludeCountries": [
      "GBR"
    ]
  }
}'
```

AWS CLI

```
aws geo-places autocomplete --key ${YourKey} --query-text "100 McCullum Rd" \
--filter '{"IncludeCountries": ["GBR"]}'
```

This example returns additional data, allowing the returned address
details to be used without a follow-up query. The `Core` set of
additional features is sufficient for this use case.

Sample request

```
{
  "QueryText": "100 McCullum Rd",
  "Filter": {
    "IncludeCountries": [
      "GBR"
    ]
  },
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
  "QueryText": "100 McCullum Rd",
  "Filter": {
    "IncludeCountries": [
      "GBR"
    ]
  },
  "AdditionalFeatures": [
    "Core"
  ]
}'
```

AWS CLI

```
aws geo-places autocomplete --key ${YourKey} --query-text "100 McCullum Rd" \
--additional-features "Core" \
--filter '{"IncludeCountries": ["GBR"]}'
```

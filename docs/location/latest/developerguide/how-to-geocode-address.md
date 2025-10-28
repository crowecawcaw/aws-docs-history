# How to geocode an address

The Geocode API enables you to geocode a specific point address, interpolated address,
or street. The API response contains location information, including geographical
coordinates and match scores that i ndicate how accurately the result aligns with the
query.

## Potential use cases

- **Clean address database:** Enhance data
  quality by identifying and correcting errors in address records.
- **Normalize and standardize addresses:**
  Ensure consistent address formatting across datasets for improved data
  interoperability.
- **Enrich addresses with additional
  information:** Add geographic coordinates and other relevant
  details to address records to support location-based analytics and
  insights.

## Examples

Sample request

```
{
  "QueryText": "510 W Georgia St, Vancouver, BC"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
            "Address": {
                "Label": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
                "Country": {
                    "Code2": "CA",
                    "Code3": "CAN",
                    "Name": "Canada"
                },
                "Region": {
                    "Code": "BC",
                    "Name": "British Columbia"
                },
                "SubRegion": {
                    "Name": "Metro Vancouver"
                },
                "Locality": "Vancouver",
                "District": "Downtown Vancouver",
                "PostalCode": "V6B 0M3",
                "Street": "W Georgia St",
                "StreetComponents": [
                    {
                        "BaseName": "Georgia",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "510"
            },
            "Position": [
                -123.11694,
                49.28126
            ],
            "MapView": [
                -123.11832,
                49.28036,
                -123.11556,
                49.28216
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.11656,
                        49.28151
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Region": 1,
                        "Locality": 1,
                        "Intersection": [
                            1
                        ],
                        "AddressNumber": 1
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
  --data '{"QueryText": "510 W Georgia St, Vancouver, BC"}'
```

AWS CLI

```
aws geo-places geocode --key ${`YourAPIKey`} --query-text "510 W Georgia St, Vancouver, BC"
```

Sample request

```
{
  "QueryComponents": {
    "AddressNumber": "510",
    "Locality": "Vancouver",
    "Region": "BC",
    "Country": "Canada",
    "Street": "Georgia"
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
            "Title": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
            "Address": {
                "Label": "510 W Georgia St, Vancouver, BC V6B 0M3, Canada",
                "Country": {
                    "Code2": "CA",
                    "Code3": "CAN",
                    "Name": "Canada"
                },
                "Region": {
                    "Code": "BC",
                    "Name": "British Columbia"
                },
                "SubRegion": {
                    "Name": "Metro Vancouver"
                },
                "Locality": "Vancouver",
                "District": "Downtown Vancouver",
                "PostalCode": "V6B 0M3",
                "Street": "W Georgia St",
                "StreetComponents": [
                    {
                        "BaseName": "Georgia",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "510"
            },
            "Position": [
                -123.11694,
                49.28126
            ],
            "MapView": [
                -123.11832,
                49.28036,
                -123.11556,
                49.28216
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.11656,
                        49.28151
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 0.99,
                "Components": {
                    "Address": {
                        "Country": 1,
                        "Region": 1,
                        "Locality": 1,
                        "Intersection": [
                            0.78
                        ],
                        "AddressNumber": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "InterpolatedAddress",
            "Title": "510 E Georgia St, Vancouver, BC V6A 1Z9, Canada",
            "Address": {
                "Label": "510 E Georgia St, Vancouver, BC V6A 1Z9, Canada",
                "Country": {
                    "Code2": "CA",
                    "Code3": "CAN",
                    "Name": "Canada"
                },
                "Region": {
                    "Code": "BC",
                    "Name": "British Columbia"
                },
                "SubRegion": {
                    "Name": "Metro Vancouver"
                },
                "Locality": "Vancouver",
                "District": "Strathcona",
                "PostalCode": "V6A 1Z9",
                "Street": "E Georgia St",
                "StreetComponents": [
                    {
                        "BaseName": "Georgia",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "E",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "510"
            },
            "Position": [
                -123.0932,
                49.27829
            ],
            "MapView": [
                -123.09458,
                49.27739,
                -123.09182,
                49.27919
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.0932,
                        49.27842
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 0.99,
                "Components": {
                    "Address": {
                        "Country": 1,
                        "Region": 1,
                        "Locality": 1,
                        "Intersection": [
                            0.78
                        ],
                        "AddressNumber": 1
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
  --data '{"QueryComponents": {"AddressNumber": "510", "Locality": "Vancouver", "Region": "BC", "Country": "Canada", "Street": "Georgia"}}'
```

AWS CLI

```
./aws geo-places geocode --key ${`YourAPIKey`} --query-components '{
"AddressNumber" : "510",
"Locality": "vancouver",
"Region": "BC",
"Country": "Canada",
"Street": "Georgia"}'
```

Sample request

```
{
  "QueryText": "W. 6th St",
  "QueryComponents": {
    "AddressNumber": "415",
    "Locality": "Vancouver"
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
            "Title": "415 W 6th St, Vancouver, WA 98660-3375, United States",
            "Address": {
                "Label": "415 W 6th St, Vancouver, WA 98660-3375, United States",
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
                "District": "Esther Short",
                "PostalCode": "98660-3375",
                "Street": "W 6th St",
                "StreetComponents": [
                    {
                        "BaseName": "6th",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "415"
            },
            "Position": [
                -122.67543,
                45.62527
            ],
            "MapView": [
                -122.67672,
                45.62437,
                -122.67414,
                45.62617
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.67543,
                        45.62506
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Locality": 1,
                        "Intersection": [
                            1
                        ],
                        "AddressNumber": 1
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
  --data '{"QueryText": "W. 6th St", "QueryComponents": {"AddressNumber": "415", "Locality": "Vancouver"}}'
```

AWS CLI

```
./aws geo-places geocode -key ${`YourAPIKey`} --query-text "W. 6th St" \
--query-components '{"AddressNumber" : "415", "Locality": "Vancouver"}'
```

## Developer Tips

Use filters like `IncludeCountries` and `IncludePlaceTypes` to obtain accurate results. For instance, if you need Vancouver from the USA, apply `"IncludeCountries": ["USA"]` to prioritize results in the USA.
To learn more, see [How to geocode using filters](how-to-geocode-filters.md "how-to-geocode-filters.md").

```
{
  "QueryText": "Vancouver",
  "Filter": {
    "IncludeCountries": ["USA"],
    "IncludePlaceTypes": ["City"]
  }
}
```

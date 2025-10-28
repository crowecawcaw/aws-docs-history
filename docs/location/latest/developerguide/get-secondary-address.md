# How to get secondary addresses

`SecondaryAddresses` allows you to retrieve all secondary addresses that
are under a main address. Additionally, `Geocode` also returns secondary
units, if any are present within the `QueryText`.

## Potential use cases

- **Address form completion:** To select a more
  accurate secondary address, which also includes more accurate positional
  information.
- **Deliveries:** For countries that lack
  secondary address coverage, this information can help inform deliveries by
  including all provided unit information.

## Examples

###### Note

Coverage for `Address.SecondaryAddressComponents` is
available in the following countries:

AUS, CAN, NZL, USA, PRI

Coverage for
`ParsedQuery.Address.SecondaryAddressComponents` is
available in the following countries:

AUS, AUT, BRA, CAN, ESP, FRA, GBR, IDN, IND, NZL, TUR, TWN, USA

Sample request

```
{
    "QueryText":"910 Beach Avenue, Vancouver",
    "AdditionalFeatures": ["SecondaryAddresses"]
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
            "Address": {
                "Label": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
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
                "PostalCode": "V6Z 2W7",
                "Street": "Beach Ave",
                "StreetComponents": [
                    {
                        "BaseName": "Beach",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "910"
            },
            "Position": [
                -123.13325,
                49.27542
            ],
            "MapView": [
                -123.13463,
                49.27452,
                -123.13187,
                49.27632
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
            },
            "ParsedQuery": {
                "Address": {
                    "Locality": [
                        {
                            "StartIndex": 18,
                            "EndIndex": 27,
                            "Value": "Vancouver",
                            "QueryComponent": "Query"
                        }
                    ],
                    "Street": [
                        {
                            "StartIndex": 4,
                            "EndIndex": 16,
                            "Value": "Beach Avenue",
                            "QueryComponent": "Query"
                        }
                    ],
                    "AddressNumber": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 3,
                            "Value": "910",
                            "QueryComponent": "Query"
                        }
                    ]
                }
            },
            "SecondaryAddresses": [
                {
                    "PlaceId": "<Redacted>",
                    "PlaceType": "SecondaryAddress",
                    "Title": "101-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                    "Address": {
                        "Label": "101-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                        "SecondaryAddressComponents": [
                            {
                                "Number": "101"
                            }
                        ]
                    },
                    "Position": [
                        -123.1334,
                        49.27532
                    ]
                },
                {
                    "PlaceId": "<Redacted>",
                    "PlaceType": "SecondaryAddress",
                    "Title": "102-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                    "Address": {
                        "Label": "102-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                        "SecondaryAddressComponents": [
                            {
                                "Number": "102"
                            }
                        ]
                    },
                    "Position": [
                        -123.1334,
                        49.27532
                    ]
                },
                ...
             ]
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
    "QueryText":"910 Beach Avenue, Vancouver",
    "AdditionalFeatures": ["SecondaryAddresses"]
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "910 Beach Avenue, Vancouver" --additional-features "SecondaryAddresses"
```

Coverage for this functionality is available in the following countries:
AUS, AUT, BRA, CAN, ESP, FRA, GBR, IDN, IND, NZL, TUR, TWN, USA.

Sample request

```
{
  "QueryText": "101-910 Beach Avenue, Vancouver"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "SecondaryAddress",
            "Title": "101-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
            "Address": {
                "Label": "101-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
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
                "PostalCode": "V6Z 2W7",
                "Street": "Beach Ave",
                "StreetComponents": [
                    {
                        "BaseName": "Beach",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "910",
                "SecondaryAddressComponents": [
                    {
                        "Number": "101"
                    }
                ]
            },
            "Position": [
                -123.1334,
                49.27532
            ],
            "MapView": [
                -123.13478,
                49.27442,
                -123.13202,
                49.27622
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "Locality": 1,
                        "Intersection": [
                            1
                        ],
                        "AddressNumber": 1,
                        "SecondaryAddressComponents": [
                            {
                                "Number": 1
                            }
                        ]
                    }
                }
            },
            "ParsedQuery": {
                "Address": {
                    "Locality": [
                        {
                            "StartIndex": 22,
                            "EndIndex": 31,
                            "Value": "Vancouver",
                            "QueryComponent": "Query"
                        }
                    ],
                    "Street": [
                        {
                            "StartIndex": 8,
                            "EndIndex": 20,
                            "Value": "Beach Avenue",
                            "QueryComponent": "Query"
                        }
                    ],
                    "AddressNumber": [
                        {
                            "StartIndex": 4,
                            "EndIndex": 7,
                            "Value": "910",
                            "QueryComponent": "Query"
                        }
                    ],
                    "SecondaryAddressComponents": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 3,
                            "Value": "101",
                            "Number": "101",
                            "Designator": "unknown"
                        }
                    ]
                }
            },
            "MainAddress": {
                "PlaceId": "<Redacted>",
                "PlaceType": "PointAddress",
                "Title": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                "Address": {
                    "Label": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada"
                },
                "Position": [
                    -123.13325,
                    49.27542
                ]
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
    "QueryText":"101-910 Beach Avenue, Vancouver"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "101-910 Beach Avenue, Vancouver"
```

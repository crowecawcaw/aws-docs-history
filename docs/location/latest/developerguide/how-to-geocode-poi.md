# How to geocode a point of interest

You can use the geocode API to geocode the coordinates of a known place (Point of
interest) such as business addresses, landmark, or tourist spot. The API response
contains location information, including geographical coordinates, and match scores that
indicate how well the result matches the query.

## Potential use cases

- Provide geographical coordinates that correspond to points of interest
  enhances the user experience
- Provide geographical coordinates that correspond to points of interest can
  optimize logistics

## Examples

Sample request

```
{
    "QueryText": "Starbucks , Vancouver"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 1099 Robson St, Vancouver, BC V6E 1A9, Canada",
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
                "District": "West End",
                "PostalCode": "V6E 1A9",
                "Street": "Robson St",
                "StreetComponents": [
                    {
                        "BaseName": "Robson",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "1099"
            },
            "Position": [
                -123.12454,
                49.28462
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.12463,
                        49.28447
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 980 Seymour St, Vancouver, BC V6B 1B5, Canada",
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
                "PostalCode": "V6B 1B5",
                "Street": "Seymour St",
                "StreetComponents": [
                    {
                        "BaseName": "Seymour",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "980"
            },
            "Position": [
                -123.12142,
                49.2786
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.12185,
                        49.27873
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 918 SE 164th Ave, Vancouver, WA 98683-9603, United States",
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
                "District": "Cascade Highlands",
                "PostalCode": "98683-9603",
                "Street": "SE 164th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "164th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "SE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "918"
            },
            "Position": [
                -122.50495,
                45.61409
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.50493,
                        45.61401
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 304 W 8th St, Vancouver, WA 98660-3112, United States",
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
                "PostalCode": "98660-3112",
                "Street": "W 8th St",
                "StreetComponents": [
                    {
                        "BaseName": "8th",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "304"
            },
            "Position": [
                -122.67418,
                45.6274
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.67419,
                        45.62725
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 3707 Main St, Vancouver, WA 98663-2227, United States",
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
                "District": "Shumway",
                "PostalCode": "98663-2227",
                "Street": "Main St",
                "StreetComponents": [
                    {
                        "BaseName": "Main",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "3707"
            },
            "Position": [
                -122.667,
                45.64849
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.66705,
                        45.64849
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 2811 E Fourth Plain Blvd, Vancouver, WA 98661, United States",
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
                "District": "Rose Village",
                "PostalCode": "98661",
                "Street": "E Fourth Plain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Fourth Plain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "E",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "2811"
            },
            "Position": [
                -122.64149,
                45.63818
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.64185,
                        45.63828
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 2500 Columbia House Blvd, Vancouver, WA 98661-7758, United States",
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
                "District": "Hudson Bay",
                "PostalCode": "98661-7758",
                "Street": "Columbia House Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Columbia House",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "2500"
            },
            "Position": [
                -122.64584,
                45.62036
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.64584,
                        45.61986
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 8801 NE Hazel Dell Ave, Vancouver, WA 98665-8145, United States",
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
                "District": "Northeast Hazel Dell-Starcrest",
                "PostalCode": "98665-8145",
                "Street": "NE Hazel Dell Ave",
                "StreetComponents": [
                    {
                        "BaseName": "Hazel Dell",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "8801"
            },
            "Position": [
                -122.66834,
                45.68623
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.66834,
                        45.68641
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 7720 NE Highway 99, Vancouver, WA 98665, United States",
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
                "District": "Northeast Hazel Dell",
                "PostalCode": "98665",
                "Street": "NE Highway 99",
                "StreetComponents": [
                    {
                        "BaseName": "Highway 99",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "7720"
            },
            "Position": [
                -122.66264,
                45.67787
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.66293,
                        45.67793
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 408 NE 81st St, Vancouver, WA 98665-8111, United States",
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
                "District": "Northeast Hazel Dell-Starcrest",
                "PostalCode": "98665-8111",
                "Street": "NE 81st St",
                "StreetComponents": [
                    {
                        "BaseName": "81st",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "408"
            },
            "Position": [
                -122.66824,
                45.68161
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.66824,
                        45.68138
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 6701 E Mill Plain Blvd, Vancouver, WA 98661-7459, United States",
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
                "District": "Vancouver Heights",
                "PostalCode": "98661-7459",
                "Street": "E Mill Plain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Mill Plain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "E",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "6701"
            },
            "Position": [
                -122.6031,
                45.62623
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.6031,
                        45.62635
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 8700 NE Vancouver Mall Dr, Vancouver, WA 98662-6416, United States",
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
                "PostalCode": "98662-6416",
                "Street": "NE Vancouver Mall Dr",
                "StreetComponents": [
                    {
                        "BaseName": "Vancouver Mall",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "8700"
            },
            "Position": [
                -122.58543,
                45.65786
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.58512,
                        45.65739
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 8302 E Mill Plain Blvd, Vancouver, WA 98664-2007, United States",
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
                "District": "North Garrison Heights",
                "PostalCode": "98664-2007",
                "Street": "E Mill Plain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Mill Plain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "E",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "8302"
            },
            "Position": [
                -122.58719,
                45.62393
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.58712,
                        45.62393
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 7809 NE Vancouver Plaza Dr, Vancouver, WA 98662-6624, United States",
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
                "District": "Ogden",
                "PostalCode": "98662-6624",
                "Street": "NE Vancouver Plaza Dr",
                "StreetComponents": [
                    {
                        "BaseName": "Vancouver Plaza",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "7809"
            },
            "Position": [
                -122.5919,
                45.65126
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.59217,
                        45.65112
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 2615 NE 112th Ave, Vancouver, WA 98684-4283, United States",
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
                "District": "Landover-Sharmel",
                "PostalCode": "98684-4283",
                "Street": "NE 112th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "112th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "2615"
            },
            "Position": [
                -122.55675,
                45.64148
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.55675,
                        45.64157
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 13719 SE Mill Plain Blvd, Vancouver, WA 98684-6945, United States",
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
                "District": "Mountain View",
                "PostalCode": "98684-6945",
                "Street": "SE Mill Plain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Mill Plain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "SE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "13719"
            },
            "Position": [
                -122.53093,
                45.61691
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.53093,
                        45.61714
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 6711 NE 63rd St, Vancouver, WA 98661-1997, United States",
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
                "District": "Walnut Grove",
                "PostalCode": "98661-1997",
                "Street": "NE 63rd St",
                "StreetComponents": [
                    {
                        "BaseName": "63rd",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "6711"
            },
            "Position": [
                -122.60365,
                45.66671
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.60365,
                        45.66679
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 8720 NE Centerpointe Dr, Vancouver, WA 98665-1153, United States",
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
                "District": "Sunnyside-Walnut Grove",
                "PostalCode": "98665-1153",
                "Street": "NE Centerpointe Dr",
                "StreetComponents": [
                    {
                        "BaseName": "Centerpointe",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "8720"
            },
            "Position": [
                -122.6019,
                45.68537
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.60189,
                        45.6852
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 7411 NE 117th Ave, Vancouver, WA 98662-4705, United States",
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
                "District": "Orchards Area",
                "PostalCode": "98662-4705",
                "Street": "NE 117th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "117th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "7411"
            },
            "Position": [
                -122.55103,
                45.67666
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.55103,
                        45.67684
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "STARBUCKS",
            "Address": {
                "Label": "STARBUCKS, 11211 NE Fourth Plain Blvd, Vancouver, WA 98662-5770, United States",
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
                "District": "Orchards Area",
                "PostalCode": "98662-5770",
                "Street": "NE Fourth Plain Blvd",
                "StreetComponents": [
                    {
                        "BaseName": "Fourth Plain",
                        "Type": "Blvd",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "11211"
            },
            "Position": [
                -122.5575,
                45.66574
            ],
            "Categories": [
                {
                    "Id": "coffee_shop",
                    "Name": "Coffee Shop",
                    "LocalizedName": "Coffee Shop",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.55751,
                        45.66587
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
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
    "QueryText": "Starbucks , Vancouver"
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "Starbucks , Vancouver"
```

Sample request

```
{
    "QueryText": "Eiffel Tower, Paris"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "The Eiffel Tower Romance",
            "Address": {
                "Label": "The Eiffel Tower Romance, Rue de Rivoli, 75004 Paris, France",
                "Country": {
                    "Code2": "FR",
                    "Code3": "FRA",
                    "Name": "France"
                },
                "Region": {
                    "Code": "IDF",
                    "Name": "Île-de-France"
                },
                "SubRegion": {
                    "Name": "Paris"
                },
                "Locality": "Paris",
                "District": "4e Arrondissement",
                "PostalCode": "75004",
                "Street": "Rue de Rivoli",
                "StreetComponents": [
                    {
                        "BaseName": "Rivoli",
                        "Type": "Rue de",
                        "TypePlacement": "BeforeBaseName",
                        "TypeSeparator": " ",
                        "Language": "fr"
                    }
                ]
            },
            "Position": [
                2.35284,
                48.85702
            ],
            "Categories": [
                {
                    "Id": "theatre,_music_and_culture",
                    "Name": "Theatre, Music and Culture",
                    "LocalizedName": "Théâtre, musique et culture",
                    "Primary": true
                },
                {
                    "Id": "historical_monument",
                    "Name": "Historical Monument",
                    "LocalizedName": "Monument historique",
                    "Primary": false
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        2.3529,
                        48.85714
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Eiffel Tower",
            "Address": {
                "Label": "Eiffel Tower, 2025 S Collegiate Dr, Paris, TX 75460-7853, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "TX",
                    "Name": "Texas"
                },
                "SubRegion": {
                    "Name": "Lamar"
                },
                "Locality": "Paris",
                "PostalCode": "75460-7853",
                "Street": "S Collegiate Dr",
                "StreetComponents": [
                    {
                        "BaseName": "Collegiate",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "S",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "2025"
            },
            "Position": [
                -95.52403,
                33.64055
            ],
            "Categories": [
                {
                    "Id": "historical_monument",
                    "Name": "Historical Monument",
                    "LocalizedName": "Historical Monument",
                    "Primary": true
                },
                {
                    "Id": "landmark-attraction",
                    "Name": "Landmark-Attraction",
                    "LocalizedName": "Landmark-Attraction",
                    "Primary": false
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -95.52411,
                        33.6405
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
                    "Address": {
                        "Locality": 1
                    }
                }
            }
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Eiffel Tower",
            "Address": {
                "Label": "Eiffel Tower, Northland Dr, Paris, MI 49338, United States",
                "Country": {
                    "Code2": "US",
                    "Code3": "USA",
                    "Name": "United States"
                },
                "Region": {
                    "Code": "MI",
                    "Name": "Michigan"
                },
                "SubRegion": {
                    "Name": "Mecosta"
                },
                "Locality": "Paris",
                "PostalCode": "49338",
                "Street": "Northland Dr",
                "StreetComponents": [
                    {
                        "BaseName": "Northland",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ]
            },
            "Position": [
                -85.50268,
                43.78907
            ],
            "Categories": [
                {
                    "Id": "outdoor-recreation",
                    "Name": "Outdoor-Recreation",
                    "LocalizedName": "Outdoor/Recreation",
                    "Primary": true
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -85.50282,
                        43.78907
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Title": 1,
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
    "QueryText": "Eiffel Tower, Paris"
    }'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-text "Eiffel Tower, Paris"
```

## Developer tips

- Use complete addresses or query component for better results. To learn
  more, see [How to geocode an address](how-to-geocode-address.md "how-to-geocode-address.md").
- Use filters like `IncludeCountries` and `IncludePlaceTypes` to obtain accurate results. For instance, if you need Vancouver from the USA, apply `"IncludeCountries": ["USA"]` to prioritize results in the USA.
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

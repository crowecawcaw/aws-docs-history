# How to search places using query ID

The `SearchText` API enables you get details of the query result returned
by [Suggest](suggest.md "suggest.md").

## Potential use cases

Get search results for Query ID, which are returned by the `Suggestion`
API.

## Examples

Sample request

```
{
    "QueryId": "<Redacted>"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Restore",
            "Address": {
                "Label": "Restore, 400 Urban Plz, Kirkland, WA 98033, United States",
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
                    "Name": "King"
                },
                "Locality": "Kirkland",
                "District": "Moss Bay",
                "PostalCode": "98033",
                "Street": "Urban Plz",
                "StreetComponents": [
                    {
                        "BaseName": "Urban",
                        "Type": "Plz",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "400"
            },
            "Position": [
                -122.19958,
                47.67822
            ],
            "Distance": 190670,
            "Categories": [
                {
                    "Id": "wellness_center_and_services",
                    "Name": "Wellness Center and Services",
                    "LocalizedName": "Wellness Center & Services",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "Restore",
                    "Id": "Restore"
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+14258352271"
                    },
                    {
                        "Value": "+14254205116"
                    }
                ],
                "Websites": [
                    {
                        "Value": "https://restore.com"
                    },
                    {
                        "Value": "https://restore.com/locations"
                    },
                    {
                        "Value": "https://www.facebook.com/rhwkirkland"
                    },
                    {
                        "Value": "https://www.restore.com/locations/wa-kirkland-wa001?utm_source=extnet&utm_medium=Yext&y_source=1_MzE2Mjk5NTgtNTY2LWxvY2F0aW9uLndlYnNpdGU%3D"
                    },
                    {
                        "Value": "https://www.restore.com/sitemap.xml"
                    }
                ],
                "Emails": [
                    {
                        "Value": "kirkland@restore.com"
                    }
                ]
            },
            "OpeningHours": [
                {
                    "Display": [
                        "Mon-Thu: 10:00 - 19:00",
                        "Fri: 10:00 - 17:00",
                        "Sat: 09:00 - 17:00",
                        "Sun: 10:00 - 16:00"
                    ],
                    "OpenNow": false,
                    "Components": [
                        {
                            "OpenTime": "T100000",
                            "OpenDuration": "PT09H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH"
                        },
                        {
                            "OpenTime": "T100000",
                            "OpenDuration": "PT07H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:FR"
                        },
                        {
                            "OpenTime": "T090000",
                            "OpenDuration": "PT08H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:SA"
                        },
                        {
                            "OpenTime": "T100000",
                            "OpenDuration": "PT06H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:SU"
                        }
                    ]
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.19944,
                        47.67801
                    ]
                }
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Restore",
            "Address": {
                "Label": "Restore, 1520 Highlands Dr NE, Issaquah, WA 98029, United States",
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
                    "Name": "King"
                },
                "Locality": "Issaquah",
                "District": "Issaquah Highlands",
                "PostalCode": "98029",
                "Street": "Highlands Dr NE",
                "StreetComponents": [
                    {
                        "BaseName": "Highlands",
                        "Type": "Dr",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Suffix": "NE",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "1520"
            },
            "Position": [
                -122.01868,
                47.54262
            ],
            "Distance": 209665,
            "Categories": [
                {
                    "Id": "wellness_center_and_services",
                    "Name": "Wellness Center and Services",
                    "LocalizedName": "Wellness Center & Services",
                    "Primary": true
                }
            ],
            "BusinessChains": [
                {
                    "Name": "Restore",
                    "Id": "Restore"
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+14256518137"
                    }
                ],
                "Websites": [
                    {
                        "Value": "https://restore.com",
                        "Categories": [
                            {
                                "Id": "wellness_center_and_services",
                                "Name": "Wellness Center and Services"
                            }
                        ]
                    },
                    {
                        "Value": "https://www.facebook.com/rhwissaquah",
                        "Categories": [
                            {
                                "Id": "wellness_center_and_services",
                                "Name": "Wellness Center and Services"
                            }
                        ]
                    },
                    {
                        "Value": "https://www.restore.com/locations",
                        "Categories": [
                            {
                                "Id": "wellness_center_and_services",
                                "Name": "Wellness Center and Services"
                            }
                        ]
                    },
                    {
                        "Value": "https://www.restore.com/locations/wa-issaquah-wa002?utm_source=extnet&utm_medium=Yext&y_source=1_MzE2Mjk5NTktNTY2LWxvY2F0aW9uLndlYnNpdGU%3D",
                        "Categories": [
                            {
                                "Id": "wellness_center_and_services",
                                "Name": "Wellness Center and Services"
                            }
                        ]
                    },
                    {
                        "Value": "https://www.restore.com/sitemap.xml",
                        "Categories": [
                            {
                                "Id": "wellness_center_and_services",
                                "Name": "Wellness Center and Services"
                            }
                        ]
                    }
                ],
                "Emails": [
                    {
                        "Value": "issaquah@restore.com",
                        "Categories": [
                            {
                                "Id": "wellness_center_and_services",
                                "Name": "Wellness Center and Services"
                            }
                        ]
                    }
                ]
            },
            "OpeningHours": [
                {
                    "Display": [
                        "Mon-Thu: 10:00 - 18:00",
                        "Fri: 10:00 - 17:00",
                        "Sat: 09:00 - 17:00"
                    ],
                    "OpenNow": false,
                    "Components": [
                        {
                            "OpenTime": "T100000",
                            "OpenDuration": "PT08H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH"
                        },
                        {
                            "OpenTime": "T100000",
                            "OpenDuration": "PT07H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:FR"
                        },
                        {
                            "OpenTime": "T090000",
                            "OpenDuration": "PT08H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:SA"
                        }
                    ],
                    "Categories": [
                        {
                            "Id": "wellness_center_and_services",
                            "Name": "Wellness Center and Services"
                        }
                    ]
                }
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -122.01894,
                        47.54262
                    ]
                }
            ]
        }
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryId": "<Redacted>"
}'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-id "<Redacted>"
```

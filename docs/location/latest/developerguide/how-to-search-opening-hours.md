# How to search for contact and opening

hours

The `SearchText` API enables you to search for contacts and opening hours
of a POI (Point of Interest).

One way to use the SearchText API is to get the contact information for a location
(phone number, website, email) and opening hours by searching with business name and
bias position. These bias positions can be a device position, IP position, map‘s view
port center. Another way is to let end users provide the city name or place name and the
application can bias results based on the geo-coordinates.

For more information, see [Contacts and opening hours](contacts-opening-hours.md "contacts-opening-hours.md").

## Potential use cases

You can use the `SearchText` API to filter on contacts and opening
hours.

## Examples

Sample request

```
{
    "QueryText": "Nursing Home",
    "BiasPosition": [
                -123.11336,
                49.26038
            ],
        "AdditionalFeatures":["Contact"]

}
```

Sample response

```
{
    "PricingBucket": "Advanced",
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Para Med Home Health Care",
            "Address": {
                "Label": "Para Med Home Health Care, 601 W Broadway, Vancouver, BC V5Z 4C2, Canada",
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
                "District": "Fairview",
                "PostalCode": "V5Z 4C2",
                "Street": "W Broadway",
                "StreetComponents": [
                    {
                        "BaseName": "Broadway",
                        "Prefix": "W",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "601"
            },
            "Position": [
                -123.11771,
                49.26341
            ],
            "Distance": 462,
            "Categories": [
                {
                    "Id": "nursing_home",
                    "Name": "Nursing Home",
                    "LocalizedName": "Nursing Home",
                    "Primary": true
                },
                {
                    "Id": "hospital_or_health_care_facility",
                    "Name": "Hospital or Health Care Facility",
                    "LocalizedName": "Hospital or Health Care Facility",
                    "Primary": false
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+16045634663"
                    },
                    {
                        "Value": "+16047311594",
                        "Categories": [
                            {
                                "Id": "hospital_or_health_care_facility",
                                "Name": "Hospital or Health Care Facility"
                            }
                        ]
                    }
                ],
                "Websites": [
                    {
                        "Value": "http://www.rightathomecanada.com/vancouver",
                        "Categories": [
                            {
                                "Id": "nursing_home",
                                "Name": "Nursing Home"
                            }
                        ]
                    },
                    {
                        "Value": "https://www.facebook.com/507123162974954",
                        "Categories": [
                            {
                                "Id": "nursing_home",
                                "Name": "Nursing Home"
                            }
                        ]
                    }
                ]
            }
        },
         {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointOfInterest",
            "Title": "Yaletown House",
            "Address": {
                "Label": "Yaletown House, 1099 Cambie St, Vancouver, BC V6B 5A8, Canada",
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
                "District": "Yaletown",
                "PostalCode": "V6B 5A8",
                "Street": "Cambie St",
                "StreetComponents": [
                    {
                        "BaseName": "Cambie",
                        "Type": "St",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "1099"
            },
            "Position": [
                -123.11949,
                49.27533
            ],
            "Distance": 1721,
            "Categories": [
                {
                    "Id": "nursing_home",
                    "Name": "Nursing Home",
                    "LocalizedName": "Nursing Home",
                    "Primary": true
                },
                {
                    "Id": "restaurant",
                    "Name": "Restaurant",
                    "LocalizedName": "Restaurant",
                    "Primary": false
                },
                {
                    "Id": "clothing_and_accessories",
                    "Name": "Clothing and Accessories",
                    "LocalizedName": "Clothing & Accessories",
                    "Primary": false
                },
                {
                    "Id": "market",
                    "Name": "Market",
                    "LocalizedName": "Market",
                    "Primary": false
                },
                {
                    "Id": "jeweler",
                    "Name": "Jeweler",
                    "LocalizedName": "Jeweler",
                    "Primary": false
                },
                {
                    "Id": "advertising-marketing,_pr_and_market_research",
                    "Name": "Advertising-Marketing, PR and Market Research",
                    "LocalizedName": "Advertising/Marketing, PR & Market Research",
                    "Primary": false
                },
                {
                    "Id": "management_and_consulting_services",
                    "Name": "Management and Consulting Services",
                    "LocalizedName": "Management and Consulting Services",
                    "Primary": false
                },
                {
                    "Id": "organizations_and_societies",
                    "Name": "Organizations and Societies",
                    "LocalizedName": "Organizations and Societies",
                    "Primary": false
                },
                {
                    "Id": "finance_and_insurance",
                    "Name": "Finance and Insurance",
                    "LocalizedName": "Finance and Insurance",
                    "Primary": false
                },
                {
                    "Id": "consumer_services",
                    "Name": "Consumer Services",
                    "LocalizedName": "Consumer Services",
                    "Primary": false
                },
                {
                    "Id": "attorney",
                    "Name": "Attorney",
                    "LocalizedName": "Attorney",
                    "Primary": false
                },
                {
                    "Id": "social_service",
                    "Name": "Social Service",
                    "LocalizedName": "Social Services",
                    "Primary": false
                }
            ],
            "Contacts": {
                "Phones": [
                    {
                        "Value": "+16045584546",
                        "Categories": [
                            {
                                "Id": "management_and_consulting_services",
                                "Name": "Management and Consulting Services"
                            },
                            {
                                "Id": "consumer_services",
                                "Name": "Consumer Services"
                            }
                        ]
                    },
                    {
                        "Value": "+16046464065",
                        "Categories": [
                            {
                                "Id": "finance_and_insurance",
                                "Name": "Finance and Insurance"
                            }
                        ]
                    },
                    {
                        "Value": "+16046699800",
                        "Categories": [
                            {
                                "Id": "clothing_and_accessories",
                                "Name": "Clothing and Accessories"
                            },
                            {
                                "Id": "jeweler",
                                "Name": "Jeweler"
                            }
                        ]
                    },
                    {
                        "Value": "+16046838109",
                        "Categories": [
                            {
                                "Id": "attorney",
                                "Name": "Attorney"
                            }
                        ]
                    },
                    {
                        "Value": "+16046841838",
                        "Categories": [
                            {
                                "Id": "advertising-marketing,_pr_and_market_research",
                                "Name": "Advertising-Marketing, PR and Market Research"
                            },
                            {
                                "Id": "management_and_consulting_services",
                                "Name": "Management and Consulting Services"
                            }
                        ]
                    },
                    {
                        "Value": "+16046848898",
                        "Categories": [
                            {
                                "Id": "attorney",
                                "Name": "Attorney"
                            }
                        ]
                    },
                    {
                        "Value": "+16046890022"
                    },
                    {
                        "Value": "+16046999120",
                        "Categories": [
                            {
                                "Id": "nursing_home",
                                "Name": "Nursing Home"
                            }
                        ]
                    },
                    {
                        "Value": "+16046999121",
                        "Categories": [
                            {
                                "Id": "nursing_home",
                                "Name": "Nursing Home"
                            }
                        ]
                    },
                    {
                        "Value": "+16048016446",
                        "Categories": [
                            {
                                "Id": "management_and_consulting_services",
                                "Name": "Management and Consulting Services"
                            }
                        ]
                    }
                ],
                "Faxes": [
                    {
                        "Value": "+16046464068",
                        "Categories": [
                            {
                                "Id": "finance_and_insurance",
                                "Name": "Finance and Insurance"
                            }
                        ]
                    },
                    {
                        "Value": "+16046627954",
                        "Categories": [
                            {
                                "Id": "organizations_and_societies",
                                "Name": "Organizations and Societies"
                            }
                        ]
                    },
                    {
                        "Value": "+16046841801",
                        "Categories": [
                            {
                                "Id": "advertising-marketing,_pr_and_market_research",
                                "Name": "Advertising-Marketing, PR and Market Research"
                            }
                        ]
                    },
                    {
                        "Value": "+16046848608",
                        "Categories": [
                            {
                                "Id": "attorney",
                                "Name": "Attorney"
                            }
                        ]
                    }
                ],
                "Websites": [
                    {
                        "Value": "http://www.yaletown.org",
                        "Categories": [
                            {
                                "Id": "organizations_and_societies",
                                "Name": "Organizations and Societies"
                            },
                            {
                                "Id": "social_service",
                                "Name": "Social Service"
                            },
                            {
                                "Id": "nursing_home",
                                "Name": "Nursing Home"
                            }
                        ]
                    },
                    {
                        "Value": "http://www.yaletownhq.com",
                        "Categories": [
                            {
                                "Id": "advertising-marketing,_pr_and_market_research",
                                "Name": "Advertising-Marketing, PR and Market Research"
                            }
                        ]
                    },
                    {
                        "Value": "http://www.yaletownlaw.ca",
                        "Categories": [
                            {
                                "Id": "attorney",
                                "Name": "Attorney"
                            }
                        ]
                    },
                    {
                        "Value": "https://www.facebook.com/1509112252725564",
                        "Categories": [
                            {
                                "Id": "nursing_home",
                                "Name": "Nursing Home"
                            }
                        ]
                    }
                ],
                "Emails": [
                    {
                        "Value": "nina@yaletownhq.com",
                        "Categories": [
                            {
                                "Id": "advertising-marketing,_pr_and_market_research",
                                "Name": "Advertising-Marketing, PR and Market Research"
                            }
                        ]
                    }
                ]
            },
            "OpeningHours": [
                {
                    "Display": [
                        "Mon-Fri: 08:30 - 16:00"
                    ],
                    "OpenNow": true,
                    "Components": [
                        {
                            "OpenTime": "T083000",
                            "OpenDuration": "PT07H30M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR"
                        }
                    ],
                    "Categories": [
                        {
                            "Id": "organizations_and_societies",
                            "Name": "Organizations and Societies"
                        }
                    ]
                },
                {
                    "Display": [
                        "Mon-Fri: 09:00 - 17:00"
                    ],
                    "OpenNow": true,
                    "Components": [
                        {
                            "OpenTime": "T090000",
                            "OpenDuration": "PT08H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR"
                        }
                    ],
                    "Categories": [
                        {
                            "Id": "attorney",
                            "Name": "Attorney"
                        }
                    ]
                },
                {
                    "Display": [
                        "Tue: 10:00 - 16:30",
                        "Wed-Sat: 09:30 - 16:30"
                    ],
                    "OpenNow": true,
                    "Components": [
                        {
                            "OpenTime": "T100000",
                            "OpenDuration": "PT06H30M",
                            "Recurrence": "FREQ:DAILY;BYDAY:TU"
                        },
                        {
                            "OpenTime": "T093000",
                            "OpenDuration": "PT07H00M",
                            "Recurrence": "FREQ:DAILY;BYDAY:WE,TH,FR,SA"
                        }
                    ],
                    "Categories": [
                        {
                            "Id": "clothing_and_accessories",
                            "Name": "Clothing and Accessories"
                        },
                        {
                            "Id": "jeweler",
                            "Name": "Jeweler"
                        }
                    ]
                }
            ]
        },
    ]
}
```

cURL

```
curl --request POST \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/search-text?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
    "QueryText": "Nursing Home",
    "BiasPosition": [
                -123.11336,
                49.26038
       ],
    "AdditionalFeatures":["Contact"]
}'
```

AWS CLI

```
aws geo-places search-text --key ${YourKey} --query-text "Nursing Home" \
--bias-position -123.11336 49.26038 \
--additional-features "Contact"
```

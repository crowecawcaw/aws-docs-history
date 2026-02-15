# Use Suggest and the ability to filter

for a region or country

The Suggest API enables completing queries for places or categories of results. The
results are sorted for most likely to less likely matches. Additionally, you can further
filter results to specific regions or countries.

## Potential use cases

- **Filter the results:** When performing a
  search, you can filter by country or only the region in which your business
  operates.

## Examples

Adding a filter by country ensures you only receive the most relevant results. Use
Filter.IncludeCountries for this.

Sample request

```
{
  "QueryText": "hote",
  "BiasPosition": [
    2.2982750966095398, 48.856078089325294
  ],
  "Filter": {
    "IncludeCountries": [
      "FRA"
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
            "Title": "Hôtel de Matignon (Hôtel Matignon)",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "Redacted",
                "PlaceType": "PointOfInterest",
                "Address": {
                    "Label": "Hôtel de Matignon, 57 Rue de Varenne, 75007 Paris, France",
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
                    "District": "7e Arrondissement",
                    "PostalCode": "75007",
                    "Street": "Rue de Varenne",
                    "StreetComponents": [
                        {
                            "BaseName": "Varenne",
                            "Type": "Rue de",
                            "TypePlacement": "BeforeBaseName",
                            "TypeSeparator": " ",
                            "Language": "fr"
                        }
                    ],
                    "AddressNumber": "57"
                },
                "Position": [
                    2.32072,
                    48.85471
                ],
                "Distance": 1650,
                "Categories": [
                    {
                        "Id": "tourist_attraction",
                        "Name": "Tourist Attraction",
                        "LocalizedName": "Attraction touristique",
                        "Primary": true
                    },
                    {
                        "Id": "landmark-attraction",
                        "Name": "Landmark-Attraction",
                        "LocalizedName": "Lieu d'intérêt/Attraction",
                        "Primary": false
                    },
                    {
                        "Id": "historical_monument",
                        "Name": "Historical Monument",
                        "LocalizedName": "Monument historique",
                        "Primary": false
                    },
                    {
                        "Id": "residential_area-building",
                        "Name": "Residential Area-Building",
                        "LocalizedName": "Bâtiment résidentiel",
                        "Primary": false
                    }
                ]
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 0,
                        "EndIndex": 4,
                        "Value": "Hôt"
                    },
                    {
                        "StartIndex": 19,
                        "EndIndex": 23,
                        "Value": "(Hô"
                    }
                ],
                "Address": {
                    "Label": [
                        {
                            "StartIndex": 0,
                            "EndIndex": 4,
                            "Value": "Hôt"
                        }
                    ]
                }
            }
        },
        ...
        {
            "Title": "Hotel",
            "SuggestResultItemType": "Query",
            "Query": {
                "QueryId": "Redacted",
                "QueryType": "Category"
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 0,
                        "EndIndex": 4,
                        "Value": "Hote"
                    }
                ]
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
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/suggest?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "hote",
  "BiasPosition": [
    2.2982750966095398, 48.856078089325294
  ],
  "Filter": {
    "IncludeCountries": [
      "FRA"
    ]
  },
  "AdditionalFeatures": [
    "Core"
  ]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} \
--query-text "hote" \
--bias-position 2.2982750966095398 48.856078089325294 \
--filter '{"IncludeCountries": ["FRA"]}' \
--additional-features "Core"
```

Adding a filter-by-region option for a search limits results to only those which fit
within the provided region. This is used to limit the scope of the search to the region
that concerns your business. The following example shows a misspelled search for
Marriott hotels near the Boston area being completed with some hotel results and a
follow-up query.

Sample request

```
{
  "QueryText": "Mariot",
  "Filter": {
    "IncludeCountries": [
      "USA"
    ],
    "BoundingBox": [
      -71.15693983012913,42.261623506672635,
      -70.97249727163558,42.37584075627763
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
            "Title": "Boston Marriott Copley Place",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "Redacted",
                "PlaceType": "PointOfInterest",
                "Address": {
                    "Label": "Boston Marriott Copley Place, 110 Huntington Ave, Boston, MA 02116, United States",
                    "Country": {
                        "Code2": "US",
                        "Code3": "USA",
                        "Name": "United States"
                    },
                    "Region": {
                        "Code": "MA",
                        "Name": "Massachusetts"
                    },
                    "SubRegion": {
                        "Name": "Suffolk"
                    },
                    "Locality": "Boston",
                    "District": "Back Bay",
                    "PostalCode": "02116",
                    "Street": "Huntington Ave",
                    "StreetComponents": [
                        {
                            "BaseName": "Huntington",
                            "Type": "Ave",
                            "TypePlacement": "AfterBaseName",
                            "TypeSeparator": " ",
                            "Language": "en"
                        }
                    ],
                    "AddressNumber": "110"
                },
                "Position": [
                    -71.07769,
                    42.34726
                ],
                "Distance": 3347,
                "Categories": [
                    {
                        "Id": "hotel",
                        "Name": "Hotel",
                        "LocalizedName": "Hotel",
                        "Primary": true
                    }
                ],
                "BusinessChains": [
                    {
                        "Name": "Marriott",
                        "Id": "Marriott"
                    }
                ],
                "AccessPoints": [
                    {
                        "Position": [
                            -71.07922,
                            42.34665
                        ]
                    }
                ]
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 7,
                        "EndIndex": 14,
                        "Value": "Marriot"
                    }
                ],
                "Address": {
                    "Label": [
                        {
                            "StartIndex": 7,
                            "EndIndex": 14,
                            "Value": "Marriot"
                        }
                    ]
                }
            }
        },
        ...
        {
            "Title": "Marriott",
            "SuggestResultItemType": "Query",
            "Query": {
                "QueryId": "Redacted",
                "QueryType": "BusinessChain"
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 0,
                        "EndIndex": 8,
                        "Value": "Marriott"
                    }
                ]
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
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/suggest?key=Your_Key' \
  --header 'Content-Type: application/json' \
  --data '{
  "QueryText": "Mariot",
  "Filter": {
    "IncludeCountries": [
      "USA"
    ],
    "BoundingBox": [
      -71.15693983012913,42.261623506672635,
      -70.97249727163558,42.37584075627763
    ]
  },
  "AdditionalFeatures": [
    "Core"
  ]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} \
--query-text "hote" \
--filter '{"IncludeCountries": ["FRA"], "BoundingBox": [ -71.15693983012913,42.261623506672635, -70.97249727163558,42.37584075627763]}' \
--additional-features "Core"
```

## Developer tips

Display search results using the `Title` response field to provide
users with concise, recognizable entries. For results that might look similar, use
the `Place.Address.Label` field to show additional address details that
help users distinguish between them. For more information, see [How to help users disambiguate between
similar results](suggest-disambiguate-results.md "suggest-disambiguate-results.md").

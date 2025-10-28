# Choose a route using Suggest and

the ability to highlight matched query terms

With the Suggest API, you get real-time autocomplete suggestions as users type their
search queries for places or categories. Results are ranked by relevance, with the most
likely matches appearing first. The API response includes highlighting information that
shows how each suggestion matches the user's query.

## Potential use cases

Use highlighting to show users which parts of each suggestion match their input,
making it easier to quickly select the desired result.

## Examples

When displaying the result list to users, the **Highlights**
fields in the response can be used to help the user identify how the input has been
matched to the results. In the example below, the user makes a query for “Effel
tow”. This matches a result with the **Title** “Tour Eiffel (Eiffel
Tower)”. Using the Highlights result field, the result can be styled to show where
the input query was matched to the output, resulting in the text being showed to the
user as “Tour Eiffel (**Eiffel Tow**er).”

This example demonstrates how to use the Suggest API to look up a
misspelled point of interest.

Sample request

```
{
  "QueryText": "Effel tow",
  "Filter": {
    "Circle": {
      "Radius": 10000,
      "Center": [
        2.3431932014695382, 48.858844492141145
      ]
    },
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
            "Title": "Tour Eiffel (Eiffel Tower)",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "<Redacted>",
                "PlaceType": "PointOfInterest",
                "Address": {
                    "Label": "Tour Eiffel, * Avenue Anatole France, ***** Paris, France",
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
                    "District": "*e Arrondissement",
                    "PostalCode": "*****",
                    "Street": "Avenue Anatole France",
                    "StreetComponents": [
                        {
                            "BaseName": "Anatole France",
                            "Type": "Avenue",
                            "TypePlacement": "BeforeBaseName",
                            "TypeSeparator": " ",
                            "Language": "fr"
                        }
                    ],
                    "AddressNumber": "5"
                },
                "Position": [
                    2.2945,
                    48.85824
                ],
                "Distance": 3563,
                "Categories": [
                    {
                        "Id": "historical_monument",
                        "Name": "Historical Monument",
                        "LocalizedName": "Monument historique",
                        "Primary": true
                    },
                    {
                        "Id": "landmark-attraction",
                        "Name": "Landmark-Attraction",
                        "LocalizedName": "Lieu d'intérêt/Attraction",
                        "Primary": false
                    },
                    {
                        "Id": "tourist_attraction",
                        "Name": "Tourist Attraction",
                        "LocalizedName": "Attraction touristique",
                        "Primary": false
                    },
                    {
                        "Id": "sports_complex-stadium",
                        "Name": "Sports Complex-Stadium",
                        "LocalizedName": "Stade ou complexe sportif",
                        "Primary": false
                    }
                ]
            },
            "Highlights": {
                "Title": [
                    {
                        "StartIndex": 13,
                        "EndIndex": 23,
                        "Value": "Eiffel Tow"
                    }
                ],
                "Address": {}
            }
        }
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
  "QueryText": "Effel tow",
  "Filter": {
    "Circle": {
      "Radius": 10000,
      "Center": [
        2.3431932014695382, 48.858844492141145
      ]
    },
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
--query-text "Effel tow" \
--filter '{"Circle": {"Radius": 10000, "Center": [2.3431932014695382, 48.858844492141145]}, "IncludeCountries": ["FRA"]}' \
--additional-features "Core"
```

## Developer tips

Display search results using the `Title` response field to provide
users with concise, recognizable entries. For results that might look similar, use
the `Place.Address.Label` field to show additional address details that
help users distinguish between them. For more information, see [How to help users disambiguate between
similar results](suggest-disambiguate-results.md "suggest-disambiguate-results.md").

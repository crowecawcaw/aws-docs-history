# How to get

results for a partially typed or misspelled query

The Suggest API enables applications to complete user queries for places or categories
of results. These results are sorted from most likely to less-likely matches, allowing
the API to resolve incomplete or misspelled words.

## Potential use cases

- **Complete a partially typed point of interest
  query:** Assists users by providing suggestions based on
  partially typed or incorrect entries.

## Examples

Sample request

```
{
  "QueryText": "Effel tow",
  "Filter": {
    "Circle": {
      "Radius": 10000,
      "Center": [2.3431932014695382, 48.858844492141145]
    },
    "IncludeCountries": ["FRA"]
  },
  "AdditionalFeatures": ["Core"]
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
                    "Label": "Tour Eiffel, 5 Avenue Anatole France, 75007 Paris, France",
                    "Country": {"Code2": "FR", "Code3": "FRA", "Name": "France"},
                    "Region": {"Code": "IDF", "Name": "Île-de-France"},
                    "SubRegion": {"Name": "Paris"},
                    "Locality": "Paris",
                    "District": "7e Arrondissement",
                    "PostalCode": "75007",
                    "Street": "Avenue Anatole France",
                    "StreetComponents": [{"BaseName": "Anatole France", "Type": "Avenue", "Language": "fr"}],
                    "AddressNumber": "5"
                },
                "Position": [2.2945, 48.85824],
                "Distance": 3563,
                "Categories": [
                    {"Id": "historical_monument", "Name": "Historical Monument", "LocalizedName": "Monument historique", "Primary": true},
                    {"Id": "landmark-attraction", "Name": "Landmark-Attraction", "LocalizedName": "Lieu d'intérêt/Attraction", "Primary": false},
                    {"Id": "tourist_attraction", "Name": "Tourist Attraction", "LocalizedName": "Attraction touristique", "Primary": false},
                    {"Id": "sports_complex-stadium", "Name": "Sports Complex-Stadium", "LocalizedName": "Stade ou complexe sportif", "Primary": false}
                ]
            },
            "Highlights": {"Title": [{"StartIndex": 13, "EndIndex": 23, "Value": "Eiffel Tow"}]}
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
    "Circle": {"Radius": 10000, "Center": [2.3431932014695382, 48.858844492141145]},
    "IncludeCountries": ["FRA"]
  },
  "AdditionalFeatures": ["Core"]
}'
```

AWS CLI

```
aws geo-places suggest --key ${YourKey} \
--query-text "Effel tow" \
--filter '{"Circle": {"Radius": 1000, "Center": [2.3431932014695382, 48.858844492141145]}, "IncludeCountries": ["FRA"]}' \
--additional-features "Core"
```

## Developer tips

Use filters such as `Filter.IncludeCountries` or
`Filter.BoundingBox` with `BiasPosition`. These filters
can help narrow down possible results and improve accuracy.

```
{
  "QueryText": "Effel tow",
  "BiasPosition": [2.2982750966095398, 48.856078089325294],
  "Filter": {"IncludeCountries": ["FRA"]}
}
```

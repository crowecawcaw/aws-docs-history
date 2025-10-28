# How to help users disambiguate between

similar results

The Suggest API enables you to create queries for places or categories of results. The
results are sorted for more likely to less likely matches. Information is provided for
each result which helps you quickly identify the correct match, particularly with regard
to the Title and Label fields.

## Potential use cases

- **Display the result options:** You can
  select the option that best suits your needs.

## Examples

The Title field is usually enough information for you to understand when the
result is what was intended. For cases where the title doesn't provide enough
information, the Label field is used to add address information context to the
result. The Label field can be provided as a second line of information which is
de-emphasized from the main text when the results are rendered for you. In the
example below, two similar results are provided and the address of the hotel can
help you select the one that is more applicable to your needs. Additionally,
position is provided so the results can be rendered on a map as an alternate way for
you to select between results.

Sample request

```
{
  "QueryText": "Marriott",
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
            "Title": "Marriott-Boston Cambridge",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "Redacted",
                "PlaceType": "PointOfInterest",
                "Address": {
                    "Label": "Marriott-Boston Cambridge, 50 Broadway, Cambridge, MA 02138-4137, United States",
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
                        "Name": "Middlesex"
                    },
                    "Locality": "Cambridge",
                    "District": "MIT",
                    "PostalCode": "02138-4137",
                    "Street": "Broadway",
                    "StreetComponents": [
                        {
                            "BaseName": "Broadway",
                            "Language": "en"
                        }
                    ],
                    "AddressNumber": "50"
                },
                "Position": [
                    -71.0858,
                    42.36294
                ],
                "Distance": 5212,
            ...
        },
        {
            "Title": "Marriott-Boston Copley Place",
            "SuggestResultItemType": "Place",
            "Place": {
                "PlaceId": "Redacted",
                "PlaceType": "PointOfInterest",
                "Address": {
                    "Label": "Marriott-Boston Copley Place, 110 Huntington Ave, Boston, MA 02116-5706, United States",
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
                    "PostalCode": "02116-5706",
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
                    -71.0792,
                    42.34701
                ],
                "Distance": 3362,
            ...
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
  "QueryText": "Marriott",
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
--query-text "Marriott" \
--filter '{"IncludeCountries": ["USA"], "BoundingBox": [ -71.15693983012913,42.261623506672635, -70.97249727163558,42.37584075627763]}' \
--additional-features "Core"

```

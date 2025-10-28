# How to geocode an administrative and

postal area

The Geocode API allows you to perform geocoding for a geographic area using a query
text input, such as the name of a country, region (state or province), or city. The API
response includes location details like geographic coordinates, bounding boxes for map
visualizations, and match scores indicating the result's relevance to the query.

## Potential use cases

- **Obtain coordinates for an administrative
  area:** Use coordinates as a bias position or center in other
  Places APIs.
- **Visualize information on a map:** Geocoded
  coordinates can be used to display data visually on a map.

## Examples

Sample request

```
{
  "QueryText": "Canada"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId":"<Redacted>",
            "PlaceType": "Country",
            "Title": "Canada",
            "Address": {
                "Label": "Canada",
                "Country": {
                    "Code2": "CA",
                    "Code3": "CAN",
                    "Name": "Canada"
                }
            },
            "Position": [-75.69122, 45.42177],
            "MapView": [-141.00271, 41.67659, -52.61901, 83.11062],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": { "Country": 1 }
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
  "QueryText": "Canada"
}'
```

AWS CLI

```
aws geo-places geocode --key ${`YourAPIKey`} --query-text "Canada"
```

Sample request

```
{
  "QueryText": "BC"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Region",
            "Title": "BC, Canada",
            "Address": {
                "Label": "BC, Canada",
                "Country": {
                    "Code2": "CA",
                    "Code3": "CAN",
                    "Name": "Canada"
                },
                "Region": {
                    "Code": "BC",
                    "Name": "British Columbia"
                }
            },
            "Position": [-123.36445, 48.42854],
            "MapView": [-139.04941, 48.22478, -114.05201, 60.00043],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": { "Region": 1 }
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
  "QueryText": "BC"
}'
```

AWS CLI

```
aws geo-places geocode --key ${`YourAPIKey`} --query-text "BC"
```

Sample request

```
{
  "QueryText": "Vancouver"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "Locality",
            "Title": "Vancouver, BC, Canada",
            "Address": {
                "Label": "Vancouver, BC, Canada",
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
                "PostalCode": "V5Y"
            },
            "Position": [-123.11336, 49.26038],
            "MapView": [-123.26754, 49.19891, -123.02301, 49.33557],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": { "Locality": 1 }
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
  "QueryText": "Vancouver"
}'
```

AWS CLI

```
aws geo-places geocode --key ${`YourAPIKey`} --query-text "Vancouver"
```

You can geocode a postal code. Use `IncludePlaceTypes` with
`["PostalCode"]` for more precise results.

Sample request

```
{
  "QueryText": "800006",
  "Filter": { "IncludePlaceTypes": ["PostalCode"] }
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PostalCodeArea",
            "Title": "800006, Patna, Bihar, India",
            "Address": {
                "Label": "800006, Patna, Bihar, India",
                "Country": {
                    "Code2": "IN",
                    "Code3": "IND",
                    "Name": "India"
                },
                "Region": {
                    "Code": "BR",
                    "Name": "Bihar"
                },
                "SubRegion": { "Name": "Patna" },
                "Locality": "Patna",
                "PostalCode": "800006"
            },
            "Position": [85.18048, 25.61532],
            "MapView": [85.16599, 25.60054, 85.19103, 25.6221],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": { "PostalCode": 1 }
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
  "QueryText": "800006",
  "Filter": { "IncludePlaceTypes": ["PostalCode"] }
}'
```

AWS CLI

```
aws geo-places geocode --key ${`YourAPIKey`} --query-text "800006" --filter '{"IncludePlaceTypes": ["PostalCode"]}'
```

## Developer tips

Use filters like `IncludeCountries` and `IncludePlaceTypes`
for more targeted results. For example, to ensure results from Vancouver in the USA,
set `"IncludeCountries": ["USA"]`. For more details, see
.

```
{
  "QueryText": "Vancouver",
  "Filter": { "IncludeCountries": ["USA"] }
}
```

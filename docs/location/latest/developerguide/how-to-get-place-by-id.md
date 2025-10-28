# How to get results for a PlaceId

The GetPlace API retrieves detailed information about a place using its unique
PlaceId, allowing applications to access comprehensive details about specified
locations.

## Potential use cases

- **Retrieve store locations:** Use PlaceId to
  obtain details about various store locations for improved user experience
  and efficient resource management.
- **Access related place details:** Fetch
  details of places that were identified using other PlaceIds returned by
  previous queries.

## Examples

Sample request

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP?key=Your_Key
```

Sample response

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointOfInterest",
    "Title": "London Eye",
    "Address": {
        "Label": "London Eye, County Hall, Westminster Bridge Road, London, SE1 7, United Kingdom",
        "Country": {
            "Code2": "GB",
            "Code3": "GBR",
            "Name": "United Kingdom"
        },
        "Region": {
            "Name": "England"
        },
        "SubRegion": {
            "Code": "LDN",
            "Name": "London"
        },
        "Locality": "London",
        "District": "Waterloo",
        "PostalCode": "SE1 7",
        "Street": "County Hall, Westminster Bridge Road",
        "StreetComponents": [
            {
                "BaseName": "County Hall, Westminster Bridge Road",
                "Language": "en-GB"
            }
        ]
    },
    "Position": [
        -0.11953,
        51.50336
    ],
    "Categories": [
        {
            "Id": "tourist_attraction",
            "Name": "Tourist Attraction",
            "LocalizedName": "Tourist Attraction",
            "Primary": true
        },
        {
            "Id": "landmark-attraction",
            "Name": "Landmark-Attraction",
            "LocalizedName": "Landmark-Attraction",
            "Primary": false
        },
        {
            "Id": "residential_area-building",
            "Name": "Residential Area-Building",
            "LocalizedName": "Residential Area/Building",
            "Primary": false
        }
    ]
}
```

cURL

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP?key=Your_Key&language=en'
```

AWS CLI

```
export PLACEID=AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIs
aws geo-places get-place --key ${YourKey} --place-id ${PLACEID}
```

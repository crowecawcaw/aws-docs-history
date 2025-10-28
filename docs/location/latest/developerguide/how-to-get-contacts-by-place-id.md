# How to get contacts for a

PlaceId

The GetPlace API allows retrieval of contact information associated with a specific
PlaceId, providing you with details such as phone numbers and website URLs.

## Potential use cases

- **Obtain additional contact information for a saved
  PlaceId:** Enhance stored place details by accessing contact
  data.
- **Retrieve contact details for addresses from
  Autocomplete:** Use the PlaceId from the Autocomplete API to
  fetch specific contact details.

## Examples

Sample request

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP?additional-features=Contact&key=Your_Key
```

Sample response

```
{
    "PlaceId": "AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP",
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
    ],
    "Contacts": {
        "Phones": [
            {
                "Value": "+44870500600"
            },
            {
                "Value": "+448709908883"
            }
        ],
        "Websites": [
            {
                "Value": "http://www.londoneye.com"
            }
        ]
    }
}
```

cURL

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP?key=Your_Key&additional-features=Contact&language=en'
```

AWS CLI

```
export PLACEID=AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP
aws geo-places get-place --key ${YourKey} --place-id ${PLACEID} --additional-features "Contact" --language "en"
```

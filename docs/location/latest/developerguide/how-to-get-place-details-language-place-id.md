# How to get the details for

PlaceId in a specific language

The feature allows you to select a preferred response language from BCP47-compliant
codes. It detects the query language based on name variants and uses the preferred
language for unmatched tokens and ambiguous cases. If no requested language is stated,
the Places API provides results in whatever language the country uses, but it
prioritizes the regional language in regions where it differs. As a fallback, Places
APIs return addresses in the default language when some address elements are unavailable
in the requested language.

## Potential use cases

- **Add PlaceId details:** Add additional
  detail in a specified language for a stored place ID.
- **Retrieve PlaceId details for addresses from
  Autocomplete:** Get additional detail in a specific language
  for a stored PlaceId.

## Examples

Sample request

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAFUAY0R_4qfQ9LZ0j6lpOggbNLAQ31TRf-sESER_bKKjCar9FF6A3UA0HrYWa4yfeUN5V0qkk6NmdrI3y7fB7PZ4vfuo-Z8Wd-u-01an4KNvWaqfYmEh14s22yCV9Nb1yMXl4-HTfpX5D-jWQT14FEIBqoiuKwLq?language=EN&key=Your_Key
```

Sample response

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointOfInterest",
    "Title": "Parking Area",
    "Address": {
        "Label": "Parking Area, Al Nahda Sharjah, United Arab Emirates",
        "Country": {
            "Code2": "AE",
            "Code3": "ARE",
            "Name": "United Arab Emirates"
        },
        "SubRegion": {
            "Name": "Sharjah"
        },
        "Locality": "Sharjah",
        "District": "Al Nahda"
    },
    "Position": [
        55.3733,
        25.30388
    ],
    "Categories": [
        {
            "Id": "parking_lot",
            "Name": "Parking Lot",
            "LocalizedName": "Parking Lot",
            "Primary": true
        }
    ],
    "Contacts": {
        "Phones": [
            {
                "Value": "+971507766189"
            }
        ]
    },
    "AccessPoints": [
        {
            "Position": [
                55.37348,
                25.30398
            ]
        }
    ]
}
```

cURL

```
curl --request GET \
  --url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAFUAY0R_4qfQ9LZ0j6lpOggbNLAQ31TRf-sESER_bKKjCar9FF6A3UA0HrYWa4yfeUN5V0qkk6NmdrI3y7fB7PZ4vfuo-Z8Wd-u-01an4KNvWaqfYmEh14s22yCV9Nb1yMXl4-HTfpX5D-jWQT14FEIBqoiuKwLq?language=EN&key=Your_Key`
```

AWS CLI

```
export PLACEID=AQAAAFUAcrFHu947JATTY9gIGcfNlNVzD3UftkkI9ayJjtquaC7IquYz-_FFnJnzJSQ7JePd-sY0MSpA64V0w4aXLc-lB2fZLJKk6uoAMSgtwvwxzg1fvPxFM9zXsx77EaLXarl7F4gSPTyQ6fiEnj0b0ipOXpnOoIsP

aws geo-places get-place --key ${YourKey} \
--place-id ${PLACEID} \
--language "en"
```

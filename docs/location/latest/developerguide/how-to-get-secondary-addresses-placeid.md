# How to get secondary addresses

of a Place ID

The `SecondaryAddresses` API command allows you to retrieve all secondary
addresses that are under a main address. Geocode also returns secondary units, if any
that are present within the `QueryText` parameter.

## Potential use

cases

**Retrieve all secondary addresses that are under a main
address.** This can be used for address form completion use cases to
select a more accurate secondary address which includes more accurate positional
information as well.

Sample request

```
https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAGAAY8Dw_tn6pyN_R5E9_mfwAP5h9Rd5E_xY2CyyRHpX2wolGeK8O3IY13k5xeHmF4To445fCLg0x3GPnTZnCuUWXbfg9SKpijUskj-xf6jNC_3CUSabHVKy-Or51xHTd3KNi6idTkrfeQOjZOkXZ5TaoXsg0GHGMWqs-sZhmr8npQc?additional-features=SecondaryAddresses&key=Your_Key
```

Sample response

```
{
    "PlaceId": "<Redacted>",
    "PlaceType": "PointAddress",
    "Title": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
    "Address": {
        "Label": "910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
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
        "District": "Downtown Vancouver",
        "PostalCode": "V6Z 2W7",
        "Street": "Beach Ave",
        "StreetComponents": [
            {
                "BaseName": "Beach",
                "Type": "Ave",
                "TypePlacement": "AfterBaseName",
                "TypeSeparator": " ",
                "Language": "en"
            }
        ],
        "AddressNumber": "910"
    },
    "Position": [
        -123.13325,
        49.27542
    ],
    "MapView": [
        -123.13377,
        49.2741,
        -123.13087,
        49.27599
    ],
    "SecondaryAddresses": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "SecondaryAddress",
            "Title": "101-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
            "Address": {
                "Label": "101-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                "SecondaryAddressComponents": [
                    {
                        "Number": "101"
                    }
                ]
            },
            "Position": [
                -123.1334,
                49.27532
            ]
        },
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "SecondaryAddress",
            "Title": "102-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
            "Address": {
                "Label": "102-910 Beach Ave, Vancouver, BC V6Z 2W7, Canada",
                "SecondaryAddressComponents": [
                    {
                        "Number": "102"
                    }
                ]
            },
            "Position": [
                -123.1334,
                49.27532
            ]
        },
        ...
    ]
}
```

cURL

```
curl ‐‐request GET \
  ‐‐url 'https://places.geo.eu-central-1.amazonaws.com/v2/place/AQAAAGAAY8Dw_tn6pyN_R5E9_mfwAP5h9Rd5E_xY2CyyRHpX2wolGeK8O3IY13k5xeHmF4To445fCLg0x3GPnTZnCuUWXbfg9SKpijUskj-xf6jNC_3CUSabHVKy-Or51xHTd3KNi6idTkrfeQOjZOkXZ5TaoXsg0GHGMWqs-sZhmr8npQc?key=Your_Key&additional-features=SecondaryAddresses'
```

AWS CLI

```
export PLACEID=AQAAAGAAY8Dw_tn6pyN_R5E9_mfwAP5h9Rd5E_xY2CyyRHpX2wolGeK8O3IY13k5xeHmF4To445fCLg0x3GPnTZnCuUWXbfg9SKpijUskj-xf6jNC_3CUSabHVKy-Or51xHTd3KNi6idTkrfeQOjZOkXZ5TaoXsg0GHGMWqs-sZhmr8npQc

aws geo-places get-place ‐‐key ${YourKey} \
‐‐place-id ${PLACEID} \
‐‐additional-features "SecondaryAddresses"
```

# How to geocode an address number

with a postal code

In countries where postal codes are highly specific (linking only a few addresses on
the same street), an address can be found using only the house number and postal code.
This practice is common in transportation and parcel delivery logistics. This feature is
supported in Canada, the United Kingdom, the Netherlands, the United States (ZIP+4),
Israel, Ireland, and Singapore. In both Ireland and Singapore, postal codes provide
exact location details down to the specific house number.

## Examples

Sample request
Use query component

```
{
  "QueryComponents": {
    "AddressNumber": "1368",
    "PostalCode": "V5N 1T2"
  }
}
```

Use free text

```
{
  "QueryText": "1368, V5N1T2"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "1368 E 8th Ave, Vancouver, BC V5N 1T2, Canada",
            "Address": {
                "Label": "1368 E 8th Ave, Vancouver, BC V5N 1T2, Canada",
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
                "District": "Grandview-Woodland",
                "PostalCode": "V5N 1T2",
                "Street": "E 8th Ave",
                "StreetComponents": [
                    {
                        "BaseName": "8th",
                        "Type": "Ave",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Prefix": "E",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "1368"
            },
            "Position": [
                -123.07612,
                49.26306
            ],
            "MapView": [
                -123.0775,
                49.26216,
                -123.07474,
                49.26396
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -123.07611,
                        49.26333
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "PostalCode": 1,
                        "AddressNumber": 1
                    }
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
  "QueryComponents": {
    "AddressNumber": "1368",
    "PostalCode": "V5N 1T2"
  }
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-components '{"AddressNumber" : "1368", "PostalCode": "V5N 1T2"}'
```

In Ireland, the Eircode system assigns a unique code to every home and
business, while in Singapore, postal codes are equally specific. In both
countries, a postal code alone can identify an exact address: there is no
need for the street name, city, or house number.

- Singapore: 6-digit postal code
- Ireland: 7-character Eircode

Sample request
Use query component

```
{
  "QueryComponents": {
    "PostalCode": "D02 X285"
  }
}
```

Use free text

```
{
  "QueryText": "D02 X285"
}
```

Sample response

```
{
    "ResultItems": [
        {
            "PlaceId": "<Redacted>",
            "PlaceType": "PointAddress",
            "Title": "29-31 Adelaide Road, Dublin, County Dublin, D02 X285, Ireland",
            "Address": {
                "Label": "29-31 Adelaide Road, Dublin, County Dublin, D02 X285, Ireland",
                "Country": {
                    "Code2": "IE",
                    "Code3": "IRL",
                    "Name": "Ireland"
                },
                "SubRegion": {
                    "Code": "D",
                    "Name": "County Dublin"
                },
                "Locality": "Dublin",
                "District": "Dublin 2",
                "PostalCode": "D02 X285",
                "Street": "Adelaide Road",
                "StreetComponents": [
                    {
                        "BaseName": "Adelaide",
                        "Type": "Road",
                        "TypePlacement": "AfterBaseName",
                        "TypeSeparator": " ",
                        "Language": "en"
                    }
                ],
                "AddressNumber": "29-31"
            },
            "Position": [
                -6.25549,
                53.33207
            ],
            "MapView": [
                -6.257,
                53.33117,
                -6.25398,
                53.33297
            ],
            "AccessPoints": [
                {
                    "Position": [
                        -6.25536,
                        53.33231
                    ]
                }
            ],
            "MatchScores": {
                "Overall": 1,
                "Components": {
                    "Address": {
                        "PostalCode": 1
                    }
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
  "QueryComponents": {
    "PostalCode": "D02 X285"
  }
}'
```

AWS CLI

```
aws geo-places geocode --key ${YourKey} --query-components '{"PostalCode": "V5N 1T2"}'
```

## Developer tips

Learn more about [ZIP+4](https://en.wikipedia.org/wiki/ZIP_Code#ZIP+4 "https://en.wikipedia.org/wiki/ZIP_Code#ZIP+4") (United States) and [Eircode](https://en.wikipedia.org/wiki/Postal_addresses_in_the_Republic_of_Ireland "https://en.wikipedia.org/wiki/Postal_addresses_in_the_Republic_of_Ireland") (Ireland). Also, learn about postal code system in Canada, the
United Kingdom, the Netherlands, Singapore, and Israel.

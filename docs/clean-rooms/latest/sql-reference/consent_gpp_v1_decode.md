# consent_gpp_v1_decode function

The `consent_gpp_v1_decode` function is used to decode Global Privacy Platform
(GPP) v1 consent data. It takes the encoded consent string as input and returns the decoded
consent data, which includes information about the user's privacy preferences and consent
choices. This function is useful when working with data that includes GPP v1 consent
information, as it allows you to access and analyze the consent data in a structured
format.

## Syntax

```
consent_gpp_v1_decode(gpp_string)
```

## Arguments

_gpp_string_

The encoded GPP v1 consent string.

## Returns

The returned dictionary includes the following key-value pairs:

- `version`: The version of the GPP specification used (currently 1).
- `cmpId`: The ID of the Consent Management Platform (CMP) that
  encoded the consent string.
- `cmpVersion`: The version of the CMP that encoded the consent
  string.
- `consentScreen`: The ID of the screen in the CMP UI where the user
  provided consent.
- `consentLanguage`: The language code of the consent information.
- `vendorListVersion`: The version of the vendor list used.
- `publisherCountryCode`: The country code of the publisher.
- `purposeConsent`: A list of integers representing the purposes for
  which the user has consented to.
- `purposeLegitimateInterest`: A list of purpose IDs for which the
  user's legitimate interest has been transparently communicated.
- `specialFeatureOptIns`: A list of integers representing the special
  features that the user has opted into.
- `vendorConsent`: A list of vendor IDs that the user has consented
  to.
- `vendorLegitimateInterest`: A list of vendor IDs for which the
  user's legitimate interest has been transparently communicated.

## Example

The following example takes a single argument, which is the encoded consent string.
It returns a dictionary containing the decoded consent data, including information about
the user's privacy preferences, consent choices, and other metadata.

```
SELECT * FROM consent_gpp_v1_decode('ABCDEFGHIJK');

```

The basic structure of the returned consent data includes information about the
consent string version, the CMP (Consent Management Platform) details, the user's
consent and legitimate interest choices for different purposes and vendors, and other
metadata.

```
{
    "version": 1,
    "cmpId": 12,
    "cmpVersion": 34,
    "consentScreen": 5,
    "consentLanguage": "en",
    "vendorListVersion": 89,
    "publisherCountryCode": "US",
    "purposeConsent": [1],
    "purposeLegitimateInterests": [1],
    "specialFeatureOptins": [1],
    "vendorConsent": [1],
    "vendorLegitimateInterests": [1]}
}
```

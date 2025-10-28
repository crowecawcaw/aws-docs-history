# consent_tcf_v2_decode function

The `consent_tcf_v2_decode` function is used to decode Transparency and
Consent Framework (TCF) v2 consent data. It takes the encoded consent string as input and
returns the decoded consent data, which includes information about the user's privacy
preferences and consent choices. This function is useful when working with data that
includes TCF v2 consent information, as it allows you to access and analyze the consent
data in a structured format.

## Syntax

```
consent_tcf_v2_decode(tcf_string)
```

## Arguments

_tcf_string_

The encoded TCF v2 consent string.

## Returns

The `consent_tcf_v2_decode` function returns a dictionary containing the
decoded consent data from a Transparency and Consent Framework (TCF) v2 consent string.

The returned dictionary includes the following key-value pairs:

**Core segment**

- `version`: The version of the TCF specification used (currently 2).
- `created`: The date and time when the consent string was
  created.
- `lastUpdated`: The date and time when the consent string was last
  updated.
- `cmpId`: The ID of the Consent Management Platform (CMP) that
  encoded the consent string.
- `cmpVersion`: The version of the CMP that encoded the consent
  string.
- `consentScreen`: The ID of the screen in the CMP UI where the user
  provided consent.
- `consentLanguage`: The language code of the consent information.
- `vendorListVersion`: The version of the vendor list used.
- `tcfPolicyVersion`: The version of the TCF policy that the consent
  string is based on.
- `isServiceSpecific`: A Boolean value indicating whether the consent
  is specific to a particular service or applies to all services.
- `useNonStandardStacks`: A Boolean value indicating whether
  non-standard stacks are used.
- `specialFeatureOptIns`: A list of integers representing the special
  features that the user has opted into.
- `purposeConsent`: A list of integers representing the purposes for
  which the user has consented to.
- `purposesLITransparency`: A list of integers representing the
  purposes for which the user has given legitimate interest transparency.
- `purposeOneTreatment`: A Boolean value indicating whether the user
  has requested the "purpose one treatment" (that is, all purposes are treated
  equally).
- `publisherCountryCode`: The country code of the publisher.
- `vendorConsent`: A list of vendor IDs that the user has consented
  to.
- `vendorLegitimateInterest`: A list of vendor IDs for which the
  user's legitimate interest has been transparently communicated.
- `pubRestrictionEntry`: A list of publisher restrictions. This field
  contains the Purpose ID, Restriction Type, and List of Vendor IDs under that
  Purpose restriction.

**Disclosed vendor segment**

- `disclosedVendors`: A list of integers representing the vendors that
  have been disclosed to the user.

**Publisher purposes segment**

- `pubPurposesConsent`: A list of integers representing the
  publisher-specific purposes for which the user has given consent.
- `pubPurposesLITransparency`: A list of integers representing the
  publisher-specific purposes for which the user has given legitimate interest
  transparency.
- `customPurposesConsent`: A list of integers representing the custom
  purposes for which the user has given consent.
- `customPurposesLITransparency`: A list of integers representing the
  custom purposes for which the user has given legitimate interest
  transparency.

This detailed consent data can be used to understand and respect the user's privacy
preferences when working with personal data.

## Example

The following example takes a single argument, which is the encoded consent string.
It returns a dictionary containing the decoded consent data, including information about
the user's privacy preferences, consent choices, and other metadata.

```
from aws_clean_rooms.functions import consent_tcf_v2_decode

consent_string = "CO1234567890abcdef"
consent_data = consent_tcf_v2_decode(consent_string)

print(consent_data)
```

The basic structure of the returned consent data includes information about the
consent string version, the CMP (Consent Management Platform) details, the user's
consent and legitimate interest choices for different purposes and vendors, and other
metadata.

```

    /** core segment **/
    version: 2,
    created: "2023-10-01T12:00:00Z",
    lastUpdated: "2023-10-01T12:00:00Z",
    cmpId: 1234,
    cmpVersion: 5,
    consentScreen: 1,
    consentLanguage: "en",
    vendorListVersion: 2,
    tcfPolicyVersion: 2,
    isServiceSpecific: false,
    useNonStandardStacks: false,
    specialFeatureOptIns: [1, 2, 3],
    purposeConsent: [1, 2, 3],
    purposesLITransparency: [1, 2, 3],
    purposeOneTreatment: true,
    publisherCountryCode: "US",
    vendorConsent: [1, 2, 3],
    vendorLegitimateInterest: [1, 2, 3],
    pubRestrictionEntry: [
        { purpose: 1, restrictionType: 2, restrictionDescription: "Example restriction" },
    ],

    /** disclosed vendor segment **/
    disclosedVendors: [1, 2, 3],

    /** publisher purposes  segment **/
    pubPurposesConsent: [1, 2, 3],
    pubPurposesLITransparency: [1, 2, 3],
    customPurposesConsent: [1, 2, 3],
    customPurposesLITransparency: [1, 2, 3],
};
```

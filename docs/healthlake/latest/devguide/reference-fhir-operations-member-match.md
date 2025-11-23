# `$member-match` operation for HealthLake

AWS HealthLake now supports the `$member-match` operation for Patient resources, enabling healthcare organizations to find a member's unique identifier across different healthcare systems using demographic and coverage information. This operation is essential for achieving CMS compliance and facilitating secure payer-to-payer data exchange while maintaining patient privacy.

This operation is particularly useful when you need to:

- Enable secure healthcare data exchange between organizations
- Maintain patient continuity of care across different systems
- Support CMS compliance requirements
- Facilitate accurate member identification across healthcare networks

## Usage

The `$member-match` operation can be invoked on Patient resources using the POST method:

```
POST [base]/Patient/$member-match
```

## Supported Parameters

HealthLake supports the following FHIR `$member-match` parameters:

| Parameter       | Type     | Required | Default | Description                                                                      |
| --------------- | -------- | -------- | ------- | -------------------------------------------------------------------------------- |
| MemberPatient   | Patient  | Yes      | —       | Patient resource containing demographic information for the member to be matched |
| CoverageToMatch | Coverage | Yes      | —       | Coverage resource that will be used for matching against existing records        |
| CoverageToLink  | Coverage | No       | —       | Coverage resource to be linked during the matching process                       |
| Consent         | Consent  | No       | —       | Consent resource for authorization purposes                                      |

## Examples

### POST Request with Parameters

```
POST [base]/Patient/$member-match
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "MemberPatient",
      "resource": {
        "resourceType": "Patient",
        "name": [
          {
            "family": "Jones",
            "given": ["Sarah"]
          }
        ],
        "gender": "female",
        "birthDate": "1985-05-15"
      }
    },
    {
      "name": "CoverageToMatch",
      "resource": {
        "resourceType": "Coverage",
        "status": "active",
        "beneficiary": {
          "reference": "Patient/1"
        },
        "relationship": {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/subscriber-relationship",
              "code": "self",
              "display": "Self"
            }
          ]
        },
        "payor": [
          {
            "reference": "Organization/payer456"
          }
        ]
      }
    },
    {
      "name": "Consent",
      "resource": {
        "resourceType": "Consent",
        "status": "active",
        "scope": {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/consentscope",
              "code": "patient-privacy"
            }
          ]
        },
        "category": [
          {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
                "code": "IDSCL"
              }
            ]
          }
        ],
        "patient": {
          "reference": "Patient/1"
        },
        "performer": [
          {
            "reference": "Patient/patient123"
          }
        ],
        "sourceReference": {
          "reference": "Document/someconsent"
        },
        "policy": [
          {
            "uri": "http://hl7.org/fhir/us/davinci-hrex/StructureDefinition-hrex-consent.html#regular"
          }
        ]
      }
    }
  ]
}
```

### Sample Response

The operation returns a Parameters resource containing the matching results:

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "MemberIdentifier",
      "valueIdentifier": {
        "system": "http://hospital.org/medical-record-number",
        "value": "MRN-123456"
      }
    },
    {
      "name": "MemberId",
      "valueReference": {
        "reference": "Patient/patient123"
      }
    },
    {
      "name": "matchAlgorithm",
      "valueString": "DEMOGRAPHIC_MATCH"
    },
    {
      "name": "matchDetails",
      "valueString": "Demographic match: DOB + Name"
    },
    {
      "name": "matchedFields",
      "valueString": "given,birthdate,gender,family"
    }
  ]
}
```

## Response Parameters

The response includes the following parameters when a match is found:

| Parameter        | Type       | Description                                                                    |
| ---------------- | ---------- | ------------------------------------------------------------------------------ |
| MemberIdentifier | Identifier | The unique identifier for the matched member                                   |
| MemberId         | Reference  | Reference to the Patient resource                                              |
| matchAlgorithm   | String     | Type of match algorithm used (EXACT_MATCH, STRONG_MATCH, or DEMOGRAPHIC_MATCH) |
| matchDetails     | String     | Detailed information about the matching process                                |
| matchedFields    | String     | List of specific fields that were successfully matched                         |

## Matching Algorithms

The `$member-match` API employs a multi-tiered matching approach to ensure accurate member identification:

EXACT_MATCH

Uses Patient Identifier combined with Coverage SubscriberId

Provides the highest confidence level for member matching

STRONG_MATCH

Uses Patient Identifier with minimum coverage information

Offers high confidence when exact match criteria are not met

DEMOGRAPHIC_MATCH

Relies on basic demographic information

Used when identifier-based matching is not possible

## Behavior

The `$member-match` operation:

- Accepts patient demographics, coverage details, and optional consent information as input
- Returns a unique member identifier that can be used for subsequent interactions
- Implements multi-tiered matching (exact, strong, demographic) to ensure accurate member identification across different healthcare systems
- Saves any provided consent information for future authorization purposes
- Supports secure payer-to-payer data exchange while maintaining patient privacy
- Complies with CMS requirements for healthcare data exchange

## Authorization

The API uses SMART on FHIR authorization protocol with the following required scopes:

- `system/Patient.read`
- `system/Coverage.read`
- `system/Organization.read` (conditional)
- `system/Practitioner.read` (conditional)
- `system/PractitionerRole.read` (conditional)
- `system/Consent.write` (conditional)

## Error Handling

The operation handles the following error conditions:

- `400 Bad Request`: Invalid `$member-match` operation (non-conformant request or missing required parameters)
- `422 Unprocessable Entity`: No matching or multiple matches found

# `$member-remove` operation for HealthLake

The `$member-remove` operation allows you to remove members from a FHIR Member Attribution List (Group resource) in AWS HealthLake. This operation is part of the DaVinci Member Attribution Implementation Guide and supports the reconciliation process for managing member attributions.

## Prerequisites

- AWS HealthLake FHIR datastore
- Appropriate IAM permissions for HealthLake operations
- Member Attribution List (Group resource) in draft or open status

## Operation Details

Endpoint
`POST /Group/{id}/$member-remove`

Content Type
`application/fhir+json`

## Parameters

The operation accepts a FHIR Parameters resource with the following optional parameters:

| Parameter         | Cardinality | Type       | Description                                                                                 |
| ----------------- | ----------- | ---------- | ------------------------------------------------------------------------------------------- |
| memberId          | 0..1        | Identifier | Business identifier of the member to remove                                                 |
| providerNpi       | 0..1        | Identifier | NPI of the attributed provider                                                              |
| patientReference  | 0..1        | Reference  | Direct reference to the Patient resource                                                    |
| providerReference | 0..1        | Reference  | Direct reference to the Provider resource (Practitioner, PractitionerRole, or Organization) |
| coverageReference | 0..1        | Reference  | Reference to the Coverage resource                                                          |

### Supported Parameter Combinations

The following parameter combinations are supported:

- `memberId` only - Removes all attributions for the specified member
- `memberId` + `providerNpi` - Removes attributions for the specific member-provider combination
- `patientReference` only - Removes all attributions for the specified patient
- `patientReference` + `providerReference` - Removes attributions for the specific patient-provider combination
- `patientReference` + `providerReference` + `coverageReference` - Removes the specific attribution based on patient, provider, and coverage

## Request Example

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "patientReference",
      "valueReference": {
        "reference": "Patient/12345"
      }
    },
    {
      "name": "providerReference",
      "valueReference": {
        "reference": "Practitioner/67890"
      }
    }
  ]
}
```

## Response

### Successful Response

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "result",
      "valueBoolean": true
    },
    {
      "name": "effectiveDate",
      "valueDate": "2024-06-30"
    },
    {
      "name": "status",
      "valueCode": "inactive"
    },
    {
      "name": "message",
      "valueString": "Member successfully removed from attribution list"
    }
  ]
}
```

## Behavior

Status Requirements

The operation only works on attribution lists with status `draft` or `open`

Lists with `final` status will reject the operation with a 422 error

Member Removal Process

_Draft Status Lists_: Members are marked as inactive (`inactive: true`) and their `changeType` extension is updated to `changed`

_Open Status Lists_: Similar behavior to draft status

_Final Status Lists_: Operation is rejected

Validation

References are validated to ensure they exist in the HealthLake datastore

If both identifier and reference are provided for the same resource type, they must correspond to the same resource

Parameter combinations are validated according to the supported patterns

## Error Handling

### Common Error Responses

Resource Not Found (404)

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "not-found",
      "details": {
        "text": "Patient with identifier 'http://example.org/fhir/identifiers|99999' not found in system"
      },
      "diagnostics": "Cannot remove member from attribution list. Verify patient identifier and try again.",
      "expression": ["memberId"]
    }
  ]
}
```

Attribution List Final Status (422)

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "business-rule",
      "details": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/us/davinci-atr/CodeSystem/atr-error-codes",
            "code": "list-final",
            "display": "Attribution list is final and cannot be modified"
          }
        ]
      },
      "diagnostics": "Cannot modify attribution list with status 'final'. List modifications are not permitted after finalization.",
      "expression": ["Group.status"]
    }
  ]
}
```

Invalid Operation (400)

Returned when parameter combinations are invalid or malformed.

Multiple Matches Found (412)

Returned when the provided parameters match multiple members in the attribution list.

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "processing",
      "diagnostics": "Multiple members found matching the criteria"
    }
  ]
}
```

## Best Practices

- _Use Specific Parameters_: When possible, use the most specific parameter combination to avoid unintended removals
- _Check List Status_: Verify the attribution list status before attempting removals
- _Handle Errors Gracefully_: Implement proper error handling for all possible error conditions
- _Validate References_: Ensure all referenced resources exist before making the request

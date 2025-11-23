# FHIR R4 `$attribution-status` operation for HealthLake

Retrieves the attribution status for a specific member, returning a Bundle containing all attribution resources related to the Patient. This operation is part of the [FHIR Member Attribution (ATR) List IG 2.1.0 implementation.](https://build.fhir.org/ig/HL7/davinci-atr/spec.html "https://build.fhir.org/ig/HL7/davinci-atr/spec.html")

## Endpoint

```
POST [base]/Group/[id]/$attribution-status
```

## Request Parameters

The operation accepts the following optional parameters:

| Parameter        | Type       | Description                                                         |
| ---------------- | ---------- | ------------------------------------------------------------------- |
| memberId         | Identifier | The MemberId of the member for whom attribution status is requested |
| patientReference | Reference  | Reference to the patient resource in the Producer's system          |

###### Note

Either `memberId` or `patientReference` can be provided, or both for validation purposes.

## Sample Request

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "memberId",
      "valueIdentifier": {
        "system": "http://example.org",
        "value": "MBR123456789"
      }
    },
    {
      "name": "patientReference",
      "valueReference": {
        "reference": "Patient/patient-123",
        "display": "John Doe"
      }
    }
  ]
}
```

## Response

Returns a Bundle containing attribution resources related to the Patient:

| Resource                                   | Cardinality | Location                                  |
| ------------------------------------------ | ----------- | ----------------------------------------- |
| Patient                                    | 1..1        | Group.member.entity                       |
| Coverage                                   | 0..1        | Group.member.extension:coverageReference  |
| Organization/Practitioner/PractitionerRole | 0..1        | Group.member.extension:attributedProvider |
| Any Resource                               | 0..1        | Group.member.extension:associatedData     |

### Sample Response

```
{
  "resourceType": "Bundle",
  "id": "bundle-response",
  "meta": {
    "lastUpdated": "2014-08-18T01:43:33Z"
  },
  "type": "collection",
  "entry": [
    {
      "fullUrl": "http://example.org/fhir/Patient/12423",
      "resource": {
        "resourceType": "Patient",
        "id": "12423",
        "meta": {
          "versionId": "1",
          "lastUpdated": "2014-08-18T01:43:31Z"
        },
        "active": true,
        "name": [
          {
            "use": "official",
            "family": "Chalmers",
            "given": ["Peter", "James"]
          }
        ],
        "gender": "male",
        "birthDate": "1974-12-25"
      }
    },
    {
      "fullUrl": "http://example.org/fhir/Coverage/123456",
      "resource": {
        "resourceType": "Coverage",
        "id": "1"
        // ... additional Coverage resource details
      }
    },
    {
      "fullUrl": "http://example.org/fhir/Organization/666666",
      "resource": {
        "resourceType": "Organization",
        "id": "2"
        // ... additional Organization resource details
      }
    }
  ]
}
```

## Error Handling

The operation handles the following error conditions:

| Error                      | HTTP Status | Description                                    |
| -------------------------- | ----------- | ---------------------------------------------- |
| Invalid operation request  | 400         | Non-conformant request parameters or structure |
| Group resource not found   | 404         | The specified Group ID does not exist          |
| Patient resource not found | 404         | The specified Patient reference does not exist |

## Authorization and Security

SMART Scope Requirements

Clients must have appropriate privileges to read Group resources and related attribution resources

Standard FHIR authorization mechanisms apply to all operations

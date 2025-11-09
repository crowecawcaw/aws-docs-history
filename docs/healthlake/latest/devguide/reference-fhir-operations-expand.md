# Retrieving ValueSet Codes with `$expand`

AWS HealthLake now supports the `$expand` operation for ValueSets that were ingested by you as a customer, enabling you to retrieve the complete list of codes contained within those ValueSet resource(s). This operation is particularly useful when you need to:

- Retrieve all possible codes for validation purposes
- Display available options in user interfaces
- Perform comprehensive code lookups within a specific terminology context

## Usage

The `$expand` operation can be invoked on ValueSet resources using both GET and POST methods:

###### Supported Operations

```
GET/POST [base]/ValueSet/[id]/$expand
GET [base]/ValueSet/$expand?url=http:`//example.com`
POST [base]/ValueSet/$expand
```

## Supported Parameters

HealthLake supports a subset of FHIR R4 `$expand` parameters:

| Parameter | Type    | Required | Description                                                                                                                                                              |
| --------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `url`     | uri     | No       | Canonical URL of the ValueSet to expand                                                                                                                                  |
| `id`      | id      | No       | ValueSet resource id to expand (for GET or POST operations)                                                                                                              |
| `filter`  | string  | No       | Filter the code expansion result                                                                                                                                         |
| `count`   | integer | No       | Number of codes to return                                                                                                                                                |
| `offset`  | integer | No       | Number of matching codes to skip before returning. Applies after filtering and only to the matching codes, not to the full, unfiltered contents of the original ValueSet |

## Examples

###### GET Request by ID

```
GET [base]/ValueSet/example-valueset/$expand
```

###### GET Request by URL with Filter

```
GET [base]/ValueSet/$expand?url=http:`//example.com/ValueSet/my-valueset&filter=male&count=5`
```

###### POST Request with Parameters (by ID)

```
POST [base]/ValueSet/example-valueset/$expand
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "count",
      "valueInteger": 10
    },
    {
      "name": "filter",
      "valueString": "admin"
    }
  ]
}
```

###### POST Request with Parameters (by URL)

```
POST [base]/ValueSet/$expand
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "url",
      "valueUri": "http://hl7.org/fhir/ValueSet/administrative-gender"
    },
    {
      "name": "count",
      "valueInteger": 10
    }
  ]
}
```

###### Sample Response

The operation returns a ValueSet resource with an `expansion` element containing the expanded codes:

```
{
  "resourceType": "ValueSet",
  "id": "administrative-gender",
  "status": "active",
  "expansion": {
    "identifier": "urn:uuid:12345678-1234-1234-1234-123456789abc",
    "timestamp": "2024-01-15T10:30:00Z",
    "total": 4,
    "parameter": [
      {
        "name": "count",
        "valueInteger": 10
      }
    ],
    "contains": [
      {
        "system": "http://hl7.org/fhir/administrative-gender",
        "code": "male",
        "display": "Male"
      },
      {
        "system": "http://hl7.org/fhir/administrative-gender",
        "code": "female",
        "display": "Female"
      },
      {
        "system": "http://hl7.org/fhir/administrative-gender",
        "code": "other",
        "display": "Other"
      },
      {
        "system": "http://hl7.org/fhir/administrative-gender",
        "code": "unknown",
        "display": "Unknown"
      }
    ]
  }
}
```

The response includes:

- expansion.total: Total number of codes in the expanded ValueSet
- expansion.contains: Array of expanded codes with their system, code, and display values
- expansion.parameter: Parameters used in the expansion request

For more information about the `$expand` operation specification, see the [FHIR R4 ValueSet `$expand`](https://build.fhir.org/valueset-operation-expand.html "https://build.fhir.org/valueset-operation-expand.html") documentation.

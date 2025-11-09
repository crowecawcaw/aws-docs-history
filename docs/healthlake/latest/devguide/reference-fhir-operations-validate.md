# Validating FHIR Resources with `$validate`

AWS HealthLake now supports the `$validate` operation for FHIR resources, enabling you to validate a resource against the FHIR specification and check its conformance to a specified profile or base resource definition without performing any storage operations. This operation is particularly useful when you need to:

- Validate FHIR CMS compliance requirements
- Test resources prior to using them in production
- Provide real-time validation feedback as users edit clinical data
- Reduce invalid data submissions to create and update APIs

## Usage

The `$validate` operation can be invoked on FHIR resources using POST methods:

###### Supported Operations

```
POST [base]/[type]/[id]/$validate
POST [base]/[type]/$validate
```

## Supported Payloads

###### Parameters resource

HealthLake supports the following FHIR `$validate` parameters:

| Parameter  | Type      | Required | Description                                      |
| ---------- | --------- | -------- | ------------------------------------------------ |
| `resource` | Resource  | Yes      | The resource to be validated                     |
| `profile`  | canonical | No       | Canonical URL of the profile to validate against |
| `mode`     | code      | No       | Validation mode: `create`, or `update`           |

###### Direct resource with Query Parameters

| Parameter | Type      | Required | Description                                      |
| --------- | --------- | -------- | ------------------------------------------------ |
| `profile` | canonical | No       | Canonical URL of the profile to validate against |
| `mode`    | code      | No       | Validation mode: `create`, or `update`           |

## Examples

###### POST Request for Resource with ID and Parameters payload

```
POST [base]/Patient/example-patient/$validate
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "resource",
      "resource": {
        "resourceType": "Patient",
        "id": "example-patient",
        "name": [
          {
            "family": "Smith",
            "given": ["John"]
          }
        ],
        "gender": "male",
        "birthDate": "1990-01-01"
      }
    },
    {
      "name": "profile",
      "valueCanonical": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
    },
    {
      "name": "mode",
      "valueString": "create"
    }
  ]
}
```

###### POST Request for Resource Type and Parameters payload

```
POST [base]/Patient/$validate
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "resource",
      "resource": {
        "resourceType": "Patient",
        "name": [
          {
            "family": "Doe",
            "given": ["Jane"]
          }
        ],
        "gender": "female",
        "birthDate": "1985-05-15"
      }
    },
    {
      "name": "profile",
      "valueCanonical": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
    },
    {
      "name": "mode",
      "valueString": "update"
    }
  ]
}
```

###### POST Request for Resource with ID and direct resource payload

```
POST [base]/Patient/example-patient/$validate?profile=`http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient&mode=create`
Content-Type: application/fhir+json

{
    "resourceType": "Patient",
    "id": "example-patient",
    "name": [
        {
        "family": "Smith",
        "given": ["John"]
        }
    ],
    "gender": "male",
    "birthDate": "1990-01-01"
}
```

###### POST Request for Resource Type and direct resource payload

```
POST [base]/Patient/$validate?profile=`http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient&mode=create`
Content-Type: application/fhir+json

{
    "resourceType": "Patient",
    "id": "example-patient",
    "name": [
        {
        "family": "Smith",
        "given": ["John"]
        }
    ],
    "gender": "male",
    "birthDate": "1990-01-01"
}
```

###### Sample Response

The operation returns an OperationOutcome resource with validation results:

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "information",
      "code": "informational",
      "diagnostics": "Validation successful"
    }
  ]
}
```

###### Sample Response with Validation Errors

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "required",
      "details": {
        "text": "Missing required element"
      },
      "diagnostics": "Patient.identifier is required by the US Core Patient profile",
      "location": [
        "Patient.identifier"
      ]
    },
    {
      "severity": "warning",
      "code": "code-invalid",
      "details": {
        "text": "Invalid code value"
      },
      "diagnostics": "The provided gender code is not from the required value set",
      "location": [
        "Patient.gender"
      ]
    }
  ]
}
```

## Behavior

The `$validate` operation:

1. Validates the resource against the FHIR specification and base resource definition
2. Checks conformance to specified profiles when the `profile` parameter is provided
3. Validates based on the specified mode (`create` or `update`)
4. Returns detailed validation results including errors, warnings, and informational messages
5. Does not perform any storage operations - validation only
6. Returns HTTP 200 OK when validation can be performed, regardless of whether validation issues are found

## Validation Modes

- **create**: Validates the resource as if it were being created (new resource)
- **update**: Validates the resource as if it were being updated (existing resource)

## Error Handling

The operation returns:

- 200 OK: Validation was performed successfully (regardless of validation outcome)
- 400 Bad Request: Invalid request format or parameters
- 404 Not Found: Resource type or profile not found

For more information about the `$validate` operation specification, see the [FHIR R4 Resource `$validate`](https://www.hl7.org/fhir/R4/operation-resource-validate.html "https://www.hl7.org/fhir/R4/operation-resource-validate.html") documentation.

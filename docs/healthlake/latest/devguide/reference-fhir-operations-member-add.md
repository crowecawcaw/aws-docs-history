

# `$member-add` operation for HealthLake
<a name="reference-fhir-operations-member-add"></a>

The FHIR `$member-add` operation adds a member (patient) to a Group resource, specifically a Member Attribution List. This operation is part of the DaVinci Member Attribution Implementation Guide and supports the reconciliation process for managing member attributions.

## Operation Endpoint
<a name="member-add-endpoint"></a>

```
POST [base]/datastore/{datastoreId}/r4/Group/{groupId}/$member-add
Content-Type: application/json
```

## Parameters
<a name="member-add-parameters"></a>

The operation accepts a FHIR Parameters resource with the following parameter combinations:

### Parameter Options
<a name="member-add-parameter-options"></a>

You can use one of the following parameter combinations:

Option 1: Member ID \+ Provider NPI  
`memberId` \+ `providerNpi`  
`memberId` \+ `providerNpi` \+ `attributionPeriod`

Option 2: Patient Reference \+ Provider Reference  
`patientReference` \+ `providerReference`  
`patientReference` \+ `providerReference` \+ `attributionPeriod`

### Parameter Details
<a name="member-add-parameter-details"></a>

memberId (Optional)  
The identifier of the member to be added to the Group.  
Type: Identifier  
System: Patient identifier system  

```
{
  "name": "memberId",
  "valueIdentifier": {
    "system": "http://example.org/patient-id",
    "value": "patient-new"
  }
}
```

providerNpi (Optional)  
The National Provider Identifier (NPI) of the attributed provider.  
Type: Identifier  
System: http://terminology.hl7.org/CodeSystem/NPI  

```
{
  "name": "providerNpi",
  "valueIdentifier": {
    "system": "http://terminology.hl7.org/CodeSystem/NPI",
    "value": "1234567890"
  }
}
```

patientReference (Optional)  
Direct reference to the patient resource to be added.  
Type: Reference  

```
{
  "name": "patientReference",
  "valueReference": {
    "reference": "Patient/patient-123"
  }
}
```

providerReference (Optional)  
Direct reference to the provider resource.  
Type: Reference  

```
{
  "name": "providerReference",
  "valueReference": {
    "reference": "Practitioner/provider-456"
  }
}
```

attributionPeriod (Optional)  
The time period over which the patient is attributed to the provider.  
Type: Period  

```
{
  "name": "attributionPeriod",
  "valuePeriod": {
    "start": "2024-07-15",
    "end": "2025-07-14"
  }
}
```

## Request Examples
<a name="member-add-examples"></a>

### Using Member ID and Provider NPI
<a name="member-add-example-id-npi"></a>

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "memberId",
      "valueIdentifier": {
        "system": "http://example.org/patient-id",
        "value": "patient-new"
      }
    },
    {
      "name": "providerNpi",
      "valueIdentifier": {
        "system": "http://terminology.hl7.org/CodeSystem/NPI",
        "value": "1234567890"
      }
    },
    {
      "name": "attributionPeriod",
      "valuePeriod": {
        "start": "2024-07-15",
        "end": "2025-07-14"
      }
    }
  ]
}
```

### Using Patient and Provider References
<a name="member-add-example-references"></a>

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "patientReference",
      "valueReference": {
        "reference": "Patient/patient-123"
      }
    },
    {
      "name": "providerReference",
      "valueReference": {
        "reference": "Practitioner/provider-456"
      }
    },
    {
      "name": "attributionPeriod",
      "valuePeriod": {
        "start": "2024-07-15",
        "end": "2025-07-14"
      }
    }
  ]
}
```

## Response Format
<a name="member-add-response"></a>

### Successful Addition Response
<a name="member-add-success-response"></a>

```
HTTP Status: 200 OK
Content-Type: application/fhir+json

{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "success",
      "code": "informational",
      "details": {
        "text": "Member Patient/patient-new successfully added to the Member Attribution List."
      }
    }
  ]
}
```

### Error Responses
<a name="member-add-error-responses"></a>

Invalid Request Syntax  
HTTP Status: 400 Bad Request  

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "invalid",
      "details": {
        "text": "Invalid parameter combination provided"
      }
    }
  ]
}
```

Resource Not Found  
HTTP Status: 404 Not Found  

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "not-found",
      "details": {
        "text": "Resource not found."
      }
    }
  ]
}
```

Version Conflict  
HTTP Status: 409 Conflict  

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "conflict",
      "details": {
        "text": "Resource version conflict detected"
      }
    }
  ]
}
```

Invalid Attribution Status  
HTTP Status: 422 Unprocessable Entity  

```
{
  "resourceType": "OperationOutcome",
  "issue": [
    {
      "severity": "error",
      "code": "business-rule",
      "details": {
        "text": "Cannot add member to Attribution List with status 'final'. Status must be 'draft' or 'open'."
      }
    }
  ]
}
```

## Business Rules
<a name="member-add-business-rules"></a>

Attribution Status Validation  
The operation can only be performed when the Group's Attribution Status is:  
+ `draft`
+ `open`
Operations are not allowed when the status is `final`.

Duplicate Member Prevention  
The system prevents adding duplicate members based on the unique combination of:  
+ Member Identifier
+ Payer Identifier
+ Coverage Identifier

Coverage Period Validation  
When an `attributionPeriod` is provided, it must fall within the bounds of the member's coverage period. The system will:  
+ Search for the member's Coverage resource
+ Use the most recent Coverage (highest versionId) if multiple exist
+ Validate that the attribution period does not exceed the coverage period

Reference Validation  
When both ID and reference are provided for the same resource (patient or provider), the system validates that they correspond to the same resource.  
When both ID and reference.identifier fields are provided for the same resource (patient or provider), an error is thrown.

## Authentication & Authorization
<a name="member-add-auth"></a>

The operation requires SMART on FHIR authorization for:
+ Read permissions - To validate patient, provider, and group resources
+ Search permissions - To find resources by identifier
+ Update permissions - To modify the Group resource

## Operational Behavior
<a name="member-add-behavior"></a>

Resource Updates  
+ Updates the Group resource version ID
+ Creates a history entry with the original resource state before the operation
+ Adds member information to the Group.member array with:
  + Patient reference in entity.reference
  + Attribution period in period
  + Coverage and provider information in extension fields

Validation Steps  
+ Parameter Validation - Ensures valid parameter combinations
+ Resource Existence - Validates patient, provider, and group resources exist
+ Attribution Status - Confirms group status allows modifications
+ Duplicate Check - Prevents adding existing members
+ Coverage Validation - Ensures attribution period is within coverage bounds

## Limitations
<a name="member-add-limitations"></a>
+ All referenced resources must exist within the same datastore
+ Operation only works with Member Attribution List Group resources
+ Attribution periods must be within coverage bounds
+ Cannot modify groups with "final" status
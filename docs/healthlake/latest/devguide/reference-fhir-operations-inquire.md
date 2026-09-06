

# FHIR `$inquire` operation for HealthLake
<a name="reference-fhir-operations-inquire"></a>

The `$inquire` operation enables you to check the status of a previously submitted prior authorization request. This operation implements the [Da Vinci Prior Authorization Support (PAS) Implementation Guide](https://hl7.org/fhir/us/davinci-pas/), providing a standardized FHIR-based workflow to retrieve the current authorization decision.

## How it works
<a name="inquire-how-it-works"></a>
+ **Submit Inquiry**: You send a FHIR Bundle containing the Claim you want to check and supporting information
+ **Search**: HealthLake searches for the corresponding ClaimResponse in your data store
+ **Retrieve**: The most recent authorization status is retrieved
+ **Respond**: You receive an immediate response with the current authorization status (queued, approved, denied, etc.)

**Note**  
`$inquire` is a **read-only operation** that retrieves existing authorization status. It does not modify or update any resources in your data store.

## API endpoint
<a name="inquire-api-endpoint"></a>

```
POST /datastore/{datastoreId}/r4/Claim/$inquire  
Content-Type: application/fhir+json
```

## Request structure
<a name="inquire-request-structure"></a>

### Bundle requirements
<a name="inquire-bundle-requirements"></a>

Your request must be a FHIR Bundle resource with:
+ **Bundle.type**: Must be `"collection"`
+ **Bundle.entry**: Must contain exactly **one** Claim resource with:
  + `use = "preauthorization"`
  + `status = "active"`
+ **Referenced Resources**: All resources referenced by the Claim must be included in the Bundle

**Query-by-Example**  
The resources in your input Bundle serve as a search template. HealthLake uses the information provided to locate the corresponding ClaimResponse.

### Required resources
<a name="inquire-required-resources"></a>


| Resource | Cardinality | Profile | Description | 
| --- | --- | --- | --- | 
| Claim | 1 | PAS Claim Inquiry | The prior authorization you're inquiring about | 
| Patient | 1 | PAS Beneficiary Patient | Patient demographic information | 
| Organization (Insurer) | 1 | PAS Insurer Organization | Insurance company | 
| Organization (Provider) | 1 | PAS Requesting Organization | Healthcare provider who submitted the request | 

### Important search criteria
<a name="inquire-search-criteria"></a>

HealthLake searches for the ClaimResponse using:
+ **Patient reference** from the Claim
+ **Insurer reference** from the Claim
+ **Provider reference** from the Claim
+ **Created date** from the Claim (as a time filter)

**Patient-Specific Queries Only**  
All inquiries must be tied to a specific patient. System-wide queries without patient identification are not permitted.

## Example request
<a name="inquire-example-request"></a>

```
POST /datastore/example-datastore/r4/Claim/$inquire  
Content-Type: application/fhir+json  
Authorization: Bearer <your-token>  
  
{  
  "resourceType": "Bundle",  
  "id": "PASClaimInquiryBundleExample",  
  "meta": {  
    "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-pas-inquiry-request-bundle"]  
  },  
  "identifier": {  
    "system": "http://example.org/SUBMITTER_TRANSACTION_IDENTIFIER",  
    "value": "5269368"  
  },  
  "type": "collection",  
  "timestamp": "2005-05-02T14:30:00+05:00",  
  "entry": [  
    {  
      "fullUrl": "http://example.org/fhir/Claim/MedicalServicesAuthorizationExample",  
      "resource": {  
        "resourceType": "Claim",  
        "id": "MedicalServicesAuthorizationExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim-inquiry"]  
        },  
        "status": "active",  
        "type": {  
          "coding": [{  
            "system": "http://terminology.hl7.org/CodeSystem/claim-type",  
            "code": "professional"  
          }]  
        },  
        "use": "preauthorization",  
        "patient": {  
          "reference": "Patient/SubscriberExample"  
        },  
        "created": "2005-05-02T11:01:00+05:00",  
        "insurer": {  
          "reference": "Organization/InsurerExample"  
        },  
        "provider": {  
          "reference": "Organization/UMOExample"  
        }  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Patient/SubscriberExample",  
      "resource": {  
        "resourceType": "Patient",  
        "id": "SubscriberExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-beneficiary"]  
        },  
        "name": [{  
          "family": "SMITH",  
          "given": ["JOE"]  
        }],  
        "gender": "male"  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Organization/UMOExample",  
      "resource": {  
        "resourceType": "Organization",  
        "id": "UMOExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-requestor"]  
        },  
        "name": "Provider Organization"  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Organization/InsurerExample",  
      "resource": {  
        "resourceType": "Organization",  
        "id": "InsurerExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-insurer"]  
        },  
        "name": "Insurance Company"  
      }  
    }  
  ]  
}
```

## Response format
<a name="inquire-response-format"></a>

### Success response (200 OK)
<a name="inquire-success-response"></a>

You'll receive a PAS Inquiry Response Bundle containing:
+ **ClaimResponse** with the current authorization status; multiple **ClaimResponse** if it matches search criteria
+ All original resources from your request (echoed back)
+ Timestamp of when the response was assembled

**Possible ClaimResponse Outcomes**  



| Outcome | Description | 
| --- | --- | 
| queued | Authorization request is still pending review | 
| complete | Authorization decision has been made (check disposition for approved/denied) | 
| error | An error occurred during processing | 
| partial | Partial authorization granted | 

```
{  
  "resourceType": "Bundle",  
  "identifier": {  
        "system": "http://example.org/SUBMITTER_TRANSACTION_IDENTIFIER",  
        "value": "5269367"  
  },  
  "type": "collection",  
  "timestamp": "2005-05-02T14:30:15+05:00",  
  "entry": [  
    {  
      "fullUrl": "http://example.org/fhir/ClaimResponse/InquiryResponseExample",  
      "resource": {  
        "resourceType": "ClaimResponse",  
        "id": "InquiryResponseExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claimresponse-inquiry"]  
        },  
        "status": "active",  
        "type": {  
          "coding": [{  
            "system": "http://terminology.hl7.org/CodeSystem/claim-type",  
            "code": "professional"  
          }]  
        },  
        "use": "preauthorization",  
        "patient": {  
          "reference": "Patient/SubscriberExample"  
        },  
        "created": "2005-05-02T11:05:00+05:00",  
        "insurer": {  
          "reference": "Organization/InsurerExample"  
        },  
        "request": {  
          "reference": "Claim/MedicalServicesAuthorizationExample"  
        },  
        "outcome": "complete",  
        "disposition": "Approved",  
        "preAuthRef": "AUTH12345"  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Claim/MedicalServicesAuthorizationExample",  
      "resource": {  
        "resourceType": "Claim",  
        "id": "MedicalServicesAuthorizationExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim-inquiry"]  
        },  
        "status": "active",  
        "type": {  
          "coding": [{  
            "system": "http://terminology.hl7.org/CodeSystem/claim-type",  
            "code": "professional"  
          }]  
        },  
        "use": "preauthorization",  
        "patient": {  
          "reference": "Patient/SubscriberExample"  
        },  
        "created": "2005-05-02T11:01:00+05:00",  
        "insurer": {  
          "reference": "Organization/InsurerExample"  
        },  
        "provider": {  
          "reference": "Organization/UMOExample"  
        }  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Patient/SubscriberExample",  
      "resource": {  
        "resourceType": "Patient",  
        "id": "SubscriberExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-beneficiary"]  
        },  
        "name": [{  
          "family": "SMITH",  
          "given": ["JOE"]  
        }],  
        "gender": "male"  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Organization/UMOExample",  
      "resource": {  
        "resourceType": "Organization",  
        "id": "UMOExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-requestor"]  
        },  
        "name": "Provider Organization"  
      }  
    },  
    {  
      "fullUrl": "http://example.org/fhir/Organization/InsurerExample",  
      "resource": {  
        "resourceType": "Organization",  
        "id": "InsurerExample",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-insurer"]  
        },  
        "name": "Insurance Company"  
      }  
    }  
  ]  
}
```

## Error responses
<a name="inquire-error-responses"></a>

### 400 Bad Request
<a name="inquire-400-error"></a>

Returned when the request format is invalid or validation fails.

```
{  
    "resourceType": "OperationOutcome",  
    "issue": [  
        {  
            "severity": "error",  
            "code": "required",  
            "diagnostics": "Reference 'Patient/SubscriberExample' at path 'patient' for 'CLAIM' resource not found(at Bundle.entry[0].resource)"  
        }  
    ]  
}
```

### 401 Unauthorized
<a name="inquire-401-error"></a>

Returned when authentication credentials are missing or invalid.

```
{  
    "resourceType": "OperationOutcome",  
    "issue": [  
        {  
            "severity": "error",  
            "code": "forbidden",  
            "diagnostics": "Invalid authorization header"  
        }  
    ]  
}
```

### 403 Forbidden
<a name="inquire-403-error"></a>

Returned when the authenticated user lacks permission to access the requested resource.

```
{  
    "resourceType": "OperationOutcome",  
    "issue": [  
        {  
            "severity": "error",  
            "code": "exception",  
            "diagnostics": "Insufficient SMART scope permissions."  
        }  
    ]  
}
```

### 400 When none found
<a name="inquire-400-none-found"></a>

Returned when no matching ClaimResponse is found for the inquiry.

```
{  
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "not-found",
    "diagnostics": "Resource not found. No ClaimResponse found from the input Claim that matches the specified Claim properties patient, insurer, provider, and created(at Bundle.entry[0].resource)"
  }]
}
```

### 415 Unsupported Media Type
<a name="inquire-415-error"></a>

Returned when the Content-Type header is not application/fhir\+json.

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "error",  
    "code": "value",  
    "diagnostics": "Incorrect MIME-type. Update request Content-Type header."  
  }]  
}
```

### 429 Too Many Requests
<a name="inquire-429-error"></a>

Returned when rate limits are exceeded.

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "error",  
    "code": "throttled",  
    "diagnostics": "Rate limit exceeded. Please retry after some time."  
  }]  
}
```

## Validation rules
<a name="inquire-validation-rules"></a>

HealthLake performs comprehensive validation on your inquiry:

### Bundle validation
<a name="inquire-bundle-validation"></a>
+ Must conform to PAS Inquiry Request Bundle profile
+ `Bundle.type` must be `"collection"`
+ Must contain exactly one Claim resource
+ All referenced resources must be included in the Bundle

### Claim validation
<a name="inquire-claim-validation"></a>
+ Must conform to PAS Claim Inquiry profile
+ `Claim.use` must be `"preauthorization"`
+ `Claim.status` must be `"active"`
+ Required fields: `patient`, `insurer`, `provider`, `created`

### Resource validation
<a name="inquire-resource-validation"></a>
+ All resources must conform to their respective PAS Inquiry profiles
+ Required supporting resources must be present (Patient, Insurer Organization, Provider Organization)
+ Cross-references must be valid and resolvable within the Bundle

## Performance specifications
<a name="inquire-performance-specs"></a>


| Metric | Specification | 
| --- | --- | 
| Resource Count Limit | 500 resources per Bundle | 
| Bundle Size Limit | 5 MB maximum | 

## Required permissions
<a name="inquire-required-permissions"></a>

To use the `$inquire` operation, ensure your IAM role has:
+ `healthlake:InquirePreAuthClaim` - To call the operation

**SMART on FHIR Scopes**  
**Minimum required scopes:**
+ **SMART v1**: `user/ClaimResponse.read`
+ **SMART v2**: `user/ClaimResponse.s`

## Important implementation notes
<a name="inquire-implementation-notes"></a>

### Search behavior
<a name="inquire-search-behavior"></a>

When you submit an inquiry, HealthLake searches for the ClaimResponse using:
+ **Patient reference** from the input Claim
+ **Insurer reference** from the input Claim
+ **Provider reference** from the input Claim
+ **Created date** from the input Claim (as a time filter)

**Multiple Matches**: If multiple ClaimResponses match your search criteria, HealthLake returns all matching results. You should use the most recent `ClaimResponse.created` timestamp to identify the latest status.

### Updated claims
<a name="inquire-updated-claims"></a>

If you've submitted multiple updates to the same prior authorization (e.g., Claim v1.1, v1.2, v1.3), the `$inquire` operation will retrieve the ClaimResponse associated with the **most recent version** based on the search criteria provided.

### Read-only operation
<a name="inquire-read-only"></a>

The `$inquire` operation:
+ **Does** retrieve existing authorization status
+ **Does** return the most recent ClaimResponse
+ **Does not** modify or update any resources
+ **Does not** create new resources
+ **Does not** trigger new authorization processing

## Workflow example
<a name="inquire-workflow-example"></a>

**Typical Prior Authorization Inquiry Workflow**  


```
1. Provider submits PA request  
   POST /Claim/$submit  
   → Returns ClaimResponse with outcome="queued"  
  
2. Payer reviews request (asynchronous)  
   → Updates ClaimResponse status internally  
  
3. Provider checks status  
   POST /Claim/$inquire  
   → Returns ClaimResponse with outcome="queued" (still pending)  
  
4. Provider checks status again later  
   POST /Claim/$inquire  
   → Returns ClaimResponse with outcome="complete", disposition="Approved"
```

## Related operations
<a name="inquire-related-operations"></a>
+ `Claim/$submit` - Submit a new prior authorization request or update an existing one
+ `Patient/$everything` - Retrieve comprehensive patient data for prior authorization context
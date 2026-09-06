

# FHIR `$submit` operation for HealthLake
<a name="reference-fhir-operations-submit"></a>

The `$submit` operation enables you to electronically submit prior authorization requests to payers for approval. This operation implements the [Da Vinci Prior Authorization Support (PAS) Implementation Guide](https://hl7.org/fhir/us/davinci-pas/), providing a standardized FHIR-based workflow for prior authorization submissions.

## How it works
<a name="submit-how-it-works"></a>
+ **Submit**: You send a FHIR Bundle containing your prior authorization request and supporting clinical data
+ **Validate**: HealthLake validates the submission against PAS requirements
+ **Persist**: All resources are stored in your HealthLake data store
+ **Respond**: You receive an immediate response with "queued" status
+ **Process**: The authorization decision is processed asynchronously by the payer

## API endpoint
<a name="submit-api-endpoint"></a>

```
POST /datastore/{datastoreId}/r4/Claim/$submit  
Content-Type: application/fhir+json
```

## Request structure
<a name="submit-request-structure"></a>

### Bundle requirements
<a name="submit-bundle-requirements"></a>

Your request must be a FHIR Bundle resource with:
+ **Bundle.type**: Must be `"collection"`
+ **Bundle.entry**: Must contain exactly **one** Claim resource with `use = "preauthorization"`
+ **Referenced Resources**: All resources referenced by the Claim must be included in the Bundle

### Required resources
<a name="submit-required-resources"></a>


| Resource | Cardinality | Profile | Description | 
| --- | --- | --- | --- | 
| Claim | 1 | PAS Claim | The prior authorization request | 
| Patient | 1 | PAS Patient | Patient demographic information | 
| Organization (Insurer) | 1 | PAS Insurer | Insurance company | 
| Organization (Provider) | 1 | PAS Requestor | Healthcare provider submitting the request | 
| Coverage | 1 or more | PAS Coverage | Insurance coverage details | 

### Optional resources
<a name="submit-optional-resources"></a>


| Resource | Cardinality | Profile | Description | 
| --- | --- | --- | --- | 
| Practitioner | 0 or more | PAS Practitioner | Healthcare practitioners | 
| PractitionerRole | 0 or more | PAS PractitionerRole | Practitioner roles | 
| ServiceRequest | 0 or more | PAS ServiceRequest | Requested medical services | 
| DeviceRequest | 0 or more | PAS DeviceRequest | Requested medical devices | 
| MedicationRequest | 0 or more | PAS MedicationRequest | Requested medications | 
| DocumentReference | 0 or more | PAS DocumentReference | Supporting clinical documentation | 

## Example request
<a name="submit-example-request"></a>

```
POST /datastore/example-datastore/r4/Claim/$submit  
Content-Type: application/fhir+json  
Authorization: Bearer <your-token>  
  
{  
  "resourceType" : "Bundle",  
  "id" : "MedicalServicesAuthorizationBundleExample",  
  "meta" : {  
    "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-pas-request-bundle"]  
  },  
  "identifier" : {  
    "system" : "http://example.org/SUBMITTER_TRANSACTION_IDENTIFIER",  
    "value" : "5269367"  
  },  
  "type" : "collection",  
  "timestamp" : "2005-05-02T11:01:00+05:00",  
  "entry" : [{  
    "fullUrl" : "http://example.org/fhir/Claim/MedicalServicesAuthorizationExample",  
    "resource" : {  
      "resourceType" : "Claim",  
      "id" : "MedicalServicesAuthorizationExample",  
      "meta" : {  
        "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim"]  
      },  
      "identifier" : [{  
        "system" : "http://example.org/PATIENT_EVENT_TRACE_NUMBER",  
        "value" : "111099"   
      }],  
      "status" : "active",  
      "type" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/claim-type",  
          "code" : "professional"  
        }]  
      },  
      "use" : "preauthorization",  
      "patient" : {  
        "reference" : "Patient/SubscriberExample"  
      },  
      "created" : "2005-05-02T11:01:00+05:00",  
      "insurer" : {  
        "reference" : "Organization/InsurerExample"  
      },  
      "provider" : {  
        "reference" : "Organization/UMOExample"  
      },  
      "priority" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/processpriority",  
          "code" : "normal"  
        }]  
      },  
      "insurance" : [{  
        "sequence" : 1,  
        "focal" : true,  
        "coverage" : {  
          "reference" : "Coverage/InsuranceExample"  
        }  
      }],  
      "item" : [{  
        "extension" : [{  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-serviceItemRequestType",  
          "valueCodeableConcept" : {  
            "coding" : [{  
              "system" : "https://codesystem.x12.org/005010/1525",  
              "code" : "IN",  
              "display" : "Initial Medical Services Reservation"  
            }]  
          }  
        },  
        {  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-certificationType",  
          "valueCodeableConcept" : {  
            "coding" : [{  
              "system" : "https://codesystem.x12.org/005010/1322",  
              "code" : "I",  
              "display" : "Initial"  
            }]  
          }  
        },  
        {  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-authorizationNumber",  
          "valueString" : "1122344"  
        },  
        {  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-administrationReferenceNumber",  
          "valueString" : "33441122"  
        }],  
        "sequence" : 1,  
        "category" : {  
          "coding" : [{  
            "system" : "https://codesystem.x12.org/005010/1365",  
            "code" : "1",  
            "display" : "Medical Care"  
          }]  
        },  
        "productOrService" : {  
          "coding" : [{  
            "system" : "http://www.cms.gov/Medicare/Coding/HCPCS​ReleaseCodeSets",  
            "code" : "99212",  
            "display" : "Established Office Visit"  
          }]  
        },  
        "servicedDate" : "2005-05-10",  
        "locationCodeableConcept" : {  
          "coding" : [{  
            "system" : "https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set",  
            "code" : "11"  
          }]  
        }  
      }]  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Organization/UMOExample",  
    "resource" : {  
      "resourceType" : "Organization",  
      "id" : "UMOExample",  
      "meta" : {  
        "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-requestor"]  
      },  
      "identifier" : [{  
        "system" : "http://hl7.org/fhir/sid/us-npi",  
        "value" : "8189991234"  
      }],  
      "active" : true,  
      "type" : [{  
        "coding" : [{  
          "system" : "https://codesystem.x12.org/005010/98",  
          "code" : "X3"  
        }]  
      }],  
      "name" : "DR. JOE SMITH CORPORATION",  
      "address" : [{  
        "line" : ["111 1ST STREET"],  
        "city" : "SAN DIEGO",  
        "state" : "CA",  
        "postalCode" : "92101",  
        "country" : "US"  
      }]  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Organization/InsurerExample",  
    "resource" : {  
      "resourceType" : "Organization",  
      "id" : "InsurerExample",  
      "meta" : {  
        "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-insurer"]  
      },  
      "identifier" : [{  
        "system" : "http://hl7.org/fhir/sid/us-npi",  
        "value" : "1234567893"  
      }],  
      "active" : true,  
      "type" : [{  
        "coding" : [{  
          "system" : "https://codesystem.x12.org/005010/98",  
          "code" : "PR"  
        }]  
      }],  
      "name" : "MARYLAND CAPITAL INSURANCE COMPANY"  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Coverage/InsuranceExample",  
    "resource" : {  
      "resourceType" : "Coverage",  
      "id" : "InsuranceExample",  
      "meta" : {  
        "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-coverage"]  
      },  
      "status" : "active",  
      "subscriberId" : "1122334455",  
      "beneficiary" : {  
        "reference" : "Patient/SubscriberExample"  
      },  
      "relationship" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/subscriber-relationship",  
          "code" : "self"  
        },  
        {  
          "system" : "https://codesystem.x12.org/005010/1069",  
          "code" : "18"  
        }]  
      },  
      "payor" : [{  
        "reference" : "Organization/InsurerExample"  
      }]  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Patient/SubscriberExample",  
    "resource" : {  
      "resourceType" : "Patient",  
      "id" : "SubscriberExample",  
      "meta" : {  
        "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-subscriber"]  
      },  
      "extension" : [{  
        "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-militaryStatus",  
        "valueCodeableConcept" : {  
          "coding" : [{  
            "system" : "https://codesystem.x12.org/005010/584",  
            "code" : "RU"  
          }]  
        }  
      }],  
      "identifier" : [{  
        "type" : {  
          "coding" : [{  
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",  
            "code" : "MB"  
          }]  
        },  
        "system" : "http://example.org/MIN",  
        "value" : "12345678901"  
      }],  
      "name" : [{  
        "family" : "SMITH",  
        "given" : ["JOE"]  
      }],  
      "gender" : "male"  
    }  
  }]  
}
```

## Response format
<a name="submit-response-format"></a>

### Success response (200 OK)
<a name="submit-success-response"></a>

You'll receive a PAS Response Bundle containing:
+ **ClaimResponse** with `outcome: "queued"` and `status: "active"`
+ All original resources from your request
+ Timestamp confirming receipt

```
{  
  "resourceType" : "Bundle",  
  "identifier": {  
        "system": "http://example.org/SUBMITTER_TRANSACTION_IDENTIFIER",  
        "value": "5269367"  
  },  
  "type" : "collection",  
  "timestamp" : "2005-05-02T11:02:00+05:00",  
  "entry" : [{  
    "fullUrl" : "http://example.org/fhir/ClaimResponse/PractitionerRequestorPendingResponseExample",  
    "resource" : {  
      "resourceType" : "ClaimResponse",  
      "id" : "PractitionerRequestorPendingResponseExample",  
      "meta" : {  
        "profile" : ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claimresponse"]  
      },  
      "identifier" : [{  
        "system" : "http://example.org/PATIENT_EVENT_TRACE_NUMBER",  
        "value" : "111099"  
      }],  
      "status" : "active",  
      "type" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/claim-type",  
          "code" : "professional"  
        }]  
      },  
      "use" : "preauthorization",  
      "patient" : {  
        "reference" : "Patient/SubscriberExample"  
      },  
      "created" : "2005-05-02T11:02:00+05:00",  
      "insurer" : {  
        "reference" : "Organization/InsurerExample"  
      },  
      "requestor" : {  
        "reference" : "PractitionerRole/ReferralPractitionerRoleExample"  
      },  
      "request" : {  
        "reference" : "Claim/MedicalServicesAuthorizationExample"  
      },  
      "outcome" : "queued"  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Claim/MedicalServicesAuthorizationExample",  
    "resource" : {  
      "resourceType" : "Claim",  
      "id" : "MedicalServicesAuthorizationExample",  
      "meta" : {  
        "profile": [  
            "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim",  
            "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim|2.1.0"  
        ]  
      },  
      "identifier" : [{  
        "system" : "http://example.org/PATIENT_EVENT_TRACE_NUMBER",  
        "value" : "111099"  
        }  
      }],  
      "status" : "active",  
      "type" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/claim-type",  
          "code" : "professional"  
        }]  
      },  
      "use" : "preauthorization",  
      "patient" : {  
        "reference" : "Patient/SubscriberExample"  
      },  
      "created" : "2005-05-02T11:01:00+05:00",  
      "insurer" : {  
        "reference" : "Organization/InsurerExample"  
      },  
      "provider" : {  
        "reference" : "Organization/UMOExample"  
      },  
      "priority" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/processpriority",  
          "code" : "normal"  
        }]  
      },  
      "insurance" : [{  
        "sequence" : 1,  
        "focal" : true,  
        "coverage" : {  
          "reference" : "Coverage/InsuranceExample"  
        }  
      }],  
      "item" : [{  
        "extension" : [{  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-serviceItemRequestType",  
          "valueCodeableConcept" : {  
            "coding" : [{  
              "system" : "https://codesystem.x12.org/005010/1525",  
              "code" : "IN",  
              "display" : "Initial Medical Services Reservation"  
            }]  
          }  
        },  
        {  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-certificationType",  
          "valueCodeableConcept" : {  
            "coding" : [{  
              "system" : "https://codesystem.x12.org/005010/1322",  
              "code" : "I",  
              "display" : "Initial"  
            }]  
          }  
        },  
        {  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-authorizationNumber",  
          "valueString" : "1122344"  
        },  
        {  
          "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-administrationReferenceNumber",  
          "valueString" : "33441122"  
        }],  
        "sequence" : 1,  
        "category" : {  
          "coding" : [{  
            "system" : "https://codesystem.x12.org/005010/1365",  
            "code" : "1",  
            "display" : "Medical Care"  
          }]  
        },  
        "productOrService" : {  
          "coding" : [{  
            "system" : "http://www.cms.gov/Medicare/Coding/HCPCS​ReleaseCodeSets",  
            "code" : "99212",  
            "display" : "Established Office Visit"  
          }]  
        },  
        "servicedDate" : "2005-05-10",  
        "locationCodeableConcept" : {  
          "coding" : [{  
            "system" : "https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set",  
            "code" : "11"  
          }]  
        }  
      }]  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Organization/UMOExample",  
    "resource" : {  
      "resourceType" : "Organization",  
      "id" : "UMOExample",  
      "meta" : {  
        "profile": [  
            "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-requestor",  
            "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-requestor|2.1.0"  
        ]  
      },  
      "identifier" : [{  
        "system" : "http://hl7.org/fhir/sid/us-npi",  
        "value" : "8189991234"  
      }],  
      "active" : true,  
      "type" : [{  
        "coding" : [{  
          "system" : "https://codesystem.x12.org/005010/98",  
          "code" : "X3"  
        }]  
      }],  
      "name" : "DR. JOE SMITH CORPORATION",  
      "address" : [{  
        "line" : ["111 1ST STREET"],  
        "city" : "SAN DIEGO",  
        "state" : "CA",  
        "postalCode" : "92101",  
        "country" : "US"  
      }]  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Organization/InsurerExample",  
    "resource" : {  
      "resourceType" : "Organization",  
      "id" : "InsurerExample",  
      "meta" : {  
           "profile": [  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-insurer",  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-insurer|2.1.0"  
            ]  
      },  
      "identifier" : [{  
        "system" : "http://hl7.org/fhir/sid/us-npi",  
        "value" : "1234567893"  
      }],  
      "active" : true,  
      "type" : [{  
        "coding" : [{  
          "system" : "https://codesystem.x12.org/005010/98",  
          "code" : "PR"  
        }]  
      }],  
      "name" : "MARYLAND CAPITAL INSURANCE COMPANY"  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Coverage/InsuranceExample",  
    "resource" : {  
      "resourceType" : "Coverage",  
      "id" : "InsuranceExample",  
      "meta": {  
            "profile": [  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-coverage",  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-coverage|2.1.0"  
            ]  
        },  
      "status" : "active",  
      "subscriberId" : "1122334455",  
      "beneficiary" : {  
        "reference" : "Patient/SubscriberExample"  
      },  
      "relationship" : {  
        "coding" : [{  
          "system" : "http://terminology.hl7.org/CodeSystem/subscriber-relationship",  
          "code" : "self"  
        },  
        {  
          "system" : "https://codesystem.x12.org/005010/1069",  
          "code" : "18"  
        }]  
      },  
      "payor" : [{  
        "reference" : "Organization/InsurerExample"  
      }]  
    }  
  },  
  {  
    "fullUrl" : "http://example.org/fhir/Patient/SubscriberExample",  
    "resource" : {  
      "resourceType" : "Patient",  
      "id" : "SubscriberExample",  
      "meta": {  
            "profile": [  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-subscriber",  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-beneficiary",  
                "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-beneficiary|2.1.0"  
            ]  
        },  
      "extension" : [{  
        "url" : "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-militaryStatus",  
        "valueCodeableConcept" : {  
          "coding" : [{  
            "system" : "https://codesystem.x12.org/005010/584",  
            "code" : "RU"  
          }]  
        }  
      }],  
      "identifier" : [{  
        "type" : {  
          "coding" : [{  
            "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",  
            "code" : "MB"  
          }]  
        },  
        "system" : "http://example.org/MIN",  
        "value" : "12345678901"  
      }],  
      "name" : [{  
        "family" : "SMITH",  
        "given" : ["JOE"]  
      }],  
      "gender" : "male"  
    }  
  }]  
}
```

## Error responses
<a name="submit-error-responses"></a>

### 400 Bad Request
<a name="submit-400-error"></a>

Returned when the request format is invalid or malformed.

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "error",  
    "code": "invalid",  
    "diagnostics": "The provided payload was invalid and could not be parsed correctly."  
  }]  
}
```

### 412 Precondition Failed
<a name="submit-412-error"></a>

Returned when the same prior authorization request has already been submitted (duplicate submission detected).

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "error",  
    "code": "processing",  
    "diagnostics": "PreAuth Claim already exists"  
  }]  
}
```

**Idempotency**  
The `$submit` operation is idempotent. Submitting the same request multiple times will not create duplicate prior authorization requests. Instead, you'll receive a 412 error directing you to use `$inquire` to check the status of your original submission.

### 422 Unprocessable Entity
<a name="submit-422-error"></a>

Returned when FHIR validation fails.

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "error",  
    "code": "required",  
    "diagnostics": "Bundle contains more than one preauthorization claim"  
  }]  
}
```

## Validation rules
<a name="submit-validation-rules"></a>

HealthLake performs comprehensive validation on your submission:

### Bundle validation
<a name="submit-bundle-validation"></a>
+ Must conform to PAS Request Bundle profile
+ `Bundle.type` must be `"collection"`
+ Can contain multiple Claim resources
+ However, must contain exactly one Claim resource with preauthorization use
  + And this Claim resource must be the first entry in the bundle
+ All referenced resources must be included in the Bundle

### Claim validation
<a name="submit-claim-validation"></a>
+ Must conform to PAS Claim profile
+ `Claim.use` must be `"preauthorization"`
+ Required fields: `patient`, `insurer`, `provider`, `created`, `priority`
+ Business identifiers must be present and valid

### Resource validation
<a name="submit-resource-validation"></a>
+ All resources must conform to their respective PAS profiles
+ Required supporting resources must be present (Patient, Coverage, Organization)
+ Cross-references must be valid and resolvable within the Bundle

## Performance specifications
<a name="submit-performance-specs"></a>


| Metric | Specification | 
| --- | --- | 
| Bundle Size Limit | 5 MB maximum | 
| Resource Count Limit | 500 resources per Bundle | 

## Required permissions
<a name="submit-required-permissions"></a>

To use the `$submit` operation, one can use either AWS Sigv4 or SMART on FHIR:
+ Ensure your IAM role has: `healthlake:SubmitPreAuthClaim` - To call the operation

**SMART on FHIR Scopes**  
**Minimum required scopes:**
+ **SMART v1**: `user/Claim.write & <all_resourceTypes_in_Bundle>.write`
+ **SMART v2**: `user/Claim.c & <all_resourceTypes_in_Bundle>.c or system/*.*`

## Important implementation notes
<a name="submit-implementation-notes"></a>

### Resource persistence
<a name="submit-resource-persistence"></a>
+ All Bundle entries are persisted as individual FHIR resources in your data store
+ Customer-supplied IDs are preserved when provided
+ Version history is maintained for audit purposes
+ Duplicate detection prevents resource conflicts

### Processing behavior
<a name="submit-processing-behavior"></a>
+ Each valid submission results in exactly one ClaimResponse with `"queued"` outcome
+ Invalid submissions return 400 or 422 status codes with detailed error information
+ System errors return appropriate 5xx status codes
+ All successful submissions return 200 status with a pended ClaimResponse

### Bundle requirements
<a name="submit-bundle-requirements-impl"></a>
+ `Bundle.entry.fullUrl` values must be either REST URLs or `"urn:uuid:[guid]"` format
+ All GUIDs must be unique across submissions (except for the same resource instances)
+ Referenced resources must exist within the Bundle or be resolvable

## Related operations
<a name="submit-related-operations"></a>
+ `Claim/$inquire` - Query the status of a submitted prior authorization request
+ `Patient/$everything` - Retrieve comprehensive patient data for prior authorization context
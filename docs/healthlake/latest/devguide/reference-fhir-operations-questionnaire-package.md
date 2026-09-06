

# FHIR `$questionnaire-package` operation for HealthLake
<a name="reference-fhir-operations-questionnaire-package"></a>

The `$questionnaire-package` operation retrieves a comprehensive bundle containing a FHIR Questionnaire and all its dependencies needed to render and process the questionnaire. This operation implements the [Da Vinci Documentation Templates and Rules (DTR) Implementation Guide](https://hl7.org/fhir/us/davinci-dtr/OperationDefinition-questionnaire-package.html), enabling dynamic form rendering for documentation requirements in healthcare workflows.

## How it works
<a name="questionnaire-package-how-it-works"></a>
+ **Request**: You send parameters identifying the questionnaire(s) needed, along with coverage and order context
+ **Retrieve**: HealthLake gathers the Questionnaire and all dependencies (ValueSets, CQL Libraries, etc.)
+ **Package**: All resources are bundled together in a standardized format
+ **Respond**: You receive a complete package ready for rendering and data collection

**Use Cases**  

+ **Prior Authorization Documentation**: Collect required clinical information for prior authorization requests
+ **Coverage Requirements**: Gather documentation needed to satisfy payer coverage requirements
+ **Clinical Data Exchange**: Structure clinical data for submission to payers
+ **Dynamic Forms**: Render questionnaires with pre-populated patient data and conditional logic

## API endpoint
<a name="questionnaire-package-api-endpoint"></a>

```
POST /datastore/{datastoreId}/r4/Questionnaire/$questionnaire-package  
Content-Type: application/fhir+json
```

## Request parameters
<a name="questionnaire-package-request-parameters"></a>

### Input parameters
<a name="questionnaire-package-input-parameters"></a>

The request body must contain a FHIR Parameters resource with the following parameters:


| Parameter | Type | Cardinality | Description | 
| --- | --- | --- | --- | 
| coverage | Coverage | 1..\* (Required) | Coverage resource(s) to establish the member and coverage for documentation | 
| questionnaire | canonical | 0..\* | Canonical URL(s) for specific Questionnaire(s) to return (may include version) | 
| order | Resource | 0..\* | Order resources (DeviceRequest, ServiceRequest, MedicationRequest, Encounter, Appointment) to establish context | 
| changedSince | dateTime | 0..1 | If present, only return resources changed after this timestamp | 

### Parameter validation rules
<a name="questionnaire-package-parameter-validation"></a>

**At least ONE of the following must be provided** (in addition to required `coverage`):
+ One or more `questionnaire` canonical URLs
+ One or more `order` resources

**Valid Request Combinations:**  

+ `coverage` \+ `questionnaire`
+ `coverage` \+ `order`
+ `coverage` \+ `questionnaire` \+ `order`

## Example request
<a name="questionnaire-package-example-request"></a>

```
POST /datastore/example-datastore/r4/Questionnaire/$questionnaire-package  
Content-Type: application/fhir+json  
Authorization: Bearer <your-token>  
  
{  
  "resourceType": "Parameters",  
  "parameter": [  
    {  
      "name": "coverage",  
      "resource": {  
        "resourceType": "Coverage",  
        "id": "example-coverage",  
        "status": "active",  
        "beneficiary": {  
          "reference": "Patient/example-patient"  
        },  
        "payor": [{  
          "reference": "Organization/example-payer"  
        }],  
        "class": [{  
          "type": {  
            "coding": [{  
              "system": "http://terminology.hl7.org/CodeSystem/coverage-class",  
              "code": "group"  
            }]  
          },  
          "value": "12345"  
        }]  
      }  
    },  
    {  
      "name": "questionnaire",  
      "valueCanonical": "http://example.org/fhir/Questionnaire/home-oxygen-therapy|2.0"  
    },  
    {  
      "name": "order",  
      "resource": {  
        "resourceType": "ServiceRequest",  
        "id": "example-service-request",  
        "status": "active",  
        "intent": "order",  
        "code": {  
          "coding": [{  
            "system": "http://www.ama-assn.org/go/cpt",  
            "code": "94660",  
            "display": "Continuous positive airway pressure ventilation (CPAP)"  
          }]  
        },  
        "subject": {  
          "reference": "Patient/example-patient"  
        }  
      }  
    },  
    {  
      "name": "changedSince",  
      "valueDateTime": "2024-01-01T00:00:00Z"  
    }  
  ]  
}
```

## Response format
<a name="questionnaire-package-response-format"></a>

### Success response (200 OK)
<a name="questionnaire-package-success-response"></a>

The operation returns a FHIR Parameters resource containing one or more **Package Bundles**. Each Package Bundle includes:


| Entry Type | Cardinality | Description | 
| --- | --- | --- | 
| Questionnaire | 1 | The questionnaire to be rendered | 
| QuestionnaireResponse | 0..1 | Pre-populated or partially completed response (if applicable) | 
| Library | 0..\* | CQL Libraries containing pre-population and conditional logic | 
| ValueSet | 0..\* | Expanded ValueSets (for answer choices with <40 expansions) | 

**Example response**  

```
{  
  "resourceType": "Parameters",  
  "parameter": [  
    {  
      "name": "PackageBundle",  
      "resource": {  
        "resourceType": "Bundle",  
        "id": "questionnaire-package-example",  
        "meta": {  
          "profile": ["http://hl7.org/fhir/us/davinci-dtr/StructureDefinition/DTR-QPackageBundle"]  
        },  
        "type": "collection",  
        "timestamp": "2024-03-15T10:30:00Z",  
        "entry": [  
          {  
            "fullUrl": "http://example.org/fhir/Questionnaire/home-oxygen-therapy",  
            "resource": {  
              "resourceType": "Questionnaire",  
              "id": "home-oxygen-therapy",  
              "url": "http://example.org/fhir/Questionnaire/home-oxygen-therapy",  
              "version": "2.0",  
              "status": "active",  
              "title": "Home Oxygen Therapy Documentation",  
              "item": [  
                {  
                  "linkId": "1",  
                  "text": "Patient diagnosis",  
                  "type": "choice",  
                  "answerValueSet": "http://example.org/fhir/ValueSet/oxygen-diagnoses"  
                }  
              ]  
            }  
          },  
          {  
            "fullUrl": "http://example.org/fhir/Library/oxygen-prepopulation",  
            "resource": {  
              "resourceType": "Library",  
              "id": "oxygen-prepopulation",  
              "url": "http://example.org/fhir/Library/oxygen-prepopulation",  
              "version": "1.0",  
              "type": {  
                "coding": [{  
                  "system": "http://terminology.hl7.org/CodeSystem/library-type",  
                  "code": "logic-library"  
                }]  
              },  
              "content": [{  
                "contentType": "text/cql",  
                "data": "bGlicmFyeSBPeHlnZW5QcmVwb3B1bGF0aW9u..."  
              }]  
            }  
          },  
          {  
            "fullUrl": "http://example.org/fhir/ValueSet/oxygen-diagnoses",  
            "resource": {  
              "resourceType": "ValueSet",  
              "id": "oxygen-diagnoses",  
              "url": "http://example.org/fhir/ValueSet/oxygen-diagnoses",  
              "status": "active",  
              "expansion": {  
                "timestamp": "2024-03-15T10:30:00Z",  
                "contains": [  
                  {  
                    "system": "http://hl7.org/fhir/sid/icd-10",  
                    "code": "J44.0",  
                    "display": "COPD with acute lower respiratory infection"  
                  },  
                  {  
                    "system": "http://hl7.org/fhir/sid/icd-10",  
                    "code": "J96.01",  
                    "display": "Acute respiratory failure with hypoxia"  
                  }  
                ]  
              }  
            }  
          },  
          {  
            "fullUrl": "http://example.org/fhir/QuestionnaireResponse/example-prepopulated",  
            "resource": {  
              "resourceType": "QuestionnaireResponse",  
              "id": "example-prepopulated",  
              "questionnaire": "http://example.org/fhir/Questionnaire/home-oxygen-therapy|2.0",  
              "status": "in-progress",  
              "subject": {  
                "reference": "Patient/example-patient"  
              },  
              "basedOn": [{  
                "reference": "ServiceRequest/example-service-request"  
              }],  
              "item": [  
                {  
                  "linkId": "1",  
                  "text": "Patient diagnosis",  
                  "answer": [{  
                    "valueCoding": {  
                      "system": "http://hl7.org/fhir/sid/icd-10",  
                      "code": "J44.0",  
                      "display": "COPD with acute lower respiratory infection"  
                    }  
                  }]  
                }  
              ]  
            }  
          }  
        ]  
      }  
    },  
    {  
      "name": "Outcome",  
      "resource": {  
        "resourceType": "OperationOutcome",  
        "issue": [{  
          "severity": "information",  
          "code": "informational",  
          "details": {  
            "text": "Successfully retrieved questionnaire package"  
          }  
        }]  
      }  
    }  
  ]  
}
```

## Operation workflow
<a name="questionnaire-package-operation-workflow"></a>

**How HealthLake Processes Your Request**  
When you call `$questionnaire-package`, HealthLake performs the following steps:

1. **Identify Patient & Payer**: Extracts the patient and insurance organization from your `coverage` parameter.

1. **Find the Right Questionnaire**:
   + **With **`questionnaire`** parameter**: Uses the canonical URL you provided
   + **With **`order`** parameter**: Matches the order code (CPT/HCPCS/LOINC) and payer to find the appropriate questionnaire

1. **Gather Dependencies**: Automatically retrieves everything needed to render the questionnaire:
   + **CQL Libraries** - Logic for pre-population and conditional questions
   + **ValueSets** - Answer choices (automatically expanded if <40 options)
   + **QuestionnaireResponse** - Any existing in-progress or completed responses

1. **Package Everything Together**:
   + Bundles all resources (each resource included only once)
   + Filters by `changedSince` timestamp if provided
   + Adds warnings to `Outcome` if any resources are missing

**Result**: A complete, self-contained package ready for rendering.

## Error responses
<a name="questionnaire-package-error-responses"></a>

### 400 Bad Request
<a name="questionnaire-package-400-error"></a>

Returned when request validation fails.

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "error",  
    "code": "required",  
    "details": {  
      "text": "At least one of 'questionnaire' or 'order' must be provided along with 'coverage'"  
    }  
  }]  
}
```

### 424 Failed Dependency
<a name="questionnaire-package-424-error"></a>

Returned when a dependent resource cannot be retrieved.

```
{  
  "resourceType": "OperationOutcome",  
  "issue": [{  
    "severity": "warning",  
    "code": "not-found",  
    "details": {  
      "text": "Referenced Library 'http://example.org/fhir/Library/missing-library' could not be retrieved"  
    }  
  }]  
}
```

### 401 Unauthorized
<a name="questionnaire-package-401-error"></a>

Returned when authentication credentials are missing or invalid.

### 403 Forbidden
<a name="questionnaire-package-403-error"></a>

Returned when the authenticated user lacks permission to access the requested resources.

### 406 Not Acceptable
<a name="questionnaire-package-406-error"></a>

Returned when the requested content type cannot be provided.

### 409 Conflict
<a name="questionnaire-package-409-error"></a>

Returned when there's a version or concurrency conflict.

### 410 Gone
<a name="questionnaire-package-410-error"></a>

Returned when the requested resource has been permanently deleted.

### 429 Too Many Requests
<a name="questionnaire-package-429-error"></a>

Returned when rate limits are exceeded.

### 500 Internal Server Error
<a name="questionnaire-package-500-error"></a>

Returned when an unexpected server error occurs.

### 501 Not Implemented
<a name="questionnaire-package-501-error"></a>

Returned when the requested operation is not yet implemented.

## Validation rules
<a name="questionnaire-package-validation-rules"></a>

### Input validation
<a name="questionnaire-package-input-validation"></a>
+ `coverage` parameter is **required** (1..\* cardinality)
+ At least one of `questionnaire` or `order` must be provided
+ All Coverage resources must be valid FHIR resources
+ All Order resources must be valid FHIR resources
+ Canonical URLs must be properly formatted
+ `changedSince` must be a valid ISO 8601 dateTime

### QuestionnaireResponse validation
<a name="questionnaire-package-response-validation"></a>
+ `status` must be appropriate (`in-progress`, `completed`, `amended`)
+ Structure must match the referenced Questionnaire
+ `basedOn` must reference valid Order resources
+ `subject` must reference valid Patient resources

### Resource deduplication
<a name="questionnaire-package-resource-dedup"></a>
+ Each resource appears only once in the bundle
+ Exception: Different versions of the same resource may both be included
+ Resources are identified by their canonical URL and version

## Performance specifications
<a name="questionnaire-package-performance-specs"></a>


| Metric | Specification | 
| --- | --- | 
| Resource Count Limit | 500 resources per Bundle | 
| Bundle Size Limit | 5 MB maximum | 

## Required permissions
<a name="questionnaire-package-required-permissions"></a>

To use the `$questionnaire-package` operation, ensure your IAM role has:
+ `healthlake:QuestionnairePackage` - To call the operation
+ `healthlake:ReadResource` - To retrieve Questionnaire and dependent resources
+ `healthlake:SearchWithPost` - To search for QuestionnaireResponse and related resources

**SMART on FHIR Scopes**  
**Minimum required scopes:**
+ **SMART v1**: `user/Questionnaire.read user/Library.read user/ValueSet.read user/QuestionnaireResponse.read`
+ **SMART v2**: `user/Questionnaire.rs user/Library.rs user/ValueSet.rs user/QuestionnaireResponse.rs`

## Important implementation notes
<a name="questionnaire-package-implementation-notes"></a>

### Resource retrieval strategy
<a name="questionnaire-package-retrieval-strategy"></a>

**Questionnaire Identification Priority:**  

+ **Canonical URL** (if `questionnaire` parameter provided) - Highest priority
+ **Order Analysis** (if `order` parameter provided):
  + Match order codes (CPT, HCPCS, LOINC) to payer medical policies
  + Use coverage payor to filter payer-specific questionnaires
  + Consider reason codes for additional context

### Dependency resolution
<a name="questionnaire-package-dependency-resolution"></a>

**CQL Libraries:**  

+ Retrieved via the `cqf-library` extension on Questionnaire resources
+ Recursively fetches dependent libraries through `Library.relatedArtifact` with type `depends-on`
+ All library dependencies are included in the package

**ValueSets:**  

+ Automatically expanded if they contain fewer than 40 concepts
+ Larger ValueSets are included without expansion
+ ValueSets referenced in both Questionnaire and Library resources are included

### QuestionnaireResponse pre-population
<a name="questionnaire-package-prepopulation"></a>

The operation may return a QuestionnaireResponse with pre-populated data when:
+ An existing in-progress or completed response is found
+ CQL logic in associated Libraries can extract data from patient records
+ The response is linked to the relevant order and coverage

**Search Criteria for QuestionnaireResponse:**  



| Search Parameter | FHIR Path | Description | 
| --- | --- | --- | 
| based-on | QuestionnaireResponse.basedOn | Links to ServiceRequest or CarePlan | 
| patient | QuestionnaireResponse.subject | The patient who is the subject | 
| questionnaire | QuestionnaireResponse.questionnaire | The questionnaire being answered | 

### Changed resources filtering
<a name="questionnaire-package-changed-filtering"></a>

When the `changedSince` parameter is provided:
+ Only resources modified **after** the specified timestamp are included
+ If no resources have changed, returns `200 OK` with an empty package
+ Useful for incremental updates and caching strategies
+ Timestamp comparison uses resource `meta.lastUpdated` field

### Multiple package bundles
<a name="questionnaire-package-multiple-bundles"></a>

The operation may return **multiple Package Bundles** when:
+ Multiple questionnaires are requested via canonical URLs
+ Multiple orders require different questionnaires
+ Different versions of the same questionnaire are applicable

Each Package Bundle is self-contained with all necessary dependencies.

## Common use cases
<a name="questionnaire-package-common-use-cases"></a>

### Use Case 1: Prior Authorization Documentation
<a name="questionnaire-package-use-case-1"></a>

**Scenario**: A provider needs to collect documentation for a home oxygen therapy prior authorization.

```
{  
  "resourceType": "Parameters",  
  "parameter": [  
    {  
      "name": "coverage",  
      "resource": { /* Patient's insurance coverage */ }  
    },  
    {  
      "name": "order",  
      "resource": {  
        "resourceType": "ServiceRequest",  
        "code": {  
          "coding": [{  
            "system": "http://www.ama-assn.org/go/cpt",  
            "code": "94660"  
          }]  
        }  
      }  
    }  
  ]  
}
```

**Result**: Returns a package with the oxygen therapy questionnaire, pre-populated with patient vitals and diagnosis codes from the EHR.

### Use Case 2: Retrieve Specific Questionnaire Version
<a name="questionnaire-package-use-case-2"></a>

**Scenario**: A provider needs a specific version of a questionnaire for compliance.

```
{  
  "resourceType": "Parameters",  
  "parameter": [  
    {  
      "name": "coverage",  
      "resource": { /* Coverage resource */ }  
    },  
    {  
      "name": "questionnaire",  
      "valueCanonical": "http://example.org/fhir/Questionnaire/dme-request|3.1.0"  
    }  
  ]  
}
```

**Result**: Returns exactly version 3.1.0 of the DME request questionnaire with all dependencies.

### Use Case 3: Check for Updates
<a name="questionnaire-package-use-case-3"></a>

**Scenario**: A provider wants to check if any questionnaire resources have been updated since last retrieval.

```
{  
  "resourceType": "Parameters",  
  "parameter": [  
    {  
      "name": "coverage",  
      "resource": { /* Coverage resource */ }  
    },  
    {  
      "name": "questionnaire",  
      "valueCanonical": "http://example.org/fhir/Questionnaire/medication-request"  
    },  
    {  
      "name": "changedSince",  
      "valueDateTime": "2024-03-01T00:00:00Z"  
    }  
  ]  
}
```

**Result**: Returns only resources that have been modified after March 1, 2024, or an empty package if nothing changed.

### Use Case 4: Multiple Orders
<a name="questionnaire-package-use-case-4"></a>

**Scenario**: A provider submits multiple service requests that may require different questionnaires.

```
{  
  "resourceType": "Parameters",  
  "parameter": [  
    {  
      "name": "coverage",  
      "resource": { /* Coverage resource */ }  
    },  
    {  
      "name": "order",  
      "resource": { /* ServiceRequest for imaging */ }  
    },  
    {  
      "name": "order",  
      "resource": { /* ServiceRequest for DME */ }  
    }  
  ]  
}
```

**Result**: Returns multiple Package Bundles, one for each applicable questionnaire.

## Integration with Other Da Vinci IGs
<a name="questionnaire-package-integration"></a>

### Coverage Requirements Discovery (CRD)
<a name="questionnaire-package-crd-integration"></a>

**Workflow Integration:**  

+ Provider orders a service in their EHR
+ CRD hook fires, checking coverage requirements
+ Payer responds indicating documentation is needed
+ Provider calls `$questionnaire-package` to retrieve the documentation form
+ Provider completes the questionnaire
+ Documentation is submitted via PAS or CDex

### Prior Authorization Support (PAS)
<a name="questionnaire-package-pas-integration"></a>

**Workflow Integration:**  

+ Use `$questionnaire-package` to retrieve documentation requirements
+ Complete the QuestionnaireResponse with required clinical data
+ Submit the prior authorization using `Claim/$submit` with the completed QuestionnaireResponse
+ Check status using `Claim/$inquire`

### Clinical Data Exchange (CDex)
<a name="questionnaire-package-cdex-integration"></a>

**Workflow Integration:**  

+ Payer requests additional documentation for a claim
+ Provider uses `$questionnaire-package` to retrieve the structured data collection form
+ Provider completes the QuestionnaireResponse
+ Documentation is submitted to payer via CDex attachment workflow

## Troubleshooting guide
<a name="questionnaire-package-troubleshooting"></a>

### Issue: No Questionnaire Returned
<a name="questionnaire-package-no-questionnaire"></a>

**Possible Causes:**  

+ Canonical URL doesn't match any Questionnaire in the data store
+ Order code doesn't map to any questionnaire in payer's medical policy
+ Coverage payor doesn't have associated questionnaires

**Solutions:**  

+ Verify the canonical URL is correct and the Questionnaire exists
+ Check that order codes (CPT/HCPCS) are correctly specified
+ Confirm the payor organization has questionnaires configured

### Issue: Missing Dependencies in Package
<a name="questionnaire-package-missing-dependencies"></a>

**Possible Causes:**  

+ Referenced Library or ValueSet doesn't exist in the data store
+ Library references are broken or incorrect
+ ValueSet expansion failed

**Solutions:**  

+ Check the `Outcome` parameter for warnings about missing resources
+ Verify all referenced resources exist in your data store
+ Ensure ValueSet URLs are correct and resolvable

### Issue: Empty Package with changedSince
<a name="questionnaire-package-empty-package"></a>

**Possible Causes:**  

+ This is expected behavior - no resources have been modified since the specified timestamp

**Solutions:**  

+ Use the cached version of the package
+ Remove `changedSince` parameter to retrieve the full package

### Issue: QuestionnaireResponse Not Pre-populated
<a name="questionnaire-package-not-prepopulated"></a>

**Possible Causes:**  

+ No existing QuestionnaireResponse found
+ CQL Library logic couldn't extract required data
+ Patient data is missing or incomplete

**Solutions:**  

+ This may be expected - not all questionnaires have pre-population logic
+ Check that patient data exists in the data store
+ Review CQL Library logic for data extraction requirements

## Best practices
<a name="questionnaire-package-best-practices"></a>

### 1. Use Canonical URLs with Versions
<a name="questionnaire-package-bp-versions"></a>

Always specify version numbers when requesting specific questionnaires:

```
{  
  "name": "questionnaire",  
  "valueCanonical": "http://example.org/fhir/Questionnaire/dme|2.1.0"  
}
```

**Why**: Ensures consistency and prevents unexpected changes when questionnaires are updated.

### 2. Leverage changedSince for Performance
<a name="questionnaire-package-bp-changed-since"></a>

For frequently accessed questionnaires, use `changedSince` to minimize data transfer:

```
{  
  "name": "changedSince",  
  "valueDateTime": "2024-03-10T15:30:00Z"  
}
```

**Why**: Reduces latency and bandwidth usage by retrieving only updated resources.

### 3. Include Complete Coverage Information
<a name="questionnaire-package-bp-coverage"></a>

Provide comprehensive coverage details to ensure correct questionnaire selection:

```
{  
  "name": "coverage",  
  "resource": {  
    "resourceType": "Coverage",  
    "beneficiary": { "reference": "Patient/123" },  
    "payor": [{ "reference": "Organization/payer-abc" }],  
    "class": [{ /* Group/plan information */ }]  
  }  
}
```

**Why**: Helps HealthLake identify payer-specific questionnaires and requirements.

## Related operations
<a name="questionnaire-package-related-operations"></a>
+ `Claim/$submit` - Submit prior authorization requests with completed documentation
+ `Claim/$inquire` - Check status of submitted prior authorizations
+ `ValueSet/$expand` - Expand ValueSets for answer choices
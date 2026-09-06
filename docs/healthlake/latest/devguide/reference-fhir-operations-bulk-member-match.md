

# `$bulk-member-match` operation for HealthLake
<a name="reference-fhir-operations-bulk-member-match"></a>

AWS HealthLake supports the `$bulk-member-match` operation for processing multiple member match requests asynchronously. This operation enables healthcare organizations to efficiently match hundreds of members' unique identifiers across different healthcare systems using demographic and coverage information in a single bulk request. This capability is essential for large-scale payer-to-payer data exchange, member transitions, and CMS compliance requirements and follows the FHIR [specification](https://build.fhir.org/ig/HL7/davinci-epdx/OperationDefinition-BulkMemberMatch.html).

**Note**  
The `$bulk-member-match` operation is based on an underlying FHIR specification that is currently experimental and subject to change. As the specification evolves, the behavior and interface of this API will be updated accordingly. Developers are advised to monitor AWS HealthLake release notes and the relevant FHIR specification updates to stay informed of any changes that may impact their integrations.

This operation is particularly useful when you need to:
+ Process member matching at scale during open enrollment periods
+ Facilitate bulk member transitions between payers
+ Support large-scale CMS compliance data exchange requirements
+ Efficiently match member cohorts across healthcare networks
+ Minimize API calls and improve operational efficiency for high-volume matching scenarios

## Usage
<a name="bulk-member-match-usage"></a>

The `$bulk-member-match` operation is an asynchronous operation invoked on Group resources using the POST method:

```
POST [base]/Group/$bulk-member-match
```

After submitting a bulk match request, you can poll the job status using:

```
GET [base]/$bulk-member-match-status/{jobId}
```

Each request supports up to 500 members with a maximum payload of 5 MB.

## Quick start
<a name="bulk-member-match-quick-start"></a>

To get started with bulk member match, follow these steps:

1. Submit a bulk match request with MemberBundles using the `Group/$bulk-member-match` operation. The response includes a job ID.

1. Poll the job status using the `$bulk-member-match-status` operation until the status is COMPLETED.

1. Extract the `MatchedMembers` Group ID from the completed job response.

1. Export clinical data using the `Group/$davinci-data-export` operation on the matched Group.

## Supported parameters
<a name="bulk-member-match-parameters"></a>

HealthLake supports the following FHIR `$bulk-member-match` parameters:


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
| `MemberPatient` | Patient | Yes | Patient resource containing demographic information for the member to be matched. | 
| `CoverageToMatch` | Coverage | Yes | Coverage resource that will be used for matching against existing records. | 
| `CoverageToLink` | Coverage | No | Coverage resource to be linked during the matching process. | 
| `Consent` | Consent | Yes | Consent resource for authorization purposes is also stored. This is different than the individual `$member-match` operation where Consent is *not* required. | 

## POST request to submit bulk member match job
<a name="bulk-member-match-request-example"></a>

The following example shows a POST request to submit a bulk member match job. Each member is wrapped in a `MemberBundle` parameter containing the required `MemberPatient`, `CoverageToMatch`, and `Consent` resources, along with an optional `CoverageToLink`.

```
POST [base]/Group/$bulk-member-match
Content-Type: application/fhir+json
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "MemberBundle",
      "part": [
        {
          "name": "MemberPatient",
          "resource": {
            "resourceType": "Patient",
            "identifier": [
              {
                "system": "http://example.org/patient-id",
                "value": "patient-0"
              }
            ],
            "name": [
              {
                "family": "Smith",
                "given": ["James"]
              }
            ],
            "gender": "male",
            "birthDate": "1950-01-01"
          }
        },
        {
          "name": "CoverageToMatch",
          "resource": {
            "resourceType": "Coverage",
            "status": "active",
            "identifier": [
              {
                "system": "http://example.org/coverage-id",
                "value": "cov-0"
              }
            ],
            "subscriberId": "sub-0",
            "beneficiary": {
              "reference": "Patient/patient123"
            },
            "relationship": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/subscriber-relationship",
                  "code": "self"
                }
              ]
            },
            "payor": [
              {
                "reference": "Organization/org123"
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
              "reference": "Patient/patient123"
            },
            "performer": [
              {
                "reference": "Patient/patient123"
              }
            ],
            "sourceReference": {
              "reference": "http://example.org/DocumentReference/consent-source"
            },
            "policy": [
              {
                "uri": "http://hl7.org/fhir/us/davinci-hrex/StructureDefinition-hrex-consent.html#regular"
              }
            ],
            "provision": {
              "type": "permit",
              "period": {
                "start": "2024-01-01",
                "end": "2025-12-31"
              },
              "actor": [
                {
                  "role": {
                    "coding": [
                      {
                        "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
                        "code": "performer"
                      }
                    ]
                  },
                  "reference": {
                    "identifier": {
                      "system": "http://hl7.org/fhir/sid/us-npi",
                      "value": "9876543210"
                    },
                    "display": "Old Health Plan"
                  }
                },
                {
                  "role": {
                    "coding": [
                      {
                        "system": "http://terminology.hl7.org/CodeSystem/v3-ParticipationType",
                        "code": "IRCP"
                      }
                    ]
                  },
                  "reference": {
                    "identifier": {
                      "system": "http://hl7.org/fhir/sid/us-npi",
                      "value": "0123456789"
                    },
                    "display": "New Health Plan"
                  }
                }
              ],
              "action": [
                {
                  "coding": [
                    {
                      "system": "http://terminology.hl7.org/CodeSystem/consentaction",
                      "code": "disclose"
                    }
                  ]
                }
              ]
            }
          }
        },
        {
          "name": "CoverageToLink",
          "resource": {
            "resourceType": "Coverage",
            "status": "active",
            "identifier": [
              {
                "system": "http://example.org/coverage-link-id",
                "value": "cov-link-0"
              }
            ],
            "subscriberId": "new-sub-0",
            "beneficiary": {
              "reference": "Patient/patient123"
            },
            "relationship": {
              "coding": [
                {
                  "system": "http://terminology.hl7.org/CodeSystem/subscriber-relationship",
                  "code": "self"
                }
              ]
            },
            "payor": [
              {
                "identifier": {
                  "system": "http://hl7.org/fhir/sid/us-npi",
                  "value": "0123456789"
                },
                "display": "New Health Plan"
              }
            ]
          }
        }
      ]
    }
  ]
}
```

## Completed job response with output
<a name="bulk-member-match-response-example"></a>

When the job completes, the response includes job metadata and a FHIR Parameters resource containing three Group resources that categorize the match results.

```
{
  "datastoreId": "datastoreId",
  "jobId": "jobId",
  "status": "COMPLETED",
  "submittedTime": "2026-03-20T18:45:26.321Z",
  "numberOfMembers": 3,
  "numberOfMembersProcessedSuccessfully": 3,
  "numberOfMembersWithCustomerError": 0,
  "numberOfMembersWithServerError": 0,
  "output": {
    "resourceType": "Parameters",
    "meta": {
      "profile": [
        "http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/pdex-parameters-multi-member-match-bundle-out"
      ]
    },
    "parameter": [
      {
        "name": "MatchedMembers",
        "resource": {
          "resourceType": "Group",
          "id": "group1",
          "text": {
            "status": "generated",
            "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Matched members group</div>"
          },
          "contained": [
            {
              "resourceType": "Patient",
              "id": "1",
              "identifier": [
                {
                  "system": "http://example.org/patient-id",
                  "value": "patient-0"
                }
              ],
              "name": [
                {
                  "family": "Smith",
                  "given": ["James"]
                }
              ],
              "gender": "male",
              "birthDate": "1950-01-01"
            }
          ],
          "type": "person",
          "actual": true,
          "code": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/us/davinci-pdex/CodeSystem/PdexMultiMemberMatchResultCS",
                "code": "match",
                "display": "Matched"
              }
            ]
          },
          "quantity": 1,
          "member": [
            {
              "entity": {
                "extension": [
                  {
                    "url": "http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/base-ext-match-parameters",
                    "valueReference": {
                      "reference": "#1"
                    }
                  }
                ],
                "reference": "Patient/patient123"
              }
            }
          ]
        }
      },
      {
        "name": "NonMatchedMembers",
        "resource": {
          "resourceType": "Group",
          "id": "Group2",
          "text": {
            "status": "generated",
            "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Non-matched members group</div>"
          },
          "contained": [
            {
              "resourceType": "Patient",
              "id": "1",
              "identifier": [
                {
                  "system": "http://example.org/patient-id",
                  "value": "patient-501"
                }
              ],
              "name": [
                {
                  "family": "Carter",
                  "given": ["Emily"]
                }
              ],
              "gender": "female",
              "birthDate": "1985-06-15"
            }
          ],
          "type": "person",
          "actual": true,
          "code": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/us/davinci-pdex/CodeSystem/PdexMultiMemberMatchResultCS",
                "code": "nomatch",
                "display": "Not Matched"
              }
            ]
          },
          "quantity": 1,
          "member": [
            {
              "entity": {
                "extension": [
                  {
                    "url": "http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/base-ext-match-parameters",
                    "valueReference": {
                      "reference": "#1"
                    }
                  }
                ],
                "reference": "Patient/patient123"
              }
            }
          ]
        }
      },
      {
        "name": "ConsentConstrainedMembers",
        "resource": {
          "resourceType": "Group",
          "id": "group3",
          "text": {
            "status": "generated",
            "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\">Consent constrained members group</div>"
          },
          "contained": [
            {
              "resourceType": "Patient",
              "id": "1",
              "identifier": [
                {
                  "system": "http://example.org/patient-id",
                  "value": "patient-502"
                }
              ],
              "name": [
                {
                  "family": "Nguyen",
                  "given": ["David"]
                }
              ],
              "gender": "male",
              "birthDate": "1972-11-22"
            }
          ],
          "type": "person",
          "actual": true,
          "code": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/us/davinci-pdex/CodeSystem/PdexMultiMemberMatchResultCS",
                "code": "consentconstraint",
                "display": "Consent Constraint"
              }
            ]
          },
          "quantity": 1,
          "member": [
            {
              "entity": {
                "extension": [
                  {
                    "url": "http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/base-ext-match-parameters",
                    "valueReference": {
                      "reference": "#1"
                    }
                  }
                ],
                "reference": "Patient/123"
              }
            }
          ]
        }
      }
    ]
  }
}
```

## How HealthLake classifies members into output Groups
<a name="bulk-member-match-processing"></a>

Every member submitted in a `$bulk-member-match` request is evaluated through a sequential pipeline. The outcome of each step determines which output Group the member is placed in.

1. **Structural validation** — Does the MemberBundle conform to required profiles? On failure: Error (not in any Group).

1. **Patient matching** — Can HealthLake find patients matching the submitted demographics? On failure: NonMatchedMembers.

1. **Coverage confirmation** — Can HealthLake narrow to exactly one patient with valid CoverageToMatch? On failure: NonMatchedMembers.

1. **Consent evaluation** — Does `provision.period` cover the current date? On failure: ConsentConstrainedMembers.

1. **Success** — All checks pass. Consent stored in datastore. Member placed in MatchedMembers.

**Key principle:** A member can only appear in one destination. The first failing step determines placement. Members who fail Steps 2 or 3 are never placed in ConsentConstrainedMembers — that Group is exclusively for members who matched successfully but whose consent cannot be honored.

**Consent evaluation details (Step 4):**
+ **Provision period:** Does `provision.period` cover the current date? If current date is before `period.start` or after `period.end` → ConsentConstrainedMembers.

All checks must pass for the member to be placed in MatchedMembers and for the Consent to be stored.

**Note**  
The operation does not validate the `performer` reference against the `patient` field. A parent or guardian can consent on behalf of a dependent.

The following table describes how consent classification determines member placement:


| Provision type | Policy URI | Status | Period | Outcome | 
| --- | --- | --- | --- | --- | 
| `permit` | `#regular` | `active` | Covers current date | MatchedMembers (Consent stored) | 
| `permit` | `#sensitive` | `active` | Covers current date | MatchedMembers (Consent stored) | 
| `permit` | `#regular` or `#sensitive` | `active` | Expired or not started | ConsentConstrainedMembers | 
| `deny` | Any | Any | Any | 400 Bad Request (Step 1) | 
| `permit` | Not ending in `#regular` or `#sensitive` | Any | Any | 400 Bad Request (Step 1) | 
| Any | Any | Not `active` | Any | 400 Bad Request (Step 1) | 

## Coverage matching behavior
<a name="bulk-member-match-coverage-behavior"></a>

During member matching, only `CoverageToMatch` is validated against the responding payer's datastore. `CoverageToLink` belongs to the new/requesting payer and is *not* validated against the old payer's datastore. Including `CoverageToLink` in the request will not affect matching results.

Each Patient \+ Coverage combination in the request is processed independently. The same patient can be submitted multiple times with different coverage plans, and each entry receives its own result based on its specific coverage.

## Consent performer reference handling
<a name="bulk-member-match-performer-handling"></a>

The new payer may send a temporary or local patient reference in `Consent.performer` (for example, the same reference used in `Consent.patient`). HealthLake resolves these references automatically:
+ If `Consent.performer` contains the same local reference as `Consent.patient`, HealthLake replaces it with the actual matched patient reference after matching succeeds.
+ HealthLake supports performer references of type Patient, RelatedPerson, Practitioner, PractitionerRole, and Organization (both direct references and logical identifier references).
+ The `performer` reference is not cross-validated against `patient`. A parent/guardian consenting on behalf of a dependent is valid and will not route the member to ConsentConstrainedMembers.

## Output Group resources
<a name="bulk-member-match-output-groups"></a>

The completed job returns a Parameters resource containing three Group resources:

**MatchedMembers Group**  
Contains Patient references for all successfully matched members whose consent is active and valid at the time of the request. The Consent resource is created and stored in the datastore for each matched member. This Group is instantiated in the datastore and can be used directly with `$davinci-data-export`.

**NonMatchedMembers Group**  
Contains references to members where no unique match was found. A member is placed here when no patient in the datastore matches the provided demographics, no valid coverage exists for any matched patient candidate, or multiple patients match demographics and multiple have valid coverage (ambiguous). This Group is **not instantiated** in the datastore. It exists only in the completed job response.

**ConsentConstrainedMembers Group**  
Contains Patient references for members who were successfully matched (demographics and coverage confirmed) but whose consent cannot be honored at the time of the request. The Consent resource is *not* stored for consent-constrained members. The matched member identity (MemberIdentifier and MemberId) is still included so the requesting payer knows who was constrained. This Group is **not instantiated** in the datastore. It exists only in the completed job response.

The `Group.quantity` field contains the total count of members in each of their respective groups.

**Group member references:**
+ `Group.member.entity.reference` — For MatchedMembers and ConsentConstrainedMembers, contains the Patient ID of the matched member in the responding payer's system. For NonMatchedMembers, references the contained input Patient.
+ `Group.member.entity.extension (base-ext-match-parameters)` — Contains the Patient ID from the original input request (the ID submitted by the requesting payer, derived from `Patient.id`, `Coverage.beneficiary.reference`, or `Consent.patient.reference`).

## Consent-Patient linkage
<a name="bulk-member-match-consent-patient-linkage"></a>

**Important**  
The stored Consent resource retains the patient reference exactly as submitted by the requesting payer. HealthLake does not automatically update the Consent's patient field to point to the matched Patient in the receiving datastore.

To link a stored Consent to the matched Patient, use the job output: each member in the MatchedMembers Group has a `member.entity.reference` pointing to the matched Patient and a `member.entity.extension` (`base-ext-match-parameters`) pointing to the contained input Patient. Cross-reference these with the Consent's patient field to build the mapping in your application layer.

## What gets stored vs. what is transient
<a name="bulk-member-match-stored-resources"></a>

The following table documents what HealthLake persists to the datastore during `$bulk-member-match` processing and what exists only in the job response:


| Resource | Stored? | Queryable via REST? | Notes | 
| --- | --- | --- | --- | 
| MemberPatient (input) | No | No | Used only for matching; not persisted | 
| CoverageToMatch (input) | No | No | Used only for coverage confirmation | 
| CoverageToLink (input) | No | No | Not validated against the datastore; belongs to the new payer | 
| **Consent (matched members)** | **Yes** | Yes — GET [base]/Consent/{id} | Stored as-received from requesting payer | 
| Consent (constrained members) | No | No | Not stored. Member identity still included in response. | 
| **MatchedMembers Group (output)** | **Yes** | Yes — GET [base]/Group/{id} | Instantiated; usable with $davinci-data-export | 
| NonMatchedMembers Group | No | No | Job response only | 
| ConsentConstrainedMembers Group | No | No | Job response only | 

## Integration with $davinci-data-export
<a name="bulk-member-match-davinci-integration"></a>

The MatchedMembers Group resource returned by `$bulk-member-match` can be directly used with the `$davinci-data-export` operation to retrieve bulk member data:

```
POST [base]/Group/{matched-group-id}/$davinci-data-export
GET [base]/Group/{matched-group-id}
```

This integration enables efficient workflows where you first identify matched members in bulk, then export their complete health records using the resulting Group resource.

### Using $member-remove before export
<a name="bulk-member-match-member-remove"></a>

If you need to exclude specific members from export after matching (for example, a member revokes consent between matching and export), use `$member-remove` on the MatchedMembers Group.

**Important**  
Removing a member via `$member-remove` marks the member as inactive in the Group, but `$davinci-data-export` only excludes inactive members after the Group is updated to status "final". If you call `$davinci-data-export` on a Group that still has the default status, removed members may still appear in export results.

Workflow:

1. `POST [base]/Group/{id}/$member-remove` — mark members inactive

1. `PUT [base]/Group/{id}` — update Group status to "final"

1. `POST [base]/Group/{id}/$davinci-data-export` — export now excludes removed members

## Performance characteristics
<a name="bulk-member-match-performance"></a>

The `$bulk-member-match` operation is designed for high-volume processing and runs asynchronously:
+ **Concurrency**: Maximum of 5 concurrent operations per data store.
+ **Scalability**: Handles up to 500 members per request (5 MB payload limit).
+ **Parallel operations**: Compatible with concurrent import, export, or bulk-delete operations.

## Authorization
<a name="bulk-member-match-authorization"></a>

The API uses SMART on FHIR authorization protocol with the following required scopes:
+ `system/Patient.read` — Required to search and match patient resources.
+ `system/Coverage.read` — Required to validate coverage information.
+ `system/Group.write` — Required to create result Group resources.
+ `system/Organization.read` — Conditional, required if coverage references organizations.
+ `system/Practitioner.read` — Conditional, required if coverage references practitioners.
+ `system/PractitionerRole.read` — Conditional, required if coverage references practitioner roles.
+ `system/Consent.write` — Conditional, required if consent resources are provided.

The operation also supports AWS IAM Signature Version 4 (SigV4) authorization for programmatic access.

## Validation rules
<a name="bulk-member-match-validation-rules"></a>

The following validation rules are applied to each MemberBundle at Step 1. Members that fail validation are reported as errors and do not appear in any output Group.

### MemberPatient
<a name="bulk-member-match-validation-patient"></a>


| Field | How HealthLake uses it | Validation failure if... | 
| --- | --- | --- | 
| `name.family` | Demographic search | Missing | 
| `name.given` | Demographic search | Missing (at least one required) | 
| `birthDate` | Demographic search | Missing | 
| `gender` | Demographic search; if absent, Birth Sex extension used | Neither gender nor Birth Sex present (hrex-pat-1) | 
| `identifier` | Included in search when present; improves confidence | Never causes failure (optional) | 

### CoverageToMatch / CoverageToLink
<a name="bulk-member-match-validation-coverage"></a>


| Field | How HealthLake uses it | Validation failure if... | 
| --- | --- | --- | 
| `status` | Confirms coverage is actionable | Missing | 
| `beneficiary` | Links coverage to a patient candidate | Missing | 
| `relationship` | Confirms subscriber-beneficiary relationship | Missing | 
| `identifier (MB) or subscriberId` | Primary disambiguation key | Neither present | 

### Consent
<a name="bulk-member-match-validation-consent"></a>


| Field | How HealthLake uses it | Validation failure if... | 
| --- | --- | --- | 
| `scope` | Confirms consent scope is patient-privacy | Missing or no patient-privacy code | 
| `category` | Confirms disclosure classification | Missing | 
| `patient` | Identifies the consent subject | Missing | 
| `performer` | Identifies who is agreeing | Missing | 
| `sourceReference` | Documents the consent source | Missing | 
| `policy.uri` | Determines data sharing scope | Missing or URI not ending in \#regular or \#sensitive | 
| `provision.type` | Must be "permit" per HRex Consent profile | Missing or not "permit" (including "deny") | 
| `provision.period` | Evaluated at Step 4 for consent-constrained check | Missing or no start/end | 
| `provision.actor` | Identifies source and recipient payers | Missing or does not include required source \+ recipient actors per HRex profile | 
| `provision.action` | Confirms disclosure action | Missing or no "disclose" code | 
| `status` | Must be "active" per HRex IG | Not "active" — returns 400 validation error | 

**Note**  
Per the HRex IG, `Consent.status` is fixed to "active". HealthLake enforces this at Step 1 (structural validation) and returns a 400 validation error if any other status is provided. Non-active consent will not be processed nor classified into ConsentConstrainedMembers — it is rejected upfront.

## Matching behavior
<a name="bulk-member-match-matching-behavior"></a>
+ **Patient search (Step 2)** — HealthLake searches using `name.family` \+ `name.given` (exact, case-insensitive), `birthDate` (exact), `gender` (exact; Birth Sex used if gender absent), and `identifier` (when present, optional).
+ **Coverage disambiguation (Step 3)** — When multiple patient candidates are found, `CoverageToMatch` is used to narrow to one. A coverage is "valid" when an active Coverage resource exists in the datastore matching on `subscriberId` or `identifier` (MB type).
+ **Consent evaluation (Step 4)** — Only performed after a successful unique match. See the consent evaluation details section above.

## Error handling
<a name="bulk-member-match-errors"></a>

The operation handles the following error conditions:
+ **400 Bad Request**: Invalid request format, missing required parameters, or payload exceeds size limits (500 members or 5 MB).
+ **422 Unprocessable Entity**: Processing errors during job execution.
+ **Individual member errors**: When a specific member fails to process, the operation continues with remaining members and includes error details with appropriate reason codes. For example, a `MemberBundle` with a Patient missing the `birthDate` parameter will return the following error:

  ```
  "errors": [
    {
      "memberIndex": 1,
      "jsonBlob": {
        "resourceType": "OperationOutcome",
        "issue": [
          {
            "severity": "error",
            "code": "invalid",
            "diagnostics": "MemberPatient.birthDate is required"
          }
        ],
        "statusCode": 400
      }
    }
  ]
  ```

Error details are available through the status polling endpoint and include:
+ `numberOfMembersWithCustomerError`: Count of members with validation or input errors.
+ `numberOfMembersWithServerError`: Count of members with server-side processing errors.

## Related operations
<a name="bulk-member-match-related"></a>
+ [`$member-match` operation for HealthLake](reference-fhir-operations-member-match.md) — Individual member matching operation.
+ [FHIR R4 `$davinci-data-export` operation for HealthLake](reference-fhir-operations-davinci-data-export.md) — Bulk data export using Group resources.
+ [FHIR R4 `$operations` for HealthLake](reference-fhir-operations.md) — Complete list of supported operations.
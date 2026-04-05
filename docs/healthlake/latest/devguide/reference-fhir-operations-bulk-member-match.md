# `$bulk-member-match` operation for HealthLake

AWS HealthLake supports the `$bulk-member-match` operation for processing multiple member match requests asynchronously. This operation enables healthcare organizations to efficiently match hundreds of members' unique identifiers across different healthcare systems using demographic and coverage information in a single bulk request. This capability is essential for large-scale payer-to-payer data exchange, member transitions, and CMS compliance requirements and follows the FHIR [specification](https://build.fhir.org/ig/HL7/davinci-epdx/OperationDefinition-BulkMemberMatch.html "https://build.fhir.org/ig/HL7/davinci-epdx/OperationDefinition-BulkMemberMatch.html").

###### Note

The `$bulk-member-match` operation is based on an underlying FHIR specification that is currently experimental and subject to change. As the specification evolves, the behavior and interface of this API will be updated accordingly. Developers are advised to monitor AWS HealthLake release notes and the relevant FHIR specification updates to stay informed of any changes that may impact their integrations.

This operation is particularly useful when you need to:

- Process member matching at scale during open enrollment periods
- Facilitate bulk member transitions between payers
- Support large-scale CMS compliance data exchange requirements
- Efficiently match member cohorts across healthcare networks
- Minimize API calls and improve operational efficiency for high-volume matching scenarios

## Usage

The `$bulk-member-match` operation is an asynchronous operation invoked on Group resources using the POST method:

```
POST [base]/Group/$bulk-member-match
```

After submitting a bulk match request, you can poll the job status using:

```
GET [base]/$bulk-member-match-status/{jobId}
```

## Supported parameters

HealthLake supports the following FHIR `$bulk-member-match` parameters:

| Parameter         | Type     | Required | Description                                                                                                                                                       |
| ----------------- | -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MemberPatient`   | Patient  | Yes      | Patient resource containing demographic information for the member to be matched.                                                                                 |
| `CoverageToMatch` | Coverage | Yes      | Coverage resource that will be used for matching against existing records.                                                                                        |
| `CoverageToLink`  | Coverage | No       | Coverage resource to be linked during the matching process.                                                                                                       |
| `Consent`         | Consent  | Yes      | Consent resource for authorization purposes is also stored. This is different than the individual `$member-match` operation where Consent is \*not<br>• required. |

## POST request to submit bulk member match job

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

## Output Group resources

The completed job returns a Parameters resource containing three Group resources:

**MatchedMembers Group**
Contains Patient references for all successfully matched members and is not categorized as consent constraint.

The `Group.quantity` field contains the total count of members in each of their respective groups.

**NonMatchedMembers Group**
Contains references to members where no match was found or multiple matches were identified.

**ConsentConstrainedMembers Group**

Contains Patient references for all successfully matched members where consent constraints prevent data sharing. A Consent resource is considered constrained when both of the following conditions are present:

- **The policy URI ends in `#sensitive`** — This is the clearest, most direct signal. The submitting payer is explicitly saying: "This member's data is sensitive — handle with care."

```
"policy": [{ "uri": "...hrex-consent.html#sensitive" }]
```

- **The top-level provision type is `deny`** — The member has broadly refused data sharing.

```
"provision": { "type": "deny" }
```

## Integration with $davinci-data-export

The MatchedMembers Group resource returned by `$bulk-member-match` can be directly used with the `$davinci-data-export` operation to retrieve bulk member data:

```
POST [base]/Group/{matched-group-id}/$davinci-data-export
GET [base]/Group/{matched-group-id}
```

This integration enables efficient workflows where you first identify matched members in bulk, then export their complete health records using the resulting Group resource.

## Performance characteristics

The `$bulk-member-match` operation is designed for high-volume processing and runs asynchronously:

- **Concurrency**: Maximum of 5 concurrent operations per data store.
- **Scalability**: Handles up to 500 members per request (5 MB payload limit).
- **Parallel operations**: Compatible with concurrent import, export, or bulk-delete operations.

## Authorization

The API uses SMART on FHIR authorization protocol with the following required scopes:

- `system/Patient.read` — Required to search and match patient resources.
- `system/Coverage.read` — Required to validate coverage information.
- `system/Group.write` — Required to create result Group resources.
- `system/Organization.read` — Conditional, required if coverage references organizations.
- `system/Practitioner.read` — Conditional, required if coverage references practitioners.
- `system/PractitionerRole.read` — Conditional, required if coverage references practitioner roles.
- `system/Consent.write` — Conditional, required if consent resources are provided.

The operation also supports AWS IAM Signature Version 4 (SigV4) authorization for programmatic access.

## Error handling

The operation handles the following error conditions:

- **400 Bad Request**: Invalid request format, missing required parameters, or payload exceeds size limits (500 members or 5 MB).
- **422 Unprocessable Entity**: Processing errors during job execution.
- **Individual member errors**: When a specific member fails to process, the operation continues with remaining members and includes error details in the NonMatchedMembers Group with appropriate reason codes. For example, a `MemberBundle` with a Patient missing the `birthDate` parameter will return the following error:

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

- `numberOfMembersWithCustomerError`: Count of members with validation or input errors.
- `numberOfMembersWithServerError`: Count of members with server-side processing errors.

## Related operations

- [$member-match operation for HealthLake](reference-fhir-operations-member-match.md "reference-fhir-operations-member-match.md") — Individual member matching operation.
- [FHIR R4 $davinci-data-export operation for HealthLake](reference-fhir-operations-davinci-data-export.md "reference-fhir-operations-davinci-data-export.md") — Bulk data export using Group resources.
- [FHIR R4 $operations for HealthLake](reference-fhir-operations.md "reference-fhir-operations.md") — Complete list of supported operations.

# Bundling FHIR resources

A FHIR `Bundle` is a container for a collection of FHIR resources in
AWS HealthLake. AWS HealthLake supports two types of bundles with different processing
behaviors.

[`Batch`](https://hl7.org/fhir/R4/http.html#transaction "https://hl7.org/fhir/R4/http.html#transaction")
bundles process each resource independently. If one resource fails, the remaining resources
can still succeed. Each operation is processed individually, and processing continues even when
some operations fail. Use batch bundles for bulk operations where partial success is
acceptable, such as uploading multiple unrelated patient records.

[`Transaction`](https://hl7.org/fhir/R4/http.html#transaction "https://hl7.org/fhir/R4/http.html#transaction")
bundles process all resources atomically as a single unit. Either all resource operations succeed,
or AWS HealthLake commits none of them. Use transaction bundles when you need guaranteed
referential integrity across related resources, such as creating a patient with related
observations and conditions where all data must be recorded together.

Differences between batch and transaction bundles| Feature | Batch | Transaction |
| --- | --- | --- |
| Processing model | Each operation succeeds or fails independently. | All operations succeed or fail as a single atomic unit. |
| Failure handling | Processing continues even if individual operations fail. | The entire bundle fails if any single operation fails. |
| Execution order | Execution order is not guaranteed. | Operations are processed in the order specified. |
| Referential integrity | Not enforced across operations. | Enforced for locally referenced resources within the bundle. |
| Best used for | Bulk operations where partial success is acceptable. | Related resources that must be created or updated together. |

You can bundle FHIR resources of the same or different types, and they can include a mix
of FHIR operations, such as `create`,
`read`, `update`, `delete`, and `patch`.
For additional information, see [Resource
Bundle](https://hl7.org/fhir/R4/Bundle "https://hl7.org/fhir/R4/Bundle") in the **FHIR R4 documentation**.

The following are example use cases for each bundle type.

Batch bundles

- Upload multiple unrelated patient records from different facilities during nightly data synchronization.
- Bulk upload historical medication records where some records might have validation issues.
- Load reference data, such as organizations and practitioners, where individual failures don't affect other entries.

Transaction bundles

- Create a patient with related observations and conditions during an emergency department admission where all data must be recorded together.
- Update a patient's medication list and related allergy information that must remain consistent.
- Record a complete encounter with the patient, observations, procedures, and billing information as a single atomic unit.

###### Important

Both batch and transaction bundles use the same `Bundle` resource structure. The only difference is the value of the `type` field.

The following example shows a transaction bundle with multiple resource types and operations.

```
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "fullUrl": "urn:uuid:4f6a30fb-cd3c-4ab6-8757-532101f72065",
      "resource": {
        "resourceType": "Patient",
        "id": "new-patient",
        "active": true,
        "name": [
          {
            "family": "Johnson",
            "given": [
              "Sarah"
            ]
          }
        ],
        "gender": "female",
        "birthDate": "1985-08-12",
        "telecom": [
          {
            "system": "phone",
            "value": "555-123-4567",
            "use": "home"
          }
        ]
      },
      "request": {
        "method": "POST",
        "url": "Patient"
      }
    },
    {
      "fullUrl": "urn:uuid:7f83f473-d8cc-4a8d-86d3-9d9876a3248b",
      "resource": {
        "resourceType": "Observation",
        "id": "blood-pressure",
        "status": "final",
        "code": {
          "coding": [
            {
              "system": "http://loinc.org",
              "code": "85354-9",
              "display": "Blood pressure panel"
            }
          ],
          "text": "Blood pressure panel"
        },
        "subject": {
          "reference": "urn:uuid:4f6a30fb-cd3c-4ab6-8757-532101f72065"
        },
        "effectiveDateTime": "2023-10-15T09:30:00Z",
        "component": [
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "8480-6",
                  "display": "Systolic blood pressure"
                }
              ]
            },
            "valueQuantity": {
              "value": 120,
              "unit": "mmHg",
              "system": "http://unitsofmeasure.org",
              "code": "mm[Hg]"
            }
          },
          {
            "code": {
              "coding": [
                {
                  "system": "http://loinc.org",
                  "code": "8462-4",
                  "display": "Diastolic blood pressure"
                }
              ]
            },
            "valueQuantity": {
              "value": 80,
              "unit": "mmHg",
              "system": "http://unitsofmeasure.org",
              "code": "mm[Hg]"
            }
          }
        ]
      },
      "request": {
        "method": "POST",
        "url": "Observation"
      }
    },
    {
      "resource": {
        "resourceType": "Appointment",
        "id": "appointment-123",
        "status": "booked",
        "description": "Annual physical examination",
        "start": "2023-11-15T09:00:00Z",
        "end": "2023-11-15T09:30:00Z",
        "participant": [
          {
            "actor": {
              "reference": "urn:uuid:4f6a30fb-cd3c-4ab6-8757-532101f72065"
            },
            "status": "accepted"
          }
        ]
      },
      "request": {
        "method": "PUT",
        "url": "Appointment/appointment-123"
      }
    },
    {
      "request": {
        "method": "DELETE",
        "url": "MedicationRequest/med-request-456"
      }
    }
  ]
}
```

## Bundling FHIR resources as independent entities

###### To bundle FHIR resources as independent entities

1. Collect HealthLake `region` and `datastoreId` values. For
   more information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Construct a URL for the request using the collected values for HealthLake
   `region` and `datastoreId`. Do
   _not_ specify a FHIR resource type in the URL. To view
   the entire URL path in the following example, scroll over the
   **Copy** button.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/
```

3. Construct a JSON body for the request, specifying each HTTP verb as part of
   the `method` elements. The following example uses a
   `batch` type interaction with the `Bundle` resource to
   create new `Patient` and `Medication` resources. All
   required sections are commented accordingly. For the purpose of this procedure,
   save the file as `batch-independent.json`.

```
{
    "resourceType": "Bundle",
    "id": "bundle-batch",
    "meta": {
        "lastUpdated": "2014-08-18T01:43:30Z"
    },
    "type": "batch",
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "meta": {
                    "lastUpdated": "2022-06-03T17:53:36.724Z"
                },
                "text": {
                    "status": "generated",
                    "div": "Some narrative"
                },
                "active": true,
                "name": [
                    {
                        "use": "official",
                        "family": "Jackson",
                        "given": [
                            "Mateo",
                            "James"
                        ]
                    }
                ],
                "gender": "male",
                "birthDate": "1974-12-25"
            },
            "request": {
                "method": "POST",
                "url": "Patient"
            }
        },
        {
            "resource": {
                "resourceType": "Medication",
                "id": "med0310",
                "contained": [
                    {
                        "resourceType": "Substance",
                        "id": "sub03",
                        "code": {
                            "coding": [
                                {
                                    "system": "http://snomed.info/sct",
                                    "code": "55452001",
                                    "display": "Oxycodone (substance)"
                                }
                            ]
                        }
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "430127000",
                            "display": "Oral Form Oxycodone (product)"
                        }
                    ]
                },
                "form": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "385055001",
                            "display": "Tablet dose form (qualifier value)"
                        }
                    ]
                },
                "ingredient": [
                    {
                        "itemReference": {
                            "reference": "#sub03"
                        },
                        "strength": {
                            "numerator": {
                                "value": 5,
                                "system": "http://unitsofmeasure.org",
                                "code": "mg"
                            },
                            "denominator": {
                                "value": 1,
                                "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
                                "code": "TAB"
                            }
                        }
                    }
                ]
            },
            "request": {
                "method": "POST",
                "url": "Medication"
            }
        }
    ]
}

```

4. Send the request. The FHIR `Bundle` batch type uses a
   `POST` request with either [AWS Signature Version
   4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") or SMART on FHIR authorization. The following code example uses
   the `curl` command line tool for demonstration purposes.

SigV4
SigV4 authorization

```
curl --request POST \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json' \
  --data @batch-type.json

```

SMART on FHIR
SMART on FHIR authorization example for the [`IdentityProviderConfiguration`](../APIReference/API_IdentityProviderConfiguration.md "../APIReference/API_IdentityProviderConfiguration.md") data type.

```
{
    "AuthorizationStrategy": "SMART_ON_FHIR",
    "FineGrainedAuthorizationEnabled": true,
    "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
    "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\",\"permission-v2\"]}"
}

```

The caller can assign permissions in the authorization lambda. For more
information, see [OAuth 2.0
scopes](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md").

The server returns a response showing the `Patient` and
`Medication` resources created as a result of the
`Bundle` batch type request.

## Conditional PUTs in bundles

AWS HealthLake supports conditional updates within bundles using the following query parameters:

###### Note

Conditional PUTs are supported only in `batch` bundles. `Transaction` bundles do not support conditional PUTs.

- `_id` (standalone)
- `_id` in combination with one of the following:

  - `_tag`
  - `createdAt`
  - `_lastUpdated`

When you use conditional PUTs in bundles, AWS HealthLake evaluates the query parameters against existing resources and takes action based on the match results.

Conditional update behavior| Scenario | HTTP status | Action taken |
| --- | --- | --- |
| Resource without ID provided | 201 Created | Always creates a new resource. |
| Resource with new ID (no match) | 201 Created | Creates a new resource with the specified ID. |
| Resource with existing ID (single match) | 200 OK | Updates the matching resource. |
| Resource with existing ID (conflict detected) | 409 Conflict | Returns an error. No changes are made. |
| Resource with existing ID (ID mismatch) | 400 Bad Request | Returns an error. No changes are made. |
| Multiple resources match conditions | 412 Precondition Failed | Returns an error. No changes are made. |

In the following example bundle with a conditional update, the `Patient` resource with FHIR ID `476` updates only if the condition `_lastUpdated=lt2025-04-20` is met.

```
{
    "resourceType": "Bundle",
    "id": "bundle-batch",
    "meta": {
        "lastUpdated": "2014-08-18T01:43:30Z"
    },
    "type": "batch",
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "id": "476",
                "meta": {
                    "lastUpdated": "2022-06-03T17:53:36.724Z"
                },
                "active": true,
                "name": [
                    {
                        "use": "official",
                        "family": "Jackson",
                        "given": [
                            "Mateo",
                            "James"
                        ]
                    }
                ],
                "gender": "male",
                "birthDate": "1974-12-25"
            },
            "request": {
                "method": "PUT",
                "url": "Patient?_id=476&_lastUpdated=lt2025-04-20"
            }
        },
        {
            "resource": {
                "resourceType": "Medication",
                "id": "med0310",
                "contained": [
                    {
                        "resourceType": "Substance",
                        "id": "sub03",
                        "code": {
                            "coding": [
                                {
                                    "system": "http://snomed.info/sct",
                                    "code": "55452001",
                                    "display": "Oxycodone (substance)"
                                }
                            ]
                        }
                    }
                ],
                "code": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "430127000",
                            "display": "Oral Form Oxycodone (product)"
                        }
                    ]
                },
                "form": {
                    "coding": [
                        {
                            "system": "http://snomed.info/sct",
                            "code": "385055001",
                            "display": "Tablet dose form (qualifier value)"
                        }
                    ]
                },
                "ingredient": [
                    {
                        "itemReference": {
                            "reference": "#sub03"
                        },
                        "strength": {
                            "numerator": {
                                "value": 5,
                                "system": "http://unitsofmeasure.org",
                                "code": "mg"
                            },
                            "denominator": {
                                "value": 1,
                                "system": "http://terminology.hl7.org/CodeSystem/v3-orderableDrugForm",
                                "code": "TAB"
                            }
                        }
                    }
                ]
            },
            "request": {
                "method": "POST",
                "url": "Medication"
            }
        }
    ]
}

```

## Bundling FHIR resources as a single entity

###### To bundle FHIR resources as a single entity

1. Collect HealthLake `region` and `datastoreId` values. For
   more information, see [Getting data store
   properties](managing-data-stores-describe.md "managing-data-stores-describe.md").
2. Construct a URL for the request using the collected values for HealthLake
   `region` and `datastoreId`. Include the FHIR
   resource type `Bundle` as part of the URL. To view the entire URL
   path in the following example, scroll over the **Copy**
   button.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Bundle

```

3. Construct a JSON body for the request, specifying the FHIR resources to
   group together. The following example groups two `Patient` resources
   in HealthLake. For the purpose of this procedure, save the file as
   `batch-single.json`.

```
{
    "resourceType": "Bundle",
    "id": "bundle-minimal",
    "language": "en-US",
    "identifier": {
        "system": "urn:oid:1.2.3.4.5",
        "value": "28b95815-76ce-457b-b7ae-a972e527db4f"
    },
    "type": "document",
    "timestamp": "2020-12-11T14:30:00+01:00",
    "entry": [
        {
            "fullUrl": "urn:uuid:f40b07e3-37e8-48c3-bf1c-ae70fe12dabf",
            "resource": {
                "resourceType": "Composition",
                "id": "f40b07e3-37e8-48c3-bf1c-ae70fe12dabf",
                "status": "final",
                "type": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "60591-5",
                            "display": "Patient summary Document"
                        }
                    ]
                },
                "date": "2020-12-11T14:30:00+01:00",
                "author": [
                    {
                        "reference": "urn:uuid:45271f7f-63ab-4946-970f-3daaaa0663ff"
                    }
                ],
                "title": "Patient Summary as of December 7, 2020 14:30"
            }
        },
        {
            "fullUrl": "urn:uuid:45271f7f-63ab-4946-970f-3daaaa0663ff",
            "resource": {
                "resourceType": "Practitioner",
                "id": "45271f7f-63ab-4946-970f-3daaaa0663ff",

                "active": true,
                "name": [
                    {
                        "family": "Doe",
                        "given": [
                            "John"
                        ]
                    }
                ]
            }
        }
    ]
}

```

4. Send the request. The FHIR `Bundle` document type uses a
   `POST` request with [AWS Signature Version
   4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") signing protocol. The following code example uses the
   `curl` command line tool for demonstration purposes.

SigV4
SigV4 authorization

```
curl --request POST \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Bundle' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json' \
  --data @document-type.json

```

SMART on FHIR
SMART on FHIR authorization example for the [`IdentityProviderConfiguration`](../APIReference/API_IdentityProviderConfiguration.md "../APIReference/API_IdentityProviderConfiguration.md") data type.

```
{
    "AuthorizationStrategy": "SMART_ON_FHIR",
    "FineGrainedAuthorizationEnabled": true,
    "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
    "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\",\"permission-v2\"]}"
}

```

The caller can assign permissions in the authorization lambda. For more
information, see [OAuth 2.0
scopes](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md").

The server returns a response showing two `Patient` resources
created as a result of the `Bundle` document type request.

## Configuring validation level for bundles

When bundling FHIR resources, you can optionally specify an
`x-amzn-healthlake-fhir-validation-level` HTTP header to configure a
validation level for the resource. This validation level will be set for all create and update
requests within the bundle. AWS HealthLake currently supports the following validation levels:

- `strict`: Resources are validated according to the profile element of
  the resource, or the R4 specification if no profile is present. This is the default validation
  level for AWS HealthLake.
- `structure-only`: Resources are validated against R4, ignoring any
  referenced profiles.
- `minimal`: Resources are validated minimally, ignoring certain R4
  rules. Resources that fail structure checks required for search/analytics will be updated to
  include a warning for audit.

Resources bundled with the minimal validation level may be ingested into a Datastore despite
failing validation required for search indexing. In this case, resources will be updated to include
a Healthlake specific extension to document said failures, and the entries within the Bundle
response will include OperationOutcome resources as follows:

```
{
    "resourceType": "Bundle",
    "type": "batch-response",
    "timestamp": "2025-08-25T22:58:48.846287342Z",
    "entry": [
        {
            "response": {
                "status": "201",
                "location": "Patient/195abc49-ba8e-4c8b-95c2-abc88fef7544/_history/1",
                "etag": "W/\"1\"",
                "lastModified": "2025-08-25T22:58:48.801245445Z",
                "outcome": {
                    "resourceType": "OperationOutcome",
                    "issue": [
                        {
                            "severity": "error",
                            "code": "processing",
                            "details": {
                                "text": "FHIR resource in payload failed FHIR validation rules."
                            },
                            "diagnostics": "FHIR resource in payload failed FHIR validation rules."
                        }
                    ]
                }
            }
        }
    ]
}
```

Additionally, the following HTTP response header will be included with a value of "true":

```
x-amzn-healthlake-validation-issues : true
```

###### Note

Note that data ingested that is malformed according the R4 specification may not be
searchable as expected if these errors are present.

## Limited support for Bundle type "message"

HealthLake provides limited support for FHIR Bundle type `message` through an internal conversion process. This support is designed for scenarios where message bundles cannot be reformatted at the source, such as ingesting ADT (Admission, Discharge, Transfer) feeds from legacy hospital systems.

###### Warning

This feature requires explicit AWS account allowlisting and does not enforce FHIR R4 message semantics or referential integrity. Contact AWS Support to request enablement for your account before using message bundles.

### Key differences from standard message processing

- **Message Bundles** (FHIR specification): First entry must be a `MessageHeader` that references other resources. Resources lack individual `request` objects, and the MessageHeader event determines processing actions.
- **HealthLake Processing**: Converts message Bundles to batch Bundles by automatically assigning PUT operations to each resource entry. Resources are processed independently without enforcing message semantics or referential integrity.

### Important limitations

- FHIR R4 Message-specific processing rules are not enforced
- No transactional integrity across resources
- Inter-resource references are not validated
- Requires explicit account allowlisting

### Example message Bundle structure

```
{
              "resourceType": "Bundle",
              "type": "message",
              "entry": [
                {
                  "resource": {
                    "resourceType": "MessageHeader",
                    "eventCoding": {
                      "system": "http://hl7.org/fhir/us/davinci-alerts/CodeSystem/notification-event",
                      "code": "notification-admit"
                    },
                    "focus": [{"reference": "Encounter/example-id"}]
                  }
                },
                {
                  "resource": {"resourceType": "Patient", "id": "example-id"}
                },
                {
                  "resource": {"resourceType": "Encounter", "id": "example-id"}
                }
              ]
            }

```

###### Note

Each resource is stored independently as if submitted via individual PUT operations. If full FHIR messaging semantics or referential integrity validation are required, pre-process message Bundles or implement application-level validation before submission.

## Asynchronous bundle transactions

AWS HealthLake supports asynchronous `Bundle` type `transaction` that allows you to submit
transactions with up to 500 resources. When you submit an
asynchronous transaction, HealthLake queues it for processing and immediately returns a
polling URL. You can use this URL to check the status and retrieve the response. This follows the [FHIR async
bundle pattern](https://hl7.org/fhir/async-bundle.html "https://hl7.org/fhir/async-bundle.html").

###### When to use asynchronous transactions

- You need to submit more than 100 resources (synchronous limit) in a single transaction.
- You want to avoid blocking your application while waiting for transaction processing to complete.
- You need to process high volumes of related resources with better throughput.

###### Important

Polling results are available for 90 days after the transaction is completed. After this 90-day period, the polling URL no longer returns results. Design your integration to retrieve and store results within this window.

###### Note

Synchronous `Bundle` type `transaction` continues to support up to 100 resources and is the default processing mode. If you submit a `Bundle` type `transaction` with more than 100 resources without the `Prefer: respond-async` header, HealthLake returns a `422 Unprocessable Entity` error. Bundles with type `batch` are not supported for asynchronous processing—only `Bundle` type `transaction` can be submitted asynchronously (with up to 500 operations).

###### Note

`PATCH` operations and conditional PUTs are not supported in asynchronous bundle transactions.

### Submitting an asynchronous transaction

To submit an asynchronous transaction, send a `POST` request to the
data store endpoint with the `Prefer: respond-async` header. The bundle
must have type `transaction`. Bundles with type `batch`
are not supported for asynchronous bundle processing.

HealthLake does initial validations for the bundle at submission time.
If validation succeeds, HealthLake returns HTTP 202 Accepted with a
`content-location` response header that contains the polling URL.

###### To submit an asynchronous `Bundle` type `transaction`

1. Send a `POST` request to the HealthLake data store endpoint.

```
POST https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/
```

2. Construct a JSON body for the request with bundle type
   `transaction`. For the purpose of this procedure, save the file
   as `async-transaction.json`.

```
{
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "resource": {
                "resourceType": "Patient",
                "active": true,
                "name": [
                    {
                        "use": "official",
                        "family": "Smith",
                        "given": ["Jane"]
                    }
                ],
                "gender": "female",
                "birthDate": "1990-01-15"
            },
            "request": {
                "method": "POST",
                "url": "Patient"
            }
        },
        {
            "resource": {
                "resourceType": "Observation",
                "status": "final",
                "code": {
                    "coding": [
                        {
                            "system": "http://loinc.org",
                            "code": "85354-9",
                            "display": "Blood pressure panel"
                        }
                    ]
                },
                "subject": {
                    "reference": "urn:uuid:example-patient-id"
                }
            },
            "request": {
                "method": "POST",
                "url": "Observation"
            }
        }
    ]
}
```

3. Send the request with the `Prefer: respond-async` header. The
   FHIR `Bundle` transaction type uses a `POST`
   request with either [AWS Signature Version
   4](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") or SMART on FHIR authorization. The following code example
   uses the `curl` command line tool for demonstration
   purposes.

SigV4
SigV4 authorization

```
curl --request POST \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json' \
  --header 'Prefer: respond-async' \
  --data @async-transaction.json

```

SMART on FHIR
SMART on FHIR authorization example for the [`IdentityProviderConfiguration`](../APIReference/API_IdentityProviderConfiguration.md "../APIReference/API_IdentityProviderConfiguration.md") data type.

```
{
    "AuthorizationStrategy": "SMART_ON_FHIR",
    "FineGrainedAuthorizationEnabled": true,
    "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name",
    "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\",\"permission-v2\"]}"
}

```

The caller can assign permissions in the authorization lambda. For more
information, see [OAuth 2.0
scopes](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md"). 4. On successful submission, the server returns HTTP 202 Accepted. The
`content-location` response header contains the polling URL.
The response body is an `OperationOutcome` resource.

```
HTTP/1.1 202 Accepted
content-location: https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Transaction/`transactionId`
```

```
{
    "resourceType": "OperationOutcome",
    "issue": [
        {
            "severity": "information",
            "code": "informational",
            "diagnostics": "Submitted Asynchronous Bundle Transaction",
            "location": [
                "https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Transaction/`transactionId`"
            ]
        }
    ]
}
```

### Polling for transaction status

After you submit an asynchronous transaction, use the polling URL from the
`content-location` response header to check the transaction status.
Send a `GET` request to the polling URL.

###### Note

For SMART on FHIR enabled data stores, the authorization token must include
`read` permissions on the `Transaction` resource type
to poll for transaction status. For more information about SMART on FHIR
scopes, see [SMART on FHIR OAuth 2.0 scopes supported by HealthLake](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md").

Send a `GET` request to the polling URL. The following example uses
the `curl` command line tool.

SigV4
SigV4 authorization

```
curl --request GET \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Transaction/`transactionId`' \
  --aws-sigv4 'aws:amz:`region`:healthlake' \
  --user "`$AWS_ACCESS_KEY_ID`:`$AWS_SECRET_ACCESS_KEY`" \
  --header "x-amz-security-token:`$AWS_SESSION_TOKEN`" \
  --header 'Accept: application/json'
```

SMART on FHIR
SMART on FHIR authorization. The authorization token must include
`read` permissions on the `Transaction`
resource type.

```
curl --request GET \
  'https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Transaction/`transactionId`' \
  --header 'Authorization: Bearer `$SMART_ACCESS_TOKEN`' \
  --header 'Accept: application/json'
```

The following table describes the possible responses.

Polling response codes| HTTP status | Meaning | Response body |
| --- | --- | --- |
| 202 Accepted | Transaction is queued | `OperationOutcome` with diagnostics<br>"SUBMITTED" |
| 202 Accepted | Transaction is being processed | `OperationOutcome` with diagnostics<br>"IN\_PROGRESS" |
| 200 OK | Transaction completed successfully | `Bundle` with type<br>`transaction-response` |
| 4xx/5xx | Transaction failed | `OperationOutcome` with error details |

The following examples show each response type.

###### Transaction queued (202)

```
{
    "resourceType": "OperationOutcome",
    "id": "`transactionId`",
    "issue": [
        {
            "severity": "information",
            "code": "informational",
            "diagnostics": "SUBMITTED"
        }
    ]
}
```

###### Transaction processing (202)

```
{
    "resourceType": "OperationOutcome",
    "id": "`transactionId`",
    "issue": [
        {
            "severity": "information",
            "code": "informational",
            "diagnostics": "IN_PROGRESS"
        }
    ]
}
```

###### Transaction completed (200)

```
{
    "resourceType": "Bundle",
    "type": "transaction-response",
    "entry": [
        {
            "response": {
                "status": "201",
                "location": "Patient/example-id/_history/1",
                "etag": "W/\"1\"",
                "lastModified": "2024-01-15T10:30:00.000Z"
            }
        },
        {
            "response": {
                "status": "201",
                "location": "Observation/example-id/_history/1",
                "etag": "W/\"1\"",
                "lastModified": "2024-01-15T10:30:00.000Z"
            }
        }
    ]
}
```

###### Transaction failed (4xx/5xx)

```
{
    "resourceType": "OperationOutcome",
    "issue": [
        {
            "severity": "error",
            "code": "exception",
            "diagnostics": "Transaction failed: conflict detected on resource Patient/example-id"
        }
    ]
}
```

### Processing order

Asynchronous bundles of type `transaction` are queued but are not processed in strict submission order. HealthLake optimizes processing based on available capacity and system load.

###### Important

Do not depend on transactions being processed in the order they were submitted. For example, if you submit Transaction A at 10:00 AM and Transaction B at 10:01 AM, Transaction B might complete before Transaction A. Design your application to:

- Handle out-of-order completion.
- Use the polling URL to track each transaction independently.
- Implement application-level sequencing if order matters for your use case.

### Quotas and throttling

The following quotas and rate limits apply to asynchronous transactions.

Asynchronous transaction quotas| Quota | Value | Adjustable |
| --- | --- | --- |
| Maximum operations per asynchronous transaction | 500 | No |
| Maximum pending transactions per data store | 500 | Yes |

- Asynchronous transactions share the same API rate limits defined under
  [Service quotas](reference-healthlake-endpoints-quotas.md#reference-healthlake-quotas "reference-healthlake-endpoints-quotas.md#reference-healthlake-quotas").
- Polling for transaction status shares the same API rate limits as read
  (`GET`) operations on FHIR resources.
- If the pending transaction limit is reached, subsequent submissions
  return an error until existing transactions complete.

### Error handling

For a 'transaction' bundle, all FHIR resources contained in the bundle are
processed as an atomic operation. All the resources in the operation must
succeed, or no operations in the bundle are processed.

Errors fall into two categories: submission errors that HealthLake returns
synchronously, and processing errors that you retrieve through polling.

###### Submission errors

HealthLake validates the bundle at submission time and returns errors synchronously
before the transaction is queued. Submission errors include invalid FHIR resource
validation errors, unsupported resource types, exceeding the 500 operations limit,
and using the `Prefer: respond-async` header with batch bundles. If the
pending transaction limit for the data store has been reached, HealthLake returns a
`ThrottlingException`. When a submission error occurs, the
transaction will not be queued.

###### Processing errors

Processing errors occur after the transaction has been queued and are returned
through the polling URL. These include transaction conflicts, where another
operation modified a resource that is part of the transaction, and server errors
during processing. When a processing error occurs, no resource mutations are done
for resources in the transaction. The polling URL will return an
`OperationOutcome` with the error details.

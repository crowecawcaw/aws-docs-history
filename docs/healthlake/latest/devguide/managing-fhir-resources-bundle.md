# Bundling FHIR resources

A FHIR `Bundle` is a container for a collection of FHIR resources in
AWS HealthLake. AWS HealthLake supports two types of bundles with different behaviors: [`batch`](https://hl7.org/fhir/R4/http.html#transaction "https://hl7.org/fhir/R4/http.html#transaction") or [`transaction`](https://hl7.org/fhir/R4/http.html#transaction "https://hl7.org/fhir/R4/http.html#transaction").

- For a 'batch' bundle, each FHIR resource contained in the bundle is processed and logged individually. Each resource operation is treated independently from the other resources.
- For a ‘transaction’ bundle, all FHIR resources contained in the bundle are processed as an atomic operation. All of the resources in the operation must succeed, or no resource updates in the bundle are committed and stored.
  You can bundle FHIR resources of the same or different types, and they can include a mix
  of other FHIR interactions defined in this chapter (e.g. `create`,
  `read`, `update`, `delete`, and `search`).
  For additional information, see [Resource
  Bundle](https://hl7.org/fhir/R4/Bundle "https://hl7.org/fhir/R4/Bundle") in the **FHIR R4 documentation**.

Key differences between Batch and Transaction type Bundles:

Batch

- Independent operations that can succeed or fail individually
- Processing continues even if some operations fail
- Order of execution not guaranteed
- Ideal for bulk operations where partial success is acceptable

Transaction

- Atomicity guaranteed - either all succeed or all fail
- Maintains referential integrity for locally referenced (within Bundle) resources
- Operations processed in the order specified
- Fails completely if any operation fails

Example Use Cases:

- Batch: Uploading multiple unrelated patient records
- Transaction: Creating a patient with related observations and conditions where all must succeed together

###### Note

Both use Bundle resource type but differ in 'type' field:

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

## Bundling FHIR resources as

independent entities

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

## Conditional PUTs in Bundles

AWS HealthLake supports conditional updates within Bundles using the following query parameters:

- `_id` (standalone)
- `_id` in combination with one of the following:
  - `_tag`
  - `_createdAt`
  - `_lastUpdated`

Based on the results of matching the conditions provided to the existing resource, the following will occur with the associated result codes indicating the action taken:

When creating or updating FHIR resources, the system handles different scenarios based on resource ID provision and existing matches:

- Resources without IDs are always created (201).
- Resources with new IDs are created (201).
- Resources with existing IDs either update the matching resource (200) or return errors if there's a conflict (409) or ID mismatch (400).
- Multiple matching resources trigger a precondition failure (419).

In the example Bundle with conditional update, the Patient resource with FHIR ID `456` will only update if the condition `_lastUpdated=lt2025-04-20` is met.

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

## Bundling FHIR resources as a

single entity

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

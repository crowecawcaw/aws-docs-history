# Migrating from an existing FHIR server

To migrate data from an existing FHIR server to HealthLake, follow these steps.

## Step 1: Validate your HealthLake environment

Before beginning any data migration, set up and validate HealthLake through a
proof-of-concept in a development account.

###### To validate your HealthLake environment

1. Create a data store with your chosen authorization strategy (SMART on FHIR
   or AWS SigV4-only) and AWS KMS encryption key. The authorization
   configuration is specified as part of the create data store request. For
   more information, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md") and
   [Creating a SMART on FHIR enabled HealthLake data store](reference-smart-on-fhir-create-data-store.md "reference-smart-on-fhir-create-data-store.md").
2. Set up your API Gateway proxy.
3. Confirm that HealthLake works with your EHR's FHIR API integration
   patterns.
4. Validate the CapabilityStatement (`GET /metadata`) against your
   application's expected supported resources and search parameters.

## Step 2: Export from your existing FHIR server

Run a `$export` operation (System-level or Group-level) against
your current FHIR server per the [FHIR Bulk Data
Access IG](https://build.fhir.org/ig/HL7/bulk-data/en/export.html "https://build.fhir.org/ig/HL7/bulk-data/en/export.html"). This produces
NDJSON files—one newline per FHIR resource, one file per resource
type.

If your server does not support `$export`, extract resources directly
from the underlying database and serialize them as FHIR R4 JSON bundles.

## Step 3: Stage in Amazon S3 and Import

Upload NDJSON containing FHIR resources to an Amazon S3 bucket. The import job
request requires the following four parameters:

- The Amazon S3 input URI
- The Amazon S3 output URI (for job results)
- The data store ID
- The IAM data access role ARN

For more information, see [Starting a FHIR import job](importing-fhir-data-start.md "importing-fhir-data-start.md").

Set the `ValidationLevel` parameter based on your data quality
posture:

| Validation level   | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `strict` (default) | Resources are validated according to the profile element of<br>the resource, or the R4 specification if no profile is present.<br>Profiles must be supported by HealthLake. For a list of supported<br>profiles, see [FHIR profile validations for HealthLake](reference-fhir-profile-validations.md "reference-fhir-profile-validations.md").<br>HealthLake rejects resources that fail validation. |
| `structure-only`   | Resources are validated against R4, ignoring any<br>referenced profiles.                                                                                                                                                                                                                                                                                                                             |
| `minimal`          | Resources are validated minimally, ignoring certain R4<br>rules. Resources that fail structure checks required for<br>search/analytics are updated to include a warning extension<br>for audit.                                                                                                                                                                                                      |

For more information about validation levels, see
[Importing FHIR data with AWS HealthLake](importing-fhir-data.md "importing-fhir-data.md").

## Step 4: Validate the import

HealthLake generates a `manifest.json` file in the output Amazon S3 bucket for
each import job, reporting resource counts for success and failure.

###### To validate the import

1. Reconcile manifest counts against your source system's resource counts by
   type.
2. Inspect `FAILURE/` logs for common causes: invalid references,
   malformed date formats, or profile validation failures.

## Step 5: Cutover

During the cutover window, use HealthLake's standard FHIR create and update APIs for
real-time writes while the bulk import handles historical backfill. For more
information, see [Creating a FHIR resource](managing-fhir-resources-create.md "managing-fhir-resources-create.md") and
[Updating a FHIR resource](managing-fhir-resources-update.md "managing-fhir-resources-update.md"). Once complete,
redirect your application's FHIR endpoint to HealthLake.

HealthLake exposes a standard FHIR R4 RESTful API, so the application-layer
change is typically a base URL swap. If your application uses SMART on FHIR,
you must also update your authorization server's FHIR resource server URL to
point to your HealthLake data store endpoint.

## Step 6: Post-migration validation

Validate that all FHIR operations are working as expected. HealthLake provides
monitoring options across data stores through Amazon CloudWatch and AWS CloudTrail.

###### Note

HealthLake supports R4 only. If your existing server runs STU3 or DSTU2, you must
transform resources to R4 before import. AWS HealthLake Partners provide conversion
tooling for non-R4 data.

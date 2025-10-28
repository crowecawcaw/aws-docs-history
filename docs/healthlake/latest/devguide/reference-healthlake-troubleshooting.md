# Troubleshooting AWS HealthLake

The following topics provide troubleshooting advice for errors and issues that you might
encounter when using the AWS CLI, AWS SDKs, or HealthLake console. If you find an issue that is
not listed in this section, use the **Provide feedback** button on the
right sidebar of this page to report it.

###### Topics

- [Data store actions](#troubleshooting-data-store "#troubleshooting-data-store")
- [Import actions](#troubleshooting-import "#troubleshooting-import")
- [FHIR APIs](#troubleshooting-fhir-apis "#troubleshooting-fhir-apis")
- [NLP integrations](#troubleshooting-nlp-integrations "#troubleshooting-nlp-integrations")
- [SQL integrations](#troubleshooting-sql-integrations "#troubleshooting-sql-integrations")

## Data store actions

**Issue:**
_When I try to create a HealthLake data store, I receive the following
error:_

```
AccessDeniedException: Insufficient Lake Formation permission(s): Required Database on Catalog
```

On November 14, 2022, HealthLake updated the required IAM permissions to create a new
data store. For more information, see [Configure an IAM user or role to use HealthLake
(IAM Administrator)](getting-started-setting-up.md#setting-up-configure-iam "getting-started-setting-up.md#setting-up-configure-iam").

**Issue:**
_When creating a HealthLake data store using the AWS SDKs, the data store creation
status returns an exception or unknown status._

Update your AWS SDK to the latest version if your `DescribeFHIRDatastore` or
`ListFHIRDatastores` API calls return an exception or unknown data store status.

## Import actions

**Issue:**
_Can I still use HealthLake if my data isn't in FHIR R4 format?_

Only FHIR R4 formatted data can be imported into a HealthLake data store. For a list of
partners that can help transform existing health data to FHIR R4 format, see [AWS HealthLake Partners](../../partners.md "../../partners.md").

**Issue:**
_Why did my FHIR import job fail?_

A successful import job will generate a folder with results (output log) in
`.ndjson` format, however, individual records can fail to import. When
this happens, a second `FAILURE` folder will be generated with a manifest of
records that failed to import. For more information, see [Importing FHIR data with AWS HealthLake](importing-fhir-data.md "importing-fhir-data.md").

To analyze why an import job failed use the `DescribeFHIRImportJob` API to analyze the
JobProperties. The following is recommended:

- If the status is `FAILED` and a message is present, the failures
  are related to job parameters such as input data size or number of input files
  being beyond HealthLake quotas.
- If the import job status is `COMPLETED_WITH_ERRORS`, check the
  manifest file, `manifest.json`, for information on which
  files did not import successfully.
- If the import job status is `FAILED` and a message is not present,
  go to the job output location to access the manifest file,
  `manifest.json`.

For each input file, there is failure output file with input file name for any
resource that fails to import. The responses contain line number (lineId) corresponding
to the location of input data, FHIR response object (UpdateResourceResponse), and status
code (statusCode) of the response.

A sample output file might be similar to the following:

```
{"lineId":3, UpdateResourceResponse:{"jsonBlob":{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":"processing","diagnostics":"1 validation error detected: Value 'Patient123' at 'resourceType' failed to satisfy constraint: Member must satisfy regular expression pattern: [A-Za-z]{1,256}"}]}, "statusCode":400}
{"lineId":5, UpdateResourceResponse:{"jsonBlob":{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":"processing","diagnostics":"This property must be an simple value, not a com.google.gson.JsonArray","location":["/EffectEvidenceSynthesis/name"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@telecom'","location":["/EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@gender'","location":["/EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@birthDate'","location":["/EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@address'","location":["/EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@maritalStatus'","location":["/EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@multipleBirthBoolean'","location":["/EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Unrecognised property '@communication'","location":["/EffectEvidenceSynthesis"]},{"severity":"warning","code":"processing","diagnostics":"Name should be usable as an identifier for the module by machine processing applications such as code generation [name.matches('[A-Z]([A-Za-z0-9_]){0,254}')]","location":["EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Profile http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis, Element 'EffectEvidenceSynthesis.status': minimum required = 1, but only found 0","location":["EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Profile http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis, Element 'EffectEvidenceSynthesis.population': minimum required = 1, but only found 0","location":["EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Profile http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis, Element 'EffectEvidenceSynthesis.exposure': minimum required = 1, but only found 0","location":["EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Profile http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis, Element 'EffectEvidenceSynthesis.exposureAlternative': minimum required = 1, but only found 0","location":["EffectEvidenceSynthesis"]},{"severity":"error","code":"processing","diagnostics":"Profile http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis, Element 'EffectEvidenceSynthesis.outcome': minimum required = 1, but only found 0","location":["EffectEvidenceSynthesis"]},{"severity":"information","code":"processing","diagnostics":"Unknown extension http://synthetichealth.github.io/synthea/disability-adjusted-life-years","location":["EffectEvidenceSynthesis.extension[3]"]},{"severity":"information","code":"processing","diagnostics":"Unknown extension http://synthetichealth.github.io/synthea/quality-adjusted-life-years","location":["EffectEvidenceSynthesis.extension[4]"]}]}, "statusCode":400}
{"lineId":7, UpdateResourceResponse:{"jsonBlob":{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":"processing","diagnostics":"2 validation errors detected: Value at 'resourceId' failed to satisfy constraint: Member must satisfy regular expression pattern: [A-Za-z0-9-.]{1,64}; Value at 'resourceId' failed to satisfy constraint: Member must have length greater than or equal to 1"}]}, "statusCode":400}
{"lineId":9, UpdateResourceResponse:{"jsonBlob":{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":"processing","diagnostics":"Missing required id field in resource json"}]}, "statusCode":400}
{"lineId":15, UpdateResourceResponse:{"jsonBlob":{"resourceType":"OperationOutcome","issue":[{"severity":"error","code":"processing","diagnostics":"Invalid JSON found in input file"}]}, "statusCode":400}

```

The example above shows that there were failures on lines 3, 4, 7, 9, 15 from the
corresponding input lines from input file. For each of those lines, the explanations are
as follows:

- On Line 3, the response explains that `resourceType` provided in
  line 3 of input file is not valid.
- On Line 5, the response explains that there is a FHIR validation error in
  line 5 of input file.
- On Line 7, the response explains that there is a validation issue with
  `resourceId` provided as input.
- On Line 9, the response explains that input file must contain a valid resource
  id.
- On line 15, the response of input file is that the file is not in a valid JSON
  format.

## FHIR APIs

**Issue:** _How do I implement authorization for
the FHIR RESTful APIs?_

Determine the [Data store authorization
strategy](getting-started-concepts.md#concept-data-store-authorization-strategy "getting-started-concepts.md#concept-data-store-authorization-strategy") to use.

To create SigV4 authorization using the AWS SDK for Python (Boto3), create a script similar to the
following example.

```
import boto3
import requests
import json
from requests_auth_aws_sigv4 import AWSSigV4

# Set the input arguments
data_store_endpoint = 'https://healthlake.us-east-1.amazonaws.com/datastore/<datastore id>/r4//'
resource_path = "Patient"
requestBody = {"resourceType": "Patient", "active": True, "name": [{"use": "official","family": "Dow","given": ["Jen"]},{"use": "usual","given": ["Jen"]}],"gender": "female","birthDate": "1966-09-01"}
region = 'us-east-1'

#Frame the resource endpoint
resource_endpoint = data_store_endpoint+resource_path
session = boto3.session.Session(region_name=region)
client = session.client("healthlake")

# Frame authorization
auth = AWSSigV4("healthlake", session=session)

# Call data store FHIR endpoint using SigV4 auth

r = requests.post(resource_endpoint, json=requestBody, auth=auth, )
print(r.json())

```

**Issue:**
_Why am I receiving `AccessDenied` errors when using the FHIR
RESTful APIs for a data store encrypted with a customer managed KMS
key?_

Permissions for both customer managed keys and IAM policies are required for a user or
role to access a data store. A user must have the required IAM permissions for using a
customer managed key. If a user revoked or retired a grant that gave HealthLake permission to
use the customer managed KMS key, HealthLake will return an `AccessDenied`
error.

HealthLake must have the permission in place to access customer data, to encrypt new FHIR
resources imported to a data store, and to decrypt the FHIR resources when they are
requested. For more information, see [Troubleshooting AWS KMS
permissions](../../../kms/latest/developerguide/policy-evaluation.md "../../../kms/latest/developerguide/policy-evaluation.md").

**Issue:**
_A FHIR `POST` API operation to HealthLake using a 10MB document is
returning the `413 Request Entity Too Large` error._

AWS HealthLake has a synchronous Create and Update API limit of 5MB to avoid increased
latencies and timeouts. You can ingest large documents, up to 164MB, using the
`Binary` resource type using the Bulk Import API.

## NLP integrations

**Issue:**
_How do I turn on HealthLake's integrated natural language processing
feature?_

As of November 14, 2022, the default behavior of HealthLake data stores changed.

**Current data stores**: All current HealthLake data stores
will stop using natural language processing (NLP) on base64-encoded
`DocumentReference` resources. This means that new
`DocumentReference` resources will not be analyzed using NLP, and no new
resources will be generated based off of text in the `DocumentReference`
resource type. For existing `DocumentReference` resources, the data and
resources generated via NLP remain, but they will not be updated after February 20, 2023.

**New data stores**: HealthLake data stores created after
February 20, 2023 will _not_ perform natural language processing
(NLP) on base64-encoded `DocumentReference` resources.

To turn on HealthLake NLP integration, create a support case using [AWS Support Center Console](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). To create your case, log
in to your AWS account, and then choose **Create case**. To learn
more about creating a case and case management, see [Creating support cases and case
management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") in the _Support User Guide_.

**Issue:**
_>How do I find `DocumentReference` resources that could not be
processed by integrated NLP?_

If a `DocumentReference` resource is not valid, HealthLake provides an extension
indicating a validation error instead of providing it in the integrated medical NLP
output. To find `DocumentReference` resources that led to a validation error
during NLP processing, you can use HealthLake’s FHIR `search` function with
search key **cm-decoration-status** and search value
**VALIDATION_ERROR**. This search will list all
`DocumentReference` resources that led to validation errors, along with
an error message describing the nature of the error. The structure of the extension
field in those `DocumentReference` resources with validation errors will
resemble the following example.

```
"extension": [
          {
              "extension": [
                  {
                      "url": "http://healthlake.amazonaws.com/aws-cm/status/",
                      "valueString": "VALIDATION_ERROR"
                  },
                  {
                      "url": "http://healthlake.amazonaws.com/aws-cm/message/",
                      "valueString": "Resource led to too many nested objects after NLP operation processed the document. 10937 nested objects exceeds the limit of 10000."
                  }
              ],
              "url": "http://healthlake.amazonaws.com/aws-cm/"
          }
    ]

```

###### Note

A `VALIDATION_ERROR` can also occur if NLP decoration creates more than
10,000 nested objects. When this happens, the document must be split into smaller
documents before processing.

## SQL integrations

**Issue:**
_Why do I get a Lake Formation `permissions error:
 lakeformation:PutDataLakeSettings` when adding a new data lake
administrator?_

If your IAM user or role contains the `AWSLakeFormationDataAdmin` AWS managed
policy you cannot add new data lake administrators. You will get an error containing the
following:

```
User arn:aws:sts::111122223333:assumed-role/lakeformation-admin-user is not authorized to perform: lakeformation:PutDataLakeSettings on resource: arn:aws:lakeformation:us-east-2:111122223333:catalog:111122223333 with an explicit deny in an identity-based policy
```

The AWS managed policy `AdministratorAccess` is required to add an IAM
user or role as a AWS Lake Formation data lake administrator. If your IAM user or role also
contains `AWSLakeFormationDataAdmin` the action will fail. The
`AWSLakeFormationDataAdmin` AWS managed policy contains an explicit deny for
the AWS Lake Formation API operation, `PutDataLakeSetting`. Even administrators with
full access to AWS using the `AdministratorAccess` managed policy can be
limited by the `AWSLakeFormationDataAdmin` policy.

**Issue:**
_How do I migrate an existing HealthLake data store to use Amazon Athena SQL
integration?_

HealthLake data stores created before November 14, 2022 are functional, but are not
queryable in Athena using SQL. To query a preexisting data store with Athena, you must
first migrate it to a new data store.

###### To migrate your HealthLake data to a new data store

1. Create a new data store.
2. Export the data from the pre-existing to an Amazon S3 bucket.
3. Import the data into the new data store from the Amazon S3 bucket.

###### Note

Exporting data to an Amazon S3 bucket incurs an extra charge. The extra charge depends
on the size of the data that you export.

**Issue:**
_When creating a new HealthLake data store for SQL integration, the data store
status is not changing from `Creating`._

If you try to create a new HealthLake data store, and your data store status is not
changing from **Creating** you need to update Athena to use the
AWS Glue Data Catalog. For more information, see [Upgrading to the AWS Glue Data Catalog
step-by-step](../../../athena/latest/ug/glue-upgrade.md "../../../athena/latest/ug/glue-upgrade.md") in the _Amazon Athena User Guide_.

After successfully upgrading the AWS Glue Data Catalog, you can create a HealthLake data
store.

To remove an old HealthLake data store, create a support case using [AWS Support Center Console](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). To create your case, log
in to your AWS account, and then choose **Create case**. To learn
more, see [Creating support cases and case management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") in the _Support User
Guide_.

**Issue:**
_The Athena console is not working after importing data into a new HealthLake data
store_

After you import data into a new HealthLake data store, the data may not be available for
immediate use. This is to allow time for the data to be ingested into Apache Iceberg
tables. Try again at a later time.

**Issue:**
_How do I connect search results in Athena to other AWS
services?_

When sharing your search results from Athena with other AWS services, issues can
occur when you use `json_extract[1]` as part of a SQL search query. To fix
this issue, you must update to `CATVAR`.

You might encounter this issue when trying to **Create** save
results, a **Table** (static), or a **View**
(dynamic).

# Importing FHIR data with AWS HealthLake

After creating a HealthLake data store, the next step is to import files from an Amazon Simple Storage Service (S3)
bucket. You can start a FHIR import job using the AWS Management Console, AWS CLI, or AWS SDKs. Use native
AWS HealthLake actions to start, describe, and list FHIR import jobs.

###### Important

HealthLake supports the [FHIR R4
specification](https://hl7.org/fhir/R4/index.html "https://hl7.org/fhir/R4/index.html") for health care data exchange. If needed, you can work with an [AWS HealthLake Partner](https://aws.amazon.com/healthlake/partners/ "https://aws.amazon.com/healthlake/partners/") to convert your health
data to FHIR R4 format prior to import.

When starting a FHIR import job, you specify an Amazon S3 bucket input location, an Amazon S3 bucket
output location (for job processing results), an IAM role that grants HealthLake access to your
Amazon S3 buckets, and a customer owned or AWS owned AWS Key Management Service key. For more information, see [Setting up permissions for import
jobs](getting-started-setting-up.md#setting-up-import-permissions "getting-started-setting-up.md#setting-up-import-permissions").

###### Note

You can queue import jobs. The asynchronous import jobs are
processed in a FIFO (First In First Out) manner. You can queue jobs the same way you start
import jobs. If one is in progress, it will simply queue up. You can create, read,
update, or delete FHIR resources while an import job is in progress.

HealthLake generates a `manifest.json` file for each FHIR import job. The
file describes both the successes and failures of a FHIR import job. HealthLake outputs the
`manifest.json` file to the Amazon S3 bucket specified when starting a FHIR
import job. Log files are organized into two folders, named `SUCCESS` and
`FAILURE`. Use the `manifest.json` file as the first
step in troubleshooting a failed import job, as it provides details on each file.

```
{
    "inputDataConfig": {
        "s3Uri": "s3://`amzn-s3-demo-source-bucket`/healthlake-input/invalidInput/"
    },
    "outputDataConfig": {
        "s3Uri": "s3://`amzn-s3-demo-logging-bucket`/32839038a2f47f17c2fe0f53f0c3a0ba-FHIR_IMPORT-19dd7bb7bcc8ee12a09bf6d322744a3d/",
        "encryptionKeyID": "arn:aws:kms:us-west-2:123456789012:key/fbbbfee3-20b3-42a5-a99d-c48c655ed545"
    },
    "successOutput": {
        "successOutputS3Uri": "s3://`amzn-s3-demo-logging-bucket`/32839038a2f47f17c2fe0f53f0c3a0ba-FHIR_IMPORT-19dd7bb7bcc8ee12a09bf6d322744a3d/SUCCESS/"
    },
    "failureOutput": {
        "failureOutputS3Uri": "s3://`amzn-s3-demo-logging-bucket`/32839038a2f47f17c2fe0f53f0c3a0ba-FHIR_IMPORT-19dd7bb7bcc8ee12a09bf6d322744a3d/FAILURE/"
    },
    "numberOfScannedFiles": 1,
    "numberOfFilesImported": 1,
    "sizeOfScannedFilesInMB": 0.023627,
    "sizeOfDataImportedSuccessfullyInMB": 0.011232,
    "numberOfResourcesScanned": 9,
    "numberOfResourcesImportedSuccessfully": 4,
    "numberOfResourcesWithCustomerError": 5,
    "numberOfResourcesWithServerError": 0
}

```

###### Configuring validation level for imports

When starting a FHIR import job, you can optionally specify a `ValidationLevel`
to apply to each resource. AWS HealthLake currently supports the following validation levels:

- `strict`: Resources are validated according to the profile element of
  the resource, or the R4 specification if no profile is present. This is the default validation
  level for AWS HealthLake.
- `structure-only`: Resources are validated against R4, ignoring any
  referenced profiles.
- `minimal`: Resources are validated minimally, ignoring certain R4
  rules. Resources that fail structure checks required for search/analytics will be updated to
  include a warning for audit.
  When importing using the `minimal` validation level, additional log files
  may be generated in a folder named `SUCCESS_WITH_SEARCH_VALIDATION_FAILURES`.
  Resources within the log files of this folder were ingested into your datastore despite failing
  search related validation checks. This implies certain aspects of your FHIR resource were invalid
  according to FHIR, and malformed fields may not be searchable. These resources will have an
  `extension` appended to them describing said failure.

###### Topics

- [Starting an import job](importing-fhir-data-start.md "importing-fhir-data-start.md")
- [Getting import job
  properties](importing-fhir-data-describe.md "importing-fhir-data-describe.md")
- [Listing import jobs](importing-fhir-data-list.md "importing-fhir-data-list.md")

# Understanding import jobs

After creating a [data store](getting-started-concepts.md#concept-data-store "getting-started-concepts.md#concept-data-store") in AWS HealthImaging, you must
import your medical imaging data from your Amazon S3 input bucket into your data store to create [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"). You can use the AWS Management Console, AWS CLI, and AWS SDKs
to start, describe, and list import jobs.

When you import your DICOM P10 data to an AWS HealthImaging data store, the service attempts to
automatically organize instances according to the DICOM hierarchy of Study UID, Series UID, Instance
UID, based on the [metadata elements](understanding-image-sets.md "understanding-image-sets.md"). Imported data will be made primary if the
[metadata elements](understanding-image-sets.md "understanding-image-sets.md") of the imported data do not conflict with existing primary
[image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") in the data store. If the metadata elements of newly imported DICOM P10 data conflict with existing
primary [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"), the new data will be added to non-primary [image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"). When data imports create non-primary
[image sets](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"), AWS HealthImaging emits an EventBridge Event with `isPrimary: False`, and the record written to the
`success.ndjson` will also have `isPrimary: False` within the `importResponse` object.

When you import data, HealthImaging does the following:

- If instances comprising a DICOM series are imported in one import job and the instances do
  not conflict with instances already in the data store, then all instances are organized into one
  primary [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set").
- If the instances comprising a DICOM series are imported in two or more import jobs and the
  instances don't conflict with instances already in the data store, then all instances are
  organized as one Primary [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set").
- If an instance is imported more than once, the latest version will overwrite any older version
  stored within a primary [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set"), and the version number of the primary [image set](getting-started-concepts.md#concept-image-set "getting-started-concepts.md#concept-image-set") will be incremented.
  You can update the instances in the primary with the steps described in [Updating Image set metadata](update-image-set-metadata.md "update-image-set-metadata.md").

During import, binary values in private tags (with VR types OB, OD, OF, OL, OV, OW, UN) that exceed 1MB in size are stored
separately from the metadata. When retrieving metadata for these instances using `GetDICOMInstanceMetadata` or `GetDICOMSeriesMetadata`,
these large binary values are replaced with BulkDataURIs, and the actual binary data can be retrieved using the `GetDICOMBulkdata` API.

Keep the following points in mind when importing your medical imaging files from Amazon S3 into an
HealthImaging data store:

- The instances corresponding to a DICOM Series will be automatically combined in a single image set,
  denoted primary.
- You can import DICOM P10 data in one import job, or multiple import jobs, and the service
  will organize the instances into primary image sets that correspond to DICOM Series
- Length constraints apply to specific DICOM elements during import. To ensure a successful
  import job, verify that your medical imaging data does not exceed the length constraints. For
  more information, see [DICOM element constraints](dicom-element-constraints.md "dicom-element-constraints.md").
- A pixel data verification check is performed at the beginning of import jobs. For more
  information, see [Pixel data verification](pixel-data-verification.md "pixel-data-verification.md").
- There are endpoints, quotas, and throttling limits associated with HealthImaging import actions.
  For more information, see [Endpoints and quotas](endpoints-quotas.md "endpoints-quotas.md") and [Throttling limits](throttling-limits.md "throttling-limits.md").
- For each import job, processing results are stored at the `outputS3Uri`
  location. The processing results are organized as a `job-output-manifest.json` file
  and `SUCCESS` and `FAILURE` folders.

###### Note

You can include up to 10,000 nested folders for a single import job.

    + The `job-output-manifest.json` file contains `jobSummary` output
     and additional details about the processed data. The following example shows output from a
     `job-output-manifest.json` file.



    ```
    {
    "jobSummary": {
    "jobId": "09876543210987654321098765432109",
            "datastoreId": "12345678901234567890123456789012",
            "inputS3Uri": "s3://medical-imaging-dicom-input/dicom_input/",
            "outputS3Uri": "s3://medical-imaging-output/job_output/12345678901234567890123456789012-DicomImport-09876543210987654321098765432109/",
            "successOutputS3Uri": "s3://medical-imaging-output/job_output/12345678901234567890123456789012-DicomImport-09876543210987654321098765432109/SUCCESS/",
            "failureOutputS3Uri": "s3://medical-imaging-output/job_output/12345678901234567890123456789012-DicomImport-09876543210987654321098765432109/FAILURE/",
            "warningsOutputS3Uri": "s3://medical-imaging-output/job_output/12345678901234567890123456789012-DicomImport-09876543210987654321098765432109/WARNING/",
            "numberOfScannedFiles": 5,
            "numberOfImportedFiles": 3,
            "numberOfFilesWithCustomerError": 2,
            "numberOfFilesWithServerError": 0,
            "numberOfGeneratedImageSets": 2,
            "imageSetsSummary": [{
    "imageSetId": "12345612345612345678907890789012",
                    "numberOfMatchedSOPInstances": 2
                },
                {
    "imageSetId": "12345612345612345678917891789012",
                    "numberOfMatchedSOPInstances": 1
                }
            ]
        }
    }

    ```
    + The `SUCCESS` folder holds the `success.ndjson` file containing
     results of all imaging files that imported successfully. The following example shows output
     from a `success.ndjson` file.



    ```
    {"inputFile":"dicomInputFolder/1.3.51.5145.5142.20010109.1105620.1.0.1.dcm","importResponse":{"imageSetId":"12345612345612345678907890789012", "isPrimary": True}}
    {"inputFile":"dicomInputFolder/1.3.51.5145.5142.20010109.1105630.1.0.1.dcm","importResponse":{"imageSetId":"12345612345612345678917891789012", "isPrimary": True}}

    ```
    + The `FAILURE` folder holds the `failure.ndjson` file containing
     results of all imaging files that did not import successfully. The following example shows output
     from a `failure.ndjson` file.



    ```
    {"inputFile":"dicom_input/invalidDicomFile1.dcm","exception":{"exceptionType":"ValidationException","message":"DICOM attribute TransferSyntaxUID does not exist"}}
    {"inputFile":"dicom_input/invalidDicomFile2.dcm","exception":{"exceptionType":"ValidationException","message":"DICOM attributes does not exist"}}

    ```
    + The `WARNING` folder holds the `warning.ndjson` file containing
     results of all imaging files that imported successfully but with warnings. The following example shows output
     from a `warning.ndjson` file.



    ```
    {"inputFile":"dicom_input/warningDicomFile1.dcm","importResponse":{"imageSetId":"12345612345612345678907890789012","imageSetVersion":1,"isPrimary":true,"warnings":[{"warning_reason_code":45330,"type":"InvalidOffsetTable","message":"The file was imported but contains an invalid offset table, may see issues when retrieving certain frames."}]}}

    ```

- Import jobs are retained in the list of jobs for 90 days and then archived.

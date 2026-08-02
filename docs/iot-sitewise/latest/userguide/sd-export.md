# Exporting your curated data

You use the `CreateDatasetExportJob` API to export processed data from a
Scenario Discovery dataset to an Amazon S3 destination. Before you can export, you must configure
an S3 bucket policy that grants the AWS IoT SiteWise service principal write access to your target bucket.
You then submit the export job by specifying the destination S3 URI and the processing input
source, and the service writes the exported data asynchronously. For the full API reference,
bucket policy, request payloads, and invocation examples, see
[CreateDatasetExportJob for Scenario Discovery](sd-export-job.md "sd-export-job.md").

## SDK experience

Use _Using this service with an AWS SDK_ and
_Installing or updating to the latest version of the AWS CLI_.

The SDK binaries are available at the AWS SDK downloads page.

## API documentation

The full API reference is provided in the AWS IoT SiteWise API Reference. Additional examples and
usage patterns are covered in the appendices.



# Exporting your curated data
<a name="sd-export"></a>

You use the `CreateDatasetExportJob` API to export processed data from a Scenario Discovery dataset to an Amazon S3 destination. Before you can export, you must configure an S3 bucket policy that grants the AWS IoT SiteWise service principal write access to your target bucket. You then submit the export job by specifying the destination S3 URI and the processing input source, and the service writes the exported data asynchronously. For the full API reference, bucket policy, request payloads, and invocation examples, see [CreateDatasetExportJob for Scenario Discovery](sd-export-job.md).

## SDK experience
<a name="sd-sdk-experience"></a>

Use *Using this service with an AWS SDK* and *Installing or updating to the latest version of the AWS CLI*.

The SDK binaries are available at the AWS SDK downloads page.

## API documentation
<a name="sd-api-documentation"></a>

The full API reference is provided in the AWS IoT SiteWise API Reference. Additional examples and usage patterns are covered in the appendices.
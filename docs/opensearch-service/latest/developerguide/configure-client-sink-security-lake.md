# Using an OpenSearch Ingestion

pipeline with Amazon Security Lake as a sink

Use the Amazon S3 sink plugin in OpenSearch Ingestion to send data from any supported source
to Amazon Security Lake. Security Lake collects and stores security data from AWS, on-premises
environments, and SaaS providers in a dedicated data lake.

To configure your pipeline to write log data to Security Lake, use the preconfigured
**Firewall Traffic logs** blueprint. The blueprint includes a
default configuration for retrieving raw security logs or other data stored in an
Amazon S3 bucket, processing the records, and normalizing them. It then maps the data to
Open Cybersecurity Schema Framework (OCSF) and sends the transformed OCSF-compliant
data to Security Lake.

The pipeline has the following metadata attributes:

- `bucket_name`: The name of the Amazon S3 bucket created by Security Lake for
  storing security data.
- `path_prefix`: The custom source name defined in the Security Lake IAM
  role policy.
- `region`: The AWS Region where the Security Lake S3 bucket is
  located.
- `accountID`: The AWS account ID in which Security Lake is
  enabled.
- `sts_role_arn`: The ARN of the IAM role intended for use with
  Security Lake.

## Prerequisites

Before you create a pipeline to send data to Security Lake, perform the following
steps:

- **Enable and configure Amazon Security Lake**: Set up
  Amazon Security Lake to centralize security data from various sources. For
  instructions, see [Enabling Security Lake using the console](../../../security-lake/latest/userguide/get-started-console.md "../../../security-lake/latest/userguide/get-started-console.md").

When you select a source, choose **Ingest specific AWS
sources** and select one or more log and event sources that
you want to ingest.

- **Set up permissions**: Configure the
  pipeline role with the required permissions to write data to Security Lake. For
  more information, see [Pipeline role](pipeline-security-overview.md#pipeline-security-sink "pipeline-security-overview.md#pipeline-security-sink").

### Create the

pipeline

Use the preconfigured Security Lake blueprint to create the pipeline. For more
information, see [Using blueprints to create a pipeline](pipeline-blueprint.md "pipeline-blueprint.md").

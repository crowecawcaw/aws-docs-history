# Data sources

CloudWatch pipelines supports three types of data:

- **AWS services logs through CloudWatch Logs**

When an AWS service source is selected, CloudWatch pipelines intercepts logs ingested into
CloudWatch Logs for processing. Processing of vended AWS service data occurs at
the Log Source and Source Type level through CloudWatch Logs data sources. To get
started enable logging of vended logs for the supported AWS services using the
service’s console and then select the data source and type in the CloudWatch pipelines creation
wizard. For more information about CloudWatch Logs data sources, see [Data
source discovery and management](../logs/data-source-discovery-management.md "../logs/data-source-discovery-management.md").

AWS vended sources provide _native integration_ with AWS
services for automatic data collection. For a list of data source names and types,
see [Supported AWS services for data sources](../logs/supported-aws-services-data-sources.md "../logs/supported-aws-services-data-sources.md").

- **Third-party log data through integration**

Third-party log data can extend monitoring capabilities to support identity and
access management as well as endpoint and network security. CloudWatch pipelines manages collection
of data from third-party platforms through either direct API integration or an S3
bucket integration. For more details, see [Third-party data sources integration](third-party-integration-setup.md "third-party-integration-setup.md"). For a list of data source names
and types, see [Supported third-party sources for data sources](../logs/supported-third-party-sources-data-sources.md "../logs/supported-third-party-sources-data-sources.md").

- **Custom logs through CloudWatch Logs or S3 buckets**

CloudWatch pipelines can process custom Logs stored in CloudWatch Logs or S3 buckets. Custom
sources accommodate unique organizational requirements:

    + **Application-specific logs** – Custom
     application telemetry from EC2 instances with specialized logging
     formats
    + **File-based ingestion** – S3-based
     log files from legacy systems or batch processing workflows
    + **Serverless integration** – Lambda
     function logs and custom serverless application telemetry

For more details, see [Custom log data from CloudWatch Logs or an Amazon S3 bucket](ingestion-custom-data-sources.md "ingestion-custom-data-sources.md").

###### Topics

- [Third-party data sources integration](third-party-integration-setup.md "third-party-integration-setup.md")
- [Custom log data from CloudWatch Logs or an Amazon S3 bucket](ingestion-custom-data-sources.md "ingestion-custom-data-sources.md")
- [Configuring Custom S3 Bucket Sources](configuring-custom-s3-bucket-sources.md "configuring-custom-s3-bucket-sources.md")
- [AWS service logs from CloudWatch Logs](aws-service-logs-from-cwl.md "aws-service-logs-from-cwl.md")

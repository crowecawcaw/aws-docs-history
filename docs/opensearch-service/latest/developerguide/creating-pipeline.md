# Creating Amazon OpenSearch Ingestion pipelines

A _pipeline_ is the mechanism that Amazon OpenSearch Ingestion uses to move
data from its _source_ (where the data comes from) to its
_sink_ (where the data goes). In OpenSearch Ingestion, the sink will
always be a single Amazon OpenSearch Service domain, while the source of your data could be clients like
Amazon S3, Fluent Bit, or the OpenTelemetry Collector.

For more information, see [Pipelines](https://opensearch.org/docs/latest/clients/data-prepper/pipelines/ "https://opensearch.org/docs/latest/clients/data-prepper/pipelines/") in the OpenSearch documentation.

###### Topics

- [Prerequisites and required IAM
  role](#manage-pipeline-prerequisites "#manage-pipeline-prerequisites")
- [Required IAM permissions](#create-pipeline-permissions "#create-pipeline-permissions")
- [Specifying the pipeline version](#pipeline-version "#pipeline-version")
- [Specifying the ingestion path](#pipeline-path "#pipeline-path")
- [Creating pipelines](#create-pipeline "#create-pipeline")
- [Tracking the status of pipeline creation](#get-pipeline-progress "#get-pipeline-progress")
- [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md")

## Prerequisites and required IAM

role

To create an OpenSearch Ingestion pipeline, you must have the following resources:

- An IAM role, called the _pipeline role_, that
  OpenSearch Ingestion assumes in order to write to the sink. You can create this role
  ahead of time, or you can have OpenSearch Ingestion create it automatically while
  you're creating the pipeline.
- An OpenSearch Service domain or OpenSearch Serverless collection to act as the sink. If you're writing to a
  domain, it must be running OpenSearch 1.0 or later, or Elasticsearch 7.4 or
  later. The sink must have an access policy that grants the appropriate
  permissions to your IAM pipeline role.

For instructions to create these resources, see the following topics:

- [Granting Amazon OpenSearch Ingestion pipelines access to
  domains](pipeline-domain-access.md "pipeline-domain-access.md")
- [Granting Amazon OpenSearch Ingestion pipelines access
  to collections](pipeline-collection-access.md "pipeline-collection-access.md")

###### Note

If you're writing to a domain that uses fine-grained access control, there are
extra steps you need to complete. See [Map the pipeline role (only for
domains that use fine-grained access control)](pipeline-domain-access.md#pipeline-access-domain-fgac "pipeline-domain-access.md#pipeline-access-domain-fgac").

## Required IAM permissions

OpenSearch Ingestion uses the following IAM permissions for creating pipelines:

- `osis:CreatePipeline` – Create a pipeline.
- `osis:ValidatePipeline` – Check whether a pipeline
  configuration is valid.
- `iam:CreateRole` and `iam:AttachPolicy` – Have
  OpenSearch Ingestion automatically create the pipeline role for you.
- `iam:PassRole` – Pass the pipeline role to OpenSearch Ingestion
  so that it can write data to the domain. This permission must be on the [pipeline role resource](pipeline-domain-access.md#pipeline-access-configure "pipeline-domain-access.md#pipeline-access-configure"), or simply
  `*` if you plan to use different roles in each pipeline.

For example, the following policy grants permission to create a pipeline:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Resource":"*",
 "Action":[
 "osis:CreatePipeline",
 "osis:ListPipelineBlueprints",
 "osis:ValidatePipeline"
 ]
 },
 {
 "Resource":[
 "arn:aws:iam::`111122223333`:role/`pipeline-role`"
 ],
 "Effect":"Allow",
 "Action":[
 "iam:CreateRole",
 "iam:AttachRolePolicy",
 "iam:PassRole"
 ]
 }
 ]
}`

```

OpenSearch Ingestion also includes a permission called `osis:Ingest`, which is
required in order to send signed requests to the pipeline using [Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). For more information, see [Creating an ingestion role](configure-client.md#configure-client-auth "configure-client.md#configure-client-auth").

###### Note

In addition, the first user to create a pipeline in an account must have
permissions for the `iam:CreateServiceLinkedRole` action. For more
information, see [pipeline role
resource](pipeline-security.md#pipeline-vpc-slr "pipeline-security.md#pipeline-vpc-slr").

For more information about each permission, see [Actions, resources, and condition keys for OpenSearch Ingestion](../../../service-authorization/latest/reference/list_opensearchingestionservice.md "../../../service-authorization/latest/reference/list_opensearchingestionservice.md") in the
_Service Authorization Reference_.

## Specifying the pipeline version

When you create a pipeline using the configuration editor, you must specify the major
[version of
Data Prepper](https://github.com/opensearch-project/data-prepper/releases "https://github.com/opensearch-project/data-prepper/releases") that the pipeline will run. To specify the version, include the
`version` option in your pipeline configuration:

```
`version: "2"`
log-pipeline:
  source:
    ...
```

When you choose **Create**, OpenSearch Ingestion determines the latest
available _minor_ version of the major version that you specify, and
provisions the pipeline with that version. For example, if you specify `version:
 "2"`, and the latest supported version of Data Prepper is 2.1.1,
OpenSearch Ingestion provisions your pipeline with version 2.1.1. We don't publicly display
the minor version that your pipeline is running.

In order to upgrade your pipeline when a new major version of Data Prepper is
available, edit the pipeline configuration and specify the new version. You can't
downgrade a pipeline to an earlier version.

###### Note

OpenSearch Ingestion doesn't immediately support new versions of Data Prepper as soon
as they're released. There will be some lag between when a new version is publicly
available and when it's supported in OpenSearch Ingestion. In addition, OpenSearch Ingestion
might explicitly not support certain major or minor versions altogether. For a
comprehensive list, see [Supported Data Prepper versions](ingestion.md#ingestion-supported-versions "ingestion.md#ingestion-supported-versions").

Any time you make a change to your pipeline that initiates a blue/green deployment,
OpenSearch Ingestion can upgrade it to the latest minor version of the major version that's
currently configured for the pipeline. For more information, see [Blue/green deployments for pipeline updates](update-pipeline.md#pipeline-bg "update-pipeline.md#pipeline-bg"). OpenSearch Ingestion can't change the major version of your
pipeline unless you explicitly update the `version` option within the
pipeline configuration.

## Specifying the ingestion path

For pull-based sources like [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/") and [OTel metrics](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/"), OpenSearch Ingestion requires the additional `path`
option in your source configuration. The path is a string such as
`/log/ingest`, which represents the URI path for ingestion. This path
defines the URI that you use to send data to the pipeline.

For example, say you specify the following path for a pipeline with an HTTP
source:

![Input field for specifying the path for ingestion, with an example path entered.](/images/opensearch-service/latest/developerguide/images/ingestion-path.png)

When you [ingest data](configure-client.md "configure-client.md") into the pipeline, you
must specify the following endpoint in your client configuration:
`https://`pipeline-name-abc123`.`us-west-2`.osis.amazonaws.com/`my`/`test_path``.

The path must start with a slash (/) and can contain the special characters '-', '\_',
'.', and '/', as well as the `${pipelineName}` placeholder. If you use
`${pipelineName}` (such as `/${pipelineName}/test_path`),
OpenSearch Ingestion replaces the variable with the name of the associated
sub-pipeline.

## Creating pipelines

This section describes how to create OpenSearch Ingestion pipelines using the OpenSearch Service console
and the AWS CLI.

To create a pipeline, sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home "https://console.aws.amazon.com/aos/home") and choose **Create
pipeline**.

Either select a blank pipeline, or choose a configuration blueprint.
Blueprints include a preconfigured pipeline for a variety of common use cases.
For more information, see [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md").

Choose **Select blueprint**.

#### Configure source

1. If you're starting from a blank pipeline, select a source from the
   dropdown menu. Available sources might include other AWS services,
   OpenTelemetry, or HTTP. For more information, see [Integrating Amazon OpenSearch Ingestion pipelines with other
   services and applications](configure-client.md "configure-client.md").
2. Depending on which source you choose, configure additional settings
   for the source. For example, to use Amazon S3 as a source, you must specify
   the URL of the Amazon SQS queue from the pipeline receives messagess. For a
   list of supported source plugins and links to their documentation, see
   [Supported plugins and options for
   Amazon OpenSearch Ingestion pipelines](pipeline-config-reference.md "pipeline-config-reference.md").
3. For some sources, you must specify **Source network
   options**. Choose either **VPC access** or
   **Public access**. If you choose **Public
   access**, skip to the next step. If you choose
   **VPC access**, configure the following
   settings:

| Setting                    | Description                                                                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Endpoint management**    | Choose whether you want to create your virtual<br>private cloud (VPC) endpoints yourself, or have<br>OpenSearch Ingestion create them for you. Endpoint<br>management defaults to endpoints managed by<br>OpenSearch Ingestion. |
| **VPC**                    | Choose the ID of the VPC that you want to use. The<br>VPC and pipeline must be in the same<br>AWS Region.                                                                                                                       |
| **Subnets**                | Choose one or more subnets. OpenSearch Service will place a VPC<br>endpoint and \*elastic network<br>interfaces<br>• in the subnets.                                                                                            |
| **Security groups**        | Choose one or more VPC security groups that allow<br>your required application to reach the<br>OpenSearch Ingestion pipeline on the ports (80 or 443)<br>and protocols (HTTP or HTTPs) exposed by the<br>pipeline.              |
| **VPC attachment options** | If your source is a self-managed endpoint, attach<br>your pipeline to a VPC. Choose one of the default<br>CIDR options provided, or use a custom CIDR.                                                                          |

For more information, see [Configuring VPC access for Amazon OpenSearch Ingestion
pipelines](pipeline-security.md "pipeline-security.md"). 4. Choose **Next**.

#### Configure processor

Add one or more processors to your pipeline. Processors are
components within a sub-pipeline that let you filter, transform, and enrich
events before publishing records to the domain or collection sink. For a
list of supported processors and links to their documentation, see [Supported plugins and options for
Amazon OpenSearch Ingestion pipelines](pipeline-config-reference.md "pipeline-config-reference.md").

You can choose **Actions** and add the
following:

- **Conditional routing** – Routes
  events to different sinks based on specific conditions. For
  more information, see [Conditional routing](https://opensearch.org/docs/latest/data-prepper/pipelines/pipelines/#conditional-routing "https://opensearch.org/docs/latest/data-prepper/pipelines/pipelines/#conditional-routing").
- **Sub-pipeline** – Each
  sub-pipeline is a combination of a single source, zero or
  more processors, and a single sink. Only one sub-pipeline
  can have an external source. All others must have sources
  that are other sub-pipelines within the overall pipeline
  configuration. A single pipeline configuration can contain
  1-10 sub-pipelines.

Choose **Next**.

#### Configure sink

Select the destination where the pipeline publishes records. Every
sub-pipeline must contain at least one sink. You can add a maximum of 10
sinks to a pipeline.

For OpenSearch sinks, configure the following fields:

| Setting                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Network policy name**(Serverless<br>sinks only) | If you selected an OpenSearch Serverless collection, enter a<br>**Network policy name**.<br>OpenSearch Ingestion either creates the policy if it doesn't<br>exist, or updates it with a rule that grants access to<br>the VPC endpoint connecting the pipeline and the<br>collection. For more information, see [Granting Amazon OpenSearch Ingestion pipelines access<br>to collections](pipeline-collection-access.md "pipeline-collection-access.md").           |
| **Index name**                                    | The name of the index where the pipeline sends data.<br>OpenSearch Ingestion creates this index if it doesn't already<br>exist.                                                                                                                                                                                                                                                                                                                                     |
| **Index mapping options**                         | Choose how the pipeline stores and indexes documents and<br>their fields into the OpenSearch sink. If you select<br>**Dynamic mapping**, OpenSearch adds<br>fields automatically when you index a document. If you<br>select **Customize mapping**, enter an<br>index mapping template. For more information, see [Index templates](https://opensearch.org/docs/latest/im-plugin/index-templates/ "https://opensearch.org/docs/latest/im-plugin/index-templates/"). |
| **Enable DLQ**                                    | Configure an Amazon S3 dead-letter queue (DLQ) for the<br>pipeline. For more information, see [Dead-letter queues](osis-features-overview.md#osis-features-dlq "osis-features-overview.md#osis-features-dlq").                                                                                                                                                                                                                                                      |
| **Additional settings**                           | Configure advanced options for the OpenSearch sink. For<br>more information, see [Configuration options](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/#configuration-options "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/#configuration-options") in the Data Prepper<br>documentation.                                                                                   |

To add an Amazon S3 sink, choose **Add sink** and
**Amazon S3**. For more information, see [Amazon S3 as a destination](configure-client-s3.md#s3-destination "configure-client-s3.md#s3-destination").

Choose **Next**.

#### Configure pipeline

Configure the following additional pipeline settings:

| Setting                    | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pipeline name**          | A unique name for the pipeline.                                                                                                                                                                                                                                                                                                                                                                                       |
| **Persistent buffer**      | A persistent buffer stores your data in a disk-based<br>buffer across multiple Availability Zones. For more<br>information, see [Persistent buffering](osis-features-overview.md#persistent-buffering "osis-features-overview.md#persistent-buffering").<br>If you enable persistent buffering, select the<br>AWS Key Management Service key to encrypt the buffer data.                                              |
| **Pipeline capacity**      | The minimum and maximum pipeline capacity, in Ingestion<br>OpenSearch Compute Units (OCUs). For more information,<br>see [Scaling pipelines in Amazon OpenSearch Ingestion](ingestion-scaling.md "ingestion-scaling.md").                                                                                                                                                                                             |
| **Pipeline role**          | The IAM role that provides the required permissions for<br>the pipeline to write to the sink and read from<br>pull-based sources. You can create the role yourself, or<br>have OpenSearch Ingestion create it for you based on your<br>selected use case.<br>For more information, see [Setting up roles and users in<br>Amazon OpenSearch Ingestion](pipeline-security-overview.md "pipeline-security-overview.md"). |
| **Tags**                   | Add one or more tags to your pipeline. For more<br>information, see [Tagging Amazon OpenSearch Ingestion pipelines](tag-pipeline.md "tag-pipeline.md").                                                                                                                                                                                                                                                               |
| **Log publishing options** | Enable pipeline log publishing to Amazon CloudWatch Logs. We recommend<br>that you enable log publishing so that you can more easily<br>troubleshoot pipeline issues. For more information, see<br>[Monitoring pipeline logs](monitoring-pipeline-logs.md "monitoring-pipeline-logs.md").                                                                                                                             |

Choose **Next**., then review your pipeline
configuration and choose **Create pipeline**.

OpenSearch Ingestion runs an asynchronous process to build the pipeline. Once the
pipeline status is `Active`, you can start ingesting data.

The [create-pipeline](../../../cli/latest/reference/osis/create-pipeline.md "../../../cli/latest/reference/osis/create-pipeline.md")
command accepts the pipeline configuration as a string or within a .yaml or
.json file. If you provide the configuration as a string, each new line must be
escaped with `\n`. For example, `"log-pipeline:\n source:\n
 http:\n processor:\n - grok:\n ...`

The following sample command creates a pipeline with the following
configuration:

- Minimum of 4 Ingestion OCUs, maximum of 10 Ingestion OCUs
- Provisioned within a virtual private cloud (VPC)
- Log publishing enabled

```
aws osis create-pipeline \
  --pipeline-name `my-pipeline` \
  --min-units 4 \
  --max-units 10 \
  --log-publishing-options  IsLoggingEnabled=true,CloudWatchLogDestination={LogGroup="`MyLogGroup`"} \
  --vpc-options SecurityGroupIds={`sg-12345678`,`sg-9012345`},SubnetIds=`subnet-1212234567834asdf` \
  --pipeline-configuration-body "file://`pipeline-config.yaml`" \
  --pipeline-role-arn  arn:aws:iam::`1234456789012`:role/`pipeline-role`
```

OpenSearch Ingestion runs an asynchronous process to build the pipeline. Once the
pipeline status is `Active`, you can start ingesting data. To check the
status of the pipeline, use the [GetPipeline](../APIReference/API_osis_GetPipeline.md "../APIReference/API_osis_GetPipeline.md") command.

To create an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the
[CreatePipeline](../APIReference/API_osis_CreatePipeline.md "../APIReference/API_osis_CreatePipeline.md") operation.

After your pipeline is successfully created, you can configure your client and
start ingesting data into your OpenSearch Service domain. For more information, see [Integrating Amazon OpenSearch Ingestion pipelines with other
services and applications](configure-client.md "configure-client.md").

## Tracking the status of pipeline creation

You can track the status of a pipeline as OpenSearch Ingestion provisions it and prepares
it to ingest data.

After you initially create a pipeline, it goes through multiple stages as
OpenSearch Ingestion prepares it to ingest data. To view the various stages of
pipeline creation, choose the pipeline name to see its **Pipeline
settings** page. Under **Status**, choose
**View details**.

A pipeline goes through the following stages before it's available to ingest
data:

- **Validation** – Validating pipeline
  configuration. When this stage is complete, all validations have
  succeeded.
- **Create environment** – Preparing
  and provisioning resources. When this stage is complete, the new
  pipeline environment has been created.
- **Deploy pipeline** – Deploying
  the pipeline. When this stage is complete, the pipeline has been
  successfully deployed.
- **Check pipeline health** –
  Checking the health of the pipeline. When this stage is complete, all
  health checks have passed.
- **Enable traffic** – Enabling the
  pipeline to ingest data. When this stage is complete, you can start
  ingesting data into the pipeline.
  Use the [get-pipeline-change-progress](../../../cli/latest/reference/osis/get-pipeline-change-progress.md "../../../cli/latest/reference/osis/get-pipeline-change-progress.md") command to check the status of a
  pipeline. The following AWS CLI request checks the status of a pipeline named
  `my-pipeline`:

```
aws osis get-pipeline-change-progress \
    --pipeline-name `my-pipeline`
```

**Response**:

```
{
   "ChangeProgressStatuses": {
      "ChangeProgressStages": [
         {
            "Description": "Validating pipeline configuration",
            "LastUpdated": 1.671055851E9,
            "Name": "VALIDATION",
            "Status": "PENDING"
         }
      ],
      "StartTime": 1.671055851E9,
      "Status": "PROCESSING",
      "TotalNumberOfStages": 5
   }
}
```

To track the status of pipeline creation using the OpenSearch Ingestion API, call
the [GetPipelineChangeProgress](../APIReference/API_osis_GetPipelineChangeProgress.md "../APIReference/API_osis_GetPipelineChangeProgress.md") operation.

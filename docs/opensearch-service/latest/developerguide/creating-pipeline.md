

# Creating Amazon OpenSearch Ingestion pipelines
<a name="creating-pipeline"></a>

A *pipeline* is the mechanism that Amazon OpenSearch Ingestion uses to move data from its *source* (where the data comes from) to its *sink* (where the data goes). In OpenSearch Ingestion, the sink will always be a single Amazon OpenSearch Service domain, while the source of your data could be clients like Amazon S3, Fluent Bit, or the OpenTelemetry Collector.

For more information, see [Pipelines](https://opensearch.org/docs/latest/clients/data-prepper/pipelines/) in the OpenSearch documentation.

**Topics**
+ [Prerequisites and required IAM role](#manage-pipeline-prerequisites)
+ [Required IAM permissions](#create-pipeline-permissions)
+ [Specifying the pipeline version](#pipeline-version)
+ [Specifying the ingestion path](#pipeline-path)
+ [Creating pipelines](#create-pipeline)
+ [Tracking the status of pipeline creation](#get-pipeline-progress)
+ [Working with blueprints](pipeline-blueprint.md)

## Prerequisites and required IAM role
<a name="manage-pipeline-prerequisites"></a>

To create an OpenSearch Ingestion pipeline, you must have the following resources:
+ An IAM role, called the *pipeline role*, that OpenSearch Ingestion assumes in order to write to the sink. You can create this role ahead of time, or you can have OpenSearch Ingestion create it automatically while you're creating the pipeline.
+ An OpenSearch Service domain or OpenSearch Serverless collection to act as the sink. If you're writing to a domain, it must be running OpenSearch 1.0 or later, or Elasticsearch 7.4 or later. The sink must have an access policy that grants the appropriate permissions to your IAM pipeline role.

For instructions to create these resources, see the following topics:
+ [Granting Amazon OpenSearch Ingestion pipelines access to domains](pipeline-domain-access.md)
+ [Granting Amazon OpenSearch Ingestion pipelines access to collections](pipeline-collection-access.md)

**Note**  
If you're writing to a domain that uses fine-grained access control, there are extra steps you need to complete. See [Map the pipeline role (only for domains that use fine-grained access control)](pipeline-domain-access.md#pipeline-access-domain-fgac).

## Required IAM permissions
<a name="create-pipeline-permissions"></a>

OpenSearch Ingestion uses the following IAM permissions for creating pipelines:
+ `osis:CreatePipeline` – Create a pipeline.
+ `osis:ValidatePipeline` – Check whether a pipeline configuration is valid.
+ `iam:CreateRole` and `iam:AttachPolicy` – Have OpenSearch Ingestion automatically create the pipeline role for you.
+ `iam:PassRole` – Pass the pipeline role to OpenSearch Ingestion so that it can write data to the domain. This permission must be on the [pipeline role resource](pipeline-domain-access.md#pipeline-access-configure), or simply `*` if you plan to use different roles in each pipeline.

For example, the following policy grants permission to create a pipeline:

------
#### [ JSON ]

****  

```
{
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
            "arn:aws:iam::{{111122223333}}:role/{{pipeline-role}}"
         ],
         "Effect":"Allow",
         "Action":[
            "iam:CreateRole",
            "iam:AttachRolePolicy",
            "iam:PassRole"
         ]
      }
   ]
}
```

------

OpenSearch Ingestion also includes a permission called `osis:Ingest`, which is required in order to send signed requests to the pipeline using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). For more information, see [Creating an ingestion role](configure-client.md#configure-client-auth).

**Note**  
In addition, the first user to create a pipeline in an account must have permissions for the `iam:CreateServiceLinkedRole` action. For more information, see [pipeline role resource](pipeline-security.md#pipeline-vpc-slr).

For more information about each permission, see [Actions, resources, and condition keys for OpenSearch Ingestion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_opensearchingestionservice.html) in the *Service Authorization Reference*.

## Specifying the pipeline version
<a name="pipeline-version"></a>

When you create a pipeline using the configuration editor, you must specify the major [version of Data Prepper](https://github.com/opensearch-project/data-prepper/releases) that the pipeline will run. To specify the version, include the `version` option in your pipeline configuration:

```
{{version: "2"}}
log-pipeline:
  source:
    ...
```

When you choose **Create**, OpenSearch Ingestion determines the latest available *minor* version of the major version that you specify, and provisions the pipeline with that version. For example, if you specify `version: "2"`, and the latest supported version of Data Prepper is 2.1.1, OpenSearch Ingestion provisions your pipeline with version 2.1.1. We don't publicly display the minor version that your pipeline is running.

In order to upgrade your pipeline when a new major version of Data Prepper is available, edit the pipeline configuration and specify the new version. You can't downgrade a pipeline to an earlier version.

**Note**  
OpenSearch Ingestion doesn't immediately support new versions of Data Prepper as soon as they're released. There will be some lag between when a new version is publicly available and when it's supported in OpenSearch Ingestion. In addition, OpenSearch Ingestion might explicitly not support certain major or minor versions altogether. For a comprehensive list, see [Supported Data Prepper versions](ingestion.md#ingestion-supported-versions).

Any time you make a change to your pipeline that initiates a blue/green deployment, OpenSearch Ingestion can upgrade it to the latest minor version of the major version that's currently configured for the pipeline. For more information, see [Blue/green deployments for pipeline updates](update-pipeline.md#pipeline-bg). OpenSearch Ingestion can't change the major version of your pipeline unless you explicitly update the `version` option within the pipeline configuration.

## Specifying the ingestion path
<a name="pipeline-path"></a>

For pull-based sources like [OTel trace](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-trace/) and [OTel metrics](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/otel-metrics-source/), OpenSearch Ingestion requires the additional `path` option in your source configuration. The path is a string such as `/log/ingest`, which represents the URI path for ingestion. This path defines the URI that you use to send data to the pipeline. 

For example, say you specify the following path for a pipeline with an HTTP source:

![Path field containing the example value /my/test_path.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/ingestion-path.png)


When you [ingest data](configure-client.md) into the pipeline, you must specify the following endpoint in your client configuration: `https://{{pipeline-name-abc123}}.{{us-west-2}}.osis.amazonaws.com/{{my}}/{{test_path}}`.

The path must start with a slash (/) and can contain the special characters '-', '\_', '.', and '/', as well as the `${pipelineName}` placeholder. If you use `${pipelineName}` (such as `/${pipelineName}/test_path`), OpenSearch Ingestion replaces the variable with the name of the associated sub-pipeline.

## Creating pipelines
<a name="create-pipeline"></a>

This section describes how to create OpenSearch Ingestion pipelines using the OpenSearch Service console and the AWS CLI.

### Console
<a name="create-pipeline-console"></a>

To create a pipeline, sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines) and choose **Create pipeline**. 

Either select a blank pipeline, or choose a configuration blueprint. Blueprints include a preconfigured pipeline for a variety of common use cases. For more information, see [Working with blueprints](pipeline-blueprint.md).

Choose **Select blueprint**.

#### Configure source
<a name="create-pipeline-console-source"></a>

1. If you're starting from a blank pipeline, select a source from the dropdown menu. Available sources might include other AWS services, OpenTelemetry, or HTTP. For more information, see [Integrating Amazon OpenSearch Ingestion pipelines with other services and applications](configure-client.md).

1. Depending on which source you choose, configure additional settings for the source. For example, to use Amazon S3 as a source, you must specify the URL of the Amazon SQS queue from the pipeline receives messagess. For a list of supported source plugins and links to their documentation, see [Supported plugins and options for Amazon OpenSearch Ingestion pipelines](pipeline-config-reference.md).

1. For some sources, you must specify **Source network options**. Choose either **VPC access** or **Public access**. If you choose **Public access**, skip to the next step. If you choose **VPC access**, configure the following settings:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html)

   For more information, see [Configuring VPC access for Amazon OpenSearch Ingestion pipelines](pipeline-security.md).

1. Choose **Next**.

#### Configure processor
<a name="create-pipeline-console-processor"></a>

Add one or more processors to your pipeline. Processors are components within a sub-pipeline that let you filter, transform, and enrich events before publishing records to the domain or collection sink. For a list of supported processors and links to their documentation, see [Supported plugins and options for Amazon OpenSearch Ingestion pipelines](pipeline-config-reference.md).

You can choose **Actions** and add the following:
+ **Conditional routing** – Routes events to different sinks based on specific conditions. For more information, see [Conditional routing](https://opensearch.org/docs/latest/data-prepper/pipelines/pipelines/#conditional-routing).
+ **Sub-pipeline** – Each sub-pipeline is a combination of a single source, zero or more processors, and a single sink. Only one sub-pipeline can have an external source. All others must have sources that are other sub-pipelines within the overall pipeline configuration. A single pipeline configuration can contain 1-10 sub-pipelines.

Choose **Next**.

#### Configure sink
<a name="create-pipeline-console-sink"></a>

Select the destination where the pipeline publishes records. Every sub-pipeline must contain at least one sink. You can add a maximum of 10 sinks to a pipeline.

For OpenSearch sinks, configure the following fields:


| Setting | Description | 
| --- | --- | 
| Network policy name(Serverless sinks only) | If you selected an OpenSearch Serverless collection, enter a **Network policy name**. OpenSearch Ingestion either creates the policy if it doesn't exist, or updates it with a rule that grants access to the VPC endpoint connecting the pipeline and the collection. For more information, see [Granting Amazon OpenSearch Ingestion pipelines access to collections](pipeline-collection-access.md). | 
| Index name | The name of the index where the pipeline sends data. OpenSearch Ingestion creates this index if it doesn't already exist. | 
| Index mapping options | Choose how the pipeline stores and indexes documents and their fields into the OpenSearch sink. If you select **Dynamic mapping**, OpenSearch adds fields automatically when you index a document. If you select **Customize mapping**, enter an index mapping template. For more information, see [Index templates](https://opensearch.org/docs/latest/im-plugin/index-templates/). | 
| Enable DLQ | Configure an Amazon S3 dead-letter queue (DLQ) for the pipeline. For more information, see [Dead-letter queues](osis-features-overview.md#osis-features-dlq). | 
| Additional settings | Configure advanced options for the OpenSearch sink. For more information, see [Configuration options](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sinks/opensearch/#configuration-options) in the Data Prepper documentation. | 

To add an Amazon S3 sink, choose **Add sink** and **Amazon S3**. For more information, see [Amazon S3 as a destination](configure-client-s3.md#s3-destination).

Choose **Next**.

#### Configure pipeline
<a name="create-console-pipeline"></a>

Configure the following additional pipeline settings:


| Setting | Description | 
| --- | --- | 
| Pipeline name | A unique name for the pipeline. | 
| Persistent buffer | A persistent buffer stores your data in a disk-based buffer across multiple Availability Zones. For more information, see [Persistent buffering](osis-features-overview.md#persistent-buffering). <br />If you enable persistent buffering, select the AWS Key Management Service key to encrypt the buffer data.  | 
| Pipeline capacity | The minimum and maximum pipeline capacity, in Ingestion OpenSearch Compute Units (OCUs). For more information, see [Scaling pipelines in Amazon OpenSearch Ingestion](ingestion-scaling.md). | 
| Pipeline role | The IAM role that provides the required permissions for the pipeline to write to the sink and read from pull-based sources. You can create the role yourself, or have OpenSearch Ingestion create it for you based on your selected use case. <br />For more information, see [Setting up roles and users in Amazon OpenSearch Ingestion](pipeline-security-overview.md). | 
| Tags | Add one or more tags to your pipeline. For more information, see [Tagging Amazon OpenSearch Ingestion pipelines](tag-pipeline.md). | 
| Log publishing options | Enable pipeline log publishing to Amazon CloudWatch Logs. We recommend that you enable log publishing so that you can more easily troubleshoot pipeline issues. For more information, see [Monitoring pipeline logs](monitoring-pipeline-logs.md). | 

Choose **Next**., then review your pipeline configuration and choose **Create pipeline**.

OpenSearch Ingestion runs an asynchronous process to build the pipeline. Once the pipeline status is `Active`, you can start ingesting data.

### AWS CLI
<a name="create-pipeline-cli"></a>

The [create-pipeline](https://docs.aws.amazon.com/cli/latest/reference/osis/create-pipeline.html) command accepts the pipeline configuration as a string or within a .yaml or .json file. If you provide the configuration as a string, each new line must be escaped with `\n`. For example, `"log-pipeline:\n source:\n http:\n processor:\n - grok:\n ...`

The following sample command creates a pipeline with the following configuration:
+ Minimum of 4 Ingestion OCUs, maximum of 10 Ingestion OCUs
+ Provisioned within a virtual private cloud (VPC)
+ Log publishing enabled

```
aws osis create-pipeline \
  --pipeline-name {{my-pipeline}} \
  --min-units 4 \
  --max-units 10 \
  --log-publishing-options  IsLoggingEnabled=true,CloudWatchLogDestination={LogGroup="{{MyLogGroup}}"} \
  --vpc-options SecurityGroupIds={{{sg-12345678}},{{sg-9012345}}},SubnetIds={{subnet-1212234567834asdf}} \
  --pipeline-configuration-body "file://{{pipeline-config.yaml}}" \
  --pipeline-role-arn  arn:aws:iam::{{1234456789012}}:role/{{pipeline-role}}
```

OpenSearch Ingestion runs an asynchronous process to build the pipeline. Once the pipeline status is `Active`, you can start ingesting data. To check the status of the pipeline, use the [GetPipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipeline.html) command.

### OpenSearch Ingestion API
<a name="create-pipeline-api"></a>

To create an OpenSearch Ingestion pipeline using the OpenSearch Ingestion API, call the [CreatePipeline](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_CreatePipeline.html) operation.

After your pipeline is successfully created, you can configure your client and start ingesting data into your OpenSearch Service domain. For more information, see [Integrating Amazon OpenSearch Ingestion pipelines with other services and applications](configure-client.md).

## Tracking the status of pipeline creation
<a name="get-pipeline-progress"></a>

You can track the status of a pipeline as OpenSearch Ingestion provisions it and prepares it to ingest data.

### Console
<a name="get-pipeline-progress-console"></a>

After you initially create a pipeline, it goes through multiple stages as OpenSearch Ingestion prepares it to ingest data. To view the various stages of pipeline creation, choose the pipeline name to see its **Pipeline settings** page. Under **Status**, choose **View details**.

A pipeline goes through the following stages before it's available to ingest data:
+ **Validation** – Validating pipeline configuration. When this stage is complete, all validations have succeeded.
+ **Create environment** – Preparing and provisioning resources. When this stage is complete, the new pipeline environment has been created.
+ **Deploy pipeline** – Deploying the pipeline. When this stage is complete, the pipeline has been successfully deployed.
+ **Check pipeline health** – Checking the health of the pipeline. When this stage is complete, all health checks have passed.
+ **Enable traffic** – Enabling the pipeline to ingest data. When this stage is complete, you can start ingesting data into the pipeline.

### CLI
<a name="get-pipeline-progress-cli"></a>

Use the [get-pipeline-change-progress](https://docs.aws.amazon.com/cli/latest/reference/osis/get-pipeline-change-progress.html) command to check the status of a pipeline. The following AWS CLI request checks the status of a pipeline named `my-pipeline`:

```
aws osis get-pipeline-change-progress \
    --pipeline-name {{my-pipeline}}
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

### OpenSearch Ingestion API
<a name="get-pipeline-progress-api"></a>

To track the status of pipeline creation using the OpenSearch Ingestion API, call the [GetPipelineChangeProgress](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipelineChangeProgress.html) operation.
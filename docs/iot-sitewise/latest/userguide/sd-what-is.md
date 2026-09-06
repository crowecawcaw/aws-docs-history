

# Welcome to Scenario Discovery
<a name="sd-what-is"></a>

## What is Scenario Discovery?
<a name="sd-what-is-overview"></a>

Scenario Discovery is an agentic data curation solution within AWS IoT SiteWise that enables you to find the right scenarios in your data faster, with greater confidence in what you have and what you're missing, so you can build more holistic datasets to train and test your autonomous functions in shorter time.

![Scenario Discovery data flow and architecture](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image1.png)


If you develop autonomous vehicles, warehouse robotics, or last-mile delivery systems, you generate petabytes of sensor data, yet your perception engineers likely spend much of their time on data preparation instead of model development. Scenario Discovery enables you to discover previously unfindable scenarios by finding the most critical and relevant data from petabytes of operational data, helping to reduce scenario discovery from days to minutes.

## Key benefits
<a name="sd-key-benefits"></a>

Scenario Discovery provides the following benefits:
+ Find edge cases in hours, not weeks.
+ Build balanced, diverse training datasets using AI-driven curation.
+ Reduce manual labeling effort with pre-enriched semantic embeddings.
+ Integrate with downstream simulation tools through standard export formats.

## Key capabilities
<a name="sd-key-capabilities"></a>

Scenario Discovery offers the following capabilities:
+ **Curate datasets with natural language** – Describe the scenarios you need in plain language and receive a training-ready dataset, distilled from petabytes of multimodal data.
+ **Correlate data across modalities** – Query your annotations, telemetry, and video through a single time-aligned index so you can pinpoint exactly when and where events occur.
+ **Find scenarios quickly** – Search across video content, telemetry signals, and annotation metadata using natural language or structured queries to surface the scenarios you need.
+ **Build custom processing pipelines** – Package your data transformation, enrichment, and multi-step processing tasks as containers, then orchestrate them into repeatable workflows.
+ **Connect your existing toolchain** – Move data bidirectionally between your upstream collection systems and downstream training, labeling, and simulation tools without manual reformatting.
+ **Govern and reuse your datasets** – Organize data into source and curated datasets with full lineage traceability, governed access, and cross-team reusability from collection to training-ready outputs.

## Who should use this guide
<a name="sd-who-should-use"></a>

Use this guide if you fill one of the following roles:
+ **Data Wrangler** – You own the data pipeline from ingestion through enrichment.
+ **Data Curator / Perception Engineer** – You search and discover scenarios and assemble curated datasets.
+ **Workspace Admin / Data Lifecycle Manager** – You manage environments, datasets, lineage, and governance.

## Prerequisites
<a name="sd-prerequisites"></a>

Before you use Scenario Discovery, ensure you have the following:
+ A modern web browser (Chrome, Firefox, or Edge, latest version)
+ You must be allowlisted by AWS before proceeding.
+ An AWS account with SiteWise access: Your account is the highest level of organization in the system. At the root, your account contains all AWS resources you use. At the account level, you can also implement other AWS concepts such as Organizations. For the purposes of this discussion, your account includes all your data, its storage, and the actions you perform on that data. Your account is where all billing usage for your AWS resources rolls up to.
+ AWS Identity Center (IAM Identity Center) must be enabled in your organization. Scenario Discovery uses Identity Center for workforce authentication. For more information, visit [https://aws.amazon.com/iam/identity-center/](https://aws.amazon.com/iam/identity-center/).
+ To use IAM Identity Center with Scenario Discovery, the IAM Identity Center instance must be present in the same region and account as where you are using Scenario Discovery.
+ If the AWS account using Scenario Discovery is part of an organization, they must have the ability to list IAM Identity Center instances and create IAM Identity Center applications.
+ In addition to the IAM Identity Center instance by the managing account, there needs to be an IAM Identity Center instance in the region where Scenario Discovery is running.
+ If you do have an AWS Identity Center instance, replicate the Identity Center region into the required region.
+ Supported data formats: Prepare your data as Parquet for Telemetry, MP4 (H.264) for video, and OpenLABEL for Annotations.

**Important**  
Scenario Discovery is currently available in `us-east-1` and `eu-west-1`. Your S3 bucket and workspace must reside in the same Region.


# Regions and limits for SageMaker AI Data Preparation

## Supported Regions
<a name="ai-data-preparation-regions-limits-regions"></a>

SageMaker AI Data Preparation is available in the following AWS Regions:
+ US East (N. Virginia) – `us-east-1`
+ US West (Oregon) – `us-west-2`

Human-in-the-loop annotation is available in those Regions and in the following additional Regions:
+ Europe (Ireland) – `eu-west-1`
+ Asia Pacific (Tokyo) – `ap-northeast-1`

## Limits for all capabilities
<a name="ai-data-preparation-regions-limits-shared"></a>

The following limits apply to every SageMaker AI Data Preparation job.


| Item | Limit | 
| --- | --- | 
| Amazon S3 locations | All input and output locations must be in the same AWS Region as the job. | 
| Datasets per hub | 2,000. When a hub is full, jobs fail with ResourceLimitExceeded. Delete datasets that you no longer need. | 
| Supported data types for SageMaker AI Data Preparation | With SageMaker AI Data Preparation, you can work with text data. You cannot use image, audio, or video data. | 

## Service quotas
<a name="ai-data-preparation-regions-limits-quotas"></a>

Each capability that runs jobs has its own quota for the number of jobs that can run at the same time. These quotas apply per account in each Region, and all of them are adjustable.


| Name in Service Quotas | Applies to | Default | Adjustable | 
| --- | --- | --- | --- | 
| Maximum number of concurrent synthetic data generation jobs | [Synthetic data generation](ai-data-preparation-sdg.md#ai-data-preparation-sdg-limits) jobs, including [auto-labeling](ai-data-preparation-autolabel.md#ai-data-preparation-autolabel-limits) jobs | 3 | Yes | 
| Maximum number of concurrent data quality evaluation jobs | [Data quality evaluation](ai-data-preparation-dq.md#ai-data-preparation-dq-limits) jobs | 3 | Yes | 
| Maximum number of concurrent data transformation jobs | [Data transformation](ai-data-preparation-dt.md#ai-data-preparation-dt-limits) jobs | 3 | Yes | 

Human-in-the-loop annotation has no SageMaker AI Data Preparation quotas. Its labeling space runs in Studio, so Studio quotas apply. For more information about sizing its Label Studio application, see [Limits and quotas](ai-data-preparation-hil.md#ai-data-preparation-hil-limits) in [Human-in-the-loop annotation](ai-data-preparation-hil.md).

To run more jobs at the same time, request an increase to the matching quota in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). Jobs that invoke Amazon Bedrock models also depend on the Amazon Bedrock quotas in your account. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) in the *Amazon Bedrock User Guide*.

## Limits for each capability
<a name="ai-data-preparation-regions-limits-by-primitive"></a>

For limits that apply to a single capability, see the limits section of its page:
+ [Synthetic data generation](ai-data-preparation-sdg.md#ai-data-preparation-sdg-limits)
+ [Data quality evaluation](ai-data-preparation-dq.md#ai-data-preparation-dq-limits)
+ [Data transformation](ai-data-preparation-dt.md#ai-data-preparation-dt-limits)
+ [Auto-labeling](ai-data-preparation-autolabel.md#ai-data-preparation-autolabel-limits)
+ [Human-in-the-loop annotation](ai-data-preparation-hil.md#ai-data-preparation-hil-limits)
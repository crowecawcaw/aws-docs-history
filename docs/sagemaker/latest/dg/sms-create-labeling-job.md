

# Create a Labeling Job
<a name="sms-create-labeling-job"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

You can create a labeling job in the Amazon SageMaker AI console and by using an AWS SDK in your preferred language to run `CreateLabelingJob`. After a labeling job has been created, you can track worker metrics (for private workforces) and your labeling job status using [CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-monitor-cloud-watch.html).

Before you create a labeling job it is recommended that you review the following pages, as applicable:
+ You can specify your input data using an automatic data setup in the console, or an input manifest file in either the console or when using `CreateLabelingJob` API. For automated data setup, see [Automate data setup for labeling jobs](sms-console-create-manifest-file.md). To learn how to create an input manifest file, see [Input manifest files](sms-input-data-input-manifest.md).
+ Review labeling job input data quotas: [Input Data Quotas](input-data-limits.md).

After you have chosen your task type, use the topics on this page to learn how to create a labeling job.

If you are a new Ground Truth user, we recommend that you start by walking through the demo in [Getting started: Create a bounding box labeling job with Ground Truth](sms-getting-started.md).

**Important**  
Ground Truth requires all S3 buckets that contain labeling job input image data to have a CORS policy attached. To learn more, see [CORS Requirement for Input Image Data](sms-cors-update.md).

**Topics**
+ [Built-in Task Types](sms-task-types.md)
+ [Create instruction pages](sms-creating-instruction-pages.md)
+ [Create a Labeling Job (Console)](sms-create-labeling-job-console.md)
+ [Create a Labeling Job (API)](sms-create-labeling-job-api.md)
+ [Create a streaming labeling job](sms-streaming-create-job.md)
+ [Labeling category configuration file with label category and frame attributes reference](sms-label-cat-config-attributes.md)
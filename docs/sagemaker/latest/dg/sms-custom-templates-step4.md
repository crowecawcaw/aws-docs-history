# Create a custom workflow using the

API

When you have created your custom UI template (Step 2) and processing Lambda functions
(Step 3), you should place the template in an Amazon S3 bucket with a file name format of:
`<FileName>.liquid.html`. Use the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") action to configure your task. You'll use the
location of a custom template ([Creating a custom worker task template](sms-custom-templates-step2.md "sms-custom-templates-step2.md")) stored in a
``<filename>`.liquid.html`file on S3
 as the value for the`UiTemplateS3Uri` field in the [`UiConfig`](../APIReference/API_UiConfig.md "../APIReference/API_UiConfig.md") object within the [`HumanTaskConfig`](../APIReference/API_HumanTaskConfig.md "../APIReference/API_HumanTaskConfig.md") object.

For the AWS Lambda tasks described in [Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md "sms-custom-templates-step3.md"), the post-annotation task's ARN will be used as the value for the `AnnotationConsolidationLambdaArn` field, and the pre-annotation task will be used as the value for the `PreHumanTaskLambdaArn.`

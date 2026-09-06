

# Create a custom workflow using the API
<a name="sms-custom-templates-step4"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

When you have created your custom UI template (Step 2) and processing Lambda functions (Step 3), you should place the template in an Amazon S3 bucket with a file name format of: `<FileName>.liquid.html`. Use the [`CreateLabelingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html) action to configure your task. You'll use the location of a custom template ([Creating a custom worker task template](sms-custom-templates-step2.md)) stored in a `{{<filename>}}.liquid.html` file on S3 as the value for the `UiTemplateS3Uri` field in the [`UiConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UiConfig.html) object within the [`HumanTaskConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanTaskConfig.html) object.

For the AWS Lambda tasks described in [Processing data in a custom labeling workflow with AWS Lambda](sms-custom-templates-step3.md), the post-annotation task's ARN will be used as the value for the `AnnotationConsolidationLambdaArn` field, and the pre-annotation task will be used as the value for the `PreHumanTaskLambdaArn.` 


# Create a 3D point cloud semantic segmentation labeling job
<a name="sms-point-cloud-semantic-segmentation-create-labeling-job"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

You can create a 3D point cloud labeling job using the SageMaker AI console or API operation, [`CreateLabelingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html). To create a labeling job for this task type you need the following: 
+ A single-frame input manifest file. To learn how to create this type of manifest file, see [Create a Point Cloud Frame Input Manifest File](sms-point-cloud-single-frame-input-data.md). If you are a new user of Ground Truth 3D point cloud labeling modalities, we recommend that you review [Accepted Raw 3D Data Formats](sms-point-cloud-raw-data-types.md). 
+ A work team from a private or vendor workforce. You cannot use Amazon Mechanical Turk workers for 3D point cloud labeling jobs. To learn how to create workforces and work teams, see [Workforces](sms-workforce-management.md).
+ A label category configuration file. For more information, see [Labeling category configuration file with label category and frame attributes reference](sms-label-cat-config-attributes.md). 

Additionally, make sure that you have reviewed and satisfied the [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md). 

Use one of the following sections to learn how to create a labeling job using the console or an API. 

## Create a labeling job (console)
<a name="sms-point-cloud-semantic-segmentation-console"></a>

You can follow the instructions [Create a Labeling Job (Console)](sms-create-labeling-job-console.md) in order to learn how to create a 3D point cloud semantic segmentation labeling job in the SageMaker AI console. While you are creating your labeling job, be aware of the following: 
+ Your input manifest file must be a single-frame manifest file. For more information, see [Create a Point Cloud Frame Input Manifest File](sms-point-cloud-single-frame-input-data.md). 
+ Automated data labeling and annotation consolidation are not supported for 3D point cloud labeling tasks. 
+ 3D point cloud semantic segmentation labeling jobs can take multiple hours to complete. You can specify a longer time limit for these labeling jobs when you select your work team (up to 7 days, or 604800 seconds). 

## Create a labeling job (API)
<a name="sms-point-cloud-semantic-segmentation-api"></a>

This section covers details you need to know when you create a labeling job using the SageMaker API operation `CreateLabelingJob`. This API defines this operation for all AWS SDKs. To see a list of language-specific SDKs supported for this operation, review the **See Also** section of [`CreateLabelingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html). 

The page, [Create a Labeling Job (API)](sms-create-labeling-job-api.md), provides an overview of the `CreateLabelingJob` operation. Follow these instructions and do the following while you configure your request: 
+ You must enter an ARN for `HumanTaskUiArn`. Use `arn:aws:sagemaker:{{<region>}}:394669845002:human-task-ui/PointCloudSemanticSegmentation`. Replace `{{<region>}}` with the AWS Region you are creating the labeling job in. 

  There should not be an entry for the `UiTemplateS3Uri` parameter. 
+ Your [`LabelAttributeName`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html#sagemaker-CreateLabelingJob-request-LabelAttributeName) must end in `-ref`. For example, `{{ss-labels}}-ref`. 
+ Your input manifest file must be a single-frame manifest file. For more information, see [Create a Point Cloud Frame Input Manifest File](sms-point-cloud-single-frame-input-data.md). 
+ You specify your labels and worker instructions in a label category configuration file. See [Labeling category configuration file with label category and frame attributes reference](sms-label-cat-config-attributes.md) to learn how to create this file. 
+ You need to provide a pre-defined ARNs for the pre-annotation and post-annotation (ACS) Lambda functions. These ARNs are specific to the AWS Region you use to create your labeling job. 
  + To find the pre-annotation Lambda ARN, refer to [`PreHumanTaskLambdaArn`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HumanTaskConfig.html#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn). Use the Region you are creating your labeling job in to find the correct ARN. For example, if you are creating your labeling job in us-east-1, the ARN will be `arn:aws:lambda:us-east-1:432418664414:function:PRE-3DPointCloudSemanticSegmentation`. 
  + To find the post-annotation Lambda ARN, refer to [`AnnotationConsolidationLambdaArn`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AnnotationConsolidationConfig.html#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn). Use the Region you are creating your labeling job in to find the correct ARN. For example, if you are creating your labeling job in us-east-1, the ARN will be `arn:aws:lambda:us-east-1:432418664414:function:ACS-3DPointCloudSemanticSegmentation`. 
+ The number of workers specified in `NumberOfHumanWorkersPerDataObject` should be `1`. 
+ Automated data labeling is not supported for 3D point cloud labeling jobs. You should not specify values for parameters in `[LabelingJobAlgorithmsConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html#sagemaker-CreateLabelingJob-request-LabelingJobAlgorithmsConfig)`. 
+ 3D point cloud semantic segmentation labeling jobs can take multiple hours to complete. You can specify a longer time limit for these labeling jobs in `TaskTimeLimitInSeconds` (up to 7 days, or 604800 seconds). 
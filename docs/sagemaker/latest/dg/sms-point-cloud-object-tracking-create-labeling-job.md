# Create a 3D point

cloud object tracking labeling job

You can create a 3D point cloud labeling job using the SageMaker AI console or API operation,
[`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md"). To create a labeling job for this task type you
need the following:

- A sequence input manifest file. To learn how to create this type of manifest
  file, see [Create a Point Cloud Sequence
  Input Manifest](sms-point-cloud-multi-frame-input-data.md "sms-point-cloud-multi-frame-input-data.md"). If you are a new user
  of Ground Truth 3D point cloud labeling modalities, we recommend that you review [Accepted Raw 3D Data Formats](sms-point-cloud-raw-data-types.md "sms-point-cloud-raw-data-types.md").
- A work team from a private or vendor workforce. You cannot use Amazon Mechanical Turk for 3D
  point cloud labeling jobs. To learn how to create workforces and work teams, see
  [Workforces](sms-workforce-management.md "sms-workforce-management.md").
  Additionally, make sure that you have reviewed and satisfied the [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md "sms-security-permission.md").

To learn how to create a labeling job using the console or an API, see the following
sections.

## Create

a labeling job (console)

You can follow the instructions [Create a Labeling Job (Console)](sms-create-labeling-job-console.md "sms-create-labeling-job-console.md") in order to learn how to create a
3D point cloud object tracking labeling job in the SageMaker AI console. While you are
creating your labeling job, be aware of the following:

- Your input manifest file must be a sequence manifest file. For more
  information, see [Create a Point Cloud Sequence
  Input Manifest](sms-point-cloud-multi-frame-input-data.md "sms-point-cloud-multi-frame-input-data.md").
- Optionally, you can provide label category attributes. Workers can assign
  one or more of these attributes to annotations to provide more information
  about that object. For example, you might want to use the attribute
  _occluded_ to have workers identify when an
  object is partially obstructed.
- Automated data labeling and annotation consolidation are not supported for
  3D point cloud labeling tasks.
- 3D point cloud object tracking labeling jobs can take multiple hours to
  complete. You can specify a longer time limit for these labeling jobs when
  you select your work team (up to 7 days, or 604800 seconds).

## Create a

labeling job (API)

This section covers details you need to know when you create a labeling job using
the SageMaker API operation `CreateLabelingJob`. This API defines this
operation for all AWS SDKs. To see a list of language-specific SDKs supported for
this operation, review the **See Also** section of [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md").

[Create a Labeling Job (API)](sms-create-labeling-job-api.md "sms-create-labeling-job-api.md") provides an overview of the
`CreateLabelingJob` operation. Follow these instructions and do the
following while you configure your request:

- You must enter an ARN for `HumanTaskUiArn`. Use
  `arn:aws:sagemaker:`<region>`:394669845002:human-task-ui/PointCloudObjectTracking`.
  Replace `<region>` with the AWS
  Region you are creating the labeling job in.

There should not be an entry for the `UiTemplateS3Uri`
parameter.

- Your [`LabelAttributeName`](../APIReference/API_CreateLabelingJob.md#sagemaker-CreateLabelingJob-request-LabelAttributeName "../APIReference/API_CreateLabelingJob.md#sagemaker-CreateLabelingJob-request-LabelAttributeName") must end in `-ref`. For
  example, ``ot-labels`-ref`.
- Your input manifest file must be a point cloud frame sequence manifest
  file. For more information, see [Create a Point Cloud Sequence
  Input Manifest](sms-point-cloud-multi-frame-input-data.md "sms-point-cloud-multi-frame-input-data.md").
- You specify your labels, label category and frame attributes, and worker
  instructions in a label category configuration file. For more information,
  see [Labeling category configuration file with
  label category and frame attributes reference](sms-label-cat-config-attributes.md "sms-label-cat-config-attributes.md") to learn how to create
  this file.
- You need to provide pre-defined ARNs for the pre-annotation and
  post-annotation (ACS) Lambda functions. These ARNs are specific to the AWS
  Region you use to create your labeling job.
  - To find the pre-annotation Lambda ARN, refer to [`PreHumanTaskLambdaArn`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn"). Use the Region you are
    creating your labeling job in to find the correct ARN that ends with
    `PRE-3DPointCloudObjectTracking`.
  - To find the post-annotation Lambda ARN, refer to [`AnnotationConsolidationLambdaArn`](../APIReference/API_AnnotationConsolidationConfig.md#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn "../APIReference/API_AnnotationConsolidationConfig.md#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn"). Use the
    Region you are creating your labeling job in to find the correct ARN
    that ends with `ACS-3DPointCloudObjectTracking`.

- The number of workers specified in
  `NumberOfHumanWorkersPerDataObject` should be `1`.
- Automated data labeling is not supported for 3D point cloud labeling jobs.
  You should not specify values for parameters in `LabelingJobAlgorithmsConfig`.
- 3D point cloud object tracking labeling jobs can take multiple hours to
  complete. You can specify a longer time limit for these labeling jobs in
  `TaskTimeLimitInSeconds` (up to 7 days, or 604,800 seconds).

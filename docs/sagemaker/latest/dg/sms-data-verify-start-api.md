# Start a label verification or adjustment job

(API)

Start a label verification or adjustment job by chaining a successfully completed
job or starting a new job from scratch using the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") operation. The procedure is almost the
same as setting up a new labeling job with `CreateLabelingJob`, with a
few modifications. Use the following sections to learn what modifications are
required to chain a labeling job to create an adjustment or verification labeling
job.

When you create an adjustment or verification labeling job using the Ground Truth API,
you _must_ use a different
`LabelAttributeName` than the original labeling job. The original
labeling job is the job used to create the labels you want adjusted or verified.

###### Important

The label category configuration file you identify for an adjustment or
verification job in [`LabelCategoryConfigS3Uri`](../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri "../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri") of
`CreateLabelingJob` must contain the same labels used in the
original labeling job. You can add new labels. For 3D point cloud and video
frame jobs, you can add new label category and frame attributes to the label
category configuration file.

## Bounding Box and Semantic Segmentation

To create a bounding box or semantic segmentation label verification or
adjustment job, use the following guidelines to specify API attributes for the
`CreateLabelingJob` operation.

- Use the [`LabelAttributeName`](../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelAttributeName "../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelAttributeName") parameter to specify
  the output label name that you want to use for verified or adjusted
  labels. You must use a different `LabelAttributeName` than
  the one used for the original labeling job.
- If you are chaining the job, the labels from the previous labeling job to
  be adjusted or verified will be specified in the custom UI template. To
  learn how to create a custom template, see [Create Custom Worker Task Templates](a2i-custom-templates.md "a2i-custom-templates.md").

Identify the location of the UI template in the [`UiTemplateS3Uri`](../APIReference/API_UiConfig.md "../APIReference/API_UiConfig.md") parameter. SageMaker AI provides
widgets that you can use in your custom template to display old labels.
Use the `initial-value` attribute in one of the following
crowd elements to extract the labels that need verification or
adjustment and include them in your task template:

    + [crowd-semantic-segmentation](sms-ui-template-crowd-semantic-segmentation.md "sms-ui-template-crowd-semantic-segmentation.md")—Use this crowd element in your custom UI task template to
     specify semantic segmentation labels that need to be verified or
     adjusted.
    + [crowd-bounding-box](sms-ui-template-crowd-bounding-box.md "sms-ui-template-crowd-bounding-box.md")—Use
     this crowd element in your custom UI task template to specify
     bounding box labels that need to be verified or adjusted.

- The [`LabelCategoryConfigS3Uri`](../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri "../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri") parameter must
  contain the same label categories as the previous labeling job.
- Use the bounding box or semantic segmentation adjustment or
  verification lambda ARNs for [`PreHumanTaskLambdaArn`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn") and [`AnnotationConsolidationLambdaArn`](../APIReference/API_AnnotationConsolidationConfig.md#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn "../APIReference/API_AnnotationConsolidationConfig.md#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn"):
  - For bounding box, the adjustment labeling job lambda function
    ARNs end with `AdjustmentBoundingBox` and the
    verification lambda function ARNs end with
    `VerificationBoundingBox`.
  - For semantic segmentation, the adjustment labeling job lambda
    function ARNs end with
    `AdjustmentSemanticSegmentation` and the
    verification lambda function ARNs end with
    `VerificationSemanticSegmentation`.

## 3D point cloud and video frame

- Use the [`LabelAttributeName`](../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelAttributeName "../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelAttributeName") parameter to specify
  the output label name that you want to use for verified or adjusted
  labels. You must use a different `LabelAttributeName` than
  the one used for the original labeling job.
- You must use the human task UI Amazon Resource Name (ARN)
  (`HumanTaskUiArn`) used for the original labeling job. To
  see supported ARNs, see [`HumanTaskUiArn`](../APIReference/API_UiConfig.md#sagemaker-Type-UiConfig-HumanTaskUiArn "../APIReference/API_UiConfig.md#sagemaker-Type-UiConfig-HumanTaskUiArn").
- In the label category configuration file, you must specify the label
  attribute name ([`LabelAttributeName`](../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelAttributeName "../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelAttributeName")) of the previous
  labeling job that you use to create the adjustment or verification
  labeling job in the `auditLabelAttributeName`
  parameter.
- You specify whether your labeling job is a _verification_ or _adjustment_ labeling job using the
  `editsAllowed` parameter in your label category
  configuration file identified by the [`LabelCategoryConfigS3Uri`](../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri "../APIReference/API_CreateLabelingJob.md#SageMaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri") parameter.

      + For *verification* labeling
       jobs, you must use the `editsAllowed` parameter to
       specify that all labels cannot be modified.
       `editsAllowed` must be set to `"none"`
       in each entry in `labels`. Optionally, you can
       specify whether or not label categories attributes and frame
       attributes can be adjusted by workers.
      + Optionally, for *adjustment*
       labeling jobs, you can use the `editsAllowed`
       parameter to specify labels, label category attributes, and
       frame attributes that can or cannot be modified by workers. If
       you do not use this parameter, all labels, label category
       attributes, and frame attributes will be adjustable.

  To learn more about the `editsAllowed` parameter and
  configuring your label category configuration file, see [Label category configuration file schema](sms-label-cat-config-attributes.md#sms-label-cat-config-attributes-schema "sms-label-cat-config-attributes.md#sms-label-cat-config-attributes-schema").

- Use the 3D point cloud or video frame adjustment lambda ARNs for
  [`PreHumanTaskLambdaArn`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-PreHumanTaskLambdaArn") and [`AnnotationConsolidationLambdaArn`](../APIReference/API_AnnotationConsolidationConfig.md#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn "../APIReference/API_AnnotationConsolidationConfig.md#sagemaker-Type-AnnotationConsolidationConfig-AnnotationConsolidationLambdaArn") for both
  adjustment and verification labeling jobs:
  - For 3D point clouds, the adjustment and verification labeling
    job lambda function ARNs end with
    `Adjustment3DPointCloudSemanticSegmentation`,
    `Adjustment3DPointCloudObjectTracking`, and
    `Adjustment3DPointCloudObjectDetection` for 3D
    point cloud semantic segmentation, object detection, and object
    tracking respectively.
  - For video frames, the adjustment and verification labeling job
    lambda function ARNs end with
    `AdjustmentVideoObjectDetection` and
    `AdjustmentVideoObjectTracking` for video frame
    object detection and object tracking respectively.

Ground Truth stores the output data from a label verification or adjustment job in the S3
bucket that you specified in the [`S3OutputPath`](../APIReference/API_LabelingJobOutputConfig.md#SageMaker-Type-LabelingJobOutputConfig-S3OutputPath "../APIReference/API_LabelingJobOutputConfig.md#SageMaker-Type-LabelingJobOutputConfig-S3OutputPath") parameter of the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") operation. For more information about
the output data from a label verification or adjustment labeling job, see [Label verification and adjustment data in the
output manifest](sms-data-verify-manifest.md "sms-data-verify-manifest.md").

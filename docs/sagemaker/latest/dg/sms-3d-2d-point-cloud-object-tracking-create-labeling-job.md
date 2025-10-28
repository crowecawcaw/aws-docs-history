# Create a

3D-2D point cloud object tracking labeling job

You can create a 3D-2D point cloud labeling job using the SageMaker API operation, [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md"). To create a labeling job for this task type you
need the following:

- A work team from a private or vendor workforce. You cannot use Amazon Mechanical Turk for 3D
  point cloud labeling jobs. To learn how to create workforces and work teams, see
  [Workforces](sms-workforce-management.md "sms-workforce-management.md").
- Add a CORS policy to an S3 bucket that contains input data in the Amazon S3
  console. To set the required CORS headers on the S3 bucket that contains your
  input images in the S3 console, follow the directions detailed in [CORS
  Permission Requirement](sms-cors-update.md "sms-cors-update.md").
- Additionally, make sure that you have reviewed and satisfied the [Assign IAM Permissions to Use Ground Truth](sms-security-permission.md "sms-security-permission.md").
  To learn how to create a labeling job using the API, see the following sections.

## Create a labeling job (API)

This section covers details you need to know when you create a 3D-2D object
tracking labeling job using the SageMaker API operation `CreateLabelingJob`.
This API defines this operation for all AWS SDKs. To see a list of
language-specific SDKs supported for this operation, review the **See
Also** section of [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md").

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
  Input Manifest](sms-point-cloud-multi-frame-input-data.md "sms-point-cloud-multi-frame-input-data.md"). You also need to
  provide a label category configuration file as mentioned above.
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
- 3D-2D object tracking labeling jobs can take multiple hours to complete.
  You can specify a longer time limit for these labeling jobs in
  `TaskTimeLimitInSeconds` (up to 7 days, or 604,800 seconds).

###### Note

After you have successfully created a 3D-2D object tracking job, it shows up
on the console under labeling jobs. The task type for the job is displayed as
**Point Cloud Object Tracking**.

## Input data

format

You can create a 3D-2D object tracking job using the SageMaker API operation, [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md"). To create a labeling job for this task type
you need the following:

- A sequence input manifest file. To learn how to create this type of
  manifest file, see [Create a Point Cloud Sequence
  Input Manifest](sms-point-cloud-multi-frame-input-data.md "sms-point-cloud-multi-frame-input-data.md"). If you are a new
  user of Ground Truth 3D point cloud labeling modalities, we recommend that you
  review [Accepted Raw 3D Data Formats](sms-point-cloud-raw-data-types.md "sms-point-cloud-raw-data-types.md").
- You specify your labels, label category and frame attributes, and worker
  instructions in a label category configuration file. For more information,
  see [Create a
  Labeling Category Configuration File with Label Category and Frame
  Attributes](sms-label-cat-config-attributes.md "sms-label-cat-config-attributes.md") to learn how to create this file. The following is an
  example showing a label category configuration file for creating a 3D-2D
  object tracking job.

```
{
    "document-version": "2020-03-01",
    "categoryGlobalAttributes": [
        {
            "name": "Occlusion",
            "description": "global attribute that applies to all label categories",
            "type": "string",
            "enum":[
                "Partial",
                "Full"
            ]
        }
    ],
    "labels":[
        {
            "label": "Car",
            "attributes": [
                {
                    "name": "Type",
                    "type": "string",
                    "enum": [
                        "SUV",
                        "Sedan"
                    ]
                }
            ]
        },
        {
            "label": "Bus",
            "attributes": [
                {
                    "name": "Size",
                    "type": "string",
                    "enum": [
                        "Large",
                        "Medium",
                        "Small"
                    ]
                }
            ]
        }
    ],
    "instructions": {
        "shortIntroduction": "Draw a tight cuboid around objects after you select a category.",
        "fullIntroduction": "<p>Use this area to add more detailed worker instructions.</p>"
    },
    "annotationType": [
        {
            "type": "BoundingBox"
        },
        {
            "type": "Cuboid"
        }
    ]
}
```

###### Note

You need to provide `BoundingBox` and `Cuboid`
as annotationType in the label category configuration file to create a
3D-2D object tracking job.

# Label verification and adjustment

When the labels on a dataset need to be validated, Amazon SageMaker Ground Truth provides functionality to
have workers verify that labels are correct or to adjust previous labels. These types of
jobs fall into two distinct categories:

- _Label verification_ — Workers indicate
  if the existing labels are correct, or rate their quality, and can add comments to
  explain their reasoning. Workers will not be able to modify or adjust labels.

If you create a 3D point cloud or video frame label adjustment or verification
job, you can choose to make label category attributes (not supported for 3D point
cloud semantic segmentation) and frame attributes editable by workers.

- _Label adjustment_ — Workers adjust prior
  annotations and, if applicable, label category and frame attributes to correct them.
  The following Ground Truth [built-in task types](sms-task-types.md "sms-task-types.md") support adjustment and
  verification labeling jobs:

- Bounding box
- Semantic segmentation
- 3D point cloud object detection, 3D point cloud object tracking, and 3D point
  cloud semantic segmentation
- All video frame object detection and video frame object tracking task types
  — bounding box, polyline, polygon and keypoint

###### Tip

For 3D point cloud and video frame labeling verification jobs, it is recommended that
you add new label category attributes or frame attributes to the labeling job. Workers
can use these attribute to verify individual labels or the entire frame. To learn more
about label category and frame attributes, see [Worker user interface (UI)](sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui "sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui") for 3D point cloud and [Worker user interface (UI)](sms-video-overview.md#sms-video-worker-task-ui "sms-video-overview.md#sms-video-worker-task-ui") for
video frame.

You can start a label verification and adjustment jobs using the SageMaker AI console or the API.

## Cautions and considerations

To get expected behavior when creating a label verification or adjustment job,
carefully verify your input data.

- If you are using image data, verify that your manifest file contains
  hexadecimal RGB color information.
- To save money on processing costs, filter your data to ensure you are not
  including unwanted objects in your labeling job input manifest.
- Add required Amazon S3 permissions to ensure your input data is processed
  correctly.

When you create an adjustment or verification labeling job using the Ground Truth API, you
_must_ use a different
`LabelAttributeName` than the original labeling job.

### Color information requirements for

semantic segmentation jobs

To properly reproduce color information in verification or adjustment tasks, the
tool requires hexadecimal RGB color information in the manifest (for example,
#FFFFFF for white). When you set up a Semantic Segmentation verification or
adjustment job, the tool examines the manifest to determine if this information is
present. If it can't find it,Amazon SageMaker Ground Truth displays an error message and the ends job
setup.

In prior iterations of the Semantic Segmentation tool, category color information
wasn't output in hexadecimal RGB format to the output manifest. That feature was
introduced to the output manifest at the same time the verification and adjustment
workflows were introduced. Therefore, older output manifests aren't compatible with
this new workflow.

### Filter your data before starting the

job

Amazon SageMaker Ground Truth processes all objects in your input manifest. If you have a partially
labeled data set, you might want to create a custom manifest using an [Amazon S3 Select query](../../../AmazonS3/latest/dev/selecting-content-from-objects.md "../../../AmazonS3/latest/dev/selecting-content-from-objects.md") on your input manifest. Unlabeled objects
individually fail, but they don't cause the job to fail, and they might incur
processing costs. Filtering out objects you don't want verified reduces your
costs.

If you create a verification job using the console, you can use the filtering
tools provided there. If you create jobs using the API, make filtering your data
part of your workflow where needed.

###### Topics

- [Requirements to create verification and adjustment
  labeling jobs](sms-data-verify-adjust-prereq.md "sms-data-verify-adjust-prereq.md")
- [Create a label verification job
  (console)](sms-data-verify-start-console.md "sms-data-verify-start-console.md")
- [Create a label adjustment job
  (console)](sms-data-adjust-start-console.md "sms-data-adjust-start-console.md")
- [Start a label verification or adjustment job
  (API)](sms-data-verify-start-api.md "sms-data-verify-start-api.md")
- [Label verification and adjustment data in the
  output manifest](sms-data-verify-manifest.md "sms-data-verify-manifest.md")

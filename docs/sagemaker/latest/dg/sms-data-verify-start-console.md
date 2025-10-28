# Create a label verification job

(console)

Use one of the following sections to create a label verification job for your task
type. Bounding box and semantic segmentation labeling jobs are created by choosing the
**Label verification** task type in the console. To create a
verification job for 3D point cloud and video frame task types, you must choose the same
task type as the original labeling job and choose to display existing labels.

## Create an image label

verification job (console)

Use the following procedure to create a bounding box or semantic segmentation
verification job using the console. This procedure assumes that you have already
created a bounding box or semantic segmentation labeling job and its status is
Complete. This the labeling job that produces the labels you want verified.

###### To create an image label verification job:

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and choose **Labeling
   jobs**.
2. Start a new labeling job by [chaining](sms-reusing-data.md "sms-reusing-data.md") a prior job or start from scratch, specifying an input
   manifest that contains labeled data objects.
3. In the **Task type** pane, select **Label
   verification**.
4. Choose **Next**.
5. In the **Workers** section, choose the type of workforce
   you would like to use. For more details about your workforce options see
   [Workforces](sms-workforce-management.md "sms-workforce-management.md").
6. (Optional) After you've selected your workforce, specify the
   **Task timeout** and **Task expiration
   time**.
7. In the **Existing-labels display options** pane, the
   system shows the available label attribute names in your manifest. Choose
   the label attribute name that identifies the labels that you want workers to
   verify. Ground Truth tries to detect and populate these values by analyzing the
   manifest, but you might need to set the correct value.
8. Use the instructions areas of the tool designer to provide context about
   what the previous labelers were asked to do and what the current verifiers
   need to check.

You can add new labels that workers choose from to verify labels. For
example, you can ask workers to verify the image quality, and provide the
labels _Clear_ and _Blurry_. Workers will also have the option to add a comment
to explain their selection. 9. Choose **See preview** to check that the tool is
displaying the prior labels correctly and presents the label verification
task clearly. 10. Select **Create**. This will create and start your
labeling job.

## Create a point cloud or video frame label

verification job (console)

Use the following procedure to create a 3D point cloud or video frame verification job
using the console. This procedure assumes that you have already created a labeling job
using the task type that produces the types of labels you want to be verified and its
status is Complete.

###### To create an image label verification job:

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and choose **Labeling
   jobs**.
2. Start a new labeling job by [chaining](sms-reusing-data.md "sms-reusing-data.md") a
   prior job or start from scratch, specifying an input manifest that contains
   labeled data objects.
3. In the **Task type** pane, select the same task type as the
   labeling job that you chained. For example, if the original labeling job was a
   video frame object detection keypoint labeling job, select that task type.
4. Choose **Next**.
5. In the **Workers** section, choose the type of workforce you
   would like to use. For more details about your workforce options see [Workforces](sms-workforce-management.md "sms-workforce-management.md").
6. (Optional) After you've selected your workforce, specify the
   **Task timeout** and **Task expiration
   time**.
7. Toggle on the switch next to **Display existing
   labels**.
8. Select **Verification**.
9. For **Label attribute name**, choose the name from your
   manifest that corresponds to the labels that you want to display for
   verification. You will only see label attribute names for labels that match
   the task type you selected on the previous screen. Ground Truth tries to detect and
   populate these values by analyzing the manifest, but you might need to set
   the correct value.
10. Use the instructions areas of the tool designer to provide context about
    what the previous labelers were asked to do and what the current verifiers
    need to check.

You cannot modify or add new labels. You can remove, modify and add new
label category attributes or frame attributes. It is recommended that you
add new label category attributes or frame attributes to the labeling job.
Workers can use these attribute to verify individual labels or the entire
frame.

By default, preexisting label category attributes and frame attributes
will not be editable by workers. If you want to make a label category or
frame attribute editable, select the **Allow workers to edit this
attribute** check box for that attribute.

To learn more about label category and frame attributes, see [Worker user interface (UI)](sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui "sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui") for 3D point cloud and
[Worker user interface (UI)](sms-video-overview.md#sms-video-worker-task-ui "sms-video-overview.md#sms-video-worker-task-ui") for video frame. 11. Choose **See preview** to check that the tool is displaying
the prior labels correctly and presents the label verification task
clearly. 12. Select **Create**. This will create and start your labeling
job.

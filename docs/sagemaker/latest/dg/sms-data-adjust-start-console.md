

# Create a label adjustment job (console)
<a name="sms-data-adjust-start-console"></a>

**Note**  
Amazon SageMaker Ground Truth is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Ground Truth, but we do not plan to introduce new features.

Use one of the following sections to create a label verification job for your task type.

**Topics**
+ [Create an image label adjustment job (console)](#sms-data-adjust-start-console-bb-ss)
+ [Create a point cloud or video frame label adjustment job (console)](#sms-data-adjust-start-console-frame)

## Create an image label adjustment job (console)
<a name="sms-data-adjust-start-console-bb-ss"></a>

Use the following procedure to create a bounding box or semantic segmentation adjustment labeling job using the console. This procedure assumes that you have already created a bounding box or semantic segmentation labeling job and its status is Complete. This the labeling job that produces the labels you want adjusted.

**To create an image label adjustment job (console)**

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/) and choose **Labeling jobs**.

1. Start a new labeling job by [chaining](sms-reusing-data.md) a prior job or start from scratch, specifying an input manifest that contains labeled data objects.

1. Choose the same task type as the original labeling job.

1. Choose **Next**.

1. In the **Workers** section, choose the type of workforce you would like to use. For more details about your workforce options see [Workforces](sms-workforce-management.md).

1. (Optional) After you've selected your workforce, specify the **Task timeout** and **Task expiration time**.

1. Expand **Existing-labels display options** by selecting the arrow next to the title.

1. Check the box next to **I want to display existing labels from the dataset for this job**.

1. For **Label attribute name**, choose the name from your manifest that corresponds to the labels that you want to display for adjustment. You will only see label attribute names for labels that match the task type you selected on the previous screen. Ground Truth tries to detect and populate these values by analyzing the manifest, but you might need to set the correct value.

1. Use the instructions areas of the tool designer to provide context about what the previous labelers were tasked with doing and what the current verifiers need to check and adjust.

1. Choose **See preview** to check that the tool shows the prior labels correctly and presents the task clearly.

1. Select **Create**. This will create and start your labeling job.

## Create a point cloud or video frame label adjustment job (console)
<a name="sms-data-adjust-start-console-frame"></a>

Use the following procedure to create a 3D point cloud or video frame adjustment job using the console. This procedure assumes that you have already created a labeling job using the task type that produces the types of labels you want to be verified and its status is Complete.

**To create a 3D point cloud or video frame label adjustment job (console)**

1. Open the SageMaker AI console: [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/) and choose **Labeling jobs**.

1. Start a new labeling job by [chaining](sms-reusing-data.md) a prior job or start from scratch, specifying an input manifest that contains labeled data objects.

1. Choose the same task type as the original labeling job.

1. Toggle on the switch next to **Display existing labels**.

1. Select **Adjustment**.

1. For **Label attribute name**, choose the name from your manifest that corresponds to the labels that you want to display for adjustment. You will only see label attribute names for labels that match the task type you selected on the previous screen. Ground Truth tries to detect and populate these values by analyzing the manifest, but you might need to set the correct value.

1. Use the instructions areas of the tool designer to provide context about what the previous labelers were asked to do and what the current adjusters need to check. 

   You cannot remove or modify existing labels but you can add new labels. You can remove, modify and add new label category attributes or frame attributes.

   Be default, preexisting label category attributes and frame attributes will be editable by workers. If you want to make a label category or frame attribute uneditable, deselect the **Allow workers to edit this attribute** check box for that attribute.

   To learn more about label category and frame attributes, see [Worker user interface (UI)](sms-point-cloud-general-information.md#sms-point-cloud-worker-task-ui) for 3D point cloud and [Worker user interface (UI)](sms-video-overview.md#sms-video-worker-task-ui) for video frame. 

1. Choose **See preview** to check that the tool shows the prior labels correctly and presents the task clearly.

1. Select **Create**. This will create and start your labeling job.
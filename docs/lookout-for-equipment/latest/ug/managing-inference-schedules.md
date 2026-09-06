

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Managing inference schedules
<a name="managing-inference-schedules"></a>

## Stopping inference
<a name="stopping-inference"></a>

This section explains how to halt the inference process.

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.

1. If necessary, choose the **Active schedules** tab.

1. Select the schedule that you want to stop.

1. Choose **Stop**.

1. Choose **Stop schedule**.

1. Your stopped schedule will appear on the **Inactive schedules** tab.

## Resuming inference
<a name="resuming-inference"></a>

This section explains how to resume a stopped inference schedule.

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.

1. If necessary, choose the **Inactive schedules** tab.

1. Choose **Set as active**.

1. Your stopped schedule will appear on the **Active schedules** tab.

## Editing an active schedule
<a name="editing-from-active"></a>

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.

1. If necessary, choose the **Active schedules** tab.

1. Select the schedule that you want to edit.

1. Choose **Edit**.

1. On the pop-up window, choose **edit**.

**Note**  
After you finish editing an inference schedule, the schedule returns to the activation status that it was in before you started editing.  
A schedule that was active before editing will return to active status after editing. 

## Editing an inactive schedule
<a name="editing-from-inactive"></a>

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.

1. If necessary, choose the **Inactive schedules** tab.

1. Select the schedule that you want to edit.

1. Choose **Edit**.

1. On the pop-up window, choose **edit**.

**Note**  
After you finish editing an inference schedule, the schedule returns to the activation status that it was in before you started editing.  
A schedule that was inactive before editing will remain inactive after editing. To re-activate it, you must select the schedule on the **Inactive schedules** page and choose **Set as active**.

## Delete an active schedule
<a name="inference-deleting-active"></a>

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.

1. If necessary, choose the **Active schedules** tab.

1. Select the schedule that you want to delete.

1. Choose **Delete**.

1. In the pop-up window, choose **Stop** to indicate that you are going to stop the schedule before deleting it.

1. In the pop-up window, enter {{delete}} in the text field.

1. In the pop-up window, choose **delete**.

## Delete an inactive schedule
<a name="inference-deleting-inactive"></a>

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.

1. If necessary, choose the **Inactive schedules** tab.

1. Select the schedule that you want to delete.

1. Choose **Delete**.

1. In the pop-up window, enter {{delete}} in the text field.

1. In the pop-up window, choose **delete**.
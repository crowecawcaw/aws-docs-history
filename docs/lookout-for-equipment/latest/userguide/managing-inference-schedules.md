On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Managing inference schedules

## Stopping inference

This section explains how to halt the inference process.

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.
2. If necessary, choose the **Active schedules** tab.
3. Select the schedule that you want to stop.
4. Choose **Stop**.
5. Choose **Stop schedule**.
6. Your stopped schedule will appear on the **Inactive schedules** tab.

## Resuming inference

This section explains how to resume a stopped inference schedule.

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.
2. If necessary, choose the **Inactive schedules** tab.
3. Choose **Set as active**.
4. Your stopped schedule will appear on the **Active schedules** tab.

## Editing an active schedule

1. From the AWS console, under Lookout for Equipment, from the left nav, choose **Inference schedules**.
2. If necessary, choose the **Active schedules** tab.
3. Select the schedule that you want to edit.
4. Choose **Edit**.
5. On the pop-up window, choose **edit**.

###### Note

After you finish editing an inference schedule, the schedule returns to the activation status that it was in before you started editing.

A schedule that was active before editing will return to active status after editing.

## Editing an inactive schedule

1. From the AWS console, under Lookout for Equipment, from the left nav, choose
   **Inference schedules**.
2. If necessary, choose the **Inactive schedules** tab.
3. Select the schedule that you want to edit.
4. Choose **Edit**.
5. On the pop-up window, choose **edit**.

###### Note

After you finish editing an inference schedule, the schedule returns to the
activation status that it was in before you started editing.

A schedule that was inactive before editing will remain inactive after editing. To
re-activate it, you must select the schedule on the **Inactive
schedules** page and choose **Set as active**.

## Delete an active schedule

1. From the AWS console, under Lookout for Equipment, from the left nav, choose
   **Inference schedules**.
2. If necessary, choose the **Active schedules** tab.
3. Select the schedule that you want to delete.
4. Choose **Delete**.
5. In the pop-up window, choose **Stop** to indicate that you are going to stop the schedule before deleting it.
6. In the pop-up window, enter `delete` in the text field.
7. In the pop-up window, choose **delete**.

## Delete an inactive schedule

1. From the AWS console, under Lookout for Equipment, from the left nav, choose
   **Inference schedules**.
2. If necessary, choose the **Inactive schedules** tab.
3. Select the schedule that you want to delete.
4. Choose **Delete**.
5. In the pop-up window, enter `delete` in the text field.
6. In the pop-up window, choose **delete**.

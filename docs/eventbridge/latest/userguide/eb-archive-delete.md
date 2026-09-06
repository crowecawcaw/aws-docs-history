

# Deleting event archives in Amazon EventBridge
<a name="eb-archive-delete"></a>

When you delete an archive, EventBridge deletes the following resources:
+ The archive and any events it contains.
+ The event pattern, if any, specified for the archive.
+ The managed rule EventBridge generated for the archive.

**To delete an archive from an event bus (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Navigate to the archive directly, or from the source event bus:
   + In the navigation pane, choose **Event buses**.

     On the events bus details page, choose the **Archives** tab.
   + In the navigation pane, choose **Archives**.

1. Choose the event bus that contains the archive you want to delete.

1. On the event bus details page, select the **Archives** tab.

1. Select the archive, and then select **Delete**.

**To delete an archive (AWS CLI)**
+ Use [delete-archive](https://docs.aws.amazon.com/cli/latest/reference/events/delete-archive.html).
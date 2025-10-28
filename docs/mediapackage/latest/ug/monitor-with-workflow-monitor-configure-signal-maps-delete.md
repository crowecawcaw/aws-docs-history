# Deleting the signal map of your AWS media workflow

If you not longer need a signal map, it can be deleted. If you have
monitoring templates deployed on the signal map, the deletion process will
ask you to delete any CloudWatch and EventBridge resources that have been deployed to
this signal map. Deleting the deployed resources does not affect the
templates that created them. This resource deletion is to ensure that you do
not have CloudWatch and EventBridge resources that are deployed but not used.

###### To delete a signal map

1. From the workflow monitor console's navigation pane, select **Signal
   maps** and select the radio button next to the signal
   map you want to delete.
2. Select the **Delete** button. You will be asked
   to confirm the deletion of the monitoring resources. Select
   **Delete** to begin the monitoring resource
   deletion process.
3. The **Monitor deployment** column will display
   the current status. When the status has changed to
   **DELETE_COMPLETE**, select the
   **Delete** button again.
4. You will be asked to confirm deletion of the signal map. Select
   **Delete** to proceed and delete the signal
   map.

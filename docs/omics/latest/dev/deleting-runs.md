# Delete a run in HealthOmics

When you no longer need a run, you can delete it using the AWS CLI, API, or console.
You can delete a run when its status is `COMPLETED` or `CANCELED`.

From the console, follow these steps to delete a run:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, select one or more runs to delete.
4. From the action menu above the table, choose **Delete**.
5. In the modal form, type **confirm** to confirm the deletion.
   The following AWS CLI command deletes a run. To run the example, replace the `run id` with the ID of the run you want to delete. There is no response if the run is successfully
   deleted.

```
aws omics delete-run --id ``run id``
```

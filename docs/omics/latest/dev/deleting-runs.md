AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

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

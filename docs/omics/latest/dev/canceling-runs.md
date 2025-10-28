AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Cancel a run in HealthOmics

You can cancel a run if its status is
`PENDING`, `STARTING`, `RUNNING`, or `STOPPING`.

###### Note

When you cancel a run, HealthOmics doesn't save any of the run outputs.

From the console, follow these steps to cancel a run:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, choose the run to cancel.
4. The console opens the **Run details** page.
   From the status banner at the top of the page, choose **Stop run**.
5. Enter **confirm** to stop the run.
   To cancel a run using the API, use the **CancelRun** API operation.

The following example shows how to cancel a run using the AWS CLI . To run the example, replace the
`run id` with the ID of the run you would like to cancel. If successful,
there is no response.

```
aws omics cancel-run --id ``run id``
```

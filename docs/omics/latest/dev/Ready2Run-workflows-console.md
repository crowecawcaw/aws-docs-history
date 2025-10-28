AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Starting HealthOmics Ready2Run workflows using the console

Using Ready2Run workflows in the console is similar to using a private workflow.
One key difference is that the workflow publisher provides sample data, so that you can try out
the workflow without creating your own data.

###### To use a Ready2Run workflow in the console

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Ready2Run workflows**.
3. On the **Ready2Run workflows** page, choose the workflow that you want to use.
   The console opens the details page for that workflow.
4. The details tab lists information such as the
   name, list price per run, description, workflow language type, run storage
   capacity, status, creation date, and parameters with descriptions. The
   details tab also tells you whether the workflow requires a subscription.
5. To use the workflow, choose **Create run**
6. In the **Specify run details** page, enter a run name. Optionally, you can specify the
   workflow version. You can also add run priority to the run.
7. Enter or select an Amazon S3 location for the run output.
8. For **Run metadata retention mode**, choose whether to retain or remove run metadata.
9. In the **Service role** panel, choose whether to use an existing service role or create a new one.
10. (Optional) Add tags to help identify and manage your run.
11. Choose **Next**.
12. From the **Add parameters** page, choose one of the options to add the run parameter
    values:
    - Select a parameter file (in JSON format) from an Amazon S3 location.
    - Select a parameter file (in JSON format) from your local drive.
    - Manually enter the parameter values.
    - Run workflow with Ready2Run sample data provided by the workflow publisher.

13. If you upload a JSON file, the console parses the file and performs inline validation.
    You can then manually update the values of your parameters as needed.
14. Choose **Next**.
15. Review your inputs, then choose **Start run**.

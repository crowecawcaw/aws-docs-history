AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Clone a run in HealthOmics

You can clone an existing run using the HealthOmics console. Cloning creates a new run using the cloned run's configuration values. You can
modify these default values and add other optional inputs.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, select the run to clone.
4. From the action menu above the table, choose **Clone run**.
   The console opens the Clone run form. The form is identical to **Start run**,
   except the console populates the form with all relevant values from the cloned run.

The console creates a new run ID for the run clone, and adds this run ID as a suffix
to the run name.

As you proceed through the form pages, you can adjust the configuration values as required. 5. After you review the run configuration, choose **Start run**.

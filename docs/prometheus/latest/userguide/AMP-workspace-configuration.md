# Configure your workspace

You can configure your workspace for the following:

- Define _label sets_ and define limits on the active time series that match your defined label sets.
  A label set is a set of one or more _labels_, which are name/value pairs that help give context to time series metrics.

By defining label sets and setting active time series limits, you can limit spikes in one tenant or source to affect only that tenant or source. For example,
if you set a 1,000,000 active time series limit on the label set `team=A env=prod`, then if the number of ingested time series that match that label set
exceed the limit, then only the time series that match the label set are throttled. This way, other tenants or metric sources are unaffected.

For more information about labels in Prometheus, see [Data Model](https://prometheus.io/docs/concepts/data_model/#data-model "https://prometheus.io/docs/concepts/data_model/#data-model").

- Set a retention period to define the number of days for the data to be retained in the workspace.

###### To configure your workspace

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home "https://console.aws.amazon.com/prometheus/home").
2. In the upper left corner of the page, choose the menu icon and then choose
   **All workspaces**.
3. Choose the **Workspace ID** of the workspace.
4. Choose the **Workspace configurations** tab.
5. To set the retention period for the workspace, choose **Edit** in the **Retention period** section. Then
   specify the new retention period in days. The maximum is 1095 days (three years).
6. To add or modify label sets and their active series limits, choose **Edit** in the **Label sets** section. Then do
   the following:
   1. (Optional) Enter a value in **Default bucket limit** to set a limit on the maximum number of active time series that can be ingested in the workspace,
      counting only time series that don’t match any defined label set.
   2. To define a label set, enter an active time series limit for the new label set under **Active series limit**.

   Then, enter a label and value for one label that will be used in the label set, and choose **Add label**. 3. (Optional) To define another label set, choose **Add another label set** and repeat the previous steps.

7. When you are finished, choose **Save changes**.

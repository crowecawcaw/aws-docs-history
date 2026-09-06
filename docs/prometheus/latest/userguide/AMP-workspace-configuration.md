

# Configure your workspace
<a name="AMP-workspace-configuration"></a>

You can configure your workspace for the following:
+ Define *label sets* and define limits on the active time series that match your defined label sets. A label set is a set of one or more *labels*, which are name/value pairs that help give context to time series metrics.

  By defining label sets and setting active time series limits, you can limit spikes in one tenant or source to affect only that tenant or source. For example, if you set a 1,000,000 active time series limit on the label set `team=A env=prod`, then if the number of ingested time series that match that label set exceed the limit, then only the time series that match the label set are throttled. This way, other tenants or metric sources are unaffected.

  For more information about labels in Prometheus, see [Data Model](https://prometheus.io/docs/concepts/data_model/#data-model). 
+ Set a retention period to define the number of days for the data to be retained in the workspace.
+ Set an *out-of-order time window* to allow the workspace to accept samples that arrive out of chronological order. All workspaces have a default out-of-order time window of 60 seconds. Setting this value to 0 disables the feature and out-of-order samples are discarded.
+ Set a *rule query offset* to introduce a global delay before rule evaluation queries run. This compensates for ingestion delays or out-of-order samples, ensuring that rules evaluate against a more complete dataset. A query offset configured at the rule group level takes priority over this workspace-level setting. For more information, see [Use offset in queries to handle ingestion delays](troubleshoot-rule-evaluations.md#troubleshoot-rule-offset-queries).

**To configure your workspace**

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home).

1. In the upper left corner of the page, choose the menu icon and then choose **All workspaces**.

1. Choose the **Workspace ID** of the workspace.

1. Choose the **Workspace configurations** tab.

1. To set the retention period for the workspace, choose **Edit** in the **Retention period** section. Then specify the new retention period in days. The maximum is 1095 days (three years).

1. To set the out-of-order time window, choose **Edit** in the **Out of order time window** section. Then specify the time window in seconds. All workspaces have a default out-of-order time window of 60 seconds. The minimum value is 0 seconds; when set to 0, out-of-order samples are discarded. The maximum value is 600 seconds. To request a higher maximum, see [Amazon Managed Service for Prometheus service quotas](AMP_quotas.md).

1. To set the rule query offset, choose **Edit** in the **Rule query offset** section. Then specify the offset in seconds. The default value for new workspaces is 60 seconds. The minimum value is 0 seconds and the maximum value is 86,400 seconds (24 hours).
**Note**  
Existing workspaces have a default rule query offset of 0 seconds, which you can update through the console.  
If you have configured an out-of-order time window, consider setting the rule query offset to a value greater than or equal to the out-of-order time window. This ensures that out-of-order samples are included in rule evaluations. A rule query offset delays rule evaluations and any resulting alerts by the configured duration.

1. To add or modify label sets and their active series limits, choose **Edit** in the **Label sets** section. Then do the following:

   1. (Optional) Enter a value in **Default bucket limit** to set a limit on the maximum number of active time series that can be ingested in the workspace, counting only time series that don’t match any defined label set.

   1. To define a label set, enter an active time series limit for the new label set under **Active series limit**.

      Then, enter a label and value for one label that will be used in the label set, and choose **Add label**. 

   1. (Optional) To define another label set, choose **Add another label set** and repeat the previous steps.

1. When you are finished, choose **Save changes**.
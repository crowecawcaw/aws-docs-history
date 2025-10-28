# Adding historical usage to your bill scenario

This section outlines how to add historical usage to your bill scenario.

## Prerequisites

The following procedure assumes that you have already completed the [Creating a bill scenario](pc-create-bill-scenario.md "pc-create-bill-scenario.md") process.

## Procedure

###### To add historical usage to a bill scenario

1. Open the Pricing Calculator console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/") .
2. In the navigation pane, choose **Pricing Calculator**.
3. In the **Bill scenario** of the **Bill estimate** tab, choose
   the scenario you want to add usage to.
4. From the **Add** dropdown in the **Usage** section, choose
   **Historical workload from my accounts**.
5. Select the time range of historical usage that you want to import.

###### Note

A maximum of 2000 usage lines that can be added to a single bill scenario. 6. (Optional) Add up to five filters. Filters allow you to specify lines of your usage
that you want to add. Filter example include cost category and services.

###### Note

For each filters, the values are based on the time period selected in the previous
step. 7. You can choose to add your usage to an existing group or a new group you create. 8. Choose **Preview**. 9. Check that the preview shows the usage that you want to import to your workload estimate.

###### Note

The usage is aggregated based on the account, Region, service code, usage type, and
operation. This means that if the time range is across multiple months and
your selection yields usage from the same account, Region, service code, usage type,
and operation across multiple months, then all the usage amount and cost is
added together into one line. 10. To add the historical usage to the workload estimate, choose **Import**.

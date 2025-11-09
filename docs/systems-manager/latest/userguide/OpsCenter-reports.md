AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Viewing OpsCenter summary reports

AWS Systems Manager OpsCenter includes a summary page that automatically displays the following
information:

- **OpsItem status summary** – A summary of OpsItems by
  status, such as `Open` and `In progress`.
- **Sources with most open OpsItems** – A breakdown of the
  top AWS services that have open OpsItems.
- **OpsItems by source and age** – A count of OpsItems,
  grouped by source and number of days since creation.

###### To view OpsCenter summary reports

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **OpsCenter**, and then choose
   the **Summary** tab.
3. In the **OpsItems by source and age** section, do the
   following:
   1. (Optional) In the filter field, choose **Source**,
      select `Equal`, `Begin With`, or
      `Not Equal`, and then enter a search
      parameter.
   2. In the adjacent list, select one of the following status
      values:
      - `Open`
      - `In progress`
      - `Resolved`
      - `Open and in progress`
      - `All`

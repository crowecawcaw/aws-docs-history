# Run Configuration Checks

Follow along these steps to evaluate the SAP Configuration of a Systems Manager for SAP application.

###### Note

SAP Configuration Checks are currently only supported for Application type SAP HANA. See also [support restrictions for Systems Manager for SAP](supported-versions.md "supported-versions.md").

**To access configuration checks:**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/")
2. In the navigation pane, choose **Application Tools**, then choose **Application Manager**
3. From the list of registered applications, choose the SAP HANA application you want to evaluate
4. Choose **Actions**, then choose **SAP Configuration Checks**

**To evaluate configuration checks:**

1. Select one or more checks you want to evaluate
2. Choose **Run**
3. Monitor the task status using either the operation ID provided in the notification banner or by choosing **Actions** > **View operations**

**To view and analyze check results:**

1. Select a single check to view its details
2. Expand individual subchecks to see detailed rules
3. Sort subchecks by Rule Status, Description, or Component
4. Filter results by rule status using the status totals or the filter box
5. Clear filters by selecting the cancel indicator
6. View previous results by selecting a different evaluation date from the dropdown list
7. Access additional information through the provided Documentation links

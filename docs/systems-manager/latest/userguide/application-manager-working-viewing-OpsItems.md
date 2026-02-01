• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Viewing OpsItems for

an application

In Application Manager, a component of AWS Systems Manager, the **OpsItems** tab
displays operational work items (OpsItems) for resources in the selected application.
You can configure Systems Manager OpsCenter to automatically create OpsItems from Amazon CloudWatch alarms
and Amazon EventBridge events. You can also manually create OpsItems.

###### Actions you can perform on this tab

You can perform the following actions on this page:

- Filter the list of OpsItems by using the search field. You can filter by OpsItem
  name, ID, source ID, or severity. You can also filter the list based on
  status. OpsItems support the following statuses: Open, In progress, Open and In
  progress, Resolved, or All.
- Change the status of an OpsItem by choosing the option button beside it and
  then choosing an option in the **Set status** menu.
- Open Systems Manager OpsCenter to create an OpsItem by choosing **Create
  OpsItem**.

###### To open the **OpsItems** tab

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Application Manager**.
3. In the **Applications** section, choose a category. If
   you want to open an application you created manually in Application Manager, choose
   **Custom applications**.
4. Choose the application in the list. Application Manager opens the
   **Overview** tab.
5. Choose the **OpsItems** tab.

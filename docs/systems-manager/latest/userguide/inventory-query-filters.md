• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Querying an inventory collection by using

filters

After you collect inventory data, you can use the filter capabilities in AWS Systems Manager to
query a list of managed nodes that meet certain filter criteria.

###### To query nodes based on inventory filters

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Inventory**.
3. In the **Filter by resource groups, tags or inventory types**
   section, choose the filter box. A list of predefined filters is
   displayed.
4. Choose an attribute to filter on. For example, choose
   `**AWS:Application**`. If prompted, choose a
   secondary attribute to filter. For example, choose
   `**AWS:Application.Name**`.
5. Choose a delimiter from the list. For example, choose **Begin
   with**. A text box is displayed in the filter.
6. Enter a value in the text box. For example, enter _Amazon_
   (SSM Agent is named _Amazon SSM Agent_).
7. Press **Enter**. The system returns a list of managed nodes that
   include an application name that begins with the word
   _Amazon_.

###### Note

You can combine multiple filters to refine your search.

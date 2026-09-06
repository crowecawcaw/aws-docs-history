

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Choosing a filter view for managed node summaries
<a name="explore-nodes-filter-view"></a>

The **Explore nodes** page in Systems Manager lets you view aggregated data about your fleet according to several available filter views.

**To choose a filter view for managed node summaries**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Explore nodes**.

1. For **Filter view**, select one of the filter options and optionally further refine the report:
   + **Managed nodes** – In the search (![The search icon](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/search-icon.png)) box, you can select a property and delimiter, such as `Node type = Managed EC2 instances`.
   + **Operating systems** – In the **Filter Operating system versions** list, you can select an OS version number. In the search (![The search icon](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/search-icon.png)) box, you can select a property and delimiter, such as `Node type = Managed EC2 instances`.
   + **SSM Agent versions** – In the **Filter Operating systems** list, you can select an OS name. In the search (![The search icon](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/search-icon.png)) box, you can select a property and delimiter, such as `Node type = Managed EC2 instances`.
   + **Node types** – In the **Filter Operating systems** list, you can select an OS name. In the search (![The search icon](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/search-icon.png)) box, you can select a property and delimiter, such as `Node type = Managed EC2 instances`.

After optionally filtering the list, you can view details about a specific managed node by choosing its ID in the **Node ID** column. From that detailed view, you can perform several actions on the node.


• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Configure AWS Resource Explorer using Quick Setup
<a name="Resource-explorer-quick-setup"></a>

With Quick Setup, you can quickly configure AWS Resource Explorer to search and discover resources in your AWS account or across an entire AWS organization. You can search for your resources using metadata like names, tags, and IDs. AWS Resource Explorer provides fast responses to your search queries by using *indexes*. Resource Explorer creates and maintains indexes using a variety of data sources to gather information about resources in your AWS account. 

Quick Setup for Resource Explorer automates the index configuration process. For more information about AWS Resource Explorer, see [ What is AWS Resource Explorer?](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html) in the AWS Resource Explorer User Guide.

During Quick Setup, Resource Explorer does the following: 
+ Creates an index in every AWS Region in your AWS account.
+ Updates the index in the Region you specify to be the aggregator index for the account.
+ Creates a default view in the aggregator index Region. This view has no filters so it returns all resources found in the index.

**Minimum permissions**

To perform the steps in the following procedure, you must have the following permissions:
+ **Action**: `resource-explorer-2:*` – **Resource**: no specific resource (`*`)
+ **Action**: `iam:CreateServiceLinkedRole` – **Resource**: no specific resource (`*`)

**To configure Resource Explorer**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Quick Setup**.

1. On the **Resource Explorer** card, choose **Create**.

1. In the **Aggregator Index Region** section, choose which Region you want to contain the **aggregator index**. You should select the Region that is appropriate for the geographic location for your users.

1. (Optional) Select the **Replace existing aggregator indexes in Regions other than the one selected above** check box. 

1. In the **Targets** section, choose the target **organization** or specific **Organizational Units (OUs)** containing the resources you want to discover. 

1. In the **Regions** section, choose which **Regions** to include in the configuration. 

1. Review the configuration summary, and then choose **Create**. 

On the **Resource Explorer** page, you can monitor the configuration status.
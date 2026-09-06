

# Work with inventory search in License Manager
<a name="discovery"></a>

License Manager uses [Systems Manager inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to discover software usage on premises. After you associate a self-managed license with on-premises servers, License Manager periodically collects software inventory, updates licensing information, and refreshes its dashboards to report usage.

**Topics**
+ [Set up for inventory search](#discovery-setup)
+ [Use inventory search](#using-discovery)
+ [Add automated discovery rules to a self-managed license](#add-discovery-rule)
+ [Associate a self-managed license with inventory search](#discovered)
+ [Disassociate a self-managed license and a resource](#disassociate)

## Set up for inventory search
<a name="discovery-setup"></a>

Complete the following requirements before using resource inventory search:
+ Enable cross-account inventory discovery by integrating License Manager with your AWS Organizations account. For more information, see [Settings in License Manager](settings.md).
+ Create self-managed licenses for the servers and applications to manage. For example, create a self-managed license that reflects the terms of your licensing agreement with Microsoft for SQL Server Enterprise.

## Use inventory search
<a name="using-discovery"></a>

Complete the following steps to search your resource inventory. You can search for applications by name (for example, names that begin with "SQL Server") and the type of license included (for example, a license that is not for "SQL Server Web").

**Search your resource inventory**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Inventory search**.

1. (Optional) You can specify filter options to streamline search results as follows.  
**Amazon EC2 resources**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/license-manager/latest/userguide/discovery.html)  
**Amazon RDS resources**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/license-manager/latest/userguide/discovery.html)

   For more information about Amazon RDS database product licenses, see [RDS for Oracle licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.Licensing.html), [RDS for Db2 licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html), or [RDS for SQL Server licensing options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.Licensing.html) in the *Amazon RDS User Guide*.

## Add automated discovery rules to a self-managed license
<a name="add-discovery-rule"></a>

After you add product information to your self-managed license, License Manager can track license usage for the instances that have those products installed. For more information, see [Automated discovery of inventory in License Manager](automated-discovery.md).

**To add automated discovery rules to a self-managed license**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Open the **Inventory search** page.

1. Select the resource and choose **Add automated discovery rules**.

1. For **Self-managed license**, select a self-managed license.

1. Specify the products to discover and track.

1. (Optional) Select **Stop tracking instances when software is uninstalled** to make the license available for reuse after License Manager detects that the software was uninstalled and any license affinity period has elapsed.

1. (Optional) To exclude resources from automated discovery select **Add exclusion rule**.
**Note**  
Exclusion rules do not apply to Amazon RDS products (such as RDS for Oracle, RDS for Db2, and RDS for SQL Server).

   1. Choose a **Property** to filter on, currently **Account ID**, and **Tag** are supported.

   1. Enter the information to identify that property. For an **Account ID** specify the 12 digit AWS Account ID as the value. For **Tags** enter a key/value pair.

   1. Repeat step 7 to add additional rules.

1. Choose **Add**.

## Associate a self-managed license with inventory search
<a name="discovered"></a>

After you have identified the unmanaged resources that you need to manage, you can manually associate them with a self-managed license, instead of using automated discovery.

**To associate a self-managed license with a resource**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Open the **Inventory search** page.

1. Select the resource and choose **Associate self-managed license**.

1. For **self-managed license name**, select a self-managed license.

1. (Optional) Select **Share self-managed license with all my member accounts**.

1. Choose **Associate**.

## Disassociate a self-managed license and a resource
<a name="disassociate"></a>

If the licensing terms from your software vendors change, you can disassociate resources that were associated manually and then delete the self-managed license.

**To disassociate a self-managed license and a resource**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **self-managed license**.

1. Choose the name of the self-managed license.

1. Choose **Resources**.

1. Select each of the resources to disassociate from the self-managed license and then choose **Disassociate resource**.
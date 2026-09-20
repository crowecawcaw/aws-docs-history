

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

<table>
<thead>
  <tr><th>Filter name</th><th>Description</th><th>Logical operators</th><th>Supported values</th></tr>
</thead>
<tbody>
  <tr><td>Resource ID</td><td>The ID of the resource.</td><td><code>Equals</code>, <code>Not equals</code></td><td></td></tr>
  <tr><td>Account ID</td><td>The ID of the AWS account that owns the resource.</td><td><code>Equals</code>, <code>Not equals</code></td><td></td></tr>
  <tr><td>Platform name</td><td>The operating system platform for the resource.</td><td><code>Equals</code>, <code>Not equals</code>, <code>Begins with</code>, <code>Contains</code></td><td></td></tr>
  <tr><td>Application name</td><td>The name of the application.</td><td><code>Equals</code>, <code>Begins with</code></td><td></td></tr>
  <tr><td>License included name</td><td>The type of license included.</td><td><code>Equals</code>, <code>Not equals</code></td><td> <ul><li> <code>SQL Server Enterprise</code> </li><li> <code>SQL Server Standard</code> </li><li> <code>SQL Server Web</code> </li><li> <code>Windows Server Datacenter</code> </li></ul> </td></tr>
  <tr><td>Tag</td><td>A metadata tag key and optional value that's assigned to the resource.<br />Note, the <code>Not equals</code> logical operator is only available if cross-account discovery is enabled.</td><td><code>Equals</code>, <code>Not equals</code></td><td></td></tr>
</tbody>
</table>



**Amazon RDS resources**  

<table>
<thead>
  <tr><th>Filter name</th><th>Description</th><th>Logical operators</th><th>Supported values</th></tr>
</thead>
<tbody>
  <tr><td>Engine Edition</td><td>The database engine edition.</td><td><code>Equals</code></td><td> <ul><li> <code>oracle-ee</code> </li><li> <code>oracle-se</code> </li><li> <code>oracle-se1</code> </li><li> <code>oracle-se2</code> </li><li> <code>db2-se</code> </li><li> <code>db2-ae</code> </li><li> <code>sqlserver-ee</code> </li><li> <code>sqlserver-se</code> </li></ul> </td></tr>
  <tr><td>License Pack (Oracle only)</td><td>The management pack associated with an Amazon RDS for Oracle license.</td><td><code>Equals</code></td><td> <ul><li> <code>Spatial and Graph</code> </li><li> <code>Active Data Guard</code> </li><li> <code>Label Security</code> </li><li> <code>Oracle On-Line Analytical Processing (OLAP)</code> </li><li> <code>Diagnostic Pack and Tuning Pack</code> </li></ul> </td></tr>
</tbody>
</table>


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
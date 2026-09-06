

# Mixpanel connector for Amazon AppFlow
<a name="connectors-mixpanel"></a>

Mixpanel is a service that provides analytics about user engagement in web and mobile applications. If you use Mixpanel, you can also use Amazon AppFlow to transfer your data to certain AWS services or other supported applications.

**Topics**
+ [Mixpanel support](#mixpanel-support)
+ [Before you begin](#mixpanel-prereqs)
+ [Connecting Amazon AppFlow to your Mixpanel account](#mixpanel-connecting)
+ [Transferring data from Mixpanel with a flow](#mixpanel-import-data)
+ [Supported objects](#mixpanel-reference-objects)
+ [Supported destinations](#mixpanel-reference-destinations)

## Mixpanel support
<a name="mixpanel-support"></a>

Amazon AppFlow supports Mixpanel as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from your Mixpanel account.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to your Mixpanel account.

## Before you begin
<a name="mixpanel-prereqs"></a>

Before you can use Amazon AppFlow to transfer data from Mixpanel, you need the following:
+ A Mixpanel project that contains the data that you want to transfer.
+ A *service account* for your Mixpanel project. In Mixpanel, a service account is a type of user that you authorize to access a project programmatically with the Mixpanel API. Amazon AppFlow needs this account to access your data. For more information, see [Service Accounts](https://developer.mixpanel.com/reference/service-accounts) in the Mixpanel documentation.

  When you create a Mixpanel connection in Amazon AppFlow, you provide the following properties from your service account:
  + Username
  + Secret

## Connecting Amazon AppFlow to your Mixpanel account
<a name="mixpanel-connecting"></a>

To connect Amazon AppFlow to your Mixpanel project, provide details about the service account that enables Amazon AppFlow to access your data. To create a service account, see [Before you begin](#mixpanel-prereqs).

**To connect to Mixpanel**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Mixpanel**.

1. Choose **Create connection**.

1. In the **Connect to Mixpanel** window, enter the following:
   + **User name** – The user name of the Mixpanel service account that provides access to your project.
   + **Password** – The service account secret.
   + **MixPanel Instance URL** – Choose **https://mixpanel.com/api/app/me**.
   + **MixPanel API version** – Choose **2.0**.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Mixpanel as the data source, you can select this connection.

## Transferring data from Mixpanel with a flow
<a name="mixpanel-import-data"></a>

To transfer data from Mixpanel, create an Amazon AppFlow flow, and choose Mixpanel as the data source. To learn how to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose which data object that you want to transfer. For more information about the objects that Amazon AppFlow supports for Mixpanel, see [Supported objects](#mixpanel-reference-objects).

**Required filters for Mixpanel data objects**  
When you create a flow and use Mixpanel as the data source, most data objects require you to specify one or more *filters*. Filters are typically optional criteria that you use to transfer data objects selectively. Specifically for flows that transfer from Mixpanel, you must specify filters to provide Amazon AppFlow with parameter values that it needs to query your data.  
For the filters that are required for each Mixpanel data object, see [Supported objects](#mixpanel-reference-objects).

Also choose the destination where you want to transfer the data object that you selected. For more information on how to configure your destination, see [Supported destinations](#mixpanel-reference-destinations).

## Supported objects
<a name="mixpanel-reference-objects"></a>

When you create a flow that uses Mixpanel as the data source, you can transfer any of the data objects shown in the following table. To retrieve each object, Amazon AppFlow sends a query to the URI in the *Mixpanel endpoint* column. Most data objects support one or more filters that appear under *Supported filters*. Flows that transfer from Mixpanel require certain filters.


| Object | Mixpanel endpointThe following paths are appended to the base URI: `https://mixpanel.com/api/2.0`. | Supported filters | 
| --- | --- | --- | 
| Annotations | /annotations |  +  from\_date   | 
| Cohorts | /cohorts/list | None | 
| Engage | /engage | None | 
| Events | /events |  +  event\* <br />+  from\_date\* <br />+  interval <br />+  to\_date\* <br />+  type\* <br />+  unit\* <br />+  workspace\_id   | 
| Events Names | /events/names |  +  limit <br />+  type\* <br />+  workspace\_id   | 
| Events Properties | /events/properties |  +  event\* <br />+  from\_date\* <br />+  interval <br />+  limit <br />+  name\* <br />+  to\_date\* <br />+  type\* <br />+  unit\* <br />+  workspace\_id   | 
| Events Properties Top | /events/properties/top |  +  event\* <br />+  limit <br />+  workspace\_id   | 
| Events Properties Values | /events/properties/values |  +  event\* <br />+  limit <br />+  name\* <br />+  workspace\_id   | 
| Events Top | /events/top |  +  limit <br />+  type\* <br />+  workspace\_id   | 
| Funnels | /funnels |  +  from\_date\* <br />+  funnel\_id\* <br />+  interval <br />+  length <br />+  length\_unit <br />+  limit <br />+  to\_date <br />+  unit\* <br />+  workspace\_id   | 
| Profile Event Activity | /stream/query |  +  distinct\_ids <br />+  from\_date\* <br />+  to\_date\* <br />+  workspace\_id   | 
| Retention | /retention/addiction |  +  addiction\_unit <br />+  event <br />+  from\_date\* <br />+  limit <br />+  to\_date\* <br />+  unit\* <br />+  workspace\_id   | 
| Segmentation | /segmentation |  +  event\* <br />+  from\_date\* <br />+  interval <br />+  limit <br />+  to\_date\* <br />+  type <br />+  unit <br />+  workspace\_id   | 
| Segmentation Average | /segmentation/average |  +  event\* <br />+  from\_date\* <br />+  on\* <br />+  to\_date\* <br />+  unit <br />+  workspace\_id   | 
| Segmentation Numeric | /segmentation/numeric |  +  event\* <br />+  from\_date\* <br />+  on\* <br />+  to\_date\* <br />+  type <br />+  unit <br />+  workspace\_id   | 
| Segmentation Sum | /segmentation/sum |  +  event\* <br />+  from\_date\* <br />+  on\* <br />+  to\_date\* <br />+  unit <br />+  workspace\_id   | 

\* You must specify this filter in your flow definition before Amazon AppFlow can successfully retrieve your data.

## Supported destinations
<a name="mixpanel-reference-destinations"></a>

When you create a flow that uses Mixpanel as the data source, you can set the destination to any of the following connectors: 
+ [Amazon Lookout for Metrics](lookout.md)
+ [Amazon Redshift](redshift.md)
+ [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md)
+ [Amazon S3](s3.md)
+ [HubSpot](connectors-hubspot.md)
+ [Marketo](marketo.md)
+ [Salesforce](salesforce.md)
+ [SAP OData](sapodata.md)
+ [Snowflake](snowflake.md)
+ [Upsolver](upsolver.md)
+ [Zendesk](zendesk.md)
+ [Zoho CRM](connectors-zoho-crm.md)
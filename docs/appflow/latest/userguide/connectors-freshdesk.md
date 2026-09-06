

# Freshdesk connector for Amazon AppFlow
<a name="connectors-freshdesk"></a>

Freshdesk is an online customer service solution. If you're a Freshdesk user, your account contains data about your customer engagements, including agents, conversations, and satisfaction ratings. You can use Amazon AppFlow to transfer data from Freshdesk to certain AWS services or other supported applications.

## Amazon AppFlow support for Freshdesk
<a name="freshdesk-support"></a>

Amazon AppFlow supports Freshdesk as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Freshdesk.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Freshdesk.

## Before you begin
<a name="freshdesk-prereqs"></a>

To use Amazon AppFlow to transfer data from Freshdesk to supported destinations, you must meet these requirements:
+ You have an account with Freshdesk that contains the data that you want to transfer. For more information about the Freshdesk data objects that Amazon AppFlow supports, see [Supported objects](#freshdesk-objects).

Note the following values because you specify them in the connection settings in Amazon AppFlow.
+ The API key from the profile settings of your Freshdesk account. The API key authenticates third-party services like Amazon AppFlow to access your account. For the steps to find the key, see [How to find your API key](https://support.freshdesk.com/en/support/solutions/articles/215517-how-to-find-your-api-key) at the Freshdesk support site.
+ Your Freshdesk address.

## Connecting Amazon AppFlow to your Freshdesk account
<a name="freshdesk-connecting"></a>

To connect Amazon AppFlow to your Freshdesk account, provide your API key and Freshdesk address.

**To connect to Freshdesk**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Freshdesk**.

1. Choose **Create connection**.

1. 

   In the **Connect to Freshdesk** window, enter the following information:
   + **API key** – The API key from your Freshdesk profile settings.
   + **Instance URL** – Your Freshdeskaddress, such as `https:{{my-company-name}}.freshdesk.com`.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Freshdesk as the data source, you can select this connection.

## Transferring data from Freshdesk with a flow
<a name="freshdesk-transfer-data"></a>

To transfer data from Freshdesk, create an Amazon AppFlow flow, and choose Freshdesk as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Freshdesk, see [Supported objects](#freshdesk-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#freshdesk-destinations).

## Supported destinations
<a name="freshdesk-destinations"></a>

When you create a flow that uses Freshdesk as the data source, you can set the destination to any of the following connectors: 
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

## Supported objects
<a name="freshdesk-objects"></a>

When you create a flow that uses Freshdesk as the data source, you can transfer any of the following data objects to supported destinations:



- ** Agent**
  - **** Field**:** Available / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Available Since / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Contact / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Mobile / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Occasional / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Signature / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ticket Scope / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Business Hour**
  - **** Field**:** Business Hour / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Is Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Time Zone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Comment**
  - **** Field**:** Answer / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Forum ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Published / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Spam / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Topic ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Trash / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User ID / **** Data type**:** Long / **** Supported filters**:** 

- ** Company**
  - **** Field**:** Account Tier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Custom Field / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Domain / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Domain / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Health Score / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Industry / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Renewal Date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Contact**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Address / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Company ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Custom Fields / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Job Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Mobile / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Other Companies / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Tag / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Time Zone / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Twitter Id / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Conversation**
  - **** Field**:** Attachment / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Bcc Email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Body / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Body Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Cc Email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** From Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Incoming / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Last Edited At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Edited User ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Private / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Support Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Ticket ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** To Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User ID / **** Data type**:** Long / **** Supported filters**:** 

- ** Email Config**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Group ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Primary Role / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Product Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Reply Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** To Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Email Inbox**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Custom Mailbox / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Default Reply Email / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Forward Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Freshdesk Mailbox / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Group ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Mailbox Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Product ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Support\_Email / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** id / **** Data type**:** Long / **** Supported filters**:** 

- ** Forum**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Forum Category ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Forum Type / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Forum Visibility / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Position / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Posts Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Topics Count / **** Data type**:** Long / **** Supported filters**:** 

- ** Forum Category**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Group**
  - **** Field**:** Auto Ticket Assign / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Business Hour Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Escalate To / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Unassigned For / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Product**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Role**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Default / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Satisfaction Rating**
  - **** Field**:** Agent ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Created\_Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Feedback / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Group ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Rating / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Survey ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Ticket ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Updated\_At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO

- ** Skill**
  - **** Field**:** Agent / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Condtion / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime  / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Match Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Rank / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Solution**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Term / **** Data type**:** String / **** Supported filters**:** CONTAINS
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Survey**
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Question / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 

- ** Ticket**
  - **** Field**:** Agent ID / **** Data type**:** Integer / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Cc Email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO, EQUAL\_TO
  - **** Field**:** Custom Field / **** Data type**:** Map / **** Supported filters**:** 
  - **** Field**:** Due By / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Email Config Id / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Fr Due By / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Fr Escalated / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Fwd Email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Group ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Is Escalated / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Priority / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Product ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Reply Cc Email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Requester ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Responder ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Spam / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Subject / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tag / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** To email / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO

- ** Time Entry**
  - **** Field**:** Agent ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Billable / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Company ID / **** Data type**:** Long / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Executed After / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Executed At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Executed Before / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start Time / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Ticket ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Time Spent / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timer Running / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 

- ** Topic**
  - **** Field**:** Created At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Forum ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Hit / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Locked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Merged Topic ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Post Count / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Published / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Replied At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Replied By / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Stamp Type / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** Sticky / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** User ID / **** Data type**:** Long / **** Supported filters**:** 
  - **** Field**:** User Vote / **** Data type**:** Long / **** Supported filters**:** 


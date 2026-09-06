

# Asana connector for Amazon AppFlow
<a name="connectors-asana"></a>

Asana is a cloud-based team collaboration solution that helps teams organize, plan, and complete tasks and projects. If you're an Asana user, your account contains data about your workspaces, projects, tasks, teams, and more. You can use Amazon AppFlow to transfer data from Asana to certain AWS services or other supported applications.

## Amazon AppFlow support for Asana
<a name="asana-support"></a>

Amazon AppFlow supports Asana as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Asana.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Asana.

## Before you begin
<a name="asana-prereqs"></a>

To use Amazon AppFlow to transfer data from Asana to supported destinations, you must meet these requirements:
+ You have an account with Asana that contains the data that you want to transfer. For more information about the Asana data objects that Amazon AppFlow supports, see [Supported objects](#asana-objects).
+ In your Asana account settings, you've created either of the following resources for Amazon AppFlow. These resources provide credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account.
  + A Developer App, which supports OAuth 2.0 authentication. For information about how to create a Developer App, see [OAuth](https://developers.asana.com/docs/oauth) in the Asana Developers documentation.
  + A personal access token. For more information, see [Personal access token](https://developers.asana.com/docs/personal-access-token) in the Asana Developers documentation.
+ If you created an OAuth app, you've configured it with one or more redirect URLs for Amazon AppFlow.

  Redirect URLs have the following format:

  ```
  https://{{region}}.console.aws.amazon.com/appflow/oauth
  ```

  In this URL, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from Asana. For example, the code for the US East (N. Virginia) Region is `us-east-1`. For that Region, the URL is the following:

  ```
  https://us-east-1.console.aws.amazon.com/appflow/oauth
  ```

  For the AWS Regions that Amazon AppFlow supports, and their codes, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

If you created a Developer App, note the client ID and client secret. If you created a personal access token, note the token value. You provide these values to Amazon AppFlow when you connect to your Asana account.

## Connecting Amazon AppFlow to your Asana account
<a name="asana-connecting"></a>

To connect Amazon AppFlow to your Asana account, provide the client credentials from your Developer App, or provide a personal access token. If you haven't yet configured your Asana account for Amazon AppFlow integration, see [Before you begin](#asana-prereqs).

**To connect to Asana**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Asana**.

1. Choose **Create connection**.

1. In the **Connect to Asana** window, for **Select authentication type**, choose how to authenticate Amazon AppFlow with your Asana account when it requests to access your data:
   + Choose **OAuth2** to authenticate Amazon AppFlow with the client ID and client secret from an Asana Developer App. Then enter values for **Client ID** and **Client secret**.
   + Choose **PAT** to authenticate Amazon AppFlow with a personal access token. Then enter the token value for **Personal access token**.

1. In the **Connect to Asana** window, enter the following information:

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your Asana account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Asana as the data source, you can select this connection.

## Transferring data from Asana with a flow
<a name="asana-transfer-data"></a>

To transfer data from Asana, create an Amazon AppFlow flow, and choose Asana as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Asana, see [Supported objects](#asana-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#asana-destinations).

## Supported destinations
<a name="asana-destinations"></a>

When you create a flow that uses Asana as the data source, you can set the destination to any of the following connectors: 
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
<a name="asana-objects"></a>

When you create a flow that uses Asana as the data source, you can transfer any of the following data objects to supported destinations:



- ** Audit Log Event**
  - **** Field**:** actor / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** actor\_type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** context / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** details / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** event\_category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** event\_type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** resource / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** start\_end\_at / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO

- ** Goal**
  - **** Field**:** current\_status\_update / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** due\_on / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** followers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** html\_notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** is\_workspace\_level / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** liked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** likes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** metric / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** num\_likes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** start\_on / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** team / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** time\_period / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** workspace / **** Data type**:** Struct / **** Supported filters**:** 

- ** Portfolio**
  - **** Field**:** color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created\_by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** current\_status\_update / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** custom\_field\_settings / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** due\_on / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** permalink\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** public / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** start\_on / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** workspace / **** Data type**:** Struct / **** Supported filters**:** 

- ** Project**
  - **** Field**:** archived / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** completed / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** completed\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** completed\_by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** created\_from\_template / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** current\_status / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** current\_status\_update / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** custom\_field\_settings / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** custom\_fields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** default\_view / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** due\_date / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** due\_on / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** followers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** html\_notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** icon / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** is\_template / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** members / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** modified\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** owner / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** permalink\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** public / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** start\_on / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** team / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** workspace / **** Data type**:** Struct / **** Supported filters**:** 

- ** Section**
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** project / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 

- ** Tag**
  - **** Field**:** color / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** followers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** permalink\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** workspace / **** Data type**:** Struct / **** Supported filters**:** 

- ** Task**
  - **** Field**:** approval\_status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** assignee / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** assignee\_section / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** assignee\_status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** completed / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** completed\_at / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** completed\_by / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** completed\_on / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** created\_at / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** custom\_fields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** dependencies / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** dependents / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** due\_at / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** due\_on / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** external / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** followers / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** has\_attachment / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** hearted / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** hearts / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** html\_notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** is\_blocked / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** is\_blocking / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** is\_rendered\_as\_separator / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** is\_subtask / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** liked / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** likes / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** memberships / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** modified\_at / **** Data type**:** DateTime / **** Supported filters**:** LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** modified\_on / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** num\_hearts / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** num\_likes / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** num\_subtasks / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** parent / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** permalink\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** projects / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** resource\_subtype / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** start\_at / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** start\_on / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO, LESS\_THAN\_OR\_EQUAL\_TO, GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** tags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** text / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** workspace / **** Data type**:** Struct / **** Supported filters**:** 

- ** Team**
  - **** Field**:** description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** html\_description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** organization / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** permalink\_url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** visibility / **** Data type**:** String / **** Supported filters**:** 

- ** User**
  - **** Field**:** email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** photo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** workspaces / **** Data type**:** List / **** Supported filters**:** 

- ** Workspace**
  - **** Field**:** email\_domains / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** gid / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** is\_organization / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** resource\_type / **** Data type**:** String / **** Supported filters**:** 




# Facebook Page Insights connector for Amazon AppFlow
<a name="connectors-facebook-page-insights"></a>

Facebook Page Insights provides Facebook Page owners with information about the performance and visitor demographics of their Pages. You can use Amazon AppFlow to transfer data from Facebook Page Insights to certain AWS services or other supported applications.

## Amazon AppFlow support for Facebook Page Insights
<a name="facebook-page-insights-support"></a>

Amazon AppFlow supports Facebook Page Insights as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from Facebook Page Insights.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to Facebook Page Insights.

**Supported API version**  
Amazon AppFlow retrieves your Facebook Page Insights data by sending requests to Graph API v15.0. 

## Before you begin
<a name="facebook-page-insights-prereqs"></a>

To use Amazon AppFlow to transfer data from Facebook Page Insights to supported destinations, you must meet these requirements:
+ You have a Facebook account and one or more Facebook Pages that contain the data that you want to transfer. For more information about the Facebook Page Insights data objects that Amazon AppFlow supports, see [Supported objects](#facebook-page-insights-objects).
+ You have a Meta for Developers account.
+ Your account contains an app with its type set to *Business*. For information about how to create an app, see [Create an App](https://developers.facebook.com/docs/development/create-an-app) in the Meta for Developers App Development documentation.
+ Your Meta for Developers app includes the *Facebook Login* product, and you've configured this product to meet the following additional requirements:
  + Client OAuth login is enabled.
  + Web OAuth login is enabled.
  + One or more OAuth redirect URIs are present for Amazon AppFlow. Each of these URIs has the following form:

    `https://{{region}}.console.aws.amazon.com/appflow/oauth`

    In this URI, *region* is the code for the AWS Region where you use Amazon AppFlow to transfer data from the Marketing API. For example, if you use Amazon AppFlow in the US East (N. Virginia) region, the URI is `https://us-east-1.console.aws.amazon.com/appflow/oauth`.

    For the AWS Regions that Amazon AppFlow supports, see [Amazon AppFlow endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/appflow.html) in the *AWS General Reference.*

  For more information about Facebook Login, see [Facebook Login](https://developers.facebook.com/docs/facebook-login) in the Meta For Developers documentation.
+ In the Data Use Checkup settings for your app, you've activated the public\_profile and email permissions. For the steps to configure Data Use Checkup settings, see [Data Use Checkup](https://developers.facebook.com/docs/development/maintaining-data-access/data-use-checkup/) in the Meta for Developers App Development documentation.
+ You've configured your app with the following permissions:
  + `ads_management`
  + `ads_read`
  + `page_events`
  + `pages_manage_ads`
  + `pages_manage_cta`
  + `pages_manage_engagement`
  + `pages_manage_instant_articles`
  + `pages_manage_metadata`
  + `pages_manage_posts`
  + `pages_read_engagement`
  + `pages_read_user_content`
  + `pages_show_list`
  + `public_profile`
  + `read_insights`

  For more information about these permissions, see [Permissions Reference](https://developers.facebook.com/docs/permissions/reference) in the Meta for Developers Graph API documentation.

From the settings for your app, note the app ID and app secret. You provide these values to Amazon AppFlow in the connection settings.

## Connecting Amazon AppFlow to your Facebook Page Insights account
<a name="facebook-page-insights-connecting"></a>

To connect Amazon AppFlow to your Facebook account, provide the app credentials from your Meta for Developers app so that Amazon AppFlow can access your data. If you haven't yet configured an app for Amazon AppFlow integration, see [Before you begin](#facebook-page-insights-prereqs).

**To connect to Facebook Page Insights**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **Facebook Page Insights**.

1. Choose **Create connection**.

1. In the **Connect to Facebook Page Insights** window, enter the following information:
   + **Client ID** – The app ID from your Meta for Developers app.
   + **Client secret** – The app secret from your Meta for Developers app.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your Facebook account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses Facebook Page Insights as the data source, you can select this connection.

## Transferring data from Facebook Page Insights with a flow
<a name="facebook-page-insights-transfer-data"></a>

To transfer data from Facebook Page Insights, create an Amazon AppFlow flow, and choose Facebook Page Insights as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for Facebook Page Insights, see [Supported objects](#facebook-page-insights-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#facebook-page-insights-destinations).

## Supported destinations
<a name="facebook-page-insights-destinations"></a>

When you create a flow that uses Facebook Page Insights as the data source, you can set the destination to any of the following connectors: 
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
<a name="facebook-page-insights-objects"></a>

When you create a flow that uses Facebook Page Insights as the data source, you can transfer any of the following data objects to supported destinations:



- ** Feed**
  - **** Field**:** Created Time / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Message / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Story / **** Data type**:** String / **** Supported filters**:** 

- ** Page**
  - **** Field**:** Category / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Category List / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Task / **** Data type**:** List / **** Supported filters**:** 

- ** Page CTA Click**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Content**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Engagement**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Impression**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Post**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Post Engagement**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Post Impression**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Post Reaction**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Reaction**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page User Demographics**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Video Post**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page Video View**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Page View**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 

- ** Story**
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Period / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Since / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Value / **** Data type**:** List / **** Supported filters**:** 


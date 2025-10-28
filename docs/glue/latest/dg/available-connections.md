# Available connections

AWS Glue supports the following connection types:

- Adobe Analytics
- Adobe Marketo Engage
- Amazon Aurora (supported if the native JDBC driver is being used. Not all driver features can be leveraged)
- Amazon DocumentDB
- Amazon DynamoDB
- Amazon OpenSearch Service, for use with AWS Glue for Spark.
- Amazon Redshift
- Asana
- Azure Cosmos, for use of Azure Cosmos DB for NoSQL with AWS Glue ETL jobs
- Azure SQL, for use with AWS Glue for Spark.
- Blackbaud
- CircleCI
- Datadog
- Docusign Monitor
- Domo
- Dynatrace
- Facebook Ads
- Facebook Page Insights
- Freshdesk
- Freshsales
- Google Ads
- Google Analytics 4
- Google BigQuery, for use with AWS Glue for Spark.
- Google Search Console
- Google Sheets
- HubSpot
- Instagram Ads
- Intercom
- JDBC
- Jira Cloud
- Kafka
- Kustomer
- LinkedIn
- Mailchimp
- Microsoft Dynamics 365 CRM
- Microsoft Teams
- Mixpanel
- Monday
- MongoDB
- MongoDB Atlas
- Okta
- Oracle NetSuite
- Paypal
- Pendo
- Pipedrive
- Productboard
- QuickBooks
- Salesforce
- Salesforce Commerce Cloud
- Salesforce Marketing Cloud
- Salesforce Marketing Cloud Account Engagement (previously Salesforce Pardot)
- SAP HANA, for use with AWS Glue for Spark.
- SAP OData
- SendGrid
- ServiceNow
- Slack
- Smartsheet
- Snapchat Ads
- Stripe
- Snowflake, for use with AWS Glue for Spark.
- Teradata Vantage, when using AWS Glue for Spark.
- Twilio
- Vertica, for use with AWS Glue for Spark.
- WooCommerce
- Zendesk
- Zoho CRM
- Zoom Meetings
- Various Amazon Relational Database Service (Amazon RDS) offerings.
- Network (designates a connection to a data source that is in an Amazon Virtual
  Private Cloud (Amazon VPC))
  With AWS Glue Studio, you can also create a connection for a _connector_. A connector is an optional code package that assists with
  accessing data stores in AWS Glue Studio. For more information, see [Using connectors and connections with
  AWS Glue Studio](../ug/connectors-chapter.md "../ug/connectors-chapter.md")

For information about how to connect to on-premises databases, see [How to access and analyze on-premises data stores using
AWS Glue](https://aws.amazon.com/blogs/big-data/how-to-access-and-analyze-on-premises-data-stores-using-aws-glue/ "https://aws.amazon.com/blogs/big-data/how-to-access-and-analyze-on-premises-data-stores-using-aws-glue/") at the AWS Big Data Blog website.

To create a connection with VPC configuration while using a custom IAM role, it must have the following VPC access actions:

- secretsmanager:GetSecretValue
- secretsmanager:PutSecretValue
- secretsmanager:DescribeSecret
- ec2:CreateNetworkInterface
- ec2:DeleteNetworkInterface
- ec2:DescribeNetworkInterfaces
- ec2:DescribeSubnets

## Limitations

- You can't edit connections through the AWS Glue console if you created a v2 connection using AWS Glue APIs:
  - Amazon DocumentDB
  - Amazon Aurora
  - MariaDB
  - MongoDB Atlas
  - MongoDB

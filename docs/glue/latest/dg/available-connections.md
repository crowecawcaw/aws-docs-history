

# Available connections
<a name="available-connections"></a>

AWS Glue supports the following connection types:
+ Adobe Analytics
+ Adobe Marketo Engage
+ Adyen
+ Airship
+ Amazon Aurora (supported if the native JDBC driver is being used. Not all driver features can be leveraged)
+ Amazon DocumentDB
+ Amazon DynamoDB
+ Amazon OpenSearch Service, for use with AWS Glue for Spark.
+ Amazon Redshift
+ Amplitude
+ Amplitude Experiment
+ Anthropic
+ Apollo
+ Asana
+ Attio
+ Avalara
+ Azure Cosmos, for use of Azure Cosmos DB for NoSQL with AWS Glue ETL jobs
+ Azure SQL, for use with AWS Glue for Spark.
+ BambooHR
+ Bitbucket
+ Blackbaud
+ Brevo
+ Brex
+ BugSnag
+ Calendly
+ Chargebee
+ Checkout.com
+ CircleCI
+ ClickUp
+ Close CRM
+ Coalesce
+ Coda
+ Constant Contact
+ Contentful
+ Copper
+ Crisp
+ Datadog
+ dbt Cloud
+ DevRev
+ Docusign Monitor
+ Domo
+ Dynatrace
+ Facebook Ads
+ Facebook Page Insights
+ Finch
+ FireHydrant
+ Fivetran
+ Folk
+ Freshdesk
+ Freshsales
+ Front
+ Fullstory
+ GetResponse
+ Ghost
+ GoCardless
+ Google Ads
+ Google Analytics 4
+ Google BigQuery, for use with AWS Glue for Spark.
+ Google Search Console
+ Google Sheets
+ Gorgias
+ Grafana
+ Gusto
+ Harness
+ Hex
+ Honeycomb
+ HubSpot
+ Insightly
+ Instagram Ads
+ Intercom
+ JDBC
+ Jenkins
+ Jira Cloud
+ Kafka
+ Kameleoon
+ Klaviyo
+ Kommo
+ Kustomer
+ LaunchDarkly
+ Lemon Squeezy
+ LinkedIn
+ LiveChatAI
+ LogRocket
+ mabl
+ Mailchimp
+ Maxio
+ Microsoft Dynamics 365 CRM
+ Microsoft Teams
+ Miro
+ Mixpanel
+ Mollie
+ Monday
+ MongoDB
+ MongoDB Atlas
+ Network (designates a connection to a data source that is in an Amazon Virtual Private Cloud (Amazon VPC))
+ New Relic
+ Nimble
+ Nuclino
+ Octopus Deploy
+ Okta
+ Omnisend
+ Ontraport
+ Oracle NetSuite
+ Paddle
+ PagerDuty
+ Paypal
+ Pendo
+ Persona
+ Pinecone
+ Pipedrive
+ Pipeliner
+ Port
+ Postman
+ Productboard
+ QuickBooks
+ Re:amaze
+ Recurly
+ REST API (requires connection type setup, see [REST API Connections](https://docs.aws.amazon.com/glue/latest/dg/rest-api-connections.html))
+ Rho
+ Rollbar
+ Rootly
+ RudderStack
+ Salesforce
+ Salesforce Commerce Cloud
+ Salesforce Marketing Cloud
+ Salesforce Marketing Cloud Account Engagement (previously Salesforce Pardot)
+ SAP HANA, for use with AWS Glue for Spark.
+ SAP OData
+ Sender
+ SendGrid
+ Sentry
+ ServiceNow
+ ShipBob
+ Shortcut
+ Slack
+ Smartlook
+ Smartsheet
+ Snapchat Ads
+ Snowflake, for use with AWS Glue for Spark.
+ SonarCloud
+ Square
+ Statuspage
+ Streak
+ Stripe
+ Tableau
+ Teamwork
+ Teradata Vantage, when using AWS Glue for Spark.
+ TestRail
+ Todoist
+ Trello
+ Twenty CRM
+ Twilio
+ Typeform
+ Various Amazon Relational Database Service (Amazon RDS) offerings.
+ Vercel
+ Vertica, for use with AWS Glue for Spark.
+ Vonage
+ VWO
+ Weaviate
+ Webex
+ Webflow
+ WooCommerce
+ Workday Live Data Query
+ Xero
+ Zendesk
+ Zoho Books
+ Zoho CRM
+ Zoho Desk
+ Zoho Invoice
+ Zoom Meetings
+ Zuora

With AWS Glue Studio, you can also create a connection for a *connector*. A connector is an optional code package that assists with accessing data stores in AWS Glue Studio. For more information, see [Using connectors and connections with AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html) 

For information about how to connect to on-premises databases, see [How to access and analyze on-premises data stores using AWS Glue](https://aws.amazon.com/blogs/big-data/how-to-access-and-analyze-on-premises-data-stores-using-aws-glue/) at the AWS Big Data Blog website.

To create a connection with VPC configuration while using a custom IAM role, it must have the following VPC access actions:
+ secretsmanager:GetSecretValue
+ secretsmanager:PutSecretValue
+ secretsmanager:DescribeSecret
+ ec2:CreateNetworkInterface
+ ec2:DeleteNetworkInterface
+ ec2:DescribeNetworkInterfaces
+ ec2:DescribeSubnets

## Limitations
<a name="available-connections-limitations"></a>
+  You can't edit connections through the AWS Glue console if you created a v2 connection using AWS Glue APIs: 
  + Amazon DocumentDB
  + Amazon Aurora
  + MariaDB
  + MongoDB Atlas
  + MongoDB
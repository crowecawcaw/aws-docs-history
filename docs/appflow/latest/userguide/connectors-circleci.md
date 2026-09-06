

# CircleCI connector for Amazon AppFlow
<a name="connectors-circleci"></a>

CircleCI is a continuous integration and continuous delivery platform. If you're a CircleCI user, your account contains data about your projects, pipelines, workflows, and more. You can use Amazon AppFlow to transfer data from CircleCI to certain AWS services or other supported applications.

## Amazon AppFlow support for CircleCI
<a name="circleci-support"></a>

Amazon AppFlow supports CircleCI as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from CircleCI.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to CircleCI.

## Before you begin
<a name="circleci-prereqs"></a>

To use Amazon AppFlow to transfer data from CircleCI to supported destinations, you must meet these requirements:
+ You have an account with CircleCI that contains the data that you want to transfer. For more information about the CircleCI data objects that Amazon AppFlow supports, see [Supported objects](#circleci-objects).
+ In the user settings for your account, you've created a personal API token. For the steps to do this, see [Creating a personal API token](https://circleci.com/docs/managing-api-tokens/?utm_source=google&utm_medium=sem&utm_campaign=sem-google-dg--uscan-en-dsa-maxConv-auth-nb&utm_term=g_-_c__dsa_&utm_content=&gclid=Cj0KCQiA4OybBhCzARIsAIcfn9lS-1gBgq0NRzEsA_b20-dhUG8aEHQqIu9wdXFEhSfg0kHsXEhufi8aAtPGEALw_wcB#creating-a-personal-api-token) in the CircleCI Docs site.

You provide the personal API token to Amazon AppFlow in the settings for your CircleCI connection.

## Connecting Amazon AppFlow to your CircleCI account
<a name="circleci-connecting"></a>

To connect Amazon AppFlow to your CircleCI account, provide your personal API token so that Amazon AppFlow can access your data. If you haven't yet configured your CircleCI account for Amazon AppFlow integration, see [Before you begin](#circleci-prereqs).

**To connect to CircleCI**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **CircleCI**.

1. Choose **Create connection**.

1. In the **Connect to CircleCI** window, for **CircleCI Token**, enter the personal API token from the user settings of your CircleCI account

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses CircleCI as the data source, you can select this connection.

## Transferring data from CircleCI with a flow
<a name="circleci-transfer-data"></a>



To transfer data from CircleCI, create an Amazon AppFlow flow, and choose CircleCI as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for CircleCI, see [Supported objects](#circleci-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#circleci-destinations).

## Supported destinations
<a name="circleci-destinations"></a>

When you create a flow that uses CircleCI as the data source, you can set the destination to any of the following connectors: 
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
<a name="circleci-objects"></a>

When you create a flow that uses CircleCI as the data source, you can transfer any of the following data objects to supported destinations:



- ** Context**
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Owner Type / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Organization Summary Metric**
  - **** Field**:** All Projects / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Org Data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Org Project Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Project Names / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Reporting Window / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Pipeline**
  - **** Field**:** Branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Errors / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Project Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Trigger / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Trigger Parameters / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** VCS / **** Data type**:** Struct / **** Supported filters**:** 

- ** Pipeline Workflow**
  - **** Field**:** Canceled By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Errored By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pipeline ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pipeline Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Project Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Started By / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stopped At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tag / **** Data type**:** String / **** Supported filters**:** 

- ** Project Branch**
  - **** Field**:** Branches / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Org ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Project ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Workflow Name / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Project Flaky Test**
  - **** Field**:** Classname / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** File / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Job Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Job Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Pipeline Number / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Test Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Time Wasted / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Times Flaked / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Workflow Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Workflow ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Workflow Name / **** Data type**:** String / **** Supported filters**:** 

- ** Project Summary Metric**
  - **** Field**:** All Branches / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** All Workflows / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Branches / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Organization ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Project Data / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Project ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Project Workflow Branch Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Project Workflow Data / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Reporting Window / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Workflow Names / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Schedule**
  - **** Field**:** Actor / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Parameters / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Project Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Timetable / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Updated At / **** Data type**:** String / **** Supported filters**:** 

- ** Workflow Job Timeseries**
  - **** Field**:** Branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Granularity / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Max Ended At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Metrics / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Min Started At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Start End Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN
  - **** Field**:** Timestamp / **** Data type**:** String / **** Supported filters**:** 

- ** Workflow Metric and Trend**
  - **** Field**:** All Branches / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Branches / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Metrics / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Trends / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Workflow Names / **** Data type**:** List / **** Supported filters**:** 

- ** Workflow Recent Run**
  - **** Field**:** All Branches / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Created At / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Credits Used / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Duration / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Approval / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Start End Date / **** Data type**:** DateTime / **** Supported filters**:** EQUAL\_TO, BETWEEN
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Stopped At / **** Data type**:** String / **** Supported filters**:** 

- ** Workflow Summary Metric**
  - **** Field**:** All Branches / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Metrics / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Project ID / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Reporting Window / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Window End / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Window Start / **** Data type**:** String / **** Supported filters**:** 

- ** Workflow Test Metric**
  - **** Field**:** Average Test Count / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Branch / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Most Failed Tests / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Most Failed Tests Extra / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Slowest Tests / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Slowest Tests Extra / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Test Runs / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Total Test Runs / **** Data type**:** Integer / **** Supported filters**:** 


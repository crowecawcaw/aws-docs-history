

# BambooHR connector for Amazon AppFlow
<a name="connectors-bamboohr"></a>

BambooHR is a human resources software as a service (SaaS) solution. If you’re a BambooHR user, your account contains data on employees and applicants, such as employee information, benefits, vacation time, openings, reports, files, and more. You can use Amazon AppFlow to transfer data from BambooHR to certain AWS services or other supported applications. 



## Amazon AppFlow support for BambooHR
<a name="bamboohr-support"></a>

Amazon AppFlow supports BambooHR as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from BambooHR.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to BambooHR.

## Before you begin
<a name="bamboohr-prereqs"></a>

To use Amazon AppFlow to transfer data from BambooHR to supported destinations, you must meet these requirements:
+ You have an account with BambooHR that contains the data that you want to transfer. For more information about the BambooHR data objects that Amazon AppFlow supports, see [Supported objects](#bamboohr-objects).
+ In the API keys settings for your account, you've created an API key for Amazon AppFlow. Amazon AppFlow uses the API key to make authenticated calls to your account and securely access your data. For more information, see [Authentication](https://documentation.bamboohr.com/docs#authentication) in the BambooHR documentation.

Note the value of your API key. When you connect to your BambooHR account, you provide this value to Amazon AppFlow.

## Connecting Amazon AppFlow to your BambooHR account
<a name="bamboohr-connecting"></a>

To connect Amazon AppFlow to your BambooHR account, provide details from your BambooHR project so that Amazon AppFlow can access your data. If you haven't yet configured your BambooHR project for Amazon AppFlow integration, see [Before you begin](#bamboohr-prereqs).

**To connect to BambooHR**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **BambooHR**.

1. Choose **Create connection**.

1. In the **Connect to BambooHR** window, enter the following information:
   + **API key** – Enter your API key.
   + **Instance URL** – The URL of the instance where you want to run the operation, for example, https://api.bamboohr.com/api/gateway.php/amazonawstest.
   + **Zone (Optional)** – The time zone that you access Amazon AppFlow from.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your BambooHR account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses BambooHR as the data source, you can select this connection.

## Transferring data from BambooHR with a flow
<a name="bamboohr-transfer-data"></a>

To transfer data from BambooHR, create an Amazon AppFlow flow, and choose BambooHR as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for BambooHR, see [Supported objects](#bamboohr-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#bamboohr-destinations).

## Supported destinations
<a name="bamboohr-destinations"></a>

When you create a flow that uses BambooHR as the data source, you can set the destination to any of the following connectors: 
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
<a name="bamboohr-objects"></a>

When you create a flow that uses BambooHR as the data source, you can transfer any of the following data objects to supported destinations:



- ** Company Files**
  - **** Field**:** Company Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** can Upload Files / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** files / **** Data type**:** List / **** Supported filters**:** 

- ** Deduction types**
  - **** Field**:** Additional Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Allowable Benefit Types / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Can BeCollected By Trax / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Deduction Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Deduction Note Link / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Deduction Note Link Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Deduction Type Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Default Deduction Code / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Hide Annual Max / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Managed Deduction Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Non Benefit Deduction Type / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Sub Type Text / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sub Types / **** Data type**:** List / **** Supported filters**:** 

- ** Employee Dependents**
  - **** Field**:** Address Line 1 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Address Line 2 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** City / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Date Of Birth / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Employee Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gender / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Home Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Student / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Is Us Citizen / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Masked SIN / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Masked SSN / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Middle Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Relationship / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** State / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Zip Code / **** Data type**:** String / **** Supported filters**:** 

- ** Employees**
  - **** Field**:** Can Upload Photo / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Department / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Display Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Division / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Employee photo url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ID / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Instagram / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Job Title / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Last Changed / **** Data type**:** DateTime / **** Supported filters**:** GREATER\_THAN\_OR\_EQUAL\_TO
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LinkedIn / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Location / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Manager / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mobile Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Photo Uploaded / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Preferred Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Pronouns / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Work Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Work Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Work Phone Extension / **** Data type**:** String / **** Supported filters**:** 

- ** Training Type**
  - **** Field**:** Category / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Due From Hire Date / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Frequency / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Link Url / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Renewable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Required / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Training Type / **** Data type**:** String / **** Supported filters**:** 

- ** Users**
  - **** Field**:** Email / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Employee Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** First Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** Last Login / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Last Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Status / **** Data type**:** String / **** Supported filters**:** 


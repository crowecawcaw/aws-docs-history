

# QuickBooks Online connector for Amazon AppFlow
<a name="connectors-quickbooks-online"></a>

QuickBooks Online is a cloud-based accounting solution for businesses. If you're a QuickBooks Online user, your account contains data about your accounts, customers, invoices, and more. You can use Amazon AppFlow to transfer data from QuickBooks Online to certain AWS services or other supported applications.

## Amazon AppFlow support for QuickBooks Online
<a name="quickbooks-online-support"></a>

Amazon AppFlow supports QuickBooks Online as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from QuickBooks Online.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to QuickBooks Online.

## Before you begin
<a name="quickbooks-online-prereqs"></a>

To use Amazon AppFlow to transfer data from QuickBooks Online to supported destinations, you must meet these requirements:
+ You have an account with QuickBooks Online that contains the data that you want to transfer. For more information about the QuickBooks Online data objects that Amazon AppFlow supports, see [Supported objects](#quickbooks-online-objects).
+ In your Intuit developer account, you've created an app for Amazon AppFlow. This app provides the client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated calls to your account. For the steps to create an app, see [Create and start developing your app](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app) in the Intuit Developer documentation.
+ You've configured your app to permit the `com.intuit.quickbooks.accounting` scope.

Note the following values because you specify them in the connection settings in Amazon AppFlow.
+ The client ID and client secret from your app settings.
+ The company ID from your QuickBooks Online account settings.

## Connecting Amazon AppFlow to your QuickBooks Online account
<a name="quickbooks-online-connecting"></a>

To connect Amazon AppFlow to your QuickBooks Online account, provide details from your app so that Amazon AppFlow can access your data. If you haven't yet configured your QuickBooks Online account for Amazon AppFlow integration, see [Before you begin](#quickbooks-online-prereqs).

**To connect to QuickBooks Online**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **QuickBooks Online**.

1. Choose **Create connection**.

1. In the **Connect to QuickBooks Online** window, enter the following information:
   + **Client ID** – The client ID from your app settings.
   + **Client secret** – The client secret from your app settings.
   + **Instance URL** – The endpoint where Amazon AppFlow sends requests to access your data. Choose one of the following:
     + **https://sandbox-quickbooks.api.intuit.com** – The base URL for the QuickBooks Online development environment. For more information about this environment and the data that it contains, see [Create and test with a sandbox company](https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/manage-your-sandboxes) in the Intuit Developer documentation.
     + **https://quickbooks.api.intuit.com** – The base URL for the QuickBooks Online production environment.
   + **QuickBooks CompanyId** – The company ID from your QuickBooks Online account settings.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Continue**.

1. In the window that appears, sign in to your Intuit account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses QuickBooks Online as the data source, you can select this connection.

## Transferring data from QuickBooks Online with a flow
<a name="quickbooks-online-transfer-data"></a>



To transfer data from QuickBooks Online, create an Amazon AppFlow flow, and choose QuickBooks Online as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for QuickBooks Online, see [Supported objects](#quickbooks-online-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#quickbooks-online-destinations).

## Supported destinations
<a name="quickbooks-online-destinations"></a>

When you create a flow that uses QuickBooks Online as the data source, you can set the destination to any of the following connectors: 
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
<a name="quickbooks-online-objects"></a>

When you create a flow that uses QuickBooks Online as the data source, you can transfer any of the following data objects to supported destinations:



- ** Account**
  - **** Field**:** AccountAlias / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** AccountSubType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** AccountType / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** AcctNum / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Classification / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CurrentBalance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** CurrentBalanceWithSubAccounts / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** FullyQualifiedName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ParentRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SubAccount / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxCodeRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** TxnLocationType / **** Data type**:** String / **** Supported filters**:** 

- ** Bill**
  - **** Field**:** APAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Balance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DepartmentRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DocNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DueDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** ExchangeRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** GlobalTaxCalculation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** HomeBalance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** IncludeInAnnualTPAR / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** LinkedTxn / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrivateNote / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** RecurDataRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SalesTermRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TotalAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** TransactionLocationType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TxnDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** TxnTaxDetail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** VendorRef / **** Data type**:** Struct / **** Supported filters**:** 

- ** Company Info**
  - **** Field**:** CompanyAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CompanyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CompanyStartDate / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Country / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CustomerCommunicationAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Email / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** FiscalYearStartMonth / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** LegalAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** LegalName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** NameValue / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryPhone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SupportedLanguages / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** WebAddr / **** Data type**:** Struct / **** Supported filters**:** 

- ** Customer**
  - **** Field**:** ARAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** AlternatePhone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Balance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** BalanceWithJobs / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** BillAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** BillWithParent / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** BusinessNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CompanyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomerTypeRef / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DefaultTaxCodeRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DisplayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** FamilyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fax / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** FullyQualifiedName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GSTIN / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GSTRegistrationType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GivenName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** IsProject / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Job / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Level / **** Data type**:** BigInteger / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MiddleName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mobile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Notes / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OpenBalanceDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** ParentRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PaymentMethodRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PreferredDeliveryMethod / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PrimaryEmailAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryPhone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryTaxIdentifier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PrintOnCheckName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ResaleNum / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SalesTermRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SecondaryTaxIdentifier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ShipAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxExemptionReasonId / **** Data type**:** BigInteger / **** Supported filters**:** 
  - **** Field**:** Taxable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** WebAddr / **** Data type**:** Struct / **** Supported filters**:** 

- ** Employee**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** BillRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** BillableTime / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** BirthDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** CostRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** DisplayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** EmployeeNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** FamilyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Gender / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GivenName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HiredDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MiddleName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mobile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Organization / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** PrimaryAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryEmailAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryPhone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrintOnCheckName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ReleasedDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** SSN / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** V4IDPseudonym / **** Data type**:** String / **** Supported filters**:** 

- ** Estimate**
  - **** Field**:** AcceptedBy / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** AcceptedDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** ApplyTaxAfterDiscount / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** BillAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** BillEmail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ClassRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomField / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomerMemo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomerRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DepartmentRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DocNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DueDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** EmailStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ExchangeRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** ExpirationDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** FreeFormAddress / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** GlobalTaxCalculation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** HomeTotalAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** LinkedTxn / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrintStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PrivateNote / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** RecurDataRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SalesTermRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ShipAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ShipDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** ShipFromAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ShipMethodRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxExemptionRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** TotalAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** TransactionLocationType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TxnDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** TxnStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TxnTaxDetail / **** Data type**:** Struct / **** Supported filters**:** 

- ** Invoice**
  - **** Field**:** AllowOnlineACHPayment / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** AllowOnlineCreditCardPayment / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ApplyTaxAfterDiscount / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Balance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** BillAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** BillEmail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** BillEmailBcc / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** BillEmailCc / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ClassRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomField / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomerMemo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomerRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DeliveryInfo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DepartmentRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Deposit / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** DepositToAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DocNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DueDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** EmailStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ExchangeRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** FreeFormAddress / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** GlobalTaxCalculation / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** HomeBalance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** HomeTotalAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** InvoiceLink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** LinkedTxn / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrintStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PrivateNote / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** RecurDataRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SalesTermRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ShipAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ShipDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** ShipFromAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ShipMethodRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxExemptionRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** TotalAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** TrackingNum / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TransactionLocationType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TxnDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** TxnSource / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TxnTaxDetail / **** Data type**:** Struct / **** Supported filters**:** 

- ** Item**
  - **** Field**:** AbatementRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** AssetAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ClassRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Description / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ExpenseAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** FullyQualifiedName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** IncomeAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** InvStartDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** ItemCategoryType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Level / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ParentRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrefVendorRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PurchaseCost / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** PurchaseDesc / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PurchaseTaxCodeRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PurchaseTaxIncluded / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** QtyOnHand / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** ReorderPoint / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** ReverseChargeRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** SalesTaxCodeRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SalesTaxIncluded / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ServiceType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Sku / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SubItem / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxClassificationRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Taxable / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** TrackQtyOnHand / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Type / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UQCDisplayText / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UQCId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UnitPrice / **** Data type**:** BigDecimal / **** Supported filters**:** 

- ** Payment**
  - **** Field**:** ARAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CreditCardPayment / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CustomerRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DepositToAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ExchangeRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** Line / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PaymentMethodRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PaymentRefNum / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PrivateNote / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxExemptionRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** TotalAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** TransactionLocationType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TxnDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** TxnSource / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UnappliedAmt / **** Data type**:** BigDecimal / **** Supported filters**:** 

- ** Preference**
  - **** Field**:** AccountingInfoPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** EmailMessagesPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** OtherPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ProductAndServicesPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** ReportPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SalesFormsPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** TimeTrackingPrefs / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** VendorAndPurchasesPrefs / **** Data type**:** Struct / **** Supported filters**:** 

- ** Profit And Loss**
  - **** Field**:** Accounting Method / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Adjusted Gain Loss / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Class / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Columns / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Customer / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Date Macro / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Department / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** End Date / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Header / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Item / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Rows / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Sort Order / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Start Date / **** Data type**:** Date / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Summarize Column By / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** Vendor / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** qzurl / **** Data type**:** String / **** Supported filters**:** EQUAL\_TO

- ** Tax Agency**
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** DisplayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastFileDate / **** Data type**:** Date / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxAgencyConfig / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxRegistrationNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxTrackedOnPurchases / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** TaxTrackedOnSales / **** Data type**:** Boolean / **** Supported filters**:** 

- ** Vendor**
  - **** Field**:** APAccountRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** AcctNum / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** EQUAL\_TO
  - **** Field**:** AlternatePhone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Balance / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** BillAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** BillRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** BusinessNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CompanyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CostRate / **** Data type**:** BigDecimal / **** Supported filters**:** 
  - **** Field**:** CreateTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CurrencyRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** DisplayName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** FamilyName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Fax / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** GSTIN / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GSTRegistrationType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** GivenName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** HasTPAR / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastUpdatedTime / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** MetaData / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** MiddleName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Mobile / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** OtherContactInfo / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryEmailAddr / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrimaryPhone / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** PrintOnCheckName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Suffix / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SyncToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** T4AEligible / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** T5018Eligible / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** TaxIdentifier / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TaxReportingBasis / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TermRef / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Vendor1099 / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** VendorPaymentBankDetail / **** Data type**:** Struct / **** Supported filters**:** 
  - **** Field**:** WebAddr / **** Data type**:** Struct / **** Supported filters**:** 


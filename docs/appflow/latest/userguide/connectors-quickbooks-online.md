# QuickBooks Online connector for Amazon AppFlow

QuickBooks Online is a cloud-based accounting solution for businesses. If you're a
QuickBooks Online user, your account contains data about your accounts, customers, invoices, and
more. You can use Amazon AppFlow to transfer data from
QuickBooks Online to certain AWS services or other supported applications.

## Amazon AppFlow support for QuickBooks Online

Amazon AppFlow supports QuickBooks Online as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from QuickBooks Online.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to QuickBooks Online.

## Before you begin

To use Amazon AppFlow to transfer data from QuickBooks Online to supported destinations, you must meet these
requirements:

- You have an account with QuickBooks Online that contains the data that you want to transfer. For more
  information about the QuickBooks Online data objects that Amazon AppFlow supports, see [Supported objects](#quickbooks-online-objects "#quickbooks-online-objects").
- In your Intuit developer account, you've created an app for Amazon AppFlow. This app provides the
  client credentials that Amazon AppFlow uses to access your data securely when it makes authenticated
  calls to your account. For the steps to create an app, see [Create and start developing your app](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app "https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app") in the Intuit Developer documentation.
- You've configured your app to permit the `com.intuit.quickbooks.accounting`
  scope.

Note the following values because you specify them in the connection settings in
Amazon AppFlow.

- The client ID and client secret from your app settings.
- The company ID from your QuickBooks Online account settings.

## Connecting Amazon AppFlow to your QuickBooks Online account

To connect Amazon AppFlow to your QuickBooks Online account, provide details from your app so that
Amazon AppFlow can access your data. If you haven't yet configured your QuickBooks Online account for
Amazon AppFlow integration, see [Before you begin](#quickbooks-online-prereqs "#quickbooks-online-prereqs").

###### To connect to QuickBooks Online

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **QuickBooks Online**.
4. Choose **Create connection**.
5. In the **Connect to QuickBooks Online** window, enter the following
   information:
   - **Client ID** – The client ID from your app settings.
   - **Client secret** – The client secret from your app
     settings.
   - **Instance URL** – The endpoint where Amazon AppFlow sends requests to
     access your data. Choose one of the following:
     - **https://sandbox-quickbooks.api.intuit.com** – The base URL
       for the QuickBooks Online development environment. For more information about this
       environment and the data that it contains, see [Create and test with a sandbox company](https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/manage-your-sandboxes "https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/manage-your-sandboxes") in the Intuit Developer
       documentation.
     - **https://quickbooks.api.intuit.com** – The base URL for the
       QuickBooks Online production environment.

   - **QuickBooks CompanyId** – The company ID from your
     QuickBooks Online account settings.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Continue**. 9. In the window that appears, sign in to your Intuit account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses QuickBooks Online as the data source, you can select this connection.

## Transferring data from QuickBooks Online with a flow

To transfer data from QuickBooks Online, create an Amazon AppFlow flow, and choose QuickBooks Online as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for QuickBooks Online, see [Supported objects](#quickbooks-online-objects "#quickbooks-online-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#quickbooks-online-destinations "#quickbooks-online-destinations").

## Supported destinations

When you create a flow that uses QuickBooks Online as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses QuickBooks Online as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                    | **Field**             | **Data type** | **Supported filters** |
| ----------------------------- | --------------------- | ------------- | --------------------- |
| Account                       | AccountAlias          | String        |                       |
| AccountSubType                | String                |               |
| AccountType                   | Struct                |               |
| AcctNum                       | String                |               |
| Active                        | Boolean               | EQUAL_TO      |
| Classification                | String                |               |
| CreateTime                    | DateTime              |               |
| CurrencyRef                   | Struct                |               |
| CurrentBalance                | BigDecimal            |               |
| CurrentBalanceWithSubAccounts | BigDecimal            |               |
| Description                   | String                |               |
| FullyQualifiedName            | String                |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| Name                          | String                |               |
| ParentRef                     | Struct                |               |
| SubAccount                    | Boolean               | EQUAL_TO      |
| SyncToken                     | String                |               |
| TaxCodeRef                    | Struct                |               |
| TxnLocationType               | String                |               |
| Bill                          | APAccountRef          | Struct        |                       |
| Balance                       | BigDecimal            |               |
| CreateTime                    | DateTime              |               |
| CurrencyRef                   | Struct                |               |
| DepartmentRef                 | Struct                |               |
| DocNumber                     | String                |               |
| DueDate                       | Date                  |               |
| ExchangeRate                  | BigDecimal            |               |
| GlobalTaxCalculation          | Struct                |               |
| HomeBalance                   | BigDecimal            |               |
| Id                            | String                |               |
| IncludeInAnnualTPAR           | Boolean               |               |
| LastUpdatedTime               | DateTime              |               |
| Line                          | Struct                |               |
| LinkedTxn                     | Struct                |               |
| MetaData                      | Struct                |               |
| PrivateNote                   | String                |               |
| RecurDataRef                  | Struct                |               |
| SalesTermRef                  | Struct                |               |
| SyncToken                     | String                |               |
| TotalAmt                      | BigDecimal            |               |
| TransactionLocationType       | String                |               |
| TxnDate                       | Date                  |               |
| TxnTaxDetail                  | Struct                |               |
| VendorRef                     | Struct                |               |
| Company Info                  | CompanyAddr           | Struct        |                       |
| CompanyName                   | String                |               |
| CompanyStartDate              | DateTime              |               |
| Country                       | String                |               |
| CreateTime                    | DateTime              |               |
| CustomerCommunicationAddr     | Struct                |               |
| Email                         | Struct                |               |
| FiscalYearStartMonth          | Struct                |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| LegalAddr                     | Struct                |               |
| LegalName                     | String                |               |
| MetaData                      | Struct                |               |
| NameValue                     | Struct                |               |
| PrimaryPhone                  | Struct                |               |
| SupportedLanguages            | String                |               |
| SyncToken                     | String                |               |
| WebAddr                       | Struct                |               |
| Customer                      | ARAccountRef          | Struct        |                       |
| Active                        | Boolean               | EQUAL_TO      |
| AlternatePhone                | Struct                |               |
| Balance                       | BigDecimal            |               |
| BalanceWithJobs               | BigDecimal            |               |
| BillAddr                      | Struct                |               |
| BillWithParent                | Boolean               |               |
| BusinessNumber                | String                |               |
| CompanyName                   | String                |               |
| CreateTime                    | DateTime              |               |
| CurrencyRef                   | Struct                |               |
| CustomerTypeRef               | String                |               |
| DefaultTaxCodeRef             | Struct                |               |
| DisplayName                   | String                |               |
| FamilyName                    | String                |               |
| Fax                           | Struct                |               |
| FullyQualifiedName            | String                |               |
| GSTIN                         | String                |               |
| GSTRegistrationType           | String                |               |
| GivenName                     | String                |               |
| Id                            | String                |               |
| IsProject                     | Boolean               |               |
| Job                           | Boolean               |               |
| LastUpdatedTime               | DateTime              |               |
| Level                         | BigInteger            |               |
| MetaData                      | Struct                |               |
| MiddleName                    | String                |               |
| Mobile                        | Struct                |               |
| Notes                         | String                |               |
| OpenBalanceDate               | Date                  |               |
| ParentRef                     | Struct                |               |
| PaymentMethodRef              | Struct                |               |
| PreferredDeliveryMethod       | String                |               |
| PrimaryEmailAddr              | Struct                |               |
| PrimaryPhone                  | Struct                |               |
| PrimaryTaxIdentifier          | String                |               |
| PrintOnCheckName              | String                |               |
| ResaleNum                     | String                |               |
| SalesTermRef                  | Struct                |               |
| SecondaryTaxIdentifier        | String                |               |
| ShipAddr                      | Struct                |               |
| Source                        | String                |               |
| Suffix                        | String                |               |
| SyncToken                     | String                |               |
| TaxExemptionReasonId          | BigInteger            |               |
| Taxable                       | Boolean               |               |
| Title                         | String                |               |
| WebAddr                       | Struct                |               |
| Employee                      | Active                | Boolean       | EQUAL_TO              |
| BillRate                      | BigDecimal            |               |
| BillableTime                  | Boolean               |               |
| BirthDate                     | Date                  |               |
| CostRate                      | BigDecimal            |               |
| CreateTime                    | DateTime              |               |
| DisplayName                   | String                |               |
| EmployeeNumber                | String                |               |
| FamilyName                    | String                |               |
| Gender                        | String                |               |
| GivenName                     | String                |               |
| HiredDate                     | Date                  |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| MetaData                      | Struct                |               |
| MiddleName                    | String                |               |
| Mobile                        | Struct                |               |
| Organization                  | Boolean               |               |
| PrimaryAddr                   | Struct                |               |
| PrimaryEmailAddr              | Struct                |               |
| PrimaryPhone                  | Struct                |               |
| PrintOnCheckName              | String                |               |
| ReleasedDate                  | Date                  |               |
| SSN                           | String                |               |
| Suffix                        | String                |               |
| SyncToken                     | String                |               |
| Title                         | String                |               |
| V4IDPseudonym                 | String                |               |
| Estimate                      | AcceptedBy            | String        |                       |
| AcceptedDate                  | Date                  |               |
| ApplyTaxAfterDiscount         | Boolean               |               |
| BillAddr                      | Struct                |               |
| BillEmail                     | Struct                |               |
| ClassRef                      | Struct                |               |
| CreateTime                    | DateTime              |               |
| CurrencyRef                   | Struct                |               |
| CustomField                   | Struct                |               |
| CustomerMemo                  | Struct                |               |
| CustomerRef                   | Struct                |               |
| DepartmentRef                 | Struct                |               |
| DocNumber                     | String                |               |
| DueDate                       | Date                  |               |
| EmailStatus                   | String                |               |
| ExchangeRate                  | BigDecimal            |               |
| ExpirationDate                | Date                  |               |
| FreeFormAddress               | Boolean               |               |
| GlobalTaxCalculation          | Struct                |               |
| HomeTotalAmt                  | BigDecimal            |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| Line                          | Struct                |               |
| LinkedTxn                     | Struct                |               |
| MetaData                      | Struct                |               |
| PrintStatus                   | String                |               |
| PrivateNote                   | String                |               |
| RecurDataRef                  | Struct                |               |
| SalesTermRef                  | Struct                |               |
| ShipAddr                      | Struct                |               |
| ShipDate                      | Date                  |               |
| ShipFromAddr                  | Struct                |               |
| ShipMethodRef                 | Struct                |               |
| SyncToken                     | String                |               |
| TaxExemptionRef               | Struct                |               |
| TotalAmt                      | BigDecimal            |               |
| TransactionLocationType       | String                |               |
| TxnDate                       | Date                  |               |
| TxnStatus                     | String                |               |
| TxnTaxDetail                  | Struct                |               |
| Invoice                       | AllowOnlineACHPayment | Boolean       |                       |
| AllowOnlineCreditCardPayment  | Boolean               |               |
| ApplyTaxAfterDiscount         | Boolean               |               |
| Balance                       | BigDecimal            |               |
| BillAddr                      | Struct                |               |
| BillEmail                     | Struct                |               |
| BillEmailBcc                  | Struct                |               |
| BillEmailCc                   | Struct                |               |
| ClassRef                      | Struct                |               |
| CreateTime                    | DateTime              |               |
| CurrencyRef                   | Struct                |               |
| CustomField                   | Struct                |               |
| CustomerMemo                  | Struct                |               |
| CustomerRef                   | Struct                |               |
| DeliveryInfo                  | Struct                |               |
| DepartmentRef                 | Struct                |               |
| Deposit                       | BigDecimal            |               |
| DepositToAccountRef           | Struct                |               |
| DocNumber                     | String                |               |
| DueDate                       | Date                  |               |
| EmailStatus                   | String                |               |
| ExchangeRate                  | BigDecimal            |               |
| FreeFormAddress               | Boolean               |               |
| GlobalTaxCalculation          | Struct                |               |
| HomeBalance                   | BigDecimal            |               |
| HomeTotalAmt                  | BigDecimal            |               |
| Id                            | String                |               |
| InvoiceLink                   | String                |               |
| LastUpdatedTime               | DateTime              |               |
| Line                          | Struct                |               |
| LinkedTxn                     | Struct                |               |
| MetaData                      | Struct                |               |
| PrintStatus                   | String                |               |
| PrivateNote                   | String                |               |
| RecurDataRef                  | Struct                |               |
| SalesTermRef                  | Struct                |               |
| ShipAddr                      | Struct                |               |
| ShipDate                      | Date                  |               |
| ShipFromAddr                  | Struct                |               |
| ShipMethodRef                 | Struct                |               |
| SyncToken                     | String                |               |
| TaxExemptionRef               | Struct                |               |
| TotalAmt                      | BigDecimal            |               |
| TrackingNum                   | String                |               |
| TransactionLocationType       | String                |               |
| TxnDate                       | Date                  |               |
| TxnSource                     | String                |               |
| TxnTaxDetail                  | Struct                |               |
| Item                          | AbatementRate         | BigDecimal    |                       |
| Active                        | Boolean               | EQUAL_TO      |
| AssetAccountRef               | Struct                |               |
| ClassRef                      | Struct                |               |
| CreateTime                    | DateTime              |               |
| Description                   | String                |               |
| ExpenseAccountRef             | Struct                |               |
| FullyQualifiedName            | String                |               |
| Id                            | String                |               |
| IncomeAccountRef              | Struct                |               |
| InvStartDate                  | Date                  |               |
| ItemCategoryType              | String                |               |
| LastUpdatedTime               | DateTime              |               |
| Level                         | Integer               |               |
| MetaData                      | Struct                |               |
| Name                          | String                |               |
| ParentRef                     | Struct                |               |
| PrefVendorRef                 | Struct                |               |
| PurchaseCost                  | BigDecimal            |               |
| PurchaseDesc                  | String                |               |
| PurchaseTaxCodeRef            | Struct                |               |
| PurchaseTaxIncluded           | Boolean               |               |
| QtyOnHand                     | BigDecimal            |               |
| ReorderPoint                  | BigDecimal            |               |
| ReverseChargeRate             | BigDecimal            |               |
| SalesTaxCodeRef               | Struct                |               |
| SalesTaxIncluded              | Boolean               |               |
| ServiceType                   | String                |               |
| Sku                           | String                |               |
| Source                        | String                |               |
| SubItem                       | Boolean               |               |
| SyncToken                     | String                |               |
| TaxClassificationRef          | Struct                |               |
| Taxable                       | Boolean               |               |
| TrackQtyOnHand                | Boolean               |               |
| Type                          | String                |               |
| UQCDisplayText                | String                |               |
| UQCId                         | String                |               |
| UnitPrice                     | BigDecimal            |               |
| Payment                       | ARAccountRef          | Struct        |                       |
| CreateTime                    | DateTime              |               |
| CreditCardPayment             | Struct                |               |
| CurrencyRef                   | Struct                |               |
| CustomerRef                   | Struct                |               |
| DepositToAccountRef           | Struct                |               |
| ExchangeRate                  | BigDecimal            |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| Line                          | Struct                |               |
| MetaData                      | Struct                |               |
| PaymentMethodRef              | Struct                |               |
| PaymentRefNum                 | String                |               |
| PrivateNote                   | String                |               |
| SyncToken                     | String                |               |
| TaxExemptionRef               | Struct                |               |
| TotalAmt                      | BigDecimal            |               |
| TransactionLocationType       | String                |               |
| TxnDate                       | Date                  |               |
| TxnSource                     | String                |               |
| UnappliedAmt                  | BigDecimal            |               |
| Preference                    | AccountingInfoPrefs   | Struct        |                       |
| CreateTime                    | DateTime              |               |
| CurrencyPrefs                 | Struct                |               |
| EmailMessagesPrefs            | Struct                |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| MetaData                      | Struct                |               |
| OtherPrefs                    | Struct                |               |
| ProductAndServicesPrefs       | Struct                |               |
| ReportPrefs                   | Struct                |               |
| SalesFormsPrefs               | Struct                |               |
| SyncToken                     | String                |               |
| TaxPrefs                      | Struct                |               |
| TimeTrackingPrefs             | Struct                |               |
| VendorAndPurchasesPrefs       | Struct                |               |
| Profit And Loss               | Accounting Method     | String        | EQUAL_TO              |
| Adjusted Gain Loss            | String                | EQUAL_TO      |
| Class                         | String                | EQUAL_TO      |
| Columns                       | Struct                |               |
| Customer                      | String                | EQUAL_TO      |
| Date Macro                    | String                | EQUAL_TO      |
| Department                    | String                | EQUAL_TO      |
| End Date                      | Date                  | EQUAL_TO      |
| Header                        | Struct                |               |
| Item                          | String                | EQUAL_TO      |
| Rows                          | Struct                |               |
| Sort Order                    | String                | EQUAL_TO      |
| Start Date                    | Date                  | EQUAL_TO      |
| Summarize Column By           | String                | EQUAL_TO      |
| Vendor                        | String                | EQUAL_TO      |
| qzurl                         | String                | EQUAL_TO      |
| Tax Agency                    | CreateTime            | DateTime      |                       |
| DisplayName                   | String                |               |
| Id                            | String                |               |
| LastFileDate                  | Date                  |               |
| LastUpdatedTime               | DateTime              |               |
| MetaData                      | Struct                |               |
| SyncToken                     | String                |               |
| TaxAgencyConfig               | String                |               |
| TaxRegistrationNumber         | String                |               |
| TaxTrackedOnPurchases         | Boolean               |               |
| TaxTrackedOnSales             | Boolean               |               |
| Vendor                        | APAccountRef          | Struct        |                       |
| AcctNum                       | String                |               |
| Active                        | Boolean               | EQUAL_TO      |
| AlternatePhone                | Struct                |               |
| Balance                       | BigDecimal            |               |
| BillAddr                      | Struct                |               |
| BillRate                      | BigDecimal            |               |
| BusinessNumber                | String                |               |
| CompanyName                   | String                |               |
| CostRate                      | BigDecimal            |               |
| CreateTime                    | DateTime              |               |
| CurrencyRef                   | Struct                |               |
| DisplayName                   | String                |               |
| FamilyName                    | String                |               |
| Fax                           | Struct                |               |
| GSTIN                         | String                |               |
| GSTRegistrationType           | String                |               |
| GivenName                     | String                |               |
| HasTPAR                       | Boolean               |               |
| Id                            | String                |               |
| LastUpdatedTime               | DateTime              |               |
| MetaData                      | Struct                |               |
| MiddleName                    | String                |               |
| Mobile                        | Struct                |               |
| OtherContactInfo              | Struct                |               |
| PrimaryEmailAddr              | Struct                |               |
| PrimaryPhone                  | Struct                |               |
| PrintOnCheckName              | String                |               |
| Source                        | String                |               |
| Suffix                        | String                |               |
| SyncToken                     | String                |               |
| T4AEligible                   | Boolean               |               |
| T5018Eligible                 | Boolean               |               |
| TaxIdentifier                 | String                |               |
| TaxReportingBasis             | String                |               |
| TermRef                       | Struct                |               |
| Title                         | String                |               |
| Vendor1099                    | Boolean               |               |
| VendorPaymentBankDetail       | Struct                |               |
| WebAddr                       | Struct                |               |

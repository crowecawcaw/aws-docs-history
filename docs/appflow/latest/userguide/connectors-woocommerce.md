# WooCommerce connector for Amazon AppFlow

WooCommerce helps online merchants build commercial websites with a plugin for
WordPress. If you're a WooCommerce user, then your account contains data about your site
and your transactions, such as your orders, products, reviews, shipments, and more.
You can use Amazon AppFlow to transfer data from
WooCommerce to certain AWS services or other supported applications.

## Amazon AppFlow support for WooCommerce

Amazon AppFlow supports WooCommerce as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from WooCommerce.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to WooCommerce.

## Before you begin

To use Amazon AppFlow to transfer data from WooCommerce to supported destinations, you must meet these
requirements:

- You have an account with WooCommerce that contains the data that you want to transfer. For more
  information about the WooCommerce data objects that Amazon AppFlow supports, see [Supported objects](#woocommerce-objects "#woocommerce-objects").
- In your WooCommerce account, you've created a REST API key for Amazon AppFlow. For
  information about how create a key, see [Authentication](https://woocommerce.github.io/woocommerce-rest-api-docs/?shell#authentication "https://woocommerce.github.io/woocommerce-rest-api-docs/?shell#authentication") in the WooCommerce documentation.

From the REST API key details, note the consumer key and consumer secret. You provide these
values to Amazon AppFlow when you connect to your WooCommerce account.

## Connecting Amazon AppFlow to your WooCommerce account

To connect Amazon AppFlow to your WooCommerce account, provide the credentials from the REST
API key in your WooCommerce account so that Amazon AppFlow can access your data. If you haven't
yet configured your WooCommerce account for Amazon AppFlow integration, see [Before you begin](#woocommerce-prereqs "#woocommerce-prereqs").

###### To connect to WooCommerce

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **WooCommerce**.
4. Choose **Create connection**.
5. In the **Connect to WooCommerce** window, enter the following
   information:
   - **Consumer Key** — The consumer key from your REST API
     key.
   - **Consumer Secret** — The consumer secret from your REST API
     key.
   - **Instance URL** — The site name that you assigned when you
     created your site in WooCommerce.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your WooCommerce account, and grant access to
Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses WooCommerce as the data source, you can select this connection.

## Transferring data from WooCommerce with a flow

To transfer data from WooCommerce, create an Amazon AppFlow flow, and choose WooCommerce as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for WooCommerce, see [Supported objects](#woocommerce-objects "#woocommerce-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#woocommerce-destinations "#woocommerce-destinations").

## Supported destinations

When you create a flow that uses WooCommerce as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses WooCommerce as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                     | **Field**      | **Data type** | **Supported filters** |
| ------------------------------ | -------------- | ------------- | --------------------- |
| Coupon                         | After          | DateTime      | EQUAL_TO              |
| Amount                         | String         |               |
| Before                         | DateTime       | EQUAL_TO      |
| Code                           | String         | EQUAL_TO      |
| Context                        | String         | EQUAL_TO      |
| Date Created                   | DateTime       |               |
| Date Created GMT               | DateTime       |               |
| Date Expires GMT               | String         |               |
| Date Expiry                    | String         |               |
| Date Modified                  | DateTime       |               |
| Date Modified GMT              | DateTime       |               |
| Description                    | String         |               |
| Discount Type                  | String         |               |
| Email Restriction              | List           |               |
| Exclude Sale Item              | Boolean        |               |
| Excluded Product Category List | List           |               |
| Excluded Product ID            | List           |               |
| Free Shipping                  | Boolean        |               |
| ID                             | Integer        |               |
| Individual Use                 | Boolean        |               |
| Limit Usage To X Item          | Integer        |               |
| Maximum Amount                 | String         |               |
| Meta Data                      | List           |               |
| Minimum Amount                 | String         |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Product Category List          | List           |               |
| Product ID                     | List           |               |
| Search                         | String         | EQUAL_TO      |
| Status                         | String         |               |
| Usage Count                    | Integer        |               |
| Usage Limit                    | Integer        |               |
| Usage Limit Per User           | Integer        |               |
| Used By                        | List           |               |
| Coupon Total                   | Name           | String        |                       |
| Slug                           | String         |               |
| Total                          | String         |               |
| Customer Total                 | Name           | String        |                       |
| Slug                           | String         |               |
| Total                          | String         |               |
| Order                          | After          | DateTime      | EQUAL_TO              |
| Before                         | DateTime       | EQUAL_TO      |
| Billing                        | Struct         |               |
| Cart Hash                      | String         |               |
| Cart Tax                       | String         |               |
| Context                        | String         | EQUAL_TO      |
| Coupon Line                    | List           |               |
| Created Via                    | String         |               |
| Currency                       | String         |               |
| Currency Symbol                | String         |               |
| Customer                       | Integer        | EQUAL_TO      |
| Customer IP Address            | String         |               |
| Customer Id                    | Integer        |               |
| Customer Note                  | String         |               |
| Customer User Agent            | String         |               |
| DP                             | Integer        | EQUAL_TO      |
| Date Completed                 | DateTime       |               |
| Date Completed GMT             | DateTime       |               |
| Date Created                   | DateTime       |               |
| Date Created GMT               | DateTime       |               |
| Date Modified                  | DateTime       |               |
| Date Modified GMT              | DateTime       |               |
| Date Paid                      | DateTime       |               |
| Date Paid GMT                  | DateTime       |               |
| Discount Tax                   | String         |               |
| Discount Total                 | String         |               |
| Fee Line                       | List           |               |
| ID                             | Integer        |               |
| Is Editable                    | Boolean        |               |
| Line Item                      | List           |               |
| Meta Data                      | List           |               |
| Needs Payment                  | Boolean        |               |
| Needs Processing               | Boolean        |               |
| Number                         | String         |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Order Key                      | String         |               |
| Parent ID                      | Integer        |               |
| Payment Method                 | String         |               |
| Payment Method Title           | String         |               |
| Payment Url                    | String         |               |
| Prices Include Tax             | Boolean        |               |
| Product                        | Integer        | EQUAL_TO      |
| Refund                         | List           |               |
| Search                         | String         | EQUAL_TO      |
| Set Paid                       | Boolean        |               |
| Shipping                       | Struct         |               |
| Shipping Line                  | List           |               |
| Shipping Tax                   | String         |               |
| Shipping Total                 | String         |               |
| Status                         | String         |               |
| Tax Line                       | List           |               |
| Total                          | String         |               |
| Total Tax                      | String         |               |
| Transaction ID                 | String         |               |
| Version                        | String         |               |
| Order Total                    | Name           | String        |                       |
| Slug                           | String         |               |
| Total                          | String         |               |
| Payment Gateway                | Connection Url | String        |                       |
| Description                    | String         |               |
| Enabled                        | Boolean        |               |
| ID                             | String         |               |
| Method Description             | String         |               |
| Method Support                 | List           |               |
| Method Title                   | String         |               |
| Needs Setup                    | Boolean        |               |
| Order                          | Integer        |               |
| Post Install Script            | List           |               |
| Required Settings Key          | List           |               |
| Setting                        | Struct         |               |
| Settings Url                   | String         |               |
| Setup Help Text                | String         |               |
| Title                          | String         |               |
| Product                        | After          | DateTime      | EQUAL_TO              |
| Attribute List                 | List           |               |
| Average Rating                 | String         |               |
| Backorder                      | String         |               |
| Backordered                    | Boolean        |               |
| Backorders Allowed             | Boolean        |               |
| Before                         | DateTime       | EQUAL_TO      |
| Button Text                    | String         |               |
| Catalog Visibility             | String         |               |
| Category List                  | List           |               |
| Context                        | String         | EQUAL_TO      |
| Date Created                   | DateTime       |               |
| Date Created GMT               | DateTime       |               |
| Date Modified                  | DateTime       |               |
| Date Modified GMT              | DateTime       |               |
| Date On Sale From              | DateTime       |               |
| Date On Sale From GMT          | DateTime       |               |
| Date On Sale To                | DateTime       |               |
| Date On Sale To GMT            | DateTime       |               |
| Default Attribute List         | List           |               |
| Description                    | String         |               |
| Dimension                      | Struct         |               |
| Download                       | List           |               |
| Download Expiry                | Integer        |               |
| Download Limit                 | Integer        |               |
| Downloadable                   | Boolean        |               |
| External Url                   | String         |               |
| Featured                       | Boolean        | EQUAL_TO      |
| Grouped Product List           | List           |               |
| Has Option                     | Boolean        |               |
| ID                             | Integer        |               |
| Image List                     | List           |               |
| Jetpack Likes Enabled          | Boolean        |               |
| Jetpack Publicize Connection   | List           |               |
| Jetpack Sharing Enabled        | Boolean        |               |
| List of Cross Sell ID          | List           |               |
| List of Jetpack Related Post   | List           |               |
| List of Upsell ID              | List           |               |
| Low Stock Amount               | Integer        |               |
| Manage Stock                   | Boolean        |               |
| Menu Order                     | Integer        |               |
| Meta Data                      | List           |               |
| Name                           | String         |               |
| On Sale                        | Boolean        | EQUAL_TO      |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Parent ID                      | Integer        |               |
| Permalink                      | String         |               |
| Price                          | String         |               |
| Price Html                     | String         |               |
| Purchasable                    | Boolean        |               |
| Purchase Note                  | String         |               |
| Rating Count                   | Integer        |               |
| Regular Price                  | String         |               |
| Related ID                     | List           |               |
| Reviews Allowed                | Boolean        |               |
| Sale Price                     | String         |               |
| Search                         | String         | EQUAL_TO      |
| Shipping Class                 | String         | EQUAL_TO      |
| Shipping Class ID              | Integer        |               |
| Shipping Required              | Boolean        |               |
| Shipping Taxable               | Boolean        |               |
| Short Description              | String         |               |
| Sku                            | String         | EQUAL_TO      |
| Slug                           | String         | EQUAL_TO      |
| Sold Individually              | Boolean        |               |
| Status                         | String         | EQUAL_TO      |
| Stock Quantity                 | Integer        |               |
| Stock Status                   | String         | EQUAL_TO      |
| Tag                            | List           |               |
| Tag                            | String         | EQUAL_TO      |
| Tax Class                      | String         | EQUAL_TO      |
| Tax Status                     | String         |               |
| Total Sale                     | Integer        |               |
| Type                           | String         | EQUAL_TO      |
| Variation List                 | List           |               |
| Virtual                        | Boolean        |               |
| Weight                         | String         |               |
| Product Attribute              | Context        | String        | EQUAL_TO              |
| Has Archive                    | Boolean        |               |
| ID                             | Integer        |               |
| Name                           | String         |               |
| Order By                       | String         |               |
| Slug                           | String         |               |
| Type                           | String         |               |
| Product Attribute Term         | Context        | String        | EQUAL_TO              |
| Count                          | Integer        |               |
| Description                    | String         |               |
| Hide Empty                     | Boolean        | EQUAL_TO      |
| ID                             | Integer        |               |
| Menu Order                     | Integer        |               |
| Name                           | String         |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Parent                         | Integer        | EQUAL_TO      |
| Product                        | Integer        | EQUAL_TO      |
| Search                         | String         | EQUAL_TO      |
| Slug                           | String         | EQUAL_TO      |
| Product Category               | Context        | String        | EQUAL_TO              |
| Count                          | Integer        |               |
| Description                    | String         |               |
| Display                        | String         |               |
| Hide Empty                     | Boolean        | EQUAL_TO      |
| ID                             | Integer        |               |
| Image                          | Struct         |               |
| Menu Order                     | Integer        |               |
| Name                           | String         |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Parent                         | Integer        | EQUAL_TO      |
| Product                        | Integer        | EQUAL_TO      |
| Search                         | String         | EQUAL_TO      |
| Slug                           | String         | EQUAL_TO      |
| Product Review                 | After          | DateTime      | EQUAL_TO              |
| Before                         | DateTime       | EQUAL_TO      |
| Context                        | String         | EQUAL_TO      |
| Date Created                   | DateTime       |               |
| Date Created GMT               | DateTime       |               |
| ID                             | Integer        |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Product ID                     | Integer        |               |
| Product Name                   | String         |               |
| Product Permalink              | String         |               |
| Rating                         | Integer        |               |
| Review                         | String         |               |
| Reviewer                       | String         |               |
| Reviewer Avatar URL            | Struct         |               |
| Reviewer Email                 | String         |               |
| Search                         | String         | EQUAL_TO      |
| Status                         | String         | EQUAL_TO      |
| Verified                       | Boolean        |               |
| Product Shipping Class         | Context        | String        | EQUAL_TO              |
| Count                          | Integer        |               |
| Description                    | String         |               |
| Hide Empty                     | Boolean        | EQUAL_TO      |
| ID                             | Integer        |               |
| Name                           | String         |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Product                        | Integer        | EQUAL_TO      |
| Search                         | String         | EQUAL_TO      |
| Slug                           | String         | EQUAL_TO      |
| Product Tag                    | Context        | String        | EQUAL_TO              |
| Count                          | Integer        |               |
| Description                    | String         |               |
| Hide Empty                     | Boolean        | EQUAL_TO      |
| ID                             | Integer        |               |
| Name                           | String         |               |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Product                        | Integer        | EQUAL_TO      |
| Search                         | String         | EQUAL_TO      |
| Slug                           | String         | EQUAL_TO      |
| Product Total                  | Name           | String        |                       |
| Slug                           | String         |               |
| Total                          | String         |               |
| Product Variation              | After          | DateTime      | EQUAL_TO              |
| Backorder                      | String         |               |
| Backordered                    | Boolean        |               |
| Backorders Allowed             | Boolean        |               |
| Before                         | DateTime       | EQUAL_TO      |
| Context                        | String         | EQUAL_TO      |
| Date Created                   | DateTime       |               |
| Date Created GMT               | DateTime       |               |
| Date Modified                  | DateTime       |               |
| Date Modified GMT              | DateTime       |               |
| Date On Sale From              | DateTime       |               |
| Date On Sale From GMT          | DateTime       |               |
| Date On Sale To                | DateTime       |               |
| Date On Sale To GMT            | DateTime       |               |
| Description                    | String         |               |
| Dimension                      | Struct         |               |
| Download                       | List           |               |
| Download Expiry                | Integer        |               |
| Download Limit                 | Integer        |               |
| Downloadable                   | Boolean        |               |
| ID                             | Integer        |               |
| Image                          | Struct         |               |
| List of attribute              | List           |               |
| Low Stock Amount               | Integer        |               |
| MAX Price                      | String         | EQUAL_TO      |
| MIN Price                      | String         | EQUAL_TO      |
| Manage Stock                   | Boolean        |               |
| Menu Order                     | Integer        |               |
| Meta Data                      | List           |               |
| On Sale                        | Boolean        | EQUAL_TO      |
| Order                          | String         | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Permalink                      | String         |               |
| Price                          | String         |               |
| Purchasable                    | Boolean        |               |
| Regular Price                  | String         |               |
| Sale Price                     | String         |               |
| Search                         | String         | EQUAL_TO      |
| Shipping Class                 | String         |               |
| Shipping Class ID              | Integer        |               |
| Sku                            | String         | EQUAL_TO      |
| Slug                           | String         | EQUAL_TO      |
| Status                         | String         | EQUAL_TO      |
| Stock Quantity                 | Integer        |               |
| Stock Status                   | String         | EQUAL_TO      |
| Tax Class                      | String         | EQUAL_TO      |
| Tax Status                     | String         |               |
| Virtual                        | Boolean        |               |
| Weight                         | String         |               |
| Report                         | Description    | String        |                       |
| Slug                           | String         |               |
| Review Total                   | Name           | String        |                       |
| Slug                           | String         |               |
| Total                          | String         |               |
| Sale Report                    | Average Sale   | String        |                       |
| Context                        | String         | EQUAL_TO      |
| Date Max                       | Date           | EQUAL_TO      |
| Date Min                       | Date           | EQUAL_TO      |
| Net Sale                       | String         |               |
| Period                         | String         | EQUAL_TO      |
| Total                          | Struct         |               |
| Total Customer                 | Integer        |               |
| Total Discount                 | Integer        |               |
| Total Item                     | Integer        |               |
| Total Order                    | Integer        |               |
| Total Refund                   | Integer        |               |
| Total Sale                     | String         |               |
| Total Shipping                 | String         |               |
| Total Tax                      | String         |               |
| Totals Grouped By              | String         |               |
| Shipping Method                | Description    | String        |                       |
| ID                             | String         |               |
| Title                          | String         |               |
| Shipping Zone                  | ID             | Integer       | EQUAL_TO              |
| Name                           | String         |               |
| Order                          | Integer        |               |
| Shipping Zone Location         | Code           | String        |                       |
| Type                           | String         |               |
| Shipping Zone Method           | Enabled        | Boolean       |                       |
| ID                             | Integer        | EQUAL_TO      |
| Instance ID                    | Integer        |               |
| Method Description             | String         |               |
| Method ID                      | String         |               |
| Method Title                   | String         |               |
| Order                          | Integer        |               |
| Setting                        | Struct         |               |
| Title                          | String         |               |
| Tax Class                      | Name           | String        |                       |
| Slug                           | String         |               |
| Tax Rate                       | Cities         | List          |                       |
| City                           | String         |               |
| Class                          | String         | EQUAL_TO      |
| Compound                       | Boolean        |               |
| Context                        | String         | EQUAL_TO      |
| Country                        | String         |               |
| ID                             | Integer        |               |
| Name                           | String         |               |
| Order                          | Integer        | EQUAL_TO      |
| Order By                       | String         | EQUAL_TO      |
| Postcode                       | List           |               |
| Postcode                       | String         |               |
| Priority                       | Integer        |               |
| Rate                           | String         |               |
| Shipping                       | Boolean        |               |
| State                          | String         |               |
| Top Seller Report              | Context        | String        | EQUAL_TO              |
| Date Max                       | Date           | EQUAL_TO      |
| Date Min                       | Date           | EQUAL_TO      |
| Name                           | String         |               |
| Period                         | String         | EQUAL_TO      |
| Product ID                     | Integer        |               |
| Quantity                       | Integer        |               |

# AfterShip connector for Amazon AppFlow

AfterShip is a shipment tracking software as a service (SaaS) solution for
e-commerce companies. AfterShip user accounts manage tracking data across more than 600
shipping services worldwide. You can use Amazon AppFlow to transfer data from AfterShip to
certain AWS services or other supported applications.

## Amazon AppFlow support for AfterShip

Amazon AppFlow supports AfterShip as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from AfterShip.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to AfterShip.

## Before you begin

To use Amazon AppFlow to transfer data from AfterShip to supported destinations, you must meet these
requirements:

- You have an account with AfterShip that contains the data that you want to transfer. For more
  information about the AfterShip data objects that Amazon AppFlow supports, see [Supported objects](#aftership-objects "#aftership-objects").
- In the settings for your account, you've created an API key for Amazon AppFlow. Amazon AppFlow uses the
  API key to make authenticated calls to your account and securely access your data. For more
  information, see [Get
  the API key](https://www.aftership.com/docs/shipping/quickstart/api-quick-start#2-get-the-api-key "https://www.aftership.com/docs/shipping/quickstart/api-quick-start#2-get-the-api-key") in the _AfterShip API Quick
  Start_.

Note the value of your API key. When you connect to your AfterShip account, you
provide this value to Amazon AppFlow.

## Connecting Amazon AppFlow to your AfterShip account

To connect Amazon AppFlow to your AfterShip account, provide details from your
AfterShip account so that Amazon AppFlow can access your data. If you haven't yet configured
your AfterShip account for Amazon AppFlow integration, see [Before you begin](#aftership-prereqs "#aftership-prereqs").

Users who run the AfterShip connector for Amazon AppFlow can use one of two API
versions:

- If you created your API key after July 7, 2022, select as-api-key. This is the latest
  version of the key and has additional security features, such as Advanced Encryption Standard
  (AES) and Rivest, Shamir, Adleman (RSA) signatures.
- If you created your API key prior to July 7, 2022, you must select the aftership-api-key.
  This is a legacy version of the key and doesn't include the additional security features. To
  use AES or RSA signatures, replace your existing legacy key with a new API key. For more
  information, see [Authentication](https://www.aftership.com/docs/tracking/quickstart/authentication#4-legacy-api-keys "https://www.aftership.com/docs/tracking/quickstart/authentication#4-legacy-api-keys") in the _AfterShip API Quick Start_.

###### To connect to AfterShip

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **AfterShip**.
4. Choose **Create connection**.
5. In the **Connect to AfterShip** window, enter the following
   information:
   - **API key** – Enter your API key.
   - **API secret key** – Enter your secret key.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your AfterShip account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses AfterShip as the data source, you can select this connection.

## Transferring data from AfterShip with a flow

To transfer data from AfterShip, create an Amazon AppFlow flow, and choose AfterShip as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for AfterShip, see [Supported objects](#aftership-objects "#aftership-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#aftership-destinations "#aftership-destinations").

## Supported destinations

When you create a flow that uses AfterShip as the data source, you can set the destination to any of the following connectors:

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

When you create a flow that uses AfterShip as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                     | **Field** | **Data type** | **Supported filters** |
| ------------------------------ | --------- | ------------- | --------------------- |
| Couriers                       | Name      | String        |                       |
| Phone                          | String    |               |
| Slug                           | String    |               |
| defaultLanguage                | String    |               |
| optionalFields                 | List      |               |
| otherName                      | String    |               |
| requiredFields                 | List      |               |
| serviceFromCountryIso3         | List      |               |
| supportLanguages               | List      |               |
| webUrl                         | String    |               |
| Trackings                      | Active    | Boolean       |                       |
| AftershipEstimatedDeliveryDate | String    |               |
| Android                        | List      |               |
| Checkpoints                    | List      |               |
| CourierDestinationCountryIso3  | String    |               |
| CourierRedirectLink            | String    |               |
| CourierTrackingLink            | String    |               |
| CreatedAt                      | DateTime  |               |
| CustomFields                   | List      |               |
| CustomerName                   | String    |               |
| DeliveryTime                   | Integer   |               |
| DeliveryType                   | String    |               |
| DestinationCountryIso3         | String    |               |
| DestinationRawLocation         | String    |               |
| Emails                         | List      |               |
| ExpectedDelivery               | String    |               |
| FirstAttemptedAt               | DateTime  |               |
| IOs                            | List      |               |
| Id                             | String    |               |
| Language                       | String    |               |
| LastMileTrackingSupported      | Boolean   |               |
| LastUpdatedAt                  | DateTime  |               |
| LatestEstimatedDelivery        | String    |               |
| Note                           | String    |               |
| OnTimeDifference               | Integer   |               |
| OnTimeStatus                   | String    |               |
| OrderDate                      | DateTime  |               |
| OrderId                        | String    |               |
| OrderIdPath                    | String    |               |
| OrderNumber                    | String    |               |
| OrderPromisedDeliveryDate      | String    |               |
| OrderTags                      | List      |               |
| OriginCountryIso3              | String    |               |
| PickupLocation                 | String    |               |
| PickupNote                     | String    |               |
| ReturnToSender                 | Boolean   |               |
| ShipmentDeliveryDate           | DateTime  |               |
| ShipmentPackageCount           | Integer   |               |
| ShipmentPickupDate             | DateTime  |               |
| ShipmentType                   | String    |               |
| ShipmentWeight                 | Float     |               |
| ShipmentWeightUnit             | String    |               |
| SignedBy                       | String    |               |
| Slug                           | String    |               |
| Smses                          | List      |               |
| Source                         | String    |               |
| SubscribedEmails               | List      |               |
| SubscribedSmses                | List      |               |
| Subtag                         | String    |               |
| SubtagMessage                  | String    |               |
| Tag                            | String    |               |
| Title                          | String    |               |
| TrackedCount                   | Integer   |               |
| TrackingAccountNumber          | String    |               |
| TrackingDestinationCountry     | String    |               |
| TrackingKey                    | String    |               |
| TrackingNumber                 | String    |               |
| TrackingOriginCountry          | String    |               |
| TrackingPostalCode             | String    |               |
| TrackingShipDate               | String    |               |
| TrackingState                  | String    |               |
| UniqueToken                    | String    |               |
| UpdatedAt                      | DateTime  |               |
| shipmentTags                   | List      |               |

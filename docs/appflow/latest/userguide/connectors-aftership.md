

# AfterShip connector for Amazon AppFlow
<a name="connectors-aftership"></a>

AfterShip is a shipment tracking software as a service (SaaS) solution for e-commerce companies. AfterShip user accounts manage tracking data across more than 600 shipping services worldwide. You can use Amazon AppFlow to transfer data from AfterShip to certain AWS services or other supported applications.

## Amazon AppFlow support for AfterShip
<a name="aftership-support"></a>

Amazon AppFlow supports AfterShip as follows.

**Supported as a data source?**  
Yes. You can use Amazon AppFlow to transfer data from AfterShip.

**Supported as a data destination?**  
No. You can't use Amazon AppFlow to transfer data to AfterShip.

## Before you begin
<a name="aftership-prereqs"></a>

To use Amazon AppFlow to transfer data from AfterShip to supported destinations, you must meet these requirements:
+ You have an account with AfterShip that contains the data that you want to transfer. For more information about the AfterShip data objects that Amazon AppFlow supports, see [Supported objects](#aftership-objects).
+ In the settings for your account, you've created an API key for Amazon AppFlow. Amazon AppFlow uses the API key to make authenticated calls to your account and securely access your data. For more information, see [Get the API key](https://www.aftership.com/docs/shipping/quickstart/api-quick-start#2-get-the-api-key) in the *AfterShip API Quick Start*.

Note the value of your API key. When you connect to your AfterShip account, you provide this value to Amazon AppFlow.

## Connecting Amazon AppFlow to your AfterShip account
<a name="aftership-connecting"></a>

To connect Amazon AppFlow to your AfterShip account, provide details from your AfterShip account so that Amazon AppFlow can access your data. If you haven't yet configured your AfterShip account for Amazon AppFlow integration, see [Before you begin](#aftership-prereqs).

Users who run the AfterShip connector for Amazon AppFlow can use one of two API versions:
+ If you created your API key after July 7, 2022, select as-api-key. This is the latest version of the key and has additional security features, such as Advanced Encryption Standard (AES) and Rivest, Shamir, Adleman (RSA) signatures.
+ If you created your API key prior to July 7, 2022, you must select the aftership-api-key. This is a legacy version of the key and doesn't include the additional security features. To use AES or RSA signatures, replace your existing legacy key with a new API key. For more information, see [Authentication](https://www.aftership.com/docs/tracking/quickstart/authentication#4-legacy-api-keys) in the *AfterShip API Quick Start*. 

**To connect to AfterShip**

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/).

1. In the navigation pane on the left, choose **Connections**.

1. On the **Manage connections** page, for **Connectors**, choose **AfterShip**.

1. Choose **Create connection**.

1. In the **Connect to AfterShip** window, enter the following information:
   + **API key** – Enter your API key.
   + **API secret key** – Enter your secret key.

1. Optionally, under **Data encryption**, choose **Customize encryption settings (advanced)** if you want to encrypt your data with a customer managed key in the AWS Key Management Service (AWS KMS).

   By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages for you. Choose this option if you want to encrypt your data with your own KMS key instead.

   Amazon AppFlow always encrypts your data during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md).

   If you want to use a KMS key from the current AWS account, select this key under **Choose an AWS KMS key**. If you want to use a KMS key from a different AWS account, enter the Amazon Resource Name (ARN) for that key.

1. For **Connection name**, enter a name for your connection.

1. Choose **Connect**.

1. In the window that appears, sign in to your AfterShip account, and grant access to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the **Connections** table. When you create a flow that uses AfterShip as the data source, you can select this connection.

## Transferring data from AfterShip with a flow
<a name="aftership-transfer-data"></a>

To transfer data from AfterShip, create an Amazon AppFlow flow, and choose AfterShip as the data source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md).

When you configure the flow, choose the data object that you want to transfer. For the objects that Amazon AppFlow supports for AfterShip, see [Supported objects](#aftership-objects).

Also, choose the destination where you want to transfer the data object that you selected. For more information about how to configure your destination, see [Supported destinations](#aftership-destinations).

## Supported destinations
<a name="aftership-destinations"></a>

When you create a flow that uses AfterShip as the data source, you can set the destination to any of the following connectors: 
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
<a name="aftership-objects"></a>

When you create a flow that uses AfterShip as the data source, you can transfer any of the following data objects to supported destinations:



- ** Couriers**
  - **** Field**:** Name / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Phone / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** defaultLanguage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** optionalFields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** otherName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** requiredFields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** serviceFromCountryIso3 / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** supportLanguages / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** webUrl / **** Data type**:** String / **** Supported filters**:** 

- ** Trackings**
  - **** Field**:** Active / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** AftershipEstimatedDeliveryDate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Android / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Checkpoints / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** CourierDestinationCountryIso3 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CourierRedirectLink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CourierTrackingLink / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** CreatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** CustomFields / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** CustomerName / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DeliveryTime / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** DeliveryType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DestinationCountryIso3 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** DestinationRawLocation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Emails / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** ExpectedDelivery / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** FirstAttemptedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** IOs / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Id / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Language / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** LastMileTrackingSupported / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** LastUpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** LatestEstimatedDelivery / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Note / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OnTimeDifference / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** OnTimeStatus / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OrderDate / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** OrderId / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OrderIdPath / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OrderNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OrderPromisedDeliveryDate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** OrderTags / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** OriginCountryIso3 / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PickupLocation / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** PickupNote / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ReturnToSender / **** Data type**:** Boolean / **** Supported filters**:** 
  - **** Field**:** ShipmentDeliveryDate / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ShipmentPackageCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** ShipmentPickupDate / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** ShipmentType / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** ShipmentWeight / **** Data type**:** Float / **** Supported filters**:** 
  - **** Field**:** ShipmentWeightUnit / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SignedBy / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Slug / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Smses / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Source / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SubscribedEmails / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** SubscribedSmses / **** Data type**:** List / **** Supported filters**:** 
  - **** Field**:** Subtag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** SubtagMessage / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Tag / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** Title / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackedCount / **** Data type**:** Integer / **** Supported filters**:** 
  - **** Field**:** TrackingAccountNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingDestinationCountry / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingKey / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingNumber / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingOriginCountry / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingPostalCode / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingShipDate / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** TrackingState / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UniqueToken / **** Data type**:** String / **** Supported filters**:** 
  - **** Field**:** UpdatedAt / **** Data type**:** DateTime / **** Supported filters**:** 
  - **** Field**:** shipmentTags / **** Data type**:** List / **** Supported filters**:** 


# Data in AWS Data Exchange

Data is organized in AWS Data Exchange using three building blocks:

- **[Assets](#assets "#assets")** – A piece of
  data
- **[Revisions](#revisions "#revisions")** – A
  container for one or more assets
- **[Data sets](#data-sets-concept "#data-sets-concept")**
  – A series of one or more revisions
  These three building blocks form the foundation of the product that you manage using the
  AWS Data Exchange console or the AWS Data Exchange API.

To create, view, update, or delete data sets, you can use the AWS Data Exchange console, the AWS Command Line Interface
(AWS CLI), your own REST client, or one of the AWS SDKs. For more information about
programmatically managing AWS Data Exchange data sets, see the [AWS Data Exchange API Reference](../apireference.md "../apireference.md").

## Assets

Assets are the _data_ in AWS Data Exchange.

The type of asset defines how the data is delivered to the
receiver or
subscriber through the data
sets, data
grants, or products that
contain
them.

An asset can be any of the following:

- A file stored on your local computer
- A file stored as an object in Amazon Simple Storage Service (Amazon S3)
- A REST API created in Amazon API Gateway
- An Amazon Redshift data set
- An AWS Lake Formation data permission (Preview)
- An Amazon S3 data access data set

### Asset structure

Assets have the following parameters:

- `DataSetId` – The ID of the data set that contains this
  asset.
- `RevisionId` – The ID of the revision that contains this
  asset.
- `Id` – A unique ID generated when the asset is created.
- `Arn` – A unique identifier for an AWS resource name.
- `CreatedAt` and `UpdatedAt` – Date and timestamps for
  the creation and last update of the asset.
- `AssetDetails` – Information about the asset.
- `AssetType` – Either a snapshot of an Amazon S3 object, an Amazon API Gateway
  API, an Amazon Redshift data set, or an Amazon S3 data set.

###### Example asset resource

```
{
    "Name": "`automation/cloudformation.yaml`",
    "Arn": "arn:aws:dataexchange:us-east-1::data-sets/`29EXAMPLE24b82c6858af3cEXAMPLEcf`/revisions/`bbEXAMPLE74c02f4745c660EXAMPLE20`/assets/`baEXAMPLE660c9fe7267966EXAMPLEf5`",
    "Id": "`baEXAMPLE660c9fe7267966EXAMPLEf5`",
    "CreatedAt": "2019-10-17T21:31:29.833Z",
    "UpdatedAt": "2019-10-17T21:31:29.833Z",
    "AssetType": "S3_SNAPSHOT",
    "RevisionId": "`bbEXAMPLE74c02f4745c660EXAMPLE20`",
    "DataSetId": "`29EXAMPLE24b82c6858af3cEXAMPLEcf`",
    "AssetDetails": {
        "S3SnapshotAsset": {
            "Size": 9423
        }
    }
}
```

### Asset types

###### Types

- [Files data set](#s3-asset-type "#s3-asset-type")
- [API assets](#API-asset-type "#API-asset-type")
- [Amazon Redshift datashare assets](#RS-asset-type "#RS-asset-type")
- [AWS Lake Formation data permission (Preview)](#LF-asset-type "#LF-asset-type")
- [Amazon S3 data access](#S3-access-asset-type "#S3-access-asset-type")

#### Files data set

Using Files, subscribers can access a copy of the data set as an entitled data set and
export the assets.

A data set owner can both import and export Files using the AWS Data Exchange console,
programmatically through the AWS CLI, their own REST application, or one of the AWS SDKs.
For more information, about importing Amazon S3 assets. see [Importing AWS Data Exchange assets from an S3 bucket](importing-from-s3.md "importing-from-s3.md"). For more information about exporting assets, see
[Exporting AWS Data Exchange assets to an S3 bucket](exporting-from-s3.md "exporting-from-s3.md").

#### API assets

With API assets, data recipients or subscribers can view the API and download the API
specification as an entitled data set. You can also make API calls to AWS Data Exchange-managed
endpoints, which are then proxied through to API-owner endpoints.

A data set owner who has an existing Amazon API Gateway API can add an API asset using the
AWS Data Exchange console, programmatically through the AWS CLI, or one of the AWS SDKs. For more
information about importing API assets, see [Importing AWS Data Exchange assets from an Amazon API Gateway API](import-API-asset.md "import-API-asset.md").

###### Note

Currently, the `SendApiAsset` operation is not supported for the
following SDKs:

- SDK for .NET
- AWS SDK for C++
- SDK for Java 2.x

Data set owners who do not have an existing Amazon API Gateway API must create one before
adding an API asset to their product. For more information, see [Developing a REST API in API Gateway](../../../apigateway/latest/developerguide/rest-api-develop.md "../../../apigateway/latest/developerguide/rest-api-develop.md") in the _Amazon API Gateway
Developer Guide_.

#### Amazon Redshift datashare assets

With Amazon Redshift datashare assets, recipients can get read-only access to query the data in
Amazon Redshift without extracting, transforming, and loading data.

For more information about importing Amazon Redshift datashare assets, see [Importing AWS Data Exchange assets from an AWS Data Exchange datashare for
Amazon Redshift](import-RS-asset.md "import-RS-asset.md").

#### AWS Lake Formation data permission (Preview)

With AWS Lake Formation data permission assets, recipients or subscribers can access and query
all databases, tables, or columns associated with the tags specified.

Data set owners must create and tag their data before importing the tags as part of an
AWS Data Exchange asset. For more information about importing Lake Formation data permission assets, see [Importing AWS Data Exchange assets from AWS Lake Formation (Preview)](import-LF-asset.md "import-LF-asset.md").

#### Amazon S3 data access

With Amazon S3 data access assets, recipients or subscribers can directly access and use
the provider's data without creating or managing data copies. Data set owners can set up
AWS Data Exchange for Amazon S3 on top of their existing Amazon S3 buckets to share direct access to an
entire S3 bucket or specific prefixes and Amazon S3 objects.

## Revisions

A revision is a _container_ for one or more assets.

You use revisions to update data in Amazon S3. For example, you can group a collection of .csv
files or a single .csv file and a dictionary to create a revision. As new data is available, you
create revisions and add assets. After you create and finalize the revision using the AWS Data Exchange
console, that revision will be immediately available to subscribers. For more information, see
[Publishing a new product in AWS Data Exchange](publishing-products.md "publishing-products.md").

Keep the following in mind:

- To be finalized, a revision must contain at least one asset.
- It is your responsibility to ensure that the assets are correct before you finalize
  your revision.
- A finalized revision published to at least one data grant or product can't be
  unfinalized or changed in any way. (Except through the revoke revision process)
- After the revision is finalized, it is automatically published to your data grants or
  products.

### Revision structure

Revisions have the following parameters:

- `DataSetId` – The ID of the data set that contains this
  revision.
- `Comment` – A comment about the revision. This field can be 128
  characters long.
- `Finalized` – Either true or false. Used to indicate whether the
  revision is finalized.
- `Id` – The unique identifier for the revision generated when it's
  created.
- `Arn` – A unique identifier for an AWS resource name.
- `CreatedAt` – Date and timestamp for the creation of the revision.
  Entitled revisions are created at the time of publishing.
- `UpdatedAt` – Date and timestamp for the last update of the
  revision.
- `Revoked` – A status indicating that subscribers' access to the
  revision was revoked.
- `RevokedAt` – Date and timestamp indicating when subscriber access
  to the revision was revoked.
- `RevocationComment` – A required comment to inform subscribers of
  the reason their access to the revision was revoked. The minimum required character
  length is 10. This field can be between 10 and 512 characters long.
- `SourceID` – The revision ID of the owned revision corresponding to
  the entitled revision being viewed. This parameter is returned when a revision owner is
  viewing the entitled copy of its owned revision.

###### Example revision resource

```

        {
            "UpdatedAt": "2019-10-11T14:13:31.749Z",
            "DataSetId": "`1EXAMPLE404460dc9b005a0d9EXAMPLE2f`",
            "Comment": "`initial data revision`",
            "Finalized": true,
            "Id": "`e5EXAMPLE224f879066f9999EXAMPLE42`",
            "Arn": "arn:aws:dataexchange:us-east-1:`123456789012`:data-sets/`1EXAMPLE404460dc9b005a0d9EXAMPLE2f`/revisions/`e5EXAMPLE224f879066f9999EXAMPLE42`",
            "CreatedAt": "2019-10-11T14:11:58.064Z"
        }

```

## Data sets

A data set in AWS Data Exchange is a _collection_ of data that
can change over time.

When recipients or subscribers access a Files data set, they're accessing a specific
revision in the data set. This structure enables providers to change the data available in
data sets over time without having to worry about changes to historical data.

When recipients or subscribers access an API data set, they're accessing a data set that
contains API assets, which enable subscribers to make API calls to AWS Data Exchange-managed endpoints,
which are then proxied through to provider endpoints.

When recipients or subscribers access an Amazon Redshift data set, they're accessing an AWS Data Exchange
datashare for Amazon Redshift. This datashare gives subscribers read-only access to the schemas, tables,
views, and user-defined functions that the data owner has added to the datashares.

When recipients or subscribers access an AWS Lake Formation data permission data set, they're
accessing the databases, tables, and/or columns tagged with an LF-tag specified by the data
set owner.

When recipients or subscribers access an Amazon S3 data access data set, they're granted
read-only access to shared Amazon S3 objects hosted in the provider's Amazon S3 buckets. Recipients or
subscribers can use this data directly with other AWS services.

To create, view, update, or delete data sets, providers can use the AWS Data Exchange console, AWS
CLI, your own REST client, or one of the AWS SDKs. For more information about
programmatically managing AWS Data Exchange data sets, see the [AWS Data Exchange API Reference](../apireference/welcome.md "../apireference/welcome.md").

###### Topics

- [Owned data sets](#owned-data-sets "#owned-data-sets")
- [Entitled data sets](#entitled-data-sets "#entitled-data-sets")
- [Data set types](#data-set-types "#data-set-types")
- [Amazon S3 data access data set](#s3-data-set-type "#s3-data-set-type")
- [AWS Lake Formation data set (Preview)](#LF-data-set-type "#LF-data-set-type")
- [AWS Regions and data sets](#data-set-regions "#data-set-regions")
- [Data set structure](#data-set-structure "#data-set-structure")
- [Data set best practices](#data-set-best-practices "#data-set-best-practices")

### Owned data sets

A data set is owned by the account that created it. Owned data sets can be identified
using the `origin` parameter, which is set to `OWNED`.

### Entitled data sets

Entitled data sets are a read-only view of a sender's owned data sets. Entitled data
sets are created at time of data grant creation or product publishing and are made available
to recipients or subscribers who have an active data grant or subscription to the product.
Entitled data sets can be identified using the `origin` parameter, which is set
to `ENTITLED`.

As a recipient, you can view and interact with your entitled data sets using the AWS Data Exchange
API or in the AWS Data Exchange console.

As a data set owner, you also have access to the entitled data set view that your
recipients or subscribers see. You can do so using the AWS Data Exchange API, or by choosing the data
set name in the data grant or product page in the AWS Data Exchange console.

### Data set types

The following data set types are supported in AWS Data Exchange:

- [Files data set](#S3-object-data-set-type "#S3-object-data-set-type")
- [API data set](#api-data-set-type "#api-data-set-type")
- [Amazon Redshift data set](#RS-data-set-type "#RS-data-set-type")
- [Amazon S3 data access data set](#s3-data-set-type "#s3-data-set-type")
- [AWS Lake Formation data set (Preview)](#LF-data-set-type "#LF-data-set-type")

#### Files data set

A Files data set is a data set that contains flat files permitted by Amazon S3.

As a recipient or subscriber, you can export data either locally (download to your
computer) or to your Amazon S3 bucket.

As a data set owner, you can import any type of flat file from your Amazon S3 bucket and
add it to the data set.

#### API data set

An API data set is a data set that contains API assets. API assets enable recipients
or subscribers to make API calls to AWS Data Exchange-managed endpoints, which are then proxied
through to data set owner endpoints.

As a data set owner, you create an API in Amazon API Gateway and add it to the data set to
license access to your API upon data grant creation or subscription.

#### Amazon Redshift data set

An Amazon Redshift data set includes AWS Data Exchange datashares for Amazon Redshift. When you subscribe to a data set
with datashares, you are added as a consumer of the datashare. This gives you read-only
access to the schemas, tables, views, and user-defined functions the data set owner has
added to the datashares.

As a data set owner, you can create a database from the datashare in Amazon Redshift and then
query live data without extracting, transforming, and loading files. You are automatically
granted access to the datashare when your data grant or subscription is activated and lose
access after your either of these expire.

As a data set owner, you create a datashare in Amazon Redshift and add it to the data set to
license access to your datashare upon data grant creation or subscription.

### Amazon S3 data access data set

With AWS Data Exchange for Amazon S3 data access, data recipients or subscribers can access third-party
data files directly from data set owners' Amazon S3 buckets.

When you subscribe to an AWS Data Exchange for Amazon S3 data access product, AWS Data Exchange automatically does
the following:

- Provisions an Amazon S3 access point. Amazon S3 Access Point is a feature of Amazon S3 that
  simplifies data sharing to an Amazon S3 bucket.
- Updates the S3 Access Point resource policies to grant you read-only access.

With AWS Data Exchange for Amazon S3, data set owners can share direct access to an entire Amazon S3 bucket or
specific prefixes and Amazon S3 objects. In addition, AWS Data Exchange can be used to automatically manage
data grants, subscriptions, entitlements, billing, and payments.

### AWS Lake Formation data set (Preview)

An AWS Lake Formation data set is a data set that contains AWS Lake Formation data permission assets.

As a data recipient or subscriber, you can manage the data made available to you in your
AWS Lake Formation. After creating resource links in your AWS Lake Formation, you can query the data using
analytics services like Amazon Athena.

As a data set owner, you tag your data using LF-tags in AWS Lake Formation and import those tags
as assets when creating your data set.

### AWS Regions and data sets

Your data sets can be in any supported AWS Region, but all data sets in a single data
grant or product must be in the same AWS Region.

### Data set structure

Data sets have the following parameters:

- `Name` – The name of the data set. This value can be up to 256
  characters long.
- `Description` – A description for the data set. This value can be
  up to 16,348 characters long.
- `AssetType` – Defines the type of assets the data set
  contains.
- `Origin` – A property that defines the data set as
  `Owned` by the account (for providers) or `Entitled` to the
  account (for subscribers).
- `Id` – An ID that uniquely identifies the data set. Data set IDs
  are generated at data set creation. Entitled data sets have a different ID than the
  original owned data set.
- `Arn` – A unique identifier for an AWS resource name.
- `CreatedAt` and `UpdatedAt` – Date and timestamps for
  the creation and last update of the data set.

###### Note

As a data set
owner,
you can change some properties for owned data sets, like the **Name** or
**Description**. Updating properties in an owned data set won't update
the properties in the corresponding entitled data set.

###### Example data set resource

```
{
    "Origin": "OWNED",
    "AssetType": "S3_SNAPSHOT",
    "Name": "`MyDataSetName`",
    "CreatedAt": "2019-09-09T19:31:49.704Z",
    "UpdatedAt": "2019-09-09T19:31:49.704Z",
    "Id": "`fEXAMPLE1fd9a5c8b0d2e6fEXAMPLEe1`",
    "Arn": "arn:aws:dataexchange:us-east-2:`123456789109`:data-sets/`fEXAMPLE1fd9a5c8b0d2e6fEXAMPLEe1`",
    "Description": "`This is my data set's description that describes the contents of the data set.`"
}
```

### Data set best practices

As a
data
set owner, when you create and update data sets, keep the following best
practices in mind:

- The name of the data set is visible in the
  data grant or
  product details in the catalog. We recommend that you choose a
  concise, descriptive name so customers easily understand the content of the data
  set.
- The description is visible to
  recipients or
  subscribers who have an active
  data grant or
  subscription to the product. We recommend that you include coverage
  information and the features and benefits of the data set.

## Tags

You can add tags to your owned data sets and their revisions. When you use tagging, you
can also use tag-based access control in AWS Identity and Access Management (IAM) policies to control access to these
data sets and revisions.

Entitled data sets can't be tagged. Tags of owned data sets and their revisions are not
propagated to their corresponding entitled versions. Specifically, recipients or subscribers,
who have read-only access to entitled data sets and revisions, won't see the tags of the
original owned data set.

###### Note

Currently, assets and jobs don't support tagging.

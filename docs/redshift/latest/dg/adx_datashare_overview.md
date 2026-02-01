Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# AWS Data Exchange datashares

You can use AWS Data Exchange datashares to manage billing for Amazon Redshift data sharing.

An AWS Data Exchange datashare is a unit of licensing for sharing your data through
AWS Data Exchange. AWS manages all billing and payments associated with subscriptions to
AWS Data Exchange and use of Amazon Redshift data sharing. Approved data providers can add AWS Data Exchange
datashares to AWS Data Exchange products. When customers subscribe to a product with AWS Data Exchange
datashares, they get access to the datashares in the product.

_AWS Data Exchange for Amazon Redshift_ makes it convenient to
license access to your Amazon Redshift data through AWS Data Exchange. When a customer subscribes to a
product with AWS Data Exchange datashares, AWS Data Exchange automatically adds the customer as a data
consumer on all AWS Data Exchange datashares included with the product. Invoices are automatically
generated, and payments are centrally collected and automatically disbursed through
AWS Marketplace Entitlement Service.

Providers can license data in Amazon Redshift at a granular level, such as schemas, tables,
views, and user-defined functions. You can use the same AWS Data Exchange datashare across multiple
AWS Data Exchange products. Any objects added to the AWS Data Exchange datashare is available to consumers.
Producers can view all AWS Data Exchange datashares managed by AWS Data Exchange on their behalf using
Amazon Redshift API operations, SQL commands, and the Amazon Redshift console. Customers who subscribe
to a product AWS Data Exchange datashares have read-only access to the objects in the datashares.

Customers who want to consume third-party producer data can browse the AWS Data Exchange
catalog to discover and subscribe to datasets in Amazon Redshift. After their AWS Data Exchange
subscription is active, they can create a database from the datashare in their cluster
and query the data in Amazon Redshift.

## How AWS Data Exchange datashares work

### Managing AWS Data Exchange datashares as a producer

administrator

If
you are a data producer (also known as a provider on AWS Data Exchange), you can create
AWS Data Exchange datashares that connect to your Amazon Redshift databases. To add AWS Data Exchange datashares to
products on AWS Data Exchange, you must be a registered AWS Data Exchange provider.

For more information on how to get started with AWS Data Exchange datashares, see [Sharing licensed Amazon Redshift data on AWS Data Exchange](adx-getting-started.md "adx-getting-started.md").

### Using AWS Data Exchange datashares as a consumer with an

active AWS Data Exchange subscription

If you are a consumer with an active AWS Data Exchange subscription (also known as a
subscriber on AWS Data Exchange), you can browse the AWS Data Exchange catalog on the AWS Data Exchange
console to discover products containing AWS Data Exchange datashares.

After you subscribe to a product that contains AWS Data Exchange datashares, create a
database from the datashare within your cluster. You can then query the data in
Amazon Redshift directly without extracting, transforming, and loading the data.

For more information on how to get started with AWS Data Exchange datashares, see [Sharing licensed Amazon Redshift data on AWS Data Exchange](adx-getting-started.md "adx-getting-started.md").

For _AWS Data Exchange datashares_, consider the
following:

- When a producer cluster is deleted, Amazon Redshift deletes the datashares created by
  the producer cluster. When a producer cluster is backed up and restored, the
  created datashares still persist on the restored cluster. For data subscribers to
  be able to continue accessing the data, create the AWS Data Exchange datashares again and
  publish them to the product's data sets. The consumer database on the consumer
  cluster points to the datashare from the original cluster where the snapshot is
  taken. To query the shared data from the restored cluster, the consumer
  administrator creates a different database, or drops and recreates an existing
  consumer database to use the newly created AWS Data Exchange datashare from the newly restored
  cluster.
- We recommend that you don't delete your cluster if you have any AWS Data Exchange
  datashares. Performing this type of alteration can breach data product terms in
  AWS Data Exchange.

## Datashare producers and

consumers

_Data producers_ (also known as data sharing
producers or datashare producers) are clusters that you want to share data from.
producer administrators and database owners can create datashares using the CREATE
DATASHARE command. You can add objects such as schemas, tables, views, and SQL
user-defined functions (UDFs) from a database that you want the producer cluster to
share with consumer clusters.

Data producers (also known as providers on AWS Data Exchange) for AWS Data Exchange datashares can license
data through AWS Data Exchange. Approved providers can add AWS Data Exchange datashares to AWS Data Exchange
products.

When a customer subscribes to a product with AWS Data Exchange datashares, AWS Data Exchange
automatically adds the customer as a data consumer on all AWS Data Exchange datashares included
with the product. AWS Data Exchange also removes all customers from AWS Data Exchange datashares when
their subscription ends. AWS Data Exchange also automatically manages billing, invoicing,
payment collection, and payment distribution for paid products with AWS Data Exchange datashares.
For more information, see [AWS Data Exchange datashares](adx_datashare_overview.md "adx_datashare_overview.md"). To register as an AWS Data Exchange data provider,
see [Getting started as a provider](../../../data-exchange/latest/userguide/provider-getting-started.md "../../../data-exchange/latest/userguide/provider-getting-started.md").

_Data consumers_ (also known as data sharing
consumers or datashare consumers) are clusters that receive datashares from producer
clusters.

Amazon Redshift clusters that share data can be in the same or different AWS accounts or
different AWS Regions, so you can share data across organizations and collaborate
with other parties. consumer administrators receive the datashares that they are
granted usage for and review the contents of each datashare. To consume shared data,
the consumer administrator creates an Amazon Redshift database from the datashare. The
administrator then assigns permissions for the database to users and roles in the
consumer cluster. After permissions are granted, users and roles can list the shared
objects as part of the standard metadata queries, along with the local data on the
consumer cluster. They can start querying immediately.

If you are a _consumer with an active AWS Data Exchange subscription_ (also
known as subscribers on AWS Data Exchange), you can find, subscribe to, and query granular,
up-to-date data in Amazon Redshift without the need to extract, transform, and load the
data. For more information, see [AWS Data Exchange datashares](adx_datashare_overview.md "adx_datashare_overview.md").

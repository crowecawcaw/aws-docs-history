Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Types of datashares in Amazon Redshift

A _datashare_ is the unit of sharing data in Amazon Redshift.
Use datashares to share data in the same AWS account or different AWS accounts. Also,
share data for read purposes across different Amazon Redshift clusters.

Each datashare is associated with a specific database in your Amazon Redshift cluster.

A producer administrator can create datashares and add datashare objects to share data
with other clusters, referred to as _outbound_ shares. A
consumer administrator can receive datashares from other clusters, referred to as _inbound_ shares. For details on producers and consumers, see
[Datashare producers and
consumers](adx_datashare_overview.md#datashare_producer_consumer "adx_datashare_overview.md#datashare_producer_consumer").

Datashare objects are objects from specific databases on a cluster that producer
administrators can add to datashares to be shared with data consumers. Datashare objects
are read-only for data consumers. Examples of datashare objects are tables, views, and
user-defined functions. You can add datashare objects to datashares while creating
datashares or editing a datashare at any time.

Data sharing continues to work when clusters are resized or when the producer cluster is
paused.

There are different types of datashares: standard datashares, AWS Data Exchange datashares, and
AWS Lake Formation-managed datashares. The following pages provide an overview of each of
these.

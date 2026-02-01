Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Monitoring and auditing data sharing in Amazon Redshift

With Amazon Redshift, you can monitor and audit data sharing activities to ensure compliance and
security.

By auditing data sharing, producers can track the datashare evolution. For example,
auditing helps track when datashares are created, objects are added or removed, and
permissions are granted or revoked to Amazon Redshift clusters, AWS accounts, or AWS
Regions.

In addition to auditing, producers and consumers track datashare usage at various
granularities, such as account, cluster, and object levels. For more information about
tracking usage and auditing views, see [SVL_DATASHARE_CHANGE_LOG](r_SVL_DATASHARE_CHANGE_LOG.md "r_SVL_DATASHARE_CHANGE_LOG.md") and [SVL_DATASHARE_USAGE_PRODUCER](r_SVL_DATASHARE_USAGE_PRODUCER.md "r_SVL_DATASHARE_USAGE_PRODUCER.md").

You can monitor datashares by querying system views.

1. The producer administrator who wants to share data creates an Amazon Redshift datashare.
   The producer administrator then adds the needed database objects. These might be
   schemas, tables, and views to the datashare and specifies a list of consumers that
   the objects to be shared with.

Use the following system views to see consolidated views for tracking changes to
and usage of datashares on producer and/or consumer clusters:

    * [SYS\_DATASHARE\_CHANGE\_LOG](SYS_DATASHARE_CHANGE_LOG.md "SYS_DATASHARE_CHANGE_LOG.md")
    * [SYS\_DATASHARE\_USAGE\_CONSUMER](SYS_DATASHARE_USAGE_CONSUMER.md "SYS_DATASHARE_USAGE_CONSUMER.md")
    * [SYS\_DATASHARE\_USAGE\_PRODUCER](SYS_DATASHARE_USAGE_PRODUCER.md "SYS_DATASHARE_USAGE_PRODUCER.md")

Use the following system views to see datashare objects and data consumer
information for outbound datashares:

    * [SVV\_DATASHARES](r_SVV_DATASHARES.md "r_SVV_DATASHARES.md")
    * [SVV\_DATASHARE\_CONSUMERS](r_SVV_DATASHARE_CONSUMERS.md "r_SVV_DATASHARE_CONSUMERS.md")
    * [SVV\_DATASHARE\_OBJECTS](r_SVV_DATASHARE_OBJECTS.md "r_SVV_DATASHARE_OBJECTS.md")

2. The consumer administrators look at the datashares for which they're granted
   use and review the contents of each datashare by viewing inbound datashares using
   [SVV_DATASHARES](r_SVV_DATASHARES.md "r_SVV_DATASHARES.md").

To consume shared data, each consumer administrator creates an Amazon Redshift database
from the datashare. The administrator then assigns permissions to appropriate users
and roles in the consumer cluster. Users and roles can list the shared objects as
part of the standard metadata queries by viewing the following metadata system views
and can start querying data immediately.

    * [SVV\_REDSHIFT\_COLUMNS](r_SVV_REDSHIFT_COLUMNS.md "r_SVV_REDSHIFT_COLUMNS.md")
    * [SVV\_REDSHIFT\_DATABASES](r_SVV_REDSHIFT_DATABASES.md "r_SVV_REDSHIFT_DATABASES.md")
    * [SVV\_REDSHIFT\_FUNCTIONS](r_SVV_REDSHIFT_FUNCTIONS.md "r_SVV_REDSHIFT_FUNCTIONS.md")
    * [SVV\_REDSHIFT\_SCHEMAS](r_SVV_REDSHIFT_SCHEMAS.md "r_SVV_REDSHIFT_SCHEMAS.md")
    * [SVV\_REDSHIFT\_TABLES](r_SVV_REDSHIFT_TABLES.md "r_SVV_REDSHIFT_TABLES.md")

To view objects of both Amazon Redshift local and shared schemas and external schemas,
use the following metadata system views to query them.

    * [SVV\_ALL\_COLUMNS](r_SVV_ALL_COLUMNS.md "r_SVV_ALL_COLUMNS.md")
    * [SVV\_ALL\_SCHEMAS](r_SVV_ALL_SCHEMAS.md "r_SVV_ALL_SCHEMAS.md")
    * [SVV\_ALL\_TABLES](r_SVV_ALL_TABLES.md "r_SVV_ALL_TABLES.md")

When you connect to a consumer database, cross -database discovery is disabled. The
metadata system views only return metadata for the shared objects in the datashare
associated with the connected database.

## Integrating Amazon Redshift data sharing with AWS CloudTrail

Data sharing is integrated with AWS CloudTrail. CloudTrail is a service that provides a record
of actions taken by a user, a role, or an AWS service in Amazon Redshift. CloudTrail captures all
API calls for data sharing as events. The calls captured include calls from the AWS CloudTrail
console and code calls to the data sharing operations. For more information about
Amazon Redshift integration with AWS CloudTrail, see [Logging with CloudTrail](../mgmt/logging-with-cloudtrail.md "../mgmt/logging-with-cloudtrail.md").

For more information about CloudTrail, see [How CloudTrail works](../../../awscloudtrail/latest/userguide/how-cloudtrail-works.md "../../../awscloudtrail/latest/userguide/how-cloudtrail-works.md").

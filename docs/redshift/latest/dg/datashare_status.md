Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Datashare status values in Amazon Redshift

With Amazon Redshift, you can securely share live data across Amazon Redshift clusters without having to copy
or transfer data. Datashares for Amazon Redshift enables you to share live query results, including
updates to the source data, with any Amazon Redshift cluster in the same or different AWS accounts
and AWS Regions. This topic describes the possible statuses that datashares can have in
Amazon Redshift.

With cross-account datashares, there are different statuses of datashares that require
your actions. Your datashare can have a status of active, action required, or inactive.

Following describes each datashare status and its required action:

- When a producer administrator creates a datashare, the datashare status on the
  producer cluster is **Pending authorization**. The producer
  administrator can authorize data consumers to access the datashare. There isn't
  any action for the consumer administrator.
- When a producer administrator authorizes the datashare, the datashare status
  becomes **Authorized** on the producer cluster. There isn't any
  action for the producer administrator. When there is at least one association with a
  data consumer for the datashare, the datashare status changes from
  **Authorized** to **Active**.

The datashare share status then becomes **Available (Action required on
the Amazon Redshift console)** on the consumer cluster. The consumer
administrator can associate the datashare with data consumers or reject the
datashare. The consumer administrator can also use the AWS CLI command
`describeDatashareforConsumer` to view the status of datashares. Or the
administrator can use the CLI command `describeDatashare` and provide the
datashare Amazon Resource Name (ARN) to view the status of the datashare.

- When the consumer administrator associates a datashare with data consumers, the
  datashare status becomes **Active** on the producer cluster. When
  there is at least one association with a data consumer for the datashare, the
  datashare status changes from **Authorized** to
  **Active**. There isn't any action required for the producer
  administrator.

The datashare status becomes **Active** on the consumer cluster.
There isn't any action required for the consumer administrator.

- When the consumer administrator removes a consumer association from a datashare,
  the datashare status becomes either **Active** or
  **Authorized**. It becomes **Active** when there
  is at least one association exists for the datashare with another data consumer. It
  becomes **Authorized** when there isn't any consumer
  association with the datashare on the producer cluster. There isn't any action
  for the producer administrator.

The datashare status becomes **Action required** on the consumer
cluster if all associations are removed. The consumer administrator can reassociate a
datashare with data consumers when the datashare is available to the
consumers.

- When a consumer administrator declines a datashare, the datashare status on the
  producer cluster becomes **Action required** and
  **Declined** on the consumer cluster. The producer administrator
  can reauthorize the datashare. There isn't any action for the consumer
  administrator.
- When the producer administrator removes authorization from a datashare, the
  datashare's status becomes **Action required** on the producer
  cluster. The producer administrator can choose to reauthorize the datashare, if
  necessary. There isn't any action required for the consumer
  administrator.

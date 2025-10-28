# Enable dynamic partitioning in Amazon Data Firehose

You can configure dynamic partitioning for your Firehose streams through the Amazon Data Firehose
Management Console, CLI, or the APIs.

###### Important

You can enable dynamic partitioning only when you create a new Firehose stream.
You cannot enable dynamic partitioning for an existing Firehose stream that does not
have dynamic partitioning already enabled.

For detailed steps on how to enable and configure dynamic partitioning through the
Firehose management console while creating a new Firehose stream, see [Creating an Amazon Firehose stream](basic-create.md "basic-create.md"). When you get to the task of specifying the destination
for your Firehose stream, make sure to follow the steps in the [Configure destination settings](create-destination.md "create-destination.md") section, since currently, dynamic
partitioning is only supported for Firehose streams that use Amazon S3 as the destination.

Once dynamic partitioning on an active Firehose stream is enabled, you can update the
configuration by adding new or removing or updating existing partitioning keys and the
S3 prefix expressions. Once updated, Firehose starts using the new keys and the new S3
prefix expressions.

###### Important

Once you enable dynamic partitioning on a Firehose stream, it cannot be disabled
on this Firehose stream.

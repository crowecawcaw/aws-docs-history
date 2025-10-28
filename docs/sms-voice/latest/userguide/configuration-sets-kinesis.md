# Set up an Amazon Data Firehose event destination in AWS End User Messaging SMS

Amazon Data Firehose is a fully managed service for delivering real-time streaming data to multiple
types of destinations. Amazon Data Firehose is part of the Kinesis streaming data platform. To learn more
about Amazon Data Firehose, see the [Amazon Data Firehose Developer Guide](../../../firehose/latest/dev.md "../../../firehose/latest/dev.md").

Some of the examples in this section assume that you've already installed and configured
the AWS Command Line Interface. For more information about setting up the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

**Prerequisites**

1. Before you can create a Amazon Data Firehose event destination, you must first create a
   Amazon Data Firehose delivery stream. For more information about creating streams, see [Creating an
   Amazon Data Firehose Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") in the
   _Amazon Data Firehose Developer Guide_.

###### Important

You will need the Amazon Resource Name (ARN) of the Amazon Data Firehose delivery stream
to create the event destination. 2. You have to create an IAM role that allows AWS End User Messaging SMS to write to the delivery
stream, see [IAM policy for
Amazon Data Firehose](configuration-sets-kinesis-creating-role.md "configuration-sets-kinesis-creating-role.md").

###### Important

You will need the Amazon Resource Name (ARN) of the IAM role to create the
event destination. 3. You also have setup a configuration set to associate the event destinations with,
see [Create a configuration set in AWS End User Messaging SMS](configuration-set-create.md "configuration-set-create.md").

###### Topics

- [IAM policy for
  Amazon Data Firehose](configuration-sets-kinesis-creating-role.md "configuration-sets-kinesis-creating-role.md")
- [Create an Amazon Data Firehose event destination](configuration-set-kinesis-add.md "configuration-set-kinesis-add.md")
- [Edit an Amazon Data Firehose event destination](configuration-set-kinesis-edit.md "configuration-set-kinesis-edit.md")
- [Delete an Amazon Data Firehose event destination](configuration-set-kinesis-delete.md "configuration-set-kinesis-delete.md")

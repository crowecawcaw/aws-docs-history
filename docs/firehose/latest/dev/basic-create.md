# Tutorial: Create a Firehose stream from console

You can use the AWS Management Console or an AWS SDK to create a Firehose stream to your chosen destination.

You can update the configuration of your Firehose stream at any time after it’s created, using
the Amazon Data Firehose console or [UpdateDestination](../APIReference/API_UpdateDestination.md "../APIReference/API_UpdateDestination.md"). Your Firehose stream remains in the
`Active` state while your configuration is updated, and you can continue to
send data. The updated configuration normally takes effect within a few minutes. The version
number of a Firehose stream is increased by a value of `1` after you update the
configuration. It is reflected in the delivered Amazon S3 object name. For more information, see
[Configure Amazon S3 object name format](s3-object-name.md "s3-object-name.md").

Perform the steps in the following topics to create a Firehose stream.

###### Topics

- [Choose source and destination for your Firehose stream](create-name.md "create-name.md")
- [Configure source settings](configure-source.md "configure-source.md")
- [(Optional) Configure record transformation and format
  conversion](create-transform.md "create-transform.md")
- [Configure destination settings](create-destination.md "create-destination.md")
- [Configure backup settings](create-configure-backup.md "create-configure-backup.md")
- [Configure advanced settings](create-configure-advanced.md "create-configure-advanced.md")

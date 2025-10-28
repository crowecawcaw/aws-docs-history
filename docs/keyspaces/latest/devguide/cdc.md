# Working with change data capture (CDC) streams in Amazon Keyspaces

Amazon Keyspaces change data capture (CDC) records row-level change events from an Amazon Keyspaces table in near-real time.

Amazon Keyspaces CDC enables event-driven use cases such as industrial IoT and fraud detection
as well as data processing use cases like full-text search and data archival. The change events that Amazon Keyspaces CDC
captures in streams can be consumed by downstream
applications that perform business-critical functions such as data analytics, text search, ML training/inference,
and continuous data backups for archival. For example, you can transfer stream data
to AWS analytics and storage services like Amazon OpenSearch Service, Amazon Redshift, and Amazon S3 for further processing.

Amazon Keyspaces CDC offers time-ordered and de-duplicated change records for tables, with automatic scaling of
data throughput and retention time of up to 24 hours.

Amazon Keyspaces CDC streams are completely serverless, and you don't need to manage the data infrastructure for
capturing change events. In addition, Amazon Keyspaces CDC doesn't consume any table capacity for either compute or
storage. For more information, see [How change data capture (CDC) streams work in Amazon Keyspaces](cdc_how-it-works.md "cdc_how-it-works.md").

You can use the Amazon Keyspaces Streams API to build applications that consume Amazon Keyspaces CDC streams and take action based
on the contents. For available endpoints, see [How to access CDC stream endpoints in
Amazon Keyspaces](CDC_access-endpoints.md "CDC_access-endpoints.md").

For a complete listing of all operations available for Amazon Keyspaces in the Streams API, see [_Amazon Keyspaces Streams API Reference_](../StreamsAPIReference/Welcome.md "../StreamsAPIReference/Welcome.md").

###### Topics

- [How change data capture (CDC) streams work in Amazon Keyspaces](cdc_how-it-works.md "cdc_how-it-works.md")
- [How to use change data capture (CDC) streams in Amazon Keyspaces](cdc_how-to-use.md "cdc_how-to-use.md")

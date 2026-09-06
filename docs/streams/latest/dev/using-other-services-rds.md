

# Write to Kinesis Data Streams using Amazon Relational Database Service
<a name="using-other-services-rds"></a>

You can use Amazon Kinesis Data Streams to monitor activities on your Amazon RDS instances. Using Database Activity Streams, Amazon RDS pushes activities to a Kinesis data stream in real-time. You can then build applications for compliance management that consume these activities, audit them and generate alerts. You can also use Amazon Data Firehose to store the data.

For more information, see [Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html) in the *Amazon RDS Developer Guide*. 
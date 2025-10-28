# Loading streaming data from Amazon Data Firehose

Firehose supports OpenSearch Service as a delivery destination. For instructions about how to load
streaming data into OpenSearch Service, see [Creating a
Kinesis Data Firehose Delivery Stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md") and [Choose
OpenSearch Service for Your Destination](../../../firehose/latest/dev/create-destination.md#create-destination-elasticsearch "../../../firehose/latest/dev/create-destination.md#create-destination-elasticsearch") in the
_Amazon Data Firehose Developer Guide_.

Before you load data into OpenSearch Service, you might need to perform transforms on the data. To
learn more about using Lambda functions to perform this task, see [Amazon Kinesis Data Firehose Data
Transformation](../../../firehose/latest/dev/data-transformation.md "../../../firehose/latest/dev/data-transformation.md") in the same guide.

As you configure a delivery stream, Firehose features a "one-click" IAM role that gives
it the resource access it needs to send data to OpenSearch Service, back up data on Amazon S3, and
transform data using Lambda. Because of the complexity involved in creating such a role
manually, we recommend using the provided role.

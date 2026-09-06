

# Amazon DynamoDB in AWS GovCloud (US)
<a name="govcloud-ddb"></a>

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. You can use Amazon DynamoDB to create a database table that can store and retrieve any amount of data, and serve any level of request traffic. Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon DynamoDB differs
<a name="govcloud-ddb-diffs"></a>

The following differences apply to Amazon DynamoDB:
+  **Export Table** is not available in the DynamoDB console.
+  [DynamoDB Accelerator(DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) and [Global tables multi-Region strong consistency (MRSC)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.html#V2globaltables_HowItWorks.consistency-modes) are not available.
+  [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) is not available for DynamoDB.

## Documentation
<a name="govcloud-ddb-docs"></a>
+  [Amazon DynamoDB documentation](http://aws.amazon.com/documentation/dynamodb/) 

## Export-controlled content
<a name="govcloud-ddb-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  DynamoDB metadata is not permitted to contain export-controlled data. This metadata includes all the configuration data that you enter when creating and maintaining your DynamoDB tables, such as table names, hash attribute names, and range attribute names.
+ Do not enter export-controlled data in the following fields:
  + Table names
  + Hash attribute names
  + Range attribute names
  + Resource tags

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md).
# Amazon DynamoDB in AWS GovCloud (US)

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. You can use Amazon DynamoDB to create a database table that can store and retrieve any amount of data, and serve any level of request traffic. Amazon DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified by the customer and the amount of data stored, while maintaining consistent and fast performance.

## How Amazon DynamoDB differs for AWS GovCloud (US)

- **Export Table** is not available in the DynamoDB console.
- [DynamoDB Accelerator(DAX)](../../../amazondynamodb/latest/developerguide/DAX.md "../../../amazondynamodb/latest/developerguide/DAX.md") and [Global tables multi-Region strong consistency (MRSC)](../../../amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes "../../../amazondynamodb/latest/developerguide/V2globaltables_HowItWorks.md#V2globaltables_HowItWorks.consistency-modes") are not available.
- [AWS
  PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") is not supported for DynamoDB.

## Documentation for Amazon DynamoDB

[Amazon DynamoDB
documentation](http://aws.amazon.com/documentation/dynamodb/ "http://aws.amazon.com/documentation/dynamodb/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- DynamoDB metadata is not permitted to contain export-controlled data. This metadata
  includes all the configuration data that you enter when creating and maintaining your
  DynamoDB tables, such as table names, hash attribute names, and range attribute names.
- Do not enter export-controlled data in the following fields:
  - Table names
  - Hash attribute names
  - Range attribute names
  - Resource tags

If you are processing export-controlled data with this service,
use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").

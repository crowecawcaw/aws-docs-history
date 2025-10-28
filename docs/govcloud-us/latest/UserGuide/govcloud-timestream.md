# Amazon Timestream in AWS GovCloud (US)

This service is currently available in AWS GovCloud (US-West) only.

Timestream is a fast, scalable, and serverless time series database service for IoT and
operational applications. With Timestream, you can store and analyze trillions of events per
day up to 1,000 times faster than with relational databases—at as little as one-tenth of the
cost.

Timestream saves you time and cost in managing the lifecycle of time series data by
keeping recent data in memory and moving historical data to a cost-optimized storage tier,
based upon user-defined policies.

With the purpose-built query engine in Timestream, you can access and analyze recent
and historical data together, without needing to specify explicitly in the query whether the
data resides in memory or in the cost-optimized storage tier.

Timestream helps ensure that your time series data is always encrypted, whether at
rest or in transit. With Timestream, you can also specify an AWS KMS customer managed
key for encrypting data in the magnetic store.

## How Amazon Timestream differs for

AWS GovCloud (US)

The AWS GovCloud (US) Region implementation of Amazon Timestream is unique in the
following ways.

- The query editor in the Timestream console does not allow you to save your
  queries for later usage or search from saved queries.
- Customers who rely upon FIFO support with SNS notifications from the scheduled
  query service for Timestream will not be able to create such a topic in
  GovCloud since the Region does not support FIFO topics. For more information,
  see [Amazon SNS in AWS GovCloud (US)](govcloud-sns.md "govcloud-sns.md"). This might
  cause notifications for scheduled queries to arrive out of order.

## Documentation for Amazon Timestream

[Timestream documentation](../../../timestream/latest/developerguide/what-is-timestream.md "../../../timestream/latest/developerguide/what-is-timestream.md").

## Export-controlled content

For AWS services architected within the AWS GovCloud (US) Regions, the following list
explains how certain components of data may leave the AWS GovCloud (US) Regions in the
normal course of the service offerings. The list can be used as a guide to help meet
applicable customer compliance obligations. Data not included in the following list
remains within the AWS GovCloud (US) Regions.

- Amazon Timestream metadata is not permitted to contain export-controlled
  data. This metadata includes all configuration data that you enter when creating
  and maintaining your Amazon Timestream instances except the master
  password.
- Do not enter export-controlled data in the following fields.
  - Master user name
  - Database name
  - Table name
  - Scheduled query, Query Name
  - Resource tags

If you are processing export-controlled data with Amazon Timestream, follow these
guidelines in order to maintain export compliance.

- When you use the console or the AWS APIs, the only data field that is
  protected as export-controlled data is the Amazon Timestream master
  password.
- You can enter export-controlled data into any data fields by using your
  database client-side tools. Do not pass export-controlled data by using the web
  service APIs that are provided by Amazon Timestream.
- To secure export-controlled data in your VPC, set up access control lists
  (ACLs) to control traffic entering and exiting your VPC. If you have multiple
  databases configured with different ports, set up ACLs on all the ports.

For example, if you're running an application server on an Amazon EC2 instance
that connects to Amazon Timestream, a non-U.S. person could reconfigure the
DNS to redirect export-controlled data out of the VPC and into any server that
could possibly be outside of the AWS GovCloud (US) Regions.

To prevent this type of attack and to maintain export compliance, use network
ACLs to prevent network traffic from exiting the VPC on the database port. For
more information, see [Network ACLs](../../../vpc/latest/userguide/VPC_ACLs.md "../../../vpc/latest/userguide/VPC_ACLs.md") in the
_Amazon VPC User Guide_.

- For each database that contains export-controlled data, ensure that only
  specific CIDR ranges and Amazon EC2 security groups can access the database
  instance, especially when an Internet gateway is attached to the VPC. Only allow
  connections that are from the AWS GovCloud (US) Regions or other export-controlled
  environments to export-controlled database instances.
- If you are processing export-controlled data with this service, use the SSL
  (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").

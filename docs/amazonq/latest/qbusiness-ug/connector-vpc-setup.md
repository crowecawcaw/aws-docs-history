# Set up an Amazon Q Business data

source to connect to Amazon VPC

When you add a new data source in Amazon Q Business, you can use the
Amazon VPC feature if the selected data source connector supports
this feature.

You can set up a new Amazon Q Business data source with Amazon VPC enabled by using the AWS Management Console or the Amazon Q Business API.
Specifically, use the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") API operation,
and then use the `VpcConfiguration` parameter to provide the
following information:

- `SubnetIds` – A list of identifiers of Amazon VPC subnets
- `SecurityGroupIds` – A list of identifiers of
  Amazon VPC security groups
  If you use the console, you provide the required Amazon VPC
  information during connector configuration. To use the console to enable the
  Amazon VPC feature for a connector, you first choose an Amazon VPC. Then, you provide
  identifiers of any Amazon VPC subnets and identifiers of any Amazon VPC security groups.
  You can choose the Amazon VPC subnets and Amazon VPC security groups that you created in
  [Configuring Amazon VPC](connector-vpc-steps.md "connector-vpc-steps.md"), or use any existing
  ones.

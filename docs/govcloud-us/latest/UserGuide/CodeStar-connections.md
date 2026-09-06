

# AWS CodeConnections in AWS GovCloud (US)
<a name="CodeStar-connections"></a>

You can use the connections feature in the Developer Tools console to connect AWS resources to external code repositories. This feature has its own API, the [AWS CodeStar Connections API reference](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/Welcome.html). Each connection is a resource that you can give to AWS services to connect to a third-party repository, such as BitBucket. For example, you can add a connection in CodePipeline so that it starts your pipeline when a code change is made to your third-party code repository. Each connection is named and associated with a unique Amazon Resource Name (ARN) that is used to reference the connection.

## How AWS CodeStar Connections differs
<a name="how_shared_acs_connections_differs"></a>

The following differences apply to AWS CodeStar Connections:
+ Since AWS GovCloud (US) operates as isolated Regions, you cannot share or use connections resources with other services outside of the Regions. For example, you cannot use a connection in AWS GovCloud (US-East) with a pipeline in CodePipeline that is not in the AWS GovCloud (US-East) Region.

## Documentation
<a name="w132aac16c94b7"></a>
+  [AWS CodeStar Connections documentation](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html) 

## Export-controlled content
<a name="w132aac16c94b9"></a>

For AWS services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
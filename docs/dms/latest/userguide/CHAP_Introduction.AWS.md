# Using AWS DMS with other AWS services

You can use AWS DMS with several other AWS services:

- You can use an Amazon EC2 instance or Amazon RDS DB instance as a target for a data
  migration.
- You can use DMS Schema Conversion to convert your source schema and SQL
  code into a format compatible with the target database.
- You can use Amazon S3 as a storage site for your data, or you can use it as an
  intermediate step when migrating large amounts of data.
- You can use CloudFormation to set up your AWS resources for infrastructure management
  or deployment. For example, you can provision AWS DMS resources such as
  replication instances, tasks, certificates, and endpoints. You create a template
  that describes all the AWS resources that you want, and CloudFormation provisions and
  configures those resources for you.

## AWS DMS support for AWS CloudFormation

You can provision AWS DMS resources using AWS CloudFormation. AWS CloudFormation is a service that
helps you model and set up your AWS resources for infrastructure management or
deployment. For example, you can provision AWS DMS resources such as replication
instances, tasks, certificates, and endpoints. You create a template that describes
all the AWS resources that you want and AWS CloudFormation provisions and configures those
resources for you.

As a developer or system administrator, you can create and manage collections of
these resources that you can then use for repetitive migration tasks or deploying
resources to your organization. For more information about AWS CloudFormation, see [AWS CloudFormation concepts](../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md "../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.md") in the
_AWS CloudFormation User Guide._

AWS DMS supports creating the following AWS DMS resources using AWS CloudFormation:

- [AWS::DMS::Certificate](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.md")
- [AWS::DMS::Endpoint](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.md")
- [AWS::DMS::EventSubscription](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.md")
- [AWS::DMS::ReplicationInstance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.md")
- [AWS::DMS::ReplicationSubnetGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.md")
- [AWS::DMS::ReplicationTask](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.md")

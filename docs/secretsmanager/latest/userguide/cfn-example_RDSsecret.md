# Create an AWS Secrets Manager secret with automatic rotation and an

Amazon RDS MySQL DB instance with AWS CloudFormation

To create an admin secret for Amazon RDS or Aurora, we recommend you use `ManageMasterUserPassword`, as shown in the example _Create a Secrets Manager secret for a master password_ in [`AWS::RDS::DBCluster`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.md"). Then Amazon RDS creates the secret and manages rotation for you. For more information, see [Managed rotation](rotate-secrets_managed.md "rotate-secrets_managed.md").

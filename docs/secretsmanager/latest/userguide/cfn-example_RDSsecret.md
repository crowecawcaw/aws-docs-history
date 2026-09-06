

# Create an AWS Secrets Manager secret with automatic rotation and an Amazon RDS MySQL DB instance with CloudFormation
<a name="cfn-example_RDSsecret"></a>

To create an admin secret for Amazon RDS or Aurora, we recommend you use `ManageMasterUserPassword`, as shown in the example *Create a Secrets Manager secret for a master password* in [`AWS::RDS::DBCluster`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html). Then Amazon RDS creates the secret and manages rotation for you. For more information, see [Managed rotation](rotate-secrets_managed.md).
# AWS CloudFormation Ingest Guidelines, Best Practices, and Limitations

For AMS to process your CloudFormation template, there are some guidelines and restrictions.

## Guidelines

To reduce AWS CloudFormation errors while performing AWS CloudFormation ingest, follow these
guidelines:

- **Don't embed credentials or other sensitive information in the template** – The CloudFormation
  template is visible in the AWS CloudFormation console, so you don't want to embed credentials or sensitive data in the template. The template can't contain
  sensitive information. The following resources are allowed only if you use AWS Secrets Manager for the value:
  - `AWS::RDS::DBInstance` - [MasterUserPassword,TdeCredentialPassword]
  - `AWS::RDS::DBCluster` - [MasterUserPassword]
  - `AWS::ElastiCache::ReplicationGroup` - [AuthToken]

###### Note

For information about using an AWS Secrets Manager secret in a resource property, see
[How to create and retrieve secrets managed in AWS Secrets Manager using AWS CloudFormation templates](https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/ "https://aws.amazon.com/blogs/security/how-to-create-and-retrieve-secrets-managed-in-aws-secrets-manager-using-aws-cloudformation-template/") and
[Using Dynamic References to Specify Template Values](../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md "../../../AWSCloudFormation/latest/UserGuide/dynamic-references.md").

- **Use Amazon RDS snapshots to create RDS DB instances** – By
  doing this you avoid having to provide a MasterUserPassword.
- If the template you submit contains an IAM instance profile, it must be prefixed with
  'customer'. For example, using an instance profile with the
  name 'example-instance-profile', causes failure. Instead, use an instance profile with the
  name 'customer-example-instance-profile'.
- **Don't include any sensitive data in `AWS::EC2::Instance`** - [UserData]. UserData should
  not contain passwords, API keys, or any other sensitive data. This type of data can be encrypted and stored in an S3 bucket and downloaded onto the
  instance using UserData.
- **IAM policy creation using CloudFormation templates is supported with constraints** –

IAM policies have to be reviewed and approved by AMS SecOps. Currently we only support deploying IAM roles with in-line policies
that contain pre-approved permissions. In other cases, IAM policies can't be created using CloudFormation templates because that
would override the AMS SecOps process.

- **SSH KeyPairs aren't supported** – Amazon EC2 instances must be accessed through the AMS access management
  system. The AMS RFC process authenticates you. You cannot include SSH keypairs in CloudFormation templates because you don't have the permissions
  to create SSH keypairs and override the AMS access management model.
- **Security Group ingress rules are restricted** – You can't have a source CIDR range from 0.0.0.0/0, or a
  publicly routable address space, with a TCP port that is anything other than 80 or 443.
- **Follow AWS CloudFormation guidelines when writing CloudFormation resource templates** –
  Ensure that you use the right data type/property name for the resource by referring to the _AWS CloudFormation User Guide_
  for that resource. For example, the data type of SecurityGroupIds property in an AWS::EC2::Instance resource is 'List of String values', so ["sg-aaaaaaaa"]
  is ok (with brackets), but "sg-aaaaaaaa" is not (without brackets).

For more information, see
[AWS Resource and Property Types Reference](../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md "../../../AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.md").

- **Configure your custom CloudFormation templates to use parameters defined in the AMS CloudFormation ingest CT** –
  When you configure your CloudFormation template to use parameters defined in the AMS CloudFormation ingest CT, you can reuse the CloudFormation template to create
  similar stacks by submitting it with changed parameter values in the CT input with the Management | Custom stack | Stack from CloudFormation template | Update CT
  (ct-361tlo1k7339x). For an example, see [AWS CloudFormation Ingest examples: Defining resources](cfn-ingest-ex-define-resource.md "cfn-ingest-ex-define-resource.md").
- **Amazon S3 bucket endpoints with a presigned URL can't be expired** –
  If you are using an Amazon S3 bucket endpoint with a presigned URL, verify that the presigned Amazon S3 URL isn't expired. A
  CloudFormation ingest RFC submitted with an expired presigned Amazon S3 bucket URL is rejected.
- **Wait Condition requires signal logic** –
  Wait Condition is used to coordinate stack resource creation with configuration actions that are external to the stack creation. If you use
  the Wait Condition resource in the template, AWS CloudFormation waits for a success signal, and it marks stack creation as a failure if the number of success
  signals aren't made. You need to have a logic for the signal if you use the Wait Condition resource. For more information, see
  [Creating Wait Conditions in a Template](../../../AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-waitcondition.md").

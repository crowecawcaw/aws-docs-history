# Service-linked role permissions for

Amazon MSK

Amazon MSK uses the service-linked role named **AWSServiceRoleForKafka**.
Amazon MSK uses this role to access your resources and perform operations such as:

- `*NetworkInterface` – create and manage network
  interfaces in the customer account that make cluster brokers accessible to clients in the customer VPC.
- `*VpcEndpoints` – manage VPC endpoints in the customer
  account that make cluster brokers accessible to clients in the customer VPC
  using AWS PrivateLink. Amazon MSK uses
  permissions to `DescribeVpcEndpoints`, `ModifyVpcEndpoint` and `DeleteVpcEndpoints`.
- `secretsmanager` – manage client credentials with AWS Secrets Manager.
- `GetCertificateAuthorityCertificate` – retrieve the certificate for your private certificate authority.
  This service-linked role is attached to the following managed policy:
  `KafkaServiceRolePolicy`. For updates to this policy, see [KafkaServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-KafkaServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-KafkaServiceRolePolicy").

The AWSServiceRoleForKafka service-linked role trusts the following services to assume the
role:

- `kafka.amazonaws.com`
  The role permissions policy allows Amazon MSK to complete the following actions on resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:AttachNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DetachNetworkInterface",
 "ec2:DescribeVpcEndpoints",
 "acm-pca:GetCertificateAuthorityCertificate",
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:ModifyVpcEndpoint"
 ],
 "Resource": "arn:*:ec2:*:*:subnet/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteVpcEndpoints",
 "ec2:ModifyVpcEndpoint"
 ],
 "Resource": "arn:*:ec2:*:*:vpc-endpoint/*",
 "Condition": {
 "StringEquals": {
 "ec2:ResourceTag/AWSMSKManaged": "true"
 },
 "StringLike": {
 "ec2:ResourceTag/ClusterArn": "*"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:PutResourcePolicy",
 "secretsmanager:DeleteResourcePolicy",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "secretsmanager:SecretId": "arn:*:secretsmanager:*:*:secret:AmazonMSK_*"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

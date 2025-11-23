# Service-linked role to configure and launch products in AWS Marketplace

AWS Marketplace uses the service-linked role named
`AWSServiceRoleForMarketplaceDeployment` to allow
AWS Marketplace to manage deployment-related parameters, which are stored as secrets
in [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"), on your behalf. These secrets can be referenced by sellers
in CloudFormation templates, which you can launch when configuring products that have Quick
Launch enabled in
AWS Marketplace.

The `AWSServiceRoleForMarketplaceDeployment` service-linked
role trusts the following services to assume the role:

- `deployment.marketplace.amazonaws.com`
  The `AWSMarketplaceDeploymentServiceRolePolicy` allows
  AWS Marketplace to complete the following actions on your resources.

###### Note

For more information about AWS Marketplace managed policies, see [AWS managed policies for AWS Marketplace
buyers](buyer-security-iam-awsmanpol.md "buyer-security-iam-awsmanpol.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageMarketplaceDeploymentSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret",
 "secretsmanager:PutSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:DeleteSecret",
 "secretsmanager:RemoveRegionsFromReplication"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:*:secret:marketplace-deployment*!*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "ListSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:ListSecrets"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "TagMarketplaceDeploymentSecrets",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:TagResource"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:marketplace-deployment!*",
 "Condition": {
 "Null": {
 "aws:RequestTag/expirationDate": "false"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "expirationDate"
 ]
 },
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

You must configure permissions to allow your users, groups, or roles to create,
edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

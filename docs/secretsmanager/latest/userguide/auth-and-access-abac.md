# Control access to secrets using attribute-based access control (ABAC)

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes or characteristics of the user, the data, or the environment, such as the department, business unit, or other factors that could affect the authorization outcome. In AWS, these attributes are called _tags_.

Using tags to control permissions is helpful in environments that are growing rapidly and helps with situations where policy management becomes cumbersome. ABAC rules are evaluated dynamically at runtime, which means that the users' access to applications and data and the type of allowed operations automatically change based on the contextual factors in the policy. For example, if a user changes department, access is automatically adjusted without the need to update permissions or request new roles. For more information, see: [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"), [Define
permissions to access secrets based on tags.](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md"), and [Scale your authorization needs for Secrets Manager using ABAC with IAM Identity Center](https://aws.amazon.com/blogs/security/scale-your-authorization-needs-for-secrets-manager-using-abac-with-iam-identity-center/ "https://aws.amazon.com/blogs/security/scale-your-authorization-needs-for-secrets-manager-using-abac-with-iam-identity-center/").

## Example: Allow an identity access to secrets that have specific tags

The following policy allows `DescribeSecret` access on secrets with a tag with the key `ServerName` and the value `ServerABC`. If you attach this policy to an identity, the identity has permission to any secrets with that tag in the account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "secretsmanager:DescribeSecret",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "secretsmanager:ResourceTag/`ServerName`": "`ServerABC`"
 }
 }
 }
}`

```

## Example: Allow access only to identities with tags that match secrets' tags

The following policy allows any identities in the account `GetSecretValue` access to any secrets in the account where the identity's `AccessProject` tag has the same value as the secret's `AccessProject` tag.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Principal": {
 "AWS": "123456789012"
 },
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`AccessProject`": "${ aws:PrincipalTag/`AccessProject` }"
 }
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*"
 }
}`

```

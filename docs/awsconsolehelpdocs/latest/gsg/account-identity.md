# Allow AWS Management Console use for expected accounts and

organizations only (trusted identities)

AWS Management Console and AWS Sign-In support a VPC endpoint policy that specifically controls the
identity of the signed-in account.

Unlike other VPC endpoint policies, the policy is evaluated before authentication. As a
result, it specifically controls sign-in and use of the authenticated session only, and not
any AWS service-specific actions that the session takes. For example, as the session
accesses an AWS service console, such as the Amazon EC2 console, these VPC endpoint policies
will not be evaluated against the Amazon EC2 actions that are taken to display that page. Rather,
you can use the IAM policies associated with the signed-in IAM Principal to control its
permission to AWS service actions.

###### Note

VPC endpoint policies for AWS Management Console and SignIn VPC endpoints support only a limited
subset of policy formulations. Every `Principal` and `Resource`
should be set to `*` and the `Action` should be either
`*` or `signin:*`. You control access to VPC endpoints using
`aws:PrincipalOrgId` and `aws:PrincipalAccount` condition
keys.

The following policies are recommended for both the Console and SignIn VPC
endpoints.

This VPC endpoint policy allows sign-in to AWS accounts in the specified AWS
organization and blocks sign-in to any other accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": "*",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgId": "o-xxxxxxxxxxx"
 }
 }
 }
 ]
}`

```

This VPC endpoint policy limits sign-in to a list of specific AWS accounts and blocks
sign-in to any other accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": "*",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalAccount": [ "111122223333", "222233334444" ]
 }
 }
 }
 ]
}`

```

Polices that limit AWS accounts or an organization on the AWS Management Console and Sign-In VPC
endpoints are evaluated at the time of sign-in and are periodically re-evaluated for
existing sessions.

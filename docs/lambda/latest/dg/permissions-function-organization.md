# Granting function access to an organization

To grant permissions to an organization in [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"), specify the organization ID as the `principal-org-id`.
The following [add-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html") command grants invocation access to all users in organization `o-a1b2c3d4e5f`.

```
`aws lambda add-permission \
 --function-name example \
 --statement-id PrincipalOrgIDExample \
 --action lambda:InvokeFunction \
 --principal * \
 --principal-org-id o-a1b2c3d4e5f`
```

###### Note

In this command, `Principal` is `*`. This means that all users in the organization
`o-a1b2c3d4e5f` get function invocation permissions. If you specify an AWS account or role as the
`Principal`, then only that principal gets function invocation permissions, but only if they are
also part of the `o-a1b2c3d4e5f` organization.

This command creates a resource-based policy that looks like the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PrincipalOrgIDExample",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "lambda:InvokeFunction",
 "Resource": "arn:aws:lambda:us-east-2:123456789012:function:example",
 `"Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "o-a1b2c3d4e5f"
 }
 }`
 }
 ]
}`

```

For more information, see [aws:PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") in the _IAM user guide_.

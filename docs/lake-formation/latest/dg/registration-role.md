# Requirements for roles used to register

locations

You must specify an AWS Identity and Access Management (IAM) role when you register an Amazon Simple Storage Service (Amazon S3) location.
AWS Lake Formation assumes that role when accessing the data in that location.

You can use one of the following role types to register a location:

- The Lake Formation service-linked role. This role grants the required permissions on the
  location. Using this role is the simplest way to register the location. For more
  information, see [Using service-linked roles for Lake Formation](service-linked-roles.md "service-linked-roles.md") and [Service-linked role limitations](service-linked-role-limitations.md "service-linked-role-limitations.md").
- A user-defined role. Use a user-defined role when you need to grant more
  permissions than the service-linked role provides.

You must use a user-defined role in the following circumstances:

    + When registering a location in another account.


    For more information, see [Registering an Amazon S3 location in another AWS
     account](register-cross-account.md "register-cross-account.md") and
     [Registering an encrypted Amazon S3 location across AWS
     accounts](register-cross-encrypted.md "register-cross-encrypted.md").
    + If you used an AWS managed CMK (`aws/s3`) to encrypt the Amazon S3
     location.


    For more information, see [Registering an encrypted Amazon S3 location](register-encrypted.md "register-encrypted.md").
    + If you plan to access the location using Amazon EMR.


    If you already registered a location with the service-linked role and want
     to begin accessing the location with Amazon EMR, you must deregister the location
     and reregister it with a user-defined role. For more information, see [Deregistering an Amazon S3 location](unregister-location.md "unregister-location.md").

The following are the requirements for a user-defined role:

- When creating the new role, on the **Create role** page of the
  IAM console, choose **AWS service**, and then under
  **Choose a use case**, choose **Lake
  Formation**.

If you create the role using a different path, ensure that the role has a trust
relationship with `lakeformation.amazonaws.com`. For more information,
see [Modifying a role trust policy (Console)](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md").

- The role must have an inline policy that grants Amazon S3 read/write permissions on the
  location. The following is a typical policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::awsexamplebucket/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::awsexamplebucket"
 ]
 }
 ]
}`

```

- Add the following trust policy to the IAM role to allow the Lake Formation service to
  assume the role and vend temporary credentials to the integrated analytical engines.

To include IAM Identity Center user context in the CloudTrail logs, the trust policy must have the
permission for the `sts:SetContext` action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DataCatalogViewDefinerAssumeRole1",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "lakeformation.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ]
 }
 ]
}`

```

- The data lake administrator who registers the location must have the
  `iam:PassRole` permission on the role.

The following is an inline policy that grants this permission. Replace
`<account-id>` with a valid AWS account number,
and replace `<role-name>` with the name of the
role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PassRolePermissions",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`<role-name>`"
 ]
 }
 ]
}`

```

- To permit Lake Formation to add logs in CloudWatch Logs and publish metrics, add the following inline
  policy.

###### Note

Writing to CloudWatch Logs incurs a charge.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Sid1",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:CreateLogGroup",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-lakeformation-acceleration/*",
 "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws-lakeformation-acceleration/*:log-stream:*"
 ]
 }
 ]
}`

```

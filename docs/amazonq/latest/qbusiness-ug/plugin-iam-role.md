# IAM role for Amazon Q Business plugins

To successfully connect Amazon Q Business to a plugin, you need to give Amazon Q Business the following permissions using a service access role:

- Permission to access your Secrets Manager secret to get the credentials you use to
  log in to the third party service instance you are creating a plugin for.
- **(Optional)** Permission to access the customer managed
  AWS KMS key used to encrypt the content of your Secrets Manager
  secret.
  Amazon Q Business assumes this role to access your third party service instance
  credentials.

If you use the console and choose to create a new IAM role, Amazon Q creates the IAM role for you. If you use the console and choose to use an
existing secret, or you use the API, make sure your secret contains the following permissions.

###### Important

If you're changing response settings for an Amazon Q Business application created
and deployed before 16 April, 2024, you need to update your web experience service role. For
information on service role permissions needed, see [IAM role for an Amazon Q Business web experience](iam-roles.md#deploy-experience-iam-role "iam-roles.md#deploy-experience-iam-role"). For
information on how to update your web experience service role, see [Updating a web experience](supported-exp-actions.md#update-web-experience "supported-exp-actions.md#update-web-experience").

The following is the service access IAM role required:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowQBusinessToGetSecretValue",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:111122223333:secret:[[secret_id]]"
 ]
 }
 ]
}`

```

**To allow Amazon Q Business to assume a role, use the following
trust policy:**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessApplicationTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "qbusiness.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```

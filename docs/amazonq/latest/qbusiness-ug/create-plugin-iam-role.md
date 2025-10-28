# Service access roles for Amazon Q Business custom plugins

To connect Amazon Q Business to third party applications that require
authentication, you need to give the Amazon Q role permissions to access your Secrets Manager
secret. This will enable an Amazon Q Business custom plugin to access the
credentials needed to log in to the third party service.

- Permission to access your Secrets Manager secret to get the credentials you
  use to log in to the third party service instance you are creating a plugin
  for.
  You don't have to provide this role for custom plugins that don't require
  authentication.

###### Important

If you're changing response settings for an Amazon Q application
created and deployed before 16 April, 2024, you need to update your web experience
service role. For information on service role permissions needed, see [IAM role for an Amazon Q web experience](iam-roles.md#deploy-experience-iam-role "iam-roles.md#deploy-experience-iam-role").
For information on how to update your web experience service role, see [Updating a web experience](supported-exp-actions.md#update-web-experience "supported-exp-actions.md#update-web-experience").

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

**To allow Amazon Q to assume a role, use the following trust
policy:**

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

Amazon Q assumes this role to access your third party service instance
credentials.

If you use the console and choose to create a new IAM role, Amazon Q
creates the IAM role for you. If you use the console and choose to use an
existing secret, or you use the API, make sure your secret contains the permissions
above. For more information on creating IAM roles, see [Creating IAM
roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").

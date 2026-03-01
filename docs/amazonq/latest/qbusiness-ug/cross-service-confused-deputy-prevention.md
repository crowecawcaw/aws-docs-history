# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_). The
calling service can be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to access. To prevent this, AWS
provides tools that help you protect your data for all services with service principals that
have been given access to resources in your account.

We recommend using the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") global condition context key in resource
policies to limit the permissions that Amazon Q Business gives another service to the
resource.

The value of `aws:SourceArn` must be `qbusiness::Application`.

The following example—which grants Amazon Q Business permission to perform a
decryption action on an AWS KMS key within the scope of an Amazon Q Business
application—shows how you can use the `aws:SourceArn`
global condition context key in
Amazon Q Business to prevent the confused deputy problem.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid": "ConfusedDeputyPreventionExamplePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "`qbusiness`.amazonaws.com"
 },
 "Action": "kms:Decrypt",
 "Resource": [
 "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`/*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/*"
 }
 }
 }
}`

```

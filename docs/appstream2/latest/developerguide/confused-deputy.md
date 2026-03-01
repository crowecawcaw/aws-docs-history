# Amazon WorkSpaces Applications Cross-Service Confused Deputy Prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action coerces a more-privileged entity to perform the action. In
AWS, cross-service impersonation can leave account resources vulnerable to the confused
deputy problem. Cross-service impersonation occurs when one service (the _calling
service_) calls another service (the _called service_). The
calling service can manipulate the called service to use its permissions to act on a
customer's resources in ways that the calling service doesn't have permission to perform for
itself. To prevent this, AWS provides tools that helps you protect your data for all
services with service principals that have access to resources in your account.

We recommend using the `aws:SourceArn` and `aws:SourceAccount`
global condition context keys in resource policies to limit permissions when accessing these
resources. The following guidelines detail recommendations and requirements when you use
these keys to protect your resources:

- Use `aws:SourceArn` if you want only one resource associated with
  cross-service access.
- Use `aws:SourceAccount` if you want to allow any resource in the
  specified account associated with cross-service use.
- If the `aws:SourceArn` key doesn't contain an account ID, you must use
  both global condition context keys (`aws:SourceArn` and
  `aws:SourceAccount`) to limit permissions.
- If you use both global condition context keys and the `aws:SourceArn`
  value contains an account ID, the `aws:SourceAccount` key must use the
  same account ID when used in the same policy statement.
  The most effective way to protect against the confused deputy problem is to use the exact
  Amazon Resource Name (ARN) of the resource you want to allow. If you don't know the full ARN
  of the resource, use the `aws:SourceArn` global context condition key with
  wildcards (such as **\***) for the unknown portions of the ARN. You can also use
  a wildcard in the ARN if you want to specify multiple resources. For example, you can format
  the ARN as
  `arn:aws:`servicename`::`region-name`::`your
  AWS account ID`:*`.

###### Topics

- [Example: WorkSpaces Applications service role cross-service confused deputy prevention](example-confused-deputy.md "example-confused-deputy.md")
- [Example: WorkSpaces Applications fleet machine role cross-service confused deputy prevention](example-fleet-machine.md "example-fleet-machine.md")
- [Example: WorkSpaces Applications Elastic fleets session script Amazon S3 bucket policy cross-service confused deputy prevention](example-elastic-fleets.md "example-elastic-fleets.md")
- [Example: WorkSpaces Applications Application Amazon S3 bucket policy cross-service confused deputy prevention](example-s3-bucket.md "example-s3-bucket.md")

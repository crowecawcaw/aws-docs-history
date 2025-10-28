# Confused deputy prevention

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the
action. In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the calling service) calls
another service (the called service). The calling service can be manipulated to use its
permissions to act on another customer's resources in a way it should not otherwise have
permission to access. To prevent this, AWS provides tools that help you protect your
data for all services with service principals that have been given access to resources
in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn"), [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount"), [`aws:SourceOrgID`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgid"), and [`aws:SourceOrgPaths`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgpaths "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceorgpaths") global condition context keys in
resource policies to limit the permissions that gives another service to the resource.
Use `aws:SourceArn` to associate only one resource with cross-service access.
Use `aws:SourceAccount` to let any resource in that account be associated
with the cross-service use. Use `aws:SourceOrgID` to allow any resource from
any account within an organization be associated with the cross-service use. Use
`aws:SourceOrgPaths` to associate any resource from accounts within an
AWS Organizations path with the cross-service use. For more information about using and
understanding paths, see [Understand the AWS Organizations entity path](../../../IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.md#access_policies_last-accessed-viewing-orgs-entity-path "../../../IAM/latest/UserGuide/access_policies_last-accessed-view-data-orgs.md#access_policies_last-accessed-viewing-orgs-entity-path").

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full ARN of the
resource. If you don't know the full ARN of the resource or if you are specifying
multiple resources, use the `aws:SourceArn` global context condition key with
wildcard characters (`*`) for the unknown portions of the ARN. For example,
`arn:aws:`servicename`:*:`123456789012`:*`.

If the `aws:SourceArn` value does not contain the account ID, such as an
Amazon S3 bucket ARN, you must use both `aws:SourceAccount` and
`aws:SourceArn` to limit permissions.

To protect against the confused deputy problem at scale, use the
`aws:SourceOrgID` or `aws:SourceOrgPaths` global condition
context key with the organization ID or organization path of the resource in your
resource-based policies. Policies that include the `aws:SourceOrgID` or
`aws:SourceOrgPaths` key will automatically include the correct accounts
and you don't have to manually update the policies when you add, remove, or move
accounts in your organization.

The policies documented for granting access to CloudWatch Logs to write data to Kinesis Data Streams and Firehose
in [Step 1: Create a destination](CreateDestination.md "CreateDestination.md") and [Step 2: Create a
destination](CreateFirehoseStreamDestination.md "CreateFirehoseStreamDestination.md") show how you can use the
`aws:SourceArn` global condition context key to help prevent the confused deputy problem.

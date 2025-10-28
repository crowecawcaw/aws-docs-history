# Cross-service confused deputy

prevention

In AWS, cross-service impersonation can occur when one service (the _calling
service_) calls another service (the _called service_).
The calling service can be manipulated to act on another customer's resources even though it
shouldn't have the proper permissions, resulting in the confused deputy problem.

To prevent this, AWS provides tools that help you protect your data for all services
with service principals that have been given access to resources in your account.

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in resource
policies to limit the permissions that Amazon Rekognition gives another service to the
resource.

If the value of `aws:SourceArn` does not contain the account ID, such as an
Amazon S3 bucket ARN, you must use both keys to limit permissions. If you use both keys and the
`aws:SourceArn` value contains the account ID, the
`aws:SourceAccount` value and the account in the `aws:SourceArn`
value must use the same account ID when used in the same policy statement.

Use `aws:SourceArn` if you want only one resource to be associated with the
cross-service access. Use `aws:SourceAccount` if you want to allow any resource
in that account to be associated with the cross-service use.

The value of `aws:SourceArn` must be the ARN of the resource used by Rekognition, which is specified
with the following format: `arn:aws:rekognition:region:account:resource`.

The value of `arn:User ARN` should be the ARN of the user that will call the
video analysis operation (the user that assumes a role).

The recommended approach to the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the full resource ARN.

If you don't know the full ARN of the resource or if you are specifying multiple
resources, use the `aws:SourceArn` key with wildcard characters (`*`)
for the unknown portions of the ARN. For example,
`arn:aws:`rekognition`:*:111122223333:*`.

In order to protect against the confused deputy problem, carry out the following
steps:

1. In the navigation pane of the IAM console choose the **Roles** option. The console will display the roles for your current
   account.
2. Choose the name of the role that you want to modify. The role you modify should
   have the **AmazonRekognitionServiceRole** permissions
   policy. Select the **Trust relationships** tab.
3. Choose **Edit trust policy**.
4. On the **Edit trust policy** page, replace the
   default JSON policy with a policy that utilizes one or both of the
   `aws:SourceArn` and `aws:SourceAccount` global condition
   context keys. See the following example policies.
5. Choose **Update policy**.
   The following examples are trust policies that show how you can use the
   `aws:SourceArn` and `aws:SourceAccount` global condition context
   keys in Amazon Rekognition to prevent the confused deputy problem.

If you are working stored and streaming videos, you could use a policy like the following
in your IAM role:

If you are working exclusively with stored video, you could use a policy like the
following in your IAM role (note that you don't have to include the `StringLike`
argument that specifies the `streamprocessor`):

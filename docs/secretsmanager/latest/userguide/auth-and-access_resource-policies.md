# Resource-based policies

In a resource-based policy, you specify who can access the secret and the actions they can
perform on the secret. You can use resource-based policies to:

- Grant access to a single secret to multiple users and roles.
- Grant access to users or roles in other AWS accounts.
  When you attach a resource-based policy to a secret in the console, Secrets Manager uses the
  automated reasoning engine [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/ "https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/") and the API `ValidateResourcePolicy` to prevent you from
  granting a wide range of IAM principals access to your secrets. Alternatively, you can
  call the `PutResourcePolicy` API with the `BlockPublicPolicy`
  parameter from the CLI or SDK.

###### Important

Resource policy validation and the `BlockPublicPolicy` parameter help protect your resources by preventing public access from being granted through the resource policies that are directly attached to your secrets. In addition to using these features, carefully inspect the following policies to confirm that they do not grant public access:

- Identity-based policies attached to associated AWS principals (for example, IAM roles)
- Resource-based policies attached to associated AWS resources (for example, AWS Key Management Service (AWS KMS) keys)
  To review permissions to your secrets, see [Determine who has permissions to
  your secrets](determine-acccess_examine-iam-policies.md "determine-acccess_examine-iam-policies.md").

###### To view, change, or delete the resource policy for a secret (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. From the list of secrets, choose your secret.
3. On the secret details page, on the **Overview** tab, in the **Resource
   permissions** section, choose **Edit
   permissions**.
4. In the code field, do one of the following, and then choose
   **Save**:
   - To attach or modify a resource policy, enter the policy.
   - To delete the policy, clear the code field.

## AWS CLI

###### Example Retrieve a resource policy

The following [`get-resource-policy`](../../../cli/latest/reference/secretsmanager/get-resource-policy.md "../../../cli/latest/reference/secretsmanager/get-resource-policy.md") example retrieves the resource-based policy attached to a secret.

```
aws secretsmanager get-resource-policy \
    --secret-id MyTestSecret
```

###### Example Delete a resource policy

The following [`delete-resource-policy`](../../../cli/latest/reference/secretsmanager/delete-resource-policy.md "../../../cli/latest/reference/secretsmanager/delete-resource-policy.md") example deletes the resource-based policy attached to a secret.

```
aws secretsmanager delete-resource-policy \
    --secret-id MyTestSecret
```

###### Example Add a resource policy

The following [`put-resource-policy`](../../../cli/latest/reference/secretsmanager/put-resource-policy.md "../../../cli/latest/reference/secretsmanager/put-resource-policy.md") example adds a permissions policy to a secret, checking first that the policy does not provide broad access to the secret. The policy is read from a file. For more information, see [Loading AWS CLI parameters from a file](../../../cli/latest/userguide/cli-usage-parameters-file.md "../../../cli/latest/userguide/cli-usage-parameters-file.md") in the AWS CLI User Guide.

```
aws secretsmanager put-resource-policy \
    --secret-id MyTestSecret \
    --resource-policy file://mypolicy.json \
    --block-public-policy
```

Contents of `mypolicy.json`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::123456789012:role/MyRole"
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*"
 }
 ]
}`

```

## AWS SDK

To retrieve the policy attached to a secret, use [`GetResourcePolicy`](../apireference/API_GetResourcePolicy.md "../apireference/API_GetResourcePolicy.md").

To delete a policy attached to a secret, use [`DeleteResourcePolicy`](../apireference/API_DeleteResourcePolicy.md "../apireference/API_DeleteResourcePolicy.md").

To attach a policy to a secret, use [`PutResourcePolicy`](../apireference/API_PutResourcePolicy.md "../apireference/API_PutResourcePolicy.md"). If there is already a policy attached,
the command replaces it with the new policy. The policy must be
formatted as JSON structured text. See [JSON policy
document structure](../../../IAM/latest/UserGuide/access_policies.md#policies-introduction "../../../IAM/latest/UserGuide/access_policies.md#policies-introduction").

For more information, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").

## Examples

###### Examples:

- [Example: Permission to retrieve individual secret
  values](#auth-and-access_examples_read "#auth-and-access_examples_read")
- [Example: Permissions and VPCs](#auth-and-access_examples_vpc "#auth-and-access_examples_vpc")
- [Example: Service principal](#auth-and-access_service "#auth-and-access_service")

### Example: Permission to retrieve individual secret

values

To grant permission to retrieve secret values, you can attach policies to secrets or
identities. For help determining which type of policy to use, see [Identity-based
policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md"). For information about how to attach a
policy, see [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md") and [Identity-based policies](auth-and-access_iam-policies.md "auth-and-access_iam-policies.md").

This example is
useful when you want to grant access to a single secret to multiple users or roles. To grant permission to retrieve a group of secrets in a batch API call, see [Example: Permission to retrieve a group of secret values in a batch](auth-and-access_iam-policies.md#auth-and-access_examples_batch "auth-and-access_iam-policies.md#auth-and-access_examples_batch").

###### Example Read one secret

You can grant access to a secret by attaching the following policy to the secret.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`EC2RoleToAccessSecrets`"
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*"
 }
 ]
}`

```

### Example: Permissions and VPCs

If you need to access Secrets Manager from within a VPC, you can make sure that requests to
Secrets Manager come from the VPC by including a condition in your permissions policies. For more
information, see [Limit requests with VPC endpoint conditions](best-practices.md#iam-contextkeys-vpcendpoint "best-practices.md#iam-contextkeys-vpcendpoint") and [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md "vpc-endpoint-overview.md").

Make sure that requests to access the secret from other AWS services also come from
the VPC, otherwise this policy will deny them access.

###### Example Require requests to come through a VPC endpoint

The following policy allows a user to perform Secrets Manager operations only when the
request comes through the VPC endpoint
`vpce-1234a5678b9012c`.

JSON

```
`{
"Id": "example-policy-1",
"Version":"2012-10-17",
"Statement": [
{
 "Sid": "`RestrictGetSecretValueoperation`",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpce": "`vpce-12345678"`
 }
 }
}
]
}`

```

###### Example Require requests to come from a VPC

The following policy allows commands to create and manage secrets only when they
come from `vpc-12345678`. In addition, the
policy allows operations that use access the secret encrypted value only when the
requests come from `vpc-2b2b2b2b`. You might use a policy like this one
if you run an application in one VPC, but you use a second, isolated VPC for
management functions.

JSON

```
`{
"Id": "example-policy-2",
"Version":"2012-10-17",
"Statement": [
{
 "Sid": "`AllowAdministrativeActionsfromONLYvpc-12345678`",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "secretsmanager:Create*",
 "secretsmanager:Put*",
 "secretsmanager:Update*",
 "secretsmanager:Delete*",
 "secretsmanager:Restore*",
 "secretsmanager:RotateSecret",
 "secretsmanager:CancelRotate*",
 "secretsmanager:TagResource",
 "secretsmanager:UntagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpc": "`vpc-12345678`"
 }
 }
},
{
 "Sid": "`AllowSecretValueAccessfromONLYvpc-2b2b2b2b`",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpc": "`vpc-2b2b2b2b`"
 }
 }
}
]
}`

```

### Example: Service principal

If the resource policy attached to your secret includes an [AWS service principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services"), we recommend that you use the [aws:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [aws:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition keys. The ARN and account values are
included in the authorization context only when a request comes to Secrets Manager from another
AWS service. This combination of conditions avoids a potential [confused deputy
scenario](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

If a resource ARN includes characters that are not permitted in a resource policy, you
cannot use that resource ARN in the value of the `aws:SourceArn` condition
key. Instead, use the `aws:SourceAccount` condition key. For more
information, see [IAM requirements](../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names "../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names").

Service principals are not typically used as principals in a policy attached to a
secret, but some AWS services require it. For information about resource policies that
a service requires you to attach to a secret, see the service's documentation.

###### Example Allow a service to access a secret using a service principal

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
{
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "`s3`.amazonaws.com"
 ]
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*",
 "Condition": {
 "ArnLike": {
 "aws:sourceArn": "arn:aws:`s3`::`123456789012`:*"
 },
 "StringEquals": {
 "aws:sourceAccount": "`123456789012`"
 }
 }

}
]
}`

```

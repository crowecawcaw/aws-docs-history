# Working with resource-based policies in Lambda

With resource-based permissions policies, you can grant other AWS accounts, users, organizations, and AWS services access to your Lambda functions.
A resource-based policy is a JSON document that contains one or more _statements_. Each statement defines the following:

- `Principal`: The entity you want to grant permissions to (another AWS service, an IAM role or user, or another AWS account)
- `Action`: A list of the API actions you want to allow or deny for the specified principal
- `Effect`: Whether you want to allow or deny the principal the ability to use the chosen API actions
- `Resource`: The Lambda function, version, or alias you want the statement to apply to (you can also use a
  wildcard character to specify all of your function's versions and aliases)
  You can also use optional elements such as `Sid` (a statement identifier) and `Condition` (logical conditions for fine-grained access control).
  For a full list of supported policy elements, refer to
  [IAM JSON policy element reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
  _AWS Identity and Access Management User Guide_.

## Adding resource-based permissions to a Lambda function

You can add resource-based permissions to your Lambda function using two methods:

- **Full JSON policy** – Use the Lambda console, AWS CLI, or the
  [PutResourcePolicy](../api/API_PutResourcePolicy.md "../api/API_PutResourcePolicy.md") API action to add a complete
  JSON policy document. With a full JSON policy, you can use the complete range of
  [IAM global condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md"),
  add multiple statements with multiple principals, and create explicit `Deny` statements. The maximum size for a JSON
  resource-based policy is 20 KB.
- **Individual permissions** – Use the console or
  [AddPermission](../api/API_AddPermission.md "../api/API_AddPermission.md") API action to add single
  `Allow` statements. Individual permissions support only a limited set of condition keys
  (`aws:SourceArn`, `aws:SourceAccount`, and `aws:PrincipalOrgID`).

We recommend that you define complete JSON policies to add resource-based permissions to your function. Creating a complete JSON policy gives you more flexibility and fine-grained control
over your permissions.

###### Important

Using `put-resource-policy` replaces any existing resource-based policy on the resource. If the resource
already has permissions defined with `add-permission`, `put-resource-policy` overwrites them.
Use `get-resource-policy` to retrieve the existing policy before making changes.

### Required permissions

To use the `PutResourcePolicy`, `GetResourcePolicy`, and `DeleteResourcePolicy` API actions,
you need the following IAM permissions:

| API action           | Required permissions                                                              |
| -------------------- | --------------------------------------------------------------------------------- |
| PutResourcePolicy    | `lambda:PutResourcePolicy`, `lambda:AddPermission`, and `lambda:RemovePermission` |
| GetResourcePolicy    | `lambda:GetResourcePolicy` and `lambda:GetPolicy`                                 |
| DeleteResourcePolicy | `lambda:DeleteResourcePolicy` and `lambda:RemovePermission`                       |

Console

###### To create a full JSON resource-based policy

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function you want to grant access to and then select the **Configuration** tab.
3. Select **Permissions**.
4. In the **Resource-based policy statements** pane, choose **Edit**. This action opens the JSON policy editor.
5. Add statements to your function's policy. You can select API actions, add principals of different types (services, accounts, IAM roles),
   and add condition keys to control access.
6. Choose **Save**.

You can also edit your function's resource-based policy directly in the **Policy** pane.

AWS CLI

###### To add a full JSON resource-based policy

To add a full JSON policy to your function, use the `put-resource-policy` AWS CLI command.

The following example command adds a resource-based policy to your function using a policy defined in a file named `policy.json`
on your local machine. Run the command from the directory that contains the file. The `resource-arn` can specify a function version or alias,
or you can use the unqualified function ARN to apply the policy to the entire function.

```
`aws lambda put-resource-policy --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function` \
--policy file://policy.json`
```

Lambda APIs
To add a full JSON permissions policy to your function, use the [PutResourcePolicy](../api/API_PutResourcePolicy.md "../api/API_PutResourcePolicy.md")
API action. You can also delete a function's policy using the [DeleteResourcePolicy](../api/API_DeleteResourcePolicy.md "../api/API_DeleteResourcePolicy.md") action, or
retrieve the policy currently attached to a function using the [GetResourcePolicy](../api/API_GetResourcePolicy.md "../api/API_GetResourcePolicy.md") action.

To add individual permissions to a function's policy, use the [AddPermission](../api/API_AddPermission.md "../api/API_AddPermission.md") API action.

## Viewing a function's resource-based policy

Console

###### To view a function's resource-based policy

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose a function.
3. Choose **Configuration** and then choose **Permissions**.
4. Scroll down to **Resource-based policy statements** to see the policy.

AWS CLI
To view a function's resource-based policy, use the `get-resource-policy` command. You can use your function's
unqualified ARN, or specify a version or alias.

```
`aws lambda get-resource-policy --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function``
```

You can also use the `get-policy` command:

```
`aws lambda get-policy \
 --function-name my-function \
 --output text`
```

Lambda APIs
To retrieve a function's resource-based policy, use the
[GetResourcePolicy](../api/API_GetResourcePolicy.md "../api/API_GetResourcePolicy.md") API action.
You can use your function's unqualified ARN, or specify a version or alias ARN.

You can also use the [GetPolicy](../api/API_GetPolicy.md "../api/API_GetPolicy.md") API action.

## Deleting a function's resource-based policy

Console

###### To delete a function's resource-based policy

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Select the function you want to delete the permissions policy for.
3. Select the **Configuration** tab, then **Permissions**.
4. In the **Resource-based policy statements** pane, choose **Delete**.

AWS CLI
To delete your function's policy, use the `delete-resource-policy` command and specify the ARN of the
function, version, or alias you want to delete the policy from.

```
`aws lambda delete-resource-policy --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function``
```

To remove individual statements, use `remove-permission`.

```
`aws lambda remove-permission \
 --function-name example \
 --statement-id sns`
```

Lambda APIs
To delete the resource-based policy attached to a function, function version, or function alias, use the
[DeleteResourcePolicy](../api/API_DeleteResourcePolicy.md "../api/API_DeleteResourcePolicy.md") API action.

To remove individual statements from a policy, use the
[RemovePermission](../api/API_RemovePermission.md "../api/API_RemovePermission.md") API action.

## Updating existing policies

When you update a function's existing resource-based permissions, the behavior depends on the method you use:

- `put-resource-policy` / [PutResourcePolicy](../api/API_PutResourcePolicy.md "../api/API_PutResourcePolicy.md") –
  Replaces the entire existing policy. Any previously added individual permissions are overwritten.
- `add-permission` / [AddPermission](../api/API_AddPermission.md "../api/API_AddPermission.md") –
  Adds a statement to the existing policy without overwriting. If you call `add-permission` after
  `put-resource-policy`, the new statement appends to the existing JSON policy.

To avoid unintentionally overwriting existing permissions when using `put-resource-policy`, retrieve your function's existing policy first.
The `get-resource-policy` output includes a `RevisionId` field.

```
`aws lambda get-resource-policy --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function``
```

When you attach a new policy, provide the `RevisionId` value with the `--revision-id` parameter to ensure that you are updating the latest version.
If you provide an older revision ID, Lambda does not update your function's policy.

```
`aws lambda put-resource-policy \
 --resource-arn arn:aws:lambda:`us-east-2`:`123456789012`:function:`my-function` \
 --policy file://policy.json \
 --revision-id `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``
```

###### Note

Existing resource-based policies created with `AddPermission` continue to work without modification.
No changes to your function code are required to use the new `PutResourcePolicy` API.

## Security best practices

With JSON resource-based policies, you can follow least-privilege access patterns. You can also meet regulatory
requirements for explicit denials. With full JSON policies, you can:

- Create explicit `Deny` statements to block specific principals or conditions.
- Use organizational conditions (`aws:PrincipalOrgID`, `aws:PrincipalOrgPaths`) to restrict
  access to your Organizations without enumerating individual accounts.
- Scope permissions to specific source accounts or ARNs using the full range of IAM global condition keys.

## Example resource-based policies

###### Example Granting permission to Amazon S3 with a deny statement

The following policy grants all Amazon S3 buckets in an account permission to invoke a function, except for one bucket that is explicitly denied.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-s3",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                }
            }
        },
        {
            "Sid": "deny-s3-bucket",
            "Effect": "Deny",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": [
                "arn:aws:lambda:us-east-2:111122223333:function:my-function",
                "arn:aws:lambda:us-east-2:111122223333:function:my-function:*"
            ],
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:s3:::amzn-s3-demo-bucket"
                }
            }
        }
    ]
}
```

###### Example Granting permission to accounts in an organization

The following policy grants invoke access to all AWS accounts in an organization.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "org-access",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Principal": "*",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-a1b2c3d4e5f"
                }
            }
        }
    ]
}
```

###### Example Granting permission to multiple IAM roles with conditions

The following policy grants permission to two IAM roles to use the CreateAlias action from a specified IP address.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "allow-roles",
            "Effect": "Allow",
            "Action": "lambda:CreateAlias",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::444455556666:role/role-name",
                    "arn:aws:iam::444455556666:role/role-name2"
                ]
            },
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "192.0.2.0"
                }
            }
        }
    ]
}
```

###### Example Denying access unless the caller is part of a specified organization

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "deny-access",
            "Effect": "Deny",
            "Action": "lambda:InvokeFunction",
            "Principal": "*",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "ForAllValues:StringNotLike": {
                    "aws:PrincipalOrgPaths": [
                        "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/*"
                    ]
                }
            }
        },
        {
            "Sid": "allow-access",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Principal": "*",
            "Resource": "arn:aws:lambda:us-east-2:111122223333:function:my-function",
            "Condition": {
                "ForAnyValue:StringLike": {
                    "aws:PrincipalOrgPaths": [
                        "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/*"
                    ]
                }
            }
        }
    ]
}
```

## Supported API actions

The following Lambda API actions support resource-based policies:

- [CreateAlias](../api/API_CreateAlias.md "../api/API_CreateAlias.md")
- [DeleteAlias](../api/API_DeleteAlias.md "../api/API_DeleteAlias.md")
- [DeleteFunction](../api/API_DeleteFunction.md "../api/API_DeleteFunction.md")
- [DeleteFunctionConcurrency](../api/API_DeleteFunctionConcurrency.md "../api/API_DeleteFunctionConcurrency.md")
- [DeleteFunctionEventInvokeConfig](../api/API_DeleteFunctionEventInvokeConfig.md "../api/API_DeleteFunctionEventInvokeConfig.md")
- [DeleteProvisionedConcurrencyConfig](../api/API_DeleteProvisionedConcurrencyConfig.md "../api/API_DeleteProvisionedConcurrencyConfig.md")
- [GetAlias](../api/API_GetAlias.md "../api/API_GetAlias.md")
- [GetFunction](../api/API_GetFunction.md "../api/API_GetFunction.md")
- [GetFunctionConcurrency](../api/API_GetFunctionConcurrency.md "../api/API_GetFunctionConcurrency.md")
- [GetFunctionConfiguration](../api/API_GetFunctionConfiguration.md "../api/API_GetFunctionConfiguration.md")
- [GetFunctionEventInvokeConfig](../api/API_GetFunctionEventInvokeConfig.md "../api/API_GetFunctionEventInvokeConfig.md")
- [GetPolicy](../api/API_GetPolicy.md "../api/API_GetPolicy.md")
- [GetProvisionedConcurrencyConfig](../api/API_GetProvisionedConcurrencyConfig.md "../api/API_GetProvisionedConcurrencyConfig.md")
- [Invoke](../api/API_Invoke.md "../api/API_Invoke.md")
- [InvokeFunctionUrl](urls-auth.md "urls-auth.md") (permission only)
- [ListAliases](../api/API_ListAliases.md "../api/API_ListAliases.md")
- [ListFunctionEventInvokeConfigs](../api/API_ListFunctionEventInvokeConfigs.md "../api/API_ListFunctionEventInvokeConfigs.md")
- [ListProvisionedConcurrencyConfigs](../api/API_ListProvisionedConcurrencyConfigs.md "../api/API_ListProvisionedConcurrencyConfigs.md")
- [ListTags](../api/API_ListTags.md "../api/API_ListTags.md")
- [ListVersionsByFunction](../api/API_ListVersionsByFunction.md "../api/API_ListVersionsByFunction.md")
- [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md")
- [PutFunctionConcurrency](../api/API_PutFunctionConcurrency.md "../api/API_PutFunctionConcurrency.md")
- [PutFunctionEventInvokeConfig](../api/API_PutFunctionEventInvokeConfig.md "../api/API_PutFunctionEventInvokeConfig.md")
- [PutProvisionedConcurrencyConfig](../api/API_PutProvisionedConcurrencyConfig.md "../api/API_PutProvisionedConcurrencyConfig.md")
- [TagResource](../api/API_TagResource.md "../api/API_TagResource.md")
- [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md")
- [UpdateAlias](../api/API_UpdateAlias.md "../api/API_UpdateAlias.md")
- [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md")
- [UpdateFunctionEventInvokeConfig](../api/API_UpdateFunctionEventInvokeConfig.md "../api/API_UpdateFunctionEventInvokeConfig.md")

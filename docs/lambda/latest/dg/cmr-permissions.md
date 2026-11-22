

# Sharing and controlling access to customer-managed runtimes

This topic describes how Lambda controls who can use a customer-managed runtime.

To share a runtime and let other accounts use the runtime, publishers and consumers each configure permissions:
+ **Sharing a runtime** – As a runtime publisher, you attach a resource-based policy to your runtime to control which accounts can use the runtime. For more information, including how to revoke access to a runtime, see [Sharing a customer-managed runtime](#cmr-permissions-sharing).
+ **Granting consumers permission** – As an administrator in a consumer account, you use an identity-based policy to let roles configure functions to use a shared runtime. For more information, see [Grant consumers permission to use a shared runtime](#cmr-permissions-consumer-policy).

To govern customer-managed runtimes across your organization, security and organization administrators can do the following:
+ **Controlling which runtimes principals in your organization can use** – As a security or organization administrator, you use service control policies (SCPs) to block runtimes that you don't trust. For more information, see [Blocking untrusted runtimes in your organization](#cmr-permissions-restrict).
+ **Controlling what principals can create and share outside your organization** – As a security or organization administrator, you use SCPs to limit which principals can create runtimes or share runtimes. Sharing a runtime outside your organization is a potential path for data to leave your organization. For more information, see [Control who can create and share runtimes](#cmr-permissions-related-controls).

For a list of IAM actions, Amazon Resource Name (ARN) formats, and condition keys for customer-managed runtimes, see [Permissions reference for customer-managed runtimes](#cmr-permissions-reference).

## How access to customer-managed runtimes works
<a name="cmr-permissions-how"></a>

To configure a Lambda Event Function to use a customer-managed runtime, the caller needs permission for one of the following IAM actions:
+ `lambda:AssociateRuntimeAlias` – Lets the caller configure a function to use a runtime alias. The resource is the alias ARN.
+ `lambda:AssociateRuntimeVersion` – Lets the caller pin a function to a runtime version by using the [Manual runtime update mode](cmr-using.md#cmr-using-pin). The resource is the runtime version ARN.

These actions don't correspond to API operations. Instead, Lambda checks them when a principal makes one of the following requests:
+ `CreateFunction` or `UpdateFunctionConfiguration`, with a runtime alias in the function's runtime configuration
+ `PutRuntimeManagementConfig`, to pin a function to a runtime version

Permission for `lambda:AssociateRuntimeAlias` implicitly grants access to the runtime version that the alias points to. To configure a function to use the alias, a principal doesn't need `lambda:AssociateRuntimeVersion` for any runtime version. The only exception is an explicit deny: if a policy denies `lambda:AssociateRuntimeVersion` on the version that the alias points to at the time of the request, the request fails.

Lambda doesn't check these permissions again when it invokes the function. It also doesn't check them when the publisher points an alias to a new runtime version. As a result, policy changes affect only new functions and changes to a function's runtime configuration. They don't affect functions that already use the runtime. For more information, see [Revoke access to a runtime](#cmr-permissions-revoke).

How Lambda checks these actions depends on whether the function and the runtime are in the same account:
+ **Same account** – If the function and the runtime are in the same account, either an identity-based policy or a resource-based policy must allow the actions. You don't need both.
+ **Cross-account** – If the function and the runtime are in different accounts, both policies must allow the actions. The consumer's identity-based policy must allow them. The runtime's resource-based policy must also allow them for the consumer's account.

Service control policies (SCPs) and permissions boundaries can also deny these actions, even if other policies allow them. For more information about how IAM evaluates cross-account requests, see [Cross-account policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html) in the *IAM User Guide*.

Runtime consumers don't need access to the Amazon Elastic Container Registry (Amazon ECR) images that the publisher builds runtime versions from. For more information, see [Runtime versions](cmr-versions.md).

## Sharing a customer-managed runtime
<a name="cmr-permissions-sharing"></a>

To share a runtime with other accounts, attach a resource-based policy to the runtime itself, not to each alias or version. In each statement, the `Resource` element sets which aliases and versions a principal can use.

You can share a runtime in the following ways:
+ With specific AWS accounts
+ With all accounts in an organization in AWS Organizations
+ With all accounts in an organizational unit (OU)
+ Publicly, with all AWS accounts

In each statement, grant the `lambda:AssociateRuntimeAlias` action for the aliases that you want consumers to use. To let consumers pin functions to specific versions, also grant `lambda:AssociateRuntimeVersion` for those versions.

You can also grant read actions so that consumers can view details about the runtime by using the AWS CLI or the Lambda API. These actions include `lambda:GetRuntime`, `lambda:GetRuntimeAlias`, `lambda:ListRuntimeAliases`, `lambda:GetRuntimeVersion`, and `lambda:ListRuntimeVersions`. Consumers don't need these read actions to configure a function if they know the runtime ARN and alias name. However, we recommend that you grant the read actions so that consumers can do the following:
+ List the runtime aliases and read each alias description to choose an alias for a function.
+ View the release lifecycle of each runtime alias to plan for deprecation. If an alias doesn't have its own lifecycle, the alias shows the lifecycle that the publisher sets on the runtime. For more information, see [How runtime consumers see the lifecycle](cmr-lifecycle.md#cmr-lifecycle-consumers).
+ Read the runtime description and license information.
+ List the runtime versions and read the release notes for each version.

The `GetRuntimeVersion` response includes the `ResolvedUri` field, which contains the Amazon ECR image URI for the runtime version. Consumers that you grant `lambda:GetRuntimeVersion` can see the image URI, which includes your account ID and repository name. The image URI alone doesn't give consumers access to the image.

A runtime's resource-based policy applies only in the runtime's AWS Region. To share a runtime in more than one Region, attach a policy to the runtime in each Region. For more information, see [Deploying runtimes in multiple Regions](cmr-multi-region.md).

The examples in this section use the following values:
+ Runtime publisher account: `123456789012`
+ Runtime: `companyphp8` in the `us-east-1` Region, with the aliases `dev`, `test`, and `prod`
+ Consumer accounts: `111122223333` and `444455556666`
+ Organization: `o-a1b2c3d4e5`

### Share a runtime with specific accounts
<a name="cmr-permissions-share-accounts"></a>

To share a runtime with specific accounts, list the accounts in the `Principal` element. The following policy lets accounts `111122223333` and `444455556666` use all aliases and versions of the `companyphp8` runtime. The second statement lets these accounts view details about the runtime and its aliases and versions.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAccountsToUseRuntime",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::111122223333:root",
                    "arn:aws:iam::444455556666:root"
                ]
            },
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/*",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/*"
            ]
        },
        {
            "Sid": "AllowAccountsToViewRuntimeDetails",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::111122223333:root",
                    "arn:aws:iam::444455556666:root"
                ]
            },
            "Action": [
                "lambda:GetRuntime",
                "lambda:ListRuntimeAliases",
                "lambda:ListRuntimeVersions",
                "lambda:GetRuntimeAlias",
                "lambda:GetRuntimeVersion"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/*",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/*"
            ]
        }
    ]
}
```

When you share with an account root principal, an administrator in that account decides which users and roles in the account can use the runtime. The administrator grants access with identity-based policies. For more information, see [Grant consumers permission to use a shared runtime](#cmr-permissions-consumer-policy).

### Share a runtime with an organization
<a name="cmr-permissions-share-org"></a>

To share a runtime with all accounts in an organization, set `Principal` to `*` and add the `aws:PrincipalOrgID` condition key. The following policy lets all accounts in organization `o-a1b2c3d4e5` use all aliases and versions of the runtime.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOrganizationToUseRuntime",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/*",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-a1b2c3d4e5"
                }
            }
        }
    ]
}
```

Accounts that join the organization later get access automatically. Accounts that leave the organization can no longer configure functions to use the runtime. Functions that they already configured keep working. For more information, see [aws:PrincipalOrgID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid) in the *IAM User Guide*.

### Share a runtime with an organizational unit
<a name="cmr-permissions-share-ou"></a>

To share a runtime with the accounts in an OU, use the `aws:PrincipalOrgPaths` condition key. The following policy lets accounts in OU `ou-ab12-11111111` and its child OUs use all aliases and versions of the runtime.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOrganizationalUnitToUseRuntime",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/*",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/*"
            ],
            "Condition": {
                "ForAnyValue:StringLike": {
                    "aws:PrincipalOrgPaths": "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/*"
                }
            }
        }
    ]
}
```

The OU path includes the organization ID, the root ID, and each OU ID in the path. The wildcard at the end of the path matches the OU and all of its child OUs. For more information, see [aws:PrincipalOrgPaths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgpaths) in the *IAM User Guide*.

### Share a runtime publicly
<a name="cmr-permissions-share-public"></a>

To share a runtime with all AWS accounts, set `Principal` to `*` and don't add a condition. Third-party runtime publishers can use this approach to publish runtimes for any Lambda customer. The following policy lets any account use the `prod` alias of the runtime.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicUseOfProdAlias",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "lambda:AssociateRuntimeAlias",
            "Resource": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod"
        }
    ]
}
```

**Important**  
Before you share a runtime publicly, consider the following:  
Any AWS account can configure functions to use the runtime. You don't know in advance who your consumers are.
Every runtime update that you roll out reaches all consumer functions. The runtime code runs with the permissions of each consumer function's execution role. You're responsible for keeping the runtime secure and backward compatible.
Your runtime's metrics include activity from functions in consumer accounts.
If you remove public access later, functions that already use the runtime keep using it. To stop those functions from using the runtime, you must delete the alias or version that they use. This breaks those functions. For more information, see [Revoke access to a runtime](#cmr-permissions-revoke).

### Share only specific aliases or versions
<a name="cmr-permissions-share-aliases"></a>

You don't have to share all aliases of a runtime. For example, you might use the `dev` and `test` aliases for internal testing and share only the `prod` alias. To do this, list only the aliases that you want to share in the `Resource` element.

You can also limit which versions consumers can pin functions to. To do this, list the version ARNs for the `lambda:AssociateRuntimeVersion` action. The following policy lets accounts `111122223333` and `444455556666` use only the `prod` alias. It also lets them pin functions to versions `v8.3.0` and `v8.3.1`.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowProdAliasOnly",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::111122223333:root",
                    "arn:aws:iam::444455556666:root"
                ]
            },
            "Action": "lambda:AssociateRuntimeAlias",
            "Resource": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod"
        },
        {
            "Sid": "AllowPinningToReleasedVersions",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::111122223333:root",
                    "arn:aws:iam::444455556666:root"
                ]
            },
            "Action": "lambda:AssociateRuntimeVersion",
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.0",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/v8.3.1"
            ]
        }
    ]
}
```

With this policy, consumers can't use the `dev` or `test` aliases. They also can't pin functions to other versions, such as versions that you're still testing. When you release a new version, you can add its ARN to the policy.

### Combine sharing rules
<a name="cmr-permissions-share-combined"></a>

A policy can have several statements. Each statement can grant different access to different principals. The following policy grants two levels of access:
+ All accounts in organization `o-a1b2c3d4e5` can use all aliases and versions.
+ Partner account `444455556666`, which is outside the organization, can use only the `prod` alias.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOrganizationAllAliasesAndVersions",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": [
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/*",
                "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-a1b2c3d4e5"
                }
            }
        },
        {
            "Sid": "AllowPartnerProdAliasOnly",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::444455556666:root"
            },
            "Action": "lambda:AssociateRuntimeAlias",
            "Resource": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod"
        }
    ]
}
```

### Attach, view, and remove a runtime's resource-based policy
<a name="cmr-permissions-manage-policy"></a>

You can manage a runtime's resource-based policy by using the Lambda console or the AWS CLI. You need permission for the `lambda:PutResourcePolicy`, `lambda:GetResourcePolicy`, and `lambda:DeleteResourcePolicy` actions on the runtime.

When you attach a policy, the new policy replaces the runtime's existing policy. To add or change a statement, view the existing policy first. Then edit the policy and attach the complete policy, so that you don't remove access that consumers rely on. To avoid overwriting changes made after you viewed the policy, pass the revision ID from `get-resource-policy` in the `--revision-id` option. If the policy has changed, the command fails.

**To view or edit a runtime's resource-based policy (console)**

1. Open the [Runtimes page](https://console.aws.amazon.com/lambda/home#/runtimes) of the Lambda console.

1. Choose the name of the runtime.

1. Choose the **Sharing permissions** tab.

   The **Resource-based policy** panel shows the runtime's current policy.

1. To change the policy, choose **Edit**.

1. In the JSON editor, modify the policy.

1. Choose **Save**.

**To attach a resource-based policy to a runtime (AWS CLI)**

1. Save your policy in a file named `policy.json`. For example policies, see [Sharing a customer-managed runtime](#cmr-permissions-sharing).

1. To attach the policy, run the following command. For `--resource-arn`, specify the runtime ARN. This command replaces any existing policy on the runtime.

   ```bash
   aws lambda put-resource-policy \
     --resource-arn arn:aws:lambda:{{us-east-1}}:{{123456789012}}:runtime/{{companyphp8}} \
     --policy file://policy.json
   ```

**To view a runtime's resource-based policy (AWS CLI)**
+ Run the following command.

  ```bash
  aws lambda get-resource-policy \
    --resource-arn arn:aws:lambda:{{us-east-1}}:{{123456789012}}:runtime/{{companyphp8}}
  ```

**To remove a runtime's resource-based policy (AWS CLI)**
+ Run the following command.

  ```bash
  aws lambda delete-resource-policy \
    --resource-arn arn:aws:lambda:{{us-east-1}}:{{123456789012}}:runtime/{{companyphp8}}
  ```

After you remove the policy, only your account can configure new functions to use the runtime. This change doesn't affect functions in other accounts that already use the runtime. For more information, see [Revoke access to a runtime](#cmr-permissions-revoke).

### Use tags to control access to runtimes
<a name="cmr-permissions-tags"></a>

You can add tags to runtimes. Runtime versions and runtime aliases don't support tags. You can use tags in IAM policies to control access to runtimes. This is called attribute-based access control (ABAC). For more information about adding tags to a runtime, see [Creating a runtime](cmr-create.md). For more information about ABAC in Lambda, see [Using attribute-based access control in Lambda](attribute-based-access-control.md).

For runtime versions and aliases, `aws:ResourceTag` uses the tags on the runtime.

The following identity-based policy lets a principal use runtime aliases and runtime versions only from runtimes that have the tag `approved` with the value `true`.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "UseApprovedRuntimes",
            "Effect": "Allow",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/approved": "true"
                }
            }
        }
    ]
}
```

### Revoke access to a runtime
<a name="cmr-permissions-revoke"></a>

To revoke access to a shared runtime, remove or narrow the statements in the runtime's resource-based policy. Principals that lose access can't create or update functions to use the aliases that the policy no longer allows. They also can't pin functions to versions that the policy no longer allows.

Before you revoke access to a runtime alias or version, use the `RuntimeInvocations` metric to check how many function invocations the alias or version receives. For more information, see [Check usage before you delete or deprecate](cmr-monitoring.md#cmr-monitoring-uses-usage).

Revoking access doesn't affect functions that already use the runtime. Lambda checks the `Associate` actions only when a principal configures a function to use a runtime alias, or pins a function to a runtime version. Lambda doesn't check the `Associate` actions when it invokes a function. Those functions keep running. Functions that use an alias also keep using whichever version the alias points to, including new versions that you point the alias to later.

To stop existing functions from using the runtime, you must delete the runtime alias or runtime version that they use. For more information, see [Deleting and restoring runtimes](cmr-delete.md).

**Warning**  
If you delete a runtime alias or runtime version, the functions that use it break in every account. Existing execution environments continue to handle invocations, but invocations that require a cold start fail. This affects functions in the **Auto** runtime update mode after you delete their alias. It affects functions in **Function update** or **Manual** mode after you delete the version that they use. Before you delete a runtime alias or version, notify your consumers. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

To stop new functions from using a runtime on a planned date, you can also set lifecycle block dates on the runtime or alias. For more information, see [Runtime lifecycle](cmr-lifecycle.md).

## Grant consumers permission to use a shared runtime
<a name="cmr-permissions-consumer-policy"></a>

If the runtime is in another account, the runtime's resource-based policy isn't enough. An administrator in the consumer account must also grant access in an identity-based policy. If the runtime is in the same account, either an identity-based policy or the runtime's resource-based policy is enough. For more information, see [How access to customer-managed runtimes works](#cmr-permissions-how).

The following identity-based policy is for a role in consumer account `111122223333`. It lets the role create and update functions that use the `prod` alias of the `companyphp8` runtime in publisher account `123456789012`. It also lets the role pin functions to a runtime version and pass an execution role to Lambda.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ManageFunctions",
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration",
                "lambda:UpdateFunctionCode",
                "lambda:PutRuntimeManagementConfig",
                "lambda:GetFunction"
            ],
            "Resource": "arn:aws:lambda:us-east-1:111122223333:function:*"
        },
        {
            "Sid": "UseProdRuntimeAlias",
            "Effect": "Allow",
            "Action": "lambda:AssociateRuntimeAlias",
            "Resource": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/prod"
        },
        {
            "Sid": "PinToRuntimeVersions",
            "Effect": "Allow",
            "Action": "lambda:AssociateRuntimeVersion",
            "Resource": "arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/*"
        },
        {
            "Sid": "PassExecutionRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::111122223333:role/my-function-execution-role",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "lambda.amazonaws.com"
                }
            }
        }
    ]
}
```

In this example, the role can pin functions to any version of the runtime. However, the runtime's resource-based policy still limits which versions the role can use. For more information about how to configure a function to use a runtime, see [Using a customer-managed runtime](cmr-using.md).

The `PassExecutionRole` statement lets the role pass the function's execution role, and the `iam:PassedToService` condition limits the role to passing the execution role only to Lambda. Creating any Lambda function, or changing a function's execution role, requires `iam:PassRole`, whether or not the function uses a customer-managed runtime. For more information, see [Defining Lambda Event Function permissions with an execution role](lambda-intro-execution-role.md).

## Blocking untrusted runtimes in your organization
<a name="cmr-permissions-restrict"></a>

A runtime publisher can push any code into the functions that use the runtime. This code runs with the permissions of each function's execution role. If you're a security or organization administrator, you can control which runtimes the users and roles in your organization can use.

To do this, deny the `lambda:AssociateRuntimeAlias` and `lambda:AssociateRuntimeVersion` actions. You can apply the deny statements in two ways:
+ **Service control policies (SCPs)** – Apply the restriction to all accounts in an organization or OU. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.
+ **Identity-based policies or permissions boundaries** – Apply the restriction to specific users or roles. For more information, see [Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html) in the *IAM User Guide*.

SCPs don't grant permissions. They only limit the permissions that other policies grant. SCPs don't affect principals in the organization's management account.

Lambda checks the `Associate` actions only when a principal creates a function, changes its runtime configuration, or pins it to a runtime version. Lambda doesn't check them when a principal updates the function code or other settings. A deny statement prevents new functions from using a runtime. It doesn't affect functions that already use the runtime. Before you apply a restriction, we recommend that you audit existing functions, as described in the following section.

### Find functions that use customer-managed runtimes
<a name="cmr-permissions-audit"></a>

To find functions that use a customer-managed runtime, run the following command in each account and Region. The command lists the function ARN, runtime ARN, and runtime alias of each Event Function version, including `$LATEST` and published versions. The `list-functions` command doesn't return Lambda Web Functions, which can't use customer-managed runtimes.

```bash
aws lambda list-functions --function-version ALL \
  --region {{us-east-1}} \
  --query "Functions[?Runtime=='custom'].[FunctionArn,RuntimeConfig.RuntimeArn,RuntimeConfig.RuntimeAlias]" \
  --output table
```

For more queries, such as finding the functions that use a specific runtime or runtime alias, see [Find functions that use a customer-managed runtime](cmr-using.md#cmr-using-list-functions).

If a function uses a runtime that you don't trust, work with the function owner to move it to a trusted runtime.

### Block all customer-managed runtimes
<a name="cmr-permissions-block-all"></a>

The following SCP stops principals in the affected accounts from using any customer-managed runtime in their functions.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAllCustomerManagedRuntimes",
            "Effect": "Deny",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": "*"
        }
    ]
}
```

This policy applies only to customer-managed runtimes. It doesn't affect functions that use Lambda-managed runtimes.

### Allow only runtimes owned by your organization
<a name="cmr-permissions-allow-org"></a>

To allow only runtimes that accounts in your organization own, use the `aws:ResourceOrgID` condition key. The following SCP denies the `Associate` actions for runtimes that accounts outside organization `o-a1b2c3d4e5` own.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyRuntimesOutsideOrganization",
            "Effect": "Deny",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:ResourceOrgID": "o-a1b2c3d4e5"
                }
            }
        }
    ]
}
```

For more information, see [aws:ResourceOrgID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgid) in the *IAM User Guide*.

### Allow only runtimes from specific accounts
<a name="cmr-permissions-allow-accounts"></a>

To allow only runtimes that specific accounts own, use the `aws:ResourceAccount` condition key. For example, you might allow only runtimes that your platform team publishes. The following SCP denies the `Associate` actions unless the runtime owner is account `123456789012` or `999988887777`.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyRuntimesFromOtherAccounts",
            "Effect": "Deny",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:ResourceAccount": [
                        "123456789012",
                        "999988887777"
                    ]
                }
            }
        }
    ]
}
```

When you specify several values for `StringNotEquals`, the deny applies only if the runtime owner matches none of the values. For more information, see [aws:ResourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceaccount) in the *IAM User Guide*.

### Allow only specific runtimes
<a name="cmr-permissions-allowlist"></a>

To allow only specific runtimes, use the `NotResource` element in a deny statement. For example, you might approve one runtime from a trusted third-party publisher. The following SCP denies the `Associate` actions for all runtimes except the `thirdpartyruntime` runtime that account `999988887777` owns.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyAllRuntimesExceptApproved",
            "Effect": "Deny",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "NotResource": [
                "arn:aws:lambda:*:999988887777:runtime/thirdpartyruntime/alias/*",
                "arn:aws:lambda:*:999988887777:runtime/thirdpartyruntime/version/*"
            ]
        }
    ]
}
```

The wildcard in the Region part of each ARN covers the runtime in every Region. To approve only some aliases, list the alias ARNs instead of `alias/*`.

You can also combine this approach with an organization restriction. The following SCP allows runtimes that accounts in your organization own. It also allows the approved third-party `thirdpartyruntime` runtime. IAM applies the deny only if both conditions are true: the runtime isn't in the `NotResource` list, and the runtime owner is outside the organization.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyRuntimesOutsideOrganizationExceptApproved",
            "Effect": "Deny",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "NotResource": [
                "arn:aws:lambda:*:999988887777:runtime/thirdpartyruntime/alias/*",
                "arn:aws:lambda:*:999988887777:runtime/thirdpartyruntime/version/*"
            ],
            "Condition": {
                "StringNotEquals": {
                    "aws:ResourceOrgID": "o-a1b2c3d4e5"
                }
            }
        }
    ]
}
```

### Exempt specific roles from a restriction
<a name="cmr-permissions-exempt-role"></a>

You might need to let some roles use runtimes that the rest of your organization can't use. For example, a platform team might test new runtimes, or an emergency access (break-glass) role might need access during an incident. To do this, add the `aws:PrincipalArn` condition key with the `ArnNotLike` operator. The following SCP blocks all customer-managed runtimes, except for the `PlatformRuntimeAdmin` role in any account.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCustomerManagedRuntimesExceptPlatformRole",
            "Effect": "Deny",
            "Action": [
                "lambda:AssociateRuntimeAlias",
                "lambda:AssociateRuntimeVersion"
            ],
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": "arn:aws:iam::*:role/PlatformRuntimeAdmin"
                }
            }
        }
    ]
}
```

You can add the same condition to any of the previous examples. We recommend that you tightly control who can assume an exempt role. For more information, see [aws:PrincipalArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalarn) in the *IAM User Guide*.

## Control who can create and share runtimes
<a name="cmr-permissions-related-controls"></a>

In addition to controlling which runtimes functions can use, you can control how principals in your organization create and share runtimes. A runtime image can contain code, files, and data from your organization. Functions that use the runtime can read the entire runtime contents, including functions in other accounts. Sharing a runtime with accounts outside your organization is therefore a potential path for data to leave your organization.

### Prevent principals from creating runtimes
<a name="cmr-permissions-deny-create"></a>

To stop principals from publishing their own runtimes, deny the `lambda:CreateRuntime` action. The following SCP denies this action for all principals except the `PlatformRuntimeAdmin` role.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCreateRuntimeExceptPlatformRole",
            "Effect": "Deny",
            "Action": "lambda:CreateRuntime",
            "Resource": "*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": "arn:aws:iam::*:role/PlatformRuntimeAdmin"
                }
            }
        }
    ]
}
```

### Prevent principals from sharing runtimes outside your organization
<a name="cmr-permissions-deny-share"></a>

To stop principals from sharing runtimes publicly or with external accounts, deny the `lambda:PutResourcePolicy` action on runtimes. The following SCP denies the `lambda:PutResourcePolicy` action on all runtimes for all principals except the `PlatformRuntimeAdmin` role.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyRuntimePolicyExceptPlatformRole",
            "Effect": "Deny",
            "Action": "lambda:PutResourcePolicy",
            "Resource": "arn:aws:lambda:*:*:runtime/*",
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": "arn:aws:iam::*:role/PlatformRuntimeAdmin"
                }
            }
        }
    ]
}
```

The SCP blocks all runtime sharing by other principals, including sharing within your organization. The `PlatformRuntimeAdmin` role can still share runtimes in ways that follow your organization's rules, such as with the `aws:PrincipalOrgID` condition key. For more information, see [Share a runtime with an organization](#cmr-permissions-share-org).

## Permissions reference for customer-managed runtimes
<a name="cmr-permissions-reference"></a>

This section lists the IAM actions, resource ARN formats, and condition keys that this topic uses.

### IAM actions
<a name="cmr-permissions-actions"></a>

The following table lists the IAM actions for customer-managed runtimes.


**IAM actions for customer-managed runtimes**  

| Action | Resource type | Used by | 
| --- | --- | --- | 
| lambda:ListRuntimes | \* | Runtime publishers | 
| lambda:CreateRuntime | Runtime | Runtime publishers | 
| lambda:GetRuntime | Runtime | Runtime publishers, and optionally runtime consumers | 
| lambda:UpdateRuntime | Runtime | Runtime publishers | 
| lambda:DeleteRuntime | Runtime | Runtime publishers | 
| lambda:ListRuntimeVersions | Runtime | Runtime publishers, and optionally runtime consumers | 
| lambda:ListRuntimeAliases | Runtime | Runtime publishers, and optionally runtime consumers | 
| lambda:TagResource, lambda:UntagResource, lambda:ListTags | Runtime | Runtime publishers | 
| lambda:PutResourcePolicy, lambda:GetResourcePolicy, lambda:DeleteResourcePolicy | Runtime | Runtime publishers | 
| lambda:CreateRuntimeVersion | Runtime version | Runtime publishers | 
| lambda:GetRuntimeVersion | Runtime version | Runtime publishers, and optionally runtime consumers | 
| lambda:UpdateRuntimeVersion | Runtime version | Runtime publishers | 
| lambda:DeleteRuntimeVersion | Runtime version | Runtime publishers | 
| lambda:CreateRuntimeAlias | Runtime alias | Runtime publishers | 
| lambda:GetRuntimeAlias | Runtime alias | Runtime publishers, and optionally runtime consumers | 
| lambda:UpdateRuntimeAlias | Runtime alias | Runtime publishers | 
| lambda:DeleteRuntimeAlias | Runtime alias | Runtime publishers | 
| lambda:AssociateRuntimeAlias | Runtime alias | Runtime consumers, to configure a function to use an alias | 
| lambda:AssociateRuntimeVersion | Runtime version | Runtime consumers, to pin a function to a version | 
| lambda:RestoreRuntime | Runtime | Runtime publishers, to restore a runtime, runtime version, or runtime alias that's scheduled for deletion. Lambda authorizes restores of a version or alias against the runtime ARN. | 

To create a runtime version, publishers also need `ecr:BatchGetImage` and `ecr:GetDownloadUrlForLayer` on the Amazon ECR repository that contains the image. The resource is the repository ARN, in the format `arn:aws:ecr:{{region}}:{{account-id}}:repository/{{repository-name}}`. For more information, see [Required permissions](cmr-versions.md#cmr-publish-versions-iam).

### Resource ARN formats
<a name="cmr-permissions-arns"></a>

The following table shows the ARN format for each resource type. You can use the `*` wildcard to match all aliases or all versions of a runtime.


**ARN formats for customer-managed runtime resources**  

| Resource type | ARN format | Wildcard example | 
| --- | --- | --- | 
| Runtime | arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}} | arn:aws:lambda:us-east-1:123456789012:runtime/\* | 
| Runtime version | arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}/version/{{version-name}} | arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/version/\* | 
| Runtime alias | arn:aws:lambda:{{region}}:{{account-id}}:runtime/{{runtime-name}}/alias/{{alias-name}} | arn:aws:lambda:us-east-1:123456789012:runtime/companyphp8/alias/\* | 

The runtime version ARN uses the version name that you specify when you create the version. It doesn't use the image digest.

### Condition keys
<a name="cmr-permissions-condition-keys"></a>

The following table lists the global condition keys that the examples in this topic use.


**Condition keys for customer-managed runtime policies**  

| Condition key | Description | Typical use | 
| --- | --- | --- | 
| aws:PrincipalOrgID | The organization ID of the account that makes the request | Resource-based policies that share a runtime with an organization | 
| aws:PrincipalOrgPaths | The OU path of the account that makes the request | Resource-based policies that share a runtime with an OU | 
| aws:PrincipalArn | The ARN of the principal that makes the request | SCPs that exempt specific roles | 
| aws:ResourceOrgID | The organization ID of the account that owns the runtime | SCPs that allow only runtimes from your organization | 
| aws:ResourceAccount | The ID of the account that owns the runtime | SCPs that allow only runtimes from specific accounts | 
| aws:ResourceTag/{{key}} | A tag on the runtime (also used for the runtime's versions and aliases) | Attribute-based access control | 

For more information about these keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

When a principal in another account configures a function to use your runtime, AWS CloudTrail logs the request in both the caller's account and the runtime owner's account. The runtime owner's copy identifies the caller by account ID only. For more information, see [Logging customer-managed runtime API calls with CloudTrail](cmr-monitoring.md#cmr-monitoring-cloudtrail).


# Assigning custom permissions profiles

After you create a custom permissions profile, you can assign it to users, roles, or accounts. Users with sufficient permissions can also use the [`AWS::QuickSight::CustomPermissions`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermissions.html) CloudFormation resource to manage AWS Quick custom permissions profiles.

## Assigning a custom permissions profile (Quick console)
<a name="custom-permissions-assign-console"></a>

You can assign a custom permissions profile to specific users, roles, or to the entire account. Assigning a profile replaces any existing assignment at that level. A user, role, or account can only have one active custom permissions profile at a time.

**Note**  
If a user or role already has a custom permissions profile assigned, the new assignment replaces the previous one. The original profile is no longer active for that user or role. Similarly, if an account-level profile is already active, Quick displays a warning before you replace it.

**To assign a custom permissions profile**

1. Open the [Quick console](https://aws.amazon.com/quicksight/).

1. Choose **Manage Quick**.

1. In the left navigation, choose **Permissions**, and then choose **Custom permissions**.

1. On the **Custom permissions** page, locate the profile you want to assign. Choose the actions menu next to the profile, and then choose **Assign**.
**Tip**  
You can also assign a profile immediately after creating one. After you choose **Create** on the profile creation page, Quick takes you directly to the assignment page.

1. On the assignment page, configure who receives this profile:
   + **Users** – Enter the usernames of the users you want to assign this profile to. You can add multiple users.
   + **Groups** – Enter the names of the groups you want to assign this profile to. Every member of the group receives the profile. You can add multiple groups.
   + **Roles** – Select the Quick roles (Admin, Author, Reader) that you want to assign this profile to.
   + **Set as account default** – Select this option to apply the profile as the account-level default. If an account-level profile is already active, Quick displays a warning indicating that the existing assignment will be replaced.

1. When you are ready, choose **Assign**. You are returned to the custom permissions list page.

## Assigning custom permissions profiles (AWS CLI)
<a name="custom-permissions-assign-cli"></a>

Before you begin, you need to set up and configure the AWS CLI. For more information about installing the AWS CLI, see [Install or update the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the AWS Command Line Interface User guide. You also need permissions to use the Quick API.

### Updating custom permissions assignments
<a name="custom-permissions-assign-update"></a>

The following example updates the custom permissions that are assigned to a role.

```
aws quicksight update-role-custom-permission \
--role {{ROLE}} \
--aws-account-id {{AWSACCOUNTID}} \
--namespace default \
--custom-permissions-name {{PERMISSIONNAME}}
```

The following example applies a custom permissions profile to a user.

```
aws quicksight update-user-custom-permission \
--aws-account-id {{AWSACCOUNTID}} \
--namespace default \
--user-name {{USER_NAME}} \
--custom-permissions-name {{PERMISSIONNAME}}
```

The following example updates the custom permissions that are assigned to an account.

```
aws quicksight update-account-custom-permission \
--aws-account-id {{AWSACCOUNTID}} \
--custom-permissions-name {{PERMISSIONNAME}}
```

### Removing custom permissions assignments
<a name="custom-permissions-assign-delete"></a>

The following example deletes a custom permissions profile from a role.

```
aws quicksight delete-role-custom-permission \
--role {{ROLE}} \
--aws-account-id {{AWSACCOUNTID}} \
--namespace default
```

The following example deletes a custom permissions profile from a user.

```
aws quicksight delete-user-custom-permission \
--user-name {{USER_NAME}} \
--aws-account-id {{AWSACCOUNTID}} \
--namespace default
```

The following example removes a custom permissions profile from an account.

```
aws quicksight delete-account-custom-permission \
--aws-account-id {{AWSACCOUNTID}}
```

### Describing custom permissions assignments
<a name="custom-permissions-assign-describe"></a>

The following example returns the custom permissions profile that is assigned to a role.

```
aws quicksight describe-role-custom-permission \
--role {{ROLE}} \
--aws-account-id {{AWSACCOUNTID}} \
--namespace default
```

The following example returns the custom permissions profile that is assigned to an account.

```
aws quicksight describe-account-custom-permission \
--aws-account-id {{AWSACCOUNTID}}
```

## Assigning profiles to groups
<a name="custom-permissions-assign-groups"></a>

You can assign a custom permissions profile to a group. Every member of the group receives the profile. A user can belong to more than one group, and each group can have its own assigned profile.

**Note**  
Each account supports a maximum of 2,000 group assignments. A group assignment is a group that has a custom permissions profile assigned to it. If your account requires a higher limit, contact the Quick service team to request an increase.

A profile can apply to a user at several levels. Quick applies the most specific assignment, in this order: user, then group, then role, then account. A profile assigned directly to a user overrides any group profiles, and group profiles override role and account profiles. The resolution rules apply when the group level applies, that is, when the user has no profile assigned directly. For more information, see [How AWS Quick resolves multiple group assignments](#custom-permissions-assign-groups-resolution).

This section covers the following topics:
+ [Assigning a profile to a group (console)](#custom-permissions-assign-groups-console)
+ [Assigning profiles to groups with the API](#custom-permissions-assign-groups-api)
+ [How AWS Quick resolves multiple group assignments](#custom-permissions-assign-groups-resolution)

**Important**  
Custom permissions assignments read from user-identity fields will not reflect group-level custom permissions. In some cases, the value falls through to the role-level or account-level assignment instead of the group-level assignment. This behavior applies to the user-based operations that return user objects, such as `DescribeUser` and `ListUsers`. It also applies to any console page that lists users and their custom permissions. To see the effective custom permissions profile for a user, use the Check permissions feature in the custom permissions console. For more information, see [Verifying permissions for a user](#custom-permissions-verify).

### Assigning a profile to a group (console)
<a name="custom-permissions-assign-groups-console"></a>

You assign a profile to a group from the same assignment page used for users and roles. On the assignment page, in the **Groups** field, enter the names of the groups that you want to assign the profile to, and then choose **Assign**. For instructions on assigning a profile to a group, see [Assigning a custom permissions profile (Quick console)](#custom-permissions-assign-console).

### Assigning profiles to groups with the API
<a name="custom-permissions-assign-groups-api"></a>

You manage group assignments through the AWS Quick governance policy management operations. In these operations, you identify the custom permissions profile by its policy ARN (`PolicyArn`) and the group by its principal ARN (`PrincipalArn`). For custom permissions, the policy type (`PolicyType`) is `CUSTOM_PERMISSIONS`, and the principal type (`PrincipalType`) is `GROUP`. These operations currently only support group principals for custom permissions.

The following table lists the operations that manage policy assignments.


| Operation | Description | 
| --- | --- | 
| `PutPolicyAssignment` | Assigns a profile to one group, replacing any existing custom permissions assignment on that group. Returns the assigned `PolicyArn`, the displaced profile as `ReplacedPolicyArn` if one was replaced, and the new `Revision`. | 
| `BatchPutPolicyAssignmentByPolicy` | Assigns one profile to between 1 and 50 groups in a single call. The call is not atomic: The response lists `Success` and `Errors` for each group, so inspect `Errors` for any groups that failed. | 
| `GetPolicyAssignment` | Returns the profile currently assigned to a group for a given `PolicyType`, using a strongly consistent read. A group with no assignment returns an empty result. | 
| `DeletePolicyAssignment` | Removes a group's assignment to the named profile. It is idempotent: Removing an assignment that is not present still succeeds. If the group is assigned a different profile, the call fails with a conflict, so you do not remove the wrong one. | 
| `BatchDeletePolicyAssignmentByPolicy` | Removes between 1 and 50 groups' assignments to one profile in a single call. The call is not atomic: Inspect `Success` and `Errors`. | 
| `ListPrincipalsForPolicy` | Lists the principals assigned to a profile (a reverse lookup by `PolicyArn`). Optionally filter by `PrincipalType`, for example, `GROUP`. Results are paginated with `MaxResults` (1 to 100) and `NextToken`, and are eventually consistent. | 

These operations share the following parameters.

`AccountId`  
The ID of the AWS account that contains the Quick account.

`PolicyArn`  
The ARN of the custom permissions profile to assign or remove.

`PrincipalArn`  
The ARN of the group the assignment applies to.

`PolicyType`  
The policy type. For custom permissions, use `CUSTOM_PERMISSIONS`.

`PrincipalType`  
The principal type. For custom permissions, group assignments use `GROUP`, which is currently the only supported value. On `ListPrincipalsForPolicy`, this is an optional filter.

`ExistingPolicyArn`  
(Optional) The profile you believe is currently assigned to the group. When you provide it, the write proceeds only if it matches the current assignment, which prevents overwriting an assignment that changed since you last read it.

`Revision`  
(Optional) A compare-and-set token returned by the most recent read. When you provide it on a write, the change is applied only if it matches the assignment's current revision, which guards against concurrent updates.

#### Example commands (AWS CLI)
<a name="custom-permissions-assign-groups-api-examples"></a>

The following examples show how to manage group assignments with the AWS Command Line Interface (AWS CLI). The example commands use placeholders for values that you replace with your own:
+ {{account-id}} – The ID of your AWS account.
+ {{region}} – The AWS Region of your Quick account.
+ {{profile-name}} – The name of the custom permissions profile.
+ {{group-name}} – The name of the group, in the `default` namespace.

`PutPolicyAssignment` assigns the profile to one group:

```
aws quicksight put-policy-assignment \
--account-id {{account-id}} \
--policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{profile-name}} \
--principal-arn arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-name}}
```

To make the assignment conditional, add `--existing-policy-arn` (the profile you expect is currently assigned) or `--revision` (the token from your last read). The assignment proceeds only if the value matches the current assignment:

```
aws quicksight put-policy-assignment \
--account-id {{account-id}} \
--policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{profile-name}} \
--principal-arn arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-name}} \
--existing-policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{existing-profile-name}} \
--revision 3
```

`BatchPutPolicyAssignmentByPolicy` assigns one profile to up to 50 groups. The call is not atomic, so the output reports `Success` and `Errors` separately:

```
aws quicksight batch-put-policy-assignment-by-policy \
--account-id {{account-id}} \
--policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{profile-name}} \
--assignments \
PrincipalArn=arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-1}} \
PrincipalArn=arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-2}}
```

`GetPolicyAssignment` returns the profile currently assigned to a group:

```
aws quicksight get-policy-assignment \
--account-id {{account-id}} \
--policy-type CUSTOM_PERMISSIONS \
--principal-arn arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-name}}
```

`DeletePolicyAssignment` removes a group's assignment to the named profile:

```
aws quicksight delete-policy-assignment \
--account-id {{account-id}} \
--policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{profile-name}} \
--principal-arn arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-name}}
```

`BatchDeletePolicyAssignmentByPolicy` removes up to 50 groups' assignments to one profile:

```
aws quicksight batch-delete-policy-assignment-by-policy \
--account-id {{account-id}} \
--policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{profile-name}} \
--principal-arns \
arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-1}} \
arn:aws:quicksight:{{region}}:{{account-id}}:group/default/{{group-2}}
```

`ListPrincipalsForPolicy` lists the groups assigned to a profile. Filter with `--principal-type` and page with `--max-results` and `--next-token`:

```
aws quicksight list-principals-for-policy \
--account-id {{account-id}} \
--policy-arn arn:aws:quicksight:{{region}}:{{account-id}}:custompermissions/{{profile-name}} \
--principal-type GROUP \
--max-results 50
```

### How AWS Quick resolves multiple group assignments
<a name="custom-permissions-assign-groups-resolution"></a>

When a user belongs to more than one group and the group level applies, Quick combines all of the user's group profiles. A capability is available to the user only if none of their group profiles denies it. If any group profile denies a capability, it is denied for the user. This is the most restrictive combination of the profiles.

Deny by Default profiles take part the same way. A Deny by Default profile denies every capability in its restricted category except the capabilities it explicitly allows. This includes capabilities that Quick launches in that category later. Quick combines those denials with the other groups' denials.

The order of the groups does not matter. The combined result is the same.

#### Example 1: Two standard profiles
<a name="custom-permissions-assign-groups-example-standard"></a>

**Scenario:** A user belongs to two groups. The group Finance has the profile `FinanceNoExport`, which denies `ExportToCsv` and `ExportToPdf`. The group Reporting has the profile `NoExcelExport`, which denies `ExportToExcel`. Both are standard (allow-by-default) profiles.

```json
{
    "CustomPermissions": {
        "CustomPermissionsName": "FinanceNoExport",
        "Capabilities": {
            "ExportToCsv": "DENY",
            "ExportToPdf": "DENY"
        }
    }
}
```

```json
{
    "CustomPermissions": {
        "CustomPermissionsName": "NoExcelExport",
        "Capabilities": {
            "ExportToExcel": "DENY"
        }
    }
}
```

The following table shows how each group's denials combine for the user.


| Capability | Denied by `FinanceNoExport` | Denied by `NoExcelExport` | Denied for the user | 
| --- | --- | --- | --- | 
| `ExportToCsv` | Yes | No | Yes | 
| `ExportToPdf` | Yes | No | Yes | 
| `ExportToExcel` | No | Yes | Yes | 
| `ChatAgent` | No | No | No | 

**Result:** The user is denied `ExportToCsv`, `ExportToPdf`, and `ExportToExcel`. All other capabilities, such as `ChatAgent`, stay available because neither profile denies them.

#### Example 2: One Deny by Default profile and one standard profile
<a name="custom-permissions-assign-groups-example-mixed"></a>

**Scenario:** The group Finance has the standard profile `FinanceNoExport`, which denies `ExportToCsv`. The group AIReview has the profile `RestrictAI`, a Deny by Default profile on the `AI` category that explicitly allows only `ChatAgent`. `RestrictAI` therefore denies every AI capability except `ChatAgent`, for example, `Flow` and `Automate`, and also denies any AI capability launched later.

```json
{
    "CustomPermissions": {
        "CustomPermissionsName": "FinanceNoExport",
        "Capabilities": {
            "ExportToCsv": "DENY"
        }
    }
}
```

```json
{
    "CustomPermissions": {
        "CustomPermissionsName": "RestrictAI",
        "Capabilities": {
            "ChatAgent": "ALLOW"
        },
        "Governance": {
            "DefaultCategoryEffects": {
                "AI": "DENY_BY_DEFAULT"
            }
        }
    }
}
```

The following table shows how each group's denials combine for the user.


| Capability | Denied by `FinanceNoExport` | Denied by `RestrictAI` | Denied for the user | 
| --- | --- | --- | --- | 
| `ExportToCsv` | Yes | No | Yes | 
| `Flow` | No | Yes | Yes | 
| `ChatAgent` | No | No | No | 
| A new AI capability launched later | No | Yes | Yes | 

**Result:** The user is denied `ExportToCsv`, `Flow`, and every other AI capability except `ChatAgent`, including future AI capabilities. `ChatAgent` stays available because `RestrictAI` allows it, and `FinanceNoExport` does not deny it.

#### Example 3: Two Deny by Default profiles
<a name="custom-permissions-assign-groups-example-dbd"></a>

**Scenario:** Both of the user's groups use Deny by Default on the `AI` category but allow different capabilities. The group TeamA has the profile `AI-TeamA`, which allows `ChatAgent` and `Research`. The group TeamB has the profile `AI-TeamB`, which allows `ChatAgent` and `Topic`. Each profile denies every other AI capability, current and future.

```json
{
    "CustomPermissions": {
        "CustomPermissionsName": "AI-TeamA",
        "Capabilities": {
            "ChatAgent": "ALLOW",
            "Research": "ALLOW"
        },
        "Governance": {
            "DefaultCategoryEffects": {
                "AI": "DENY_BY_DEFAULT"
            }
        }
    }
}
```

```json
{
    "CustomPermissions": {
        "CustomPermissionsName": "AI-TeamB",
        "Capabilities": {
            "ChatAgent": "ALLOW",
            "Topic": "ALLOW"
        },
        "Governance": {
            "DefaultCategoryEffects": {
                "AI": "DENY_BY_DEFAULT"
            }
        }
    }
}
```

The following table shows how each group's denials combine for the user.


| Capability | Denied by `AI-TeamA` | Denied by `AI-TeamB` | Denied for the user | 
| --- | --- | --- | --- | 
| `ChatAgent` | No | No | No | 
| `Research` | No | Yes | Yes | 
| `Topic` | Yes | No | Yes | 
| Any other AI capability (current or future) | Yes | Yes | Yes | 

**Result:** Among AI capabilities, only `ChatAgent`, the capability both profiles allow, stays available. `Research` and `Topic` are each denied because only one of the two profiles allows them. When two Deny by Default profiles combine, the user keeps only the capabilities that both profiles explicitly allow.

To test the custom permissions that are applied to a role or user, log in to the user's account. When a user logs into Quick, they are granted the highest privilege role that they have access to. The highest privileged role a user can be granted is Admin. The lowest privileged role that a user can be granted is Reader. For more information about roles in Quick, see [Managing user access inside Quick](https://docs.aws.amazon.com/quicksight/latest/user/managing-users.html).

## Verifying permissions for a user
<a name="custom-permissions-verify"></a>

After you assign a custom permissions profile, you can verify which profile is active for any user and at which level it applies.

**To verify a user's active permissions profile**

1. Open the [Quick console](https://aws.amazon.com/quicksight/).

1. Choose **Manage Quick**.

1. In the left navigation, choose **Permissions**, and then choose **Custom permissions**.

1. Choose **Check permissions**.

1. Enter the username of the user you want to verify.

1. Quick displays the active profile name and the level at which it applies (user, group, role, or account). When the group level applies, a user can belong to more than one group that has an assigned profile. In that case, Quick shows the profiles from all of those groups, because the user's effective permissions combine them. For more information, see [How AWS Quick resolves multiple group assignments](#custom-permissions-assign-groups-resolution).

Use this feature to confirm that Deny by Default profiles are correctly applied and that precedence is working as expected.
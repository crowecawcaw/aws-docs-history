# Use scripts to bulk migrate your policies to use

fine-grained IAM actions

###### Note

The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:

- `*aws-portal*` namespace
- `*purchase-orders:ViewPurchaseOrders*`
- `*purchase-orders:ModifyPurchaseOrders*`
  If you're using AWS Organizations, you can use the bulk policy migrator scripts or bulk policy migrator to update
  polices from your payer account. You can also use the [old to granular action
  mapping reference](migrate-granularaccess-iam-mapping-reference.md "migrate-granularaccess-iam-mapping-reference.md") to verify the IAM actions that need to be added.

If you have an AWS account, or are a part of an AWS Organizations created on or after
March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your
organization.

To help migrate your IAM policies to use new actions, known as fine-grained actions, you
can use scripts from the [AWS
Samples](https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles "https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles") website.

You run these scripts from the payer account of your organization to identify the following
affected policies in your organization that use the old IAM actions:

- Customer managed IAM policies
- Role, group, and user IAM inline policies
- Service control policies (SCPs) (applies to the payer account only)
- Permission sets
  The scripts generate suggestions for new actions that correspond to existing actions that
  are used in the policy. You then review the suggestions and use the scripts to add the new
  actions across all affected policies in your organization. You don't need to update AWS
  managed policies or AWS managed SCPs (for example, AWS Control Tower and AWS Organizations SCPs).

You use these scripts to:

- Streamline the policy updates to help you manage the affected policies from the payer
  account.
- Reduce the amount of time that you need to update the policies. You don't need to sign
  into each member account and manually update the policies.
- Group identical policies from different member accounts together. You can then review
  and apply the same updates across all identical policies, instead of reviewing them one by
  one.
- Ensure that user access remains unaffected after AWS retires the old IAM actions on
  July 6, 2023.
  For more information about policies and service control policies (SCPs), see the following
  topics:

- [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _IAM User Guide_
- [Service control
  policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_
- [Custom permissions](../../../singlesignon/latest/userguide/permissionsetcustom.md "../../../singlesignon/latest/userguide/permissionsetcustom.md") in the _IAM Identity Center User Guide_

## Overview

Follow this topic to complete the following steps:

###### Topics

- [Prerequisites](#prerequisites-running-the-scripts "#prerequisites-running-the-scripts")
- [Step 1: Set up your
  environment](#set-up-your-environment-and-download-the-scripts "#set-up-your-environment-and-download-the-scripts")
- [Step 2: Create the CloudFormation
  StackSet](#create-the-cloudformation-stack "#create-the-cloudformation-stack")
- [Step 3: Identify the affected
  policies](#identify-the-affected-policies "#identify-the-affected-policies")
- [Step 4: Review the suggested changes](#review-the-affected-policies "#review-the-affected-policies")
- [Step 5: Update the affected policies](#update-the-affected-policies "#update-the-affected-policies")
- [Step 6: Revert your changes (Optional)](#revert-changes "#revert-changes")
- [IAM policy examples](#examples-of-similar-policies "#examples-of-similar-policies")

## Prerequisites

To get started, you must do the following:

- Download and install [Python 3](https://www.python.org/downloads/ "https://www.python.org/downloads/")
- Sign in to your payer account and verify that you have an IAM principal that has the
  following IAM permissions:

```
"iam:GetAccountAuthorizationDetails",
"iam:GetPolicy",
"iam:GetPolicyVersion",
"iam:GetUserPolicy",
"iam:GetGroupPolicy",
"iam:GetRole",
"iam:GetRolePolicy",
"iam:CreatePolicyVersion",
"iam:DeletePolicyVersion",
"iam:ListAttachedRolePolicies",
"iam:ListPolicyVersions",
"iam:PutUserPolicy",
"iam:PutGroupPolicy",
"iam:PutRolePolicy",
"iam:SetDefaultPolicyVersion",
"organizations:ListAccounts",
"organizations:ListPolicies",
"organizations:DescribePolicy",
"organizations:UpdatePolicy",
"organizations:DescribeOrganization",
"sso:DescribePermissionSet",
"sso:DescribePermissionSetProvisioningStatus",
"sso:GetInlinePolicyForPermissionSet",
"sso:ListInstances",
"sso:ListPermissionSets",
"sso:ProvisionPermissionSet",
"sso:PutInlinePolicyToPermissionSet",
"sts:AssumeRole"
```

###### Tip

To get started, we recommend that you use a subset of an account, such as a test
account, to verify that the suggested changes are expected.

You can then run the scripts again for remaining accounts in your organization.

## Step 1: Set up your

environment

To get started, download the required files from the [AWS
Samples](https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles "https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles") website. You then run commands
to set up your environment.

###### To set up your environment

1. Clone the repository from the [AWS
   Samples](https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles "https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles") website. In a command line window, you can use the
   following command:

```
git clone https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles.git
```

2. Navigate to the directory where you downloaded the files. You can use the following
   command:

```
cd bulk-policy-migrator-scripts-for-account-cost-billing-consoles
```

In the repository, you can find the following scripts and resources:

    * `billing_console_policy_migrator_role.json` – The CloudFormation template that creates the
     ``BillingConsolePolicyMigratorRole`` IAM role in member accounts of your organization. This
     role allows the scripts to assume the role, and then read and update the affected
     policies.
    * `action_mapping_config.json`– Contains the one-to-many mapping of the old actions to the
     new actions. The scripts use this file to suggest the new actions for each affected
     policy that contains the old actions.


    Each old action corresponds to multiple fine-grained actions. The new actions
     suggested in the file provide users access to the same AWS services before the
     migration.
    * `identify_affected_policies.py` – Scans and identifies affected policies in your
     organization. This script generates a `affected_policies_and_suggestions.json` file that lists the affected
     policies along with the suggested new actions.


    Affected policies that use the same set of old actions are grouped together in the
     JSON file, so that you can review or update the suggested new actions.
    * `update_affected_policies.py` – Updates the affected policies in your organization. The
     script inputs the`affected_policies_and_suggestions.json` file, and then adds the suggested new actions to the
     policies.
    * `rollback_affected_policies.py` – (Optional) Reverts changes made to the affected
     policies. This script removes the new fine-grained actions from the affected
     policies.

3. Run the following commands to set up and activate the virtual environment.

```
python3 -m venv venv
```

```
source venv/bin/activate
```

4. Run the following command to install the AWS SDK for Python (Boto3) dependency.

```
pip install -r requirements.txt
```

###### Note

You must configure your AWS credentials to use the AWS Command Line Interface (AWS CLI). For more
information, see [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html").

For more information, see the [README.md](https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles#readme "https://github.com/aws-samples/bulk-policy-migrator-scripts-for-account-cost-billing-consoles#readme") file.

## Step 2: Create the CloudFormation

StackSet

Follow this procedure to create a CloudFormation _stack set_. This stack
set then creates the `BillingConsolePolicyMigratorRole` IAM role for all member accounts in your
organization.

###### Note

You only need to complete this step once from the management account (payer
account).

###### To create the CloudFormation StackSet

1. In a text editor, open the `billing_console_policy_migrator_role.json` file, and replace each instance of
   `<management_account>` with the account ID of
   the payer account (for example, `123456789012`).
2. Save the file.
3. Sign in to the AWS Management Console as the payer account.
4. In the CloudFormation console, create a stack set with the `billing_console_policy_migrator_role.json` file that you
   updated.

For more information, see [Creating a stack set on the AWS CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.md") in the
_AWS CloudFormation User Guide_.

After CloudFormation creates the stack set, each member account in your organization has an
`BillingConsolePolicyMigratorRole` IAM role.

The IAM role contains the following permissions:

```
"iam:GetAccountAuthorizationDetails",
"iam:GetPolicy",
"iam:GetPolicyVersion",
"iam:GetUserPolicy",
"iam:GetGroupPolicy",
"iam:GetRolePolicy",
"iam:CreatePolicyVersion",
"iam:DeletePolicyVersion",
"iam:ListPolicyVersions",
"iam:PutUserPolicy",
"iam:PutGroupPolicy",
"iam:PutRolePolicy",
"iam:SetDefaultPolicyVersion"
```

###### Notes

- For each member account, the scripts call the [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API operation to get temporary credentials to assume the `BillingConsolePolicyMigratorRole` IAM role.
- The scripts call the [ListAccounts](../../../organizations/latest/APIReference/API_ListAccounts.md "../../../organizations/latest/APIReference/API_ListAccounts.md") API operation to get all member accounts.
- The scripts also call IAM API operations to perform the read and write permissions to the policies.

## Step 3: Identify the affected

policies

After you create the stack set and downloaded the files, run the `identify_affected_policies.py` script.
This script assumes the `BillingConsolePolicyMigratorRole` IAM role for each member account, and then identifies
the affected policies.

###### To identify the affected policies

1. Navigate to the directory where you downloaded the scripts.

```
cd policy_migration_scripts/scripts
```

2. Run the `identify_affected_policies.py` script.

You can use the following input parameters:

- AWS accounts that you want the script to scan. To specify accounts, use the
  following input parameters:
  - `--all` – Scans all member accounts in your organization.

  ```
  python3 `identify_affected_policies.py` --all
  ```

  - `--accounts` – Scans a subset of member accounts in your
    organization.

  ```
  python3 `identify_affected_policies.py` --accounts 111122223333, 444455556666, 777788889999
  ```

  - `--exclude-accounts`– Excludes specific member accounts in your
    organization.

  ```
  python3 `identify_affected_policies.py` --all --exclude-accounts 111111111111, 222222222222, 333333333333
  ```

- `–-action-mapping-config-file`– (Optional) Specify the path to the
  `action_mapping_config.json` file. The script uses this file to generate suggested updates for affected
  policies. If you don't specify the path, the script uses the `action_mapping_config.json` file in the
  folder.

```
python3 `identify_affected_policies.py` –-action-mapping-config-file c:\Users\username\Desktop\Scripts\`action_mapping_config.json` –-all
```

###### Note

You can't specify organizational units (OUs) with this script.

After you run the script, it creates two JSON files in a
`Affected_Policies_`<Timestamp>``
folder:

- `affected_policies_and_suggestions.json`
- `detailed_affected_policies.json`

**`affected_policies_and_suggestions.json`**

Lists the affected policies with the suggested new actions. Affected policies that
use the same set of old actions are grouped together in the file.

This file contains the following sections:

- Metadata that provides an overview of the accounts that you specified in the
  script, including:
  - Accounts scanned and the input parameter used for the `identify_affected_policies.py`
    script
  - Number of affected accounts
  - Number of affected policies
  - Number of similar policy groups

- Similar policy groups – Includes the list of accounts and policy details,
  including the following sections:
  - `ImpactedPolicies` – Specifies which policies are affected
    and included in the group
  - `ImpactedPolicyStatements` – Provides information about
    the `Sid` blocks that currently use the old actions in the affected
    policy. This section includes the old actions and IAM elements, such as
    `Effect`, `Principal`, `NotPrincipal`,
    `NotAction`, and `Condition`.

- `SuggestedPolicyStatementsToAppend` – Provides the suggested
  new actions that are added as new `SID` block.

When you update the policies, this block is appended at the end of the
policies.

###### Example `affected_policies_and_suggestions.json` file

This file groups together policies that are similar based on the following
criteria:

- Same old actions used – Policies that have the same old actions across
  all `SID` blocks.
- Matching details – In addition to affected actions, the policies have
  identical IAM elements,such as:
  - `Effect` (`Allow`/`Deny`)
  - `Principal` (who is allowed or denied access)
  - `NotAction` (what actions are not allowed)
  - `NotPrincipal` (who is explicitly denied access)
  - `Resource` (which AWS resources the policy applies to)
  - `Condition` (any specific conditions under which the policy
    applies)

###### Note

For more information, see [IAM policy examples](#examples-of-similar-policies "#examples-of-similar-policies").

###### Example `affected_policies_and_suggestions.json`

```
[{
        "AccountsScanned": [
            "111111111111",
            "222222222222"
        ],
        "TotalAffectedAccounts": 2,
        "TotalAffectedPolicies": 2,
        "TotalSimilarPolicyGroups": 2
    },
    {
        "GroupName": "Group1",
        "ImpactedPolicies": [{
                "Account": "111111111111",
                "PolicyType": "UserInlinePolicy",
                "PolicyName": "Inline-Test-Policy-Allow",
                "PolicyIdentifier": "1111111_1-user:Inline-Test-Policy-Allow"
            },
            {
                "Account": "222222222222",
                "PolicyType": "UserInlinePolicy",
                "PolicyName": "Inline-Test-Policy-Allow",
                "PolicyIdentifier": "222222_1-group:Inline-Test-Policy-Allow"
            }
        ],
        "ImpactedPolicyStatements": [
            [{
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "aws-portal:ViewAccounts"
                ],
                "Resource": "*"
            }]
        ],
        "SuggestedPolicyStatementsToAppend": [{
            "Sid": "BillingConsolePolicyMigrator0",
            "Effect": "Allow",
            "Action": [
                "account:GetAccountInformation",
                "account:GetAlternateContact",
                "account:GetChallengeQuestions",
                "account:GetContactInformation",
                "billing:GetContractInformation",
                "billing:GetIAMAccessPreference",
                "billing:GetSellerOfRecord",
                "payments:ListPaymentPreferences"
            ],
            "Resource": "*"
        }]
    },
    {
        "GroupName": "Group2",
        "ImpactedPolicies": [{
                "Account": "111111111111",
                "PolicyType": "UserInlinePolicy",
                "PolicyName": "Inline-Test-Policy-deny",
                "PolicyIdentifier": "1111111_2-user:Inline-Test-Policy-deny"
            },
            {
                "Account": "222222222222",
                "PolicyType": "UserInlinePolicy",
                "PolicyName": "Inline-Test-Policy-deny",
                "PolicyIdentifier": "222222_2-group:Inline-Test-Policy-deny"
            }
        ],
        "ImpactedPolicyStatements": [
            [{
                "Sid": "VisualEditor0",
                "Effect": "deny",
                "Action": [
                    "aws-portal:ModifyAccount"
                ],
                "Resource": "*"
            }]
        ],
        "SuggestedPolicyStatementsToAppend": [{
            "Sid": "BillingConsolePolicyMigrator1",
            "Effect": "Deny",
            "Action": [
                "account:CloseAccount",
                "account:DeleteAlternateContact",
                "account:PutAlternateContact",
                "account:PutChallengeQuestions",
                "account:PutContactInformation",
                "billing:PutContractInformation",
                "billing:UpdateIAMAccessPreference",
                "payments:UpdatePaymentPreferences"
            ],
            "Resource": "*"
        }]
    }
]
```

**`detailed_affected_policies.json`**

Contains the definition of all affected policies that the `identify_affected_policies.py` script
identified for member accounts.

The file groups similar policies together. You can use this file as reference, so
that you can review and manage policy changes without needing to sign in to each member
account to review the updates for each policy and account individually.

You can search the file for the policy name (for example,
`YourCustomerManagedReadOnlyAccessBillingUser`)
and then review the affected policy definitions.

###### Example: `detailed_affected_policies.json`

## Step 4: Review the suggested changes

After the script creates the `affected_policies_and_suggestions.json` file, review it and make any changes.

###### To review the affected policies

1. In a text editor, open the `affected_policies_and_suggestions.json` file.
2. In the `AccountsScanned` section, verify that the number of similar groups
   identified across the scanned accounts is expected.
3. Review the suggested fine-grained actions that will be added to the affected
   policies.
4. Update your file as needed and then save it.

### Example 1: Update the

`action_mapping_config.json` file

You can update the suggested mappings in the `action_mapping_config.json`. After you update the file,
you can rerun the `identify_affected_policies.py` script. This script generates updated suggestions for
the affected policies.

You can make multiple versions of the `action_mapping_config.json` file to change the policies for
different accounts with different permissions. For example, you might create one file named
`action_mapping_config_testing.json` to migrate permissions for your
test accounts and `action_mapping_config_production.json` for your
production accounts.

### Example 2: Update the

`affected_policies_and_suggestions.json` file

To make changes to the suggested replacements for a specific affected policy group, you
can directly edit the suggested replacements section within the `affected_policies_and_suggestions.json` file.

Any changes that you make in this section are applied to all policies within that
specific affected policy group.

### Example 3: Customize a specific

policy

If you find that a policy within an affected policy group that needs different changes
than the suggested updates, you can do the following:

- Exclude specific accounts from the `identify_affected_policies.py` script. You can then review
  those excluded accounts separately.
- Update the affected `Sid` blocks by removing the affected policies and
  accounts that need different permissions. Create a JSON block that includes only the
  specific accounts or excludes them from the current update affected policy run.

When you rerun the `identify_affected_policies.py` script, only the relevant accounts appear in
the updated block. You can then refine the suggested replacements for that specific
`Sid` block.

## Step 5: Update the affected policies

After you review and refine the suggested replacements, run the `update_affected_policies.py` script.
The script takes the `affected_policies_and_suggestions.json` file as input. This script assumes the `BillingConsolePolicyMigratorRole`
IAM role to update the affected policies listed in the
`affected_policies_and_suggestions.json` file.

###### To update the affected policies

1. If you haven't already, open a command line window for the AWS CLI.
2. Enter the following command to run the `update_affected_policies.py` script. You can enter the
   following input parameter:

- The directory path of the `affected_policies_and_suggestions.json` file that contains a list of the affected
  policies to be updated. This file is an output of the previous step.

```
python3 `update_affected_policies.py` --affected-policies-directory Affected_Policies_`<Timestamp>`
```

The `update_affected_policies.py` script updates the affected policies within the `affected_policies_and_suggestions.json` file
with the suggested new actions. The script adds a `Sid` block to the policies,
identified as `BillingConsolePolicyMigrator`#``, where
 `#` corresponds to an incremental counter (for example, 1, 2, 3).

For example, if there are multiple `Sid` blocks in the affected policy that use
old actions, the script adds multiple `Sid` blocks that appear as
`BillingConsolePolicyMigrator`#``to correspond to
 each`Sid` block.

###### Important

- The script doesn't remove old IAM actions from the policies, and or change
  existing `Sid` blocks in the policies. Instead, it creates `Sid`
  blocks and appends them to the end of the policy. These new `Sid` blocks have
  the suggested new actions from the JSON file. This ensures that the permissions of the
  original policies aren't changed.
- We recommend that you do not change the name of the
  `BillingConsolePolicyMigrator`#``
`Sid` blocks in case you need to revert your changes.

###### Example: Policy with appended `Sid` blocks

See the appended `Sid` blocks in the
`BillingConsolePolicyMigrator1` and `BillingConsolePolicyMigrator2`
blocks.

The script generates a status report that contains unsuccessful operations and outputs the
JSON file locally.

###### Example: Status report

```
[{
    "Account": "111111111111",
    "PolicyType": "Customer Managed Policy"
    "PolicyName": "AwsPortalViewPaymentMethods",
    "PolicyIdentifier": "identifier",
    "Status": "FAILURE", // FAILURE or SKIPPED
    "ErrorMessage": "Error message details"
}]
```

###### Important

- If you re-run the `identify_affected_policies.py` and `update_affected_policies.py` scripts , they skip all
  policies that contain the
  `BillingConsolePolicyMigratorRole`#```Sid` block. The
  scripts assume that those policies were previously scanned and updated, and that they
  don't require additional updates. This prevents the script from duplicating the same
  actions in the policy.
- After you update the affected policies, you can use the new IAM by using the
  affected policies tool. If you identify any issues, you can use the tool to switch back
  to the previous actions. You can also use a script to revert your policy updates.

For more information, see [How to use the affected policies
tool](migrate-security-iam-tool.md "migrate-security-iam-tool.md") and the [Changes to AWS Billing, Cost Management, and Account Consoles
Permissions](https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/changes-to-aws-billing-cost-management-and-account-consoles-permissions/") blog post.

- To manage your updates, you can:
  - Run the scripts for each account individually.
  - Run the script in batches for similar accounts, such as testing, QA, and
    production accounts.
  - Run the script for all accounts.
  - Choose a mix between updating some accounts in batches, and then updating others
    individually.

## Step 6: Revert your changes (Optional)

The `rollback_affected_policies.py` script reverts the changes applied to each affected policy for the
specified accounts. The script removes all `Sid` blocks that the `update_affected_policies.py`
script appended. These `Sid` blocks have the
`BillingConsolePolicyMigratorRole`#`` format.

###### To revert your changes

1. If you haven't already, open a command line window for the AWS CLI.
2. Enter the following command to run the `rollback_affected_policies.py` script. You can enter the
   following input parameters:

- `--accounts`
  - Specifies a comma-separated list of the AWS account IDs that you want to include
    in the rollback.
  - The following example scans the policies in the specified AWS accounts, and
    removes any statements with the
    `BillingConsolePolicyMigrator`#``
`Sid` block.

  ```
  python3 `rollback_affected_policies.py` –-accounts 111122223333, 555555555555, 666666666666
  ```

- `--all`
  - Includes all AWS account IDs in your organization.
  - The following example scans all policies in your organization, and removes any
    statements with the `BillingConsolePolicyMigratorRole`#``
`Sid` block.

```
python3 `rollback_affected_policies.py` –-all
```

- `--exclude-accounts`
  - Specifies a comma-separated list of the AWS account IDs that you want to exclude
    from the rollback.

  You can use this parameter only when you also specify the `--all`
  parameter.
  - The following example scans the policies for all AWS accounts in your
    organization, except for the specified accounts.

  ```
  python3 `rollback_affected_policies.py` --all --exclude-accounts 777777777777, 888888888888, 999999999999
  ```

## IAM policy examples

Policies are considered similar if they have identical:

- Affected actions across all `Sid` blocks.
- Details in the following IAM elements:
  - `Effect` (`Allow`/`Deny`)
  - `Principal` (who is allowed or denied access)
  - `NotAction` (what actions are not allowed)
  - `NotPrincipal` (who is explicitly denied access)
  - `Resource` (which AWS resources the policy applies to)
  - `Condition` (any specific conditions under which the policy
    applies)

The following examples show policies which IAM might or might not consider similar based
on the differences between them.

###### Example 1: Policies are considered similar

Each policy type is different, but both policies contain one `Sid` block with
the same affected `Action`.

Policy 1: Group inline IAM policy
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewAccount",
 "aws-portal:*Billing"
 ],
 "Resource": "*"
 }]
}`

```

Policy 2: Customer managed IAM policy
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewAccount",
 "aws-portal:*Billing"
 ],
 "Resource": "*"
 }]
}`

```

###### Example 2: Policies are considered similar

Both policies contain one `Sid` block with the same affected
`Action`. Policy 2 contains additional actions, but these actions aren't
affected.

Policy 1
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewAccount",
 "aws-portal:*Billing"
 ],
 "Resource": "*"
 }]
}`

```

Policy 2
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewAccount",
 "aws-portal:*Billing",
 "athena:*"
 ],
 "Resource": "*"
 }]
}`

```

###### Example 3: Policies aren't considered similar

Both policies contain one `Sid` block with the same affected
`Action`. However, policy 2 contains a `Condition` element that
isn't present in policy 1.

Policy 1
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewAccount",
 "aws-portal:*Billing"
 ],
 "Resource": "*"
 }]
}`

```

Policy 2
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:ViewAccount",
 "aws-portal:*Billing",
 "athena:*"
 ],
 "Resource": "*",
 "Condition": {
 "BoolIfExists": {
 "aws:MultiFactorAuthPresent": "true"
 }
 }
 }]
}`

```

###### Example 4: Policies are considered similar

Policy 1 has a single `Sid` block with an affected `Action`.
Policy 2 has multiple `Sid` blocks, but the affected `Action` appears
in only one block.

Policy 1
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:View*"
 ],
 "Resource": "*"
 }]
}`

```

Policy 2
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:View*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:Get*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example 5: Policies aren't considered similar

Policy 1 has a single `Sid` block with an affected `Action`.
Policy 2 has multiple `Sid` blocks, and the affected `Action` appears
in multiple blocks.

Policy 1
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:View*"
 ],
 "Resource": "*"
 }]
}`

```

Policy 2
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:View*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "aws-portal:Modify*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example 6: Policies are considered similar

Both policies have multiple `Sid` blocks, with the same affected
`Action` in each `Sid` block.

Policy 1
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:*Account",
 "iam:Get*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "aws-portal:Modify*",
 "iam:Update*"
 ],
 "Resource": "*"
 }
 ]
}`

```

Policy 2
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:*Account",
 "athena:Get*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "aws-portal:Modify*",
 "athena:Update*"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Example 7

The following two policies aren't considered similar.

Policy 1 has a single `Sid` block with an affected `Action`.
Policy 2 has a `Sid` block with the same affected `Action`. However,
policy 2 also contains another `Sid` block with different actions.

Policy 1
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:*Account",
 "iam:Get*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "aws-portal:Modify*",
 "iam:Update*"
 ],
 "Resource": "*"
 }
 ]
}`

```

Policy 2
JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "aws-portal:*Account",
 "athena:Get*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Deny",
 "Action": [
 "aws-portal:*Billing",
 "athena:Update*"
 ],
 "Resource": "*"
 }
 ]
}`

```

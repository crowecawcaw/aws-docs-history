# Updating organization policies with AWS Organizations

When your policy requirements change, you can update an existing policy.

This topic describes how to update policies with AWS Organizations. A _policy_
defines the controls that you want to apply to a group of AWS accounts.

###### Topics

- [Update a service control policy (SCP)](#update_policy "#update_policy")
- [Update a resource control policy (RCP)](#update_policy-rcp "#update_policy-rcp")
- [Update a declarative
  policy](#update-declarative-policy-procedure "#update-declarative-policy-procedure")
- [Update a backup policy](#update-backup-policy-procedure "#update-backup-policy-procedure")
- [Update a tag policy](#update-tag-policy-procedure "#update-tag-policy-procedure")
- [Update a chat applications
  policy](#update-chatbot-policy-procedure "#update-chatbot-policy-procedure")
- [Update an AI services opt-out
  policy](#update-ai-opt-out-policy-procedure "#update-ai-opt-out-policy-procedure")
- [Update a Security Hub policy](#update-security-hub-policy-procedure "#update-security-hub-policy-procedure")

## Update a service control policy (SCP)

When you sign in to your organization's management account, you can rename or change
the contents of a policy. Changing the contents of an SCP immediately affects any users,
groups, and roles in all attached accounts.

###### Minimum permissions

To update an SCP, you need permission to run the following actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")

AWS Management Console

###### To update a policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Service control policies](https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy "https://console.aws.amazon.com/organizations/v2/home/policies/service-control-policy")** page, choose the name of the policy that you
   want to update.
3. On the policy's detail page, choose **Edit
   policy**.
4. Make any or all of the following changes:
   - You can rename the policy by entering a new name in
     **Policy name**.
   - You can change the description by entering new text in
     **Policy description**.
   - You can edit the policy text by editing the policy in JSON
     format in the left pane. Alternatively, you can choose a
     statement in the editor on the right, and also alter its
     elements by using the controls. For more details about each
     control, see the [Creating an
     SCP procedure](orgs_policies_create.md#create-an-scp "orgs_policies_create.md#create-an-scp") earlier in this topic.

5. When you're finished, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following commands to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "MyRenamedPolicy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "MyRenamedPolicy",
 "Description": "Blocks all IAM actions",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

The following example adds or changes the description for a
service control policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --description "My new policy description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "MyRenamedPolicy",
 "Description": "My new policy description",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

The following example changes the policy document of the SCP by
specifying a file that contains the new JSON policy text.

```
`$` **aws organizations update-policy \
 --policy-id p-zlfw1r64
 --content file://MyNewPolicyText.json**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "MyRenamedPolicy",
 "Description": "My new policy description",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"AModifiedPolicy\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update a resource control policy (RCP)

When you sign in to your organization's management account, you can rename or change
the contents of a policy. Changing the contents of an RCP immediately affects any
resources in all attached accounts.

###### Minimum permissions

To update an RCP, you need permission to run the following actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")

AWS Management Console

###### To update a policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **Resource control policy** page, choose
   the name of the policy that you want to update.
3. On the policy's detail page, choose **Edit
   policy**.
4. Make any or all of the following changes:
   - You can rename the policy by entering a new name in
     **Policy name**.
   - You can change the description by entering new text in
     **Policy description**.
   - You can edit the policy text by editing the policy in JSON
     format in the left pane. Alternatively, you can choose a
     statement in the editor on the right, and also alter its
     elements by using the controls. For more details about each
     control, see the [Creating an
     RCP procedure](orgs_policies_create.md#create-an-rcp "orgs_policies_create.md#create-an-rcp") earlier in this topic.

5. When you're finished, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following commands to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "MyRenamedPolicy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "MyRenamedPolicy",
 "Description": "Blocks all IAM actions",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

The following example adds or changes the description for a
resource control policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --description "My new policy description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "MyRenamedPolicy",
 "Description": "My new policy description",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"Statement1\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

The following example changes the policy document of the RCP by
specifying a file that contains the new JSON policy text.

```
`$` **aws organizations update-policy \
 --policy-id p-zlfw1r64
 --content file://MyNewPolicyText.json**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/service_control_policy/p-i9j8k7l6m5",
 "Name": "MyRenamedPolicy",
 "Description": "My new policy description",
 "Type": "SERVICE_CONTROL_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"Version\":\"2012-10-17\", \"Statement\":[{\"Sid\":\"AModifiedPolicy\",\"Effect\":\"Deny\",\"Action\":[\"iam:*\"],\"Resource\":[\"*\"]}]}"
 }
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update a declarative

policy

###### Minimum permissions

To update a declarative policy, you must have permission to run the following
actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the Amazon Resource Name
  (ARN) of the specified policy (or "\*")

AWS Management Console

###### To update a declarative policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Declarative policies](https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2 "https://console.aws.amazon.com/organizations/v2/home/policies/declarative-policy-ec2")** page, choose the
   name of the policy that you want to update.
3. On the policy's detail page, choose **Edit
   policy**.
4. You can enter a new **Policy name**,
   **Policy description**, or edit the
   **JSON** policy text. For information about
   declarative policy syntax, see [Declarative policy syntax and
   examples](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md").
5. When you're finished updating the policy, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a declarative policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "Renamed policy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/declarative_policy_ec2/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Type": "DECLARATIVE_POLICY_EC2",
 "AwsManaged": false
 },
 "Content": "{"ec2-configuration":{"ec2_attributes":{"image_block_public_access":{"state":{"@@assign":"block_new_sharing"}}}}".
 }
}`
```

The following example adds or changes the description for a
declarative policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --description "My new description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/declarative_policy_ec2/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Description": "My new description",
 "Type": "DECLARATIVE_POLICY_EC2",
 "AwsManaged": false
 },
 "Content": "{"ec2_attributes":{"image_block_public_access":{"state":{"@@assign":"block_new_sharing"}}}}".
 }
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update a backup policy

When you sign in to your organization's management account, you can edit a policy that
requires changes in your organization.

###### Minimum permissions

To update a backup policy, you must have permission to run the following
actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the policy to
  update (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the policy to
  update (or "\*")

AWS Management Console

###### To update a backup policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Backup policies](https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy "https://console.aws.amazon.com/organizations/v2/home/policies/backup-policy")** page, choose the name of the policy that
   you want to update.
3. Choose **Edit policy**.
4. You can enter a new **Policy name**,
   **Policy description**. You can change the
   policy content by using either the **Visual
   editor** or by directly editing the
   **JSON**.
5. When you're finished updating the policy, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To update a backup policy

You can use one of the following to update a backup policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a backup policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "Renamed policy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/backup_policy/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Type": "BACKUP_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"plans\":{\"TestBackupPlan\":{\"regions\":{\"@@assign\": ....TRUNCATED FOR BREVITY.... "@@assign\":[\"Yes\"]}}}}}}}"
 }
}`
```

The following example adds or changes the description for a backup
policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --description "My new description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/backup_policy/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Description": "My new description",
 "Type": "BACKUP_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"plans\":{\"TestBackupPlan\":{\"regions\":{\"@@assign\": ....TRUNCATED FOR BREVITY.... "@@assign\":[\"Yes\"]}}}}}}}"
 }
}`
```

The following example changes the JSON policy document attached to
a backup policy. In this example, the content is taken from a file
called `policy.json` with the following
text:

```
{
    "plans": {
        "PII_Backup_Plan": {
            "regions": { "@@assign": [ "ap-northeast-2", "us-east-1", "eu-north-1" ] },
            "rules": {
                "Hourly": {
                    "schedule_expression": { "@@assign": "cron(0 5/1 ? * * *)" },
                    "start_backup_window_minutes": { "@@assign": "480" },
                    "complete_backup_window_minutes": { "@@assign": "10080" },
                    "lifecycle": {
                        "move_to_cold_storage_after_days": { "@@assign": "180" },
                        "delete_after_days": { "@@assign": "270" },
                        "opt_in_to_archive_for_supported_resources": {"@@assign": false}
                    },
                    "target_backup_vault_name": { "@@assign": "FortKnox" },
                    "copy_actions": {
                        "arn:aws:backup:us-east-1:$account:backup-vault:secondary-vault": {
                            "lifecycle": {
                                "move_to_cold_storage_after_days": { "@@assign": "10" },
                                "delete_after_days": { "@@assign": "100" },
                                "opt_in_to_archive_for_supported_resources": {"@@assign": false}
                            }
                        }
                    }
                }
            },
            "selections": {
                "tags": {
                    "datatype": {
                        "iam_role_arn": { "@@assign": "arn:aws:iam::$account:role/MyIamRole" },
                        "tag_key": { "@@assign": "dataType" },
                        "tag_value": { "@@assign": [ "PII" ] }
                    }
                }
            }
        }
    }
}
```

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --content file://policy.json**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/backup_policy/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Description": "My new description",
 "Type": "BACKUP_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"plans\":{\"TestBackupPlan\":{\"regions\":{\"@@assign\": ....TRUNCATED FOR BREVITY.... "@@assign\":[\"Yes\"]}}}}}}}"
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update a tag policy

###### Minimum permissions

To update a tag policy, you must have permission to run the following
actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")

AWS Management Console

###### To update a tag policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the \***\*[Tag policies](https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy "https://console.aws.amazon.com/organizations/v2/home/policies/tag-policy")** page\*\* page, choose the
   tag policy that you want to update.
3. Choose **Edit policy**.
4. You can enter a new **Policy name**,
   **Policy description**. You can change the
   policy content by using either the **Visual
   editor** or by editing the **JSON**.
5. When you're finished updating the tag policy, choose
   **Save changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a tag policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "Renamed tag policy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/tag_policy/p-i9j8k7l6m5",
 "Name": "Renamed tag policy",
 "Type": "TAG_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n\"tags\":{\n\"CostCenter\":{\n\"tag_key\":{\n\"@@assign\":\"CostCenter\"\n}\n}\n}\n}\n\n"
 }
}`
```

The following example adds or changes the description for a tag
policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --description "My new tag policy description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/tag_policy/p-i9j8k7l6m5",
 "Name": "Renamed tag policy",
 "Description": "My new tag policy description",
 "Type": "TAG_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n\"tags\":{\n\"CostCenter\":{\n\"tag_key\":{\n\"@@assign\":\"CostCenter\"\n}\n}\n}\n}\n\n"
 }
}`
```

The following example changes the JSON policy document attached to
an AI services opt-out policy. In this example, the content is taken
from a file called `policy.json` with the
following text:

```
{
  "tags": {
    "Stage": {
      "tag_key": {
        "@@assign": "Stage"
      },
      "tag_value": {
        "@@assign": [
          "Production",
          "Test"
        ]
      }
    }
  }
}
```

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --content file://policy.json**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/tag_policy/p-i9j8k7l6m5",
 "Name": "Renamed tag policy",
 "Description": "My new tag policy description",
 "Type": "TAG_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"tags\":{\"Stage\":{\"tag_key\":{\"@@assign\":\"Stage\"},\"tag_value\":{\"@@assign\":[\"Production\",\"Test\"]},\"enforced_for\":{\"@@assign\":[\"ec2:instance\"]}}}}"
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update a chat applications

policy

###### Minimum permissions

To update a chat applications policy, you must have permission to run the
following actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")

AWS Management Console

###### To update a chat applications policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the \***\*[Chatbot policies](https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy "https://console.aws.amazon.com/organizations/v2/home/policies/chatbot-policy")** page\*\* page, choose
   the chat applications policy that you want to update.
3. Choose **Edit policy**.
4. You can enter a new **Policy name**,
   **Policy description**. You can change the
   policy content by using either the **Visual
   editor** or by editing the **JSON**.
5. When you're finished updating the tag policy, choose
   **Save changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a chat applications policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "Renamed chat applications policy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/chatbot_policy/p-i9j8k7l6m5",
 "Name": "Renamed chat applications policy",
 "Type": "CHATBOT_POLICY",
 "AwsManaged": false
 },
 "Content": "{"chatbot":{"platforms":{"slack":{"client":{"@@assign":"enabled"},"workspaces":{"@@assign":["`Slack-Workspace-Id`"]},"default":{"supported_channel_types":{"@@assign":["private"]}}},"microsoft_teams":{"client":{"@@assign":"disabled"}}}}}"
 }
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update an AI services opt-out

policy

###### Minimum permissions

To update an AI services opt-out policy, you must have permission to run the following
actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the Amazon Resource Name
  (ARN) of the specified policy (or "\*")

AWS Management Console

###### To update an AI services opt-out policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AI services opt-out policies](https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy "https://console.aws.amazon.com/organizations/v2/home/policies/aiservices-opt-out-policy")** page, choose the name of the policy
   that you want to update.
3. On the policy's detail page, choose **Edit
   policy**.
4. You can enter a new **Policy name**,
   **Policy description**, or edit the
   **JSON** policy text. For information about
   AI services opt-out policy syntax, see [AI services opt-out policy syntax and
   examples](orgs_manage_policies_ai-opt-out_syntax.md "orgs_manage_policies_ai-opt-out_syntax.md"). For example
   policies that you can use as a starting point, see [AI services opt-out policy examples](orgs_manage_policies_ai-opt-out_syntax.md#ai-opt-out-policy-examples "orgs_manage_policies_ai-opt-out_syntax.md#ai-opt-out-policy-examples").
5. When you're finished updating the policy, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames an AI services opt-out
policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --name "Renamed policy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/aiservices_opt_out_policy/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Type": "AISERVICES_OPT_OUT_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"services\":{\"default\":{\"opt_out_policy\": ....TRUNCATED FOR BREVITY... :{\"@@assign\":\"optIn\"}}}}"
 }
}`
```

The following example adds or changes the description for an AI
services opt-out policy.

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --description "My new description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/aiservices_opt_out_policy/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Description": "My new description",
 "Type": "AISERVICES_OPT_OUT_POLICY",
 "AwsManaged": false
 },
 "Content": "{\"services\":{\"default\":{\"opt_out_policy\": ....TRUNCATED FOR BREVITY... :{\"@@assign\":\"optIn\"}}}}"
 }
}`
```

The following example changes the JSON policy document attached to
an AI services opt-out policy. In this example, the content is taken
from a file called `policy.json` with the
following text:

```
{
    "services": {
        "default": {
            "opt_out_policy": {
                "@@assign": "optOut"
            }
        },
        "comprehend": {
            "opt_out_policy": {
                "@@operators_allowed_for_child_policies": ["@@none"],
                "@@assign": "optOut"
            }
        },
        "rekognition": {
            "opt_out_policy": {
                "@@assign": "optIn"
            }
        }
    }
}
```

```
`$` **aws organizations update-policy \
 --policy-id p-i9j8k7l6m5 \
 --content file://policy.json**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-i9j8k7l6m5",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/aiservices_opt_out_policy/p-i9j8k7l6m5",
 "Name": "Renamed policy",
 "Description": "My new description",
 "Type": "AISERVICES_OPT_OUT_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n\"services\": {\n\"default\": {\n\" ....TRUNCATED FOR BREVITY.... ": \"optIn\"\n}\n}\n}\n}\n"}
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

## Update a Security Hub policy

###### Minimum permissions

To update a Security Hub policy, you must have permission to run the following
actions:

- `organizations:UpdatePolicy` with a `Resource`
  element in the same policy statement that includes the ARN of the specified
  policy (or "\*")
- `organizations:DescribePolicy` with a `Resource`
  element in the same policy statement that includes the Amazon Resource Name
  (ARN) of the specified policy (or "\*")

AWS Management Console

###### To update a Security Hub policy

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Security Hub policies](https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy "https://console.aws.amazon.com/organizations/v2/home/policies/securityhub-policy")** page, choose the name of the policy
   that you want to update.
3. On the policy's detail page, choose **Edit
   policy**.
4. You can enter a new **Policy name**,
   **Policy description**, or edit the
   **JSON** policy text. For information about
   Security Hub policy syntax, see [Security Hub policy syntax and
   examples](orgs_manage_policies_security_hub_syntax.md "orgs_manage_policies_security_hub_syntax.md"). For
   example policies that you can use as a starting point, see [Security Hub policy examples](orgs_manage_policies_security_hub_syntax.md#security-hub-policy-examples "orgs_manage_policies_security_hub_syntax.md#security-hub-policy-examples").
5. When you're finished updating the policy, choose **Save
   changes**.

AWS CLI & AWS SDKs

###### To update a policy

You can use one of the following to update a policy:

- AWS CLI: [update-policy](../../../cli/latest/reference/organizations/update-policy.md "../../../cli/latest/reference/organizations/update-policy.md")

The following example renames a Security Hub policy.

```
`$` **aws organizations update-policy \
 --policy-id p-66ev7hgcvj \
 --name "Renamed policy"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-66ev7hgcvj",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/securityhub_policy/p-66ev7hgcvj",
 "Name": "Renamed policy",
 "Type": "SECURITYHUB_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n \"securityhub\": {\n \"enable_in_regions\": {\n \"@@assign\":[\n \"ALL_SUPPORTED\"\n ]\n },\n \"disable_in_regions\": {\n \"@@assign\":[]\n }\n }\n}\n"
 }
}`
```

The following example adds or changes the description for a Security Hub
policy.

```
`$` **aws organizations update-policy \
 --policy-id p-66ev7hgcvj \
 --name "My new description"**`{
 "Policy": {
 "PolicySummary": {
 "Id": "p-66ev7hgcvj",
 "Arn": "arn:aws:organizations::123456789012:policy/o-aa111bb222/securityhub_policy/p-66ev7hgcvj",
 "Name": "My new description",
 "Type": "SECURITYHUB_POLICY",
 "AwsManaged": false
 },
 "Content": "{\n \"securityhub\": {\n \"enable_in_regions\": {\n \"@@assign\":[\n \"ALL_SUPPORTED\"\n ]\n },\n \"disable_in_regions\": {\n \"@@assign\":[]\n }\n }\n}\n"
 }
}`
```

- AWS SDKs: [UpdatePolicy](../APIReference/API_UpdatePolicy.md "../APIReference/API_UpdatePolicy.md")

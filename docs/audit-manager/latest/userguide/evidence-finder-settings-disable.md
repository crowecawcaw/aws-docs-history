# Disabling evidence finder

If you no longer want to use evidence finder, you can disable the feature at any
time.

Follow these steps to learn how to disable evidence finder. Pay close attention to the
prerequisites, as you'll need specific permissions to delete the event data store in
CloudTrail Lake that was created when you enabled evidence finder.

## Prerequisites

### Required permissions to

disable evidence finder

To disable evidence finder, you need permissions to delete an event data store
in CloudTrail Lake. For an example policy that you can use, see [Permissions to disable evidence finder](security_iam_id-based-policy-examples.md#full-administrator-access-disable-evidence-finder "security_iam_id-based-policy-examples.md#full-administrator-access-disable-evidence-finder").

If you need help with permissions, contact your AWS administrator. If you’re
an AWS administrator, you can [attach the required permission statement to an IAM policy](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#add-policies-console").

## Procedure

You can complete this task using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the
Audit Manager API.

###### Warning

Disabling evidence finder deletes the CloudTrail Lake event data store that Audit Manager
created. As a result, you can’t re-enable the feature. To re-use evidence finder
after you disable it, you must [disable
AWS Audit Manager](general-settings.md#disable "general-settings.md#disable"), and then [re-enable](setup-audit-manager.md "setup-audit-manager.md") the service completely.

Audit Manager console

###### To disable evidence finder on the Audit Manager console

1. In the **Evidence finder**
   section of the Audit Manager settings page, choose
   **Disable**.
2. In the pop-up window that appears, enter
   `Yes` to confirm your decision.
3. Choose **Request to disable**.

AWS CLI

###### To disable evidence finder in the AWS CLI

Run the [update-settings](../../../cli/latest/reference/auditmanager/update-settings.md "../../../cli/latest/reference/auditmanager/update-settings.md") command with the
`--no-evidence-finder-enabled` parameter.

```
aws auditmanager update-settings --no-evidence-finder-enabled
```

Audit Manager API

###### To disable evidence finder using the API

Call the [UpdateSettings](../APIReference/API_UpdateSettings.md "../APIReference/API_UpdateSettings.md") operation and use the [evidenceFinderEnabled](../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-evidenceFinderEnabled "../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-evidenceFinderEnabled") parameter.

For more information, choose the previous links to read more in the
_Audit Manager API Reference_. This includes
information about how to use this operation and parameter in one of the
language-specific AWS SDKs.

## Additional

resources

- [Troubleshooting evidence finder issues](evidence-finder-issues.md "evidence-finder-issues.md")

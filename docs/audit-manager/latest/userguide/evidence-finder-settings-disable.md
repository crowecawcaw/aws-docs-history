

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Disabling evidence finder
<a name="evidence-finder-settings-disable"></a>



If you no longer want to use evidence finder, you can disable the feature at any time.

Follow these steps to learn how to disable evidence finder. Pay close attention to the prerequisites, as you'll need specific permissions to delete the event data store in CloudTrail Lake that was created when you enabled evidence finder. 

## Prerequisites
<a name="evidence-finder-settings-disable-prerequisites"></a>

### Required permissions to disable evidence finder
<a name="evidence-finder-disable-permissions"></a>

To disable evidence finder, you need permissions to delete an event data store in CloudTrail Lake. For an example policy that you can use, see [Permissions to disable evidence finder](https://docs.aws.amazon.com/audit-manager/latest/userguide/security_iam_id-based-policy-examples.html#full-administrator-access-disable-evidence-finder). 

If you need help with permissions, contact your AWS administrator. If you're an AWS administrator, you can [attach the required permission statement to an IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console).

## Procedure
<a name="evidence-finder-settings-disable-procedure"></a>

You can complete this task using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API.

**Warning**  
Disabling evidence finder deletes the CloudTrail Lake event data store that Audit Manager created. As a result, you can't re-enable the feature. To re-use evidence finder after you disable it, you must [disable AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/general-settings.html#disable), and then [re-enable](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html) the service completely. 

------
#### [ Audit Manager console ]

**To disable evidence finder on the Audit Manager console**

1. In the **Evidence finder** section of the Audit Manager settings page, choose **Disable**.

1. In the pop-up window that appears, enter **Yes** to confirm your decision. 

1. Choose **Request to disable**.

------
#### [ AWS CLI ]

**To disable evidence finder in the AWS CLI**  
Run the [update-settings](https://docs.aws.amazon.com/cli/latest/reference/auditmanager/update-settings.html) command with the `--no-evidence-finder-enabled` parameter.

```
aws auditmanager update-settings --no-evidence-finder-enabled 
```

------
#### [ Audit Manager API ]

**To disable evidence finder using the API**  
Call the [UpdateSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html) operation and use the [evidenceFinderEnabled](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html#auditmanager-UpdateSettings-request-evidenceFinderEnabled) parameter.

For more information, choose the previous links to read more in the *Audit Manager API Reference*. This includes information about how to use this operation and parameter in one of the language-specific AWS SDKs.

------

## Additional resources
<a name="disable-evidence-finder-additional-resources"></a>
+ [Troubleshooting evidence finder issues](evidence-finder-issues.md)
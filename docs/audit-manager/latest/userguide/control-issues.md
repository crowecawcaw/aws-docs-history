

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Troubleshooting control and control set issues
<a name="control-issues"></a>



You can use the information on this page to resolve common issues with controls in Audit Manager.

**General issues**
+ [I can’t see any controls or control sets in my assessment](#cannot-view-controls)
+ [I can’t upload manual evidence to a control](#cannot-upload-manual-evidence)
+ [What does it mean if a control says “Replacement available”?](#control-replacement-available)

**AWS Config integration issues**
+ [I need to use multiple AWS Config rules as a data source for a single control](#need-to-use-multiple-rules)
+ [The custom rule option is unavailable when I’m configuring a control data source](#custom-rule-option-unavailable)
+ [The custom rule option is available, but no rules appear in the dropdown list](#no-custom-rules-displayed)
+ [Some custom rules are available, but I can’t see the rule that I want to use](#custom-rule-missing)
+ [I can’t see the managed rule that I want to use](#managed-rule-missing)
+ [I want to share a custom framework, but it has controls that use custom AWS Config rules as a data source. Can the recipient collect evidence for these controls?](#shared-frameworks-with-custom-aws-config-rules)
+ [What happens when a custom rule is updated in AWS Config? Do I need to take any action in Audit Manager?](#a-rule-is-updated)

## I can’t see any controls or control sets in my assessment
<a name="cannot-view-controls"></a>

In short, to view the controls for an assessment, you must be specified as an audit owner for that assessment. Moreover, you need the necessary IAM permissions to view and manage the related Audit Manager resources. 

If you need access to the controls in an assessment, ask one of the audit owners for that assessment to specify you as audit owner. You can specify audit owners when you're [creating](https://docs.aws.amazon.com/audit-manager/latest/userguide/create-assessments.html#choose-audit-owners) or [editing](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-assessment.html#edit-choose-audit-owners) an assessment. 

Make sure also that you have the necessary permissions to manage the assessment. We recommend that audit owners use the [AWSAuditManagerAdministratorAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.html) policy. If you need help with IAM permissions, contact your administrator or [AWS Support](https://aws.amazon.com/contact-us/). For more information about how to attach a policy to an IAM identity, see [Adding Permissions to a User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) and [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) in the *IAM User Guide*.

## I can’t upload manual evidence to a control
<a name="cannot-upload-manual-evidence"></a>

If you can't manually upload evidence to a control, it's likely because the control is in *inactive* status.

To upload manual evidence to a control, you must first change the control status to either *Under review* or *Reviewed*. For instructions, see [Changing the status of an assessment control in AWS Audit Manager](change-assessment-control-status.md).

**Important**  
Each AWS account can only manually upload up to 100 evidence files to a control each day. Exceeding this daily quota causes any additional manual uploads to fail for that control. If you need to upload a large amount of manual evidence to a single control, upload your evidence in batches across several days.

## What does it mean if a control says “Replacement available”?
<a name="control-replacement-available"></a>

![Screenshot of the pop-up message that prompts you to recreate your assessment.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/troubleshooting-control-replacement-available-console.png)


If you see this message, this means that an updated control definition is available for one or more of the standard controls in your custom framework. We recommend that you replace these controls so that you can benefit from the improved evidence sources that Audit Manager now provides.

For instructions on how to proceed, see [On my custom framework details page, I’m prompted to recreate my custom framework](framework-issues.md#recreate-framework-post-common-controls).

## I need to use multiple AWS Config rules as a data source for a single control
<a name="need-to-use-multiple-rules"></a>

You can use a combination of managed rules and custom rules for a single control. To do this, define multiple evidence sources for the control, and select your preferred rule type for each one. You can define up to 100 customer managed data sources for a single custom control.

## The custom rule option is unavailable when I’m configuring a control data source
<a name="custom-rule-option-unavailable"></a>

This means that you don't have permissions to view custom rules for your AWS account or organization. More specifically, you don't have permissions to perform the [DescribeConfigRules](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeConfigRules.html) operation in the Audit Manager console.

To resolve this issue, contact your AWS administrator for help. If you're an AWS administrator, you can provide permissions for your users or groups by [managing your IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html).

## The custom rule option is available, but no rules appear in the dropdown list
<a name="no-custom-rules-displayed"></a>

This means that no custom rules are enabled and available for use in your AWS account or organization.

If you don’t have any custom rules yet in AWS Config, you can create one. For instructions, see [AWS Config custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) in the *AWS Config Developer Guide*.

If you're expecting to see a custom rule, check the following troubleshooting item.

## Some custom rules are available, but I can’t see the rule that I want to use
<a name="custom-rule-missing"></a>

If you can’t see the custom rule that you’re expecting to find, this could be due to one of the following issues.

**Your account is excluded from the rule**  
It's possible that the delegated administrator account that you're using is excluded from the rule.  
Your organization's management account (or one of the AWS Config delegated administrator accounts) can create custom organization rules using the AWS Command Line Interface (AWS CLI). When they do so, they can specify a [list of accounts to be excluded](https://docs.aws.amazon.com/config/latest/APIReference/API_PutOrganizationConfigRule.html#config-PutOrganizationConfigRule-request-ExcludedAccounts) from the rule. If your account is on this list, the rule isn’t available in Audit Manager.  
To resolve this issue, contact your AWS Config administrator for help. If you're an AWS Config administrator, you can update the list of excluded accounts by running the [put-organization-config-rule](https://docs.aws.amazon.com/cli/latest/reference/configservice/put-organization-config-rule.html) command.

**The rule wasn’t successfully created and enabled in AWS Config**  
It’s also possible that the custom rule wasn't created and enabled successfully. If an [error occurred when creating the rule](https://docs.aws.amazon.com/config/latest/APIReference/API_PutConfigRule.html#API_PutConfigRule_Errors), or [the rule isn't enabled](https://docs.aws.amazon.com/config/latest/developerguide/setting-up-aws-config-rules-with-console.html), it doesn’t appear in the list of available rules in Audit Manager.  
For assistance with this issue, we recommend that you contact your AWS Config administrator.

**The rule is a managed rule**  
If you can't find the rule that you're looking for under the dropdown list of custom rules, it’s possible that the rule is a managed rule.  
You can use the [AWS Config console](https://console.aws.amazon.com/config/) to verify if a rule is a managed rule. To do so, choose **Rules** in the left navigation menu and look for the rule in the table. If the rule is a managed rule, the **Type** column shows **AWS managed**.  

![A managed rule as shown in the AWS Config console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/rules-managed-console.png)

After you've confirmed that it's a managed rule, return to Audit Manager and select **Managed rule** as the rule type. Then, look for the managed rule identifier keyword in the dropdown list of managed rules.  

![The same rule that's found in the managed rule dropdown list in the Audit Manager console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/control_data_source-managed_rule-console.png)


## I can’t see the managed rule that I want to use
<a name="managed-rule-missing"></a>

Before you select a rule from the dropdown list in the Audit Manager console, make sure that you selected **Managed rule** as the rule type.

![The managed rule option selected in the Audit Manager console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/ruletype-managed-console.png)


If you still can’t see the managed rule that you’re expecting to find, it’s possible that you’re looking for the rule *name*. Instead, you must look for the rule *identifier*. 

If you're using a default managed rule, the name and the identifier are similar. The name is in lowercase and uses dashes (for example, `iam-policy-in-use`). The identifier is in uppercase and uses underscores (for example, `IAM_POLICY_IN_USE`). To find the identifier for a default managed rule, review the [list of supported AWS Config managed rule keywords](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-managed-rules) and follow the link for the rule that you want to use. This takes you to the AWS Config documentation for that managed rule. From here, you can see both the name and the identifier. Look for the identifier keyword in the Audit Manager dropdown list.

![A managed rule name and identifier as shown in the AWS Config documentation.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/ruleidentifier-configdocs.png)


If you're using a custom managed rule, you can use the [AWS Config console](https://console.aws.amazon.com/config/) to find the rule identifier. For example, let's say that you want to use the managed rule called `customized-iam-policy-in-use`. To find the identifier for this rule, go to the AWS Config console, choose **Rules** in the left navigation menu, and choose the rule in the table.

![A managed rule with a customized name in the rules table of the AWS Config console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/managedrule-customname-configconsole.png)


Choose **Edit** to open details about the managed rule.

![The edit rule option in the AWS Config console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/editrule-configconsole.png)


Under the **Details** section, you can find the source identifier that the managed rule was created from (`IAM_POLICY_IN_USE`).

![The managed rule details in the AWS Config console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/ruledetails-configconsole.png)


You can now return to the Audit Manager console and select the same identifier keyword from the dropdown list.

![A managed rule identifier as shown in the Audit Manager console.](http://docs.aws.amazon.com/audit-manager/latest/userguide/images/ruleidentifier-console.png)


## I want to share a custom framework, but it has controls that use custom AWS Config rules as a data source. Can the recipient collect evidence for these controls?
<a name="shared-frameworks-with-custom-aws-config-rules"></a>

Yes, the recipient can collect evidence for these controls, but a few steps are needed to achieve this. 

For Audit Manager to collect evidence using an AWS Config rule as a data source mapping, the following must be true. This applies to both managed rules and custom rules.

1. The rule must exist in the recipient’s AWS environment

1. The rule must be enabled in the recipient’s AWS environment

Remember that the custom AWS Config rules in your account likely don’t exist already in the recipient’s AWS environment. Moreover, when the recipient accepts the share request, Audit Manager doesn’t recreate any of your custom rules in their account. For the recipient to collect evidence using your custom rules as a data source mapping, they must create the same custom rules in their instance of AWS Config. After the recipient [creates](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) and then [enables](https://docs.aws.amazon.com/config/latest/developerguide/setting-up-aws-config-rules-with-console.html) the rules, Audit Manager can collect evidence from that data source. 

We recommend that you communicate with the recipient to let them know if any custom rules need to be created in their instance of AWS Config.

## What happens when a custom rule is updated in AWS Config? Do I need to take any action in Audit Manager?
<a name="a-rule-is-updated"></a>

**For rule updates within your AWS environment**  
If you update a custom rule within your AWS environment, no action is needed in Audit Manager. Audit Manager detects and handles the rule updates as described in the following table. Audit Manager doesn't notify you when a rule update is detected.


| Scenario | What Audit Manager does | What you need to do | 
| --- | --- | --- | 
| A custom rule is **updated** in your instance of AWS Config | Audit Manager continues to report findings for that rule using the updated rule definition.  | No action is needed. | 
| A custom rule is **deleted** in your instance of AWS Config | Audit Manager stops reporting findings for the deleted rule. | No action is needed.<br />If you want to, you can [edit the custom controls](https://docs.aws.amazon.com/audit-manager/latest/userguide/edit-controls.html) that used the deleted rule as a data source mapping. Doing so helps to clean up your data source settings by removing the deleted rule. Otherwise, the deleted rule name remains as an unused data source mapping. | 

**For rule updates outside your AWS environment**  
If a custom rule is updated outside of your AWS environment, Audit Manager doesn’t detect the rule update. This is something to consider if you use shared custom frameworks. This is because, in this scenario, the sender and the recipient each work in separate AWS environments. The following table provides recommended actions for this scenario.


| Your role | Scenario | Recommended action | 
| --- | --- | --- | 
| Sender |  +  You shared a framework that uses custom rules as a data source mapping. <br />+  After you shared the framework, you updated or deleted one of those rules in AWS Config.   | Let the recipient know about your update. That way, they can apply the same update and stay in sync with the latest rule definition. | 
| Recipient |  +  You accepted a shared framework that uses custom rules as a data source mapping. <br />+  After you recreated the custom rules in your instance of AWS Config, the sender updated or deleted one of those rules.   | Make the corresponding rule update in your own instance of AWS Config. | 
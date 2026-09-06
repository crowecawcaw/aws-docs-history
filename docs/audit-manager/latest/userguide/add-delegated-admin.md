

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Adding a delegated administrator
<a name="add-delegated-admin"></a>



If you use AWS Organizations and want to enable multi-account support for AWS Audit Manager, you can designate a member account in your organization as the delegated administrator for Audit Manager. 

If you want to use Audit Manager in more than one AWS Region, you must designate a delegated administrator account separately in each Region. In your Audit Manager settings, you should use the same delegated administrator account across all Regions. 

## Prerequisites
<a name="add-delegated-admin-prerequisites"></a>

Take note of the following factors that define how the delegated administrator operates in Audit Manager:
+ Your account must be part of an organization.
+ Before you designate a delegated administrator, you must [enable all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html). You must also [configure your organization's Security Hub CSPM settings](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-recommendations.html#securityhub-recommendations). This way, Audit Manager can collect Security Hub CSPM evidence from your member accounts.
+ The delegated administrator account must have access on the KMS key that you provided when setting up Audit Manager. 
+ You can't use your AWS Organizations management account as a delegated administrator in Audit Manager.

## Procedure
<a name="add-delegated-admin-procedure"></a>

You can add a delegated administrator using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API.

**Note**  
After you add a delegated administrator in your Audit Manager settings, your management account can no longer create additional assessments in Audit Manager. Additionally, evidence collection stops for any existing assessments created by the management account. Audit Manager collects and attaches evidence to the delegated administrator account, which is the main account for managing your organization's assessments.

------
#### [ Audit Manager console ]

**To add a delegated administrator on the Audit Manager console**

1. From the **General** settings tab, go to the **Delegated administrator** section.

1. Under **Delegated administrator account ID**, enter the account ID of the delegated administrator.

1. Choose **Delegate**.

------
#### [ AWS CLI ]

**To add a delegated administrator in the AWS CLI**  
Run the [register-organization-admin-account](https://docs.aws.amazon.com/cli/latest/reference/auditmanager/register-organization-admin-account.html) command and use the `--admin-account-id` parameter to specify the account ID of the delegated administrator.

In the following example, replace the {{placeholder text}} with your own information.

```
aws auditmanager register-organization-admin-account --admin-account-id {{111122223333}}
```

------
#### [ Audit Manager API ]

**To add a delegated administrator using the API**  
Call the [RegisterOrganizationAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterOrganizationAdminAccount.html) operation and use the [adminAccountId](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterOrganizationAdminAccount.html#auditmanager-RegisterOrganizationAdminAccount-request-adminAccountId) parameter to specify the account ID of the delegated administrator.

For more information, choose the previous links to read more in the *Audit Manager API Reference*. This includes information about how to use this operation and parameter in one of the language-specific AWS SDKs.

------

## Next steps
<a name="add-delegated-admin-next-steps"></a>

To change your delegated administrator account, see [Changing a delegated administrator](change-delegated-admin.md).

To remove your delegated administrator account, see [Removing a delegated administrator](remove-delegated-admin.md).

## Additional resources
<a name="add-delegated-admin-additional-resources"></a>
+ [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html)
+ [Troubleshooting delegated administrator and AWS Organizations issues](delegated-admin-issues.md)
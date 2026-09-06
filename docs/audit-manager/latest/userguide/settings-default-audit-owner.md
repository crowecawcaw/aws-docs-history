

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Configuring your default audit owners
<a name="settings-default-audit-owner"></a>



You can use this setting to specify the default [](concepts.md#audit-owner)s who have primary access to your assessments in Audit Manager. 

## Procedure
<a name="settings-default-audit-owner-procedure"></a>

You can update this setting using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager API.

------
#### [ Audit Manager console ]

You can choose from the AWS accounts listed in the table, or use the search bar to look for other AWS accounts.

**To update your default audit owners on the Audit Manager console**

1. From the **Assessment** settings tab, go to the **Default audit owners** section and choose **Edit**.

1. To add a default audit owner, select the check box next to the account name under **Audit owner**.

1. To remove a default audit owner, clear the check box next to the account name under **Audit owner**.

1. When you're done, choose **Save**.

------
#### [ AWS CLI ]

**To update your default audit owner in the AWS CLI**  
Run the [update-settings](https://docs.aws.amazon.com/cli/latest/reference/auditmanager/update-settings.html) command and use the `--default-process-owners` parameter to specify an audit owner. 

In the following example, replace the {{placeholder text}} with your own information. Note that `roleType` can only be `PROCESS_OWNER`.

```
aws auditmanager update-settings --default-process-owners roleType=PROCESS_OWNER,roleArn={{arn:aws:iam::111122223333:role/Administrator}} 
```

------
#### [ Audit Manager API ]

**To update your default audit owner using the API**  
Call the [UpdateSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html) operation and use the [defaultProcessOwners](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html#auditmanager-UpdateSettings-request-defaultProcessOwners) parameter to specify default audit owners. Note that `roleType` can only be `PROCESS_OWNER`.

------

## Additional resources
<a name="settings-default-audit-owner-additional-resources"></a>
+ For more information about audit owners, see [Audit owners](https://docs.aws.amazon.com/audit-manager/latest/userguide/concepts.html#audit-owner) in the *Concepts and terminology* section of this guide.
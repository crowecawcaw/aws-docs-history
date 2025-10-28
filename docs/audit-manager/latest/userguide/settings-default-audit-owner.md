# Configuring your default audit

owners

You can use this setting to specify the default [audit owner](concepts.md#audit-owner "concepts.md#audit-owner")s who have primary access to your assessments in Audit Manager.

## Procedure

You can update this setting using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the
Audit Manager API.

Audit Manager console
You can choose from the AWS accounts listed in the table, or use the
search bar to look for other AWS accounts.

###### To update your default audit owners on the Audit Manager console

1. From the **Assessment** settings tab, go to
   the **Default audit owners** section and choose
   **Edit**.
2. To add a default audit owner, select the check box next to the
   account name under **Audit owner**.
3. To remove a default audit owner, clear the check box next to
   the account name under **Audit owner**.
4. When you’re done, choose **Save**.

AWS CLI

###### To update your default audit owner in the AWS CLI

Run the [update-settings](../../../cli/latest/reference/auditmanager/update-settings.md "../../../cli/latest/reference/auditmanager/update-settings.md") command and use the
`--default-process-owners` parameter to specify an
audit owner.

In the following example, replace the `placeholder
 text` with your own information. Note that
`roleType` can only be `PROCESS_OWNER`.

```
aws auditmanager update-settings --default-process-owners roleType=PROCESS_OWNER,roleArn=`arn:aws:iam::111122223333:role/Administrator`
```

Audit Manager API

###### To update your default audit owner using the API

Call the [UpdateSettings](../APIReference/API_UpdateSettings.md "../APIReference/API_UpdateSettings.md") operation and use the [defaultProcessOwners](../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-defaultProcessOwners "../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-defaultProcessOwners") parameter to specify default audit
owners. Note that `roleType` can only be
`PROCESS_OWNER`.

## Additional

resources

- For more information about audit owners, see [Audit
  owners](concepts.md#audit-owner "concepts.md#audit-owner") in the _Concepts and
  terminology_ section of this guide.

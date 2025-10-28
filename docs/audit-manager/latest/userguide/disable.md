# Disabling AWS Audit Manager

You can disable Audit Manager if you no longer want to use the service. When you disable Audit Manager,
you also have the option to delete all of your data.

By default, your data isn’t deleted when you disable Audit Manager. Your evidence data is
retained for two years from the time of its creation. Your other Audit Manager resources
(including assessments, custom controls, and custom frameworks) are retained
indefinitely, and will be available if you re-enable Audit Manager in the future. For more
information about data retention, see [Data Protection](data-protection.md "data-protection.md") in
this guide.

If you choose to delete your data, Audit Manager deletes all evidence data along with all of
the Audit Manager resources that you created (including assessments, custom controls, and custom
frameworks). All of your data is deleted within seven days of disabling Audit Manager.

###### Topics

- [Procedure](#disable-procedure "#disable-procedure")
- [Next steps](#disable-next-steps "#disable-next-steps")
- [Additional resources](#disable-additional-resources "#disable-additional-resources")

## Procedure

You can disable Audit Manager using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the Audit Manager
API.

###### Warning

- When you disable Audit Manager, your access is revoked and the service no longer
  collects evidence for any existing assessments. You can't access anything in
  the service unless you re-enable Audit Manager.
- Deleting all data is a permanent action. If you decide to re-enable Audit Manager
  in the future, your data won’t be recoverable.

Audit Manager console

###### To disable Audit Manager on the Audit Manager console

1. From the **General** settings tab, go to the
   **Disable AWS Audit Manager** section.
2. Choose **Disable**.
3. In the pop-up window, review your current data retention
   setting.
   1. To proceed with your current selection, choose
      **Disable Audit Manager**.
   2. To change your current selection, perform the
      following steps:
      1. Choose **Cancel** to return
         to the settings page.
      2. To use the default data retention setting,
         turn off **Delete all data**.
         This selection retains evidence data for two years
         from the time of its creation, and retains other
         Audit Manager resources indefinitely.
      3. To delete your data, turn on **Delete
         all data**.
      4. Choose **Disable**, and then
         choose **Disable Audit Manager** to
         confirm your choice.

AWS CLI

###### Before you start

Before you disable Audit Manager, you can run the [update-settings](../../../cli/latest/reference/auditmanager/update-settings.md "../../../cli/latest/reference/auditmanager/update-settings.md") command to set your preferred data
retention policy. By default, Audit Manager retains your data. If you want to
request the deletion of your data, use the
`--deregistration-policy` parameter with the
`deleteResources` value set to
`ALL`.

```
aws auditmanager update-settings --deregistration-policy deleteResources=ALL
```

###### To disable Audit Manager in the AWS CLI

When you're ready to disable Audit Manager, run the [deregister-account](../../../cli/latest/reference/auditmanager/deregister-account.md "../../../cli/latest/reference/auditmanager/deregister-account.md") command.

```
aws auditmanager deregister-account
```

Audit Manager API

###### Before you start

Before you disable Audit Manager, you can use the [UpdateSettings](../APIReference/API_UpdateSettings.md "../APIReference/API_UpdateSettings.md") API operation to set
your preferred data retention policy. By default, Audit Manager retains your
data. If you want to delete your data, you can use the [DeregistrationPolicy](../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-deregistrationPolicy "../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-deregistrationPolicy") attribute to request the deletion
of your data.

###### To disable Audit Manager using the API

When you're ready to disable Audit Manager, call the [DeregisterAccount](../APIReference/API_DeregisterAccount.md "../APIReference/API_DeregisterAccount.md") operation.

For more information, choose the previous links to read more in the
_Audit Manager API Reference_. This includes
information about how to use these operations and parameters in one of
the language-specific AWS SDKs.

## Next steps

If you need to re-enable Audit Manager after you disable it, follow these steps to get the
service up and running again.

###### To re-enable Audit Manager after you disable it

Go to the Audit Manager service homepage and follow the steps to set up Audit Manager as a new
user. For more information, see [Setting up AWS Audit Manager with the recommended settings](setting-up.md "setting-up.md").

###### Tip

- If you chose to delete your data when you disabled Audit Manager, you must wait
  until your data is deleted before you can re-enable the service.
  Depending on how much data you have, this can take up to seven days.
  However, feel free to try re-enabling Audit Manager before then. In many cases,
  data is deleted in as little as one hour.
- If you chose not to delete your data when you disabled Audit Manager, your
  existing assessments moved into a dormant state and stopped collecting
  evidence as a result. To start collecting evidence again for a
  pre-existing assessment, [edit the
  assessment](edit-assessment.md "edit-assessment.md") and choose **Save**
  without making any changes.

## Additional resources

- For more information about data retention in Audit Manager, see [Data
  Protection](data-protection.md "data-protection.md") in this guide.

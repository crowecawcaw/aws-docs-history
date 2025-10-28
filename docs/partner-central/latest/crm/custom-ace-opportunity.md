# Sandbox testing with the custom ACE opportunity and

ACE lead objects

###### Note

If you are an existing CRM connector user, refer to [Upgrading AWS Partner CRM connector to the new data
model](connector-upgrade-plan.md "connector-upgrade-plan.md").

1. Sign in to your Salesforce organization as a system administrator.
2. Choose **Setup**, **Custom settings**,
   **AWS Partner CRM connector settings**, and update version to
   **2**.
3. Choose the **ACE Mapping** tab.
4. For **Opportunity**, map it to the **ACE
   opportunity** custom object.
5. Choose **Auto Map ACE object**.

###### Note

If you want to upgrade to the new version of the CRM connector that want to use the
custom ACE opportunity and ACE lead objects from the connector for sandbox testing, we
recommend manually deleting any available records from the `Field Mappings`
and `Field Mapping Details` objects from the database before using the Auto
Map ACE object feature. You only need to do this once. 6. Review field mappings and field mapping values for picklist and multipicklist. 7. Activate schedules for opportunities and leads. 8. Review the ACE Sync Logs for synchronization errors and make any required
corrections. 9. Review the synced opportunities and leads to ensure the data transformation is
accurate. Alternatively, review the opportunities and leads in ACE to ensure that the new
data model changes have been accurately captured.

## Viewing sync log detail records for ACE

opportunities

You can view sync log details for AWS-delivered ACE opportunities on the
**Related** tab on the ACE opportunity record.

###### Note

These steps only apply to AWS-delivered ACE opportunity objects. If you map to
standard or custom objects in your Salesforce organization, you can view sync log details
on the **ACE Sync Log** tab.

1. Sign in to your Salesforce organization.
2. In the **App Launcher**, choose **AWS Partner CRM
   connector**.
3. Choose the **ACE Opportunities** tab.
4. Choose an ACE opportunity record.
5. Choose the **Related** tab to view details including **Sync
   Log Name**, **Status**, **Error Message**,
   and **Created Date**.

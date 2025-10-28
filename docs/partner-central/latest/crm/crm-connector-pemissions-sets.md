# AWS Partner Network permission sets

The CRM connector supports the following primary AWS Partner Network personas:

###### Topics

- [Business administrator (APN Business Administrator)](#business-administrator "#business-administrator")
- [Integration User (APN Integration User)](#integration-user "#integration-user")
- [Business user (APN Business User)](#business-user "#business-user")
- [Granting permissions to view reports](#report-permissions "#report-permissions")
- [Activating flow users](#activate-flow-user "#activate-flow-user")

## Business administrator (APN Business Administrator)

- Assign to a system admin or a business admin to configure the setup and
  mapping of records.
- Gives full access to the Salesforce AWS Partner Network CRM administration app.
- Can create, view, and edit field mappings.
- Can view all sync log detail records.
- Doesn’t allow the user to schedule an integration, only to set up
  configurations.
- Doesn’t provide core Salesforce setup access.
- Some settings in Salesforce require additional access. Specifically,
  named credentials and custom settings that the AWS Partner must provide to their user. However, partners can pair this permission set with a Salesforce system admin profile and enable all of the
  necessary permissions to configure the application. For more information about named credentials, refer to [Set up named credentials](set-up-api-credentials.md "set-up-api-credentials.md")

## Integration User (APN Integration User)

- Assign to a system user responsible for processing the integration.
- To schedule an integration, a Salesforce system admin signs in as this user
  and invokes the system integration schedule.
- Allows admins to configure the mappings and invoke integration schedules.
- The integration may break if this permission isn’t set for the user who runs the integration.
- In addition to this permission set, the user designated to process the integration
  should have field level access to all mapped fields. If not, the
  mappings fail to sync as assigned.
- The outbound jobs are designed to ignore updates done in the integration user
  context to prevent a race-around condition, with the same record updated during inbound
  integration being flagged to be sent for outbound integration.

## Business user (APN Business User)

- Assign to business users who might want to see the sync log details related to
  their opportunities. This allows for end-user troubleshooting if data is not
  syncing correctly.
- Does not provide visibility to the sync log records and only gives access to the
  object and fields.
- We recommend setting sync log records to private, since they contain sensitive
  opportunity information.
- If you configure a private model, APN business users can access only the
  records if the partner Salesforce administrator configures record sharing
  with users.

## Granting permissions to view reports

To allow a user to view reports on the **Home** tab of the AWS Partner CRM
connector, an administrator must grant the following permissions:

- Create and Customize Reports
- Edit My Reports
- Mange Reports in Public Folders
- Run Reports
- View Reports in Public Folders

For more information, refer to [Grant Users Access to Reports and Dashboards](https://help.salesforce.com/s/articleView?id=sfdo.PMM_Folder_Sharing_Reports_Dash.htm "https://help.salesforce.com/s/articleView?id=sfdo.PMM_Folder_Sharing_Reports_Dash.htm") in the Salesforce help.

## Activating flow users

Activating users as flow users enables them to run flows and use the **Link
private offer** button on an ACE opportunity.

1. Ensure that the system administrator has permission to assign a flow user. For
   more information, refer to [Add Run Flows Permissions](https://help.salesforce.com/s/articleView?id=sf.wcc_setup_add_run_flows_perms.htm "https://help.salesforce.com/s/articleView?id=sf.wcc_setup_add_run_flows_perms.htm") in the Salesforce help.
2. Choose **Setup**, **Users**.
3. Choose a user.
4. Choose **Flow user**.

# Editing the Directory Configuration

After a WorkSpaces Applications directory configuration has been created, you can edit it to add,
remove, or modify organizational units, update the service account username, or
update the service account password.

###### To update a directory configuration

1. Open the WorkSpaces Applications console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Directory Configs**
   and select the directory configuration to edit.
3. Choose **Actions**, **Edit**.
4. Update the fields to be changed. To add additional OUs, select the plus
   sign (**+**) next to the topmost OU field. To remove an OU
   field, select the **x** next to the field.

###### Note

At least one OU is required. OUs that are currently in use cannot be
removed. 5. To save changes, choose **Update Directory
Config**. 6. The information in the **Details** tab should now update
to reflect the changes.
Changes to the service account sign-in credentials do not impact in-process
streaming instance operations. New streaming instance operations use the updated
credentials. For more information, see [Updating the Service Account Used for Joining the Domain](active-directory-service-acct.md "active-directory-service-acct.md").

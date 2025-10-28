# Manage Connector for AD template access control entries

An access control entry grants controls which Active Directory groups can or cannot enroll certificates for a specific Connector for AD template. When you can create or manage groups and permissions in Connector for AD, you must provide the Security identifier (SID) of the group object from Active Directory. You can obtain the SID using the following PowerShell command. For information about SIDs, see [How security identifiers work](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers") in the Microsoft Directory Domain Services documentation.

```

        `$` `Get-ADGroup -Identity "`my_active_directory_group_name`"`

```

The following procedures illustrate how to create and manage Connector for AD template access group entries.

Console

**To manage template group permissions using the console**

You can manage groups and permissions for an existing template can be managed from a template's details page. For more information, see [View connector
template details](view-ad-template.md "view-ad-template.md").

Set permissions on which groups can or cannot enroll certificates for the specific
template. You provide the security identifier (SID) of the group. Then you set the enroll
and auto-enroll permissions for the group. For auto-enrollment, both enroll and auto-enroll
must be set to "Allow."

API

**To manage template group permissions using the API**

**Create**: [CreateTemplateGroupAccessControlEntry](../../../pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.md "../../../pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.md") action in the AWS Private CA Connector for Active Directory
API.

**Update**: [UpdateTemplateGroupAccessControlEntry](../../../pca-connector-ad/latest/APIReference/API_UpdateTemplateGroupAccessControlEntry.md "../../../pca-connector-ad/latest/APIReference/API_UpdateTemplateGroupAccessControlEntry.md") action in the AWS Private CA Connector for Active Directory
API.

**Retrieve**: [GetTemplateGroupAccessControlEntry](../../../pca-connector-ad/latest/APIReference/API_GetTemplateGroupAccessControlEntry.md "../../../pca-connector-ad/latest/APIReference/API_GetTemplateGroupAccessControlEntry.md") action in the AWS Private CA Connector for Active Directory
API.

**List**: [ListTemplateGroupAccessControlEntries](../../../pca-connector-ad/latest/APIReference/API_ListTemplateGroupAccessControlEntries.md "../../../pca-connector-ad/latest/APIReference/API_ListTemplateGroupAccessControlEntries.md") action in the AWS Private CA Connector for Active Directory
API.

**Delete**: [DeleteTemplateGroupAccessControlEntry](../../../pca-connector-ad/latest/APIReference/API_DeleteTemplateGroupAccessControlEntry.md "../../../pca-connector-ad/latest/APIReference/API_DeleteTemplateGroupAccessControlEntry.md") action in the AWS Private CA Connector for Active Directory
API.

CLI

**To manage template group permissions using the CLI**

**Create**: [create-template-group-access-control-entry](../../../cli/latest/reference/pca-connector-ad/create-template-group-access-control-entry.md "../../../cli/latest/reference/pca-connector-ad/create-template-group-access-control-entry.md") command in the
AWS Private CA Connector for Active Directory section of the AWS CLI.

**Update**: [update-template-group-access-control-entry](../../../cli/latest/reference/pca-connector-ad/update-template-group-access-control-entry.md "../../../cli/latest/reference/pca-connector-ad/update-template-group-access-control-entry.md") command in the
AWS Private CA Connector for Active Directory section of the AWS CLI.

**Retrieve**: [get-template-group-access-control-entry](../../../cli/latest/reference/pca-connector-ad/get-template-group-access-control-entry.md "../../../cli/latest/reference/pca-connector-ad/get-template-group-access-control-entry.md") command in the AWS Private CA Connector for Active Directory
section of the AWS CLI.

**List**: [list-template-group-access-control-entries](../../../cli/latest/reference/pca-connector-ad/list-template-group-access-control-entries.md "../../../cli/latest/reference/pca-connector-ad/list-template-group-access-control-entries.md") command in the
AWS Private CA Connector for Active Directory section of the AWS CLI.

**Delete**: [delete-template-group-access-control-entries](../../../cli/latest/reference/pca-connector-ad/delete-template-group-access-control-entries.md "../../../cli/latest/reference/pca-connector-ad/delete-template-group-access-control-entries.md") command in the
AWS Private CA Connector for Active Directory section of the AWS CLI.

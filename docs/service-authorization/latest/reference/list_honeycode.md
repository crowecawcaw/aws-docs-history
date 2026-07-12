# Actions, resources, and condition keys for Amazon Honeycode

Amazon Honeycode (service prefix: `honeycode`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../honeycode/latest/UserGuide.md "../../../honeycode/latest/UserGuide.md").
- View a list of the [API operations available for
  this service](../../../honeycode/latest/APIReference.md "../../../honeycode/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../honeycode/latest/UserGuide/getting-started-authorization.md "../../../honeycode/latest/UserGuide/getting-started-authorization.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/honeycode/honeycode.json "https://servicereference.us-east-1.amazonaws.com/v1/honeycode/honeycode.json") for this service.

###### Topics

- [Actions defined by Amazon Honeycode](#list_honeycode-actions-as-permissions "#list_honeycode-actions-as-permissions")
- [Permission-only actions for Amazon Honeycode](#list_honeycode-permission-only-actions "#list_honeycode-permission-only-actions")
- [Resource types defined by Amazon Honeycode](#list_honeycode-resources-for-iam-policies "#list_honeycode-resources-for-iam-policies")
- [Condition keys for Amazon Honeycode](#list_honeycode-policy-keys "#list_honeycode-policy-keys")

## Actions defined by Amazon Honeycode

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                     | Description                                                    | Resource types (\*required)                                                                                    | Condition keys | Access level   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------- | -------------- |
| [BatchCreateTableRows](../../../honeycode/latest/UserGuide/API_BatchCreateTableRows.md "../../../honeycode/latest/UserGuide/API_BatchCreateTableRows.md")                   | Grants permission to create new rows in a table                | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Write          |
| [BatchDeleteTableRows](../../../honeycode/latest/UserGuide/API_BatchDeleteTableRows.md "../../../honeycode/latest/UserGuide/API_BatchDeleteTableRows.md")                   | Grants permission to delete rows from a table                  | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Write          |
| [BatchUpdateTableRows](../../../honeycode/latest/UserGuide/API_BatchUpdateTableRows.md "../../../honeycode/latest/UserGuide/API_BatchUpdateTableRows.md")                   | Grants permission to update rows in a table                    | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Write          |
| [BatchUpsertTableRows](../../../honeycode/latest/UserGuide/API_BatchUpsertTableRows.md "../../../honeycode/latest/UserGuide/API_BatchUpsertTableRows.md")                   | Grants permission to upsert rows in a table                    | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Write          |
| [DescribeTableDataImportJob](../../../honeycode/latest/UserGuide/API_DescribeTableDataImportJob.md "../../../honeycode/latest/UserGuide/API_DescribeTableDataImportJob.md") | Grants permission to get details about a table data import job | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Read           |
| [GetScreenData](../../../honeycode/latest/UserGuide/API_GetScreenData.md "../../../honeycode/latest/UserGuide/API_GetScreenData.md")                                        | Grants permission to load the data from a screen               | [screen\*](#list_honeycode-resource-screen "#list_honeycode-resource-screen")                                  |                | Read           |
| [InvokeScreenAutomation](../../../honeycode/latest/UserGuide/API_InvokeScreenAutomation.md "../../../honeycode/latest/UserGuide/API_InvokeScreenAutomation.md")             | Grants permission to invoke a screen automation                | [screen-automation\*](#list_honeycode-resource-screen-automation "#list_honeycode-resource-screen-automation") |                | Write          |
| [ListTableColumns](../../../honeycode/latest/UserGuide/API_ListTableColumns.md "../../../honeycode/latest/UserGuide/API_ListTableColumns.md")                               | Grants permission to list the columns in a table               | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | List           |
| [ListTableRows](../../../honeycode/latest/UserGuide/API_ListTableRows.md "../../../honeycode/latest/UserGuide/API_ListTableRows.md")                                        | Grants permission to list the rows in a table                  | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | List           |
| [ListTables](../../../honeycode/latest/UserGuide/API_ListTables.md "../../../honeycode/latest/UserGuide/API_ListTables.md")                                                 | Grants permission to list the tables in a workbook             | [workbook\*](#list_honeycode-resource-workbook "#list_honeycode-resource-workbook")                            |                | List           |
| [ListTagsForResource](../../../honeycode/latest/UserGuide/API_ListTagsForResource.md "../../../honeycode/latest/UserGuide/API_ListTagsForResource.md")                      | Grants permission to list all tags for a resource              |                                                                                                                |                | Tagging, Write |
| [QueryTableRows](../../../honeycode/latest/UserGuide/API_QueryTableRows.md "../../../honeycode/latest/UserGuide/API_QueryTableRows.md")                                     | Grants permission to query the rows of a table using a filter  | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Read           |
| [StartTableDataImportJob](../../../honeycode/latest/UserGuide/API_StartTableDataImportJob.md "../../../honeycode/latest/UserGuide/API_StartTableDataImportJob.md")          | Grants permission to start a table data import job             | [table\*](#list_honeycode-resource-table "#list_honeycode-resource-table")                                     |                | Write          |
| [TagResource](../../../honeycode/latest/UserGuide/API_TagResource.md "../../../honeycode/latest/UserGuide/API_TagResource.md")                                              | Grants permission to tag a resource                            |                                                                                                                |                | Tagging, Write |
| [UntagResource](../../../honeycode/latest/UserGuide/API_UntagResource.md "../../../honeycode/latest/UserGuide/API_UntagResource.md")                                        | Grants permission to untag a resource                          |                                                                                                                |                | Tagging, Write |

## Permission-only actions for Amazon Honeycode

The following actions are defined by Amazon Honeycode but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                          | Description                                                                                               | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [ApproveTeamAssociation](../../../honeycode/latest/UserGuide/team-association.md#approve-team-association "../../../honeycode/latest/UserGuide/team-association.md#approve-team-association")    | Grants permission to approve a team association request for your AWS Account                              |                             |                | Write        |
| [CreateTeam](../../../honeycode/latest/UserGuide/team.md#create-team "../../../honeycode/latest/UserGuide/team.md#create-team")                                                                  | Grants permission to create a new Amazon Honeycode team for your AWS Account                              |                             |                | Write        |
| [CreateTenant](../../../honeycode/latest/UserGuide/tenant.md#create-tenant "../../../honeycode/latest/UserGuide/tenant.md#create-tenant")                                                        | Grants permission to create a new tenant within Amazon Honeycode for your AWS Account                     |                             |                | Write        |
| [DeleteDomains](../../../honeycode/latest/UserGuide/domain.md#delete-domains "../../../honeycode/latest/UserGuide/domain.md#delete-domains")                                                     | Grants permission to delete Amazon Honeycode domains for your AWS Account                                 |                             |                | Write        |
| [DeregisterGroups](../../../honeycode/latest/UserGuide/group.md#deregister-groups "../../../honeycode/latest/UserGuide/group.md#deregister-groups")                                              | Grants permission to remove groups from an Amazon Honeycode team for your AWS Account                     |                             |                | Write        |
| [DescribeTeam](../../../honeycode/latest/UserGuide/team.md#describe-team "../../../honeycode/latest/UserGuide/team.md#describe-team")                                                            | Grants permission to get details about Amazon Honeycode teams for your AWS Account                        |                             |                | Read         |
| [ListDomains](../../../honeycode/latest/UserGuide/domain.md#list-domains "../../../honeycode/latest/UserGuide/domain.md#list-domains")                                                           | Grants permission to list all Amazon Honeycode domains and their verification status for your AWS Account |                             |                | List         |
| [ListGroups](../../../honeycode/latest/UserGuide/group.md#list-groups "../../../honeycode/latest/UserGuide/group.md#list-groups")                                                                | Grants permission to list all groups in an Amazon Honeycode team for your AWS Account                     |                             |                | List         |
| [ListTeamAssociations](../../../honeycode/latest/UserGuide/team-association.md#list-team-associations "../../../honeycode/latest/UserGuide/team-association.md#list-team-associations")          | Grants permission to list all pending and approved team associations with your AWS Account                |                             |                | List         |
| [ListTenants](../../../honeycode/latest/UserGuide/tenant.md#list-tenants "../../../honeycode/latest/UserGuide/tenant.md#list-tenants")                                                           | Grants permission to list all tenants of Amazon Honeycode for your AWS Account                            |                             |                | List         |
| [RegisterDomainForVerification](../../../honeycode/latest/UserGuide/domain.md#register-domain-for-verification "../../../honeycode/latest/UserGuide/domain.md#register-domain-for-verification") | Grants permission to request verification of the Amazon Honeycode domains for your AWS Account            |                             |                | Write        |
| [RegisterGroups](../../../honeycode/latest/UserGuide/group.md#register-groups "../../../honeycode/latest/UserGuide/group.md#register-groups")                                                    | Grants permission to add groups to an Amazon Honeycode team for your AWS Account                          |                             |                | Write        |
| [RejectTeamAssociation](../../../honeycode/latest/UserGuide/team-association.md#reject-team-association "../../../honeycode/latest/UserGuide/team-association.md#reject-team-association")       | Grants permission to reject a team association request for your AWS Account                               |                             |                | Write        |
| [RestartDomainVerification](../../../honeycode/latest/UserGuide/domain.md#restart-domain-verification "../../../honeycode/latest/UserGuide/domain.md#restart-domain-verification")               | Grants permission to restart verification of the Amazon Honeycode domains for your AWS Account            |                             |                | Write        |
| [UpdateTeam](../../../honeycode/latest/UserGuide/team.md#update-team "../../../honeycode/latest/UserGuide/team.md#update-team")                                                                  | Grants permission to update an Amazon Honeycode team for your AWS Account                                 |                             |                | Write        |

## Resource types defined by Amazon Honeycode

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                             | ARN                                                                                                                                                 | Condition keys |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [screen](../../../honeycode/latest/UserGuide/resource-screen.md "../../../honeycode/latest/UserGuide/resource-screen.md")                                  | arn:${Partition}:honeycode:${Region}:${Account}:screen:workbook/${WorkbookId}/app/${AppId}/screen/${ScreenId}                                       |                |
| [screen-automation](../../../honeycode/latest/UserGuide/resource-screen-automation.md "../../../honeycode/latest/UserGuide/resource-screen-automation.md") | arn:${Partition}:honeycode:${Region}:${Account}:screen-automation:workbook/${WorkbookId}/app/${AppId}/screen/${ScreenId}/automation/${AutomationId} |                |
| [table](../../../honeycode/latest/UserGuide/resource-table.md "../../../honeycode/latest/UserGuide/resource-table.md")                                     | arn:${Partition}:honeycode:${Region}:${Account}:table:workbook/${WorkbookId}/table/${TableId}                                                       |                |
| [workbook](../../../honeycode/latest/UserGuide/resource-workbook.md "../../../honeycode/latest/UserGuide/resource-workbook.md")                            | arn:${Partition}:honeycode:${Region}:${Account}:workbook:workbook/${WorkbookId}                                                                     |                |

## Condition keys for Amazon Honeycode

Amazon Honeycode has no service-specific condition keys that can be used in the
`Condition` element of policy statements.

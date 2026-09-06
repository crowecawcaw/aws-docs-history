

# Actions, resources, and condition keys for Amazon Honeycode
<a name="list_honeycode"></a>

Amazon Honeycode (service prefix: `honeycode`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/honeycode/latest/UserGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/honeycode/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/honeycode/latest/UserGuide/getting-started-authorization.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/honeycode/honeycode.json) for this service.

**Topics**
+ [Actions defined by Amazon Honeycode](#list_honeycode-actions-as-permissions)
+ [Permission-only actions for Amazon Honeycode](#list_honeycode-permission-only-actions)
+ [Resource types defined by Amazon Honeycode](#list_honeycode-resources-for-iam-policies)
+ [Condition keys for Amazon Honeycode](#list_honeycode-policy-keys)

## Actions defined by Amazon Honeycode
<a name="list_honeycode-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateTableRows](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_BatchCreateTableRows.html)  **
  - **Description:** Grants permission to create new rows in a table
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDeleteTableRows](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_BatchDeleteTableRows.html)  **
  - **Description:** Grants permission to delete rows from a table
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchUpdateTableRows](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_BatchUpdateTableRows.html)  **
  - **Description:** Grants permission to update rows in a table
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchUpsertTableRows](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_BatchUpsertTableRows.html)  **
  - **Description:** Grants permission to upsert rows in a table
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeTableDataImportJob](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_DescribeTableDataImportJob.html)  **
  - **Description:** Grants permission to get details about a table data import job
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetScreenData](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_GetScreenData.html)  **
  - **Description:** Grants permission to load the data from a screen
  - **Resource types (\*required):** [screen\*](#list_honeycode-resource-screen)
  - **Condition keys:**  
  - **Access level:** Read

- **   [InvokeScreenAutomation](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_InvokeScreenAutomation.html)  **
  - **Description:** Grants permission to invoke a screen automation
  - **Resource types (\*required):** [screen-automation\*](#list_honeycode-resource-screen-automation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListTableColumns](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_ListTableColumns.html)  **
  - **Description:** Grants permission to list the columns in a table
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTableRows](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_ListTableRows.html)  **
  - **Description:** Grants permission to list the rows in a table
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTables](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_ListTables.html)  **
  - **Description:** Grants permission to list the tables in a workbook
  - **Resource types (\*required):** [workbook\*](#list_honeycode-resource-workbook)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [QueryTableRows](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_QueryTableRows.html)  **
  - **Description:** Grants permission to query the rows of a table using a filter
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartTableDataImportJob](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_StartTableDataImportJob.html)  **
  - **Description:** Grants permission to start a table data import job
  - **Resource types (\*required):** [table\*](#list_honeycode-resource-table)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/honeycode/latest/UserGuide/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Tagging, Write



## Permission-only actions for Amazon Honeycode
<a name="list_honeycode-permission-only-actions"></a>

The following actions are defined by Amazon Honeycode but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [ApproveTeamAssociation](https://docs.aws.amazon.com/honeycode/latest/UserGuide/team-association.html#approve-team-association)  | Grants permission to approve a team association request for your AWS Account |  |   | Write | 
|   [CreateTeam](https://docs.aws.amazon.com/honeycode/latest/UserGuide/team.html#create-team)  | Grants permission to create a new Amazon Honeycode team for your AWS Account |  |   | Write | 
|   [CreateTenant](https://docs.aws.amazon.com/honeycode/latest/UserGuide/tenant.html#create-tenant)  | Grants permission to create a new tenant within Amazon Honeycode for your AWS Account |  |   | Write | 
|   [DeleteDomains](https://docs.aws.amazon.com/honeycode/latest/UserGuide/domain.html#delete-domains)  | Grants permission to delete Amazon Honeycode domains for your AWS Account |  |   | Write | 
|   [DeregisterGroups](https://docs.aws.amazon.com/honeycode/latest/UserGuide/group.html#deregister-groups)  | Grants permission to remove groups from an Amazon Honeycode team for your AWS Account |  |   | Write | 
|   [DescribeTeam](https://docs.aws.amazon.com/honeycode/latest/UserGuide/team.html#describe-team)  | Grants permission to get details about Amazon Honeycode teams for your AWS Account |  |   | Read | 
|   [ListDomains](https://docs.aws.amazon.com/honeycode/latest/UserGuide/domain.html#list-domains)  | Grants permission to list all Amazon Honeycode domains and their verification status for your AWS Account |  |   | List | 
|   [ListGroups](https://docs.aws.amazon.com/honeycode/latest/UserGuide/group.html#list-groups)  | Grants permission to list all groups in an Amazon Honeycode team for your AWS Account |  |   | List | 
|   [ListTeamAssociations](https://docs.aws.amazon.com/honeycode/latest/UserGuide/team-association.html#list-team-associations)  | Grants permission to list all pending and approved team associations with your AWS Account |  |   | List | 
|   [ListTenants](https://docs.aws.amazon.com/honeycode/latest/UserGuide/tenant.html#list-tenants)  | Grants permission to list all tenants of Amazon Honeycode for your AWS Account |  |   | List | 
|   [RegisterDomainForVerification](https://docs.aws.amazon.com/honeycode/latest/UserGuide/domain.html#register-domain-for-verification)  | Grants permission to request verification of the Amazon Honeycode domains for your AWS Account |  |   | Write | 
|   [RegisterGroups](https://docs.aws.amazon.com/honeycode/latest/UserGuide/group.html#register-groups)  | Grants permission to add groups to an Amazon Honeycode team for your AWS Account |  |   | Write | 
|   [RejectTeamAssociation](https://docs.aws.amazon.com/honeycode/latest/UserGuide/team-association.html#reject-team-association)  | Grants permission to reject a team association request for your AWS Account |  |   | Write | 
|   [RestartDomainVerification](https://docs.aws.amazon.com/honeycode/latest/UserGuide/domain.html#restart-domain-verification)  | Grants permission to restart verification of the Amazon Honeycode domains for your AWS Account |  |   | Write | 
|   [UpdateTeam](https://docs.aws.amazon.com/honeycode/latest/UserGuide/team.html#update-team)  | Grants permission to update an Amazon Honeycode team for your AWS Account |  |   | Write | 

## Resource types defined by Amazon Honeycode
<a name="list_honeycode-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [screen](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-screen.html)  | arn:${Partition}:honeycode:${Region}:${Account}:screen:workbook/${WorkbookId}/app/${AppId}/screen/${ScreenId} |   | 
|  [screen-automation](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-screen-automation.html)  | arn:${Partition}:honeycode:${Region}:${Account}:screen-automation:workbook/${WorkbookId}/app/${AppId}/screen/${ScreenId}/automation/${AutomationId} |   | 
|  [table](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-table.html)  | arn:${Partition}:honeycode:${Region}:${Account}:table:workbook/${WorkbookId}/table/${TableId} |   | 
|  [workbook](https://docs.aws.amazon.com/honeycode/latest/UserGuide/resource-workbook.html)  | arn:${Partition}:honeycode:${Region}:${Account}:workbook:workbook/${WorkbookId} |   | 

## Condition keys for Amazon Honeycode
<a name="list_honeycode-policy-keys"></a>

Amazon Honeycode has no service-specific condition keys that can be used in the `Condition` element of policy statements.
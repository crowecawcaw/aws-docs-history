

# Actions, resources, and condition keys for AWS Lake Formation
<a name="list_lakeformation"></a>

AWS Lake Formation (service prefix: `lakeformation`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/lake-formation/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/lake-formation/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/lake-formation/latest/dg/permissions-reference.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/lakeformation/lakeformation.json) for this service.

**Topics**
+ [API operations defined by AWS Lake Formation](#list_lakeformation-operations)
+ [Actions defined by AWS Lake Formation](#list_lakeformation-actions-as-permissions)
+ [Resource types defined by AWS Lake Formation](#list_lakeformation-resources-for-iam-policies)
+ [Condition keys for AWS Lake Formation](#list_lakeformation-policy-keys)

## API operations defined by AWS Lake Formation
<a name="list_lakeformation-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_lakeformation-actions-as-permissions).




- **   BatchGrantPermissions  **
  - **IAM action:**  [lakeformation:BatchGrantPermissions](#list_lakeformation-action-BatchGrantPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   BatchRevokePermissions  **
  - **IAM action:**  [lakeformation:BatchRevokePermissions](#list_lakeformation-action-BatchRevokePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateDataCellsFilter  **
  - **IAM action:**  [lakeformation:CreateDataCellsFilter](#list_lakeformation-action-CreateDataCellsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLFTagExpression  **
  - **IAM action:**  [lakeformation:CreateLFTagExpression](#list_lakeformation-action-CreateLFTagExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLakeFormationIdentityCenterConfiguration  **
  - **IAM action:**  [lakeformation:CreateLakeFormationIdentityCenterConfiguration](#list_lakeformation-action-CreateLakeFormationIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLakeFormationOptIn  **
  - **IAM action:**  [lakeformation:CreateLakeFormationOptIn](#list_lakeformation-action-CreateLakeFormationOptIn) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataCellsFilter  **
  - **IAM action:**  [lakeformation:DeleteDataCellsFilter](#list_lakeformation-action-DeleteDataCellsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLFTagExpression  **
  - **IAM action:**  [lakeformation:DeleteLFTagExpression](#list_lakeformation-action-DeleteLFTagExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLakeFormationIdentityCenterConfiguration  **
  - **IAM action:**  [lakeformation:DeleteLakeFormationIdentityCenterConfiguration](#list_lakeformation-action-DeleteLakeFormationIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLakeFormationOptIn  **
  - **IAM action:**  [lakeformation:DeleteLakeFormationOptIn](#list_lakeformation-action-DeleteLakeFormationOptIn) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeLakeFormationIdentityCenterConfiguration  **
  - **IAM action:**  [lakeformation:DescribeLakeFormationIdentityCenterConfiguration](#list_lakeformation-action-DescribeLakeFormationIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataCellsFilter  **
  - **IAM action:**  [lakeformation:GetDataCellsFilter](#list_lakeformation-action-GetDataCellsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataLakePrincipal  **
  - **IAM action:**  [lakeformation:GetDataLakePrincipal](#list_lakeformation-action-GetDataLakePrincipal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataLakeSettings  **
  - **IAM action:**  [lakeformation:GetDataLakeSettings](#list_lakeformation-action-GetDataLakeSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEffectivePermissionsForPath  **
  - **IAM action:**  [lakeformation:GetEffectivePermissionsForPath](#list_lakeformation-action-GetEffectivePermissionsForPath) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLFTagExpression  **
  - **IAM action:**  [lakeformation:GetLFTagExpression](#list_lakeformation-action-GetLFTagExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryState  **
  - **IAM action:**  [lakeformation:GetQueryState](#list_lakeformation-action-GetQueryState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueryStatistics  **
  - **IAM action:**  [lakeformation:GetQueryStatistics](#list_lakeformation-action-GetQueryStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemporaryDataLocationCredentials  **
  - **IAM action:**  [lakeformation:GetDataAccess](#list_lakeformation-action-GetDataAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetWorkUnitResults  **
  - **IAM action:**  [lakeformation:GetWorkUnitResults](#list_lakeformation-action-GetWorkUnitResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkUnits  **
  - **IAM action:**  [lakeformation:GetWorkUnits](#list_lakeformation-action-GetWorkUnits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDataCellsFilter  **
  - **IAM action:**  [lakeformation:ListDataCellsFilter](#list_lakeformation-action-ListDataCellsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLFTagExpressions  **
  - **IAM action:**  [lakeformation:ListLFTagExpressions](#list_lakeformation-action-ListLFTagExpressions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLakeFormationOptIns  **
  - **IAM action:**  [lakeformation:ListLakeFormationOptIns](#list_lakeformation-action-ListLakeFormationOptIns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPermissions  **
  - **IAM action:**  [lakeformation:ListPermissions](#list_lakeformation-action-ListPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutDataLakeSettings  **
  - **IAM action:**  [lakeformation:PutDataLakeSettings](#list_lakeformation-action-PutDataLakeSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartQueryPlanning  **
  - **IAM action:**  [lakeformation:StartQueryPlanning](#list_lakeformation-action-StartQueryPlanning) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataCellsFilter  **
  - **IAM action:**  [lakeformation:UpdateDataCellsFilter](#list_lakeformation-action-UpdateDataCellsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLFTagExpression  **
  - **IAM action:**  [lakeformation:UpdateLFTagExpression](#list_lakeformation-action-UpdateLFTagExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLakeFormationIdentityCenterConfiguration  **
  - **IAM action:**  [lakeformation:UpdateLakeFormationIdentityCenterConfiguration](#list_lakeformation-action-UpdateLakeFormationIdentityCenterConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Lake Formation
<a name="list_lakeformation-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AddLFTagsToResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_AddLFTagsToResource.html)  | Grants permission to attach Lake Formation tags to catalog resources |  |   | Tagging, Write | 
|   [BatchGrantPermissions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_BatchGrantPermissions.html)  | Grants permission to data lake permissions to one or more principals in a batch |  |   | Permissions management, Write | 
|   [BatchRevokePermissions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_BatchRevokePermissions.html)  | Grants permission to revoke data lake permissions from one or more principals in a batch |  |   | Permissions management, Write | 
|   [CancelTransaction](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CancelTransaction.html)  | Grants permission to cancel the given transaction |  |   | Write | 
|   [CommitTransaction](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CommitTransaction.html)  | Grants permission to commit the given transaction |  |   | Write | 
|   [CreateDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateDataCellsFilter.html)  | Grants permission to create a Lake Formation data cell filter |  |   | Write | 
|   [CreateLFTag](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateLFTag.html)  | Grants permission to create a Lake Formation tag |  |   | Write | 
|   [CreateLFTagExpression](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateLFTagExpression.html)  | Grants permission to create a Lake Formation tag expression |  |   | Write | 
|   [CreateLakeFormationIdentityCenterConfiguration](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateLakeFormationIdentityCenterConfiguration.html)  | Grants permission to create an IAM Identity Center connection with Lake Formation to allow IAM Identity Center users and groups to access Data Catalog resources |  |   | Write | 
|   [CreateLakeFormationOptIn](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_CreateLakeFormationOptIn.html)  | Grants permission to enforce Lake Formation permissions for the given databases, tables, and principals |  |   | Write | 
|   [DeleteDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteDataCellsFilter.html)  | Grants permission to delete a Lake Formation data cell filter |  |   | Write | 
|   [DeleteLFTag](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLFTag.html)  | Grants permission to delete a Lake Formation tag |  |   | Write | 
|   [DeleteLFTagExpression](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLFTagExpression.html)  | Grants permission to delete a Lake Formation expression |  |   | Write | 
|   [DeleteLakeFormationIdentityCenterConfiguration](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLakeFormationIdentityCenterConfiguration.html)  | Grants permission to delete an IAM Identity Center connection with Lake Formation |  |   | Write | 
|   [DeleteLakeFormationOptIn](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteLakeFormationOptIn.html)  | Grants permission to remove the Lake Formation permissions enforcement of the given databases, tables, and principals |  |   | Write | 
|   [DeleteObjectsOnCancel](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeleteObjectsOnCancel.html)  | Grants permission to delete the specified objects if the transaction is canceled |  |   | Write | 
|   [DeregisterResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeregisterResource.html)  | Grants permission to deregister a registered location |  |   | Write | 
|   [DescribeLakeFormationIdentityCenterConfiguration](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeLakeFormationIdentityCenterConfiguration.html)  | Grants permission to describe the IAM Identity Center connection with Lake Formation |  |   | Read | 
|   [DescribeResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeResource.html)  | Grants permission to describe a registered location |  |   | Read | 
|   [DescribeTransaction](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeTransaction.html)  | Grants permission to get status of the given transaction |  |   | Read | 
|   [ExtendTransaction](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ExtendTransaction.html)  | Grants permission to extend the timeout of the given transaction |  |   | Write | 
|   [GetDataAccess](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-underlying-data.html)  | Grants permission to virtual data lake access |  | [lakeformation:EnabledOnlyForMetaDataAccess](#list_lakeformation-lakeformation_EnabledOnlyForMetaDataAccess) | Write | 
|   [GetDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataCellsFilter.html)  | Grants permission to retrieve a Lake Formation data cell filter |  |   | Read | 
|   [GetDataLakePrincipal](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataLakePrincipal.html)  | Grants permission to retrieve the identity of the invoking principal |  |   | Read | 
|   [GetDataLakeSettings](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataLakeSettings.html)  | Grants permission to retrieve data lake settings such as the list of data lake administrators and database and table default permissions |  |   | Read | 
|   [GetEffectivePermissionsForPath](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetEffectivePermissionsForPath.html)  | Grants permission to retrieve permissions attached to resources in the given path |  |   | Read | 
|   [GetLFTag](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetLFTag.html)  | Grants permission to retrieve a Lake Formation tag |  |   | Read | 
|   [GetLFTagExpression](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetLFTagExpression.html)  | Grants permission to retrieve a Lake Formation tag expression |  |   | Read | 
|   [GetQueryState](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetQueryState.html)  | Grants permission to retrieve the state of the given query |  |   | Read | 
|   [GetQueryStatistics](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetQueryStatistics.html)  | Grants permission to retrieve the statistics for the given query |  |   | Read | 
|   [GetResourceLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetResourceLFTags.html)  | Grants permission to retrieve lakeformation tags on a catalog resource |  |   | Read | 
|   [GetTableObjects](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTableObjects.html)  | Grants permission to retrieve objects from a table |  |   | Read | 
|   [GetTemporaryGluePartitionCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGluePartitionCredentials.html)  | Grants permission to get temporary credentials to access Glue partition data through Lake Formation |  |   | Read | 
|   [GetTemporaryGlueTableCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGlueTableCredentials.html)  | Grants permission to get temporary credentials to access Glue table data through Lake Formation |  |   | Read | 
|   [GetWorkUnitResults](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetWorkUnitResults.html)  | Grants permission to retrieve the results for the given work units |  |   | Read | 
|   [GetWorkUnits](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetWorkUnits.html)  | Grants permission to retrieve the work units for the given query |  |   | Read | 
|   [GrantPermissions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GrantPermissions.html)  | Grants permission to data lake permissions to a principal |  |   | Permissions management, Write | 
|   [ListDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListDataCellsFilter.html)  | Grants permission to list cell filters |  |   | List | 
|   [ListLFTagExpressions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLFTagExpressions.html)  | Grants permission to list Lake Foramtion tag expressions |  |   | Read | 
|   [ListLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLFTags.html)  | Grants permission to list Lake Formation tags |  |   | Read | 
|   [ListLakeFormationOptIns](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLakeFormationOptIns.html)  | Grants permission to retrieve the current list of resources and principals that are opt in to enforce Lake Formation permissions |  |   | List | 
|   [ListPermissions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListPermissions.html)  | Grants permission to list permissions filtered by principal or resource |  |   | List | 
|   [ListResources](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListResources.html)  | Grants permission to List registered locations |  |   | List | 
|   [ListTableStorageOptimizers](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListTableStorageOptimizers.html)  | Grants permission to list all the storage optimizers for the Governed table |  |   | List | 
|   [ListTransactions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListTransactions.html)  | Grants permission to list all transactions in the system |  |   | List | 
|   [PutDataLakeSettings](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_PutDataLakeSettings.html)  | Grants permission to overwrite data lake settings such as the list of data lake administrators and database and table default permissions |  |   | Permissions management, Write | 
|   [RegisterResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RegisterResource.html)  | Grants permission to register a new location to be managed by Lake Formation |  |   | Write | 
|   [RegisterResourceWithPrivilegedAccess](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RegisterResource.html)  | Grants permission to register a new location to be managed by Lake Formation, with privileged access |  |   | Write | 
|   [RemoveLFTagsFromResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RemoveLFTagsFromResource.html)  | Grants permission to remove lakeformation tags from catalog resources |  |   | Tagging, Write | 
|   [RevokePermissions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_RevokePermissions.html)  | Grants permission to revoke data lake permissions from a principal |  |   | Permissions management, Write | 
|   [SearchDatabasesByLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_SearchTablesByLFTags.html)  | Grants permission to list catalog databases with Lake Formation tags |  |   | Read | 
|   [SearchTablesByLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_SearchTablesByLFTags.html)  | Grants permission to list catalog tables with Lake Formation tags |  |   | Read | 
|   [StartQueryPlanning](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_StartQueryPlanning.html)  | Grants permission to initiate the planning of the given query |  |   | Write | 
|   [StartTransaction](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_StartTransaction.html)  | Grants permission to start a new transaction |  |   | Write | 
|   [UpdateDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateDataCellsFilter.html)  | Grants permission to update a Lake Formation data cell filter |  |   | Write | 
|   [UpdateLFTag](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateLFTag.html)  | Grants permission to update a Lake Formation tag |  |   | Write | 
|   [UpdateLFTagExpression](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateLFTagExpression.html)  | Grants permission to update a Lake Formation expression |  |   | Write | 
|   [UpdateLakeFormationIdentityCenterConfiguration](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateLakeFormationIdentityCenterConfiguration.html)  | Grants permission to update the IAM Identity Center connection parameters |  |   | Write | 
|   [UpdateResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateResource.html)  | Grants permission to update a registered location |  |   | Write | 
|   [UpdateTableObjects](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateTableObjects.html)  | Grants permission to add or delete the specified objects to or from a table |  |   | Write | 
|   [UpdateTableStorageOptimizer](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateTableStorageOptimizer.html)  | Grants permission to update the configuration of the storage optimizer for the Governed table |  |   | Write | 

## Resource types defined by AWS Lake Formation
<a name="list_lakeformation-resources-for-iam-policies"></a>

AWS Lake Formation does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Lake Formation
<a name="list_lakeformation-policy-keys"></a>

AWS Lake Formation defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [lakeformation:EnabledOnlyForMetaDataAccess](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awslakeformation.html#awslakeformation-policy-keys)  | Filters access by the presence of the key configured for role's identity-based policy | Bool | 


# Data retrieval APIs for AWS Lake Formation
<a name="awslakeformation"></a>

AWS Lake Formation provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="lakeformation-DescribeLakeFormationIdentityCenterConfiguration"></a>[DescribeLakeFormationIdentityCenterConfiguration](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeLakeFormationIdentityCenterConfiguration.html) | Describe the IAM Identity Center connection with Lake Formation | Read | 
| <a name="lakeformation-DescribeResource"></a>[DescribeResource](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeResource.html) | Describe a registered location | Read | 
| <a name="lakeformation-DescribeTransaction"></a>[DescribeTransaction](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeTransaction.html) | Get status of the given transaction | Read | 
| <a name="lakeformation-GetDataCellsFilter"></a>[GetDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataCellsFilter.html) | Retrieve a Lake Formation data cell filter | Read | 
| <a name="lakeformation-GetDataLakePrincipal"></a>[GetDataLakePrincipal](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataLakePrincipal.html) | Retrieve the identity of the invoking principal | Read | 
| <a name="lakeformation-GetDataLakeSettings"></a>[GetDataLakeSettings](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetDataLakeSettings.html) | Retrieve data lake settings such as the list of data lake administrators and database and table default permissions | Read | 
| <a name="lakeformation-GetEffectivePermissionsForPath"></a>[GetEffectivePermissionsForPath](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetEffectivePermissionsForPath.html) | Retrieve permissions attached to resources in the given path | Read | 
| <a name="lakeformation-GetLFTag"></a>[GetLFTag](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetLFTag.html) | Retrieve a Lake Formation tag | Read | 
| <a name="lakeformation-GetLFTagExpression"></a>[GetLFTagExpression](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetLFTagExpression.html) | Retrieve a Lake Formation tag expression | Read | 
| <a name="lakeformation-GetQueryState"></a>[GetQueryState](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetQueryState.html) | Retrieve the state of the given query | Read | 
| <a name="lakeformation-GetQueryStatistics"></a>[GetQueryStatistics](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetQueryStatistics.html) | Retrieve the statistics for the given query | Read | 
| <a name="lakeformation-GetResourceLFTags"></a>[GetResourceLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetResourceLFTags.html) | Retrieve lakeformation tags on a catalog resource | Read | 
| <a name="lakeformation-GetTableObjects"></a>[GetTableObjects](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTableObjects.html) | Retrieve objects from a table | Read | 
| <a name="lakeformation-GetTemporaryGluePartitionCredentials"></a>[GetTemporaryGluePartitionCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGluePartitionCredentials.html) | Get temporary credentials to access Glue partition data through Lake Formation | Read | 
| <a name="lakeformation-GetTemporaryGlueTableCredentials"></a>[GetTemporaryGlueTableCredentials](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetTemporaryGlueTableCredentials.html) | Get temporary credentials to access Glue table data through Lake Formation | Read | 
| <a name="lakeformation-GetWorkUnitResults"></a>[GetWorkUnitResults](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetWorkUnitResults.html) | Retrieve the results for the given work units | Read | 
| <a name="lakeformation-GetWorkUnits"></a>[GetWorkUnits](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_GetWorkUnits.html) | Retrieve the work units for the given query | Read | 
| <a name="lakeformation-ListDataCellsFilter"></a>[ListDataCellsFilter](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListDataCellsFilter.html) | List cell filters | List | 
| <a name="lakeformation-ListLFTagExpressions"></a>[ListLFTagExpressions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLFTagExpressions.html) | List Lake Foramtion tag expressions | Read | 
| <a name="lakeformation-ListLFTags"></a>[ListLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLFTags.html) | List Lake Formation tags | Read | 
| <a name="lakeformation-ListLakeFormationOptIns"></a>[ListLakeFormationOptIns](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListLakeFormationOptIns.html) | Retrieve the current list of resources and principals that are opt in to enforce Lake Formation permissions | List | 
| <a name="lakeformation-ListPermissions"></a>[ListPermissions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListPermissions.html) | List permissions filtered by principal or resource | List | 
| <a name="lakeformation-ListResources"></a>[ListResources](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListResources.html) | List registered locations | List | 
| <a name="lakeformation-ListTableStorageOptimizers"></a>[ListTableStorageOptimizers](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListTableStorageOptimizers.html) | List all the storage optimizers for the Governed table | List | 
| <a name="lakeformation-ListTransactions"></a>[ListTransactions](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_ListTransactions.html) | List all transactions in the system | List | 
| <a name="lakeformation-SearchDatabasesByLFTags"></a>[SearchDatabasesByLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_SearchTablesByLFTags.html) | List catalog databases with Lake Formation tags | Read | 
| <a name="lakeformation-SearchTablesByLFTags"></a>[SearchTablesByLFTags](https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_SearchTablesByLFTags.html) | List catalog tables with Lake Formation tags | Read | 
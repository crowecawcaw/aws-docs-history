

# Data retrieval APIs for Amazon Cognito Sync
<a name="amazoncognitosync"></a>

Amazon Cognito Sync provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cognito-sync-DescribeDataset"></a>[DescribeDataset](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeDataset.html) | Get metadata about a dataset by identity and dataset name | Read | 
| <a name="cognito-sync-DescribeIdentityPoolUsage"></a>[DescribeIdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityPoolUsage.html) | Get usage details (for example, data storage) about a particular identity pool | Read | 
| <a name="cognito-sync-DescribeIdentityUsage"></a>[DescribeIdentityUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_DescribeIdentityUsage.html) | Get usage information for an identity, including number of datasets and data usage | Read | 
| <a name="cognito-sync-GetBulkPublishDetails"></a>[GetBulkPublishDetails](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetBulkPublishDetails.html) | Get the status of the last BulkPublish operation for an identity pool | Read | 
| <a name="cognito-sync-GetCognitoEvents"></a>[GetCognitoEvents](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetCognitoEvents.html) | Get the events and the corresponding Lambda functions associated with an identity pool | Read | 
| <a name="cognito-sync-GetIdentityPoolConfiguration"></a>[GetIdentityPoolConfiguration](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_GetIdentityPoolConfiguration.html) | Get the configuration settings of an identity pool | Read | 
| <a name="cognito-sync-ListDatasets"></a>[ListDatasets](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListDatasets.html) | List datasets for an identity | List | 
| <a name="cognito-sync-ListIdentityPoolUsage"></a>[ListIdentityPoolUsage](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListIdentityPoolUsage.html) | Get a list of identity pools registered with Cognito | Read | 
| <a name="cognito-sync-ListRecords"></a>[ListRecords](https://docs.aws.amazon.com/cognitosync/latest/APIReference/API_ListRecords.html) | Get paginated records, optionally changed after a particular sync count for a dataset and identity | Read | 
| <a name="cognito-sync-QueryRecords"></a>QueryRecords | Query records | Read | 
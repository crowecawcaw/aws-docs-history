

# Data retrieval APIs for AWS CloudTrail
<a name="awscloudtrail"></a>

AWS CloudTrail provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="cloudtrail-DescribeQuery"></a>[DescribeQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeQuery.html) | List details for the query | Read | 
| <a name="cloudtrail-DescribeTrails"></a>[DescribeTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeTrails.html) | List settings for the trails associated with the current region for your account | Read | 
| <a name="cloudtrail-GenerateQueryResultsSummary"></a>[GenerateQueryResultsSummary](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-results-summary.html) | Generate a results summary for specified queries using the CloudTrail natural language generator | Read | 
| <a name="cloudtrail-GetChannel"></a>[GetChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetChannel.html) | Return information about a specific channel | Read | 
| <a name="cloudtrail-GetDashboard"></a>[GetDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetDashboard.html) | List settings for the dashboard | Read | 
| <a name="cloudtrail-GetEventConfiguration"></a>[GetEventConfiguration](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventConfiguration.html) | List event configurations that are configured for a trail or an event data store | Read | 
| <a name="cloudtrail-GetEventDataStore"></a>[GetEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventDataStore.html) | List settings for the event data store | Read | 
| <a name="cloudtrail-GetEventDataStoreData"></a>[GetEventDataStoreData](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-federation.html#query-federation-permissions) | Get data from an event data store by using the AWS Glue Data Catalog | Read | 
| <a name="cloudtrail-GetEventSelectors"></a>[GetEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventSelectors.html) | List settings for event selectors configured for a trail | Read | 
| <a name="cloudtrail-GetImport"></a>[GetImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetImport.html) | Return information about a specific import | Read | 
| <a name="cloudtrail-GetInsightSelectors"></a>[GetInsightSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetInsightSelectors.html) | List CloudTrail Insights selectors that are configured for a trail or event data store | Read | 
| <a name="cloudtrail-GetQueryResults"></a>[GetQueryResults](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetQueryResults.html) | Fetch results of a complete query | Read | 
| <a name="cloudtrail-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetResourcePolicy.html) | Get the resource policy attached to the provided resource | Read | 
| <a name="cloudtrail-GetServiceLinkedChannel"></a>[GetServiceLinkedChannel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events) | List settings for the service-linked channel | Read | 
| <a name="cloudtrail-GetTrail"></a>[GetTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetTrail.html) | List settings for the trail | Read | 
| <a name="cloudtrail-GetTrailStatus"></a>[GetTrailStatus](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetTrailStatus.html) | Retrieve a JSON-formatted list of information about the specified trail | Read | 
| <a name="cloudtrail-ListChannels"></a>[ListChannels](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListChannels.html) | List the channels in the current account, and their source names | List | 
| <a name="cloudtrail-ListDashboards"></a>[ListDashboards](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListDashboards.html) | List dashboards associated with the current region for your account | List | 
| <a name="cloudtrail-ListEventDataStores"></a>[ListEventDataStores](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListEventDataStores.html) | List event data stores associated with the current region for your account | List | 
| <a name="cloudtrail-ListImportFailures"></a>[ListImportFailures](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListImportFailures.html) | Return a list of failures for the specified import | Read | 
| <a name="cloudtrail-ListImports"></a>[ListImports](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListImports.html) | Return information on all imports, or a select set of imports by ImportStatus or Destination | List | 
| <a name="cloudtrail-ListInsightsData"></a>[ListInsightsData](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListInsightsData.html) | Retrieve data captured by CloudTrail Insights | List | 
| <a name="cloudtrail-ListPublicKeys"></a>[ListPublicKeys](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListPublicKeys.html) | List the public keys whose private keys were used to sign trail digest files within a specified time range | Read | 
| <a name="cloudtrail-ListQueries"></a>[ListQueries](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListQueries.html) | List queries associated with an event data store | List | 
| <a name="cloudtrail-ListServiceLinkedChannels"></a>[ListServiceLinkedChannels](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/viewing-service-linked-channels.html#slc-service-events) | List service-linked channels associated with the current region for a specified account | List | 
| <a name="cloudtrail-ListTags"></a>[ListTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTags.html) | List the tags for trails, event data stores, channels or dashboards in the current region | Read | 
| <a name="cloudtrail-ListTrails"></a>[ListTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTrails.html) | List trails associated with the current region for your account | List | 
| <a name="cloudtrail-LookupEvents"></a>[LookupEvents](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html) | Look up and retrieve metric data for API activity events captured by CloudTrail that create, update, or delete resources in your account | Read | 
| <a name="cloudtrail-SearchSampleQueries"></a>[SearchSampleQueries](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-console-queries.html) | Perform semantic search for CloudTrail Lake sample queries | Read | 
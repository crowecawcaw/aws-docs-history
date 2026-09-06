

# Data retrieval APIs for AWS Snowball
<a name="awssnowball"></a>

AWS Snowball provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="snowball-DescribeAddress"></a>[DescribeAddress](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddress.html) | Get specific details about that address in the form of an Address object | Read | 
| <a name="snowball-DescribeAddresses"></a>[DescribeAddresses](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeAddresses.html) | Describe a specified number of ADDRESS objects | List | 
| <a name="snowball-DescribeCluster"></a>[DescribeCluster](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeCluster.html) | Describe information about a specific cluster including shipping information, cluster status, and other important metadata | Read | 
| <a name="snowball-DescribeJob"></a>[DescribeJob](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeJob.html) | Describe information about a specific job including shipping information, job status, and other important metadata | Read | 
| <a name="snowball-DescribeReturnShippingLabel"></a>[DescribeReturnShippingLabel](https://docs.aws.amazon.com/snowball/latest/api-reference/API_DescribeReturnShippingLabel.html) | Describe information on the shipping label of a Snow device that is being returned to AWS | Read | 
| <a name="snowball-GetJobManifest"></a>[GetJobManifest](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobManifest.html) | Get a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value | Read | 
| <a name="snowball-GetJobUnlockCode"></a>[GetJobUnlockCode](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetJobUnlockCode.html) | Get the UnlockCode code value for the specified job | Read | 
| <a name="snowball-GetSnowballUsage"></a>[GetSnowballUsage](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSnowballUsage.html) | Get information about the Snowball service limit for your account, and also the number of Snowballs your account has in use | Read | 
| <a name="snowball-GetSoftwareUpdates"></a>[GetSoftwareUpdates](https://docs.aws.amazon.com/snowball/latest/api-reference/API_GetSoftwareUpdates.html) | Return an Amazon S3 presigned URL for an update file associated with a specified JobId | Read | 
| <a name="snowball-ListClusterJobs"></a>[ListClusterJobs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusterJobs.html) | List JobListEntry objects of the specified length | List | 
| <a name="snowball-ListClusters"></a>[ListClusters](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListClusters.html) | List ClusterListEntry objects of the specified length | List | 
| <a name="snowball-ListCompatibleImages"></a>[ListCompatibleImages](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListCompatibleImages.html) | Return a list of the different Amazon EC2 Amazon Machine Images (AMIs) that are owned by your AWS account that would be supported for use on a Snow device | List | 
| <a name="snowball-ListJobs"></a>[ListJobs](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListJobs.html) | List JobListEntry objects of the specified length | List | 
| <a name="snowball-ListLongTermPricing"></a>[ListLongTermPricing](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListLongTermPricing.html) | List LongTermPricingListEntry objects for the account making the request | Read | 
| <a name="snowball-ListPickupLocations"></a>[ListPickupLocations](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListPickupLocations.html) | List Address objects where pickup is available, of the specified length | List | 
| <a name="snowball-ListServiceVersions"></a>[ListServiceVersions](https://docs.aws.amazon.com/snowball/latest/api-reference/API_ListServiceVersions.html) | List all supported versions for Snow on-device services | List | 
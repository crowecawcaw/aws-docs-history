

# Data retrieval APIs for AWS DataSync
<a name="awsdatasync"></a>

AWS DataSync provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="datasync-DescribeAgent"></a>[DescribeAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeAgent.html) | View metadata such as name, network interfaces, and the status (that is, whether the agent is running or not) about a sync agent | Read | 
| <a name="datasync-DescribeDiscoveryJob"></a>[DescribeDiscoveryJob](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeDiscoveryJob.html) | Describe metadata about a discovery job | Read | 
| <a name="datasync-DescribeLocationAzureBlob"></a>[DescribeLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationAzureBlob.html) | View metadata, such as the path information about an Azure Blob Storage sync location | Read | 
| <a name="datasync-DescribeLocationEfs"></a>[DescribeLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationEfs.html) | View metadata, such as the path information about an Amazon EFS sync location | Read | 
| <a name="datasync-DescribeLocationFsxLustre"></a>[DescribeLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxLustre.html) | View metadata, such as the path information about an Amazon FSx Lustre sync location | Read | 
| <a name="datasync-DescribeLocationFsxOntap"></a>[DescribeLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxOntap.html) | View metadata, such as the path information about an Amazon FSx for ONTAP sync location | Read | 
| <a name="datasync-DescribeLocationFsxOpenZfs"></a>[DescribeLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxOpenZfs.html) | View metadata, such as the path information about an Amazon FSx OpenZFS sync location | Read | 
| <a name="datasync-DescribeLocationFsxWindows"></a>[DescribeLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxWindows.html) | View metadata, such as the path information about an Amazon FSx Windows sync location | Read | 
| <a name="datasync-DescribeLocationHdfs"></a>[DescribeLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationHdfs.html) | View metadata, such as the path information about an Amazon HDFS sync location | Read | 
| <a name="datasync-DescribeLocationNfs"></a>[DescribeLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationNfs.html) | View metadata, such as the path information, about a NFS sync location | Read | 
| <a name="datasync-DescribeLocationObjectStorage"></a>[DescribeLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationObjectStorage.html) | View metadata about a self-managed object storage server location | Read | 
| <a name="datasync-DescribeLocationS3"></a>[DescribeLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationS3.html) | View metadata, such as bucket name, about an Amazon S3 bucket sync location | Read | 
| <a name="datasync-DescribeLocationSmb"></a>[DescribeLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationSmb.html) | View metadata, such as the path information, about an SMB sync location | Read | 
| <a name="datasync-DescribeStorageSystem"></a>[DescribeStorageSystem](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystem.html) | View metadata about a storage system | Read | 
| <a name="datasync-DescribeStorageSystemResourceMetrics"></a>[DescribeStorageSystemResourceMetrics](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResourceMetrics.html) | Describe resource metrics collected by a discovery job | List | 
| <a name="datasync-DescribeStorageSystemResources"></a>[DescribeStorageSystemResources](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html) | Describe resources identified by a discovery job | List | 
| <a name="datasync-DescribeTask"></a>[DescribeTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTask.html) | View metadata about a sync task | Read | 
| <a name="datasync-DescribeTaskExecution"></a>[DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html) | View metadata about a sync task that is being executed | Read | 
| <a name="datasync-ListAgents"></a>[ListAgents](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListAgents.html) | List agents owned by an AWS account in a region specified in the request | List | 
| <a name="datasync-ListDiscoveryJobs"></a>[ListDiscoveryJobs](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListDiscoveryJobs.html) | List discovery jobs | List | 
| <a name="datasync-ListLocations"></a>[ListLocations](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListLocations.html) | List source and destination sync locations | List | 
| <a name="datasync-ListStorageSystems"></a>[ListStorageSystems](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListStorageSystems.html) | List storage systems | List | 
| <a name="datasync-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTagsForResource.html) | List tags that have been added to the specified resource | Read | 
| <a name="datasync-ListTaskExecutions"></a>[ListTaskExecutions](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTaskExecutions.html) | List executed sync tasks | List | 
| <a name="datasync-ListTasks"></a>[ListTasks](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTasks.html) | List of all the sync tasks | List | 
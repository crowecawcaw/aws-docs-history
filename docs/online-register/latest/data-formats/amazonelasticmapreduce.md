

# Data retrieval APIs for Amazon Elastic MapReduce
<a name="amazonelasticmapreduce"></a>

Amazon Elastic MapReduce provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="elasticmapreduce-DescribeCluster"></a>[DescribeCluster](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeCluster.html) | Get details about a cluster, including status, hardware and software configuration, VPC settings, and so on | Read | 
| <a name="elasticmapreduce-DescribeEditor"></a>[DescribeEditor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html) | View information about a notebook, including status, user, role, tags, location, and more | Read | 
| <a name="elasticmapreduce-DescribeJobFlows"></a>[DescribeJobFlows](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeJobFlows.html) | Describe details of clusters (job flows). This API is deprecated and will eventually be removed. We recommend you use ListClusters, DescribeCluster, ListSteps, ListInstanceGroups and ListBootstrapActions instead | Read | 
| <a name="elasticmapreduce-DescribeNotebookExecution"></a>[DescribeNotebookExecution](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html) | View information about a notebook execution | Read | 
| <a name="elasticmapreduce-DescribePersistentAppUI"></a>[DescribePersistentAppUI](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-debug.html) | Describe a persistent application history server | Read | 
| <a name="elasticmapreduce-DescribeReleaseLabel"></a>[DescribeReleaseLabel](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeReleaseLabel.html) | View information about an EMR release, such as which applications are supported | Read | 
| <a name="elasticmapreduce-DescribeRepository"></a>[DescribeRepository](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor) | Describe an EMR notebook repository | Read | 
| <a name="elasticmapreduce-DescribeSecurityConfiguration"></a>[DescribeSecurityConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeSecurityConfiguration.html) | Get details of a security configuration | Read | 
| <a name="elasticmapreduce-DescribeStep"></a>[DescribeStep](https://docs.aws.amazon.com/emr/latest/APIReference/API_DescribeStep.html) | Get details about a cluster step | Read | 
| <a name="elasticmapreduce-DescribeStudio"></a>[DescribeStudio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html) | View information about an EMR Studio | Read | 
| <a name="elasticmapreduce-GetAutoTerminationPolicy"></a>[GetAutoTerminationPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetAutoTerminationPolicy.html) | Retrieve the auto-termination policy associated with a cluster | Read | 
| <a name="elasticmapreduce-GetBlockPublicAccessConfiguration"></a>[GetBlockPublicAccessConfiguration](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetBlockPublicAccessConfiguration.html) | Retrieve the EMR block public access configuration for the AWS account in the Region | Read | 
| <a name="elasticmapreduce-GetManagedScalingPolicy"></a>[GetManagedScalingPolicy](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetManagedScalingPolicy.html) | Retrieve the managed scaling policy associated with a cluster | Read | 
| <a name="elasticmapreduce-GetSession"></a>[GetSession](https://docs.aws.amazon.com/emr/latest/APIReference/API_GetSession.html) | Get details of a Spark Connect session | Read | 
| <a name="elasticmapreduce-GetStudioSessionMapping"></a>[GetStudioSessionMapping](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html) | View information about an EMR Studio session mapping | Read | 
| <a name="elasticmapreduce-ListBootstrapActions"></a>[ListBootstrapActions](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListBootstrapActions.html) | Get details about the bootstrap actions associated with a cluster | Read | 
| <a name="elasticmapreduce-ListClusters"></a>[ListClusters](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListClusters.html) | Get the status of accessible clusters | List | 
| <a name="elasticmapreduce-ListEditors"></a>[ListEditors](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html) | List summary information for accessible EMR notebooks | List | 
| <a name="elasticmapreduce-ListInstanceFleets"></a>[ListInstanceFleets](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListInstanceFleets.html) | Get details of instance fleets in a cluster | Read | 
| <a name="elasticmapreduce-ListInstanceGroups"></a>[ListInstanceGroups](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListInstanceGroups.html) | Get details of instance groups in a cluster | Read | 
| <a name="elasticmapreduce-ListInstances"></a>[ListInstances](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListInstances.html) | Get details about the Amazon EC2 instances in a cluster | Read | 
| <a name="elasticmapreduce-ListNotebookExecutions"></a>[ListNotebookExecutions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-headless.html) | List summary information for notebook executions | List | 
| <a name="elasticmapreduce-ListReleaseLabels"></a>[ListReleaseLabels](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListReleaseLabels.html) | List and filter the available EMR releases in the current region | List | 
| <a name="elasticmapreduce-ListRepositories"></a>[ListRepositories](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks.html#emr-managed-notebooks-editor) | List existing EMR notebook repositories | List | 
| <a name="elasticmapreduce-ListSecurityConfigurations"></a>[ListSecurityConfigurations](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSecurityConfigurations.html) | List available security configurations in this account by name, along with creation dates and times | List | 
| <a name="elasticmapreduce-ListSessions"></a>[ListSessions](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSessions.html) | List Spark Connect sessions on an Amazon EMR cluster | List | 
| <a name="elasticmapreduce-ListSteps"></a>[ListSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSteps.html) | List steps associated with a cluster | Read | 
| <a name="elasticmapreduce-ListStudioSessionMappings"></a>[ListStudioSessionMappings](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html) | List summary information about EMR Studio session mappings | List | 
| <a name="elasticmapreduce-ListStudios"></a>[ListStudios](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html) | List summary information about EMR Studios | List | 
| <a name="elasticmapreduce-ListSupportedInstanceTypes"></a>[ListSupportedInstanceTypes](https://docs.aws.amazon.com/emr/latest/APIReference/API_ListSupportedInstanceTypes.html) | List the Amazon EC2 instance types that an Amazon EMR release supports | List | 
| <a name="elasticmapreduce-ListWorkspaceAccessIdentities"></a>[ListWorkspaceAccessIdentities](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html) | List identities that are granted access to a workspace | List | 
| <a name="elasticmapreduce-ViewEventsFromAllClustersInConsole"></a>[ViewEventsFromAllClustersInConsole](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelasticmapreduce.html) | Use the EMR console to view events from all clusters | List | 
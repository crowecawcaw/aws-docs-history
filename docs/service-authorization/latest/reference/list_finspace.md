

# Actions, resources, and condition keys for Amazon FinSpace
<a name="list_finspace"></a>

Amazon FinSpace (service prefix: `finspace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/finspace/latest/management-api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/finspace/latest/userguide/access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/finspace/finspace.json) for this service.

**Topics**
+ [Actions defined by Amazon FinSpace](#list_finspace-actions-as-permissions)
+ [Permission-only actions for Amazon FinSpace](#list_finspace-permission-only-actions)
+ [Resource types defined by Amazon FinSpace](#list_finspace-resources-for-iam-policies)
+ [Condition keys for Amazon FinSpace](#list_finspace-policy-keys)

## Actions defined by Amazon FinSpace
<a name="list_finspace-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateEnvironment.html)  **
  - **Description:** Grants permission to create a FinSpace environment
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxChangeset](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxChangeset.html)  **
  - **Description:** Grants permission to create a changeset for a kdb database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxCluster.html)  **
  - **Description:** Grants permission to create a cluster in a managed kdb environment
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxDatabase.html)  **
  - **Description:** Grants permission to create a kdb database in a managed kdb environment
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxDataview.html)  **
  - **Description:** Grants permission to create a dataview in a managed kdb environment
  - **Resource types (\*required):** [kxDataview\*](#list_finspace-resource-kxDataview)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxEnvironment.html)  **
  - **Description:** Grants permission to create a managed kdb environment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxScalingGroup.html)  **
  - **Description:** Grants permission to create a scaling group in a managed kdb environment
  - **Resource types (\*required):** [kxScalingGroup\*](#list_finspace-resource-kxScalingGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxUser.html)  **
  - **Description:** Grants permission to create a user in a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxVolume.html)  **
  - **Description:** Grants permission to create a volume in a managed kdb environment
  - **Resource types (\*required):** [kxVolume\*](#list_finspace-resource-kxVolume)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to create a FinSpace user
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [user\*](#list_finspace-resource-user) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteEnvironment.html)  **
  - **Description:** Grants permission to delete a FinSpace environment
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxCluster.html)  **
  - **Description:** Grants permission to delete a kdb cluster
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxClusterNode](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxClusterNode.html)  **
  - **Description:** Grants permission to delete a node from a kdb cluster
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxDatabase.html)  **
  - **Description:** Grants permission to delete a kdb database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxDataview.html)  **
  - **Description:** Grants permission to delete a dataview in a managed kdb environment
  - **Resource types (\*required):** [kxDataview\*](#list_finspace-resource-kxDataview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxEnvironment.html)  **
  - **Description:** Grants permission to delete a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxScalingGroup.html)  **
  - **Description:** Grants permission to delete a scaling group in a managed kdb environment
  - **Resource types (\*required):** [kxScalingGroup\*](#list_finspace-resource-kxScalingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxUser.html)  **
  - **Description:** Grants permission to delete a kdb user
  - **Resource types (\*required):** [kxUser\*](#list_finspace-resource-kxUser)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_DeleteKxVolume.html)  **
  - **Description:** Grants permission to delete a volume in a managed kdb environment
  - **Resource types (\*required):** [kxVolume\*](#list_finspace-resource-kxVolume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetEnvironment.html)  **
  - **Description:** Grants permission to describe a FinSpace environment
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxChangeset](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxChangeset.html)  **
  - **Description:** Grants permission to describe a changeset for a kdb database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxCluster](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxCluster.html)  **
  - **Description:** Grants permission to describe a cluster in a managed kdb environment
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxConnectionString](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxConnectionString.html)  **
  - **Description:** Grants permission to retrieve a connection string for kdb clusters
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxDatabase.html)  **
  - **Description:** Grants permission to describe a kdb database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxDataview.html)  **
  - **Description:** Grants permission to describe a databiew in a managed kdb environment
  - **Resource types (\*required):** [kxDataview\*](#list_finspace-resource-kxDataview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxEnvironment.html)  **
  - **Description:** Grants permission to describe a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxScalingGroup](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxScalingGroup.html)  **
  - **Description:** Grants permission to describe a scaling group in a managed kdb environment
  - **Resource types (\*required):** [kxScalingGroup\*](#list_finspace-resource-kxScalingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxUser.html)  **
  - **Description:** Grants permission to describe a kdb user
  - **Resource types (\*required):** [kxUser\*](#list_finspace-resource-kxUser)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxVolume.html)  **
  - **Description:** Grants permission to describe a volume in a managed kdb environment
  - **Resource types (\*required):** [kxVolume\*](#list_finspace-resource-kxVolume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLoadSampleDataSetGroupIntoEnvironmentStatus](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to request status of the loading of sample data bundle
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUser](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to describe a FinSpace user
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_finspace-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEnvironments](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListEnvironments.html)  **
  - **Description:** Grants permission to list FinSpace environments in the AWS account
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxChangesets](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxChangesets.html)  **
  - **Description:** Grants permission to list changesets for a kdb database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxClusterNodes](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxClusterNodes.html)  **
  - **Description:** Grants permission to list cluster nodes in a managed kdb environment
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxClusters](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxClusters.html)  **
  - **Description:** Grants permission to list clusters in a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxDatabases](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxDatabases.html)  **
  - **Description:** Grants permission to list kdb databases in a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxDataviews](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxDataviews.html)  **
  - **Description:** Grants permission to list dataviews in a database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxEnvironments](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxEnvironments.html)  **
  - **Description:** Grants permission to list managed kdb environments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKxScalingGroups](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxScalingGroups.html)  **
  - **Description:** Grants permission to list scaling groups in a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxUsers](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxUsers.html)  **
  - **Description:** Grants permission to list users in a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKxVolumes](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListKxVolumes.html)  **
  - **Description:** Grants permission to list volumes in a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/finspace/latest/management-api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags for a resource
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxDataview\*](#list_finspace-resource-kxDataview) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxScalingGroup\*](#list_finspace-resource-kxScalingGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxUser\*](#list_finspace-resource-kxUser) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [kxVolume\*](#list_finspace-resource-kxVolume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to list FinSpace users in an environment
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_finspace-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [LoadSampleDataSetGroupIntoEnvironment](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to load sample data bundle into your FinSpace environment
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetUserPassword](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to reset the password for a FinSpace user
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_finspace-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/finspace/latest/management-api/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [environment](#list_finspace-resource-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxCluster](#list_finspace-resource-kxCluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxDatabase](#list_finspace-resource-kxDatabase) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxDataview](#list_finspace-resource-kxDataview) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxEnvironment](#list_finspace-resource-kxEnvironment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxScalingGroup](#list_finspace-resource-kxScalingGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxUser](#list_finspace-resource-kxUser) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxVolume](#list_finspace-resource-kxVolume) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_finspace-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/finspace/latest/management-api/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [environment](#list_finspace-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxCluster](#list_finspace-resource-kxCluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxDatabase](#list_finspace-resource-kxDatabase) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxDataview](#list_finspace-resource-kxDataview) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxEnvironment](#list_finspace-resource-kxEnvironment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxScalingGroup](#list_finspace-resource-kxScalingGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxUser](#list_finspace-resource-kxUser) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Resource types (\*required):** [kxVolume](#list_finspace-resource-kxVolume) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_finspace-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateEnvironment.html)  **
  - **Description:** Grants permission to update a FinSpace environment
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxClusterCodeConfiguration](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterCodeConfiguration.html)  **
  - **Description:** Grants permission to update code configuration for a cluster in a managed kdb environment
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxClusterDatabases](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxClusterDatabases.html)  **
  - **Description:** Grants permission to update databases for a cluster in a managed kdb environment
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxDatabase](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxDatabase.html)  **
  - **Description:** Grants permission to update a kdb database
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxDataview](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxDataview.html)  **
  - **Description:** Grants permission to update a dataview in a managed kdb environment
  - **Resource types (\*required):** [kxDataview\*](#list_finspace-resource-kxDataview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxEnvironment](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxEnvironment.html)  **
  - **Description:** Grants permission to update a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxEnvironmentNetwork](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxEnvironmentNetwork.html)  **
  - **Description:** Grants permission to update the network for a managed kdb environment
  - **Resource types (\*required):** [kxEnvironment\*](#list_finspace-resource-kxEnvironment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxUser](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxUser.html)  **
  - **Description:** Grants permission to update a kdb user
  - **Resource types (\*required):** [kxUser\*](#list_finspace-resource-kxUser)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKxVolume](https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxVolume.html)  **
  - **Description:** Grants permission to update a volume in a managed kdb environment
  - **Resource types (\*required):** [kxVolume\*](#list_finspace-resource-kxVolume)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-what-is.html)  **
  - **Description:** Grants permission to update a FinSpace user
  - **Resource types (\*required):** [environment\*](#list_finspace-resource-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [user\*](#list_finspace-resource-user) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon FinSpace
<a name="list_finspace-permission-only-actions"></a>

The following actions are defined by Amazon FinSpace but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ConnectKxCluster](https://docs.aws.amazon.com/finspace/latest/userguide/interacting-with-kdb-clusters.html)  **
  - **Description:** Grants permission to connect to a kdb cluster
  - **Resource types (\*required):** [kxCluster\*](#list_finspace-resource-kxCluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [MountKxDatabase](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-managed-kdb-db.html)  **
  - **Description:** Grants permission to mount a database to a kdb cluster
  - **Resource types (\*required):** [kxDatabase\*](#list_finspace-resource-kxDatabase)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon FinSpace
<a name="list_finspace-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [environment](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:environment/${EnvironmentId} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxCluster](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId}/kxCluster/${KxCluster} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxDatabase](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId}/kxDatabase/${KxDatabase} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxDataview](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId}/kxDatabase/${KxDatabase}/kxDataview/${KxDataview} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxEnvironment](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxScalingGroup](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId}/kxScalingGroup/${KxScalingGroup} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxUser](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId}/kxUser/${UserName} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [kxVolume](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:kxEnvironment/${EnvironmentId}/kxVolume/${KxVolume} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 
|  [user](https://docs.aws.amazon.com/finspace/latest/userguide/finspace-example-policies.html)  | arn:${Partition}:finspace:${Region}:${Account}:user/${UserId} | [aws:ResourceTag/${TagKey}](#list_finspace-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon FinSpace
<a name="list_finspace-policy-keys"></a>

Amazon FinSpace defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
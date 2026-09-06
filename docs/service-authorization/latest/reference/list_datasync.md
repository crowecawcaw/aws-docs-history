

# Actions, resources, and condition keys for AWS DataSync
<a name="list_datasync"></a>

AWS DataSync (service prefix: `datasync`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/datasync/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/datasync/latest/userguide/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/datasync/latest/userguide/iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/datasync/datasync.json) for this service.

**Topics**
+ [API operations defined by AWS DataSync](#list_datasync-operations)
+ [Actions defined by AWS DataSync](#list_datasync-actions-as-permissions)
+ [Resource types defined by AWS DataSync](#list_datasync-resources-for-iam-policies)
+ [Condition keys for AWS DataSync](#list_datasync-policy-keys)

## API operations defined by AWS DataSync
<a name="list_datasync-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_datasync-actions-as-permissions).




- **   CancelTaskExecution  **
  - **IAM action:**  [datasync:CancelTaskExecution](#list_datasync-action-CancelTaskExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAgent  **
  - **IAM action:**  [datasync:CreateAgent](#list_datasync-action-CreateAgent)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLocationAzureBlob  **
  - **IAM action:**  [datasync:CreateLocationAzureBlob](#list_datasync-action-CreateLocationAzureBlob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationEfs  **
  - **IAM action:**  [datasync:CreateLocationEfs](#list_datasync-action-CreateLocationEfs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationFsxLustre  **
  - **IAM action:**  [datasync:CreateLocationFsxLustre](#list_datasync-action-CreateLocationFsxLustre)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLocationFsxOntap  **
  - **IAM action:**  [datasync:CreateLocationFsxOntap](#list_datasync-action-CreateLocationFsxOntap)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationFsxOpenZfs  **
  - **IAM action:**  [datasync:CreateLocationFsxOpenZfs](#list_datasync-action-CreateLocationFsxOpenZfs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLocationFsxWindows  **
  - **IAM action:**  [datasync:CreateLocationFsxWindows](#list_datasync-action-CreateLocationFsxWindows)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationHdfs  **
  - **IAM action:**  [datasync:CreateLocationHdfs](#list_datasync-action-CreateLocationHdfs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationNfs  **
  - **IAM action:**  [datasync:CreateLocationNfs](#list_datasync-action-CreateLocationNfs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLocationObjectStorage  **
  - **IAM action:**  [datasync:CreateLocationObjectStorage](#list_datasync-action-CreateLocationObjectStorage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationS3  **
  - **IAM action:**  [datasync:CreateLocationS3](#list_datasync-action-CreateLocationS3)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateLocationSmb  **
  - **IAM action:**  [datasync:CreateLocationSmb](#list_datasync-action-CreateLocationSmb)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   CreateTask  **
  - **IAM action:**  [datasync:CreateTask](#list_datasync-action-CreateTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   DeleteAgent  **
  - **IAM action:**  [datasync:DeleteAgent](#list_datasync-action-DeleteAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLocation  **
  - **IAM action:**  [datasync:DeleteLocation](#list_datasync-action-DeleteLocation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTask  **
  - **IAM action:**  [datasync:DeleteTask](#list_datasync-action-DeleteTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAgent  **
  - **IAM action:**  [datasync:DescribeAgent](#list_datasync-action-DescribeAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationAzureBlob  **
  - **IAM action:**  [datasync:DescribeLocationAzureBlob](#list_datasync-action-DescribeLocationAzureBlob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationEfs  **
  - **IAM action:**  [datasync:DescribeLocationEfs](#list_datasync-action-DescribeLocationEfs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationFsxLustre  **
  - **IAM action:**  [datasync:DescribeLocationFsxLustre](#list_datasync-action-DescribeLocationFsxLustre) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationFsxOntap  **
  - **IAM action:**  [datasync:DescribeLocationFsxOntap](#list_datasync-action-DescribeLocationFsxOntap) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationFsxOpenZfs  **
  - **IAM action:**  [datasync:DescribeLocationFsxOpenZfs](#list_datasync-action-DescribeLocationFsxOpenZfs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationFsxWindows  **
  - **IAM action:**  [datasync:DescribeLocationFsxWindows](#list_datasync-action-DescribeLocationFsxWindows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationHdfs  **
  - **IAM action:**  [datasync:DescribeLocationHdfs](#list_datasync-action-DescribeLocationHdfs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationNfs  **
  - **IAM action:**  [datasync:DescribeLocationNfs](#list_datasync-action-DescribeLocationNfs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationObjectStorage  **
  - **IAM action:**  [datasync:DescribeLocationObjectStorage](#list_datasync-action-DescribeLocationObjectStorage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationS3  **
  - **IAM action:**  [datasync:DescribeLocationS3](#list_datasync-action-DescribeLocationS3) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeLocationSmb  **
  - **IAM action:**  [datasync:DescribeLocationSmb](#list_datasync-action-DescribeLocationSmb) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTask  **
  - **IAM action:**  [datasync:DescribeTask](#list_datasync-action-DescribeTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTaskExecution  **
  - **IAM action:**  [datasync:DescribeTaskExecution](#list_datasync-action-DescribeTaskExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgents  **
  - **IAM action:**  [datasync:ListAgents](#list_datasync-action-ListAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLocations  **
  - **IAM action:**  [datasync:ListLocations](#list_datasync-action-ListLocations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [datasync:ListTagsForResource](#list_datasync-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTaskExecutions  **
  - **IAM action:**  [datasync:ListTaskExecutions](#list_datasync-action-ListTaskExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTasks  **
  - **IAM action:**  [datasync:ListTasks](#list_datasync-action-ListTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartTaskExecution  **
  - **IAM action:**  [datasync:StartTaskExecution](#list_datasync-action-StartTaskExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [datasync:TagResource](#list_datasync-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [datasync:UntagResource](#list_datasync-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAgent  **
  - **IAM action:**  [datasync:UpdateAgent](#list_datasync-action-UpdateAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLocationAzureBlob  **
  - **IAM action:**  [datasync:UpdateLocationAzureBlob](#list_datasync-action-UpdateLocationAzureBlob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationEfs  **
  - **IAM action:**  [datasync:UpdateLocationEfs](#list_datasync-action-UpdateLocationEfs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationFsxLustre  **
  - **IAM action:**  [datasync:UpdateLocationFsxLustre](#list_datasync-action-UpdateLocationFsxLustre) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLocationFsxOntap  **
  - **IAM action:**  [datasync:UpdateLocationFsxOntap](#list_datasync-action-UpdateLocationFsxOntap)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationFsxOpenZfs  **
  - **IAM action:**  [datasync:UpdateLocationFsxOpenZfs](#list_datasync-action-UpdateLocationFsxOpenZfs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLocationFsxWindows  **
  - **IAM action:**  [datasync:UpdateLocationFsxWindows](#list_datasync-action-UpdateLocationFsxWindows)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationHdfs  **
  - **IAM action:**  [datasync:UpdateLocationHdfs](#list_datasync-action-UpdateLocationHdfs)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationNfs  **
  - **IAM action:**  [datasync:UpdateLocationNfs](#list_datasync-action-UpdateLocationNfs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLocationObjectStorage  **
  - **IAM action:**  [datasync:UpdateLocationObjectStorage](#list_datasync-action-UpdateLocationObjectStorage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationS3  **
  - **IAM action:**  [datasync:UpdateLocationS3](#list_datasync-action-UpdateLocationS3)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateLocationSmb  **
  - **IAM action:**  [datasync:UpdateLocationSmb](#list_datasync-action-UpdateLocationSmb)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateTask  **
  - **IAM action:**  [datasync:UpdateTask](#list_datasync-action-UpdateTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datasync.amazonaws.com / **Access level:** Write

- **   UpdateTaskExecution  **
  - **IAM action:**  [datasync:UpdateTaskExecution](#list_datasync-action-UpdateTaskExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS DataSync
<a name="list_datasync-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddStorageSystem](https://docs.aws.amazon.com/datasync/latest/userguide/API_AddStorageSystem.html)  **
  - **Description:** Grants permission to create a storage system
  - **Resource types (\*required):** [agent\*](#list_datasync-resource-agent)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CancelTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_CancelTaskExecution.html)  **
  - **Description:** Grants permission to cancel execution of a sync task
  - **Resource types (\*required):** [taskexecution\*](#list_datasync-resource-taskexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateAgent.html)  **
  - **Description:** Grants permission to activate an agent that you have deployed on your host
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationAzureBlob.html)  **
  - **Description:** Grants permission to create an endpoint for a Microsoft Azure Blob Storage container
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationEfs.html)  **
  - **Description:** Grants permission to create an endpoint for an Amazon EFS file system
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxLustre.html)  **
  - **Description:** Grants permission to create an endpoint for an Amazon Fsx Lustre
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html)  **
  - **Description:** Grants permission to create an endpoint for Amazon FSx for ONTAP
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOpenZfs.html)  **
  - **Description:** Grants permission to create an endpoint for Amazon FSx for OpenZFS
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxWindows.html)  **
  - **Description:** Grants permission to create an endpoint for an Amazon FSx Windows File Server file system
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationHdfs.html)  **
  - **Description:** Grants permission to create an endpoint for an Amazon Hdfs
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationNfs.html)  **
  - **Description:** Grants permission to create an endpoint for a NFS file system
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationObjectStorage.html)  **
  - **Description:** Grants permission to create an endpoint for a self-managed object storage bucket
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationS3.html)  **
  - **Description:** Grants permission to create an endpoint for an Amazon S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationSmb.html)  **
  - **Description:** Grants permission to create an endpoint for an SMB file system
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html)  **
  - **Description:** Grants permission to create a sync task
  - **Resource types (\*required):** [agent](#list_datasync-resource-agent) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_DeleteAgent.html)  **
  - **Description:** Grants permission to delete an agent
  - **Resource types (\*required):** [agent\*](#list_datasync-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLocation](https://docs.aws.amazon.com/datasync/latest/userguide/API_DeleteLocation.html)  **
  - **Description:** Grants permission to delete a location used by AWS DataSync
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_DeleteTask.html)  **
  - **Description:** Grants permission to delete a sync task
  - **Resource types (\*required):** [task\*](#list_datasync-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeAgent.html)  **
  - **Description:** Grants permission to view metadata such as name, network interfaces, and the status (that is, whether the agent is running or not) about a sync agent
  - **Resource types (\*required):** [agent\*](#list_datasync-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDiscoveryJob](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeDiscoveryJob.html)  **
  - **Description:** Grants permission to describe metadata about a discovery job
  - **Resource types (\*required):** [discoveryjob\*](#list_datasync-resource-discoveryjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationAzureBlob.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Azure Blob Storage sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationEfs.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Amazon EFS sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxLustre.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Amazon FSx Lustre sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxOntap.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Amazon FSx for ONTAP sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxOpenZfs.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Amazon FSx OpenZFS sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxWindows.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Amazon FSx Windows sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationHdfs.html)  **
  - **Description:** Grants permission to view metadata, such as the path information about an Amazon HDFS sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationNfs.html)  **
  - **Description:** Grants permission to view metadata, such as the path information, about a NFS sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationObjectStorage.html)  **
  - **Description:** Grants permission to view metadata about a self-managed object storage server location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationS3.html)  **
  - **Description:** Grants permission to view metadata, such as bucket name, about an Amazon S3 bucket sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationSmb.html)  **
  - **Description:** Grants permission to view metadata, such as the path information, about an SMB sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStorageSystem](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystem.html)  **
  - **Description:** Grants permission to view metadata about a storage system
  - **Resource types (\*required):** [storagesystem\*](#list_datasync-resource-storagesystem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeStorageSystemResourceMetrics](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResourceMetrics.html)  **
  - **Description:** Grants permission to describe resource metrics collected by a discovery job
  - **Resource types (\*required):** [discoveryjob\*](#list_datasync-resource-discoveryjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeStorageSystemResources](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeStorageSystemResources.html)  **
  - **Description:** Grants permission to describe resources identified by a discovery job
  - **Resource types (\*required):** [discoveryjob\*](#list_datasync-resource-discoveryjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTask.html)  **
  - **Description:** Grants permission to view metadata about a sync task
  - **Resource types (\*required):** [task\*](#list_datasync-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html)  **
  - **Description:** Grants permission to view metadata about a sync task that is being executed
  - **Resource types (\*required):** [taskexecution\*](#list_datasync-resource-taskexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GenerateRecommendations](https://docs.aws.amazon.com/datasync/latest/userguide/API_GenerateRecommendations.html)  **
  - **Description:** Grants permission to generate recommendations for a resource identified by a discovery job
  - **Resource types (\*required):** [discoveryjob\*](#list_datasync-resource-discoveryjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAgents](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListAgents.html)  **
  - **Description:** Grants permission to list agents owned by an AWS account in a region specified in the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDiscoveryJobs](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListDiscoveryJobs.html)  **
  - **Description:** Grants permission to list discovery jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLocations](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListLocations.html)  **
  - **Description:** Grants permission to list source and destination sync locations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListStorageSystems](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListStorageSystems.html)  **
  - **Description:** Grants permission to list storage systems
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags that have been added to the specified resource
  - **Resource types (\*required):** [agent](#list_datasync-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [discoveryjob](#list_datasync-resource-discoveryjob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [location](#list_datasync-resource-location) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [storagesystem](#list_datasync-resource-storagesystem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [task](#list_datasync-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [taskexecution](#list_datasync-resource-taskexecution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTaskExecutions](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTaskExecutions.html)  **
  - **Description:** Grants permission to list executed sync tasks
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTasks](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTasks.html)  **
  - **Description:** Grants permission to list of all the sync tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RemoveStorageSystem](https://docs.aws.amazon.com/datasync/latest/userguide/API_RemoveStorageSystem.html)  **
  - **Description:** Grants permission to delete a storage system
  - **Resource types (\*required):** [storagesystem\*](#list_datasync-resource-storagesystem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDiscoveryJob](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartDiscoveryJob.html)  **
  - **Description:** Grants permission to start a discovery job for a storage system
  - **Resource types (\*required):** [storagesystem\*](#list_datasync-resource-storagesystem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html)  **
  - **Description:** Grants permission to start a specific invocation of a sync task
  - **Resource types (\*required):** [task\*](#list_datasync-resource-task)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Write

- **   [StopDiscoveryJob](https://docs.aws.amazon.com/datasync/latest/userguide/API_StopDiscoveryJob.html)  **
  - **Description:** Grants permission to stop a discovery job
  - **Resource types (\*required):** [discoveryjob\*](#list_datasync-resource-discoveryjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_TagResource.html)  **
  - **Description:** Grants permission to apply a key-value pair to an AWS resource
  - **Resource types (\*required):** [agent](#list_datasync-resource-agent) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [discoveryjob](#list_datasync-resource-discoveryjob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [location](#list_datasync-resource-location) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [storagesystem](#list_datasync-resource-storagesystem) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_datasync-resource-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [taskexecution](#list_datasync-resource-taskexecution) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_datasync-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from the specified resource
  - **Resource types (\*required):** [agent](#list_datasync-resource-agent) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [discoveryjob](#list_datasync-resource-discoveryjob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [location](#list_datasync-resource-location) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [storagesystem](#list_datasync-resource-storagesystem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [task](#list_datasync-resource-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Resource types (\*required):** [taskexecution](#list_datasync-resource-taskexecution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datasync-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateAgent.html)  **
  - **Description:** Grants permission to update the name of an agent
  - **Resource types (\*required):** [agent\*](#list_datasync-resource-agent)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDiscoveryJob](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateDiscoveryJob.html)  **
  - **Description:** Grants permission to update a discovery job
  - **Resource types (\*required):** [discoveryjob\*](#list_datasync-resource-discoveryjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationAzureBlob.html)  **
  - **Description:** Grants permission to update an Azure Blob Storage sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationEfs.html)  **
  - **Description:** Grants permission to update an EFS sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxLustre.html)  **
  - **Description:** Grants permission to update an FSx Lustre sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxOntap.html)  **
  - **Description:** Grants permission to update an FSx ONTAP sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxOpenZfs.html)  **
  - **Description:** Grants permission to update an FSx OpenZFS sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxWindows.html)  **
  - **Description:** Grants permission to update an FSx Windows sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationHdfs.html)  **
  - **Description:** Grants permission to update an HDFS sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationNfs.html)  **
  - **Description:** Grants permission to update an NFS sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationObjectStorage.html)  **
  - **Description:** Grants permission to update a self-managed object storage server location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationS3.html)  **
  - **Description:** Grants permission to update an S3 sync Location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationSmb.html)  **
  - **Description:** Grants permission to update a SMB sync location
  - **Resource types (\*required):** [location\*](#list_datasync-resource-location)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStorageSystem](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateStorageSystem.html)  **
  - **Description:** Grants permission to update a storage system
  - **Resource types (\*required):** [storagesystem\*](#list_datasync-resource-storagesystem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html)  **
  - **Description:** Grants permission to update metadata associated with a sync task
  - **Resource types (\*required):** [task\*](#list_datasync-resource-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTaskExecution.html)  **
  - **Description:** Grants permission to update execution of a sync task
  - **Resource types (\*required):** [taskexecution\*](#list_datasync-resource-taskexecution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS DataSync
<a name="list_datasync-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agent](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-agents.html)  | arn:${Partition}:datasync:${Region}:${AccountId}:agent/${AgentId} | [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_) | 
|  [discoveryjob](https://docs.aws.amazon.com/datasync/latest/userguide/discovery-job-create.html)  | arn:${Partition}:datasync:${Region}:${AccountId}:system/${StorageSystemId}/job/${DiscoveryJobId} | [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_) | 
|  [location](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html)  | arn:${Partition}:datasync:${Region}:${AccountId}:location/${LocationId} | [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_) | 
|  [storagesystem](https://docs.aws.amazon.com/datasync/latest/userguide/discovery-configure-storage.html)  | arn:${Partition}:datasync:${Region}:${AccountId}:system/${StorageSystemId} | [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_) | 
|  [task](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-tasks.html)  | arn:${Partition}:datasync:${Region}:${AccountId}:task/${TaskId} | [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_) | 
|  [taskexecution](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-task-executions.html)  | arn:${Partition}:datasync:${Region}:${AccountId}:task/${TaskId}/execution/${ExecutionId} | [aws:ResourceTag/${TagKey}](#list_datasync-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS DataSync
<a name="list_datasync-policy-keys"></a>

AWS DataSync defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in the request | ArrayOfString | 


# Actions, resources, and condition keys for AWS Batch
<a name="list_batch"></a>

AWS Batch (service prefix: `batch`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/batch/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/batch/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/batch/latest/userguide/IAM_policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/batch/batch.json) for this service.

**Topics**
+ [API operations defined by AWS Batch](#list_batch-operations)
+ [Actions defined by AWS Batch](#list_batch-actions-as-permissions)
+ [Permission-only actions for AWS Batch](#list_batch-permission-only-actions)
+ [Resource types defined by AWS Batch](#list_batch-resources-for-iam-policies)
+ [Condition keys for AWS Batch](#list_batch-policy-keys)

## API operations defined by AWS Batch
<a name="list_batch-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_batch-actions-as-permissions).




- **   CancelJob  **
  - **IAM action:**  [batch:CancelJob](#list_batch-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateComputeEnvironment  **
  - **IAM action:**  [batch:CreateComputeEnvironment](#list_batch-action-CreateComputeEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:SetCapacityTags](#list_batch-action-SetCapacityTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** batch.amazonaws.com, ec2.amazonaws.com, ecs.amazonaws.com, spotfleet.amazonaws.com / **Access level:** Write

- **   CreateConsumableResource  **
  - **IAM action:**  [batch:CreateConsumableResource](#list_batch-action-CreateConsumableResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateJobQueue  **
  - **IAM action:**  [batch:CreateJobQueue](#list_batch-action-CreateJobQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateQuotaShare  **
  - **IAM action:**  [batch:CreateQuotaShare](#list_batch-action-CreateQuotaShare)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSchedulingPolicy  **
  - **IAM action:**  [batch:CreateSchedulingPolicy](#list_batch-action-CreateSchedulingPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServiceEnvironment  **
  - **IAM action:**  [batch:CreateServiceEnvironment](#list_batch-action-CreateServiceEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteComputeEnvironment  **
  - **IAM action:**  [batch:DeleteComputeEnvironment](#list_batch-action-DeleteComputeEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConsumableResource  **
  - **IAM action:**  [batch:DeleteConsumableResource](#list_batch-action-DeleteConsumableResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteJobQueue  **
  - **IAM action:**  [batch:DeleteJobQueue](#list_batch-action-DeleteJobQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQuotaShare  **
  - **IAM action:**  [batch:DeleteQuotaShare](#list_batch-action-DeleteQuotaShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchedulingPolicy  **
  - **IAM action:**  [batch:DeleteSchedulingPolicy](#list_batch-action-DeleteSchedulingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServiceEnvironment  **
  - **IAM action:**  [batch:DeleteServiceEnvironment](#list_batch-action-DeleteServiceEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterJobDefinition  **
  - **IAM action:**  [batch:DeregisterJobDefinition](#list_batch-action-DeregisterJobDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeComputeEnvironments  **
  - **IAM action:**  [batch:DescribeComputeEnvironments](#list_batch-action-DescribeComputeEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeConsumableResource  **
  - **IAM action:**  [batch:DescribeConsumableResource](#list_batch-action-DescribeConsumableResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobDefinitions  **
  - **IAM action:**  [batch:DescribeJobDefinitions](#list_batch-action-DescribeJobDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobQueues  **
  - **IAM action:**  [batch:DescribeJobQueues](#list_batch-action-DescribeJobQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeJobs  **
  - **IAM action:**  [batch:DescribeJobs](#list_batch-action-DescribeJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeQuotaShare  **
  - **IAM action:**  [batch:DescribeQuotaShare](#list_batch-action-DescribeQuotaShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSchedulingPolicies  **
  - **IAM action:**  [batch:DescribeSchedulingPolicies](#list_batch-action-DescribeSchedulingPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceEnvironments  **
  - **IAM action:**  [batch:DescribeServiceEnvironments](#list_batch-action-DescribeServiceEnvironments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeServiceJob  **
  - **IAM action:**  [batch:DescribeServiceJob](#list_batch-action-DescribeServiceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobQueueSnapshot  **
  - **IAM action:**  [batch:GetJobQueueSnapshot](#list_batch-action-GetJobQueueSnapshot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConsumableResources  **
  - **IAM action:**  [batch:ListConsumableResources](#list_batch-action-ListConsumableResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobs  **
  - **IAM action:**  [batch:ListJobs](#list_batch-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListJobsByConsumableResource  **
  - **IAM action:**  [batch:ListJobsByConsumableResource](#list_batch-action-ListJobsByConsumableResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQuotaShares  **
  - **IAM action:**  [batch:ListQuotaShares](#list_batch-action-ListQuotaShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchedulingPolicies  **
  - **IAM action:**  [batch:ListSchedulingPolicies](#list_batch-action-ListSchedulingPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListServiceJobs  **
  - **IAM action:**  [batch:ListServiceJobs](#list_batch-action-ListServiceJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [batch:ListTagsForResource](#list_batch-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterJobDefinition  **
  - **IAM action:**  [batch:RegisterJobDefinition](#list_batch-action-RegisterJobDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** ecs-tasks.amazonaws.com / **Access level:** Write

- **   SubmitJob  **
  - **IAM action:**  [batch:SubmitJob](#list_batch-action-SubmitJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   SubmitServiceJob  **
  - **IAM action:**  [batch:SubmitServiceJob](#list_batch-action-SubmitServiceJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sagemaker.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [batch:TagResource](#list_batch-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateJob  **
  - **IAM action:**  [batch:TerminateJob](#list_batch-action-TerminateJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TerminateServiceJob  **
  - **IAM action:**  [batch:TerminateServiceJob](#list_batch-action-TerminateServiceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [batch:UntagResource](#list_batch-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateComputeEnvironment  **
  - **IAM action:**  [batch:UpdateComputeEnvironment](#list_batch-action-UpdateComputeEnvironment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** batch.amazonaws.com, ec2.amazonaws.com, ecs.amazonaws.com / **Access level:** Write

- **   UpdateConsumableResource  **
  - **IAM action:**  [batch:UpdateConsumableResource](#list_batch-action-UpdateConsumableResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateJobQueue  **
  - **IAM action:**  [batch:UpdateJobQueue](#list_batch-action-UpdateJobQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQuotaShare  **
  - **IAM action:**  [batch:UpdateQuotaShare](#list_batch-action-UpdateQuotaShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSchedulingPolicy  **
  - **IAM action:**  [batch:UpdateSchedulingPolicy](#list_batch-action-UpdateSchedulingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceEnvironment  **
  - **IAM action:**  [batch:UpdateServiceEnvironment](#list_batch-action-UpdateServiceEnvironment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceJob  **
  - **IAM action:**  [batch:UpdateServiceJob](#list_batch-action-UpdateServiceJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Batch
<a name="list_batch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_CancelJob.html)  **
  - **Description:** Grants permission to cancel a job in an AWS Batch job queue in your account
  - **Resource types (\*required):** [job\*](#list_batch-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html)  **
  - **Description:** Grants permission to create an AWS Batch compute environment in your account
  - **Resource types (\*required):** [compute-environment\*](#list_batch-resource-compute-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConsumableResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateConsumableResource.html)  **
  - **Description:** Grants permission to create an AWS Batch consumable resource in your account
  - **Resource types (\*required):** [consumable-resource\*](#list_batch-resource-consumable-resource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [CreateJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateJobQueue.html)  **
  - **Description:** Grants permission to create an AWS Batch job queue in your account
  - **Resource types (\*required):** [compute-environment](#list_batch-resource-compute-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [scheduling-policy](#list_batch-resource-scheduling-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [service-environment](#list_batch-resource-service-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQuotaShare](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateQuotaShare.html)  **
  - **Description:** Grants permission to create an AWS Batch quota share in your account
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [quota-share\*](#list_batch-resource-quota-share) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSchedulingPolicy](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateSchedulingPolicy.html)  **
  - **Description:** Grants permission to create an AWS Batch scheduling policy in your account
  - **Resource types (\*required):** [scheduling-policy\*](#list_batch-resource-scheduling-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServiceEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateServiceEnvironment.html)  **
  - **Description:** Grants permission to create an AWS Batch service environment in your account
  - **Resource types (\*required):** [service-environment\*](#list_batch-resource-service-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeleteComputeEnvironment.html)  **
  - **Description:** Grants permission to delete an AWS Batch compute environment in your account
  - **Resource types (\*required):** [compute-environment\*](#list_batch-resource-compute-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConsumableResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeleteConsumableResource.html)  **
  - **Description:** Grants permission to delete an AWS Batch consumable resource in your account
  - **Resource types (\*required):** [consumable-resource\*](#list_batch-resource-consumable-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeleteJobQueue.html)  **
  - **Description:** Grants permission to delete an AWS Batch job queue in your account
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQuotaShare](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeleteQuotaShare.html)  **
  - **Description:** Grants permission to delete an AWS Batch quota share in your account
  - **Resource types (\*required):** [quota-share\*](#list_batch-resource-quota-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchedulingPolicy](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeleteSchedulingPolicy.html)  **
  - **Description:** Grants permission to delete an AWS Batch scheduling policy in your account
  - **Resource types (\*required):** [scheduling-policy\*](#list_batch-resource-scheduling-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServiceEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeleteServiceEnvironment.html)  **
  - **Description:** Grants permission to delete an AWS Batch service environment in your account
  - **Resource types (\*required):** [service-environment\*](#list_batch-resource-service-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterJobDefinition](https://docs.aws.amazon.com/batch/latest/APIReference/API_DeregisterJobDefinition.html)  **
  - **Description:** Grants permission to deregister an AWS Batch job definition in your account
  - **Resource types (\*required):** [job-definition-revision\*](#list_batch-resource-job-definition-revision)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeComputeEnvironments](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeComputeEnvironments.html)  **
  - **Description:** Grants permission to describe one or more AWS Batch compute environments in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeConsumableResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeConsumableResource.html)  **
  - **Description:** Grants permission to describe one or more AWS Batch consumable resource in your account
  - **Resource types (\*required):** [consumable-resource\*](#list_batch-resource-consumable-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeJobDefinitions](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobDefinitions.html)  **
  - **Description:** Grants permission to describe one or more AWS Batch job definitions in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeJobQueues](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobQueues.html)  **
  - **Description:** Grants permission to describe one or more AWS Batch job queues in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeJobs.html)  **
  - **Description:** Grants permission to describe a list of AWS Batch jobs in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeQuotaShare](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeQuotaShare.html)  **
  - **Description:** Grants permission to describe an AWS Batch quota share in your account
  - **Resource types (\*required):** [quota-share\*](#list_batch-resource-quota-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSchedulingPolicies](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeSchedulingPolicies.html)  **
  - **Description:** Grants permission to describe one or more AWS Batch scheduling policies in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceEnvironments](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceEnvironments.html)  **
  - **Description:** Grants permission to describe one or more AWS Batch service environments in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html)  **
  - **Description:** Grants permission to describe a AWS Batch service job in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJobQueueSnapshot](https://docs.aws.amazon.com/batch/latest/APIReference/API_GetJobQueueSnapshot.html)  **
  - **Description:** Grants permission to get a snapshot of an AWS Batch job queue in your account
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListConsumableResources](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListConsumableResources.html)  **
  - **Description:** Grants permission to list AWS Batch consumable resources in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListJobs.html)  **
  - **Description:** Grants permission to list jobs for a specified AWS Batch job queue in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListJobsByConsumableResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListJobsByConsumableResource.html)  **
  - **Description:** Grants permission to list AWS Batch jobs that require a specific consumable resource in your account
  - **Resource types (\*required):** [consumable-resource\*](#list_batch-resource-consumable-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListQuotaShares](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListQuotaShares.html)  **
  - **Description:** Grants permission to list AWS Batch quota shares in your account
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSchedulingPolicies](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListSchedulingPolicies.html)  **
  - **Description:** Grants permission to list AWS Batch scheduling policies in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListServiceJobs](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListServiceJobs.html)  **
  - **Description:** Grants permission to list service jobs for a specified AWS Batch job queue in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an AWS Batch resource in your account
  - **Resource types (\*required):** [compute-environment](#list_batch-resource-compute-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [consumable-resource](#list_batch-resource-consumable-resource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job](#list_batch-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job-definition-revision](#list_batch-resource-job-definition-revision) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job-queue](#list_batch-resource-job-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [quota-share](#list_batch-resource-quota-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [scheduling-policy](#list_batch-resource-scheduling-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-environment](#list_batch-resource-service-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [service-job](#list_batch-resource-service-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RegisterJobDefinition](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)  **
  - **Description:** Grants permission to register an AWS Batch job definition in your account
  - **Resource types (\*required):** [consumable-resource](#list_batch-resource-consumable-resource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)<br />[batch:AWSLogsCreateGroup](#list_batch-batch_AWSLogsCreateGroup)<br />[batch:AWSLogsGroup](#list_batch-batch_AWSLogsGroup)<br />[batch:AWSLogsRegion](#list_batch-batch_AWSLogsRegion)<br />[batch:AWSLogsStreamPrefix](#list_batch-batch_AWSLogsStreamPrefix)<br />[batch:EKSImage](#list_batch-batch_EKSImage)<br />[batch:EKSNamespace](#list_batch-batch_EKSNamespace)<br />[batch:EKSPrivileged](#list_batch-batch_EKSPrivileged)<br />[batch:EKSRunAsGroup](#list_batch-batch_EKSRunAsGroup)<br />[batch:EKSRunAsUser](#list_batch-batch_EKSRunAsUser)<br />[batch:EKSServiceAccountName](#list_batch-batch_EKSServiceAccountName)<br />[batch:Image](#list_batch-batch_Image)<br />[batch:LogDriver](#list_batch-batch_LogDriver)<br />[batch:Privileged](#list_batch-batch_Privileged)<br />[batch:User](#list_batch-batch_User)
  - **Resource types (\*required):** [job-definition\*](#list_batch-resource-job-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)<br />[batch:AWSLogsCreateGroup](#list_batch-batch_AWSLogsCreateGroup)<br />[batch:AWSLogsGroup](#list_batch-batch_AWSLogsGroup)<br />[batch:AWSLogsRegion](#list_batch-batch_AWSLogsRegion)<br />[batch:AWSLogsStreamPrefix](#list_batch-batch_AWSLogsStreamPrefix)<br />[batch:EKSImage](#list_batch-batch_EKSImage)<br />[batch:EKSNamespace](#list_batch-batch_EKSNamespace)<br />[batch:EKSPrivileged](#list_batch-batch_EKSPrivileged)<br />[batch:EKSRunAsGroup](#list_batch-batch_EKSRunAsGroup)<br />[batch:EKSRunAsUser](#list_batch-batch_EKSRunAsUser)<br />[batch:EKSServiceAccountName](#list_batch-batch_EKSServiceAccountName)<br />[batch:Image](#list_batch-batch_Image)<br />[batch:LogDriver](#list_batch-batch_LogDriver)<br />[batch:Privileged](#list_batch-batch_Privileged)<br />[batch:User](#list_batch-batch_User)
  - **Access level:** Write

- **   [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html)  **
  - **Description:** Grants permission to submit an AWS Batch job from a job definition in your account
  - **Resource types (\*required):** [consumable-resource](#list_batch-resource-consumable-resource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job\*](#list_batch-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)<br />[batch:EKSImage](#list_batch-batch_EKSImage)<br />[batch:EKSNamespace](#list_batch-batch_EKSNamespace)<br />[batch:ShareIdentifier](#list_batch-batch_ShareIdentifier)
  - **Resource types (\*required):** [job-definition](#list_batch-resource-job-definition) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-definition-revision](#list_batch-resource-job-definition-revision) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Write

- **   [SubmitServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitServiceJob.html)  **
  - **Description:** Grants permission to submit an AWS Batch service job
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)<br />[batch:SchedulingPriority](#list_batch-batch_SchedulingPriority)
  - **Resource types (\*required):** [quota-share](#list_batch-resource-quota-share) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)<br />[batch:SchedulingPriority](#list_batch-batch_SchedulingPriority)
  - **Resource types (\*required):** [service-job\*](#list_batch-resource-service-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)<br />[batch:SchedulingPriority](#list_batch-batch_SchedulingPriority)<br />[batch:ShareIdentifier](#list_batch-batch_ShareIdentifier)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AWS Batch resource in your account
  - **Resource types (\*required):** [compute-environment](#list_batch-resource-compute-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [consumable-resource](#list_batch-resource-consumable-resource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job](#list_batch-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-definition-revision](#list_batch-resource-job-definition-revision) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-queue](#list_batch-resource-job-queue) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [quota-share](#list_batch-resource-quota-share) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [scheduling-policy](#list_batch-resource-scheduling-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [service-environment](#list_batch-resource-service-environment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [service-job](#list_batch-resource-service-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_TerminateJob.html)  **
  - **Description:** Grants permission to terminate a job in an AWS Batch job queue in your account
  - **Resource types (\*required):** [job\*](#list_batch-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TerminateServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_TerminateServiceJob.html)  **
  - **Description:** Grants permission to terminate a service job in an AWS Batch job queue in your account
  - **Resource types (\*required):** [service-job\*](#list_batch-resource-service-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an AWS Batch resource in your account
  - **Resource types (\*required):** [compute-environment](#list_batch-resource-compute-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [consumable-resource](#list_batch-resource-consumable-resource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job](#list_batch-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-definition-revision](#list_batch-resource-job-definition-revision) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [job-queue](#list_batch-resource-job-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [quota-share](#list_batch-resource-quota-share) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [scheduling-policy](#list_batch-resource-scheduling-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [service-environment](#list_batch-resource-service-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Resource types (\*required):** [service-job](#list_batch-resource-service-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html)  **
  - **Description:** Grants permission to update an AWS Batch compute environment in your account
  - **Resource types (\*required):** [compute-environment\*](#list_batch-resource-compute-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConsumableResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateConsumableResource.html)  **
  - **Description:** Grants permission to update an AWS Batch consumable resource in your account
  - **Resource types (\*required):** [consumable-resource\*](#list_batch-resource-consumable-resource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateJobQueue.html)  **
  - **Description:** Grants permission to update an AWS Batch job queue in your account
  - **Resource types (\*required):** [compute-environment](#list_batch-resource-compute-environment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [job-queue\*](#list_batch-resource-job-queue) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [scheduling-policy](#list_batch-resource-scheduling-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQuotaShare](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateQuotaShare.html)  **
  - **Description:** Grants permission to update an AWS Batch quota share in your account
  - **Resource types (\*required):** [quota-share\*](#list_batch-resource-quota-share)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSchedulingPolicy](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateSchedulingPolicy.html)  **
  - **Description:** Grants permission to update an AWS Batch scheduling policy in your account
  - **Resource types (\*required):** [scheduling-policy\*](#list_batch-resource-scheduling-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateServiceEnvironment.html)  **
  - **Description:** Grants permission to update an AWS Batch service environment in your account
  - **Resource types (\*required):** [service-environment\*](#list_batch-resource-service-environment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateServiceJob.html)  **
  - **Description:** Grants permission to update a service job in an AWS Batch job queue in your account
  - **Resource types (\*required):** [service-job\*](#list_batch-resource-service-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[batch:SchedulingPriority](#list_batch-batch_SchedulingPriority)
  - **Access level:** Write



## Permission-only actions for AWS Batch
<a name="list_batch-permission-only-actions"></a>

The following actions are defined by AWS Batch but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [SetCapacityTags](IAM_policies.html)  **
  - **Description:** Grants permission to set capacity tags on an AWS Batch compute environment in your account
  - **Resource types (\*required):** [compute-environment\*](#list_batch-resource-compute-environment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_batch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_batch-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Batch
<a name="list_batch-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [compute-environment](https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html)  | arn:${Partition}:batch:${Region}:${Account}:compute-environment/${ComputeEnvironmentName} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [consumable-resource](https://docs.aws.amazon.com/batch/latest/userguide/resource-aware-scheduling.html)  | arn:${Partition}:batch:${Region}:${Account}:consumable-resource/${ConsumableResourceName} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [job](https://docs.aws.amazon.com/batch/latest/userguide/jobs.html)  | arn:${Partition}:batch:${Region}:${Account}:job/${JobId} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [job-definition](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html)  | arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName} |   | 
|  [job-definition-revision](https://docs.aws.amazon.com/batch/latest/userguide/job_definitions.html)  | arn:${Partition}:batch:${Region}:${Account}:job-definition/${JobDefinitionName}:${Revision} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [job-queue](https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html)  | arn:${Partition}:batch:${Region}:${Account}:job-queue/${JobQueueName} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [quota-share](https://docs.aws.amazon.com/batch/latest/userguide/quota-shares.html)  | arn:${Partition}:batch:${Region}:${Account}:job-queue/${JobQueueName}/quota-share/${QuotaShareName} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [scheduling-policy](https://docs.aws.amazon.com/batch/latest/userguide/scheduling-policies.html)  | arn:${Partition}:batch:${Region}:${Account}:scheduling-policy/${SchedulingPolicyName} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [service-environment](https://docs.aws.amazon.com/batch/latest/userguide/service-environments.html)  | arn:${Partition}:batch:${Region}:${Account}:service-environment/${ServiceEnvironmentName} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 
|  [service-job](https://docs.aws.amazon.com/batch/latest/userguide/service-jobs.html)  | arn:${Partition}:batch:${Region}:${Account}:service-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_batch-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Batch
<a name="list_batch-policy-keys"></a>

AWS Batch defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [batch:AWSLogsCreateGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the specified logging driver to determine whether awslogs group will be created for the logs | Bool | 
|   [batch:AWSLogsGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the awslogs group where the logs are located | String | 
|   [batch:AWSLogsRegion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the region where the logs are sent to | String | 
|   [batch:AWSLogsStreamPrefix](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the awslogs log stream prefix | String | 
|   [batch:EKSImage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the image used to start a container for an Amazon EKS job | String | 
|   [batch:EKSNamespace](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the namespace of a cluster used to run the pod for an Amazon EKS job | String | 
|   [batch:EKSPrivileged](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the specified privileged parameter value that determines whether the container is given elevated privileges on the host container instance (similar to the root user) for an Amazon EKS job | Bool | 
|   [batch:EKSRunAsGroup](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the specified group numeric ID (gid) used to start a container in an Amazon EKS job | Numeric | 
|   [batch:EKSRunAsUser](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the specified user numeric ID (uid) used to start a a container in an Amazon EKS job | Numeric | 
|   [batch:EKSServiceAccountName](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the name of the service account used to run the pod for an Amazon EKS job | String | 
|   [batch:Image](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the image used to start a container | String | 
|   [batch:LogDriver](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the log driver used for the container | String | 
|   [batch:Privileged](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the specified privileged parameter value that determines whether the container is given elevated privileges on the host container instance (similar to the root user) | Bool | 
|   [batch:SchedulingPriority](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the scheduling priority for jobs in the job queue | Numeric | 
|   [batch:ShareIdentifier](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by the shareIdentifier used inside submit job | String | 
|   [batch:User](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html#awsbatch-policy-keys)  | Filters access by user name or numeric uid used inside the container | String | 
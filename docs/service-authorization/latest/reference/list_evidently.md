

# Actions, resources, and condition keys for Amazon CloudWatch Evidently
<a name="list_evidently"></a>

Amazon CloudWatch Evidently (service prefix: `evidently`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/evidently/evidently.json) for this service.

**Topics**
+ [Actions defined by Amazon CloudWatch Evidently](#list_evidently-actions-as-permissions)
+ [Resource types defined by Amazon CloudWatch Evidently](#list_evidently-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Evidently](#list_evidently-policy-keys)

## Actions defined by Amazon CloudWatch Evidently
<a name="list_evidently-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchEvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_BatchEvaluateFeature.html)  **
  - **Description:** Grants permission to send a batched evaluate feature request
  - **Resource types (\*required):** [Feature\*](#list_evidently-resource-Feature)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateExperiment.html)  **
  - **Description:** Grants permission to create an experiment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateFeature.html)  **
  - **Description:** Grants permission to create a feature
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateLaunch.html)  **
  - **Description:** Grants permission to create a launch
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create a project
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSegment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateSegment.html)  **
  - **Description:** Grants permission to create a segment
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteExperiment.html)  **
  - **Description:** Grants permission to delete an experiment
  - **Resource types (\*required):** [Experiment\*](#list_evidently-resource-Experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteFeature.html)  **
  - **Description:** Grants permission to delete a feature
  - **Resource types (\*required):** [Feature\*](#list_evidently-resource-Feature)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteLaunch.html)  **
  - **Description:** Grants permission to delete a launch
  - **Resource types (\*required):** [Launch\*](#list_evidently-resource-Launch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project
  - **Resource types (\*required):** [Project\*](#list_evidently-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSegment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_DeleteSegment.html)  **
  - **Description:** Grants permission to delete a segment
  - **Resource types (\*required):** [Segment\*](#list_evidently-resource-Segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html)  **
  - **Description:** Grants permission to send an evaluate feature request
  - **Resource types (\*required):** [Feature\*](#list_evidently-resource-Feature)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperiment.html)  **
  - **Description:** Grants permission to get experiment details
  - **Resource types (\*required):** [Experiment\*](#list_evidently-resource-Experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExperimentResults](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetExperimentResults.html)  **
  - **Description:** Grants permission to get experiment result
  - **Resource types (\*required):** [Experiment\*](#list_evidently-resource-Experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetFeature.html)  **
  - **Description:** Grants permission to get feature details
  - **Resource types (\*required):** [Feature\*](#list_evidently-resource-Feature)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetLaunch.html)  **
  - **Description:** Grants permission to get launch details
  - **Resource types (\*required):** [Launch\*](#list_evidently-resource-Launch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetProject.html)  **
  - **Description:** Grants permission to get project details
  - **Resource types (\*required):** [Project\*](#list_evidently-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSegment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_GetSegment.html)  **
  - **Description:** Grants permission to get segment details
  - **Resource types (\*required):** [Segment\*](#list_evidently-resource-Segment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListExperiments](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListExperiments.html)  **
  - **Description:** Grants permission to list experiments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFeatures](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeatures.html)  **
  - **Description:** Grants permission to list features
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLaunches](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListLaunches.html)  **
  - **Description:** Grants permission to list launches
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListProjects](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListProjects.html)  **
  - **Description:** Grants permission to list projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSegmentReferences](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListSegmentReferences.html)  **
  - **Description:** Grants permission to list resources referencing a segment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSegments](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListSegments.html)  **
  - **Description:** Grants permission to list segments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutProjectEvents](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_PutProjectEvents.html)  **
  - **Description:** Grants permission to send performance events
  - **Resource types (\*required):** [Project\*](#list_evidently-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StartExperiment.html)  **
  - **Description:** Grants permission to start an experiment
  - **Resource types (\*required):** [Experiment\*](#list_evidently-resource-Experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StartLaunch.html)  **
  - **Description:** Grants permission to start a launch
  - **Resource types (\*required):** [Launch\*](#list_evidently-resource-Launch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StopExperiment.html)  **
  - **Description:** Grants permission to stop an experiment
  - **Resource types (\*required):** [Experiment\*](#list_evidently-resource-Experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_StopLaunch.html)  **
  - **Description:** Grants permission to stop a launch
  - **Resource types (\*required):** [Launch\*](#list_evidently-resource-Launch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag resources
  - **Resource types (\*required):** [Experiment](#list_evidently-resource-Experiment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Feature](#list_evidently-resource-Feature) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Launch](#list_evidently-resource-Launch) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Project](#list_evidently-resource-Project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Segment](#list_evidently-resource-Segment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_evidently-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestSegmentPattern](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_TestSegmentPattern.html)  **
  - **Description:** Grants permission to test a segment pattern
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag resources
  - **Resource types (\*required):** [Experiment](#list_evidently-resource-Experiment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Feature](#list_evidently-resource-Feature) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Launch](#list_evidently-resource-Launch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Project](#list_evidently-resource-Project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Resource types (\*required):** [Segment](#list_evidently-resource-Segment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_evidently-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateExperiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateExperiment.html)  **
  - **Description:** Grants permission to update experiment
  - **Resource types (\*required):** [Experiment\*](#list_evidently-resource-Experiment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateFeature.html)  **
  - **Description:** Grants permission to update feature
  - **Resource types (\*required):** [Feature\*](#list_evidently-resource-Feature)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLaunch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateLaunch.html)  **
  - **Description:** Grants permission to update a launch
  - **Resource types (\*required):** [Launch\*](#list_evidently-resource-Launch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProject](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProject.html)  **
  - **Description:** Grants permission to update project
  - **Resource types (\*required):** [Project\*](#list_evidently-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProjectDataDelivery](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_UpdateProjectDataDelivery.html)  **
  - **Description:** Grants permission to update project data delivery
  - **Resource types (\*required):** [Project\*](#list_evidently-resource-Project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon CloudWatch Evidently
<a name="list_evidently-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Experiment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Experiment.html)  | arn:${Partition}:evidently:${Region}:${Account}:project/${ProjectName}/experiment/${ExperimentName} | [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_) | 
|  [Feature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Feature.html)  | arn:${Partition}:evidently:${Region}:${Account}:project/${ProjectName}/feature/${FeatureName} | [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_) | 
|  [Launch](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Launch.html)  | arn:${Partition}:evidently:${Region}:${Account}:project/${ProjectName}/launch/${LaunchName} | [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_) | 
|  [Project](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Project.html)  | arn:${Partition}:evidently:${Region}:${Account}:project/${ProjectName} | [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_) | 
|  [Segment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_Segment.html)  | arn:${Partition}:evidently:${Region}:${Account}:segment/${SegmentName} | [aws:ResourceTag/${TagKey}](#list_evidently-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Evidently
<a name="list_evidently-policy-keys"></a>

Amazon CloudWatch Evidently defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed the request on behalf of the IAM principal | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html)  | Filters access by the tags associated with the resource that make the request on behalf of the IAM principal | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request on behalf of the IAM principal | ArrayOfString | 
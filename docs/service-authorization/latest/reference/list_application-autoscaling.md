

# Actions, resources, and condition keys for AWS Application Auto Scaling
<a name="list_application-autoscaling"></a>

AWS Application Auto Scaling (service prefix: `application-autoscaling`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/autoscaling/application/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/autoscaling/application/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/autoscaling/application/userguide/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/application-autoscaling/application-autoscaling.json) for this service.

**Topics**
+ [API operations defined by AWS Application Auto Scaling](#list_application-autoscaling-operations)
+ [Actions defined by AWS Application Auto Scaling](#list_application-autoscaling-actions-as-permissions)
+ [Resource types defined by AWS Application Auto Scaling](#list_application-autoscaling-resources-for-iam-policies)
+ [Condition keys for AWS Application Auto Scaling](#list_application-autoscaling-policy-keys)

## API operations defined by AWS Application Auto Scaling
<a name="list_application-autoscaling-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_application-autoscaling-actions-as-permissions).




- **   DeleteScalingPolicy  **
  - **IAM action:**  [application-autoscaling:DeleteScalingPolicy](#list_application-autoscaling-action-DeleteScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduledAction  **
  - **IAM action:**  [application-autoscaling:DeleteScheduledAction](#list_application-autoscaling-action-DeleteScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterScalableTarget  **
  - **IAM action:**  [application-autoscaling:DeregisterScalableTarget](#list_application-autoscaling-action-DeregisterScalableTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeScalableTargets  **
  - **IAM action:**  [application-autoscaling:DescribeScalableTargets](#list_application-autoscaling-action-DescribeScalableTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScalingActivities  **
  - **IAM action:**  [application-autoscaling:DescribeScalingActivities](#list_application-autoscaling-action-DescribeScalingActivities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScalingPolicies  **
  - **IAM action:**  [application-autoscaling:DescribeScalingPolicies](#list_application-autoscaling-action-DescribeScalingPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeScheduledActions  **
  - **IAM action:**  [application-autoscaling:DescribeScheduledActions](#list_application-autoscaling-action-DescribeScheduledActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPredictiveScalingForecast  **
  - **IAM action:**  [application-autoscaling:GetPredictiveScalingForecast](#list_application-autoscaling-action-GetPredictiveScalingForecast) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [application-autoscaling:ListTagsForResource](#list_application-autoscaling-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutScalingPolicy  **
  - **IAM action:**  [application-autoscaling:PutScalingPolicy](#list_application-autoscaling-action-PutScalingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutScheduledAction  **
  - **IAM action:**  [application-autoscaling:PutScheduledAction](#list_application-autoscaling-action-PutScheduledAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterScalableTarget  **
  - **IAM action:**  [application-autoscaling:RegisterScalableTarget](#list_application-autoscaling-action-RegisterScalableTarget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [application-autoscaling:TagResource](#list_application-autoscaling-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** application-autoscaling.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [application-autoscaling:TagResource](#list_application-autoscaling-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [application-autoscaling:UntagResource](#list_application-autoscaling-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Application Auto Scaling
<a name="list_application-autoscaling-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DeleteScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeleteScalingPolicy.html)  **
  - **Description:** Grants permission to delete a scaling policy
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [application-autoscaling:scalable-dimension](#list_application-autoscaling-application-autoscaling_scalable-dimension)<br />[application-autoscaling:service-namespace](#list_application-autoscaling-application-autoscaling_service-namespace)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeleteScheduledAction.html)  **
  - **Description:** Grants permission to delete a scheduled action
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [application-autoscaling:scalable-dimension](#list_application-autoscaling-application-autoscaling_scalable-dimension)<br />[application-autoscaling:service-namespace](#list_application-autoscaling-application-autoscaling_service-namespace)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeregisterScalableTarget.html)  **
  - **Description:** Grants permission to deregister a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [application-autoscaling:scalable-dimension](#list_application-autoscaling-application-autoscaling_scalable-dimension)<br />[application-autoscaling:service-namespace](#list_application-autoscaling-application-autoscaling_service-namespace)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeScalableTargets](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalableTargets.html)  **
  - **Description:** Grants permission to describe one or more scalable targets in the specified namespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeScalingActivities](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingActivities.html)  **
  - **Description:** Grants permission to describe a set of scaling activities or all scaling activities in the specified namespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeScalingPolicies](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScalingPolicies.html)  **
  - **Description:** Grants permission to describe a set of scaling policies or all scaling policies in the specified namespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeScheduledActions](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DescribeScheduledActions.html)  **
  - **Description:** Grants permission to describe a set of scheduled actions or all scheduled actions in the specified namespace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPredictiveScalingForecast](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_GetPredictiveScalingForecast.html)  **
  - **Description:** Grants permission to retrieve the forecast data for a predictive scaling policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScalingPolicy.html)  **
  - **Description:** Grants permission to create and update a scaling policy for a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [application-autoscaling:scalable-dimension](#list_application-autoscaling-application-autoscaling_scalable-dimension)<br />[application-autoscaling:service-namespace](#list_application-autoscaling-application-autoscaling_service-namespace)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutScheduledAction](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PutScheduledAction.html)  **
  - **Description:** Grants permission to create and update a scheduled action for a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [application-autoscaling:scalable-dimension](#list_application-autoscaling-application-autoscaling_scalable-dimension)<br />[application-autoscaling:service-namespace](#list_application-autoscaling-application-autoscaling_service-namespace)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterScalableTarget](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html)  **
  - **Description:** Grants permission to register AWS or custom resources as scalable targets with Application Auto Scaling and to update configuration parameters used to manage a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [application-autoscaling:scalable-dimension](#list_application-autoscaling-application-autoscaling_scalable-dimension)<br />[application-autoscaling:service-namespace](#list_application-autoscaling-application-autoscaling_service-namespace)<br />[aws:RequestTag/${TagKey}](#list_application-autoscaling-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-autoscaling-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_application-autoscaling-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-autoscaling-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a scalable target
  - **Resource types (\*required):** [ScalableTarget\*](#list_application-autoscaling-resource-ScalableTarget)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_application-autoscaling-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Application Auto Scaling
<a name="list_application-autoscaling-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ScalableTarget](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:application-autoscaling:${Region}:${Account}:scalable-target/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_application-autoscaling-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Application Auto Scaling
<a name="list_application-autoscaling-policy-keys"></a>

AWS Application Auto Scaling defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [application-autoscaling:scalable-dimension](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the scalable dimension that is passed in the request | String | 
|   [application-autoscaling:service-namespace](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the service namespace that is passed in the request | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
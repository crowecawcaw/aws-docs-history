

# Actions, resources, and condition keys for Amazon Application Recovery Controller - Zonal Shift
<a name="list_arc-zonal-shift"></a>

Amazon Application Recovery Controller - Zonal Shift (service prefix: `arc-zonal-shift`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/r53recovery/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/arc-zonal-shift/arc-zonal-shift.json) for this service.

**Topics**
+ [API operations defined by Amazon Application Recovery Controller - Zonal Shift](#list_arc-zonal-shift-operations)
+ [Actions defined by Amazon Application Recovery Controller - Zonal Shift](#list_arc-zonal-shift-actions-as-permissions)
+ [Resource types defined by Amazon Application Recovery Controller - Zonal Shift](#list_arc-zonal-shift-resources-for-iam-policies)
+ [Condition keys for Amazon Application Recovery Controller - Zonal Shift](#list_arc-zonal-shift-policy-keys)

## API operations defined by Amazon Application Recovery Controller - Zonal Shift
<a name="list_arc-zonal-shift-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_arc-zonal-shift-actions-as-permissions).




- **   CancelPracticeRun  **
  - **IAM action:**  [arc-zonal-shift:CancelPracticeRun](#list_arc-zonal-shift-action-CancelPracticeRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelZonalShift  **
  - **IAM action:**  [arc-zonal-shift:CancelZonalShift](#list_arc-zonal-shift-action-CancelZonalShift) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePracticeRunConfiguration  **
  - **IAM action:**  [arc-zonal-shift:CreatePracticeRunConfiguration](#list_arc-zonal-shift-action-CreatePracticeRunConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePracticeRunConfiguration  **
  - **IAM action:**  [arc-zonal-shift:DeletePracticeRunConfiguration](#list_arc-zonal-shift-action-DeletePracticeRunConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAutoshiftObserverNotificationStatus  **
  - **IAM action:**  [arc-zonal-shift:GetAutoshiftObserverNotificationStatus](#list_arc-zonal-shift-action-GetAutoshiftObserverNotificationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedResource  **
  - **IAM action:**  [arc-zonal-shift:GetManagedResource](#list_arc-zonal-shift-action-GetManagedResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAutoshifts  **
  - **IAM action:**  [arc-zonal-shift:ListAutoshifts](#list_arc-zonal-shift-action-ListAutoshifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedResources  **
  - **IAM action:**  [arc-zonal-shift:ListManagedResources](#list_arc-zonal-shift-action-ListManagedResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListZonalShifts  **
  - **IAM action:**  [arc-zonal-shift:ListZonalShifts](#list_arc-zonal-shift-action-ListZonalShifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartPracticeRun  **
  - **IAM action:**  [arc-zonal-shift:StartPracticeRun](#list_arc-zonal-shift-action-StartPracticeRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartZonalShift  **
  - **IAM action:**  [arc-zonal-shift:StartZonalShift](#list_arc-zonal-shift-action-StartZonalShift) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAutoshiftObserverNotificationStatus  **
  - **IAM action:**  [arc-zonal-shift:UpdateAutoshiftObserverNotificationStatus](#list_arc-zonal-shift-action-UpdateAutoshiftObserverNotificationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePracticeRunConfiguration  **
  - **IAM action:**  [arc-zonal-shift:UpdatePracticeRunConfiguration](#list_arc-zonal-shift-action-UpdatePracticeRunConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateZonalAutoshiftConfiguration  **
  - **IAM action:**  [arc-zonal-shift:UpdateZonalAutoshiftConfiguration](#list_arc-zonal-shift-action-UpdateZonalAutoshiftConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateZonalShift  **
  - **IAM action:**  [arc-zonal-shift:UpdateZonalShift](#list_arc-zonal-shift-action-UpdateZonalShift) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Application Recovery Controller - Zonal Shift
<a name="list_arc-zonal-shift-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelPracticeRun.html)  **
  - **Description:** Grants permission to cancel an active practice run
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CancelZonalShift.html)  **
  - **Description:** Grants permission to cancel an active zonal shift
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_CreatePracticeRunConfiguration.html)  **
  - **Description:** Grants permission to create a practice run configuration
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_DeletePracticeRunConfiguration.html)  **
  - **Description:** Grants permission to delete a practice run configuration
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAutoshiftObserverNotificationStatus](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetAutoshiftObserverNotificationStatus.html)  **
  - **Description:** Grants permission to get autoshift observer notification status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetManagedResource](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_GetManagedResource.html)  **
  - **Description:** Grants permission to get information about a managed resource
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAutoshifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListAutoshifts.html)  **
  - **Description:** Grants permission to list active and completed autoshifts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedResources](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListManagedResources.html)  **
  - **Description:** Grants permission to list managed resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListZonalShifts](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_ListZonalShifts.html)  **
  - **Description:** Grants permission to list zonal shifts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartPracticeRun](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartPracticeRun.html)  **
  - **Description:** Grants permission to start a practice run
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_StartZonalShift.html)  **
  - **Description:** Grants permission to start a zonal shift
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutoshiftObserverNotificationStatus](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateAutoshiftObserverNotificationStatus.html)  **
  - **Description:** Grants permission to update autoshift observer notification status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePracticeRunConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdatePracticeRunConfiguration.html)  **
  - **Description:** Grants permission to update a practice run configuration
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateZonalAutoshiftConfiguration](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalAutoshiftConfiguration.html)  **
  - **Description:** Grants permission to update a zonal autoshift status
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateZonalShift](https://docs.aws.amazon.com/arc-zonal-shift/latest/api/API_UpdateZonalShift.html)  **
  - **Description:** Grants permission to update an existing zonal shift
  - **Resource types (\*required):** [ALB\*](#list_arc-zonal-shift-resource-ALB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Resource types (\*required):** [NLB\*](#list_arc-zonal-shift-resource-NLB) / **Condition keys:** [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Application Recovery Controller - Zonal Shift
<a name="list_arc-zonal-shift-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ALB](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/app/${LoadBalancerName}/${LoadBalancerId} | [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_) | 
|  [NLB](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html)  | arn:${Partition}:elasticloadbalancing:${Region}:${Account}:loadbalancer/net/${LoadBalancerName}/${LoadBalancerId} | [arc-zonal-shift:ResourceIdentifier](#list_arc-zonal-shift-arc-zonal-shift_ResourceIdentifier)<br />[aws:ResourceTag/${TagKey}](#list_arc-zonal-shift-aws_ResourceTag___TagKey_)<br />[elasticloadbalancing:ResourceTag/${TagKey}](#list_arc-zonal-shift-elasticloadbalancing_ResourceTag___TagKey_) | 

## Condition keys for Amazon Application Recovery Controller - Zonal Shift
<a name="list_arc-zonal-shift-policy-keys"></a>

Amazon Application Recovery Controller - Zonal Shift defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [arc-zonal-shift:ResourceIdentifier](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonroute53applicationrecoverycontroller-zonalshift.html#amazonroute53applicationrecoverycontroller-zonalshift-policy-keys)  | Filters access by the resource identifier of the managed resource | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html#elb-condition-keys)  | Filters access by the tags associated with the managed resource | String | 
|   [elasticloadbalancing:ResourceTag/${TagKey}](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-authentication-access-control.html#elb-condition-keys)  | Filters access by the tags associated with the managed resource | String | 
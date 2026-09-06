

# Actions, resources, and condition keys for Amazon Route 53 Recovery Controls
<a name="list_route53-recovery-control-config"></a>

Amazon Route 53 Recovery Controls (service prefix: `route53-recovery-control-config`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/recovery-cluster/latest/api/resources.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/route53-recovery-control-config/route53-recovery-control-config.json) for this service.

**Topics**
+ [API operations defined by Amazon Route 53 Recovery Controls](#list_route53-recovery-control-config-operations)
+ [Actions defined by Amazon Route 53 Recovery Controls](#list_route53-recovery-control-config-actions-as-permissions)
+ [Permission-only actions for Amazon Route 53 Recovery Controls](#list_route53-recovery-control-config-permission-only-actions)
+ [Resource types defined by Amazon Route 53 Recovery Controls](#list_route53-recovery-control-config-resources-for-iam-policies)
+ [Condition keys for Amazon Route 53 Recovery Controls](#list_route53-recovery-control-config-policy-keys)

## API operations defined by Amazon Route 53 Recovery Controls
<a name="list_route53-recovery-control-config-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53-recovery-control-config-actions-as-permissions).




- **   CreateCluster  **
  - **IAM action:**  [route53-recovery-control-config:CreateCluster](#list_route53-recovery-control-config-action-CreateCluster)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-control-config:TagResource](#list_route53-recovery-control-config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateControlPanel  **
  - **IAM action:**  [route53-recovery-control-config:CreateControlPanel](#list_route53-recovery-control-config-action-CreateControlPanel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-control-config:TagResource](#list_route53-recovery-control-config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRoutingControl  **
  - **IAM action:**  [route53-recovery-control-config:CreateRoutingControl](#list_route53-recovery-control-config-action-CreateRoutingControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSafetyRule  **
  - **IAM action:**  [route53-recovery-control-config:CreateSafetyRule](#list_route53-recovery-control-config-action-CreateSafetyRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [route53-recovery-control-config:TagResource](#list_route53-recovery-control-config-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCluster  **
  - **IAM action:**  [route53-recovery-control-config:DeleteCluster](#list_route53-recovery-control-config-action-DeleteCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteControlPanel  **
  - **IAM action:**  [route53-recovery-control-config:DeleteControlPanel](#list_route53-recovery-control-config-action-DeleteControlPanel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoutingControl  **
  - **IAM action:**  [route53-recovery-control-config:DeleteRoutingControl](#list_route53-recovery-control-config-action-DeleteRoutingControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSafetyRule  **
  - **IAM action:**  [route53-recovery-control-config:DeleteSafetyRule](#list_route53-recovery-control-config-action-DeleteSafetyRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCluster  **
  - **IAM action:**  [route53-recovery-control-config:DescribeCluster](#list_route53-recovery-control-config-action-DescribeCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeControlPanel  **
  - **IAM action:**  [route53-recovery-control-config:DescribeControlPanel](#list_route53-recovery-control-config-action-DescribeControlPanel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRoutingControl  **
  - **IAM action:**  [route53-recovery-control-config:DescribeRoutingControl](#list_route53-recovery-control-config-action-DescribeRoutingControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSafetyRule  **
  - **IAM action:**  [route53-recovery-control-config:DescribeSafetyRule](#list_route53-recovery-control-config-action-DescribeSafetyRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [route53-recovery-control-config:GetResourcePolicy](#list_route53-recovery-control-config-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssociatedRoute53HealthChecks  **
  - **IAM action:**  [route53-recovery-control-config:ListAssociatedRoute53HealthChecks](#list_route53-recovery-control-config-action-ListAssociatedRoute53HealthChecks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClusters  **
  - **IAM action:**  [route53-recovery-control-config:ListClusters](#list_route53-recovery-control-config-action-ListClusters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListControlPanels  **
  - **IAM action:**  [route53-recovery-control-config:ListControlPanels](#list_route53-recovery-control-config-action-ListControlPanels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRoutingControls  **
  - **IAM action:**  [route53-recovery-control-config:ListRoutingControls](#list_route53-recovery-control-config-action-ListRoutingControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSafetyRules  **
  - **IAM action:**  [route53-recovery-control-config:ListSafetyRules](#list_route53-recovery-control-config-action-ListSafetyRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [route53-recovery-control-config:ListTagsForResource](#list_route53-recovery-control-config-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [route53-recovery-control-config:TagResource](#list_route53-recovery-control-config-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [route53-recovery-control-config:UntagResource](#list_route53-recovery-control-config-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCluster  **
  - **IAM action:**  [route53-recovery-control-config:UpdateCluster](#list_route53-recovery-control-config-action-UpdateCluster) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateControlPanel  **
  - **IAM action:**  [route53-recovery-control-config:UpdateControlPanel](#list_route53-recovery-control-config-action-UpdateControlPanel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoutingControl  **
  - **IAM action:**  [route53-recovery-control-config:UpdateRoutingControl](#list_route53-recovery-control-config-action-UpdateRoutingControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSafetyRule  **
  - **IAM action:**  [route53-recovery-control-config:UpdateSafetyRule](#list_route53-recovery-control-config-action-UpdateSafetyRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Route 53 Recovery Controls
<a name="list_route53-recovery-control-config-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html)  **
  - **Description:** Grants permission to create a cluster
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-control-config-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Access level:** Write

- **   [CreateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html)  **
  - **Description:** Grants permission to create a control panel
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-control-config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html)  **
  - **Description:** Grants permission to create a routing control
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html)  **
  - **Description:** Grants permission to create a safety rule
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-control-config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html)  **
  - **Description:** Grants permission to delete a cluster
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html)  **
  - **Description:** Grants permission to delete a control panel
  - **Resource types (\*required):** [controlpanel\*](#list_route53-recovery-control-config-resource-controlpanel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html)  **
  - **Description:** Grants permission to delete a routing control
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-control-config-resource-routingcontrol)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html)  **
  - **Description:** Grants permission to delete a safety rule
  - **Resource types (\*required):** [safetyrule\*](#list_route53-recovery-control-config-resource-safetyrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html)  **
  - **Description:** Grants permission to describe a cluster
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html)  **
  - **Description:** Grants permission to describe a control panel
  - **Resource types (\*required):** [controlpanel\*](#list_route53-recovery-control-config-resource-controlpanel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html)  **
  - **Description:** Grants permission to describe a routing control
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-control-config-resource-routingcontrol)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html)  **
  - **Description:** Grants permission to describe a safety rule
  - **Resource types (\*required):** [safetyrule\*](#list_route53-recovery-control-config-resource-safetyrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster/resourcepolicy-resourcearn.html)  **
  - **Description:** Grants permission to get the resource policy of a cluster
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssociatedRoute53HealthChecks](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn-associatedroute53healthchecks.html)  **
  - **Description:** Grants permission to list associated Route 53 health checks
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-control-config-resource-routingcontrol)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClusters](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html)  **
  - **Description:** Grants permission to list clusters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListControlPanels](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanels.html)  **
  - **Description:** Grants permission to list control panels
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRoutingControls](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-routingcontrols.html)  **
  - **Description:** Grants permission to list routing controls
  - **Resource types (\*required):** [controlpanel\*](#list_route53-recovery-control-config-resource-controlpanel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSafetyRules](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-safetyrules.html)  **
  - **Description:** Grants permission to list safety rules
  - **Resource types (\*required):** [controlpanel\*](#list_route53-recovery-control-config-resource-controlpanel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/recovery-cluster/latest/api/tags-resource-arn.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [cluster](#list_route53-recovery-control-config-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [controlpanel](#list_route53-recovery-control-config-resource-controlpanel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [safetyrule](#list_route53-recovery-control-config-resource-safetyrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/recovery-cluster/latest/api/tags-resource-arn.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [cluster](#list_route53-recovery-control-config-resource-cluster) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-control-config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Resource types (\*required):** [controlpanel](#list_route53-recovery-control-config-resource-controlpanel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-control-config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Resource types (\*required):** [safetyrule](#list_route53-recovery-control-config-resource-safetyrule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_route53-recovery-control-config-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/recovery-cluster/latest/api/tags-resource-arn.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [cluster](#list_route53-recovery-control-config-resource-cluster) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Resource types (\*required):** [controlpanel](#list_route53-recovery-control-config-resource-controlpanel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Resource types (\*required):** [safetyrule](#list_route53-recovery-control-config-resource-safetyrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_route53-recovery-control-config-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html)  **
  - **Description:** Grants permission to update a cluster
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html)  **
  - **Description:** Grants permission to update a cluster
  - **Resource types (\*required):** [controlpanel\*](#list_route53-recovery-control-config-resource-controlpanel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html)  **
  - **Description:** Grants permission to update a routing control
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-control-config-resource-routingcontrol)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html)  **
  - **Description:** Grants permission to update a safety rule
  - **Resource types (\*required):** [safetyrule\*](#list_route53-recovery-control-config-resource-safetyrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Route 53 Recovery Controls
<a name="list_route53-recovery-control-config-permission-only-actions"></a>

The following actions are defined by Amazon Route 53 Recovery Controls but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.failover-different-accounts.html)  **
  - **Description:** Grants permission to delete the RAM access control policy for a cluster
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.failover-different-accounts.html)  **
  - **Description:** Grants permission to define the RAM access control policy for a cluster
  - **Resource types (\*required):** [cluster\*](#list_route53-recovery-control-config-resource-cluster)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon Route 53 Recovery Controls
<a name="list_route53-recovery-control-config-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [cluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html)  | arn:${Partition}:route53-recovery-control::${Account}:cluster/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_) | 
|  [controlpanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html)  | arn:${Partition}:route53-recovery-control::${Account}:controlpanel/${ControlPanelId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_) | 
|  [routingcontrol](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html)  | arn:${Partition}:route53-recovery-control::${Account}:controlpanel/${ControlPanelId}/routingcontrol/${RoutingControlId} |   | 
|  [safetyrule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html)  | arn:${Partition}:route53-recovery-control::${Account}:controlpanel/${ControlPanelId}/safetyrule/${SafetyRuleId} | [aws:ResourceTag/${TagKey}](#list_route53-recovery-control-config-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Route 53 Recovery Controls
<a name="list_route53-recovery-control-config-policy-keys"></a>

Amazon Route 53 Recovery Controls defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
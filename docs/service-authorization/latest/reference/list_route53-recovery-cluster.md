

# Actions, resources, and condition keys for Amazon Route 53 Recovery Cluster
<a name="list_route53-recovery-cluster"></a>

Amazon Route 53 Recovery Cluster (service prefix: `route53-recovery-cluster`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/routing-control/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/route53-recovery-cluster/route53-recovery-cluster.json) for this service.

**Topics**
+ [API operations defined by Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-operations)
+ [Actions defined by Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-actions-as-permissions)
+ [Resource types defined by Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-resources-for-iam-policies)
+ [Condition keys for Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-policy-keys)

## API operations defined by Amazon Route 53 Recovery Cluster
<a name="list_route53-recovery-cluster-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53-recovery-cluster-actions-as-permissions).




- **   GetRoutingControlState  **
  - **IAM action:**  [route53-recovery-cluster:GetRoutingControlState](#list_route53-recovery-cluster-action-GetRoutingControlState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRoutingControls  **
  - **IAM action:**  [route53-recovery-cluster:ListRoutingControls](#list_route53-recovery-cluster-action-ListRoutingControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UpdateRoutingControlState  **
  - **IAM action:**  [route53-recovery-cluster:UpdateRoutingControlState](#list_route53-recovery-cluster-action-UpdateRoutingControlState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoutingControlStates  **
  - **IAM action:**  [route53-recovery-cluster:UpdateRoutingControlStates](#list_route53-recovery-cluster-action-UpdateRoutingControlStates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Route 53 Recovery Cluster
<a name="list_route53-recovery-cluster-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html)  **
  - **Description:** Grants permission to get a routing control state
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-cluster-resource-routingcontrol)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListRoutingControls](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ListRoutingControls.html)  **
  - **Description:** Grants permission to list routing controls
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [UpdateRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html)  **
  - **Description:** Grants permission to update a routing control state
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-cluster-resource-routingcontrol)
  - **Condition keys:** [route53-recovery-cluster:AllowSafetyRulesOverrides](#list_route53-recovery-cluster-route53-recovery-cluster_AllowSafetyRulesOverrides)
  - **Access level:** Write

- **   [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html)  **
  - **Description:** Grants permission to update a batch of routing control states
  - **Resource types (\*required):** [routingcontrol\*](#list_route53-recovery-cluster-resource-routingcontrol)
  - **Condition keys:** [route53-recovery-cluster:AllowSafetyRulesOverrides](#list_route53-recovery-cluster-route53-recovery-cluster_AllowSafetyRulesOverrides)
  - **Access level:** Write



## Resource types defined by Amazon Route 53 Recovery Cluster
<a name="list_route53-recovery-cluster-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [routingcontrol](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html)  | arn:${Partition}:route53-recovery-control::${Account}:controlpanel/${ControlPanelId}/routingcontrol/${RoutingControlId} |   | 

## Condition keys for Amazon Route 53 Recovery Cluster
<a name="list_route53-recovery-cluster-policy-keys"></a>

Amazon Route 53 Recovery Cluster defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [route53-recovery-cluster:AllowSafetyRulesOverrides](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html)  | Override safety rules to allow routing control state updates | Bool | 
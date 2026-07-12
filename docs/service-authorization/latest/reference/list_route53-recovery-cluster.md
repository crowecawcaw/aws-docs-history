# Actions, resources, and condition keys for Amazon Route 53 Recovery Cluster

Amazon Route 53 Recovery Cluster (service prefix: `route53-recovery-cluster`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../r53recovery/latest/dg/what-is-route53-recovery.md "../../../r53recovery/latest/dg/what-is-route53-recovery.md").
- View a list of the [API operations available for
  this service](../../../routing-control/latest/APIReference/Welcome.md "../../../routing-control/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../r53recovery/latest/dg/security-iam.md "../../../r53recovery/latest/dg/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/route53-recovery-cluster/route53-recovery-cluster.json "https://servicereference.us-east-1.amazonaws.com/v1/route53-recovery-cluster/route53-recovery-cluster.json") for this service.

###### Topics

- [API operations defined by Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-operations "#list_route53-recovery-cluster-operations")
- [Actions defined by Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-actions-as-permissions "#list_route53-recovery-cluster-actions-as-permissions")
- [Resource types defined by Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-resources-for-iam-policies "#list_route53-recovery-cluster-resources-for-iam-policies")
- [Condition keys for Amazon Route 53 Recovery Cluster](#list_route53-recovery-cluster-policy-keys "#list_route53-recovery-cluster-policy-keys")

## API operations defined by Amazon Route 53 Recovery Cluster

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_route53-recovery-cluster-actions-as-permissions "#list_route53-recovery-cluster-actions-as-permissions").

| Operation                  | IAM action                                                                                                                                                                                 | Condition key | Possible value(s) | Access level |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| GetRoutingControlState     | [route53-recovery-cluster:GetRoutingControlState](#list_route53-recovery-cluster-action-GetRoutingControlState "#list_route53-recovery-cluster-action-GetRoutingControlState")             |               |                   | Read         |
| ListRoutingControls        | [route53-recovery-cluster:ListRoutingControls](#list_route53-recovery-cluster-action-ListRoutingControls "#list_route53-recovery-cluster-action-ListRoutingControls")                      |               |                   | Read         |
| UpdateRoutingControlState  | [route53-recovery-cluster:UpdateRoutingControlState](#list_route53-recovery-cluster-action-UpdateRoutingControlState "#list_route53-recovery-cluster-action-UpdateRoutingControlState")    |               |                   | Write        |
| UpdateRoutingControlStates | [route53-recovery-cluster:UpdateRoutingControlStates](#list_route53-recovery-cluster-action-UpdateRoutingControlStates "#list_route53-recovery-cluster-action-UpdateRoutingControlStates") |               |                   | Write        |

## Actions defined by Amazon Route 53 Recovery Cluster

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                       | Description                                                   | Resource types (\*required)                                                                                                         | Condition keys                                                                                                                                                                                                              | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [GetRoutingControlState](../../../routing-control/latest/APIReference/API_GetRoutingControlState.md "../../../routing-control/latest/APIReference/API_GetRoutingControlState.md")             | Grants permission to get a routing control state              | [routingcontrol\*](#list_route53-recovery-cluster-resource-routingcontrol "#list_route53-recovery-cluster-resource-routingcontrol") |                                                                                                                                                                                                                             | Read         |
| [ListRoutingControls](../../../routing-control/latest/APIReference/API_ListRoutingControls.md "../../../routing-control/latest/APIReference/API_ListRoutingControls.md")                      | Grants permission to list routing controls                    |                                                                                                                                     |                                                                                                                                                                                                                             | Read         |
| [UpdateRoutingControlState](../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md "../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md")    | Grants permission to update a routing control state           | [routingcontrol\*](#list_route53-recovery-cluster-resource-routingcontrol "#list_route53-recovery-cluster-resource-routingcontrol") | [route53-recovery-cluster:AllowSafetyRulesOverrides](#list_route53-recovery-cluster-route53-recovery-cluster_AllowSafetyRulesOverrides "#list_route53-recovery-cluster-route53-recovery-cluster_AllowSafetyRulesOverrides") | Write        |
| [UpdateRoutingControlStates](../../../routing-control/latest/APIReference/API_UpdateRoutingControlStates.md "../../../routing-control/latest/APIReference/API_UpdateRoutingControlStates.md") | Grants permission to update a batch of routing control states | [routingcontrol\*](#list_route53-recovery-cluster-resource-routingcontrol "#list_route53-recovery-cluster-resource-routingcontrol") | [route53-recovery-cluster:AllowSafetyRulesOverrides](#list_route53-recovery-cluster-route53-recovery-cluster_AllowSafetyRulesOverrides "#list_route53-recovery-cluster-route53-recovery-cluster_AllowSafetyRulesOverrides") | Write        |

## Resource types defined by Amazon Route 53 Recovery Cluster

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                    | ARN                                                                                                                     | Condition keys |
| --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------- |
| [routingcontrol](../../../recovery-cluster/latest/api/routingcontrol.md "../../../recovery-cluster/latest/api/routingcontrol.md") | arn:${Partition}:route53-recovery-control::${Account}:controlpanel/${ControlPanelId}/routingcontrol/${RoutingControlId} |                |

## Condition keys for Amazon Route 53 Recovery Cluster

Amazon Route 53 Recovery Cluster defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                      | Description                                                  | Type |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---- |
| [route53-recovery-cluster:AllowSafetyRulesOverrides](../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md "../../../routing-control/latest/APIReference/API_UpdateRoutingControlState.md") | Override safety rules to allow routing control state updates | Bool |

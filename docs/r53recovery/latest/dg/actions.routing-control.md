

# Routing control API operations
<a name="actions.routing-control"></a>

This section includes tables with lists API operations that you can use for setting up and using routing control in Amazon Application Recovery Controller (ARC), with links to relevant documentation.

For examples of how to use common routing control configuration API operations with the AWS Command Line Interface, see [Examples of using ARC routing control API operations with the AWS CLI](getting-started-cli-routing.md).

The following table lists ARC API operations that you can use for routing control configuration, with links to relevant documentation.


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Create a cluster | See [Creating routing control components in ARC](routing-control.create.md) | See [CreateCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html) | 
| Describe a cluster | See [Creating routing control components in ARC](routing-control.create.md) | See [DescribeCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html) | 
| Delete a cluster | See [Creating routing control components in ARC](routing-control.create.md) | See [DeleteCluster](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html) | 
| List clusters for an account | See [Creating routing control components in ARC](routing-control.create.md) | See [ListClusters](https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html) | 
| Create a routing control | See [Creating routing control components in ARC](routing-control.create.md) | See [CreateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html) | 
| Describe a routing control | See [Creating routing control components in ARC](routing-control.create.md) | See [DescribeRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html) | 
| Update a routing control | See [Creating routing control components in ARC](routing-control.create.md) | See [UpdateRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html) | 
| Delete a routing control | See [Creating routing control components in ARC](routing-control.create.md) | See [DeleteRoutingControl](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html) | 
| List routing controls | See [Creating routing control components in ARC](routing-control.create.md) | See [ListRoutingControls](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-routingcontrols.html) | 
| Create a control panel | See [Creating routing control components in ARC](routing-control.create.md) | See [CreateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html) | 
| Describe a control panel | See [Creating routing control components in ARC](routing-control.create.md) | See [DescribeControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html) | 
| Update a control panel | See [Creating routing control components in ARC](routing-control.create.md) | See [UpdateControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html) | 
| Delete a control panel | See [Creating routing control components in ARC](routing-control.create.md) | See [DeleteControlPanel](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html) | 
| List control panels | See [Creating routing control components in ARC](routing-control.create.md) | See [ListControlPanels](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanels.html) | 
| Create a safety rule | See [Creating safety rules for routing control](routing-control.safety-rules.md) | See [CreateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html) | 
| Describe a safety rule | See [Creating safety rules for routing control](routing-control.safety-rules.md) | See [DescribeSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html) | 
| Update a safety rule | See [Creating safety rules for routing control](routing-control.safety-rules.md) | See [UpdateSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html) | 
| Delete a safety rule | See [Creating safety rules for routing control](routing-control.safety-rules.md) | See [DeleteSafetyRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule-safetyrulearn.html) | 
| List safety rules | See [Creating safety rules for routing control](routing-control.safety-rules.md) | See [ListSafetyRules](https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-safetyrules.html) | 
| List associated Route 53 health checks | See [Creating a routing control health check in ARC](routing-control.create-health-check.md) | See [ ListAssociatedRoute53HealthChecks](https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn-associatedroute53healthchecks.html) | 
| List the AWS RAM resource policies for cluster sharing | See [Support cross-account for clusters in ARC](routing-control.failover-different-accounts.md) | See [ GetResourcePolicy](https://docs.aws.amazon.com/recovery-cluster/latest/api/resourcepolicy-resourcearn.html) | 

The following table lists common ARC API operations that you can use for managing traffic failover with the routing control data plane, with links to relevant documentation.


| Action | Using the ARC console | Using the ARC API | 
| --- | --- | --- | 
| Get a routing control state | See [Getting and updating routing control states in the AWS Management Console](routing-control.update.console.md) | See [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html) | 
| List routing controls | N/A | See [ListRoutingControls](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_ListRoutingControls.html) | 
| Update a routing control state | See [Getting and updating routing control states in the AWS Management Console](routing-control.update.console.md) | See [UpdateRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlState.html) | 
| Update multiple routing control states | See [Getting and updating routing control states in the AWS Management Console](routing-control.update.console.md) | See [UpdateRoutingControlStates](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_UpdateRoutingControlStates.html) | 
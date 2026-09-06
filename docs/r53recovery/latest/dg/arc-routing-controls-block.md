

# ARC routing control execution block
<a name="arc-routing-controls-block"></a>

If you've configured Amazon Application Recovery Controller (ARC) routing control for your application, you can add a ARC routing control step to redirect application traffic. This step enables you to change the state of one or more ARC routing controls to redirect your application traffic to a destination AWS Region. ARC routing control redirects traffic by using health checks in Amazon Route 53 that are configured with the DNS records associated with the routing controls.

**Important**  
Amazon Application Recovery Controller (ARC) routing control is only available in the AWS commercial partition.

## Configuration
<a name="arc-routing-controls-block-config"></a>

To configure a routing control execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [ARC routing controls execution block sample policy](security_iam_region_switch_arc_routing.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Desired routing controls: ** For each Region that you want to activate or deactivate, enter the routing control ARN and the initial state for the routing control, On or Off.

1. **Timeout: **Enter a timeout value.

Then, choose **Save step.**

The expected pattern for this execution block is to specify routing controls and initial states that align with how you have set up your application in specific AWS Regions. For example, if you have plan that enables you to activate Region A and Region B for your application, then you might have a routing control for Region A where you set the state to On and a routing control for Region B where you set the state to On.

Then, when you execute the plan and specify that you want to activate Region A, the workflow that includes this execution block updates the specified routing control to On, which directs traffic to Region A.

## How it works
<a name="arc-routing-controls-block-how"></a>

By configuring a ARC routing control execution block, you can reroute application traffic to a destination AWS Region, or, for an active/active approach, stop traffic from being routed to a Region that you're deactivating. If your plan includes multiple workflows, make sure that you provide the same inputs for the DNS records for all routing control execution blocks that you use. 

This block does not support ungraceful execution mode.

## Comparing ARC routing controls and Route 53 health check execution blocks
<a name="region-switch-compare-routing"></a>

The Amazon Route 53 health check execution block in Region switch provides a lower-cost alternative for DNS-based traffic management. However, this execution block depends on the AWS Region that you're activating, so that Region must be available. This meets the needs of most customers, because they are activating a healthy Region.

ARC routing controls provide highly reliable DNS-based traffic management with a 100% availability SLA. With routing controls, your operations teams can shift traffic between Regions with safety guardrails. Routing controls provide a single-tenant solution with a 100% SLA. A routing control cluster is spread across five Regions and can tolerate two Regions being offline. If you have highly critical applications, consider using routing controls.

Routing controls are not required to use Region switch. You can use Region switch to manage traffic redirection by using Route 53 health check execution blocks without routing controls.

Routing controls add value with Region switch in the following situations:
+ You require the 100% availability SLA for the traffic control mechanism itself.
+ Your organization requires manual operational controls with safety rules for critical applications.
+ You want defense-in-depth so that operations teams can manually override automated traffic routing if needed.

Route 53 health check execution blocks do not depend on the control plane. Health check record changes use the data plane, so they do not require the activating Region to process configuration updates. Route 53 health check execution blocks are sufficient in the following situations:
+ Your application can depend on the AWS Region that you are activating.
+ Automated traffic redirection as part of the recovery workflow meets your requirements.
+ Cost optimization is a priority. Route 53 health check execution blocks have lower cost than routing controls.

Most customers start with Route 53 health check execution blocks as the default traffic routing mechanism and add routing controls only for their most critical applications that require the highest reliability for the traffic management mechanism.
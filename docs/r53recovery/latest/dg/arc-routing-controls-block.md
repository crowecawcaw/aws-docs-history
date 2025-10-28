# ARC routing control execution block

If you've configured Amazon Application Recovery Controller (ARC) routing control for your application, you can add a ARC
routing control execution block to redirect application traffic. This execution block
enables you to change the state of one or more ARC routing controls
to redirect your application traffic to a destination AWS Region. ARC routing control
redirects traffic by using health checks in Amazon Route 53 that are configured with the DNS records
associated with the routing controls.

## Configuration

To configure a routing control execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [ARC routing controls execution block sample policy](security_iam_region_switch_arc_routing.md "security_iam_region_switch_arc_routing.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Desired routing controls:** For each Region
   that you want to activate or deactivate, enter the routing control ARN and the initial state
   for the routing control, On or Off.
4. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

The expected pattern for this execution block is to specify routing controls and initial
states that align with how you have set up your application in specific AWS Regions. For
example, if you have plan that enables you to activate Region A and Region B for your application,
then you might have a routing control for Region A where you set the state to On and a
routing control for Region B where you set the state to On.

Then, when you execute the plan and specify that you want to activate Region A, the
workflow that includes this execution block updates the specified routing control to
On, which directs traffic to Region A.

## How it works

By configuring a ARC routing control execution block, you can reroute application traffic
to a destination AWS Region, or, for an active/active approach, stop traffic from being routed
to a Region that you're deactivating. If your plan includes multiple workflows, make sure that
you provide the same inputs for the DNS records for all routing control execution blocks
that you use.

This block does not support ungraceful execution mode.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your routing controls execution block configuration
and permissions. Region switch verifies that the specified routing controls are properly configured and accessible.

Region switch also validates that the plan's IAM role has the required permissions for accessing and updating routing
control states. For more information about the required permissions for Region switch execution
blocks, see [Identity-based policy
examples for Region switch in ARC](security_iam_id-based-policy-examples-region-switch.md "security_iam_id-based-policy-examples-region-switch.md").

The correct IAM permissions are essential for the proper functioning of the routing control execution block. If
any of these validations fail, Region switch returns warnings that there are issues, and provides specific error messages to help
you resolve the permissions or configuration issues. This ensures that your plan has the necessary access to manage
and interact with the ARC routing controls during when this step runs during a plan execution.

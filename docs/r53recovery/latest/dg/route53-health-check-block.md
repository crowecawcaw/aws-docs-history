# Amazon Route 53 health check execution block

The Amazon Route 53 health check execution block enables you to specify the Regions that your
application's traffic will be redirected to during failover. The execution block creates Amazon Route 53
health checks, which you then attach to Route 53 DNS records in your account. When you
execute your Region switch plan, the Route 53 health check state is updated, and traffic is
redirected based on your DNS configuration.

## Configuration

To configure a Route 53 health check execution block, enter the following values.

###### Important

Before you configure the execution block, make sure that you have the correct IAM policy in place.
For more information, see [Route 53 health check execution block sample policy](security_iam_region_switch_route53.md "security_iam_region_switch_route53.md").

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Hosted zone ID:** The hosted zone Id for your domain
   and DNS records in Route 53.
4. **Record name:** Enter the record name (domain name) for
   the records that you use, with the associated health checks, to redirect traffic for your application.
   Region switch will find the Route 53 record sets for the record name and attempt to map each record
   set to a Region, based on the Region name inside the **Value** or
   **Set Identifier** of the record set.
5. **Record set identifiers (optional):** You have the option
   to manually provide the record set identifiers if Region switch cannot automatically map the
   record sets to Regions from the record name provided in step 4 after you have created the plan.
   If plan evaluation returns a warning that indicates that more information is required, update
   your plan with record set identifiers by including the following for each Region:
   - **Record set identifier:** Enter
     the **Set identifier** or the **Value/Route traffic to**
     for the record set.
   - **Region:** Enter the Region associated with
     the record set that has the record set identifier information.

6. Choose **Save step.**
7. Configure health checks in Route 53.

Region switch provides a health check ID, for each Region, for each record name within
a hosted zone defined in the execution block. Make sure that you configure the health checks
for the corresponding record sets in your account in Route 53 so that Region switch can correctly
redirect traffic for your application during plan execution. In the
**Health checks** tab on the plan details page, you can view the health checks
for all execution blocks and Regions.

## How it works

You add a health check execution block to your Region switch workflow so that you
can redirect traffic to a secondary Region, for active/passive configurations,
or away from a deactivated Region, for active/active configurations.
If you add multiple workflows to your plan, provide the same
configuration values for all health check execution blocks that use the same DNS records.

Based on the information that you provide when you configure the execution block,
Region switch attempts to determine the correct record
set for each Region in your plan. Typically, the hosted zone ID and the record name are enough information
to determine the record sets and associated Regions. If not, when Region switch runs its automatic plan evaluation
after you create the plan, a warning is returned to let you know that more information is required.

Region switch vends health checks for each Route 53 health check execution block. For plans that
use a active/passive recovery approach, the health check for the primary Region
starts as healthy, and the health check for the standby Region is
initially set to unhealthy. For plans that use the active/active recovery
approach, health checks for all Regions start in the healthy state.

To enable Region switch to successfully run this execution block for your plan,
you must add the health checks to your DNS records.

For an active/active plan, the execution step works in the following way:

- When a deactivate workflow runs for a Region, the
  health check is set to unhealthy, and traffic is no longer directed to the Region.
- When an activate workflow runs for a Region, the
  health check is set to healthy, and traffic is routed to the Region.

For an active/passive plan, the execution step works in the following way:

- When an activate workflow runs for a Region, the
  health check for that Region is set to healthy, and traffic is
  routed to the Region. At the same time, the health check for
  the other Region in the plan is set to unhealthy, and traffic
  stops being directed to that Region.

## What is evaluated as part of plan evaluation

When Region switch evaluates your plan, Region switch performs several checks on your Route 53 health check execution block configuration
and permissions. Region switch verifies that health checks are attached to the DNS records
specified in the execution block configuration. That is, Region switch
verifies that the DNS records for a specific AWS Region
are configured to use health checks for that Region.

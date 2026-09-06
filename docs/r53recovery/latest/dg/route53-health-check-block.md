

# Amazon Route 53 health check execution block
<a name="route53-health-check-block"></a>

The Amazon Route 53 health check execution block enables you to specify the Regions that your application's traffic will be redirected to during failover. The execution block creates Amazon Route 53 health checks, which you then attach to Route 53 DNS records in your account. When you execute your Region switch plan, the Route 53 health check state is updated, and traffic is redirected based on your DNS configuration.

**Important**  
The Route 53 hosted zone must be in the same partition as the Region switch plan.

## Configuration
<a name="route53-health-check-block-config"></a>

To configure a Route 53 health check execution block, enter the following values.

**Important**  
Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place. For more information, see [Route 53 health check execution block sample policy](security_iam_region_switch_route53.md).

1. **Step name: **Enter a name.

1. **Step description (optional): **Enter a description of the step.

1. **Hosted zone ID: **The hosted zone Id for your domain and DNS records in Route 53.

1. **Record name: **Enter the record name (domain name) for the records that you use, with the associated health checks, to redirect traffic for your application. Region switch will find the Route 53 record sets for the record name and attempt to map each record set to a Region, based on the Region name inside the **Value** or **Set Identifier** of the record set.

1. **Record set identifiers (optional): **You have the option to manually provide the record set identifiers if Region switch cannot automatically map the record sets to Regions from the record name provided in step 4 after you have created the plan. If plan evaluation returns a warning that indicates that more information is required, update your plan with record set identifiers by including the following for each Region:
   + **Record set identifier: **Enter the **Set identifier** or the **Value/Route traffic to** for the record set.
   + **Region: ** Enter the Region associated with the record set that has the record set identifier information.

1. Choose **Save step.**

1. Configure health checks in Route 53.

   Region switch provides a health check ID, for each Region, for each record name within a hosted zone defined in the execution block. Make sure that you configure the health checks for the corresponding record sets in your account in Route 53 so that Region switch can correctly redirect traffic for your application during plan execution. In the **Health checks** tab on the plan details page, you can view the health checks for all execution blocks and Regions. 

## How the Route 53 health check execution block works as a highly available DNS failover mechanism
<a name="route53-health-check-block-how"></a>

ARC Region Switch Route53 health check execution block creates two sets of health checks — one for each Region if your workload is deployed in two Regions. It vends these health checks to you. You can view them through the Region switch console in "Monitoring" tab or via the ListRoute53HealthChecks API. You then associate these health checks with your Route 53 DNS records.

When the Route 53 health check execution block is executed, it uses the STOP (Standby Takes Over Primary) pattern under the hood to change the state of your health checks to orchestrate the DNS failover. The primary health check is marked "unhealthy" and the secondary health check is marked "healthy" when you orchestrate a failover from primary to secondary. This change in health check state is used by Route 53 to redirect traffic during failover.

For active/passive: the primary Region's health check starts healthy; the passive Region starts unhealthy. When you use the Route53 health check execution block to failover, these states flip.

For active/active: all health checks start healthy. When you use the Route53 health check execution block in a deactivate workflow, the workflow sets the deactivating Region's health check state to unhealthy. When you use the Route53 health check execution block in an activate workflow for a Region, the workflow sets the activating Region's health check state to healthy.

### Why is this a highly available failover mechanism?
<a name="route53-health-check-block-why-ha"></a>

Two reasons make this a reliable failover mechanism:

1. **Route 53 health check state transitions are part of Route 53 data plane, which is designed for 100% availability**

   Changing the state of a Route53 health check state is a data plane operation. The Route53 data plane is globally distributed and designed for 100% availability. There is no control plane dependency to Route53 health check state changes. This means health check state change works even if the primary Region is impaired.

1. **The STOP pattern (Standby Takes Over Primary)**

   The STOP pattern is a mechanism to orchestrate a DNS failover and it was published in the blog post here: [ Creating disaster recovery mechanisms using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/). This pattern is used by the Route53 health check execution block under the hood. The STOP pattern entails using the healthy Region as a "decision agent" to change the state of the health check in the impaired Region. The STOP pattern does not take dependency on the impaired Region.

Here's how it works in practice:
+ When you create a Route53 health check execution block, health checks are created by Region switch in each Region for your workload and vended to you through Region switch console in the Monitoring tab or the ListRoute53HealthChecks API.
+ You then associate these with each Region's DNS record manually. One health check is associated with the primary Region's DNS record and the other is associated with the secondary Region's DNS record by you.
+ The health check is associated with primary Region's DNS records, but it monitors a resource in the standby (secondary) Region (for example: presence of a file in S3) to change the state of the health check.
+ The health check is inverted — if the standby resource is unreachable, the health check for the primary Region defaults to healthy. If the standby resource is discovered, the health check for the primary Region is changed to unhealthy. This prevents accidental failover.
+ To trigger a failover, the file is created by Region switch in the standby Region. The health check detects it, marks primary unhealthy, and Route53 flips DNS. The standby resource is managed by the Region switch service and is not dependent on the customer.

The combination of no control plane dependency (globally distributed data plane) and no impaired Region dependency (STOP pattern) makes this a highly available DNS failover mechanism when the customer is only operating from two Regions. See STOP pattern documented here: [ Creating disaster recovery mechanisms using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/).

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
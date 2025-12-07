# Routing control in ARC

To fail over traffic to application replicas in multiple AWS Regions, you can use routing
controls in Amazon Application Recovery Controller (ARC) that are integrated with a specific kind of health check in
Amazon Route 53. _Routing controls_ are simple on-off switches that enable you
to switch your client traffic from one Regional replica to another. The traffic rerouting is
accomplished by _routing control health checks_ that are set up with
Amazon Route 53 DNS records. For example, DNS failover records, associated with domain names that
front your application replicas in each Region.

This section explains how routing control works, how to set up routing control components, and how to
use them to reroute traffic for failover.

The routing control components in ARC are: clusters, control panels, routing controls, and routing control health checks.
All routing controls are grouped on control panels. You can group them on the default control panel that ARC creates for your
cluster, or create your own custom control panels. You must create a cluster before you can
create a control panel or a routing control. Each cluster in ARC is a data plane of endpoints in five AWS Regions.

After you create routing controls and routing control health checks, you can create safety rules for routing
control to help prevent unintentional
recovery automation side effects. You can update routing control states to reroute traffic, individually or in
batches, by using the AWS CLI or API actions (recommended), or by using the AWS Management Console.

This section explains how routing controls work, and how to create and use them to reroute traffic for your application.

###### Important

To learn about preparing to use ARC to reroute traffic as part of a failover plan for your application in a disaster
scenario, see [Best practices for routing control in ARC](route53-arc-best-practices.md "route53-arc-best-practices.md").

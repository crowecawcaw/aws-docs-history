# Supported resources

Amazon Application Recovery Controller (ARC) currently supports enabling the following resources for zonal shift and zonal autoshift:

- [Amazon EC2 Auto Scaling groups](arc-zonal-shift.resource-types.md "arc-zonal-shift.resource-types.md")
- [Amazon Elastic Kubernetes Service](arc-zonal-shift.resource-types.md "arc-zonal-shift.resource-types.md")
- [Application Load Balancers](arc-zonal-shift.resource-types.md "arc-zonal-shift.resource-types.md") with
  cross-zone load balancing enabled or disabled
- [Network Load Balancers](arc-zonal-shift.resource-types.md "arc-zonal-shift.resource-types.md") with cross-zone load balancing enabled or disabled
  For specific requirements for Network Load Balancers and Application Load Balancers, see the additional topics in this section.

Review the following conditions for working with zonal shifts, zonal autoshift, and resources in ARC:

- A resource must be active and fully provisioned to shift traffic for it. Before you
  start a zonal shift for a resource, check to make sure that it's a managed resource in ARC. For example,
  view the list of managed resources in the AWS Management Console, or use the `get-managed-resource`
  operation with the resource's identifier.
- To start a zonal shift with a resource, it must be deployed in the Availability Zone and AWS Region
  where you start the shift. Make sure that you start a zonal shift in the same Region that the AZ you want to shift away
  from is in, and that the resource that you're shifting traffic for is in the same AZ and Region as well.
- Ensure that you have the correct IAM permissions to use zonal shift with a resource. For
  more information, see [IAM and permissions for zonal shift](security_iam_service-with-iam-zonal-shift.md "security_iam_service-with-iam-zonal-shift.md").
- When a Network Load Balancer or Application Load Balancer is in a fail open state, a zonal shift will have no effect. This is
  expected behavior because zonal shift cannot force an AZ to be unhealthy and
  then shift traffic to the other AZs in a Region when a load balancer is
  failing open. For more information, see [Using Route 53 DNS failover for your load balancer](../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md#r53-dns-failover "../../../elasticloadbalancing/latest/network/load-balancer-target-groups.md#r53-dns-failover") in the _Network Load Balancers User Guide_ and [Using Route 53 DNS failover for your load balancer](../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#r53-dns-failover "../../../elasticloadbalancing/latest/application/load-balancer-target-groups.md#r53-dns-failover") in the _Application Load Balancers User Guide_.
- If multiple load balancers are forwarding traffic to the same targets, a zonal shift on
  a cross-zone enabled load balancer drops target capacity for all load balancers, even if their traffic is not
  shifted by a zonal shift.

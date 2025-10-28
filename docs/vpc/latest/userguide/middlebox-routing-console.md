# Middlebox routing wizard

If you want to configure fine-grain control over the routing path of traffic entering or
leaving your VPC, for example, by redirecting traffic to a security appliance, you can use
the middlebox routing wizard in the VPC console. The middlebox routing wizard helps you by automatically
creating the necessary route tables and routes (hops) to redirect traffic as needed.

The middlebox routing wizard can help you configure routing for the following scenarios:

- Routing traffic to a middlebox appliance, for example, an Amazon EC2 instance that's
  configured as a security appliance.
- Routing traffic to a Gateway Load Balancer. For more information, see the [User Guide for Gateway Load Balancers](../../../elasticloadbalancing/latest/gateway.md "../../../elasticloadbalancing/latest/gateway.md").
  For more information, see [Middlebox scenarios](middlebox-routing-examples.md "middlebox-routing-examples.md").

###### Contents

- [Middlebox routing wizard prerequisites](#routing-console-rules "#routing-console-rules")
- [Redirect VPC traffic to a security appliance](working-with-routing-console.md "working-with-routing-console.md")
- [Middlebox routing wizard
  considerations](#console-routes-considerations "#console-routes-considerations")
- [Middlebox scenarios](middlebox-routing-examples.md "middlebox-routing-examples.md")

## Middlebox routing wizard prerequisites

Review [Middlebox routing wizard
considerations](#console-routes-considerations "#console-routes-considerations"). Then, make sure that you
have the following information before you use the middlebox routing wizard.

- The VPC.
- The resource where traffic originates from or enters the VPC, for example, an
  internet gateway, virtual private gateway, or network interface.
- The middlebox network interface or Gateway Load Balancer endpoint.
- The destination subnet for the traffic.

## Middlebox routing wizard

considerations

Take the following into consideration when you use the middlebox routing wizard:

- If you want to inspect traffic, you can use an internet gateway or a virtual
  private gateway for the source.
- If you use the same middlebox in a multiple middlebox configuration within the
  same VPC, make sure that the middlebox is in the same hop position for both
  subnets.
- The appliance must be configured in a separate subnet from the source or
  destination subnet.
- You must disable source/destination checking on the appliance. For more
  information, see [Changing the
  Source or Destination Checking](../../../AWSEC2/latest/UserGuide/using-eni.md#change_source_dest_check "../../../AWSEC2/latest/UserGuide/using-eni.md#change_source_dest_check") in the
  _Amazon EC2 User Guide_.
- The route tables and routes that the middlebox routing wizard creates count toward your
  quotas. For more information, see [Route tables](amazon-vpc-limits.md#vpc-limits-route-tables "amazon-vpc-limits.md#vpc-limits-route-tables").
- If you delete a resource, for example a network interface, the route table
  associations with the resource are removed. If the resource is a target, the
  route destination is set to blackhole. The route tables are not deleted.
- The middlebox subnet and the destination subnet must be associated with a
  non-default route table.

###### Note

We recommend that you use the middlebox routing wizard to modify or delete any route
tables that you created using the middlebox routing wizard.

- If you use middlebox routing to route through a security appliance, [security group referencing](security-group-rules.md#security-group-referencing "security-group-rules.md#security-group-referencing") between the source and ultimate destination after inspection is not supported.

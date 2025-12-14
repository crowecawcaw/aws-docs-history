**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How Firewall Manager manages and monitors VPC route tables for your

policy

This section explains how Firewall Manager manages and monitors your VPC route tables.

###### Note

Route table management isn't currently supported for policies that use the centralized deployment model.

When Firewall Manager creates your firewall endpoints, it also creates the VPC route tables for
them. However, Firewall Manager doesn't manage your VPC route tables. You must configure your VPC
route tables to direct network traffic to the firewall endpoints that are created by
Firewall Manager. Using Amazon VPC ingress routing enhancements, change your routing tables to route
traffic through the new firewall endpoints. Your changes must insert the firewall
endpoints between the subnets that you want to protect and outside locations. The exact
routing that you need to do depends on your architecture and its components.

Currently, Firewall Manager allows monitoring of your VPC route table routes for any traffic destined to the internet gateway,
that is bypassing the firewall. Firewall Manager doesn't support other target gateways like NAT gateways.

For information about managing route tables for your VPC, see [Managing route tables for your VPC](../../../vpc/latest/userguide/VPC_Route_Tables.md "../../../vpc/latest/userguide/VPC_Route_Tables.md") in the _Amazon Virtual Private Cloud User
Guide_. For information about managing your route tables for
Network Firewall, see [Route table
configurations for AWS Network Firewall](../../../network-firewall/latest/developerguide/route-tables.md "../../../network-firewall/latest/developerguide/route-tables.md") in the
_AWS Network Firewall Developer Guide_.

When you enable monitoring for a policy, Firewall Manager continuously monitors VPC route
configurations and alerts you about traffic that bypasses firewall inspection for that
VPC. If a subnet has a firewall endpoint route, Firewall Manager looks for the following
routes:

- Routes to send traffic to the Network Firewall endpoint.
- Routes to forward the traffic from the Network Firewall endpoint to the internet
  gateway.
- Inbound routes from the internet gateway to the Network Firewall endpoint.
- Routes from the firewall subnet.
  If a subnet has a Network Firewall route but there's asymmetric routing in Network Firewall and your internet
  gateway route table, Firewall Manager reports the subnet as non-compliant. Firewall Manager also detects
  routes to the internet gateway in the firewall route table that Firewall Manager created, as well
  as the route table for your subnet, and reports them as non-compliant. Additional routes
  in the Network Firewall subnet route table and your internet gateway route table are also reported
  as non-compliant. Depending on the violation type, Firewall Manager suggests remediation actions to
  bring the route configuration into compliance. Firewall Manager doesn't offer suggestions in all
  cases. For example, if your customer subnet has a firewall endpoint that was created
  outside of Firewall Manager, Firewall Manager doesn't suggest remediation actions.

By default, Firewall Manager will mark any traffic that crosses the Availability Zone boundary for inspection as being non-compliant. However, if you choose to automatically create a single endpoint in your VPC, Firewall Manager won't mark traffic that crosses the Availability Zone boundary as non-compliant.

For policies that use distributed deployment models with custom endpoint configuration, you
can choose whether the traffic crossing the Availability Zone boundary from an
Availability Zone without a firewall endpoint is marked as compliant or
non-compliant.

###### Note

- Firewall Manager does not suggest remediation actions for non-IPv4 routes, such as
  IPv6 and prefix list routes.
- Calls made using the `DisassociateRouteTable` API call can take
  up to 12 hours to detect.
- Firewall Manager creates a Network Firewall route table for a subnet that contains the firewall endpoints.
  Firewall Manager assumes that this route table contains only valid internet gateway and
  VPC default routes. Any extra or invalid routes in this route table are
  considered to be non-compliant.
  When you configure your Firewall Manager policy, if you choose **Monitor** mode,
  Firewall Manager provides resource violation and remediation details about your resources. You can
  use these suggested remediation actions to fix route issues in your route tables. If you
  choose **Off** mode, Firewall Manager doesn't monitor your route table content for
  you. With this option, you manage your VPC route tables for yourself. For more
  information about these resource violations, see [Viewing compliance information for an AWS Firewall Manager policy](fms-compliance.md "fms-compliance.md").

###### Warning

If you choose **Monitor** under **AWS Network Firewall route
configuration** when creating your policy, you can't turn it off for
that policy. However, if you choose **Off**, you can enable it
later.

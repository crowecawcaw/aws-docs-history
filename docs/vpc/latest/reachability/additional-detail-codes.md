# Reachability Analyzer additional detail codes

Reachability Analyzer uses additional detail codes to provide information about the result of a path
analysis.

The following additional detail codes are supported.

**ASSUMPTION_PRESERVE_CLIENT_IP_IS_DISABLED**
The analysis could not describe target group attributes for the target group,
so the network path is based on the assumption that client IP preservation is disabled on
the target group. You should verify this assumption.

**ASSUMPTION_PRESERVE_CLIENT_IP_IS_ENABLED**
The analysis could not describe target group attributes for the target group,
so the network path is based on the assumption that client IP preservation is enabled on
the target group. You should verify this assumption.

**AVAILABILITY_ZONE_CROSSED**
The network path crosses Availability Zones.

**FIREWALL_UNSUPPORTED_HIGHER_PRIORITY_RULE_GROUP_TYPE**
There is at least one higher priority rule that could match the traffic
in this path, but we ignored because it contains an unsupported rule type. Verify that
the result of the analysis matches the behavior of AWS Network Firewall in your network.

**FIREWALL_UNSUPPORTED_HIGHER_PRIORITY_RULES**
There is at least one higher priority rule that could match the traffic
in this path, but we ignored because it contains an unsupported rule option. Verify that
the result of the analysis matches the behavior of AWS Network Firewall in your network.

**FIREWALL_UNSUPPORTED_RULE_OPTIONS**
The matching firewall rule contains an unsupported rule option. Verify that
the result of the analysis matches the behavior of AWS Network Firewall in your network.

**MISSING_TARGET_GROUP_ATTRIBUTES**
The target group attributes for the target were missing, so the analysis
could not consider them.

**PATH_THROUGH_GWLB_NOT_CHECKED**
The analysis does not consider that traffic entering the VPC endpoint is
forwarded to a Gateway Load Balancer for inspection before exiting the VPC endpoint.

**RESPONSE_RTB_HAS_NO_ROUTE_TO_TRANSIT_GATEWAY**
Traffic is routed from the transit gateway to the VPC endpoint. However,
there is no route from the VPC endpoint to the transit gateway, so the network might
drop the response traffic.

**TRANSIT_GATEWAY_APPLIANCE_MODE_RECOMMENDED**
The transit gateway VPC attachment has [appliance mode](../tgw/how-transit-gateways-work.md#tgw-az-overview "../tgw/how-transit-gateways-work.md#tgw-az-overview")
disabled, but traffic is inspected through a Network Firewall. We recommend that
you enable appliance mode for the VPC attachment.

**UNIDIRECTIONAL_PATH_ANALYSIS_ONLY**
The results include forward path analysis from the source to the destination.
There might be a blocking configuration in the reverse path, which could not be
analyzed.

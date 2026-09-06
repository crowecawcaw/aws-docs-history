

# Reachability Analyzer additional detail codes
<a name="additional-detail-codes"></a>

Reachability Analyzer uses additional detail codes to provide information about the result of a path analysis.

The following additional detail codes are supported.

**ASSUMPTION\_PRESERVE\_CLIENT\_IP\_IS\_DISABLED**  
The analysis could not describe target group attributes for the target group, so the network path is based on the assumption that client IP preservation is disabled on the target group. You should verify this assumption.

**ASSUMPTION\_PRESERVE\_CLIENT\_IP\_IS\_ENABLED**  
The analysis could not describe target group attributes for the target group, so the network path is based on the assumption that client IP preservation is enabled on the target group. You should verify this assumption.

**AVAILABILITY\_ZONE\_CROSSED**  
The network path crosses Availability Zones.

**FIREWALL\_UNSUPPORTED\_HIGHER\_PRIORITY\_RULE\_GROUP\_TYPE**  
There is at least one higher priority rule that could match the traffic in this path, but we ignored because it contains an unsupported rule type. Verify that the result of the analysis matches the behavior of AWS Network Firewall in your network.

**FIREWALL\_UNSUPPORTED\_HIGHER\_PRIORITY\_RULES**  
There is at least one higher priority rule that could match the traffic in this path, but we ignored because it contains an unsupported rule option. Verify that the result of the analysis matches the behavior of AWS Network Firewall in your network.

**FIREWALL\_UNSUPPORTED\_RULE\_OPTIONS**  
The matching firewall rule contains an unsupported rule option. Verify that the result of the analysis matches the behavior of AWS Network Firewall in your network.

**MISSING\_TARGET\_GROUP\_ATTRIBUTES**  
The target group attributes for the target were missing, so the analysis could not consider them.

**PATH\_THROUGH\_GWLB\_NOT\_CHECKED**  
The analysis does not consider that traffic entering the VPC endpoint is forwarded to a Gateway Load Balancer for inspection before exiting the VPC endpoint.

**RESPONSE\_RTB\_HAS\_NO\_ROUTE\_TO\_TRANSIT\_GATEWAY**  
Traffic is routed from the transit gateway to the VPC endpoint. However, there is no route from the VPC endpoint to the transit gateway, so the network might drop the response traffic.

**TRANSIT\_GATEWAY\_APPLIANCE\_MODE\_RECOMMENDED**  
The transit gateway VPC attachment has [appliance mode](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html#tgw-az-overview) disabled, but traffic is inspected through a Network Firewall. We recommend that you enable appliance mode for the VPC attachment.

**UNIDIRECTIONAL\_PATH\_ANALYSIS\_ONLY**  
The results include forward path analysis from the source to the destination. There might be a blocking configuration in the reverse path, which could not be analyzed.


# Transit gateway policy table limitations in AWS Transit Gateway
<a name="tgw-policy-tables-limitations"></a>

The following limitations apply to transit gateway policy tables at launch.
+ **TGW-to-Cloud WAN (CWAN) peering attachments** — PBR is not supported for customer-managed entries on these attachments. Traffic on CWAN peering attachments is controlled exclusively by system-managed entries, which have higher priority and are read-only. You can add customer entries to the same policy table for use with other attachment types.
+ **BGP route advertisement** — AWS Transit Gateway does not advertise any routes to BGP-speaking attachments (Site-to-Site VPN and Connect appliances) that are associated with a policy table. Associating a policy table with one of these attachments stops all BGP route advertisements to the peer.

  Direct Connect behaves differently: the prefixes advertised to the customer gateway are governed by the allowed-prefixes list on the Direct Connect gateway association, so those advertisements continue regardless of policy-table association.

  If your design relies on TGW-advertised BGP routes, do not associate a policy table with the attachment until you have verified the impact on your routing topology.
+ **Attachment exclusivity** — an attachment can be associated with either a policy table or a route table, but not both. If you attempt to associate a policy table with an attachment that already has a route table associated, the request fails. Disassociate the route table first.
+ **System entry modification** — system-managed entries cannot be modified or deleted by customers at this time. These entries are managed entirely by AWS and are visible in the `GetTransitGatewayPolicyTableEntries` API response and in the console with a rule number of `*`.
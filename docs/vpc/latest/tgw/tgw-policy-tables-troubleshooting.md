# Troubleshooting transit gateway policy tables in AWS Transit Gateway

Use the following information to diagnose and resolve issues with transit gateway policy
tables.

###### Traffic is being dropped unexpectedly

Check the `PacketDropCountNoPolicy` CloudWatch metric. If it is incrementing,
traffic is arriving on an attachment associated with a policy table but not matching any
rule. Review your rule match criteria and ensure a catch-all rule (all attributes set to
Any) is present at a high rule number if you want unmatched traffic to have a default
forwarding path.

###### A rule is not matching traffic I expect it to match

Verify rule evaluation order. Rules are evaluated in ascending numeric order and the
first match wins. A broader rule at a lower number may be matching your traffic before
the more specific rule you intended. Review your rule numbers and reorder as
needed.

Use `GetTransitGatewayPolicyTableEntries` to view all entries, including
system-managed entries. System-managed entries are evaluated before customer-managed entries
and may be matching your traffic.

###### Port ranges are not being applied to my rule

Port ranges are only evaluated when Protocol is TCP (`6`) or UDP
(`17`). If your rule specifies ICMPv4 (`1`), GRE (`47`),
or Any (`*`) as the protocol, any port range values are automatically set to
Any (`*`) and are not evaluated. To use port-based matching, set Protocol to
TCP or UDP.

If you submitted port ranges with a non-TCP/non-UDP protocol via the API, the request is
rejected with a validation error. Confirm the protocol value in your request.

###### I cannot delete a route table

A transit gateway route table that is referenced as a target by any policy table entry cannot be
deleted. Use `GetTransitGatewayPolicyTableEntries` with a filter on
`target-route-table-id` to identify which rules reference the table, then
update or delete those rules before retrying the deletion.

###### I cannot associate a policy table to my attachment

Confirm that the attachment does not already have a route table associated with it. If
it does, disassociate the route table first. See [Associate a transit gateway policy table](tgw-policy-tables-associate.md "tgw-policy-tables-associate.md") for instructions. Also confirm that
the attachment type is supported — TGW-to-CWAN peering attachments do not support
customer-managed policy based routing. See [Limitations](tgw-policy-tables-limitations.md "tgw-policy-tables-limitations.md").

###### My policy table is empty and traffic is being dropped

An attachment associated with an empty policy table drops all ingressing packets. This
is the same behavior as an empty route table. Add at least one rule, or reassociate the
attachment with a route table, to restore traffic forwarding.

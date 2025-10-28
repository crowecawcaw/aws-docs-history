# Transit gateway route tables in AWS Transit Gateway

Use transit gateway route tables to configure routing for your transit gateway attachments. A route table is a
table that contains rules that direct how your network traffic is routed between your VPCs
and VPNs. Each route in the table contains the range of IP addresses for the destinations
that you want to send traffic to.

Transit gateway route tables allows you to associate a table with a transit gateway
attachment. VPC, VPN, Direct Connect gateway, Peering, and Connect attachments are all
supported. When associated, routes for these attachments are propagated from the attachment
to the target transit gateway route table. An attachment can be propagated to multiple route
tables.

Additionally you can create and manage static routes with a route table. For example, you
might have a static route that's used as a backup route in the event of a network disruption
that affects any dynamic routes.

###### Tasks

- [Create a transit gateway route table](create-tgw-route-table.md "create-tgw-route-table.md")
- [View transit gateway route tables](view-tgw-route-tables.md "view-tgw-route-tables.md")
- [Associate a transit gateway route table](associate-tgw-route-table.md "associate-tgw-route-table.md")
- [Disassociate a transit gateway route table](disassociate-tgw-route-table.md "disassociate-tgw-route-table.md")
- [Enable route propagation](enable-tgw-route-propagation.md "enable-tgw-route-propagation.md")
- [Disable route propagation](disable-tgw-route-propagation.md "disable-tgw-route-propagation.md")
- [Create a static route](tgw-create-static-route.md "tgw-create-static-route.md")
- [Delete a static route](tgw-delete-static-route.md "tgw-delete-static-route.md")
- [Replace a static route](tgw-replace-static-route.md "tgw-replace-static-route.md")
- [Export route tables to Amazon S3](tgw-export-route-tables.md "tgw-export-route-tables.md")
- [Delete a transit gateway route table](delete-tgw-route-table.md "delete-tgw-route-table.md")
- [Create a prefix list reference](create-prefix-list-reference.md "create-prefix-list-reference.md")
- [Modify a prefix list reference](modify-prefix-list-reference.md "modify-prefix-list-reference.md")
- [Delete a prefix list reference](delete-prefix-list-reference.md "delete-prefix-list-reference.md")

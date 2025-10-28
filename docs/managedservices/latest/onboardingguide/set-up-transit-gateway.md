# Setting up additional transit gateway application route tables

AWS Managed Services (AMS) networking is flexible and supports a variety of networking use cases.

- Communication between application VPCs in the same account.
- Communication between application VPCs in different accounts.
- Isolation between application VPCs in different accounts.
- Isolation between application VPCs in same accounts.
  If you have unique/special requirements for networking, contact your AMS Cloud
  Architect and they will develop a plan for your requirements to be met by AMS network
  architecture.

Based on the networking decision taken for application account VPCs, you can create
multiple Transit Gateway (TGW) application route tables by submitting a Deployment | Managed
landing zone | Networking account | Create transit gateway route table (ct-3dscwaeyi6cup) RFC.

The change type requires you to specify `TransitGatewayRouteTableName` (a meaningful name for the TGW route table),
`TransitGatewayId`, and `TGWRouteTableType`.

###### Note

If createCustomRouteDomain is selected for TGWRouteTableType, the route table created is empty. You must file an RFC with the
[Deployment | Managed landing zone | Networking account | Add static route (ct-3r2ckznmt0a59)](../ctref/deployment-managed-networking-account-add-static-route.md "../ctref/deployment-managed-networking-account-add-static-route.md") change type.

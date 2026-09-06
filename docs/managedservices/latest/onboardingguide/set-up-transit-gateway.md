

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Setting up additional transit gateway application route tables
<a name="set-up-transit-gateway"></a>

AWS Managed Services (AMS) networking is flexible and supports a variety of networking use cases.
+ Communication between application VPCs in the same account.
+ Communication between application VPCs in different accounts.
+ Isolation between application VPCs in different accounts.
+ Isolation between application VPCs in same accounts.

If you have unique/special requirements for networking, contact your AMS Cloud Architect and they will develop a plan for your requirements to be met by AMS network architecture.

Based on the networking decision taken for application account VPCs, you can create multiple Transit Gateway (TGW) application route tables by submitting a Deployment \| Managed landing zone \| Networking account \| Create transit gateway route table (ct-3dscwaeyi6cup) RFC. 

The change type requires you to specify `TransitGatewayRouteTableName` (a meaningful name for the TGW route table), `TransitGatewayId`, and `TGWRouteTableType`.

**Note**  
If createCustomRouteDomain is selected for TGWRouteTableType, the route table created is empty. You must file an RFC with the [ Deployment \| Managed landing zone \| Networking account \| Add static route (ct-3r2ckznmt0a59)](https://docs.aws.amazon.com/managedservices/latest/ctref/deployment-managed-networking-account-add-static-route.html) change type.
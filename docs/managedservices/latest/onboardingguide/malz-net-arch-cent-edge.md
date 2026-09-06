

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Centralized edge connectivity using transit gateway
<a name="malz-net-arch-cent-edge"></a>

AWS Transit Gateway is a service that enables you to connect your VPCs and your on-premises networks to a single gateway. Transit gateway (TGW) can be used to consolidate your existing edge connectivity and route it through a single ingress/egress point. Transit gateway is created in the networking account of your AMS multi-account environment. For more details about transit gateway, see [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/).

AWS Direct Connect (DX) gateway is used to connect your DX connection over a transit virtual interface to the VPCs or VPNs that are attached to your transit gateway. You associate a Direct Connect gateway with the transit gateway. Then, create a transit virtual interface for your AWS Direct Connect connection to the Direct Connect gateway. For information on DX virtual interfaces, see [ AWS Direct Connect Virtual Interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html).

This configuration offers the following benefits. You can:
+ Manage a single connection for multiple VPCs or VPNs that are in the same AWS Region.
+ Advertise prefixes from on-premises to AWS, and from AWS to on-premises.

**Note**  
For information about using a DX with AWS services, see the Resiliency Toolkit section [Classic](https://docs.aws.amazon.com/directconnect/latest/UserGuide/getstarted.html). For more information, see [Transit Gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html).

![AWS Transit Gateway network diagram showing connections to VPCs and Direct Connect.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/malz-cent-edge.png)


To increase the resiliency of your connectivity, we recommend that you attach at least two transit virtual interfaces from different AWS Direct Connect locations to the Direct Connect gateway. For more information, see the [AWS Direct Connect resiliency recommendation](https://aws.amazon.com/directconnect/resiliency-recommendation/).
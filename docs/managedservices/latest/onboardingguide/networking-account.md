

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Networking account
<a name="networking-account"></a>

The Networking account serves as the central hub for network routing between AMS multi-account landing zone accounts, your on-premises network, and egress traffic out to the Internet. In addition, this account contains public DMZ bastions that are the entry point for AMS engineers to access hosts in the AMS environment. For details, see the following high-level diagram of the networking account below.

![Network architecture diagram showing Egress and DMZ VPCs with availability zones, NAT gateways, DMZ bastions, and routing to internet and on-premises networks.](http://docs.aws.amazon.com/managedservices/latest/onboardingguide/images/malzNetworkAccount.png)

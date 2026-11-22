

# ADVREL05-BP01 Deploy partner-facing bid gateways across multiple Availability Zones

 RTB Fabric defaults to single-AZ gateway deployment. To survive an Availability Zone failure, you must deploy gateways in at least two Availability Zones, colocate with the Availability Zones where your DSP and SSP compute runs. Each subnet must have sufficient IPv4 capacity for gateway ENIs. 

 **Desired outcome:** 
+  RTB Fabric gateways are provisioned in at least two Availability Zones, each in a separate subnet with adequate available IPv4 address capacity. 
+  Gateways are colocated with the compute fleet they serve, avoiding unnecessary cross-AZ latency. 
+  An Availability Zone failure leaves bid connectivity intact through the gateways in the surviving Availability Zones, with no manual intervention and no sustained drop in bid win rate during or after the impairment. 

 **Common anti-patterns:** 
+  Deploying all gateways in a single Availability Zone, so an Availability Zone impairment removes all bid connectivity. 
+  Provisioning a gateway in an Availability Zone that has no compute fleet. 
+  Subnets with insufficient available IPv4 addresses, which causes gateway ENI provisioning to fail during scaling or failover. 

 **Benefits of establishing this best practice:** 
+  Bid connectivity survives a single-AZ impairment without manual intervention. 
+  Co-locating gateways with compute keeps bid-path latency within budget while adding redundancy. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTB Fabric provisions gateways in one Availability Zone unless you request more. That default assumes a single zone stays healthy for the life of the workload. An Availability Zone impairment breaks that assumption, and because every gateway terminates partner traffic, the loss is total. 

 A gateway in an Availability Zone without compute adds a cross-AZ hop to every bid and provides no resilience benefit. Colocate gateways with compute so each zone can both receive bid traffic and act on it locally. 

 Multi-AZ plans often fail on subnet capacity. Each gateway attaches network interfaces that draw IPv4 addresses from its subnet, and scaling or a failover into a surviving zone raises that draw exactly when a stall is unaffordable. A tight subnet looks fine at steady state and then refuses new interfaces under load. 

 The service controls how many zones a single gateway can span, and that limit comes from a quota requested before provisioning. Your role determines which direction of connectivity each zone must permit, depending on whether you act as requester or responder. Request the quota first, before any gateway exists, and derive each zone's rules from your role. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Request the Multi-AZ gateway service quota increase:** Request the "Availability Zones per Gateway" service quota increase for Multi-AZ gateway deployment through the AWS Service Quotas console before provisioning. 

1.  **Provision gateways in at least two Availability Zones:** Provision gateways in ≥2 Availability Zones within your VPC, each in a separate subnet with adequate available IPv4 addresses. Confirm gateways are deployed in the same Availability Zones as your compute fleet. A gateway in an Availability Zone with no compute provides no resilience benefit and adds unnecessary cross-AZ latency. 

1.  **Configure security groups per Availability Zone:** Configure security groups in each Availability Zone to allow HTTPS (TCP 443) inbound per your role (requester or responder). 

1.  **Monitor subnet IPv4 capacity:** Create a scheduled Lambda function that periodically calls ec2:DescribeSubnets and publishes the AvailableIpAddressCount as a custom CloudWatch metric, enabling you to set alarms before IP exhaustion affects gateway scaling. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP03 Deploy stateful dependencies across multiple Availability Zones](advrel03-bp03.md) 
+  [ADVREL05-BP02 Monitor Availability Zone-level health and detect asymmetric failures](advrel05-bp02.md) 

 **Related documents:** 
+  [AWS RTB Fabric - Setting Up](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/setting-up-aws-rtb-service.html) 
+  [AWS RTB Fabric - Service Quotas](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/rtb-fabric-quotas.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
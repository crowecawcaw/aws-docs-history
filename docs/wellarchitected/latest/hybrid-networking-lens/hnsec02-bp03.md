

# HNSEC02-BP03 Implement least privilege access for hybrid network management
<a name="hnsec02-bp03"></a>

 To implement least privilege, hybrid connectivity resources management should be granted only to teams responsible for hybrid connectivity. The teams should own circuits, dedicated connections, and VPNs even though other teams depend on these shared networking resources. 

 **Desired outcome:** Ensure that hybrid connectivity resources are securely managed, access is restricted to authorized personnel, and operational risk is minimized by centralizing ownership and management. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Enforces least privilege and separation of duties 
+  Reduces risk of misconfiguration or unauthorized changes 
+  Improve governance and compliance 
+  Enables consistent operational practices and incident response 
+  Ensures accountability for networking and security controls 

## Implementation guidance
<a name="implementation-guidance-12"></a>
+  Assign responsibility for managing hybrid connectivity resources, such as Direct Connect, VPN, Transit Gateway, to a dedicated networking and security team. 
+  Restrict permissions so only approved networking and security personnel can create, modify, or delete connectivity resources. 
+  Separate development and operational responsibilities to prevent developers from modifying shared networking infrastructure. 
+  Establish standard operating procedures and change management workflows for connectivity changes. 
+  Audit access and configuration change regularly. For example, you can achieve this using AWS CloudTrail. 

## Resources
<a name="resources-11"></a>
+  [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) 
+  [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) 
+  [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) 
+  [AWS Transit Gateway for Amazon VPC](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) 
+  [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) 
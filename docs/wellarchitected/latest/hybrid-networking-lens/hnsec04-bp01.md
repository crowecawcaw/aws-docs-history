

# HNSEC04-BP01 Control access to network resources
<a name="hnsec04-bp01"></a>

 Comprehensive network access control applied across both on-premises and cloud environments to create a unified security posture that addresses the unique challenges of hybrid infrastructures while maintaining compliance with regulatory requirements. 

 **Desired outcome:** Protect hybrid network resources by controlling traffic from on-premises and cloud environments. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Restrict network access to only approved sources 
+  Minimizes risk of unauthorized or malicious traffic 
+  Enables granular, instance-level security controls 

## Implementation guidance
<a name="implementation-guidance-17"></a>
+  Define least-privilege inbound and outbound rules matching only approved network prefixes. 
+  Regularly review and update rules for accuracy and compliance. 

## Resources
<a name="resources-16"></a>
+  [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) 
+  [Control subnet traffic with network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) 
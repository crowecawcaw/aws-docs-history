

# HNSEC01-BP01 Implement network segmentation and least-privilege access control
<a name="hnsec01-bp01"></a>

 Segment your hybrid network using accounts, cloud networks, and on-premises controls to isolate regulated workloads. Enforce least-privilege connectivity by restricting traffic with network access controls. 

 **Desired outcome:** Sensitive workloads and data are isolated, with only authorized access allowed, reducing compliance scope and limiting potential exposure. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Reduces compliance audit complexity and risk 
+  Minimizes lateral movement and impact of security incidents 
+  Aligns with regulatory requirements for network isolation 
+  Enables focused monitoring and incident response 

## Implementation guidance
<a name="implementation-guidance-7"></a>
+  Create separate accounts for different workloads (for example, production, development, and regulated environments). For example, you can achieve this using service such as AWS Organizations. 
+  Design isolated networks for sensitive workloads and segment further using services such as Amazon VPC. 
+  Control network traffic access using services such as AWS security groups to tightly control allowed traffic at the instance level or use network access control lists for subnet-level control. 
+  Configure route tables to enforce segmentation, such as using AWS Transit Gateway route tables or AWS Cloud WAN segments. 
+  Regularly review and update access control for least-privilege access. 

## Resources
<a name="resources-6"></a>
+  [Best practices for a multi-account environment](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html) 
+  [Ensure internetwork traffic privacy in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) 
+  [Transit Gateway Segmentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html) 
+  [AWS Cloud WAN Segment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-segments.html) 


# HNSEC02-BP02 Use a central networking account to host all hybrid networking resources
<a name="hnsec02-bp02"></a>

 A central networking account makes it easier to manage network infrastructure and control access to it. By consolidating networking components in a centralized account, organizations gain improved visibility across their entire network topology, reduce redundant connections, streamline troubleshooting, and enable more efficient scaling as business needs evolve. This centralized model also supports separation of duties, allowing networking specialists to maintain connectivity services while application teams focus on their core responsibilities. 

 **Desired outcome:** Simplified and consistent management, governance, and security for all hybrid networking resources across your cloud environment. 

 **Level of risk exposed if this best practice is not established:** High 

 **Benefits of establishing this best practice:** 
+  Centralizes management of networking infrastructure 
+  Simplifies access controls and governance 
+  Reduces configuration errors and operational overhead 
+  Enables secure resource sharing across multiple accounts 
+  Facilitates compliance and auditability 

## Implementation guidance
<a name="implementation-guidance-11"></a>
+  Designate a dedicated account as your central networking account within your landing zone or multi-account environment. 
+  Deploy shared networking resources in this central networking account. 
+  Share networking resources with other accounts as needed. For example, you can use [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) to share resources. 
+  Control access to networking resources using service such as AWS IAM and resource-based policies. 

## Resources
<a name="resources-10"></a>
+  [Infrastructure OU - Network account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) 
+  [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) 
+  [Share your VPC subnets with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) 
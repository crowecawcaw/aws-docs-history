

# Networking architecture
<a name="networking-architecture"></a>

The solution uses a single Amazon VPC with the following configuration:
+  **Public Subnets** – Host NAT Gateway for outbound internet access
+  **Private Subnets** – Host MSK cluster and ElastiCache for security
+  **Security Groups** – Restrict traffic between components following least-privilege principles
+  **VPC Endpoints** – Enable private connectivity to AWS services where applicable

The networking architecture supports both public internet access and private network configurations through VPC peering or AWS Transit Gateway.
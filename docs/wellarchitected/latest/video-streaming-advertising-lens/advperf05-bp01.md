

# ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance
<a name="advperf05-bp01"></a>

 Establish private connections between your virtual network and managed cloud services such as object storage, databases, caching, and streaming. Keeping this traffic off the public internet improves security and reduces network hops and latency variability on the critical bid path. 

 **Desired outcome:** 
+  Traffic between your advertising workloads and AWS services travels entirely within the AWS private network. 
+  Public internet routing is removed from every service call on your data path, which eliminates the routing variability that contributes to p99 latency. 

 **Common anti-patterns:** 
+  Accessing AWS services over public endpoints from within a VPC, which routes traffic through the internet gateway and across the public internet before it reaches the service endpoint. 
+  Using NAT Gateways for traffic to AWS services that support VPC endpoints. 

 **Benefits of establishing this best practice:** 
+  Private connections through AWS PrivateLink keep all traffic between your VPC and AWS services on the AWS backbone network, reducing network hops and removing internet routing variability. 
+  The same configuration that improves performance also reduces the network attack surface, with little additional effort. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every AWS service call from your advertising workload that traverses the public internet is subject to internet routing variability. At the p50 level, this variability is often imperceptible. But at p99 (the tail latency that determines whether bids make it within the auction window) internet routing adds unpredictable overhead that VPC endpoints remove entirely. 

 VPC interface endpoints (AWS PrivateLink) create elastic network interfaces in your VPC subnet with private IP addresses, routing traffic for specific AWS services directly from your VPC to the service without traversing the internet gateway or NAT gateway. For advertising workloads, the highest-priority services to configure with VPC endpoints are those accessed most frequently on the bid evaluation path: S3 (model artifacts, creative assets), DynamoDB (user profiles, audience data), ElastiCache (frequency caps, session data), and Kinesis (bid event streaming). 

 Enable private DNS on VPC endpoints so that service calls automatically route to the private endpoint. Verify that DNS resolution within your VPC returns private endpoint addresses after configuration. Service calls no longer appear in VPC Flow Logs as traffic traversing the internet gateway. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit current data flows to identify public internet routing:** Use VPC Flow Logs with a filter on internet gateway traffic to identify which AWS service calls traverse the public internet. Prioritize VPC endpoint creation for the services with the highest traffic volume on the bid evaluation path. 

1.  **Create VPC interface endpoints for all AWS services on the critical path:** Create VPC endpoints for S3, DynamoDB, ElastiCache, Kinesis, and any other AWS services called during bid evaluation. Enable private DNS on each endpoint so that existing service calls automatically route to the private endpoint without application code changes. Associate security groups that allow inbound HTTPS (TCP 443) from your bidder compute. 

1.  **Verify traffic routing after endpoint creation:** Confirm that service calls are no longer traversing the internet gateway by checking VPC Flow Logs after endpoint creation. For DynamoDB and S3, verify that DNS resolution returns a private IP address (in your VPC CIDR range) rather than a public AWS endpoint address. Monitor data transfer costs in [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/). NAT Gateway data processing charges should decrease as traffic shifts to VPC endpoints. 

1.  **Create VPC endpoint policies to restrict access:** For sensitive advertising data stores (audience data, campaign configurations), configure VPC endpoint policies that restrict which principals and actions can be performed through the endpoint. This adds a network-level access control layer in addition to IAM policies. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) 
+  [Simplify private connectivity to Amazon DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/) 
+  [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) 

 **Related services:** 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
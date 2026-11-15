

# ADVCOST03-BP01 Consider private communication channels between SSP and DSP
<a name="advcost03-bp01"></a>

 Private communication channels keep traffic secure and reduce internet egress charges. When you connect supply-side and demand-side platforms over private endpoints, bid data stays off the public internet. This practice can improve performance while simplifying network architecture. 

 **Desired outcome:** 
+  Traffic between your advertising workloads and AWS services travels entirely within the AWS private network. Public internet routing and NAT Gateway charges are avoided in your data path. 
+  SSP-to-DSP bid traffic flows over private endpoints when both parties are on AWS, avoiding internet egress charges. 

 **Common anti-patterns:** 
+  Using NAT Gateways for traffic to AWS services (S3, DynamoDB, and Kinesis) that support VPC endpoints, which adds $0.045/GB data processing cost and latency unnecessarily. 
+  Routing inter-service traffic over public internet by default, so egress charges accrue on every hop and bid data becomes visible to network observers. 

 **Benefits of establishing this best practice:** 
+  Elimination of NAT Gateway data processing charges for high-volume AWS service API calls. 
+  Reduced internet egress charges by keeping traffic within the AWS network. 
+  Stronger security posture, as bid data, user signals, and auction results never traverse the public internet. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Programmatic advertising generates large traffic volumes between bidding infrastructure and AWS services. Every API call to Amazon S3, Amazon DynamoDB, or Amazon Kinesis that routes through a NAT Gateway incurs data processing charges on top of standard egress pricing. At millions of queries per second, these charges can exceed the cost of the services themselves. You decide whether to route this traffic over the public internet (through NAT Gateways or internet gateways) or keep it on the AWS private backbone through [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). If a single endpoint replaces moderate NAT Gateway throughput, it pays for itself quickly. 

 Service traffic (bidder nodes calling AWS APIs) benefits from VPC interface endpoints, which intercept API calls at the DNS layer and route them privately without code changes. Partner traffic (SSP-to-DSP bid requests between separate AWS accounts or organizations) requires either [PrivateLink endpoint services](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html) or [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/), depending on whether the partner relationship is bilateral or mediated through an exchange. 

 Teams often deploy VPC endpoints but leave NAT Gateways in place. Residual traffic continues routing through NAT because DNS resolution is cached, security group rules still permit the old path, or a subset of services was missed during migration. Without validation that the old path carries zero RTB traffic, teams pay for both the endpoints and the NAT Gateway. Use VPC Flow Logs to confirm migration is complete before decommissioning. 

 [AWS Direct Connect](https://aws.amazon.com/directconnect/) provides dedicated private bandwidth between on-premises bidding infrastructure and AWS, but requires physical cross-connects and longer provisioning timelines. The cost savings over internet egress are substantial at scale, though the commitment model (one-year or three-year reserved capacity) demands accurate traffic forecasting. 

 A shared VPC endpoint handles all workloads in the VPC, which makes cost attribution difficult unless teams tag their traffic or use separate endpoints per workload. A misconfigured shared endpoint disrupts all consumers, and per-team endpoints multiply hourly charges. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Create VPC interface endpoints for all AWS services on the bid path:** Deploy PrivateLink endpoints for S3, DynamoDB, Kinesis, SQS, and CloudWatch in each subnet used by bidding infrastructure. Enable private DNS on each endpoint so existing code automatically routes to private endpoints without changes. Verify that traffic is using private endpoints by checking that NAT Gateway BytesProcessed drops after endpoint creation. 

1.  **Establish PrivateLink for partner SSP/DSP connectivity on AWS:** Configure PrivateLink endpoint services for your bid endpoints that partners can consume from their own VPCs. This keeps all bid traffic private without requiring VPC peering or public endpoints. Prioritize the highest-volume partner connections for immediate PrivateLink migration. 

1.  **Remove NAT Gateways dedicated to RTB traffic:** After migrating all bid-path traffic to VPC endpoints and PrivateLink, identify NAT Gateways that are no longer needed. Validate using VPC Flow Logs that no RTB traffic still traverses them. Decommission unused NAT Gateways and update infrastructure as code to guard against recreation. 

1.  **Monitor data transfer costs before and after migration:** Use AWS Cost Explorer to track NAT Gateway data processing charges before migration. Compare monthly charges after PrivateLink deployment to quantify savings. Track VPC endpoint hourly charges ($0.01/hour/endpoint/Availability Zone) against NAT Gateway savings to confirm net cost reduction. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS lowers data processing charges for AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2021/07/aws-lowers-data-processing-charges-aws-privatelink/) 
+  [Get started with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html) 

 **Related services:** 
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 


# ADVCOST03-BP03 Co-locate bidder and database nodes
<a name="advcost03-bp03"></a>

 Keeping bidder and database nodes together can help transactions occur quickly and can also reduce inter-AZ and inter-Region traffic charges. 

## Implementation guidance
<a name="implementation-guidance-65"></a>

 To optimize costs when configuring advertising bidder nodes to communicate with database nodes within the same Availability Zone, consider the following guidance: 

1.  **Resource placement:** Carefully plan the placement of your bidder nodes and database nodes across Availability Zones. Co-locate bidder nodes and their corresponding database nodes within the same Availability Zone to minimize cross-AZ data transfer costs. 

1.  **Database configuration:** If using a managed database service like Amazon RDS, configure your database instances to use multi-AZ deployment within the same AWS Region. This separates the primary and standby database instances into separate Availability Zones, providing high availability while minimizing cross-AZ data transfer costs for your bidder nodes. 

1.  **Network configuration:** Configure your VPC and subnets to verify that bidder nodes and database nodes within the same AZ can communicate efficiently. Use private IP addresses, and avoid public IP addresses or internet gateways, which can incur additional data transfer costs. 

1.  **Caching and replication:** Implement caching strategies and read replicas for your database nodes to reduce the amount of data transfer required between bidder nodes and database nodes. This can further minimize cross-AZ data transfer costs. 

1.  **Monitoring and optimization:** Regularly monitor your data transfer costs and traffic patterns across AZs. Adjust your resource placement and network configurations as needed to optimize cost-effectiveness. 

1.  **Use cost optimization tools:** Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), and [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to monitor and analyze your costs, set budgets, and receive alerts for potential cost anomalies. 

## Key AWS services
<a name="key-aws-services-36"></a>

 [Network Load Balancer (NLB) ](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) 

## Resources
<a name="resources-59"></a>
+  [Exploring Data Transfer Costs for AWS Managed Databases](https://aws.amazon.com/blogs/architecture/exploring-data-transfer-costs-for-aws-managed-databases/) 
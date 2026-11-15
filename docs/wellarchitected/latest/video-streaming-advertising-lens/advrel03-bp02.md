

# ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements
<a name="advrel03-bp02"></a>

 Select AWS Regions based on compliance and disaster recovery needs, including data jurisdiction requirements (for example, GDPR and CCPA) and system redundancy for advertising audience data. 

 **Desired outcome:** 
+  AWS Region selection satisfies both legal data residency requirements for advertising audience data and disaster recovery requirements for system availability. 
+  Multi-region deployments for RTB and ad delivery services match user geography to minimize latency while maintaining data residency compliance. 
+  Regional redundancy provides failover capability for highest-tier advertising components. 

 **Common anti-patterns:** 
+  Selecting AWS Regions on cost or latency alone without checking data residency obligations for the audience data processed there. 
+  Replicating EU or California user data to noncompliant regions without GDPR/CCPA review or adequacy safeguards. 
+  Relying on documentation alone to enforce residency instead of technical guardrails like AWS Control Tower Region-deny SCPs. 
+  Routing all intake traffic to a single Region regardless of user geography, so latency rises and regional failover is gone. 

 **Benefits of establishing this best practice:** 
+  Region selection satisfies both data residency law and disaster recovery requirements simultaneously. 
+  Geolocation and latency-based routing minimize bid-path latency while keeping data in permitted Regions. 
+  Regional redundancy provides failover capability for the highest-tier advertising components. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Low latency requires placing the auction close to where impressions originate. The bid deadline is fixed, and every millisecond of round trip reduces the time available to decide. Data protection law requires placing personal data where its subjects live, and sometimes keeping it there. The two requirements agree when a viewer's traffic and their data belong in the same place. They conflict when you add redundancy, because the obvious failover target for a low-latency region might be a region the data cannot legally reach. Filter candidate regions by residency requirements first, then choose within that set by latency. 

 To apply that constraint, you must know the rules that governs the specific data you store or use. The answer differs by data type, not by workload. A campaign configuration contains no personal data and can be stored in any Region. The viewer's jurisdiction governs any bid request that contains viewer signals. An audience segment derived from that request might inherit those obligations, along with the consent scope that authorized it. A single service touches all three, and a service-level residency decision cannot fit them all. 

 When application logic enforces residency, every service must implement residency correctly, including services written later by employees who are unaware of the requirement. If any service implements incorrectly, there are no signals or alerts to determine that. Enforcing at the account boundary makes the restriction a property of the environment, so a misconfigured service is prevented, not trusted. This enforcement itself is flawed, as it lacks specific determination. For example, an environment-level restriction can't distinguish a legitimate exception from a violation. It produces a permission error that gives no indication that a residency policy caused it. 

 Cross-Region replication is where residency and reliability conflict, because replication is a data transfer and transfers are what the law regulates. Multi-Region redundancy for a global dataset such as frequency capping conflicts with keeping regional data in region, and no configuration satisfies both. Partition the data so each Region holds only what it may, and accept that some cross-region behavior becomes approximate. Keep the data unified only when the narrower set of lawful regions is acceptable. Making this choice without noticing the trade-off leaves replication technically correct and legally exposed. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Map data types to regulatory jurisdictions:** Create a data residency matrix that identifies each data type (bid request data, user profiles, campaign configurations, and audience segments) and the regulatory framework that governs it (GDPR for EU data, CCPA for California data). For each data type, document the permitted processing regions and replication restrictions. 

1.  **Apply AWS Control Tower Region deny SCPs:** Configure Service Control Policies at the AWS Organizations level that restrict specific account types from creating resources outside permitted regions. For accounts that process EU advertising audience data, deny all services outside EU regions (eu-west-1, eu-central-1, etc.). Test SCPs in a non-production account before applying to production. 

1.  **Configure Route 53 for geographic and latency-based routing:** Set up Route 53 health checks on regional workload endpoints. Configure geolocation routing to direct EU publisher traffic to EU regions and North American traffic to US regions. Use latency-based routing within continents to direct traffic to the lowest-latency regional endpoint. Set failover routing as a secondary policy to redirect traffic to an alternative region when the primary region's health check fails. 

1.  **Deploy DynamoDB global tables for globally distributed advertising data:** For user profile data that needs to be accessed from multiple regions with low latency (frequency capping across regions, global campaign configurations), use DynamoDB global tables. Configure tables in the regions where you have active advertising workloads. Understand that global table replication has eventual consistency: design frequency capping logic to tolerate brief over-delivery rather than blocking bids on replication lag. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL07-BP01 Design resilient architectures with privacy-preserving fault tolerance](advrel07-bp01.md) 
+  [ADVREL04-BP05 Back up data in multiple locations with consideration for regulatory requirements](advrel04-bp05.md) 
+  [ADVREL05-BP03 Deploy partner-facing bid gateways in multiple AWS Regions](advrel05-bp03.md) 

 **Related documents:** 
+  [Navigating GDPR Compliance on AWS](https://aws.amazon.com/compliance/gdpr-center/) 
+  [Deny services and operations for AWS Regions of your choice with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/region-deny.html) 

 **Related services:** 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/) 
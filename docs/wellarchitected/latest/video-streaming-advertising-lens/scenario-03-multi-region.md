

# Scenario 3: Multi-region advertising workloads

 Global advertising platforms serve publishers and demand partners across continents with different latency requirements, data residency regulations, and resilience goals. The architecture must balance performance, compliance, and cost, routing traffic to the right region while keeping data in the right jurisdiction. 

## Characteristics
<a name="s03-characteristics"></a>
+  Publishers and demand partners distributed across North America, Europe, and Asia-Pacific. 
+  Data residency requirements restrict EU user data to EU regions and California data to US regions (GDPR, CCPA). 
+  Sub-100 ms bid response SLOs require compute geographically near both publishers and demand partners. 
+  Campaign data (frequency caps, pacing) must be consistent across regions. 
+  High cross-region data transfer costs if replication isn't carefully managed. 
+  Advertising customers accept ranges from milliseconds to hours as appropriate recovery depending on the component. 
+  DSP and SSP traffic patterns are local within regional boundaries because of latency concerns. 

## Reference architecture
<a name="s03-reference-architecture"></a><a name="scenario-03-fig1"></a>

![Ad insertion live media workflow on AWS showing multi-region live stream origination, ad decision servicing, and ad insertion for continuous live advertising](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-03a-ad-insertion-live-media.jpg)

*Ad insertion live media workflow on AWS*


 The architecture consists of the following components: 

1.  **Amazon Route 53 (geolocation routing)**: Routes incoming intake traffic from publishers to the nearest regional workload based on geographic origin. EU publisher traffic routes to EU regions, and North American traffic routes to US regions. Failover routing policies provide resilience if a region becomes unhealthy. 

1.  **Regional ad serving workloads**: Independent copies of the complete ad serving stack (SSP, auction engine, creative serving, data stores) in each Region. Traffic patterns between an ad network and DSP are local within regional boundaries because of latency constraints. 

1.  **Intra-region traffic distribution**: Within the Americas, Route 53 weighted routing splits traffic between us-east and us-west in a 70:30 ratio, with automatic failover routing 100% to the healthy region if one fails. The same pattern applies within each continent. 

1.  **DynamoDB Global Tables**: Campaign configurations, frequency caps, and budget pacing data that must be consistent across all regions use DynamoDB Global Tables with eventual consistency. Replication lag is typically under 1 second. Design frequency capping to tolerate brief over-delivery rather than blocking bids on replication lag. 

1.  **Scheduled user profile synchronization (Step Functions \+ Lambda)**: User profile data is stored primarily in the Region closest to the user. An AWS Step Functions workflow runs 2–4 times daily to synchronize changed profiles to secondary regions using delta replication (only records changed since the last sync). Real-time replication isn't needed because users are rarely in two geographic locations simultaneously. 

1.  **AWS Control Tower \+ SCPs**: Service Control Policies at the AWS Organizations level restrict resources in EU-designated accounts to EU regions. IAM Permission Boundaries with aws:RequestedRegion conditions provide defense in depth for data residency enforcement. 

## Configuration notes
<a name="s03-configuration-notes"></a>

### Geographic routing
<a name="geographic-routing"></a><a name="scenario-03-fig2"></a>

![Intake traffic distribution across continents using Route 53 geolocation routing, directing publisher ad request traffic from EU, Americas, and APAC origins to the nearest regional ad serving workloads](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-03b-ads-traffic-distribution-1.jpg)

*Intake traffic distribution across continents*
<a name="scenario-03-fig3"></a>

![Intra-continent traffic distribution with Route 53 weighted routing between regional endpoints, including health-check-driven failover between us-east and us-west](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-03b-ads-traffic-distribution-2.jpg)

*Intra-continent traffic distribution with weighted routing and failover*


 Configure Amazon Route 53 with continent-based geolocation routing as the first-level policy. Within each continent, use latency-based routing to select the lowest-latency regional endpoint. Add health checks on regional ALBs so that failover activates automatically when a region is degraded. Test routing behavior by simulating requests from each geographic origin before go-live. 

### Data residency enforcement
<a name="data-residency-enforcement"></a><a name="scenario-03-fig4"></a>

![Regional ad serving workload interacting with multiple DSPs at a Regional level on AWS, keeping bidding traffic local to the Region to meet latency budgets and residency constraints](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-03c-regional-ad-serving.jpg)

*Regional ad serving workload with multi-DSP interaction at a Regional level*


 Activate Service Control Policies that deny resource creation outside permitted regions for accounts processing EU or California personal data. Test SCPs in non-production before applying to production. Use Amazon Macie to regularly verify that personal data has not drifted outside permitted regional boundaries. 

### Campaign data consistency
<a name="campaign-data-consistency"></a>

 Use DynamoDB Global Tables for frequency cap data, campaign budget pacing, and targeting parameters. Configure the replica tables in all regions where you operate active bidding workloads. Accept eventual consistency for frequency capping. Brief over-delivery (serving one extra impression during cross-region replication lag) is preferable to blocking bid responses waiting for synchronous confirmation. 

### User profile placement
<a name="user-profile-placement"></a>

 Store user profiles in the AWS region closest to where users are located. For North American users, store in us-east-1 or us-west-2 based on geographic distribution. For EU users, store in eu-west-1 or eu-central-1. Configure bidding infrastructure to route profile lookups to the regional store, never cross-region on the bid path. 

### Cost management
<a name="cost-management"></a>

 Schedule cross-region user profile synchronization during off-peak hours (typically 2am–6am local time) to minimize impact on bid path infrastructure. Replicate only changed records using DynamoDB Streams markers rather than full table copies. Track cross-region data transfer costs in AWS Cost Explorer filtered by the data transfer service to validate that synchronization costs are materially lower than real-time replication. 
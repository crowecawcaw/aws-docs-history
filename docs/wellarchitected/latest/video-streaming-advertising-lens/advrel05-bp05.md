

# ADVREL05-BP05 Maintain independent operational readiness in each Region
<a name="advrel05-bp05"></a>

 During a Regional event, the control plane you rely on to deploy and manage RTB Fabric gateways can be impaired in the affected Region. If your operational tooling or deployment artifacts are centralized there, you lose the ability to scale, reconfigure, or redeploy gateways in the surviving Region. A Region can hold every template and enough instances to serve peak QPS and still be commercially unready, because cold targeting indexes can miss tmax, a stale line-item index can bid on paused campaigns, an unregistered endpoint can receive no traffic, and independently maintained pacing state can spend duplicated advertiser budgets the moment both Regions serve. 

 **Desired outcome:** 
+  Each Region independently holds its own deployment artifacts and operational tooling, and current bidding data (line items and campaign state, targeting and audience-segment indexes, CTR/CVR and bid-shading model artifacts) within a defined, monitored freshness bound, with no cross-Region dependency during an event. 
+  Budget pacing and frequency-cap state is globally consistent rather than maintained for each Region, with a defined divergence budget and a reconciliation step in the failover plan. 
+  Each Region is pre-provisioned and pre-warmed to absorb full peak bid traffic with live-event headroom, with endpoints registered and QPS allocation pre-agreed with every exchange partner. Where full absorption is not economic, a prioritized supply shed order protects PMP and guaranteed deal obligations ahead of open-market traffic. 
+  The campaign trafficking and budget control plane, and the bid log and billing reconciliation path, survive the loss of either Region. 
+  Failover is automated as code, and failback is a deliberate process gated on auction-quality signals, restored QPS allocation, and pacing-state reconciliation. 

 **Common anti-patterns:** 
+  Centralizing deployment artifacts or operational tooling in the primary Region, or treating readiness as an artifact and capacity question only, so a Regional impairment removes the ability to manage the surviving Region and leaves it bidding a stale line-item, segment, or model view of the book. 
+  Maintaining budget pacing and frequency-cap counters independently for each Region, so both Regions pace to the full campaign budget and over-deliver, which produces advertiser make-goods that aren't reported by availability metrics. 
+  Pre-provisioning instance capacity but not cache, index, and connection warmth, so the standby Region's first auctions miss tmax and the exchange reads the failover as a demand outage. 
+  Sizing the standby Region for average traffic rather than peak QPS with live-event headroom, or holding capacity in a Region whose endpoints were never registered with each exchange or that holds only its steady-state QPS allocation, so traffic never arrives to use it. 
+  Running a single-Region campaign trafficking or budget API, or a regional bid log pipeline, so an over-delivering campaign cannot be paused and impressions won in the impaired Region are lost to billing. 
+  Executing failover from human-run wiki runbooks under pressure, or allowing automatic failback to a still-recovering Region. 

 **Benefits of establishing this best practice:** 
+  The surviving Region can be managed and scaled independently of the impaired Region's control plane. 
+  Pre-provisioned and pre-warmed full-load capacity means failover succeeds without racing an impaired control plane and without a cold-start window that exchanges read as a demand outage. 
+  Freshness bounds on bidding data mean the standby Region bids the current book. 
+  Globally consistent pacing and frequency state prevents the over-delivery and make-good exposure that a Regional failover otherwise creates. 
+  Pre-registered endpoints and pre-agreed allocation mean the surviving Region receives the traffic its capacity was sized for, and a prioritized shed order makes an under-capacity failover a deliberate commercial choice. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A recovery path must be exercised in order to be considered a valid option. Deploying and scaling gateways relies on control plane services, and those services can themselves be impaired in the failing Region. When your tooling or artifacts are only in that Region, the failure removes your ability to respond along with it. 

 For a bidder, the inventory that must be independently present is larger than templates and state files. A bidder answers an auction from data that changes continuously, such as the line-item and campaign book, targeting and audience-segment indexes, and the model artifacts that score and shade bids. Each dataset has a freshness bound beyond which the Region is technically healthy and commercially wrong, bidding on paused campaigns or missing newly launched ones. The standby Region's data age needs its own bound and alarm. 

 *Static stability* underlies this practice. A system is statically stable when it keeps working through a failure without a control plane action to adapt, so each Region already holds the capacity to serve everything before any event starts. A Region can be provisioned and still be cold. Empty targeting indexes, unpopulated bloom filters, and unestablished TLS sessions to exchange endpoints produce responses that arrive after tmax and are discarded upstream, which an exchange reads as a demand outage. Bid QPS follows exchange demand and spikes on scheduled live events, so a standby Region sized for the other Region's average share is under-capacity when a Regional event coincides with peak demand. 

 Gateways receive traffic because each exchange has registered the endpoint and allocated QPS to it, and that allocation is a commercial arrangement with each partner, measured in weeks of lead time. Budget pacing and frequency capping work against Regional independence, because they enforce invariants that are global to a campaign: Regions that each maintain their own pacing state will each pace toward the full budget, and the result is over-delivery and cap breach that appears as an advertiser make-good rather than an availability metric. Store pacing and frequency state where both Regions read a shared view, accept a bounded divergence during partition, and treat reconciliation as a step in the failover and failback procedure. Where full absorption is not economic, the shed order belongs in the design, expressed in exchanges, deal IDs, and spend, protecting PMP and guaranteed deals first. 

 Operational readiness extends to operator controls, as well as the record of issues. A single-Region campaign trafficking or budget API means an over-delivering campaign cannot be paused during the event, and a regional bid log pipeline loses the evidence for impressions won in the Region that failed, making them unbillable. Encode the failover as automation rather than a wiki runbook, because a person under pressure can be slow and error-prone and the event is rare enough that operators cannot stay practiced on the manual procedure. Premature failback can cause a second outage. Wait for auction-quality signals under a ramped share of traffic, exchange-side allocation restored on the partner's timeline, and pacing state reconciled before both Regions pace again. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Replicate deployment artifacts to every Region:** Store all deployment artifacts (such as AWS CloudFormation templates, Terraform state, and infrastructure configuration) in each Region independently, using Amazon S3 Cross-Region Replication for deployment buckets so the surviving Region can modify or redeploy gateways without cross-region dependencies. 

1.  **Replicate bidding data independently in each Region with a freshness bound:** Treat the line-item and campaign book, targeting and audience-segment indexes, and CTR/CVR and bid-shading model artifacts as first-class readiness inputs. Replicate each to every Region, define the maximum tolerable staleness for each (campaign and budget state in seconds to low minutes, segments and models on their own cadence), alarm on the standby Region's data age, and pin compatible model and feature-schema versions in each Region. 

1.  **Hold pacing and frequency state globally, with a bounded divergence and an explicit reconciliation step:** Keep budget pacing counters and frequency-cap state in a store that both Regions can read (for example, Amazon DynamoDB global tables or Amazon ElastiCache Global Datastore) rather than counters in each Region. Define the spend and impression divergence you can accept during a partition, bound pacing authority for each Region to stay inside it, make pacing reconciliation an explicit step in the failover and failback automation, and alarm on delivery against the pacing plan. 

1.  **Pre-provision and pre-warm full peak capacity for each Region:** Size each Region for full peak bid QPS with live-event headroom, not the other Region's average share, and do not rely on scaling up during an event. Keep the standby Region warm as well as provisioned, with loaded targeting and segment indexes, populated bloom filters, and established connections to exchange endpoints, and verify warmth by asserting on bid response rate inside tmax under shadow or probe traffic rather than on instance health checks. 

1.  **Register endpoints and negotiate QPS allocation with every exchange in every Region:** Confirm that each Region's gateway endpoints are registered with each exchange partner and that the pre-agreed QPS allocation in each Region is sufficient to absorb full load. Treat allocation parity as a commercial arrangement with lead time, tracked for each partner, and verify periodically that it has not drifted below the capacity you provisioned. 

1.  **Define a prioritized supply shed order and keep the control plane and bid log path reachable from either Region:** Where absorbing 100% in a single Region is not economic, decide in advance which traffic is dropped and in what order, expressed in exchanges, deal IDs, and spend, protecting PMP and guaranteed deal obligations first and implementing it as configuration the failover automation applies. Verify that the API used to pause campaigns and adjust budgets is available from the surviving Region, and replicate or fan out bid, win, and billing-notice logs out of the Region that produces them so impressions stay reconcilable. 

1.  **Automate failover as code, gate failback on readiness, and run commercially measured game days:** Automate failover (Amazon Systems Manager Automation documents or AWS Step Functions), including applying the shed order, triggering warm-up, and performing pacing reconciliation. Design failback as a deliberate ramp that requires the recovered Region's bid response rate inside tmax, win rate, and clearing price to match the healthy Region, confirms restored QPS allocation against partner-reported figures, and reconciles pacing state before both Regions pace again. Run quarterly game days at production-representative QPS, measuring lost bid opportunities, unspent and over-delivered budget, frequency-cap breach, and impression discrepancy. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP01 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes](advrel04-bp01.md) 
+  [ADVREL03-BP04 Reserve appropriate capacity of services in the supported regions](advrel03-bp04.md) 
+  [ADVREL05-BP03 Deploy partner-facing bid gateways in multiple AWS Regions](advrel05-bp03.md) 
+  [ADVREL05-BP04 Monitor partner-facing bid gateway health independently per Region](advrel05-bp04.md) 

 **Related documents:** 
+  [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) 
+  [Replicating objects within and across Regions (S3 CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) 
+  [Amazon DynamoDB global tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) 

 **Related services:** 
+  [Amazon S3](https://aws.amazon.com/s3/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon Route 53 Application Recovery Controller](https://aws.amazon.com/route53/application-recovery-controller/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
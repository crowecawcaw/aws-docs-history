

# ADVREL01-BP06 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful

 When deploying new code to a programmatic bidder, use phased deployment (for example, blue/green or rolling) and gate each phase on auction-side signals rather than on fleet percentages. A bidder that breaks under deployment misses the exchange's tmax, returns a well-formed no-bid from a cold index, or loses budget pacing state. Derive phase boundaries, validation windows, and rollback triggers from auction and billing quantities. 

 **Desired outcome:** 
+  Bid response rate inside each exchange's tmax holds throughout the deployment, as measured by exchange-reported counts. 
+  Budget pacing and frequency-cap state survive the deployment, so delivery keeps tracking the pacing plan and no advertiser make-goods are triggered. 
+  Won impressions stay billable: win notices (nurl) and billing notices (burl) resolve against a reachable bid cache, with no impression discrepancy against exchange-reported counts. 
+  Phase size is expressed in supply partners, Regions, and cost at risk, and rollback returns to the previous version within defined RTO bounds, with the previous fleet retained until the billing-notice tail drains. 

 **Common anti-patterns:** 
+  Shifting live auction traffic to a fleet with cold line-item, audience-segment, and bid-shading indexes, which produces a near-zero win rate that exchanges read as a demand outage. 
+  Running blue/green on the pacing tier with no state handoff, so the new fleet starts from zeroed pacing counters and over-delivers against campaign budgets. 
+  Tearing down the previous fleet on a fixed timer rather than after the p99.9 bid-to-burl interval, which risks won impressions and widens the discrepancy against the exchange. 
+  Alarming only on 5xx rate and latency, which are blind to tmax timeouts and invalid OpenRTB responses, the dominant deployment failure modes for a bidder. 
+  Sizing batches as a percent of fleet, which leaves the exposure of a single high-value exchange or deal ID unstated. 
+  Advancing phases concurrently across regions that serve the same exchange's redundant endpoints, so a bad build leaves no healthy endpoint to fall back to. 

 **Benefits of establishing this best practice:** 
+  Deployment defects appear in a small, named set of supply partners before reaching the full demand footprint. 
+  Pacing and frequency-state continuity hels you avoid budget over-delivery, which does not appear in availability monitoring but does appear to advertisers. 
+  Retaining the previous fleet through the billing-notice tail helps maintain revenue on won impressions. 
+  Gating on exchange-reported timeout rate protects QPS allocation, which exchanges shape down after timeouts. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Choose between blue/green and rolling based on where state is stored. In blue/green, rollback is a routing change, which matters most for bid evaluation engine changes, where correctness is difficult to test exhaustively and a defect must be reversible in seconds. Blue/green has structural costs: a second full-capacity fleet doubles spend for the deployment window, and the state accumulated in the old environment does not follow the traffic switch. For a bidder, that state includes warm caches, demand-partner connection pools, budget pacing counters, frequency cap counters, and the bid cache that resolves win and billing notices. A green fleet serving its first auctions with cold targeting indexes can breach tmax as effectively as a bad build, and one starting from zeroed pacing state can over-deliver against campaign budgets. 

 Rolling deployment has no duplicate fleet and no state cliff, in exchange for a mixed-version period in which old and new code serve the same auction stream. Two versions that write to shared stores must stay mutually compatible, and a schema or contract change that is obvious in blue/green can become a corruption risk during a roll. Programmatic adds hazards where model artifacts deploy on a different cadence than bidder code, so a roll can run new code against an old feature schema, and a roll overlapping an online experiment introduces an unplanned version split that biases the readout. 

 Size each phase by auction exposure, not by percent of fleet (for example, which exchanges, which deal IDs, and how much budget is at risk before an issue occurs). Pause between phases long enough for auction-quality signals to accumulate and for pacing defects to appear after a control-loop cycle. Keep initial rollouts small. Although code can be rolled back quickly, exchanges reduce QPS allocation to bidders that time out, and that capacity isn't automatically restored after a rollback. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Pre-warm the green fleet with shadow bid traffic before it takes live auctions:** A bidder's first seconds contain its worst features, such as cold line-item and audience-segment indexes, empty bloom filters, and unestablished TLS sessions to exchange endpoints. Mirror a sample of production bid requests to green with discarded responses, and gate the traffic shift on green's shadow bid response rate and clearing price distribution matching blue within tolerance. 

1.  **Hand off pacing and frequency-cap state explicitly, or keep the pacing tier off blue/green:** Budget pacing controllers and frequency-cap counters hold spend state that does not follow a target-group switch, and a green fleet that starts from zeroed counters can over-deliver against budgets. Either keep pacing state in an external store both fleets read (for example, Amazon ElastiCache or Amazon DynamoDB) so the switch is stateless, or exclude the pacing tier from blue/green and roll it with pacing state drained between batches. Verify delivery against the pacing plan before declaring success. 

1.  **Size previous-fleet retention by the win-notice and billing-notice tail:** Win notices (nurl) and billing notices (burl) arrive against bid IDs held in the bid cache quickly after the bid. Measure the p99.9 bid-to-burl interval for your top exchanges and set retention above it, or move the bid cache to a shared store so either fleet can resolve a notice. 

1.  **Phase by supply partner and Region:** Route one lower-value supply partner or low-share Region to the new version first, so the amount of risk has a definitive, tangible answer. Never advance phases concurrently across Regions serving the same exchange's redundant endpoints. Deploy outside peak dayparts, away from live-event spikes, and not at the top of the hour when pacing intervals reset. 

1.  **Alarm on programmatic signals and set validation windows by auction sample size:** Configure automatic rollback (AWS CodeDeploy) on bid response rate inside tmax, exchange-reported timeout rate, invalid bid response rate (OpenRTB validation failures), win rate, clearing price drift, and impression discrepancy against exchange-reported counts. Keep 5xx and latency as secondary signals. Hold each phase until you have a readable win sample per demand partner and per deal ID and at least two full pacing-controller intervals. Pin compatible model versions so new code cannot read an old feature schema, and stamp bid logs with build ID so a running experiment can exclude the mixed window. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP05 Through your CI/CD pipeline, implement regression, performance, and canary tests](advrel01-bp05.md) 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 

 **Related documents:** 
+  [BlueGreen Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html) 
+  [Rolling deployments](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html) 
+  [Automatic rollbacks in AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html) 

 **Related services:** 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) 
+  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
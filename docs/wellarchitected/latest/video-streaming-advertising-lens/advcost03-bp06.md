

# ADVCOST03-BP06 Maximize partner traffic routed inside a managed connectivity fabric
<a name="advcost03-bp06"></a>

 Traffic between two RTB Fabric customers costs far less than traffic sent externally, roughly 6.7 to 10 times less per billion transactions depending on Region and volume tier (about 7.5 times for US and EU traffic at the first tier). When you encourage partners to adopt RTB Fabric, both sides save, and those savings grow as more partners join. 

 **Desired outcome:** 
+  The majority of RTB partner traffic flows within the shared RTB Fabric connectivity. 
+  You engage partners directly about the mutual cost savings from internal routing. 
+  You track the ratio of inside to external traffic and set targets to raise the inside percentage. 

 **Common anti-patterns:** 
+  Adopting RTB Fabric for your own traffic but not actively encouraging partners to join, so the severalfold cost reduction available when both parties route internally never materializes. 
+  Treating partner connectivity decisions as purely technical and never communicating the mutual cost savings opportunity to partner business or finance teams who influence adoption decisions. 
+  Onboarding partners to RTB Fabric in random order rather than prioritizing by traffic volume, which delays the largest cost savings while focusing on low-volume partners with minimal impact. 
+  Failing to track the ratio of inside compared to external traffic over time. 
+  Assuming partners will discover and adopt RTB Fabric on their own without outreach, so adoption stalls when a small coordination effort would produce mutual savings. 

 **Benefits of establishing this best practice:** 
+  6.7-10x lower cost per billion transactions for inside compared to external traffic, depending on Region and volume tier. 
+  Mutual savings give partners a direct incentive to adopt. 
+  Reduced QPS throttling by partners leads to higher bid volumes and revenue. 
+  Lower latency for inside-fabric connections improves auction competitiveness. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [RTB Fabric](https://aws.amazon.com/rtb-fabric/) distinguishes between *inside* traffic, where both parties are RTB Fabric customers, and *external* traffic, where one party routes through the public internet. The per-billion-transaction price for inside traffic is roughly 7.5 times lower than external traffic, so every partner that joins the fabric reduces costs for all existing participants who transact with them. Your inside traffic ratio, the percentage of total RTB transactions routed inside the fabric, is the primary metric for tracking cost optimization progress over time. 

 The engineers who configure connectivity are rarely the people who approve new vendor integrations or evaluate cost structures, and finance and business development teams at partner organizations control adoption timelines. When you frame the conversation around mutual savings, where both the SSP and DSP benefit from lower per-transaction costs, you can accelerate decisions that would otherwise stall in procurement queues. Without business-level engagement, adoption typically plateaus after two or three partners. 

 A single high-volume partner moved to inside routing can reduce monthly costs more than ten low-volume partners combined. To prioritize, rank partners by monthly transaction count and multiply by the inside-to-external price difference, which gives you a dollar value per migration. Partners already evaluating RTB Fabric on their own are the lowest-effort wins and should move first regardless of volume ranking. 

 Partners with existing private connectivity (AWS PrivateLink or AWS Direct Connect) might see less added benefit from RTB Fabric if their current costs are already low, and partners locked into annual commitments with other connectivity providers might delay adoption until renewal. Understand these blockers early so you can focus outreach on partners whose timing aligns. 

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics on RTB Fabric links break down traffic by routing type. Without this tracking, you can't quantify the savings you've realized, spot partners whose traffic routes externally because of failover, or report progress to leadership. Set a target ratio, such as 80% inside within six months. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Rank partners by monthly transaction volume:** Use RTB Fabric link metrics to identify which partners are already on the fabric (inside routing) and which still route externally. Calculate the monthly savings opportunity from migrating each external partner to inside routing. 

1.  **Share pricing comparisons with partner technical and finance teams:** Give partners concrete data showing the price difference between inside and external routing. The mutual benefit, where the SSP saves on request costs and the DSP saves on response costs, makes the business case work for both parties. 

1.  **Establish RTB Fabric links with priority partners:** Create requester and responder gateway connections for priority partners through the RTB Fabric console. Monitor the inside-to-external traffic ratio, targeting 80% or more inside routing within 6 months. 

1.  **Review monthly Cost Explorer to validate realized savings:** Compare monthly costs before and after partner migrations. Track the inside traffic percentage as a leading indicator of future savings as additional partners migrate. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP05 Replace per-gigabyte egress with transaction-priced partner connectivity](advcost03-bp05.md) 
+  [ADVCOST03-BP08 Use volume-tier pricing by consolidating traffic](advcost03-bp08.md) 

 **Related documents:** 
+  [AWS RTB Fabric Pricing](https://aws.amazon.com/rtb-fabric/pricing/) 
+  [AWS RTB Fabric Customers](https://aws.amazon.com/rtb-fabric/customers/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
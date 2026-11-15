

# ADVCOST03-BP08 Use volume-tier pricing by consolidating traffic
<a name="advcost03-bp08"></a>

 RTB Fabric pricing drops sharply after the first 2 trillion transactions per month. When you consolidate traffic from multiple accounts or partners under a single billing entity, you reach lower pricing tiers faster and lower per-transaction costs. 

 **Desired outcome:** 
+  RTB traffic is consolidated to maximize volume-tier discounts. 
+  Monthly transaction volume against tier thresholds is monitored with alerts when approaching the next tier breakpoint. 

 **Common anti-patterns:** 
+  Running RTB traffic through separate AWS accounts or billing entities without consolidation, which keeps aggregate volume below the tier thresholds that would reduce per-transaction costs for all traffic. 
+  Splitting traffic across multiple connectivity solutions rather than consolidating eligible traffic onto the volume-discounted fabric. 
+  Failing to model how close current monthly transaction volume is to the next pricing tier, so opportunities to route additional partner traffic through RTB Fabric and trigger tier discounts are left unrealized. 
+  Treating each business unit's RTB traffic independently without evaluating consolidated billing, which pays higher per-transaction rates across all units when combined volume would qualify for lower tiers. 

 **Benefits of establishing this best practice:** 
+  67% reduction in per-transaction cost when reaching the higher volume tier (inside traffic). 
+  71% reduction for external traffic at the higher volume tier. 
+  Predictable marginal cost improvement as business grows. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [RTB Fabric pricing](https://aws.amazon.com/rtb-fabric/pricing/) uses volume tiers where the per-transaction rate drops after crossing monthly transaction thresholds. The first tier covers up to 2 trillion transactions per month, and subsequent tiers reduce per-transaction costs by 67% for inside traffic and 71% for external traffic. Volume-tier pricing means your effective rate decreases as aggregate monthly volume increases. Only transactions counted against a single billing entity contribute toward tier thresholds. 

 [AWS Organizations consolidated billing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) aggregates usage across all member accounts into a single billing entity. Without it, organizations running RTB workloads across multiple AWS accounts (common when separate teams or business units own different demand-side or supply-side operations) split their transaction volume across independent billing boundaries. Each account pays the higher first-tier rate even though their combined volume would qualify for lower tiers. 

 You can also migrate RTB traffic that routes through other connectivity methods (NAT Gateways, PrivateLink, and AWS Direct Connect) onto RTB Fabric. Each migrated partner's transaction volume adds to the aggregate count toward tier breakpoints. The migrated traffic itself costs less on RTB Fabric's per-transaction model (see ADVCOST03-BP05), and the added volume pushes all existing fabric traffic closer to the next tier discount. Weigh the migration effort and the risk of disruption during cutover against these savings. 

 Tier thresholds reset monthly. Seasonal traffic patterns in advertising (Q4 holiday spikes and mid-year lulls) can push you above a threshold in peak months and below it in slower months. If your monthly volume is close to a tier threshold, evaluate whether routing additional eligible traffic through the fabric during slower months is worth the effort to maintain tier qualification. 

 Track cost-per-billion-transactions in [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to see whether consolidation is working. A declining cost-per-billion figure over months confirms that volume growth or consolidation is moving you through tier breakpoints. A flat figure despite traffic growth might indicate that accounts remain unconsolidated or that traffic is split across billing boundaries you have not addressed. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Calculate current monthly transaction volume against tier thresholds:** Review RTB Fabric link metrics for total monthly transactions. Compare against the tier thresholds to understand distance to next tier breakpoints. 

1.  **Consolidate RTB Fabric usage under a single billing entity:** Use AWS Organizations consolidated billing so all accounts' RTB Fabric traffic counts toward shared tier thresholds. This is especially effective for organizations with multiple business units running separate RTB workloads. 

1.  **Migrate remaining non-fabric RTB traffic to increase volume:** Identify any RTB partner traffic still routed through NAT Gateways or other paths. Migrating these partners to RTB Fabric increases aggregate fabric volume toward the next pricing tier while reducing per-transaction costs. 

1.  **Set alerts when approaching tier breakpoints:** Configure Cost Explorer budget alerts when monthly transaction volume is within 10-20% of the next tier breakpoint. This enables proactive decisions about routing additional partner traffic through RTB Fabric to trigger tier discounts. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP05 Replace per-gigabyte egress with transaction-priced partner connectivity](advcost03-bp05.md) 
+  [ADVCOST03-BP06 Maximize partner traffic routed inside a managed connectivity fabric](advcost03-bp06.md) 

 **Related documents:** 
+  [AWS RTB Fabric Pricing](https://aws.amazon.com/rtb-fabric/pricing/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
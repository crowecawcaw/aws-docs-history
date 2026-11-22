

# Select the best pricing model

 The right pricing model lets a workload meet its technical requirements at the lowest rate its usage pattern allows. Cloud providers charge different rates for the same capacity depending on how the workload commits to it, where it runs, and what terms govern any third-party products it depends on. Because these requirements change over time, revisit the pricing choice as workloads evolve. This capability covers matching pricing models to how each workload component behaves, weighing geographic price differences against latency and compliance needs, and choosing third-party agreements whose cost tracks the value they return. 

 Steady, long-running components benefit from commitment-based discounts, while short-lived or elastic components are cheaper on usage-based or interruptible models. Match components to models by measuring how they run, and revisit the choice as demand shifts. 


|  COST07: How do you use pricing models to reduce cost?  | 
| --- | 
|  [COST07-BP01 Perform pricing model analysis](cost07-bp01.md)  | 
|  [COST07-BP02 Choose Regions based on cost](cost07-bp02.md)  | 
|  [COST07-BP03 Select third-party agreements with cost-efficient terms](cost07-bp03.md)  | 

## Capability intent
<a name="cost07-intent"></a>
+  Each workload component runs on the pricing model that fits its usage pattern, whether steady, variable, or interruptible, rather than a single model applied across the whole workload. 
+  Predictable, long-running usage is covered by commitment-based discounts sized to the floor of actual utilization, and interruptible work runs on discounted spare capacity. 
+  Commitments and pricing choices are reviewed on a regular cadence and adjusted as usage patterns and business requirements change. 
+  Workloads run in the lowest-cost geographic location that still meets their latency, data residency, data sovereignty, and regulatory requirements, with data transfer cost weighed alongside resource price. 
+  Third-party product and license costs scale in proportion to the value delivered, and overlapping tools are consolidated so the same capability is not paid for twice. 

## Common issues to watch for
<a name="cost07-issues"></a>
+  Steady, predictable workloads run entirely at on-demand rates, so the organization pays the highest available price for usage that would qualify for a substantial commitment discount. 
+  Commitments are sized to peak usage rather than the steady floor, so unused commitment is paid for whenever demand dips below the committed level. 
+  Commitments are bought once and never revisited, so the pricing mix drifts out of alignment as workloads grow, shrink, or change shape. 
+  Fault-tolerant and interruptible work runs on full-price capacity because no one has identified it as a candidate for discounted spare capacity. 
+  Region choice defaults to a single location without comparing cost, or a cheaper region is chosen while the data transfer it creates quietly erases the saving. 
+  Third-party agreements price against total spend or resource size rather than the value delivered, so their cost outpaces their benefit as the workload adopts services the product does not touch. 
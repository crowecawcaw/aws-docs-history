

# SUS02-BP04 Define the baseload for predictable and steady-state workloads

 Most workloads combine two kinds of demand: a steady-state baseload that runs continuously, and variable demand that rises and falls on top of that baseload. Handle variable demand with elasticity, as described in [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md). You pay for an oversized baseline every hour of every day, so the same percentage of waste costs far more resource over a year in the baseload than in a component that runs briefly. 

 Identifying the baseload shows where right-sizing effort earns the most, and how much of your demand is stable enough to commit to. Once you understand and right-size the baseline, cover it with a commitment that lowers the rate you pay without constraining how the workload evolves. Compute Savings Plans apply regardless of instance family, instance size, operating system, tenancy, or AWS Region, and extend to AWS Fargate and AWS Lambda usage. Committing to a level of compute leaves you free to later move to a more efficient instance generation, AWS Graviton, or serverless. 

 Keep the two decisions separate. A commitment lowers the price you pay for usage. A Capacity Reservation holds capacity in a specific Availability Zone so it is available when you need it, but carries no billing discount of its own. A Savings Plan discount still applies both to instances running in a reservation and to reserved capacity left unused. Most steady-state workloads need only the commitment. Create a Capacity Reservation only when the workload needs that certainty. 

 **Desired outcome:** 
+  You know which portion of your demand is steady-state baseload and which is variable, and you treat each accordingly. 
+  You match capacity to actual need for predictable and steady-state workloads, achieving high resource utilization. 
+  You reduce the waste that comes from over-provisioning while still providing sufficient capacity. 
+  Your commitments cover a right-sized baseline and remain flexible enough that future efficiency improvements do not forfeit them. 

 **Common anti-patterns:** 
+  Treating total demand as a single figure, so the continuously running baseload is never separated from peak demand and neither is optimized well. 
+  Running underutilized compute instances to verify sufficient capacity for predictable workloads. 
+  Manually managing capacity without leveraging capacity management tools. 
+  Using the same provisioning strategy for all workloads regardless of their utilization patterns and business criticality. 
+  Not analyzing historical usage patterns to inform capacity planning. 
+  Choosing a commitment that pins the workload to a specific instance family, size, or Availability Zone, so a later move to a more efficient instance generation or to serverless would forfeit the commitment. 
+  Creating a Capacity Reservation alongside a price commitment when the workload only needs the lower price. 
+  Launching instances early and leaving them running purely to hold capacity ahead of a known future need, rather than reserving that capacity for the date it is required. 
+  Committing to a one or three year term before right-sizing the workload, which locks in over-provisioned capacity for the length of the term. 
+  Treating a price commitment as an efficiency improvement. Reducing the rate you pay for capacity you were already over-provisioning leaves resource consumption unchanged. 

 **Benefits of establishing this best practice:** 
+  Reduces over-provisioning of resources for predictable workloads. 
+  Lowers environmental impact through more efficient resource allocation. 
+  Provides predictable capacity for business-critical applications. 
+  Improves overall infrastructure efficiency and utilization. 
+  Often results in cost savings through reserved capacity pricing models. 
+  Where the reservation is sized to right-sized demand, lowers the share of hardware related impacts from raw material extraction to end of life treatment (Scope 3 emissions), because fewer resources are provisioned to deliver the same outcome. 
+  Where the reservation is sized to right-sized demand, lowers the share of required energy for operating infrastructure (Scope 2 emissions), for the same reason. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Start by establishing how much of your demand is steady. Separate the baseload from variable demand, right-size that baseline, and only then decide what to commit to and whether the workload also needs a Capacity Reservation. 

 A price commitment on an over-provisioned baseline lowers the bill without changing resource consumption. The environmental benefit comes from the right-sizing you do before committing. Commit to a right-sized baseline, keep the commitment flexible, and handle everything above the baseline with elasticity. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Separate steady-state baseload from variable demand. 

   1.  Use AWS Cost Explorer or Amazon CloudWatch metrics over a period long enough to include your normal cycles, so weekly and seasonal variation is visible rather than averaged away. 

   1.  Identify the floor of demand that persists across those cycles. That floor is your baseload. 

   1.  Treat the demand above that floor as variable, and handle it with elasticity as described in [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md). 

   1.  Determine business criticality for the baseload, including whether it depends on capacity being held for it. 

1.  Right-size the baseline before committing to it. 

   1.  Act on [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) recommendations so the baseline reflects what the workload needs rather than what it currently uses. 

   1.  Establish the reduced baseline before purchasing, so a term commitment does not lock in capacity you were about to remove. 

1.  Cover the right-sized baseline with a flexible commitment. 

   1.  Use [Compute Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html) for steady-state compute, which apply regardless of instance family, size, operating system, tenancy, or Region, and extend to Fargate and Lambda. 

   1.  Size the commitment to the right-sized baseload rather than to peak demand, so elasticity rather than commitment absorbs the peaks. 

   1.  Prefer commitment terms and scopes that leave you free to adopt more efficient instance generations, AWS Graviton, or serverless during the term. 

   1.  Use AWS Cost Explorer recommendations to establish the commitment level, then adjust for planned efficiency work that will reduce the baseline. 

   1.  A Savings Plan also covers Capacity Reservation usage, including future-dated reservations. AWS applies the discount automatically to reservations with matching attributes, preferring instance usage before covering unused reserved capacity, so a reservation does not need a separate discount mechanism. 

1.  Create a Capacity Reservation only where the workload requires one. 

   1.  Use an immediate-use [Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) where existing workloads need capacity held for them. These carry no term commitment and can be modified or canceled at any time. 

   1.  Use a [future-dated Capacity Reservation](https://aws.amazon.com/blogs/aws/announcing-future-dated-amazon-ec2-on-demand-capacity-reservations/) where you know the date incremental capacity will be needed, such as a product launch, a migration, or a seasonal peak. Requests can be made between 5 and 120 days ahead, and AWS recommends at least 8 weeks to improve supportability. This is the alternative to the older pattern of provisioning capacity early and paying for it while it sits idle. 

   1.  Size a future-dated reservation to what you will actually use. It is billed at the equivalent On-Demand rate from the start date whether or not instances run in it, including through the minimum commitment duration, so over-reserving holds and pays for capacity that does no work. Cancellation is [now supported](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-fcr-cancellation/), with a charge that may apply depending on timing, and these reservations are intended for incremental instances rather than covering existing running ones. 

   1.  Use [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) to reserve accelerated compute for long running machine learning workloads such as training and fine-tuning. 

   1.  Cancel Capacity Reservations when the need passes. Reserved capacity that goes unused still counts against your On-Demand limits and still incurs charges, so it is provisioned but idle. 

1.  Monitor coverage and utilization, and optimize as needed. 

   1.  Regularly review commitment coverage and utilization using AWS Cost Explorer. 

   1.  Use AWS Compute Optimizer for ongoing right-sizing recommendations. 

   1.  [Monitor Capacity Reservation underutilization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-eventbridge.html) so reserved but unused capacity is surfaced and released rather than left held. 

   1.  Track idle reserved capacity directly: unused reservation appears in AWS Cost and Usage Report 2.0 as an UnusedBox line item, which is a measurable signal of capacity that is provisioned but doing no work. 

   1.  Re-check the baseload and right-sizing ahead of each renewal, so a term rollover does not carry forward capacity the workload has outgrown. 

1.  Establish a governance process for baseload and commitment management. 

   1.  Define roles and responsibilities for baseload analysis, right-sizing, and commitment decisions. 

   1.  Document which workloads need a Capacity Reservation and which only need a lower rate, and why. 

   1.  Schedule regular reviews of utilization and commitment coverage. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md) 
+  [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md) 
+  [COST07-BP01 Perform pricing model analysis](cost07-bp01.md) 

 **Related documents:** 
+  [What are Savings Plans?](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) 
+  [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html) 
+  [Understanding how Savings Plans apply to your usage](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) 
+  [Reserve compute capacity with EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) 
+  [Capacity Reservation pricing and billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html) 
+  [Announcing future-dated Amazon EC2 On-Demand Capacity Reservations](https://aws.amazon.com/blogs/aws/announcing-future-dated-amazon-ec2-on-demand-capacity-reservations/) 
+  [Amazon EC2 Future-dated Capacity Reservations Now Supports Cancellation](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-fcr-cancellation/) 
+  [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) 
+  [AWS re:Invent 2023 - Capacity, availability, cost efficiency: Pick three (CMP207-R) slides](https://d1.awsstatic.com/events/Summits/reinvent2023/CMP207-R_Capacity-availability-cost-efficiency-Pick-three-REPEAT.pdf) 

 **Related videos:** 
+  [Maximizing EC2 Efficiency: Smart Savings Strategies for Cost-Effective Cloud Computing](https://aws.amazon.com/video/watch/d56e2fbb847/) 
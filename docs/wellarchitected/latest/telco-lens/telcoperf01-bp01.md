

# TELCOPERF01-BP01 Deploy latency-sensitive RAN and user-plane workloads on Outposts colocated with radio infrastructure
<a name="telcoperf01-bp01"></a>

 Radio Access Network (RAN) Distributed Unit (DU) and user-plane functions have latency budgets to the radio that no remote cloud location can meet over a transport network. These workloads must run on compute physically colocated with or adjacent to the radio infrastructure. This best practice places them on AWS Outposts at cell sites and aggregation points where the budgets are achievable. 

 **Desired outcome:** 
+  RAN DU workloads run on AWS Outposts in or adjacent to the cell sites, central offices, or aggregation points where fronthaul or midhaul terminates. 
+  User-plane functions are placed to minimize the data-plane path between the gNB and the internet or enterprise breakout point. 
+  Placement decisions are driven by measured latency budgets from 3GPP specifications, not by generic proximity heuristics. 

 **Common anti-patterns:** 
+  Deploying RAN workloads to edge locations that are not physically colocated with the radio, adding unacceptable transport latency. 
+  Treating all edge workloads identically without distinguishing RAN's sub-millisecond fronthaul budget from application edge's tens-of-milliseconds tolerance. 
+  Not measuring actual round-trip latency between compute and radio units before committing to a location. 
+  Assuming a workload that met its budget in a lab will meet it under production load without margin. 

 **Benefits of establishing this best practice:** 
+  Fronthaul latency budgets are met through physical colocation, keeping the deployment 3GPP-compliant. 
+  Outposts in operator facilities provide dedicated compute with consistent latency, unlike shared edge locations. 
+  The deployment model matches how operators already manage their physical infrastructure footprint. 
+  User-plane path length is minimized, improving subscriber data-plane performance. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The latency requirements for RAN workloads come from the functional split between the Central Unit (CU), Distributed Unit (DU), and Radio Unit (RU), and they are absolute rather than negotiable. For the common 7.2x split, the fronthaul interface between DU and RU carries a one-way latency budget on the order of 100 to 250 microseconds. No location reached over a transport network can meet that budget, because the speed of light over the intervening distance already exceeds it. This is why the problem is one of physical colocation, not of choosing the closest cloud location. 

 AWS Outposts resolve this by placing AWS compute inside operator cell sites, central offices, or aggregation hubs, so the DU workload runs on local compute within the latency envelope while still reaching the parent AWS Region for control-plane operations and management. The distinction that guides placement is the budget of each interface: user-plane functions have more relaxed budgets (a few milliseconds to the gNB) and can sometimes run in a Region if the measured N3 latency fits, in which case the Region is preferable for its elasticity and operational simplicity. Derive placement from documented per-interface budgets rather than a blanket edge decision, because different functions land in different places. 

 A frequent and costly confusion is to reach for edge services designed for a different purpose. AWS Wavelength Zones, for instance, exist to give mobile application developers low latency to end-user devices over the carrier network; they are not built to host the network infrastructure itself and don't meet fronthaul budgets. Choose infrastructure by what it actually guarantees, and validate the choice by measuring real round-trip latency under load before production. 

### Implementation steps
<a name="implementation-steps"></a>
+  Map latency budgets to placement requirements: document the one-way latency budget for each interface (fronthaul, midhaul, backhaul, N3, N6) from your functional split and 3GPP specifications, and convert them to maximum physical distances for your transport technology. 
+  Identify facilities that meet the budgets by surveying cell sites, central offices, and aggregation points where AWS Outposts can be deployed within the required latency envelope of the radio. 
+  Deploy Outposts sized for DU workloads, selecting configurations matching DU compute needs (cores, memory, accelerators) and accounting for real-time processing requirements. 
+  Place user-plane functions by measured N3 latency, deploying UPFs on Outposts, AWS Local Zones, or the Region based on measured latency to the gNB, preferring the Region where its budget is met. 
+  Validate latency end to end before production by measuring actual round-trip latency between compute and radio units under load, confirming results fall within 3GPP budgets with margin for traffic variation. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 


# Cost measurement and financial management

 Maintaining a cost-efficient infrastructure is essential for the profitability of advertising workloads. With fluctuations in usage over time, the costs associated with real-time bidding workloads can vary significantly. Continually monitoring costs is the best way to keep them under control. Evaluate resiliency needs against the cost of downtime for ad delivery and bidding to make proportional investments in reliability. Fragmented measurement across linear TV and digital forces publishers to maintain separate measurement stacks, pay multiple vendors for overlapping capabilities, and run redundant identity resolution processes. Unifying measurement reduces infrastructure duplication while enabling complete reach, frequency, and attribution analysis. 


|  ADVCOST01: How do you implement cloud financial management practices for your advertising workloads?  | 
| --- | 
| [ADVCOST01-BP01 Continually measure costs of advertising workloads, and adjust resource and model allocation accordingly](advcost01-bp01.md) | 
| [ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding](advcost01-bp02.md) | 
| [ADVCOST01-BP03 Consolidate identity resolution to reduce redundant matching across linear and digital audiences](advcost01-bp03.md) | 

## Capability intent
<a name="advcost01-capability-intent"></a>
+  You have full visibility into RTB infrastructure costs at the campaign level, with automated dashboards and alerts that enable data-driven decisions about resource allocation. 
+  KPIs for each campaign evaluate cost-to-revenue ratios, including both billing metrics (resource costs) and campaign metrics (click-through rate, cost per acquisition). 
+  Cost allocation tags attribute infrastructure costs to specific campaigns, enabling accurate ROI calculations. 
+  You have a clear, quantified understanding of the financial impact of downtime for each campaign and can compare it directly against the cost of implementing resiliency measures. 
+  A single identity resolution process (AWS Entity Resolution) creates a unified audience graph spanning household-level linear identifiers and individual-level digital identifiers, reducing redundant matching costs. 
+  Separate identity resolution vendors for linear and digital are consolidated, reducing duplicate licensing and matching costs. 
+  Cross-screen frequency management enables more precise targeting, reducing over-delivery and wasted ad spend. 

## Common issues to watch for
<a name="advcost01-common-issues-to-watch-for"></a>
+  Running RTB infrastructure without cost allocation tags, making it impossible to attribute costs to specific campaigns or business units. 
+  Reviewing costs only at the end of a billing cycle rather than continuously, leading to budget overruns before corrective action can be taken. 
+  Tracking only technical metrics (CPU utilization, request latency) without correlating them to business outcomes such as cost-per-click or cost-per-acquisition. 
+  Applying the same level of resiliency to all campaigns regardless of their revenue potential or criticality. 
+  Paying separate identity resolution vendors for linear panel-based household matching and digital device graph that largely overlap in coverage, duplicating matching costs. 
+  Running real-time cross-channel identity synchronization when batch synchronization would satisfy frequency management needs at far lower cost. 
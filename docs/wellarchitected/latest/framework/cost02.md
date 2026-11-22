

# Monitor cost and usage

 Cost optimization begins with visibility. This capability covers the practices that turn a monthly total into cost data teams can act on, attributing spend to the teams, products, and environments that own it. It also covers expressing cost against the business outcomes it produces, and monitoring spend to catch changes as they happen. 

 Cost visibility is a shared responsibility. Engineering decisions to provision and operate resources create spend, so cost data must reach those engineers in a form they can use. This capability describes how an organization builds that visibility and keeps it accurate as the environment grows. 


|  COST02: How do you monitor your cost and usage?  | 
| --- | 
|  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md)  | 
|  [COST02-BP02 Allocate costs based on workload metrics and business outcomes](cost02-bp02.md)  | 
|  [COST02-BP03 Monitor cost proactively](cost02-bp03.md)  | 

## Capability intent
<a name="cost02-intent"></a>
+  Cost and usage trace back to the team, product, and environment that own them through a single, consistently applied tagging standard rather than collapsing into organization-wide totals. 
+  Shared and non-taggable spend is attributed through defined allocation rules, so no meaningful share of cost is left untraceable. 
+  Spend is expressed as cost per business outcome, so efficiency is visible even when total cost rises with growth. 
+  Cost and usage are reviewed on a defined cadence, and the data is visible to the teams that create the spend, not only to finance. 
+  Unexpected spend is detected close to when it occurs through threshold-based alerts for known limits and statistical detection for the deviations no one predicted. 
+  Tag coverage and allocation accuracy are measured, and drift is detected and corrected on a regular schedule. 

## Common issues to watch for
<a name="cost02-issues"></a>
+  Tags are applied inconsistently or only after resources exist, so the same concept carries different keys across accounts and cost data cannot be grouped the way the business is organized. 
+  Cost allocation labels are activated late, and because activation is not retroactive, spend recorded beforehand stays permanently unattributed. 
+  Shared infrastructure and non-taggable line items are left out of the allocation model, so a growing pool of cost has no owner and efficiency figures overstate how well the workload performs. 
+  Success is measured as total spend, so healthy growth and genuine waste look identical, and no unit-cost metric exists to separate them. 
+  Cost is reviewed only when the monthly statement arrives, which lets an inefficiency run for weeks before anyone notices, and monitoring relies on threshold alerts alone that miss the problems no one thought to set a limit for. 
+  Cost data sits with finance and never reaches the engineers whose decisions drive it, and alerts tuned too low or routed too widely become noise that teams learn to ignore. 
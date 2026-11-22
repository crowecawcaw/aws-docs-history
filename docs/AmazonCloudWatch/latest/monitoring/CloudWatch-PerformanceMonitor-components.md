

# Components and features of Performance Monitor

Performance Monitor uses or references the following concepts.

Scope  
In Performance Monitor, the scope defines the set of account-Region pairs for which you have network path visibility. The scope is shared with Network Flow Monitor, so changes that you make to the scope, such as adding or removing accounts, apply to both. Performance Monitor creates the scope automatically when you create your first monitor. When you add VPCs from additional accounts or specify destination account-Region pairs, the scope expands cumulatively. You can also add accounts and account-Region pairs to your scope manually on the **Account Configuration** page.  
The scope determines the following:  
+ Which destination paths can be shown at full Availability Zone to Availability Zone granularity.
+ Which accounts' subnet-level details are available for drill-down.
Without a destination account-Region pair in scope, inter-Region paths are shown at Region-to-Region level only, without subnet-level drill-down on the destination side.  
A scope can include up to 1,000 account-Region pairs.

Monitor  
You create a monitor to track the network health of specific VPCs over time. When you create a monitor, you select one or more VPCs from your accounts in the current Region. Performance Monitor then provides ongoing visibility into the network paths used by traffic from those VPCs.  
Each monitor includes the following:  
+ A set of selected VPCs, from one Region. A monitor can include up to 25 VPCs.
+ An impact score for each network path, which you can use for CloudWatch alarms.
+ A list of top network paths, ranked by impact.
+ Drill-down capability to subnet-level flows.

Network path  
A network path in Performance Monitor represents the route that traffic takes between a local location and a remote location. Paths are identified at the Availability Zone level. For example, a path from `us-east-1a` to `us-west-2b` represents traffic flowing between those two Availability Zones.  
Performance Monitor classifies paths into the following types, based on the relationship between local and remote locations:  
+ **Inter-Region** – Local Availability Zone in one Region to a remote Availability Zone or service in a different Region.
+ **Intra-Region** – Local Availability Zone to a different Availability Zone in the same Region.
+ **Intra-AZ** – Both local and remote locations within the same Availability Zone.
+ **AZ-Service-AZ** – Local Availability Zone to an AWS service endpoint, such as Amazon S3, Amazon DynamoDB, Amazon EC2, a NAT gateway, or a transit gateway.

Subnet flow  
Subnet flows are the individual traffic streams within a network path. Each subnet flow represents traffic from a specific source subnet to a specific destination, either another subnet or an AWS service. When you expand a path in the console, you can see the subnet flows contributing traffic to that path. Subnet flows include the following:  
+ Source and destination identifiers (subnet ID or service name)
+ Bytes in and bytes out
+ Associated VPC IDs
+ Associated account IDs
+ Instance IDs, when available
+ Impact score and impact level

Impact score  
The impact score measures how much a network path is experiencing unusual degradation. Performance Monitor reports an impact score for each network path.  
The impact score is calculated using the following comparisons:  
+ **Global comparison** – Is this path an outlier compared to all other measured paths at the current time?
+ **Local comparison** – Is this path behaving abnormally compared to its own recent history?
These two signals are combined into a single normalized score. The only threshold parameter is a noise floor, below which impact isn't considered significant. The impact level boundaries are based on standard statistical significance levels rather than arbitrary values.

Impact level  
Performance Monitor derives the impact level from the impact score. The `ImpactScore` metric that Performance Monitor publishes to CloudWatch has a fixed value for each impact level:  
+ **High** (95) – The combined anomaly is statistically extreme, beyond the p < 0.05 significance level.
+ **Medium** (65) – Between 1 sigma and 2 sigma of the characteristic scale.
+ **Low** (25) – Within 1 sigma. Normal variation.
+ **None** (0) – Below the noise floor. No significant impact.

Performance metrics  
Performance Monitor gathers and calculates the following information for each network path:  
+ **Impact score** (0, 25, 65, or 95) – Degradation measurement, which you can use to define CloudWatch alarm thresholds.
+ **Impact level** – High, Medium, Low, or None.
+ **p95 latency** – The 95th percentile latency for the path.
+ **Latency baseline** – Historical baseline latency, available in the detail graph, based on CloudWatch metrics over the last 14 days.
+ **Bytes in and bytes out** – Traffic volume in each direction.
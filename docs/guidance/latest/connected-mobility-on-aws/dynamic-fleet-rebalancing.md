

# Dynamic fleet rebalancing
<a name="dynamic-fleet-rebalancing"></a>

Dynamic fleet rebalancing keeps vehicles where demand is. It measures how each vehicle and location is used, forecasts demand per location, detects supply-demand imbalances, and recommends vehicle moves with their transfer cost and revenue impact.

## What it can do
<a name="dfr-what-it-can-do"></a>
+  **Utilization map** — vehicle locations, supply-demand heatmaps, and demand forecast overlays on an Amazon Location Service map.
+  **Utilization metrics** — active hours against available hours per vehicle, per location, and per region, in real time.
+  **Demand forecasts** — 7-day and 30-day demand predictions per location.
+  **Supply-demand gaps** — locations with too many or too few vehicles, with estimated transfer cost to close each gap.
+  **Action Queue** — costed rebalancing recommendations with transfer cost, revenue impact, and a confidence score, for the operator to approve, reject, or modify. See [Fleet Intelligence Action Queue](fi-action-queue.md).
+  **Auto-approval rules** — per-fleet rules, off by default, that approve moves within an operator-set transfer-cost limit.
+  **Rebalance history** — every executed move with its predicted and actual effect on utilization.

## How it works
<a name="dfr-how-it-works"></a>

1.  **Fleet data ingestion.** Vehicle telemetry (location, ignition status, speed, and trip data) streams continuously from the existing CMS normalization pipeline through Amazon MSK. Fleet enrollment and constraint data (which vehicles are where, depot capacity, maintenance windows, and charging infrastructure) is held in Amazon DynamoDB. Demand signals from booking systems and historical patterns (events, weather, seasonal patterns, reservations, and historical utilization) are uploaded to Amazon S3.

1.  **Utilization processing.** The Utilization Processor, on Amazon Managed Service for Apache Flink, reads normalized telemetry and fleet enrollment data and computes utilization per vehicle, location, and region in real time. It detects supply-demand imbalances and writes to Iceberg tables in Amazon S3, Amazon ElastiCache for Redis, and DynamoDB. An Amazon SageMaker time series model produces 7-day and 30-day demand forecasts per location.

1.  **Utilization history.** Utilization history lands in ADP as curated Iceberg products, partitioned by fleet, region, and day, with row-level isolation per fleet. Amazon Athena runs ad hoc queries and pre-built views: utilization by location, supply-demand gaps, transfer cost estimates, and rebalance history with actual impact. Redis serves real-time state to the map. An imbalance event starts the rebalancing agent.

1.  **Rebalancing agent.** The rebalancing agent (`agent-fi-rebalancing`) is an AVX Tier 2 agent: a Claude model on Amazon Bedrock that runs on imbalance events and a daily review. The SageMaker model forecasts demand; the agent decides which moves are worth making. It weighs each gap’s forecast revenue against transfer cost, depot capacity, maintenance windows, charging availability and the vehicles that are free to move, and grounds itself in the ADP knowledge base. Each move goes to the Action Queue as a fleet-scoped recommendation: the vehicles in its evidence, the source and destination locations in its parameters, with transfer cost, revenue impact and confidence. The daily review compares each executed move’s predicted and actual effect and feeds the result back to the next run.

1.  **Portal.** Fleet operators use the portal through Amazon CloudFront. Amazon API Gateway routes requests to AWS Lambda handlers that read Redis and Athena, and Amazon Cognito restricts each operator to their fleets. Amazon Location Service renders the map.

1.  **Human in the loop and execution.** Recommendations appear in the Action Queue. When the operator approves a move, or a fleet rule auto-approves it, CMS updates the vehicles' locations in the fleet record, notifies dispatch, and logs the move. Amazon EventBridge schedules daily fleet reviews that compare predicted against actual utilization after each move, which improves future forecasts.

## Architecture details
<a name="dfr-architecture"></a>

![Dynamic fleet rebalancing architecture: telemetry on Amazon MSK](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/dynamic-fleet-rebalancing-architecture.png)



| Component | Role | 
| --- | --- | 
| Amazon MSK | Carries normalized telemetry on `cms-telemetry-preprocessed`. | 
| Amazon DynamoDB | Fleet enrollment and constraints, rebalance events and imbalance flags. | 
| Amazon S3 and ADP curated products | Demand signals, and ADP Iceberg tables of utilization and forecasts partitioned by fleet, region, and day. | 
| Amazon Managed Service for Apache Flink | The Utilization Processor computes utilization and detects imbalances. | 
| Amazon SageMaker | Demand forecasting model (7-day and 30-day time series per location) and anomaly scoring. | 
| Amazon Athena | Utilization, gap, transfer-cost, and rebalance-history views. | 
| Amazon ElastiCache for Redis | Real-time utilization state per vehicle and location. | 
| AVX rebalancing agent (`agent-fi-rebalancing`), Amazon Bedrock, and the ADP knowledge base | Tier 2 agent that weighs forecast demand against transfer cost and constraints and proposes costed moves. Amazon Bedrock Guardrails filter its output. | 
| AVX Findings and Actions | The Action Queue: recommendations, decisions, auto-approval rules and guardrails. See [Fleet Intelligence Action Queue](fi-action-queue.md). | 
| Amazon CloudFront, Amazon Cognito, Amazon API Gateway, AWS Lambda, and Amazon Location Service | Serve the portal’s map and Action Queue to fleet-scoped operators. | 
| CMS move execution and Amazon EventBridge | Apply approved moves to the fleet record, and schedule the daily review that measures actual utilization after each move. | 
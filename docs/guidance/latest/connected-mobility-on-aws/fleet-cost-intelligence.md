

# Fleet cost intelligence
<a name="fleet-cost-intelligence"></a>

Fleet cost intelligence brings every cost a vehicle incurs into one model and joins it with how the vehicle is driven. Operators see total cost of ownership (TCO) for the fleet and for each vehicle, find the vehicles that cost more than they should, and act on recommendations from a cost agent.

## What it can do
<a name="fci-what-it-can-do"></a>
+  **TCO dashboard** — cost KPIs, cost breakdowns by category (fuel and energy, maintenance and repair, lease, insurance), trends over time, and outliers, for the fleet and for each vehicle.
+  **Cost per mile** — computed per vehicle from cost records and telemetry-derived distance, fuel consumption, EV energy use, and idle time, and compared against rolling baselines for the vehicle and the fleet.
+  **Preventive-maintenance compliance** — which vehicles are due, overdue, or current on scheduled service.
+  **Lifecycle and sell timing** — the month in which a vehicle’s rising maintenance cost crosses its falling depreciation, so operators can retire or remarket it before it becomes a cost drain.
+  **Maintenance forecasts** — expected maintenance spend per vehicle and per fleet.
+  **Action Queue** — the cost agent’s recommendations, each with its evidence, estimated saving and confidence, for the operator to approve, reject, or override. See [Fleet Intelligence Action Queue](fi-action-queue.md).
+  **Auto-approval rules** — per-fleet rules, off by default, that approve one action kind within a limit.
+  **Agent Activity Feed** — what the agent detected and recommended, and when it last ran.

## How it works
<a name="fci-how-it-works"></a>

1.  **Cost ingestion.** Cost data arrives from four sources: vehicle telemetry from the existing CMS normalization pipeline, fuel and energy transactions from fuel cards and EV charging networks, maintenance and repair records from fleet management systems, and asset and financial data, including leases, insurance, and market pricing. Data enters through Kafka topics in real time or through CSV batch upload to Amazon S3. A built-in simulator generates realistic cost events so the feature can be demonstrated without connecting live sources.

1.  **Cost processing and normalization.** Source-specific Flink normalizers convert each cost feed into a canonical format on a shared Kafka topic. The Cost Processor Flink job joins the normalized cost data with telemetry-derived metrics (fuel consumption, EV energy use, idle time, and cost per mile) and computes rolling baselines per vehicle and per fleet. It writes historical records to Apache Iceberg tables in Amazon S3, the latest cost state to Amazon ElastiCache for Redis, and recent transactions and anomaly flags to Amazon DynamoDB.

1.  **Cost history.** Cost history lands in the Automotive Data Platform (ADP) accelerator as curated Iceberg products, partitioned by fleet and month, with AWS Lake Formation row-level isolation per fleet. Amazon Athena views encode the business logic: fleet TCO summaries, cost outliers, lifecycle candidates, and maintenance forecasts. Redis serves the latest cost state to the dashboard.

1.  **Cost agent.** The cost agent (`agent-fi-cost`) is an AVX Tier 2 agent: a Claude model on Amazon Bedrock that runs on a schedule and on anomaly events. The SageMaker model scores how unusual a cost is; the agent works out why and what to do. It queries cost history in Athena, the latest cost state in Redis and recent transactions in DynamoDB, and grounds itself in the ADP knowledge base (business glossary, query patterns, cost playbooks). It separates causes such as idle time, route, charging rate or overdue maintenance, chooses an action, and estimates the saving. Each recommendation goes to the Action Queue with its evidence, estimated saving and confidence. Amazon Bedrock Guardrails filter the model’s output; the approval rules and guardrails in [Fleet Intelligence Action Queue](fi-action-queue.md) decide what may run.

1.  **Operator review.** The portal’s TCO dashboard reads cost KPIs, breakdowns, trends, and outliers through Amazon API Gateway and AWS Lambda. Recommendations appear in the Action Queue, where the operator approves, rejects, or overrides them; see [Fleet Intelligence Action Queue](fi-action-queue.md).

## Architecture details
<a name="fci-architecture"></a>

![Fleet cost intelligence architecture: vehicle telemetry](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/images/fleet-cost-intelligence-architecture.png)



| Component | Role | 
| --- | --- | 
| Kafka topics on Amazon MSK |  `cms-telemetry-preprocessed` (vehicle telemetry), `cms-cost-fuel` (fuel and charging), `cms-cost-maintenance` (maintenance work), and `cms-cost-assets` (assets and financial) carry the raw cost feeds. `cms-cost-normalized` carries the canonical cost records. | 
| Amazon Managed Service for Apache Flink | A fuel and charging cost processor, a maintenance cost processor, and an asset cost processor normalize each feed. The Cost Processor joins normalized cost with telemetry metrics and computes rolling baselines. | 
| ADP curated products (Amazon S3 Iceberg tables, AWS Lake Formation) | Historical cost records, partitioned by fleet and month, with row-level isolation per fleet. | 
| Amazon Athena | Ad hoc queries and the TCO, outlier, lifecycle, and forecast views. Cost per mile, preventive-maintenance compliance, and sell timing also read the ADP accelerator’s curated `service_records`, `charging_sessions`, and `energy_usage` products. See [Fleet Intelligence services](fip-architecture-details.md#fleet-intelligence). | 
| Amazon ElastiCache for Redis | Latest cost state per vehicle for dashboard rendering. | 
| Amazon DynamoDB | Recent cost transactions and anomaly flags. | 
| AVX cost agent (`agent-fi-cost`), Amazon Bedrock, and the ADP knowledge base | Tier 2 agent that diagnoses cost anomalies, chooses actions and estimates savings, using Athena, Redis and DynamoDB tools. Amazon Bedrock Guardrails filter its output. | 
| AVX Findings and Actions | The Action Queue: recommendations, decisions, auto-approval rules and guardrails. See [Fleet Intelligence Action Queue](fi-action-queue.md). | 
| Amazon SageMaker | Anomaly scoring model for cost events. | 
| Amazon API Gateway and AWS Lambda | Serve the TCO dashboard, the Action Queue (`/api/v1/fleet-intelligence/actions`), and the Agent Activity Feed to the portal. | 
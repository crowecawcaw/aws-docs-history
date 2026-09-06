

# The customer journey: one data foundation, many functions
<a name="ae-customer-journey"></a>

An automotive OEM’s different functions each need their own AI-assisted or agent-backed workflow — but they don’t each need their own data platform. The nine governed data products ADP deploys are the shared foundation that makes all of these patterns possible simultaneously.

The following table illustrates how different functions within the same organization can each build a different consumption pattern on top of the same underlying data.


| Function | Business need | Consumption pattern | ADP data products involved | 
| --- | --- | --- | --- | 
| Customer service | Answer customer questions about recalls, DTC codes, warranty coverage, and service history in real time | Conversational AI agent with grounded retrieval — retrieves relevant context from the knowledge base before answering; flags answers that come from model memory rather than retrieved documents |  `vehicle_knowledge_base` (DTCs, recalls, TSBs, warranty terms), `service_records`, `customer_360`  | 
| Fleet operations | Monitor fleet health, detect anomalies, alert on OTA failures, track asset utilization | Operational dashboards and anomaly-detection pipelines — subscribe to telemetry aggregates and OTA campaign outcomes via DataZone; surface at-risk assets before they become incidents |  `vehicle_telemetry_aggregated`, `ota_campaigns`, `vehicle_identity`, `service_records`  | 
| Executive reporting | Answer business questions in plain English without writing SQL — "which vehicles have degraded battery SoH after winter?" or "which customers have open service records and unresolved OTA failures?" | Natural-language query interface — an executive subscribes to ADP products via Amazon DataZone and queries them through Amazon Quick Suite or Quick Desktop without analyst support |  `vehicle_telemetry_aggregated`, `customer_360`, `ota_campaigns`, `service_records`  | 
| R&D / data science | Train predictive maintenance models, study OTA adoption patterns, build new ML features | ML pipeline — subscribes to multiple products via DataZone; joins them in Amazon Athena for model training; the SageMaker Studio Isolation-Forest reference-consumer notebook is the worked example |  `vehicle_telemetry_aggregated`, `charging_sessions`, `energy_usage`, `service_records`, `customer_360`  | 

Each row in this table represents a different team, a different tool, and a different interaction model — but they all start with the same foundation deploy and the same DataZone subscription mechanism. Adding a new consumption pattern does not require rebuilding the data foundation; it requires subscribing to the data products the new pattern needs and building the consumption layer on top of them.

Example 1 (below) corresponds to the first row: a customer-service conversational agent (CVX). Examples 2 and 3 both build on the executive-reporting row — an ad hoc natural-language query interface (Amazon Quick Suite) and a proactive scheduled briefing agent on the same foundation, respectively.
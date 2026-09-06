

# Example 2: Natural-language queries for business executives
<a name="ae-worked-example-quick"></a>

The same nine ADP governed data products that ground the CVX agent can also power a self-service natural-language query experience for business users who need answers without writing SQL.

 [Amazon Quick Suite](https://docs.aws.amazon.com/quicksuite/latest/userguide/) (including [Amazon Quick Desktop](https://docs.aws.amazon.com/quick/latest/userguide/what-is-desktop.html), the desktop client) connects to Amazon DataZone as a data source, inheriting the subscription and governance model DataZone enforces. A business user who has been granted access to the relevant ADP consumer project through DataZone can ask questions in plain English — the Quick Suite layer translates them to SQL against the underlying Athena tables and returns the answer.

This pattern is a demonstration of the enabling thesis at a non-technical scale: the same foundation deploy that supports ML model training and conversational agents also supports executive-level ad hoc queries, because all three consumption patterns subscribe to the same governed data products through the same DataZone catalog.

## Example queries
<a name="example-queries"></a>

The operational questions posed in [Analytical data platform for automotive OEMs on AWS](guidance-overview.md)'s "Why ADP" section translate directly to this pattern:
+  *"Which vehicles have degraded battery SoH after winter?"* — `vehicle_telemetry_aggregated` \+ `vehicle_identity`, filtered to a seasonal date range
+  *"Which customers have open service records and unresolved OTA failures?"* — `customer_360` \+ `service_records` \+ `ota_campaigns`, cross-product join on `customer_id` and `vin` 
+  *"What is the average energy efficiency delta after the most recent OTA campaign by model year?"* — `energy_usage` \+ `ota_campaigns` \+ `vehicle_identity` 

A business executive using Amazon Quick Desktop can ask these questions through a conversational interface backed by Quick Suite’s natural-language-to-SQL layer. They do not need to know the Athena table names or partition keys; Quick Suite resolves those from the DataZone catalog metadata — the same schemas and documented descriptions that ADP publishes when it registers each data product in the domain.

## Scope and framing
<a name="scope-and-framing"></a>

This is a demo-scale illustration of the pattern, not a production BI deployment guide. Production deployments of Amazon Quick Suite require IAM Identity Center configuration, DataZone group-to-reader-group mapping, and reader-group provisioning in the Quick namespace — steps that are outside the scope of this chapter and depend on the organization’s existing IAM Identity Center setup.

The value of the pattern is not the deployment complexity; it is the observation that the same `adp-{stage}-data-consumers` IAM Identity Center group that controls Athena and notebook access to ADP products also controls which users can subscribe to those products in Amazon Quick Suite — one access-control model governs all consumption patterns.
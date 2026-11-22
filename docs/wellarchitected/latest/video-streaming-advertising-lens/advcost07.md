

# Converged ad sales system cost reduction

 Publishers maintaining parallel sales planning stacks for linear TV (upfront and scatter, with age-gender guarantees) and digital (audience-based and impression-level) incur duplicated infrastructure costs for inventory management, order management, pricing engines, and forecasting models. Converging these into a unified system reduces redundant compute, storage, and operational overhead while enabling cross-channel yield optimization that increases revenue per infrastructure dollar. 


|  ADVCOST07: How do you reduce the cost of maintaining parallel sales planning systems across linear and digital properties?  | 
| --- | 
| [ADVCOST07-BP01 Consolidate inventory data into a unified data lakehouse to reduce redundant storage and ETL pipelines](advcost07-bp01.md) | 
| [ADVCOST07-BP02 Replace dedicated forecasting infrastructure with serverless ML-based inventory prediction](advcost07-bp02.md) | 
| [ADVCOST07-BP03 Remove redundant order management systems by unifying campaign booking across buying models](advcost07-bp03.md) | 
| [ADVCOST07-BP04 Use serverless pricing engines that scale with transaction volume](advcost07-bp04.md) | 
| [ADVCOST07-BP05 Implement cross-platform yield optimization to maximize revenue per infrastructure dollar](advcost07-bp05.md) | 

## Capability intent
<a name="advcost07-capability-intent"></a>
+  All advertising inventory data (linear TV avails, digital impressions, CTV streams, and FAST channels) resides in a single data lakehouse, removing the need for separate ETL pipelines. 
+  A single ML forecasting pipeline predicts available inventory across linear, digital, and CTV properties using serverless endpoints. 
+  A unified order management system handles both guaranteed linear buys and digital programmatic buying, reducing duplicate OMS licensing and hosting. 
+  Inventory is dynamically allocated across linear, digital, and CTV to maximize total yield. 

## Common issues to watch for
<a name="advcost07-common-issues-to-watch-for"></a>
+  Running separate forecasting infrastructure for linear and digital that can't capture cross-channel audience migration patterns. 
+  Maintaining separate OMS systems with point-to-point integrations that create brittle dependencies rather than a unified data layer. 
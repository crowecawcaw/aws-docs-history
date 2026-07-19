# Why this belongs to the data platform

In the v0.1.0 release, the Automotive Data Platform shipped a Flink-based real-time normalization pipeline directly as part of the ADP deployment. The v0.2 foundation does not re-run that pipeline — `vehicle_telemetry_aggregated` publishes analytical rollups (per-VIN, per-window aggregates), not raw 1 Hz signal replay.

That is a correct and intentional scope narrowing of what the **foundation deploy** ships out of the box. It does not mean telemetry normalization stopped being a data platform use case.

The distinction is identical to the platform’s posture on BI tooling or conversational AI: the ADP foundation deploy does not ship a pre-configured dashboard or a Bedrock agent, but it describes the governed data products and subscription patterns that any BI tool or conversational front-end would consume. Telemetry normalization sits in the same category — it is a **bring-your-own-compute** pattern the foundation **enables**, not a foundation-layer feature. Customers who need a running normalization pipeline deploy one guided by the architecture described in this chapter, the same way they would deploy their own BI tool guided by the DataZone subscription pattern in [Data products](data-products.md "data-products.md").

###### Important

**This is a bring-your-own-compute pattern, not a foundation feature.** Implementing the normalization architecture described here is materially more complex than deploying the ADP platform foundation alone. It requires designing and operating a stateful stream processor (Flink or equivalent), a low-latency key-value cache (Redis/Valkey), and an ingestion transport capable of carrying multi-vendor schemas at scale (Kafka or Kinesis). The foundation layer provides the durable analytical sink and governed data product surface that the normalization pipeline writes into — it does not deploy the pipeline itself.

# The enabling thesis

Every automotive organization collects data — vehicle signals, customer interactions, service visits, OTA campaign outcomes, charging events. The problem is that this data almost always lives in separate systems owned by different teams. A customer-service representative cannot easily answer "has this customer had an OTA failure AND an unresolved service record?" because the OTA data lives in one system and the service records live in another. A data scientist trying to train a predictive maintenance model cannot get clean, joined training data because no single system owns all the relevant signals.

A _governed data product_ (a dataset with an owner, an access policy, and a documented schema, published so other teams can discover and subscribe to it) changes this equation. When vehicle telemetry, customer history, service records, OTA campaigns, and charging behavior are all published as governed data products into a shared catalog, any downstream consumer — an AI agent, a machine learning pipeline, a business-intelligence tool, or a natural-language query interface — can access the same joined, consistent picture of the vehicle and the customer, without each team re-solving the data-access problem independently.

###### Important

**The core enabling thesis**: Governed cross-silo data is what makes every downstream consumption pattern possible. Agents need context that spans vehicle state, customer history, and service records in a single grounded answer. ML models need clean, joined training datasets that no single team owns alone. Business queries need a coherent picture that crosses operational silos. ADP’s nine governed data products are the enabling layer beneath all of these — rather than each team solving data access independently, every consumption pattern draws from the same foundation.

This chapter demonstrates that thesis through three concrete examples:

- **Example 1** — a customer-facing agent (the Connected Vehicle Experience, or CVX) that grounds its answers by retrieving from ADP’s `vehicle_knowledge_base` data product across an AWS account boundary. This is a pattern for builders who want to connect an AI agent to governed automotive knowledge.
- **Example 2** — a natural-language query interface for business executives ([Amazon Quick Suite](../../../quicksuite/latest/userguide.md "../../../quicksuite/latest/userguide.md") / [Quick Desktop](../../../quick/latest/userguide/what-is-desktop.md "../../../quick/latest/userguide/what-is-desktop.md")) that subscribes to ADP data products via Amazon DataZone and answers operational questions without writing a line of SQL. This is a pattern for business users who want self-service access to governed data.
- **Example 3** — a proactive briefing agent, built on the same Quick Desktop foundation, that runs on a schedule instead of on demand — delivering a synthesized answer to the questions an executive asks every day or every week, instead of a dashboard they have to remember to open.
  All three examples consume the same nine ADP governed data products. The consumption patterns are completely different. That is the point.

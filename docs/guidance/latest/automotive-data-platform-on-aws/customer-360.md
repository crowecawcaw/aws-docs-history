# Customer 360 Analytics

The Customer 360 Analytics solution provides a comprehensive view of customer interactions, health metrics, and behavioral patterns across the entire customer lifecycle. By combining [Amazon Quick Suite](../../../quicksuite/latest/userguide.md "../../../quicksuite/latest/userguide.md") dashboards with Bedrock AI agents, this use case enables automotive companies to deliver personalized experiences, predict customer needs, and proactively address issues.

This chapter describes the architecture and design patterns for building a Customer 360 solution on top of the Automotive Data Platform. The v0.2 foundation deploy provides the governed data-product layer this pattern builds on — specifically the `customer_360`, `customer_interactions`, and `service_records` data products (see [Data products](data-products.md "data-products.md")). The analytics and AI layers described here represent a full implementation pattern informed by a reference deployment, but are not themselves provisioned by the `platform-foundation/` codebase today.

## What you’ll build

- Interactive dashboards with Quick Suite for visualizing customer sentiment and quality issues
- Automated workflows with [Amazon Quick Automate](../../../quicksuite/latest/userguide/using-amazon-quick-automate.md "../../../quicksuite/latest/userguide/using-amazon-quick-automate.md") for detecting critical issues
- Approval processes with [Amazon Quick Flows](../../../quicksuite/latest/userguide/using-amazon-quick-flows.md "../../../quicksuite/latest/userguide/using-amazon-quick-flows.md") for stakeholder notifications
- AI-powered conversational analytics with Bedrock agents
- Knowledge base with Aurora pgvector for semantic search

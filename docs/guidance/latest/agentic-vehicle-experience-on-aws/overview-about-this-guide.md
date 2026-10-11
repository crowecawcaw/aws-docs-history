

# About This Guide
<a name="overview-about-this-guide"></a>

This guide is prescriptive. It explains how to build a agentic vehicle experience on AWS using AVX’s architecture and patterns and how to extend, customize, and operate it for a production customer-engagement workload.

The guide is organized as follows:
+  **Guidance Overview** (this chapter) — What AVX is, the customer-journey vision, an illustrative end-to-end scenario, features, personas, and cost introduction.
+  **Architecture Overview** — The AVX composition layer over CMS, ADP, and Amazon Connect; the agent mesh; request and data flow; deployment topology.
+  **The Customer Journey** — Prescriptive guidance on the five journey stages (Find, Acquire, Own, Service, Sell) and the agentic patterns that power each stage.
+  **Agentic Architecture** — Amazon Bedrock AgentCore, the Strands supervisor and specialist mesh, Nova 2 Sonic voice, deterministic-first triage, and booking.
+  **Building on CMS and ADP** — The composition and data-fusion pattern: how to wire an AVX deployment to existing CMS and ADP stacks.
+  **Contact Center Integration** — Amazon Connect voice and chat channels, tenant-branded contact flows, the driver-confirmed handoff, and the context the tier-2 agent receives.
+  **Personas and Tenancy** — The six personas, multi-tenancy configuration, and server-side persona inference.
+  **Knowledge and Grounding** — Grounding strategy: reference data via Bedrock KB RAG versus tabular data via AgentCore Memory LTM.
+  **Plan Your Deployment** — Prerequisites, supported regions, detailed cost model, and service quotas.
+  **Deploy the Guidance** — How to stand AVX up on the CMS and ADP foundation; tenant onboarding.
+  **Security** — Multi-tenant authentication, tenant isolation, cross-account data access, PII handling, and the P0 safety guardrail.
+  **Extend and Customize** — Adding a persona, a specialist agent tool, a tenant-specific agent, or a partner integration.
+  **Troubleshooting** — Known issues and operational constraints drawn from the AVX repository’s issues directory.
+  **Reference** — AWS services, partner integration points, and API summary.
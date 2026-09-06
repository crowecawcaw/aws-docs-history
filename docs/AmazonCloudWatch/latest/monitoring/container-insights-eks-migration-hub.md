

# Migration guides
<a name="container-insights-eks-migration-hub"></a>

This section provides step-by-step migration guides for moving from your current Container Insights setup to OTel Container Insights — the recommended, actively developed approach.

## Why migrate?
<a name="container-insights-eks-migration-hub-why"></a>

OTel Container Insights is the recommended approach for Amazon EKS observability. Migrating provides the following benefits:
+ **Active development** — OTel Container Insights receives new features, performance improvements, and expanded signal coverage on an ongoing basis.
+ **Enhanced Observability** — Access detailed Kubernetes metrics at the pod, node, and cluster level with comprehensive log collection.
+ **OpenTelemetry standard** — Built on the industry-standard observability framework, compatible with existing PromQL dashboards and community documentation.

## What's covered
<a name="container-insights-eks-migration-hub-coverage"></a>

Each migration guide covers the following areas:
+ **Parallel run** — Run both metrics streams simultaneously to validate data equivalence before switching over.
+ **Breaking changes** — Removed features and changed defaults that might affect your workflows.
+ **Migration steps** — A phased procedure for cutover with minimal monitoring gaps.
+ **Verification** — Confirm that equivalent data flows through the new pipeline.
+ **Rollback** — Restore your previous approach if needed.

## Available migration guides
<a name="container-insights-eks-migration-hub-topics"></a>

Choose the guide that matches your current Container Insights setup.

**Topics**
+ [Migrate from Enhanced Container Insights (Classic) to OTel Container Insights](container-insights-eks-migrate-from-classic.md) — Migrate from Enhanced Container Insights (Classic) to OTel Container Insights through an in-place add-on version update.


# Compare Container Insights approaches
<a name="container-insights-eks-compare"></a>

Two Container Insights approaches are available for Amazon EKS clusters, each with different capabilities, deployment models, and support levels. Both use the same `amazon-cloudwatch-observability` Amazon EKS add-on — the difference is the add-on version and configuration.

Use this page to understand the differences between the two approaches and determine which one is right for your environment. For detailed setup instructions, see [OTel Container Insights (Recommended)](container-insights-eks-otel.md) or [Enhanced Container Insights (Classic)](container-insights-eks-classic.md).

## Feature comparison
<a name="container-insights-eks-compare-table"></a>

The following table compares the two Container Insights approaches across key attributes.


| Attribute | OTel Container Insights | Enhanced Container Insights (Classic) | 
| --- | --- | --- | 
| Supported signals | Metrics, logs | Metrics, logs | 
| Enhanced Observability | Yes | Yes | 
| Maintenance status | Active development | Maintenance mode | 
| Deployment complexity | Low | Low | 
| Setup method | Amazon EKS add-on (OTel-based) | Amazon EKS add-on (managed) | 
| Minimum Amazon EKS version | 1.28 | 1.25 | 
| Minimum add-on version | v6.2.0 | Prior to v6.2.0 | 
| Configuration model | Add-on configuration | Add-on configuration | 
| Metric format | Prometheus/PromQL-native | CloudWatch-format (EMF) | 

## Capabilities and limitations
<a name="container-insights-eks-compare-capabilities"></a>

Each approach has specific strengths and constraints. Review the following sections to understand what each approach provides and where it has limitations.

### OTel Container Insights (Recommended)
<a name="container-insights-eks-compare-otel-capabilities"></a>

OTel Container Insights provides the following capabilities:
+ Full-signal observability through a single OpenTelemetry-based agent
+ Active development with new features delivered regularly
+ Simplified deployment as a managed Amazon EKS add-on
+ PromQL-queryable metrics with up to 150 labels per metric

OTel Container Insights has the following limitations:
+ Requires Amazon EKS 1.28 or later
+ Requires add-on version v6.2.0 or later
+ Newer offering with a smaller ecosystem of community examples

For setup instructions, see [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md).

### Enhanced Container Insights (Classic)
<a name="container-insights-eks-compare-classic-capabilities"></a>

Enhanced Container Insights (Classic) provides the following capabilities:
+ Managed Amazon EKS add-on with automated lifecycle management
+ Supports Enhanced Observability

Enhanced Container Insights (Classic) has the following limitations:
+ In maintenance mode — receives security patches only
+ Limited configuration flexibility
+ Metrics use proprietary CloudWatch-format names, not compatible with standard PromQL dashboards

For setup instructions, see [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md).

## Decision guide
<a name="container-insights-eks-compare-decision"></a>

Use the following table to determine which approach is right for your situation.


| Selection criteria | Recommended approach | Rationale | 
| --- | --- | --- | 
| New Amazon EKS deployment | OTel Container Insights | Actively developed, full signal coverage, lowest complexity | 
| Need full Enhanced Observability | OTel Container Insights | Only actively developed option | 
| Already running Classic in production | Classic (short-term), OTel (migration target) | Continue for stability, then plan migration | 
| Prefer managed add-on with minimal overhead | OTel Container Insights | Low configuration burden | 
| Need PromQL-compatible metrics | OTel Container Insights | Preserves original Prometheus metric names | 

If you are currently running Enhanced Container Insights (Classic) and want to migrate, see [Migration guides](container-insights-eks-migration-hub.md) for step-by-step instructions.

## Prerequisites summary
<a name="container-insights-eks-compare-prerequisites"></a>

The following table lists the prerequisites for each approach.


| Prerequisite | OTel Container Insights | Enhanced Container Insights (Classic) | 
| --- | --- | --- | 
| Minimum Amazon EKS version | 1.28 | 1.25 | 
| Minimum add-on version | v6.2.0 | Prior to v6.2.0 | 
| IAM permissions | CloudWatchAgentServerPolicy | CloudWatchAgentServerPolicy | 
| Required tools | kubectl, AWS CLI | kubectl, AWS CLI | 
| OIDC provider required | Yes (for IRSA) | Yes (for IRSA) | 

## Next steps
<a name="container-insights-eks-compare-next-steps"></a>

After you choose an approach, use the following links to get started:
+ [Quick start: OTel Container Insights on Amazon EKS](container-insights-eks-otel-quickstart.md) — Set up OTel Container Insights with the fastest path.
+ [Setup guide (AWS CLI)](container-insights-eks-classic-setup.md) — Set up Enhanced Container Insights (Classic).
+ [Migration guides](container-insights-eks-migration-hub.md) — Migrate from Classic to OTel Container Insights.
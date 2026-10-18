

# Observability
<a name="smops02"></a>

Streaming workflows are distributed systems spanning ingest, processing, origin, CDN, and client. Detecting, diagnosing, and resolving issues requires visibility into metrics, events, and dependencies across all of these layers.


| SMOPS02: How do you achieve full observability across your streaming video workflow? | 
| --- | 
| [SMOPS02-BP01 Establish performance metrics by defining key performance indicators (KPIs) and service-level objectives (SLOs)](smops02-bp01.md) | 
| [SMOPS02-BP02 Implement comprehensive monitoring and collect granular metrics across all layers of your streaming stack](smops02-bp02.md) | 
| [SMOPS02-BP03 Implement centralized logging to aggregate logs from all components of your streaming stack](smops02-bp03.md) | 
| [SMOPS02-BP04 Instrument your streaming application code and infrastructure for observability](smops02-bp04.md) | 

## Capability intent
<a name="smops02-intent"></a>
+ KPIs and SLOs are defined for each layer of the streaming workflow.
+ Metrics are collected at sufficient granularity to isolate issues to specific components.
+ Logs from all components are aggregated and correlated for cross-workflow troubleshooting.
+ Application code is instrumented with contextual telemetry for rapid diagnosis.

## Common issues to watch for
<a name="smops02-issues"></a>
+ Metrics defined but not tied to alerting thresholds or SLOs.
+ Logs siloed per component with no way to correlate events across the pipeline.
+ Client-side telemetry missing, so viewer-facing quality issues go undetected.
+ Observability instrumentation added after launch rather than built in.
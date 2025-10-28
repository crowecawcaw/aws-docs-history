# GENPERF01-BP02 Collect performance metrics from generative AI

workloads

Foundation model performance on specific tasks is measured in many
different ways. It is important to measure and discern the
performance of a model over time when selecting foundation models
for generative AI workloads.

**Desired outcome:** When
implemented, your organization improves its ability to evaluate
model performance.

**Benefits of establishing this best
practice:**
[Experiment
more often](../framework/rel-dp.md "../framework/rel-dp.md") - Testing model performance assists in the
selection of foundation models for generative AI workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Consider introducing a centralized logging and monitoring solution
for generative AI workloads. For example, Amazon CloudWatch
integrates directly with other AWS services like Amazon Bedrock,
the Amazon Q family of services, and Amazon SageMaker AI Inference
Endpoints. By configuring Amazon CloudWatch or similar, customers
collect performance metrics from model endpoints. These metrics
can be used to develop and prioritize a list of roadmap
improvements to generative AI solutions.

Performance metrics should also be collected by applications and
services that interact with model endpoints and other generative
AI services. Collect metrics and application traces pertaining to
the flow of information, rather than just a specific piece of the
workflow. Use Amazon CloudWatch or similar to determine how your
entire application performs when interacting with generative AI
solutions. This can help you triage performance concerns faster
and improve resolution times.

### Implementation steps

1. Identify and collect CloudWatch metrics.
   - Implement a trace framework like [OpenLLMetry](https://github.com/traceloop/openllmetry "https://github.com/traceloop/openllmetry") to capture
     additional metrics.

2. Establish reasonable alarm thresholds, and set alerts to go
   off when those thresholds are breached.
3. Determine the remediation action for the alarm.
   - Infrastructure alarms may require horizontal scaling to
     remediate any issues.
   - Model alarms may inform a re-examination of the model
     selection process.

4. Automate resolution actions where possible.

## Resources

**Related practices:**

- [PERF05-BP01](../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md "../performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.md")
- [PERF05-BP02](../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md "../performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.md")
- [PERF05-BP03](../performance-efficiency-pillar/perf_process_culture_workload_performance.md "../performance-efficiency-pillar/perf_process_culture_workload_performance.md")
- [PERF05-BP05](../performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.md "../performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.md")

**Related guides, videos, and documentation:**

- [Monitor
  the health and performance of Amazon Bedrock](../../../bedrock/latest/userguide/monitoring.md "../../../bedrock/latest/userguide/monitoring.md")

**Related examples:**

- [Monitoring
  Generative AI application using Amazon Bedrock and Amazon CloudWatch integration](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/ "https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/")

**Related tools:**

- [Traceloop
  OpenLLMetry](https://github.com/traceloop/openllmetry "https://github.com/traceloop/openllmetry")

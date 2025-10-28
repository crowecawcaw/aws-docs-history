# SCPERF05-BP02 Evaluate compliance with performance requirements

When many systems, including third-party systems, are involved in
a workload, it is important to know the behavior of each system
and to monitor who is contributing to performance loss so proper
adjustments can be made.

**Desired outcome**: Optimum
performance that conforms to the system requirements to handle
loads.

**Benefits of establishing this best
practice:** Enhanced visibility into system performance
across complex supply chain networks, improved ability to identify
and resolve performance bottlenecks, better accountability for
third-party system performance, and reduced mean time to
resolution for performance issues.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Monitoring of your workload at multiple levels helps verify that
your resources are performing as expected and you are aware of
deviations. Consider all dimensions of the solution for
monitoring, for example client-side and server-side metrics,
application metrics and infrastructure metrics, technical and
functional metrics.

Provide visibility of data loss in your metrics, for example, by
monitoring for lost messages.

Where possible capture inter-solution and inter-process
communication streams to aid with the reproduction of issues.

### Implementation steps

1. Establish performance baselines and SLAs for all supply
   chain systems, including third-party integrations.
2. Implement comprehensive monitoring across all system
   layers, including infrastructure, application, and
   business metrics.
3. Deploy distributed tracing to track performance across
   complex supply chain workflows and identify bottlenecks.
4. Create automated performance testing and validation
   processes to make sure systems meet established
   requirements.
5. Implement alerting mechanisms that notify teams when
   performance deviates from established baselines or SLA
   thresholds.
6. Conduct regular performance reviews and optimization
   initiatives based on monitoring data and compliance
   assessments.

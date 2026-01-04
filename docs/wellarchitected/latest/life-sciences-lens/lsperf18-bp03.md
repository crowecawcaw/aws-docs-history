# LSPERF18-BP03 Create integrated dashboards showing both

performance and metrics

The integrated dashboards combine performance and metrics into clear
visualizations. Teams gain complete system visibility through
real-time data, which enables direct decision-making and reduces
process delays. The system enhances operations while maintaining
scientific integrity and patient safety standards. Teams use this
data to optimize systems while meeting medical and regulatory
requirements.

**Desired outcome:** Deploy
integrated dashboards with real-time visualization of performance
and metrics, providing complete system visibility that enables
immediate decision-making, reducing process delays, and allows teams
to optimize operations while maintaining scientific integrity and
patient safety standards.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To effectively implement integrated monitoring systems, develop
comprehensive dashboards that seamlessly combine technical
performance metrics with audit indicators in clear, actionable
visualizations. These unified interfaces should present real-time
data streams that provide complete system visibility to both
technical and scientific stakeholders, reducing information silos
that typically delay decision-making processes.

Configure the dashboards to display critical performance
parameters (such as response times, throughput, and resource
utilization) alongside relevant metrics (including data quality
indicators, validation status, and regulatory adherence scores).
This integrated approach enables cross-functional teams to make
informed, data-driven decisions without process delays that often
occur when metrics are segregated across different systems.

Implement automated alerting mechanisms that notify appropriate
personnel when metrics approach predefined thresholds, allowing
proactive intervention before issues impact operations. The
monitoring system should maintain comprehensive audit trails that
document both performance optimizations and regulatory adherence,
supporting regulatory requirements while enabling continuous
improvement.

### Implementation steps

1. Deploy Amazon CloudWatch dashboards with custom generative
   AI performance widgets.
2. Integrate AWS Audit Manager metrics for visualization.
3. Implement Amazon EventBridge for real-time alerts on
   threshold violations.
4. Use Quick Suite for interactive data exploration and
   analysis.
5. Configure AWS Systems Manager for automated remediation
   workflows.

# LSPERF19-BP03 Schedule regular performance tests with

production-representative data
loads

Institute a cadence of regular performance tests using simulated
research and clinical data that accurately represents production
workloads in terms of volume, variety, and velocity. These scheduled
tests should be integrated into your development pipeline to
identify performance bottlenecks early, before they impact
production operations. Vary test scenarios to account for both
typical daily operations and peak usage patterns, such as
end-of-month processing or seasonal research activities. Complement
scheduled tests with on-demand testing triggered by significant
system changes. This proactive approach to performance validation
verifies that scientific and clinical users consistently experience
responsive systems that meet their demanding computational
requirements.

**Desired outcome:** By implementing
a comprehensive performance testing framework, scientific and
clinical users experience consistently responsive systems that meet
their computational requirements, with zero production incidents
caused by performance bottlenecks.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing effective performance testing for generative AI
systems requires establishing a consistent cadence of regular
evaluations using carefully constructed datasets that accurately
represent production workloads. Organizations should develop
simulated research and clinical data that mirrors actual usage
patterns in terms of volume, variety, and velocity
characteristics, verifying that test results provide meaningful
insights about real-world performance. Integrate these scheduled
performance tests directly into development pipelines as automated
gates, enabling early identification of potential bottlenecks
before they can impact production operations or scientific
outcomes.

Design a comprehensive testing strategy that incorporates diverse
scenarios reflecting both typical daily operations and anticipated
peak usage patterns, such as end-of-month processing surges or
seasonal research activities that might stress system resources.
Complement the regular testing schedule with targeted, on-demand
evaluations triggered by significant system changes, including
infrastructure updates, algorithm modifications, or data pipeline
adjustments.

This proactive, multi-faceted approach to performance validation
creates a robust quality framework so that scientific and clinical
users consistently experience responsive systems capable of
meeting their demanding computational requirements.

### Implementation steps

1. Deploy AWS DevOps tools like AWS CodePipeline with Amazon CloudWatch Synthetics for automated testing cycles.
2. Use Amazon SageMaker AI Experiments to track model performance
   across different test scenarios.
3. Implement AWS Step Functions to orchestrate complex testing
   workflows with varying loads.
4. Configure Amazon EventBridge to trigger on-demand tests when
   detecting significant system changes.
5. Use Quick Suite dashboards to visualize performance
   trends across testing cycles.

# SCPERF05-BP03 Integrate performance testing into the release cycle of the supply chain application

Load testing results help you measure how the system behaves while
in high-traffic or heavy loads. Note these measurements to help
you adjust the underlying resources without wasting cost by
over-provisioning.

**Desired outcome:** Properly sized
supply chain applications.

**Benefits of establishing this best
practice:** Cost optimization, resilience, durability,
and improved user experience.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Verify consistency and failure recovery during load tests.
Verify data consistency and recovery during periods of high
load. Making sure that your workload's RTO and RPO is still
valid under the highest load can uncover gaps in your
architecture and operational resilience.

Understand performance of the system under peak load and in
failure scenarios: Include testing of common failure scenarios
in your performance testing suites to understand your workload
behavior in these situations and determine areas for
improvement.

### Implementation steps

1. Develop comprehensive performance testing strategies that
   simulate realistic supply chain load patterns and peak
   usage scenarios.
2. Integrate automated performance testing into CI/CD
   pipelines to validate performance with every major
   release.
3. Implement chaos engineering practices to test system
   resilience and recovery capabilities under various failure
   conditions.
4. Create performance test scenarios that include third-party
   system integrations and supplier network dependencies.
5. Establish performance regression testing to make sure new
   releases don't degrade existing system performance.
6. Document and analyze performance test results to
   continuously improve system architecture and resource
   allocation strategies.

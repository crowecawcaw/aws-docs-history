

# SMOPS03-BP02 Conduct thorough pre-event testing for large-scale streaming events
<a name="smops03-bp02"></a>

Before high-profile streaming events, conduct thorough testing to validate the entire workflow's capacity, reliability, and performance under expected load conditions. This testing helps identify potential issues before they impact viewers during the actual event.

**Desired outcome:**
+ Validated streaming infrastructure that performs reliably under peak load conditions, with identified and mitigated risks before the live event.

**Benefits of establishing this best practice:**
+ Early identification of potential bottlenecks
+ Validation of scaling mechanisms
+ Improved confidence in system reliability
+ Reduced risk of viewer-affecting issues during events

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Thorough testing strategies for large-scale events validate that the streaming infrastructure can handle expected demand and recover gracefully from failures.

Load testing simulates expected viewer counts and behaviors, tests gradual ramp-up and sudden spikes in traffic, validates performance across different geographic regions, and tests with realistic device and player distributions. This validates that the system can handle the expected scale.

Failover testing validates encoder failover mechanisms, tests regional failover procedures, simulates content delivery network (CDN) failures to validate redundancy, and tests origin failover capabilities. These tests confirm that redundancy mechanisms function correctly under stress.

Workflow testing validates the entire streaming workflow under load, tests monitoring and alerting systems, verifies metrics collection and dashboard functionality, and tests runbooks and automation procedures. This confirms operational readiness beyond just infrastructure capacity.

Chaos engineering introduces controlled failures during test events, validates system resilience to component failures, tests recovery procedures and self-healing capabilities, and identifies single points of failure. This approach builds confidence that the system can withstand unexpected disruptions during the live event.

### Implementation steps
<a name="implementation-steps"></a>

1. **Define testing objectives:** Define testing objectives and success criteria that match the expected event scale and business requirements.

1. **Design test scenarios based:** Design test scenarios based on expected event conditions including peak viewership, geographic distribution, and device mix.

1. **Build test infrastructure and:** Build test infrastructure and tooling capable of generating realistic load patterns at the expected scale.

1. **Execute progressive test scenarios:** Execute progressive test scenarios starting with baseline tests and increasing to peak load and failure injection.

1. **Document findings and address:** Document findings and address identified issues with prioritized remediation plans.

1. **Conduct remediation verification testing:** Conduct remediation verification testing to confirm that identified issues have been resolved.

1. **Perform final dress rehearsal:** Perform a final dress rehearsal before the event that exercises the complete workflow under realistic conditions.

1. **Document lessons for future:** Document lessons for future events to continuously improve the pre-event testing process.

## Resources
<a name="resources"></a>

**Related documents**
+ [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)
+ [AWS Fault Injection Service](https://aws.amazon.com/fis/)

**Related services**
+ [Amazon CloudWatch Synthetics](https://aws.amazon.com/cloudwatch/)
+ [AWS Fault Injection Service](https://aws.amazon.com/fis/)
+ [Amazon EC2](https://aws.amazon.com/ec2/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
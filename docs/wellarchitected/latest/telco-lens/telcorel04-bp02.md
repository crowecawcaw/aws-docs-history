# TELCOREL04-BP02 Implement dual network planes for signaling or

control plane

A resilient network architecture implementing two independent and redundant signaling
networks that operate in parallel. Each signaling plane handles messages and controls network
resources independently, with logical and physical separation to verify that failures in one
plane do not impact the other plane's operations.

**Desired outcome:**

- Enhanced fault tolerance through dual planes.
- Independent operation capability.
- Seamless failover between planes.
- Maintained service continuity.
- Isolated failure domains.
- Verified redundancy effectiveness.
- Documented recovery procedures.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Design a resilient network architecture with separate signaling planes for control plane
traffic, maintaining comprehensive logical and physical separation. Enforce strict network
access controls and security zoning to maintain the separation. Configure robust failover
mechanisms, with automated triggers, recovery procedures, and comprehensive health monitoring
across the planes. Test the failover functionality under various failure scenarios and
document the recovery steps. Deploy advanced monitoring and observability tools to track the
performance, availability, and security of both signaling planes, establish key metrics and
alerting thresholds, and regularly review the monitoring strategy for continuous improvement.

### Implementation steps

- Design separate signaling planes:
  - Use AWS Transit Gateway and AWS Network Firewall to implement a
    vendor-neutral strategy for logical and physical separation between control and user
    plane traffic. Configure AWS Network ACLs and security groups to enforce network
    zoning, traffic classification, and security controls.

- Verify physical separation:
  - Use AWS Config to specify and enforce the
    technical requirements for network isolation, including network segments,
    addressing, and security controls. Use AWS Config Rules to monitor and enforce requirements
    affecting the separation.
  - Deploy the separate network infrastructure for
    each plane using Amazon VPC and AWS Direct Connect. Utilize AWS Transit Gateway and AWS Network Firewall to
    implement network virtualization and segmentation.
  - Configure AWS Network Firewall and Amazon VPC security groups to
    enforce strict network access controls and security policies. Define and enforce the
    security zones and trust boundaries using AWS IAM and AWS Service Control
    Policies.

- Configure failover mechanisms:
  - Use Amazon CloudWatch alarms and AWS Lambda functions to
    establish the conditions and thresholds for automated failover.
  - Deploy Amazon CloudWatch and AWS Lambda to monitor the health of
    the planes and trigger the appropriate failover responses.
  - Use AWS Fault Injection Service to regularly test the failover
    functionality under various failure conditions. Document the test procedures and
    success criteria in AWS Systems Manager.
  - Create detailed recovery procedures for different
    failure scenarios. Include troubleshooting guides and contact information.

- Monitor plane status:
  - Use Amazon CloudWatch to monitor the performance,
    availability, and security metrics for both planes.
  - Establish key performance indicators using Amazon CloudWatch
    that reflect service health, including latency, throughput, error rates, and
    resource utilization. Set appropriate thresholds and baselines.
  - Configure Amazon CloudWatch alarms and Amazon SNS to implement a notification
    system for critical events and threshold violations. Define alert severity levels
    and response procedures.
  - Regularly evaluate monitoring strategy effectiveness and
    adjust based on operational experience. Update metrics and thresholds as needed.

## Resources

**Key AWS services:**

- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")

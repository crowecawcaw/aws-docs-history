# HNREL06-BP02 Ensure service continuity with redundant hardware

and diverse telecommunications providers

Implementing redundant hardware components across geographic
locations, organizations can mitigate single points of failure that
threaten critical workloads. This resilience strategy should extend
beyond computing resources to include diverse telecommunications
providers, creating independent network paths that remain
operational even when regional carriers experience outages. The
combination of hardware redundancy and carrier diversity creates a
robust foundation that enables businesses to maintain operations
through localized disruptions, ensuring that customers experience
minimal service interruptions and that service level agreements
remain intact despite infrastructure challenges.

**Desired outcome:** Reduce risk of
connectivity loss due to hardware or carrier failures, maintaining
consistent hybrid network availability.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Increases fault tolerance and uptime
- Minimizes downtime from single hardware or carrier outages
- Supports disaster recovery planning
- Helps meet or exceed AWS and provider SLA commitments

## Implementation guidance

- Use separate network devices and cables for each connection.
- Engage more than one telecom provider with diverse paths for
  "last mile" connections.
- Periodically review and test infrastructure and SLAs.

## Resources

- [AWS Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/ "https://aws.amazon.com/directconnect/sla/")

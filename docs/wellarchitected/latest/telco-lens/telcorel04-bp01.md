# TELCOREL04-BP01 Implement the Bypass Mode on peripheral

network devices such as firewalls and network probes while connecting to the cloud

Implementing bypass mode on network peripheral devices like firewalls and network probes is
crucial for maintaining service continuity during device failures or power outages. This
mechanism automatically creates a direct connection between incoming and outgoing network ports
when a device fails, maintaining that critical network traffic continues to flow without
interruption. By deploying bypass-capable devices while connecting to the cloud-based network
infrastructure, telecom operators can block service disruptions that could occur during device
failures, maintenance windows, or unexpected outages. This approach is particularly important
for maintaining high availability in telecommunications networks where continuous service is
essential for customer satisfaction and regulatory adherence.

**Desired outcome:**

- Verify continuous network traffic flow during device level failures.
- Minimize service disruptions during maintenance or unexpected outages.
- Maintain high availability for critical network services.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Design your network architecture to include redundant paths and automated routing updates
that can quickly respond to device failures. Implement comprehensive health monitoring and
automated recovery procedures to minimize service disruptions. Establish clear operational
procedures for managing bypass events, including notification workflows and post-event
analysis to block recurring issues.

Regular testing of the bypass functionality is crucial to verify it will work as expected
during actual failures. This includes conducting controlled failure scenarios during
maintenance windows and validating that traffic continues to flow without interruption.
Document bypass events and maintain historical data to identify patterns and potential
improvements to the bypass implementation.

### Implementation steps

- Deploy AWS Network Firewall with fail-open configurations across multiple Availability Zones
  to verify continuous traffic flow during failures.
- Configure AWS Transit Gateway for centralized network management with automatic routing
  failover capabilities.
- Use Amazon CloudWatch to monitor device health and performance metrics, with automated
  alerts for potential failures on AWS services involved.

## Resources

**Key AWS services:**

[AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")

[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")

# HNSEC03-BP01 Implement network traffic monitoring and threat

detection

Monitor and implement an immediate response process that detects and
reacts to any suspicious or malicious activity. Continuously
monitoring workloads helps to identify security incidents faster. At
a minimum, the metadata of logs should be captured for hybrid
network connections with private connections.

**Desired outcome:** Detect
suspicious or unauthorized activity and improve security posture by
capturing and analyzing network traffic logs.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables early detection and response to security incidents
- Provides visibility into hybrid network activity
- Helps with forensic analysis and compliance reporting
- Reduces risk of undetected malicious activity

## Implementation guidance

- Enable flow logs on all relevant networks using services such
  as VPC Flow Logs and Transit Gateway Flow Logs
- Enable continuous threat detection across network traffic and
  accounts. For example, you can achieve this with Amazon GuardDuty.
- Review findings regularly and establish automated or manual
  incident response processes.
- Store and analyze logs in a central location for correlation
  and investigation.

## Resources

- [Logging
  IP traffic using VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md")
- [AWS Transit Gateway Flow Logs](../../../vpc/latest/tgw/tgw-flow-logs.md "../../../vpc/latest/tgw/tgw-flow-logs.md")
- [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md")
- [Centralized
  Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/ "https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/")

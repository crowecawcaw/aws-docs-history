# HNSEC01-BP03 Implement continuous logging

Continuous logging provides real-time visibility across on-premises
and cloud infrastructures. Implementing comprehensive logging
mechanisms enables teams to quickly detect anomalies, troubleshoot
connectivity issues, and maintain a consistent audit trail for
security compliance.

**Desired outcome:** Achieve
continuous visibility, reduce mean time to resolution during
incidents, and automated enforcement of compliance configurations.

**Benefits of establishing this best
practice:**

- Enables prompt incident detection and response
- Provides clear audit trails for compliance
- Ensures ongoing alignment with regulatory standards
- Reduces manual compliance effort

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

- Capture cloud environment API activities using services such
  as AWS CloudTrail.
- Enable flow logs for network visibility using services such as
  VPC Flow Logs and Transit Gateway Flow Logs.

## Resources

- [AWS services for logging and monitoring](../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.md "../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.md")
- [AWS Transit Gateway Flow Logs](../../../vpc/latest/tgw/tgw-flow-logs.md "../../../vpc/latest/tgw/tgw-flow-logs.md")
- [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
- [Logging
  IP traffic using VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md")

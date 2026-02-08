# HNSEC02-BP01 Implement a landing zone

Implementing a landing zone establishes a standardized, secure
foundation for hybrid networking infrastructure. A landing zone
provides centralized identity and access management, standardized
security controls, governance mechanisms, network architecture, and
account structures that enable scalable growth while maintaining
compliance. By automating resource provisioning and implementing
guardrails from the start, organizations can avoid costly rework
later while accelerating their cloud adoption journey with
confidence, knowing they have established proper security boundaries
and operational efficiency from day one.

**Desired outcome:** Establish a
secure foundation for your hybrid networking environment with
consistent architecture and configuration controls.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Ensures consistent security and compliance across all accounts
- Automates account provisioning and governance
- Reduces operational overhead and human error
- Enables scalable and secure hybrid networking environment

## Implementation guidance

- Deploy a landing zone using services such as AWS Control Tower.
- Apply preventive and detective guardrails for governance and
  compliance.
- Standardize account creation and management through Account
  Factory.
- Monitor the landing zone using services such as AWS Control Tower dashboard and Security Hub CSPM.

## Resources

- [AWS Control Tower Landing Zone](../../../controltower/latest/userguide/what-is-aws-control-tower.md "../../../controltower/latest/userguide/what-is-aws-control-tower.md")
- [AWS Control Tower Guardrails](../../../audit-manager/latest/userguide/controltower.md "../../../audit-manager/latest/userguide/controltower.md")
- [Provision
  and manage accounts with Account Factory](../../../controltower/latest/userguide/account-factory.md "../../../controltower/latest/userguide/account-factory.md")
- [AWS Control Tower Dashboard](../../../controltower/latest/userguide/control-tower-dashboard.md "../../../controltower/latest/userguide/control-tower-dashboard.md")
- [AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")

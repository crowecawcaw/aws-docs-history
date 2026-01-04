# TELCOREL03-BP01 Use a controlled change management mechanism

for software updates in production

Follow a controlled change management approach that blocks automatic updates in production
environments while maintaining changes are thoroughly tested in lower environments. This
includes establishing proper testing procedures, implementing structured change management, and
maintaining comprehensive rollback capabilities to minimize service disruption during system
updates.

**Desired outcome:**

- Minimized risk of service disruptions from updates.
- Validated changes before production deployment.
- Controlled deployment processes.
- Documented change procedures.
- Verified update effectiveness.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Prevent automatic software updates in production environments on the infrastructure and
network function levels. Implement a controlled change management process for the system and
service updates. Identify update mechanisms, configure update policies to disable automatic
updates while maintaining security adherence, and document detailed manual update procedures.
Establish comprehensive change control processes, including approval workflows, testing
requirements, and documentation standards. Maintain a centralized tracking system for updates
and develop robust rollback capabilities with automated and manual recovery procedures.
Continuously monitor the update process, define clear criteria for triggering rollbacks, and
validate the effectiveness of the recovery mechanisms.

### Implementation steps

- Disable automatic updates in production:
  - Use AWS Systems Manager Patch Manager to manage and control operating system
    and application updates across your AWS environment.
  - Use AWS Config to monitor and audit the configuration of your systems,
    including the update settings.

- Configure update policies:
  - Use AWS Config to define and enforce specific configurations for
    disabling automatic updates while maintaining security.
  - Use AWS Systems Manager Parameter Store to centrally manage and store your
    updated policies and configurations.

- Establish change controls:
  - Use AWS Config Rules to implement comprehensive change management processes,
    including approval workflows, testing requirements, and documentation standards.
  - Use AWS CloudTrail to track and audit update-related activities across your
    AWS environment.

- Create a tracking system:
  - Use AWS Config to track and monitor update-related changes, including
    pending updates, approved changes, and implementation status.
  - Use Amazon DynamoDB to store update-related data and provide an audit trail
    of activities.

- Maintain rollback procedures:
  - Use AWS Systems Manager Automation to design and implement the rollback
    mechanisms, including both automated and manual rollback capabilities.
  - Use Amazon CloudWatch to establish the clear criteria for determining when
    rollback procedures should be initiated, including both automated triggers and
    manual decision points.
  - Use AWS Config to verify the effectiveness of the rollback procedures by
    validating system stability and functionality after rollback completion.

## Resources

**Key AWS services:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")

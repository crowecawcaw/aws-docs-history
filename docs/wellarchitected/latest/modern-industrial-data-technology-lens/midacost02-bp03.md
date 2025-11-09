# MIDACOST02-BP03 Automate production-aware resource decommissioning

Implement automated identification and removal of unused resources synchronized with
production schedules, product lifecycles, and manufacturing compliance requirements. This
automation includes safety checks, rollback procedures, and consideration of maintenance
windows to help prevent disruption to manufacturing operations.

**Desired outcome:** Automated identification and removal of
unused resources synchronized with production schedules, product lifecycles, and manufacturing
compliance requirements.

**Common anti-patterns:**

- Implementing automated removal without considering production schedules
- Using the same automation rules for both IT and OT resources
- Not incorporating manufacturing compliance checks in automation
- Failing to account for interdependencies with MES, SCADA, or other manufacturing
  systems
- Automated decommissioning during production hours
- Not maintaining audit trails for regulated manufacturing processes
- Bypassing quality management system validations

**Benefits of establishing this best practice:**

- Reduced manual intervention
- Consistent application of decommissioning policies
- Immediate cost savings from unused resource removal
- Reduced human error

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Create automated systems that can safely identify, tag, notify relevant stakeholders,
and finally remove resources that are no longer needed, with appropriate safeguards to help
prevent disruption to manufacturing operations.

### Implementation steps

1. Define automation rules for resource identification.
2. Create automated workflows for:
   - Resource tagging
   - Notification of stakeholders
   - Backup creation
   - Resource termination

3. Implement safety checks and rollback procedures.
4. Monitor automation effectiveness.
5. Include manufacturing-specific automation rules:
   - Production schedule-aware decommissioning
   - Product lifecycle milestones
   - Equipment maintenance windows
   - Shift pattern considerations

## Key AWS services

- AWS Lambda
- Amazon EventBridge
- AWS Config Rules
- AWS Systems Manager Automation
- AWS Step Functions
- Amazon SNS

## Resources

**Related documents:**

- [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [Amazon EventBridge](../../../eventbridge/latest/userguide/scheduler.md "../../../eventbridge/latest/userguide/scheduler.md")
- [AWS Step Functions](../../../step-functions/latest/dg/welcome.md "../../../step-functions/latest/dg/welcome.md")
- [Building Lambda functions with Python](../../../lambda/latest/dg/lambda-python.md "../../../lambda/latest/dg/lambda-python.md")

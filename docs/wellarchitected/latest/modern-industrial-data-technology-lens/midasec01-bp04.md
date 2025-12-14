# MIDASEC01-BP04 Automate monitoring and reporting with cloud-ready compliance

tools

Automate the collection, evaluation, and reporting of compliance evidence using AWS Cloud
tools. Tailor configurations to meet industry-specific regulatory requirements such as NIST,
CMMC, or ISO and IEC standards for manufacturing.

**Desired outcome:** Ongoing compliance posture monitoring and
reduced manual effort in security and audit processes.

**Benefits of establishing this best practice:** Improves audit
readiness, reduces cost and error in manual compliance efforts, and verifies continuous
governance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish manufacturing compliance baselines by documenting the required controls for
industrial systems and mapping them to technical implementations.

Then, implement automated monitoring that evaluates industrial system configurations,
tracks security control changes, and validates compliance with manufacturing standards.

Use AWS Config, Security Hub CSPM, and Audit Manager, configured specifically for
manufacturing environments, to continuously monitor both IT and OT systems while maintaining
required compliance evidence.

### Implementation steps

- Enable AWS Config across all Regions and accounts.
- Use AWS Security Hub CSPM to aggregate security findings.
- Map controls in AWS Audit Manager to your industry framework.
- Schedule automated compliance report generation and alerting.

## Resources

**Related documents:**

- [What Is AWS Config?](../../../config/latest/developerguide/what-is-aws-config.md "../../../config/latest/developerguide/what-is-aws-config.md")
- [What is AWS Security Hub?](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md")
- [What is AWS Audit Manager?](../../../audit-manager/latest/userguide/what-is.md "../../../audit-manager/latest/userguide/what-is.md")

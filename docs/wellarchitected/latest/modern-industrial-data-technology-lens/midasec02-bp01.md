# MIDASEC02-BP01 Enforce least privilege and security policies to control system

access

Minimize access rights for users and systems by enforcing least privilege principles.
This reduces the risk of lateral movement and privilege escalation in manufacturing
environments.

**Desired outcome:** Users and systems can only access
resources necessary for their roles, reducing exposure to unauthorized activities.

**Benefits of establishing this best practice:** Limits the
scope of security incidents and enhances overall control over sensitive manufacturing
resources.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Map access requirements for different production roles and critical system
interactions. Implement IAM policies and SCPs aligned with manufacturing functions,
enforcing clear boundaries between IT/OT systems. Monitor access patterns using AWS IAM Access Analyzer to continually align with operational needs.

### Implementation steps

- Conduct role analysis across IT/OT to define minimum required privileges.
- Apply IAM permission boundaries and SCPs at account and organizational unit
  levels.
- Use IAM Access Analyzer to detect overly permissive roles.
- Implement regular audits to verify adherence to least privilege policies.

## Resources

**Related documents:**

- [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [Using IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer.md "../../../IAM/latest/UserGuide/access-analyzer.md")

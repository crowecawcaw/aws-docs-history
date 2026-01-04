# LSSEC01-BP01 Implement the principle of separation of

duties

For users with increased privileges, it is important to distribute
system administration activities, so no one administrator can hide
their activities or control an entire system. Separation of duties
can mitigate risk on critical tasks by requiring separate requesters
and approvers for a task. A common example is the use of an approver
during the
[running
of an automation on AWS Systems Manager](../../../systems-manager/latest/userguide/running-automations-require-approvals.md "../../../systems-manager/latest/userguide/running-automations-require-approvals.md"). This principle can
be used to implement numerous tasks including controlling access to
your cloud resources. Use roles with limited permissions based on
functional needs when increased privileges are not required.

**Desired outcome:** Administrative
tasks related to GxP data stores require approvals.

**Common anti-patterns:**

- Failure to implement a least privilege administration model.
- Lack of approvals in administration workflows.

**Benefits of establishing this best
practice:** By implementing a least-privilege model and
separating duties, appropriate control over access to GxP related
resources can be demonstrated.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Determine which administrative tasks may have the potential to
impact GxP data integrity. For each of these tasks, separate task
approval from task execution.

Configure roles with least privilege to be used for routine
functions that do not require administrative permissions.

### Implementation steps

1. Introduce approval steps into automated administrative
   workflows.
2. Set required IAM permissions as needed.

## Resources

**Related best practices:**

- [SEC03-BP02
  Grant least privilege access](../framework/sec_permissions_least_privileges.md "../framework/sec_permissions_least_privileges.md")

**Related documents:**

- [Run
  an automation that requires approvals](../../../systems-manager/latest/userguide/running-automations-require-approvals.md "../../../systems-manager/latest/userguide/running-automations-require-approvals.md")

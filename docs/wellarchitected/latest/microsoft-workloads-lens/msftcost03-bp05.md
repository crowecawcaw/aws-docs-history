# MSFTCOST03-BP05 Evaluate SQL Server on Linux

Beginning on SQL Server 2017, Microsoft offers the option to run SQL
Server on Linux operating systems. SQL Server on Linux is enterprise
ready and offers flexibility, high performance, security features,
reduced TCO, HA/DR features, and a great user experience. You can
switch from SQL Server on Windows Server to SQL Server on Linux to
save on Windows Server licensing costs.

**Desired outcome:** Successfully
migrate compatible SQL Server workloads from Windows Server to
Linux, resulting in reduced Total Cost of Ownership (TCO) through
elimination of Windows Server licensing costs. This migration would
maintain enterprise-level performance, security, and high
availability features while leveraging the flexibility of SQL Server
on Linux, ultimately optimizing costs for Microsoft workloads in the
organization's IT infrastructure.

**Common anti-patterns:**

- Automatic Migration Without Compatibility Assessment:
  Organizations hastily migrating SQL Server workloads to Linux
  without first evaluating compatibility, resulting in application
  failures, performance issues, and potential data loss due to
  unsupported features or incompatible dependencies.
- Ignoring Total Cost of Operation: Companies focusing solely on
  the potential licensing cost savings of moving to SQL Server on
  Linux, while overlooking other operational costs such as
  retraining staff, modifying existing scripts and tools, and
  potential performance tuning needed in the new environment. This
  narrow focus may lead to unexpected expenses and operational
  challenges that offset the intended cost savings.

**Benefits of establishing this best
practice:**

- Cost Optimization: Elimination of Windows Server licensing fees
  significantly reduces Total Cost of Ownership (TCO), enabling
  better resource allocation across the organization.
- Simplified Cross-Platform Management: Standardization of
  database management across Windows and Linux platforms reduces
  complexity and streamlines operational processes.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement SQL Server on Linux evaluation, start with a
comprehensive workload compatibility assessment. Create a detailed
migration plan including testing and rollback procedures. Conduct
a pilot migration on a non-critical workload. Train IT staff on
Linux and SQL Server on Linux management. Implement the full
migration in stages, closely monitoring performance and
functionality throughout to ensure a smooth transition and achieve
cost savings and management simplification.

### Implementation steps

1. Conduct workload compatibility assessment to identify SQL
   Server instances suitable for Linux migration, reviewing
   feature requirements and dependencies
2. Develop migration plan with testing procedures, success
   metrics, and rollback strategy, including pilot test
   selection
3. Implement pilot migration on selected non-critical workload
   while providing Linux administration training to IT staff
4. Implement phased migration of remaining workloads following
   successful pilot, with continuous monitoring of performance
   and costs

## Resources

**Related documents:**

- [Evaluate
  SQL Server on Linux](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-linux.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-linux.md")
- [Editions
  and supported features of SQL Server 2022 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-editions-and-components-2022?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-editions-and-components-2022?view=sql-server-ver16")

**Related tools:**
[Windows
to Linux replatforming assistant for Microsoft SQL Server
Databases](../../../sql-server-ec2/latest/userguide/replatform-sql-server.md "../../../sql-server-ec2/latest/userguide/replatform-sql-server.md")

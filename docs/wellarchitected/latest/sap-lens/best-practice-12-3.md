# Best Practice 12.3 - Define a recovery

approach for your complete SAP estate

If your SAP estate consists of multiple SAP systems, you need to create a detailed
approach that defines the order in which each system is recovered, based on business
priorities. Evaluate how data loss might impact consistency across systems and business
operations.

**Suggestion 12.3.1 – Create a business continuity plan that includes
restore priority and plans to ensure consistency**

Have a business continuity plan (BCP) that determines the priority to restore each
SAP system based on the classification of systems determined in [Reliability]: [Suggestion 10.1.2 – Classify systems based on the impact of
failure](best-practice-10-1.md "best-practice-10-1.md"). The plan should also consider the impact of cross system consistency
requirements as well as the use of multi-tenant databases on the restore priority.

**Suggestion 12.3.2 – Evaluate any dependencies on shared
services**

As you define your recovery approach, consider which shared services are either part of
the foundation for running your SAP workload (for example, DNS, Active Directory) or
required to perform the restore itself (for example, backup tools). Evaluate risks and
restore prerequisites associated with these dependencies.

**Suggestion 12.3.3 – Create runbooks to be followed in a
disaster**

A predefined runbook ensures that a proven set of steps is followed in the event of a
disaster, reducing the risk or critical activities being missed.

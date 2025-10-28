# OPS02-BP05 Mechanisms exist to request additions, changes, and

exceptions

You can make requests to owners of processes, procedures, and resources. Requests
include additions, changes, and exceptions. These requests go through a change management
process. Make informed decisions to approve requests where viable and determined to be
appropriate after an evaluation of benefits and risks.

**Desired outcome:**

- You can make requests to change processes, procedures, and resources based on assigned ownership.
- Changes are made in a deliberate manner, weighing benefits and risks.

**Common anti-patterns:**

- You must update the way you deploy your application, but there is no way to request a change to the deployment process from the operations team.
- The disaster recovery plan must be updated, but there is no identified owner to request changes to.

**Benefits of establishing this best practice:**

- Processes, procedures, and resources can evolve as requirements change.
- Owners can make informed decisions when to make changes.
- Changes are made in a deliberate manner.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement this best practice, you need to be able to request changes to processes,
procedures, and resources. The change management process can be lightweight. Document
the change management process.

**Customer example**

AnyCompany Retail uses a responsibility assignment (RACI) matrix to identify who owns changes for processes, procedures,
and resources. They have a documented change management process that’s lightweight and easy
to follow. Using the RACI matrix and the process, anyone can submit change requests.

**Implementation steps**

1. Identify the processes, procedures, and resources for your workload and the owners for each. Document them in your knowledge management system.
   1. If you have not implemented [OPS02-BP01 Resources have identified owners](ops_ops_model_def_resource_owners.md "ops_ops_model_def_resource_owners.md"),
      [OPS02-BP02 Processes and procedures have identified
      owners](ops_ops_model_def_proc_owners.md "ops_ops_model_def_proc_owners.md"), or
      [OPS02-BP03 Operations activities have identified owners
      responsible for their performance](ops_ops_model_def_activity_owners.md "ops_ops_model_def_activity_owners.md"), start with those first.

2. Work with stakeholders in your organization to develop a change management process.
   The process should cover additions, changes, and exceptions for resources, processes, and procedures.
   1. You can use [AWS Systems Manager Change Manager](../../../systems-manager/latest/userguide/change-manager.md "../../../systems-manager/latest/userguide/change-manager.md") as a change management platform for workload resources.

3. Document the change management process in your knowledge management system.

**Level of effort for the implementation plan:** Medium. Developing a change
management process requires alignment with multiple stakeholders across your organization.

## Resources

**Related best practices:**

- [OPS02-BP01 Resources have identified owners](ops_ops_model_def_resource_owners.md "ops_ops_model_def_resource_owners.md") - Resources need identified owners before you build a change management process.
- [OPS02-BP02 Processes and procedures have identified
  owners](ops_ops_model_def_proc_owners.md "ops_ops_model_def_proc_owners.md") - Processes need identified owners before you build a change management process.
- [OPS02-BP03 Operations activities have identified owners
  responsible for their performance](ops_ops_model_def_activity_owners.md "ops_ops_model_def_activity_owners.md") - Operations activities need identified owners before you build a change management process.

**Related documents:**

- [AWS Prescriptive Guidance - Foundation palybook for AWS large migrations: Creating RACI matrices](../../../prescriptive-guidance/latest/large-migration-foundation-playbook/team-org.md#raci "../../../prescriptive-guidance/latest/large-migration-foundation-playbook/team-org.md#raci")
- [Change Management in the Cloud Whitepaper](../../../whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.md "../../../whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.md")

**Related services:**

- [AWS Systems Manager Change Manager](../../../systems-manager/latest/userguide/change-manager.md "../../../systems-manager/latest/userguide/change-manager.md")

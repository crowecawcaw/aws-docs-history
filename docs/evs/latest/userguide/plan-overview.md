

# Plan

Some choices, such as the instance type and the storage model, decide which deployment path you follow. Work through the topics in this chapter in order, and record your values in the [deployment prerequisite checklist](evs-deployment-prereq-checklist.md).

The procedures in [Deploy in Self-deployed mode](getting-started-self-deployed.md) deploy VCF 9.x. Pages in [Deploy in EVS-deployed mode](evs-deployed-overview.md) cover VCF 5.2.x. A page with no line and outside those sections covers both.

## Decisions to make before you deploy
<a name="plan-overview-decisions"></a>

The following table lists the decisions to make and the topic for each one.


| Decision | What you decide | Topic | 
| --- | --- | --- | 
| Versions and hosts | The VMware Cloud Foundation (VCF) version and deployment mode, the instance type, the number of hosts, and how you reserve capacity for them. |  [Choose versions, hosts, and size](plan-hosts.md)  | 
| Storage | Whether your principal storage is vSAN ESA on local NVMe or external storage for diskless hosts, which need VCF 9.x, and what supplemental storage you add. |  [Choose storage](plan-storage.md)  | 
| Network | The VPC CIDR block, the VLAN subnet sizes, the connections to your other networks, the NSX Edge design, and HCX connectivity. |  [Plan your network](plan-network.md)  | 
| Costs and licenses | Which charges apply, how to lower the cost of hosts, and how you bring your VCF subscription. |  [Plan costs and licenses](plan-cost.md)  | 
| Security, support, and recovery | Who manages each part of the environment, which account guardrails apply, and how you recover from a failure. |  [Plan security, support, and recovery](plan-security-support.md)  | 

When you have made these decisions, see [Deploy](deploy-overview.md) to choose a deployment path. To deploy VCF 9.x with the EVS Deployment Orchestrator (EDO), a tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs), see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md).

**Topics**
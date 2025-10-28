# Automated SAP installation architecture

The example architecture shown in the diagram below uses a centralized AWS account that stores the AWS Systems Manager document (SSM document). The document is shared with AWS accounts that host Amazon EC2 instances running SAP HANA workloads.

![The Systems Manager automation document connects to three child accounts.](images/automation-installation-architecture.png)
You can use multiple AWS accounts and AWS organizations to arrange the accounts into a hierarchy and group them into organizational units. These organizational units can be used for things such as consolidated billing, workload isolation, and administrative isolation. You can create separate AWS accounts for development, testing, staging, and production on a per-application basis as part of an organization. For more information, see the [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
_AWS Organizations">User Guide_.

Systems Manager automation provides multi-account and multi-AWS Region support that allows you to execute your own automation documents across multiple accounts from a central AWS account. You can centralize the SSM documents into a Shared Services account or use an automation account. The automation account can be the AWS account that runs SAP workloads or a dedicated account that only runs SSM documents. Using a centralized AWS for automation reduces administration overhead by maintaining the SSM document and its dependencies in a single account. For more information about Shared Services, see [Infrastructure OU - Shared Services account](../../../prescriptive-guidance/latest/security-reference-architecture/shared-services.md "../../../prescriptive-guidance/latest/security-reference-architecture/shared-services.md") in the _AWS Security Reference Architecture_.

In order for Systems Manager to trigger automation documents from a centralized AWS account to the connected accounts, IAM permissions are required in the automation and child accounts. For more information, see [Running automations in multiple AWS Regions and accounts](../../../systems-manager/latest/userguide/running-automations-multiple-accounts-regions.md "../../../systems-manager/latest/userguide/running-automations-multiple-accounts-regions.md") in the _AWS Systems Manager User Guide_.

You can share SSM documents privately or publicly with accounts in the same Region. To privately share a document, modify the document permissions and allow specific individuals to access it based on their AWS account ID. For more information, see [Sharing SSM documents](../../../systems-manager/latest/userguide/ssm-sharing.md "../../../systems-manager/latest/userguide/ssm-sharing.md") in the _AWS Systems Manager User Guide_.

## Components

The installation automation workflow includes automation runbooks and SSM command documents.

**Automation runbook**

An automation runbook defines the actions that Systems Manager performs on your managed instances and other AWS resources. A runbook contains one or more steps that run in sequential order. For more information, see the following documentation:

- [What is an automation?](../../../systems-manager/latest/userguide/systems-manager-automation.md#what-is-an-automation "../../../systems-manager/latest/userguide/systems-manager-automation.md#what-is-an-automation") in the _AWS Systems Manager User Guide_
- [Systems Manager Automation runbook reference](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md")

**SSM command document**

If a task must be repeated multiple times on multiple hosts, you can create it as an SSM command document. These documents are usable across multiple runbooks. For more information, see [Systems Manager Command document plugin reference](../../../systems-manager/latest/userguide/ssm-plugins.md "../../../systems-manager/latest/userguide/ssm-plugins.md") in the _AWS Systems Manager User Guide_.

You can make the SSM command document as granular as you need, based on factors such as:

- Segregation of duties
- Types of SAP systems that are being deployed
- Complexity of SAP systems that are being deployed
- Security

**Workflow**

As an example, each runbook can be made up of several SSM documents that perform a specific configuration. The following runbooks can be used, which are illustrated in the diagram below.

- Bootstrap Amazon EC2 instances for SAP HANA database
- Bootstrap Amazon EC2 instances for SAP application servers
- Install SAP HANA database
- Install ABAP SAP Central Services (ASCS)
- Install a database instance
- Install a primary application server
- Install an additional application server

![Detailed flow chart of the SSM document.](images/automation-flow.png)

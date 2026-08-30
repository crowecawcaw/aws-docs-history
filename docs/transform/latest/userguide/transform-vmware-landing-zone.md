# Build landing zone

AWS Transform guides you through designing and deploying an AWS landing zone as part
of your migration project. A landing zone is a multi-account AWS environment that
serves as the foundation for your workloads. It puts organizational boundaries,
governance controls, and account structure in place before any workloads arrive.
AWS Transform analyzes your migration inventory and business requirements. Based on this
analysis, it recommends an Organizational Unit (OU) and account structure, applies
recommended Service Control Policies (SCPs), and generates and deploys the
infrastructure as code (IaC). What
typically takes weeks of manual planning and configuration, AWS Transform can complete
in a single conversation.

The landing zone agent automates two phases:

- **Foundation setup** – Establish the core
  landing zone structure: AWS Control Tower, foundational OUs, and core
  accounts.
- **Workload account design** – Design and
  create workload OUs and accounts based on your migration waves, business
  units, and environment separation requirements.
  AWS Transform supports both greenfield environments (no existing landing zone) and
  brownfield environments (existing OUs and accounts already deployed). In brownfield
  scenarios, AWS Transform detects your existing organization structure and recommends only
  the changes needed to fill gaps against AWS best practices. You don't have to
  start from scratch or perform a manual gap analysis.

## Connector setup

Before the agent can provision resources, you connect it to your organization
management account. The landing zone agent requires a target AWS account
connector with permissions to:

- Set up [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")
- Create [organizational units and accounts](../../../organizations/latest/userguide/orgs_manage_ous.md "../../../organizations/latest/userguide/orgs_manage_ous.md")
- Configure [Service Control Policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md")

When you approve the connector request, you grant AWS Transform permissions to:

- Provision and manage landing zone infrastructure in the target
  AWS account and Region. This includes permissions for the following
  items, restricted to resources tagged with
  `CreatedBy:AWSTransform` and by
  `ATWorkspace:{workspace-id}` where applicable:

  - S3 bucket operations (create, read, write, delete) for buckets
    starting with `transform-vmware-landing-zone-`
  - CloudFormation stack deployments and change set management for landing
    zone stacks
  - AWS Control Tower operations (managing landing zones,
    enabling baselines and controls)
  - [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") management (creating and managing
    organizational units, creating accounts, and moving
    accounts)
  - Service control policy (SCP) management through AWS Control
    Tower
  - [AWS Service Catalog](../../../servicecatalog/latest/adminguide/introduction.md "../../../servicecatalog/latest/adminguide/introduction.md") provisioning artifact management

When you create the connector, you specify a target AWS Region. This Region
should be the same as your home Control Tower Region. For more information about
Control Tower Regions, see [How AWS Regions
work with AWS Control Tower](../../../controltower/latest/userguide/region-how.md "../../../controltower/latest/userguide/region-how.md").

At the start of the landing zone setup, AWS Transform retrieves your connector
configuration and presents the AWS Organization management account ID and
target Region for confirmation. For more information, see
[AWS Transform Connectors](transform-user-connectors.md "transform-user-connectors.md").

###### Important

**IAM Identity Center Region dependency** –
AWS Transform requires AWS IAM Identity Center. Your connector Region must
match both your AWS Control Tower home Region _and_
your IAM Identity Center Region. If IAM Identity Center is already
configured in your organization and the connector targets a different
Region, AWS Control Tower initialization fails. For more information, see [Considerations for IAM Identity Center customers](../../../controltower/latest/userguide/getting-started-prereqs.md "../../../controltower/latest/userguide/getting-started-prereqs.md") in the AWS
Control Tower User Guide.

## Foundation setup

The foundation setup phase establishes the core landing zone infrastructure
using [AWS Control
Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md"). When AWS Control Tower sets up a landing zone, it
automatically provisions a set of managed resources in your management account
that form the governance foundation for your entire AWS Organization:

- **Root** – The top-level parent that
  contains all OUs in your landing zone.
- **Security OU** – Created automatically
  by Control Tower. It contains two shared accounts:

  - **Log Archive account** –
    Centralized, immutable logging for all AWS API activity and
    resource changes across your organization.
  - **Audit account** – Read-only
    access to all accounts for security and compliance
    review.
    These accounts cannot be renamed or replaced after initial
    setup.

- **Mandatory controls (guardrails)** –
  Control Tower automatically applies preventive and detective controls
  across your organization to enforce baseline governance policies. These
  cannot be disabled.
- **IAM Identity Center directory** –
  Control Tower creates a cloud-native directory with preconfigured groups
  and single sign-on access for your landing zone users. For more
  information, see [AWS IAM Identity
  Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md").

Control Tower uses [CloudFormation
StackSets](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") to deploy and manage these resources consistently across
all accounts and Regions in your organization. Don't modify or delete
Control Tower managed resources outside of supported methods. Doing so can
cause your landing zone to enter an unknown state.

### Account email convention

AWS requires a unique email address for each account. These emails
receive important notifications for the account. AWS Transform uses plus
addressing to generate unique account emails from a single mailbox.

Format: `prefix+account-name@domain`

You provide a prefix (for example, `aws-admin`) and a domain
(for example, `acme.com`), and AWS Transform derives all account
emails automatically. For example:

- Audit account: `aws-admin+audit@acme.com`
- Log Archive account:
  `aws-admin+log-archive@acme.com`
- Sandbox account:
  `aws-admin+sandbox@acme.com`

In brownfield scenarios, AWS Transform inspects existing account emails to
infer the plus-addressing convention already in use and offers to continue
with the same pattern.

### Recommended foundation structure

Based on AWS best practices, AWS Transform recommends the following
foundation OU structure. You can customize it before creation.

| OU             | Purpose                                                                                                                                                                                                     | Accounts             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Security       | Centralized audit logging and monitoring. Isolating these<br>services in dedicated accounts is designed to help keep your<br>audit trail separate from workload teams.                                      | Audit, Log Archive   |
| Infrastructure | Shared networking (Transit Gateway, VPN), DNS, and common<br>services. Centralizing these is recommended to help reduce<br>duplication and give your network team a single place to<br>manage connectivity. | None (created empty) |
| Sandbox        | Developer experimentation with spending limits and<br>restricted access. Recommended to give developers a space to<br>experiment without risking production resources.                                      | Sandbox              |
| Workloads      | Contains Production, Non-Production, and optionally<br>Regulated sub-OUs. Workload accounts are designed in the<br>next phase based on your migration requirements.                                         | None (created empty) |

###### Note

The Security OU with [Audit and Log
Archive accounts](../../../controltower/latest/userguide/accounts.md "../../../controltower/latest/userguide/accounts.md") is created as part of the Control Tower
foundation setup. The Infrastructure, Sandbox, and Workloads OUs are
created separately after you confirm the structure.

In brownfield scenarios, AWS Transform compares your existing foundation
against this recommended structure and reports only the gaps. For example:
"Your foundation has Security and Infrastructure OUs but no Sandbox
OU."

### Service Control Policies (SCPs)

SCPs are [organization-level permission guardrails](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") that set the maximum
permissions for all accounts in your AWS Organization. They don't grant
access — instead, they define boundaries that no one in the account can
exceed, even account administrators.

As part of the Control Tower deployment, baseline guardrails are applied
automatically. AWS Transform also recommends additional SCPs designed to help
strengthen your organization's posture. These are based on AWS best
practices for a minimum viable landing zone.

SCPs can be applied to the Infrastructure, Sandbox, and Workloads OUs. The
Security OU is managed by Control Tower and cannot be targeted by SCPs
through this tool.

###### Important

The Security OU is a foundation OU managed by Control Tower. You
cannot add accounts, SCPs, or any resources to it through the landing
zone agent.

In brownfield scenarios, AWS Transform checks which SCPs are already applied
and only recommends ones that would fill gaps.

### Foundation deployment

After the foundation design is complete, you choose how to deploy:

- **Deploy for me** – AWS Transform deploys
  the foundation OUs, accounts, and SCPs to your AWS
  Organization.
- **I'll deploy on my own** – AWS Transform
  generates Infrastructure as Code (IaC) artifacts for download in
  your preferred format (see [IaC formats](#transform-vmware-lz-iac-formats "#transform-vmware-lz-iac-formats")).
- **Design workload accounts first** –
  Skip deployment and continue to the workload account design phase.
  You can deploy everything together later.

#### Control Tower initialization

If AWS Transform detects that AWS Control Tower is not yet initialized in your
organization, it provides the user with a link to the AWS Transform console page.
Generating the operation in the link creates a CloudFormation stack to bootstrap
Control Tower in the CloudFormation console for your target Region. After the stack
is created, AWS Transform continues with the deployment.

## Workload account design

In the workload account design phase, AWS Transform designs the OU and account
structure for your application workloads based on your migration inventory,
business requirements, and environment separation preferences.

### Migration planning context

AWS Transform retrieves data from your migration planning phase, including
wave plans, server-to-application mappings, and shared context. If migration
planning data is available, AWS Transform displays a summary and asks you to
confirm or adjust it. If no migration planning data is available, AWS Transform
asks discovery questions directly.

### Discovery

AWS Transform asks questions to understand your workload requirements. You can
skip any question. Topics include:

- Number of business units or teams using AWS
- Industry and any applicable frameworks (HIPAA, PCI-DSS, SOC2,
  FedRAMP)
- Whether workloads handle sensitive data (PII, PHI,
  financial)
- Environment separation preferences (dev/test/staging/prod as
  separate accounts or shared)
- Workload isolation requirements
- Business applications and their purposes
- Server grouping into applications
- Cost tracking and allocation needs (by business unit, project,
  environment)
- Expected growth in the next 12–24 months
- Account strategy preference (single app per account, grouped, or
  environment-based)

### Proposed workload structure

Based on your answers and migration planning data, AWS Transform proposes an
OU and account structure under the Workloads OU. The proposal includes the
reasoning behind each design decision.

AWS Transform follows these design principles:

- All servers in a migration wave go to the same account — waves
  cannot be split across accounts. This is a rehost limitation during
  wave execution.
- If you request isolated environments, AWS Transform creates
  Workloads/Production and Workloads/Non-Production sub-OUs.
- If applicable frameworks are identified, AWS Transform creates
  Workloads/Regulated and Workloads/Standard sub-OUs.
- If multiple business units require different governance, AWS Transform
  creates business-unit-specific OUs under Workloads.
- Critical or sensitive-data applications get a single app per
  account. In this case, you might be asked to iterate on your wave
  plan.
- Tightly coupled applications with shared dependencies are grouped
  in one account.

Each proposed account includes: name, purpose, target OU, and business
unit. AWS Transform shows the naming convention being used (for example,
`<business-unit>-<environment>-<workload>`).

You can review and modify the proposed structure before AWS Transform applies
the changes. After applying, you can iterate — making additional changes
until you are satisfied.

### Workload SCP configuration

After the workload structure is created, AWS Transform presents available SCPs
and asks if you want to apply any to your workload OUs. You select which
SCPs to apply and to which OUs. AWS Transform applies the SCPs and shows the
updated organization tree with an SCP summary table.

### Workload deployment

After the workload design is complete, you choose how to deploy:

- **Deploy for me** – AWS Transform deploys
  the workload OUs, accounts, and SCPs to your AWS
  Organization.
- **I'll deploy on my own** – AWS Transform
  generates IaC artifacts for download in your preferred format (see
  [IaC formats](#transform-vmware-lz-iac-formats "#transform-vmware-lz-iac-formats")).

## IaC formats

When you choose self-deployment, AWS Transform generates Infrastructure as Code
artifacts in the following formats:

- **[AWS Cloud Development Kit (AWS CDK)](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md")** – TypeScript project for
  programmatic infrastructure deployment.
- **HashiCorp Terraform** – Generates
  HashiCorp Configuration Language (HCL) templates for managing landing
  zone resources.
- **Landing Zone Accelerator (LZA)** –
  Configuration YAML files based on LZA Universal Configuration version
  1.1.0. These enterprise-ready templates work with the Landing Zone
  Accelerator on AWS to establish multi-account AWS environments. The
  generated files include preconfigured settings for governance,
  organization structure, and networking. These settings align with AWS
  best practices. To learn more, see [LZA Universal Configuration](../../../solutions/latest/landing-zone-accelerator-on-aws/universal-configuration.md "../../../solutions/latest/landing-zone-accelerator-on-aws/universal-configuration.md").

###### Note

When you deploy through the Landing Zone Accelerator (LZA) pipeline, your
AWS Transform account and LZA installation must be in the same AWS
Organization. Deployment fails if the Organizations IDs used in AWS Transform
and LZA don't match. To learn how to set up your LZA
installation using Organizations, see [AWS Organizations based installation](../../../solutions/latest/landing-zone-accelerator-on-aws/aws-organizations-based-installation.md "../../../solutions/latest/landing-zone-accelerator-on-aws/aws-organizations-based-installation.md").

After you select a format, AWS Transform generates the artifacts and makes them
available for download.

To verify the downloaded file hasn't been corrupted or tampered with, generate
and download a checksum, then compare it to a locally generated hash
using:

```
openssl dgst -sha256 -binary <file.zip> | base64
```

## Deployment approvals process

Landing zone deployment requests require explicit approval before execution.
When you submit a deployment request, it automatically routes to authorized
approvers through the AWS Transform Approvals tab.

Approvers review CloudFormation templates and landing zone configurations. Only users with the Admin role in AWS Transform can
approve deployment requests. Each submission triggers a new review cycle, and
deployments proceed only after receiving confirmation.

If an approver denies your request, contact them directly to discuss necessary
modifications. The system tracks all approval decisions for audit purposes and
maintains deployment history.

## Tag landing zone resources

AWS Transform automatically tags all generated resources with
`"CreatedBy": "AWSTransform"` along with definition and execution
IDs for tracking purposes.

### Automatic tags

All landing zone resources receive the following tags:

- `CreatedBy` – AWSTransform
- `ATWorkspace` – Workspace identifier

###### Note

If your migration is part of the AWS Migration Acceleration Program
(MAP 2.0), you can include the required MAP tag. The key is
`map-migrated` and the value is `migMPE_ID`,
where MPE\_ID is your MPE identifier. The MAP
tag is requested during the connector setup phase, and AWS Transform
applies these tags during landing zone deployment.

## Reversing changes

Only non-deployed elements can be removed. After an OU or account is deployed,
it cannot be removed through the landing zone agent.

When removing elements, order matters — you must remove children before
parents:

1. Remove accounts first (by email).
2. Remove SCPs from OUs.
3. Remove child OUs — an OU cannot be removed if it still has accounts or
   nested OUs.

## Related resources

- [Connect target AWS accounts and regions](transform-vmware-connect-target-account.md "transform-vmware-connect-target-account.md")
- [Migrate your network to AWS](transform-vmware-migrate-network.md "transform-vmware-migrate-network.md")
- [AWS Control Tower User Guide](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md")
- [AWS Organizations User Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")
- [AWS IAM Identity Center User Guide](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")
- [CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [Landing Zone Accelerator on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/ "https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/")
- [AWS Well-Architected Framework](../../../wellarchitected/latest/framework/welcome.md "../../../wellarchitected/latest/framework/welcome.md")
- [AWS Prescriptive Guidance: Building Landing Zones](../../../prescriptive-guidance/latest/migration-landing-zone/welcome.md "../../../prescriptive-guidance/latest/migration-landing-zone/welcome.md")

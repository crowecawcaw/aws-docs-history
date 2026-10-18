

# Build landing zone
<a name="transform-vmware-landing-zone"></a>

AWS Transform guides you through designing and deploying an AWS landing zone as part of your migration project. A landing zone is a multi-account AWS environment that serves as the foundation for your workloads. It puts organizational boundaries, governance controls, and account structure in place before any workloads arrive. AWS Transform analyzes your migration inventory and business requirements. Based on this analysis, it recommends an Organizational Unit (OU) and account structure, applies recommended Service Control Policies (SCPs), and generates and deploys the infrastructure as code (IaC). What typically takes weeks of manual planning and configuration, AWS Transform can complete in a single conversation.

The landing zone agent automates two phases:
+ **Foundation setup** – Establish the core landing zone structure: [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html), foundational OUs, and core accounts.
+ **Workload account design** – Design and create workload OUs and accounts based on your migration waves, business units, and environment separation requirements.

AWS Transform supports both greenfield environments (no existing landing zone) and brownfield environments (existing OUs and accounts already deployed). In brownfield scenarios, AWS Transform detects your existing organization structure and recommends only the changes needed to fill gaps against AWS best practices. You don't have to start from scratch or perform a manual gap analysis.

AWS Transform supports two operational modes based on your connector configuration and preferences:
+ **Full deployment mode** – AWS Transform analyzes your organization, generates recommendations, creates Infrastructure as Code (IaC) artifacts, and deploys the landing zone infrastructure directly to your AWS Organization.
+ **IaC-only mode** – AWS Transform analyzes your organization, generates recommendations, and produces IaC artifacts for your review and deployment through your own pipeline. The agent does not deploy infrastructure directly. This mode is useful if you have existing deployment pipelines (such as AWS Landing Zone Accelerator, Terraform, or custom CI/CD) or prefer to manage landing zone changes through your internal change management process. For more information, see [Generate landing zone IaC without deployment](transform-vmware-lz-iac-only-flow.md).

## Connector setup
<a name="transform-vmware-lz-connector-setup"></a>

Before the agent can proceed, you connect it to your organization's Management Account or Delegated Administrator account. The connector type determines your operational mode, available capabilities, and the permissions you grant to AWS Transform:


| Connector Type | Capabilities and Workflow | 
| --- | --- | 
| Management Account | Provides full deployment capabilities. AWS Transform analyzes your organization, generates recommendations, creates Infrastructure as Code artifacts, and deploys landing zone infrastructure directly to your AWS Organization. You choose whether AWS Transform deploys automatically or only generates IaC artifacts for your review.<br />Use this option when you want AWS Transform to provision landing zone infrastructure directly, or when you want to generate IaC artifacts while retaining the option for direct deployment.<br />**Permissions** – When you approve the connector request, you grant AWS Transform permissions to provision and manage landing zone infrastructure in the target AWS account and Region. Where applicable, permissions are restricted to resources tagged with `CreatedBy:AWSTransform` and `ATWorkspace:{workspace-id}`. This includes:+  [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) operations (setting up and managing landing zones, enabling baselines and controls) <br />+  [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) management (creating and managing organizational units, creating accounts, and moving accounts) <br />+  [Service Control Policy (SCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) management through AWS Control Tower <br />+  CloudFormation stack deployments and change set management for landing zone stacks <br />+  [AWS Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) provisioning artifact management <br />+  S3 bucket operations (create, read, write, delete) for buckets starting with `transform-vmware-landing-zone-`  | 
| Delegated Administrator (DA) Account | [Provides IaC-only mode](transform-vmware-lz-iac-only-flow.md). AWS Transform analyzes your organization, generates recommendations, and produces Infrastructure as Code artifacts that you can download and deploy through your own pipeline. Direct deployment is not available with DA connectors due to AWS Control Tower's technical limitation that Delegated Admin accounts cannot provision AWS Control Tower landing zones.<br />Use this option when:+  Your security or governance policies restrict programmatic access to the Management Account <br />+  You have an established Delegated Administrator account for AWS Organizations operations <br />+  You prefer to deploy landing zone infrastructure through your own deployment pipeline (AWS Landing Zone Accelerator, Terraform, CloudFormation, CDK, or custom CI/CD) <br />If you require direct deployment capability, you can reconfigure your connector to target the Management Account.<br />**Permissions** – In IaC-only mode, permissions are limited to read and describe operations on the AWS Organization to support analysis and gap assessment.<br />To create a Delegated Administrator account, [follow the instructions to create a delegated administrator](transform-vmware-connect-target-account.md#transform-vmware-cta-delegated-admin). | 

When you create the connector, you specify a target AWS Region. This is the Region where Control Tower is enabled, and it serves as your Control Tower home Region. For more information about Control Tower Regions, see [How AWS Regions work with AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/region-how.html).

At the start of the landing zone setup, AWS Transform retrieves your connector configuration and presents the AWS Organization management account ID and target Region for confirmation. AWS Transform also detects your connector type and operational mode, informing you whether you are proceeding with full deployment or IaC-only capabilities. For more information, see [AWS Transform Connectors](transform-user-connectors.md).

**Important**  
**IAM Identity Center Region dependency** – AWS Transform requires AWS IAM Identity Center. Your connector Region must match both your AWS Control Tower home Region *and* your IAM Identity Center Region. If IAM Identity Center is already configured in your organization and the connector targets a different Region, AWS Control Tower initialization fails. For more information, see [Considerations for IAM Identity Center customers](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-prereqs.html) in the AWS Control Tower User Guide.

**Note**  
**Delegated Admin connectors and Control Tower initialization:** If you use a Delegated Administrator account connector, AWS Transform operates in IaC-only mode. If Control Tower has not yet been initialized in your organization, AWS Transform generates IaC artifacts to initialize Control Tower, which you can review and deploy through your pipeline.

## Foundation setup
<a name="transform-vmware-lz-foundation-setup"></a>

### Foundation discovery and planning
<a name="transform-vmware-lz-foundation-discovery"></a>

At the start of foundation setup, AWS Transform performs discovery to understand your current organizational state and determines the best approach for your landing zone. The agent asks you the following key questions:
+ **Does your organization already have AWS Control Tower deployed?** AWS Transform checks if Control Tower is initialized in your organization. If Control Tower is already running, AWS Transform analyzes the existing landing zone configuration.
+ **What foundation approach do you want to use?** If Control Tower is not yet deployed, AWS Transform offers you two options:
  + **Control Tower-based landing zone:** AWS Transform deploys AWS Control Tower as the foundation for your landing zone. This provides the most comprehensive governance with managed controls, mandatory guardrails, and automated OU and account management. This is the recommended approach for most organizations.
  + **Organizations-only landing zone:** AWS Transform creates a landing zone using only AWS Organizations without deploying Control Tower. This gives you foundational OU structure and account organization but does not include Control Tower's managed controls and automated guardrails. Choose this option if your organization has specific requirements that prevent Control Tower deployment.

Based on your responses, AWS Transform tailors the foundation setup workflow and recommendations to match your chosen approach. For Control Tower-based landing zones, the full governance foundation is deployed. For Organizations-only landing zones, AWS Transform focuses on OU structure, account organization, and manual SCP configuration.

### Foundation setup
<a name="transform-vmware-lz-foundation-structure"></a>

The foundation setup phase establishes the core landing zone infrastructure using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html). The landing zone agent builds the full foundation OU structure. Part of it is the AWS Control Tower baseline, which Control Tower provisions automatically in your management account. AWS Transform adds the rest based on AWS best practices. You can customize the structure before creation.

The following table shows the foundation structure and where each component comes from:


| Component | Type | Source | Purpose | 
| --- | --- | --- | --- | 
| Root | Root | AWS Control Tower baseline | The top-level parent that contains all OUs in your landing zone. | 
| Security | OU | AWS Control Tower baseline | Centralized audit logging and monitoring. Isolating these services in dedicated accounts is designed to help keep your audit trail separate from workload teams. | 
|   Audit | Account | AWS Control Tower baseline | Read-only access to all accounts for security and compliance review. | 
|   Log Archive | Account | AWS Control Tower baseline | Centralized, immutable logging for all AWS API activity and resource changes across your organization. | 
| Infrastructure | OU | AWS best practice addition | Parent OU for shared infrastructure that supports your entire organization. | 
|   Network | OU | AWS best practice addition | Shared networking infrastructure, including Transit Gateway, VPN, and DNS. Centralizing these services helps reduce duplication and gives your network team a single place to manage connectivity across all accounts. | 
|   Shared Services | OU | AWS best practice addition | Common services used across the organization, such as identity, logging, and monitoring solutions that support multiple workload accounts. | 
| Sandbox | OU | AWS best practice addition | Developer experimentation with spending limits and restricted access, without risking production resources. | 
|   Sandbox | Account | AWS best practice addition | The account developers use for experimentation. | 
| Workloads | OU | AWS best practice addition | Parent OU for your application workloads. It's created empty. Workload OUs and accounts, such as Production, Non-Production, and optionally Regulated, are designed in the next phase based on your migration requirements. For more information, see [Workload account design](#transform-vmware-lz-workload-design). | 

In addition to the Security OU and its accounts, the AWS Control Tower baseline includes the following governance resources:
+ **Mandatory controls (guardrails)** – Preventive and detective controls applied across your organization to enforce baseline governance policies. These cannot be disabled.
+ **IAM Identity Center directory** – A cloud-native directory with preconfigured groups and single sign-on access for your landing zone users. For more information, see [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

**Note**  
The Security OU with the [Audit and Log Archive accounts](https://docs.aws.amazon.com/controltower/latest/userguide/accounts.html) is created as part of the AWS Control Tower setup. These accounts cannot be renamed or replaced after initial setup. AWS Transform creates the best practice additions separately after you confirm the structure.

Control Tower uses [CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to deploy and manage its baseline resources consistently across all accounts and Regions in your organization. Don't modify or delete Control Tower managed resources outside of supported methods. Doing so can cause your landing zone to enter an unknown state.

In brownfield scenarios, AWS Transform compares your existing foundation against this structure and reports only the gaps. For example: "Your foundation has Security and Infrastructure OUs but no Sandbox OU."

### Account email convention
<a name="transform-vmware-lz-email-convention"></a>

AWS requires a unique email address for each account. These emails receive important notifications for the account. AWS Transform uses plus addressing to generate unique account emails from a single mailbox.

Format: `prefix+account-name@domain`

You provide a prefix (for example, `aws-admin`) and a domain (for example, `acme.com`), and AWS Transform derives all account emails automatically. For example:
+ Audit account: `aws-admin+audit@acme.com`
+ Log Archive account: `aws-admin+log-archive@acme.com`
+ Sandbox account: `aws-admin+sandbox@acme.com`

In brownfield scenarios, AWS Transform inspects existing account emails to infer the plus-addressing convention already in use and offers to continue with the same pattern.

### Service Control Policies (SCPs)
<a name="transform-vmware-lz-scps"></a>

SCPs are [organization-level permission guardrails](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) that set the maximum permissions for all accounts in your AWS Organization. They don't grant access — instead, they define boundaries that no one in the account can exceed, even account administrators.

As part of the Control Tower deployment, baseline guardrails are applied automatically. AWS Transform also recommends additional SCPs designed to help strengthen your organization's posture. These are based on AWS best practices for a minimum viable landing zone.

SCPs can be applied to the Infrastructure, Sandbox, and Workloads OUs. The Security OU is managed by Control Tower and cannot be targeted by SCPs through this tool.

**Important**  
The Security OU is a foundation OU managed by Control Tower. You cannot add accounts, SCPs, or any resources to it through the landing zone agent.

In brownfield scenarios, AWS Transform checks which SCPs are already applied and only recommends ones that would fill gaps.

**Note**  
**Delegated Administrator account limitation in brownfield scenarios:** When using a Delegated Administrator account connector in a brownfield environment where AWS Control Tower landing zone is already implemented, AWS Transform cannot view or modify existing SCPs managed by Control Tower. This is because Delegated Administrator accounts have limited permissions for SCP operations on Control Tower-managed policies. You can still generate IaC artifacts for new SCPs that you want to apply outside of Control Tower's management scope, but existing Control Tower SCPs will remain unchanged. If you need to modify Control Tower-managed SCPs, reconfigure your connector to target the Management Account.

### Foundation deployment
<a name="transform-vmware-lz-foundation-deployment"></a>

After the foundation design is complete, you choose how to deploy:
+ **Deploy for me** – AWS Transform deploys the foundation OUs, accounts, and SCPs to your AWS Organization.
+ **I'll deploy on my own** – AWS Transform generates Infrastructure as Code (IaC) artifacts for download in your preferred format (see [IaC formats](#transform-vmware-lz-iac-formats)).
+ **Design workload accounts first** – Skip deployment and continue to the workload account design phase. You can deploy everything together later.

#### Control Tower initialization
<a name="transform-vmware-lz-ct-init"></a>

If AWS Transform detects that AWS Control Tower is not yet initialized in your organization, it provides the user with a link to the AWS Transform console page. Generating the operation in the link creates a CloudFormation stack to bootstrap Control Tower in the CloudFormation console for your target Region. After the stack is created, AWS Transform continues with the deployment.

## Workload account design
<a name="transform-vmware-lz-workload-design"></a>

In the workload account design phase, AWS Transform designs the OU and account structure for your application workloads based on your migration inventory, business requirements, and environment separation preferences.

### Migration planning context
<a name="transform-vmware-lz-migration-context"></a>

AWS Transform retrieves data from your migration planning phase, including wave plans, server-to-application mappings, and shared context. If migration planning data is available, AWS Transform displays a summary and asks you to confirm or adjust it. If no migration planning data is available, AWS Transform asks discovery questions directly.

### Discovery
<a name="transform-vmware-lz-discovery"></a>

AWS Transform asks questions to understand your workload requirements. You can skip any question. Topics include:
+ Number of business units or teams using AWS
+ Industry and any applicable frameworks (HIPAA, PCI-DSS, SOC2, FedRAMP)
+ Whether workloads handle sensitive data (PII, PHI, financial)
+ Environment separation preferences (dev/test/staging/prod as separate accounts or shared)
+ Workload isolation requirements
+ Business applications and their purposes
+ Server grouping into applications
+ Cost tracking and allocation needs (by business unit, project, environment)
+ Expected growth in the next 12–24 months
+ Account strategy preference (single app per account, grouped, or environment-based)

### Proposed workload structure
<a name="transform-vmware-lz-proposed-structure"></a>

Based on your answers and migration planning data, AWS Transform proposes an OU and account structure under the Workloads OU. The proposal includes the reasoning behind each design decision.

AWS Transform follows these design principles:
+ All servers in a migration wave go to the same account — waves cannot be split across accounts. This is a rehost limitation during wave execution.
+ If you request isolated environments, AWS Transform creates Workloads/Production and Workloads/Non-Production sub-OUs.
+ If applicable frameworks are identified, AWS Transform creates Workloads/Regulated and Workloads/Standard sub-OUs.
+ If multiple business units require different governance, AWS Transform creates business-unit-specific OUs under Workloads.
+ Critical or sensitive-data applications get a single app per account. In this case, you might be asked to iterate on your wave plan.
+ Tightly coupled applications with shared dependencies are grouped in one account.

Each proposed account includes: name, purpose, target OU, and business unit. AWS Transform shows the naming convention being used (for example, `<business-unit>-<environment>-<workload>`).

You can review and modify the proposed structure before AWS Transform applies the changes. After applying, you can iterate — making additional changes until you are satisfied.

### Workload SCP configuration
<a name="transform-vmware-lz-workload-scps"></a>

After the workload structure is created, AWS Transform presents available SCPs and asks if you want to apply any to your workload OUs. You select which SCPs to apply and to which OUs. AWS Transform applies the SCPs and shows the updated organization tree with an SCP summary table.

### Workload deployment
<a name="transform-vmware-lz-workload-deployment"></a>

After the workload design is complete, you choose how to deploy:
+ **Deploy for me** – AWS Transform deploys the workload OUs, accounts, and SCPs to your AWS Organization.
+ **I'll deploy on my own** – AWS Transform generates IaC artifacts for download in your preferred format (see [IaC formats](#transform-vmware-lz-iac-formats)).

## IaC formats
<a name="transform-vmware-lz-iac-formats"></a>

When you choose self-deployment, AWS Transform generates Infrastructure as Code artifacts in the following formats:
+ **[AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html)** – TypeScript project for programmatic infrastructure deployment.
+ **HashiCorp Terraform** – Generates HashiCorp Configuration Language (HCL) templates for managing landing zone resources.
+ **Landing Zone Accelerator (LZA)** – Configuration YAML files based on LZA Universal Configuration version 1.1.0. These enterprise-ready templates work with the Landing Zone Accelerator on AWS to establish multi-account AWS environments. The generated files include preconfigured settings for governance, organization structure, and networking. These settings align with AWS best practices. To learn more, see [LZA Universal Configuration](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/universal-configuration.html).

**Note**  
When you deploy through the Landing Zone Accelerator (LZA) pipeline, your AWS Transform account and LZA installation must be in the same AWS Organization. Deployment fails if the Organizations IDs used in AWS Transform and LZA don't match. To learn how to set up your LZA installation using Organizations, see [AWS Organizations based installation](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/aws-organizations-based-installation.html).

After you select a format, AWS Transform generates the artifacts and makes them available for download.

To verify the downloaded file hasn't been corrupted or tampered with, generate and download a checksum, then compare it to a locally generated hash using:

```
openssl dgst -sha256 -binary <file.zip> | base64
```

## Deployment approvals process
<a name="transform-vmware-lz-approvals"></a>

Landing zone deployment requests require explicit approval before execution. When you submit a deployment request, it automatically routes to authorized approvers through the AWS Transform Approvals tab.

Approvers review CloudFormation templates and landing zone configurations. Only users with the Admin role in AWS Transform can approve deployment requests. Each submission triggers a new review cycle, and deployments proceed only after receiving confirmation.

If an approver denies your request, contact them directly to discuss necessary modifications. The system tracks all approval decisions for audit purposes and maintains deployment history.

## Tag landing zone resources
<a name="transform-vmware-lz-tagging"></a>

AWS Transform automatically tags all generated resources with `"CreatedBy": "AWSTransform"` along with definition and execution IDs for tracking purposes.

### Automatic tags
<a name="transform-vmware-lz-auto-tags"></a>

All landing zone resources receive the following tags:
+ `CreatedBy` – AWSTransform
+ `ATWorkspace` – Workspace identifier

**Note**  
If your migration is part of the AWS Migration Acceleration Program (MAP 2.0), you can include the required MAP tag. The key is `map-migrated` and the value is `migMPE_ID`, where MPE\_ID is your MPE identifier. The MAP tag is requested during the connector setup phase, and AWS Transform applies these tags during landing zone deployment.

## Reversing changes
<a name="transform-vmware-lz-reversing"></a>

Only non-deployed elements can be removed. After an OU or account is deployed, it cannot be removed through the landing zone agent.

When removing elements, order matters — you must remove children before parents:

1. Remove accounts first (by email).

1. Remove SCPs from OUs.

1. Remove child OUs — an OU cannot be removed if it still has accounts or nested OUs.

## Related resources
<a name="transform-vmware-lz-related"></a>
+ [Connect target AWS accounts and regions](transform-vmware-connect-target-account.md)
+ [Migrate network](transform-vmware-migrate-network.md)
+ [AWS Control Tower User Guide](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
+ [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
+ [AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+ [Landing Zone Accelerator on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/)
+ [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
+ [AWS Prescriptive Guidance: Building Landing Zones](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-landing-zone/welcome.html)
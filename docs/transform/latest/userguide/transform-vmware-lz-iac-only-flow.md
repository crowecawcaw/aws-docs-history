

# Generate landing zone IaC without deployment
<a name="transform-vmware-lz-iac-only-flow"></a>

The IaC-only flow enables you to use AWS Transform landing zone agent for analysis, recommendations, and Infrastructure as Code generation without direct deployment. This mode is available in two scenarios:
+ **Delegated Administrator connector:** When you connect via a Delegated Administrator account, AWS Transform operates exclusively in IaC-only mode. This allows organizations with strict governance policies to use AWS Transform without granting access to the management account.
+ **Management Account with IaC-only preference:** Even with a Management Account connector, you can choose IaC-only mode at the start of your job if you prefer to deploy through your own pipeline (AWS Landing Zone Accelerator, Terraform, CloudFormation, CDK, or custom CI/CD).

## IaC-only workflow overview
<a name="transform-vmware-lz-iac-only-workflow"></a>

In IaC-only mode, AWS Transform performs the same analysis and generates the same recommendations as full deployment mode, but outputs Infrastructure as Code artifacts instead of provisioning resources directly. The workflow includes:
+ **Organization analysis:** AWS Transform discovers your existing organizational structure, identifies gaps against AWS best practices, and recommends landing zone configuration.
+ **Foundation design:** AWS Transform proposes organizational unit (OU) hierarchy, account structure, and Service Control Policies (SCPs) based on your requirements.
+ **Workload account design:** AWS Transform designs workload OUs and accounts based on your migration waves and business requirements.
+ **IaC generation:** AWS Transform generates Infrastructure as Code artifacts in your preferred format. You download these artifacts and deploy them through your own pipeline.

## Permissions in IaC-only mode
<a name="transform-vmware-lz-iac-only-permissions"></a>

IaC-only mode requires minimal permissions compared to full deployment mode:
+ **Read and describe permissions:** AWS Transform requires read-only access to your AWS Organization to discover existing structure, accounts, organizational units, and policies.
+ **No write permissions needed:** Since AWS Transform does not provision resources, no write or create permissions are required for landing zone services like AWS Control Tower, Organizations, CloudFormation, or Service Catalog.
+ **Delegated Administrator accounts:** When using a Delegated Administrator connector, these read-only permissions are sufficient for the agent to perform analysis and generate IaC artifacts, even though Delegated Administrators cannot deploy Control Tower landing zones directly.

## Limitations in IaC-only mode
<a name="transform-vmware-lz-iac-only-limitations"></a>

Be aware of the following limitations when using IaC-only mode:
+ **No direct deployment:** AWS Transform does not provision landing zone infrastructure. You must deploy the generated IaC artifacts through your own pipeline.
+ **Delegated Administrator and Control Tower:** When using a Delegated Administrator connector in a brownfield environment where AWS Control Tower is already deployed, AWS Transform cannot view or modify existing Control Tower-managed SCPs. Existing SCPs remain unchanged. You can still generate IaC for new SCPs outside Control Tower's scope. To modify Control Tower-managed SCPs, reconfigure your connector to target the Management Account.
+ **No deployment step verification:** AWS Transform does not verify successful deployment of generated artifacts. After deploying through your pipeline, you are responsible for validating that landing zone infrastructure is created correctly and that all guardrails are in place.

## Supported IaC formats
<a name="transform-vmware-lz-iac-only-formats"></a>

AWS Transform generates IaC artifacts in multiple formats:
+ **AWS CDK:** TypeScript-based Infrastructure as Code for programmatic infrastructure deployment.
+ **Terraform / HCL:** Terraform modules and HashiCorp Configuration Language (HCL) templates for managing landing zone resources.
+ **Landing Zone Accelerator (LZA):** Configuration YAML files (accounts-config.yaml, organization-config.yaml, etc.) based on LZA Universal Configuration version 1.1.0. These enterprise-ready templates integrate with AWS Landing Zone Accelerator to establish multi-account AWS environments with governance, organization structure, and networking aligned to AWS best practices.

You can specify your preferred format upfront, and AWS Transform generates artifacts in that format without asking again during the workflow.

## When to use IaC-only mode
<a name="transform-vmware-lz-iac-only-use-cases"></a>

Consider using IaC-only mode in these scenarios:
+ **Strict governance policies:** Your organization restricts programmatic access to the management account. Using a Delegated Administrator connector with IaC-only mode bypasses this constraint.
+ **Existing deployment pipelines:** You already manage infrastructure through AWS Landing Zone Accelerator, Terraform, or custom CI/CD pipelines. AWS Transform can generate artifacts that integrate with your existing workflow.
+ **Review and customization:** You want to review and customize generated landing zone configuration before deployment.
+ **Brownfield environments:** You have an existing landing zone and want to generate IaC for recommended changes without immediate deployment.
+ **Change management processes:** Your organization requires all infrastructure changes to go through approved change management and deployment processes.
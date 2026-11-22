

# FND01-BP04 Establish a strategy for experimental and temporary environments

 Teams need safe places to experiment with new ideas without putting production at risk. They also need rigorous controls as changes move closer to customer-facing systems. Environments with progressive controls let teams test early, and only validated changes reach critical workloads. 

 **Desired outcome:** 
+  You provide sandbox environments where individual developers can experiment with new AWS services and architectures without risk to shared environments or production workloads. 
+  Experimental environments have controls tuned for exploration (detective guardrails and cost-control policies rather than broad service restrictions), so teams can try new services and the organization retains visibility and spend limits. 
+  You can create short-lived environments on demand for feature branches, pull requests, or time-limited experiments, and have them cleaned up automatically when the work ends or the environment goes idle. 
+  When scale and risk warrant it, you have a separate environment (including a separate AWS Organization if needed) for testing changes to organization-wide capabilities such as service control policies and landing zone components before those changes reach production. 
+  Load, destructive, and chaos testing happens in dedicated pre-production environments rather than in production, so experiments cannot cause customer-facing disruptions. 

 **Common anti-patterns:** 
+  Performing development in a shared environment where another developer can overwrite code changes instead of providing individual sandbox accounts. 
+  Imposing restrictive security controls on sandbox environments that prevent experimentation with new services and features. 
+  Performing load or destructive failure testing in production, causing disruptions for users. 
+  Testing only in production rather than using ephemeral or dedicated pre-production environments that can catch issues before release. 
+  Leaving short-lived environments running after the feature branch, pull request, or experiment is finished, driving cost and configuration drift. 
+  Testing changes to organization-wide capabilities (such as service control policies or landing zone components) directly in the production organization, risking a disruption that affects every workload team. 

 **Benefits of establishing this best practice:** 
+  Individual sandbox accounts give developers a place to try new AWS services and architectures without disrupting shared environments or risking production. 
+  Per-developer sandboxes and on-demand ephemeral environments support simultaneous work without conflicts between developers. 
+  Short-lived environments created and destroyed from code avoid the standing cost of permanently running pre-production infrastructure. 
+  A dedicated environment for testing service control policies, landing zone upgrades, and other organization-wide changes prevents misconfigurations from reaching the production organization. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 This best practice focuses on the environments teams use for experimentation and short-lived work: sandbox accounts for individual developers, ephemeral environments created on demand for feature branches and pull requests, and, when scale warrants it, a separate environment for testing changes to organization-wide capabilities such as service control policies and landing zone components. The broader design of development, testing, staging, and production environments and the guardrails that apply to them is covered by the [Organizing your AWS environment whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html). This best practice assumes that structure exists and concentrates on the experimental and temporary environments that sit within it. 

 Developers need flexibility to experiment with new services, test architectural hypotheses, and fail safely without impacting users. Shared development, testing, and production environments cannot serve that need, as restrictive controls slow experimentation and loose controls create operational risk. Dedicated sandbox accounts give each developer an isolated space where service controls are minimized, detective guardrails maintain visibility, and cost-control policies prevent unexpected spend. Solutions such as [Innovation Sandbox on AWS](https://docs.aws.amazon.com/solutions/innovation-sandbox-on-aws/) add automated budget alerts and scheduled cleanup on top of standard sandbox accounts. 

 Ephemeral environments provide isolated, production-like space for a specific pull request, feature branch, or time-boxed experiment without the standing cost of a permanent environment. A CI/CD pipeline typically creates them from [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates or Terraform modules when a pull request opens, and deletes them when it merges or closes. Tagging each ephemeral resource with a creation timestamp and an expiration date lets automation find and remove environments that outlive their purpose, and per-team [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) alerts catch runaway spend when cleanup fails. Instance scheduling, for example through [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/), reduces cost further for longer-lived non-production environments that must remain available during business hours. 

 Foundation, networking, and security operations teams that manage organization-wide capabilities need somewhere to test changes to service control policies, AWS Control Tower configurations, or custom landing zone extensions. Applying these changes directly to the production AWS Organization creates unacceptable risk, because a misconfigured SCP can block deployments organization-wide and a failed landing zone upgrade can impair account provisioning for every team. For most organizations, a dedicated non-production OU or account inside the production organization is enough. When you manage hundreds of accounts, change organization-wide policies often, or cannot accept the scope of impact of a mistake, a separate AWS Organization that mirrors production structure but hosts no customer workloads is the stronger pattern. The [Organizing your AWS environment whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/multiple-organizations.html#test-changes-to-your-overall-aws-environment) describes when this is warranted. 

 Match the investment to organizational scale. A startup with a handful of engineers does not need automated ephemeral environments or a second AWS Organization. Per-developer sandboxes and a shared development account are usually enough. Add ephemeral environments when feature teams start blocking each other in shared pre-production environments, and introduce a dedicated foundation-testing environment only when an organization-wide disruption from a misconfigured SCP or landing zone change becomes a credible risk. The pattern stays constant (isolation for experimentation, automated creation and cleanup for temporary work, and a separate space for testing organization-wide changes), and the specific implementation scales with organizational needs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Plan where experimental and temporary environments fit in your environment strategy:** Start from the environment types defined by your broader environment boundaries and identify the gaps this best practice addresses: sandbox environments for individual experimentation, ephemeral environments for feature branches and pull requests, and a dedicated space for testing organization-wide foundation changes. Decide whether each developer needs a dedicated sandbox account or whether sandboxes can be shared within a team, and establish naming conventions and an OU placement for these environment types. Reference the [Organizing your AWS environment whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) for OU patterns that accommodate sandbox and experimentation accounts. 

1.  **Implement sandbox environments with minimized preventative controls:** Create [sandbox organizational units](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/experimental-ous.html) with minimized preventative controls so developers can experiment with new AWS services and architectures. Provide individual sandbox accounts for developers to work in parallel without conflicts or risk of overwriting each other's changes. Apply detective guardrails (AWS Config rules, CloudTrail logging) to maintain visibility and compliance without restricting service usage. Use [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to prevent actions that could incur unexpected costs (such as launching expensive instance types) or create security risks (such as disabling CloudTrail), and allow broad service experimentation otherwise. Consider implementing [Innovation Sandbox on AWS](https://docs.aws.amazon.com/solutions/innovation-sandbox-on-aws/) for additional governance features such as automated budget alerts and scheduled resource cleanup. 

1.  **Apply cost controls to experimental and temporary environments:** Experimental and short-lived environments are the most common source of unnoticed spend because the usual signal ("the environment is still here next quarter") is missing by design. Tag every sandbox and ephemeral resource with environment type, owner, and (for ephemeral resources) a creation timestamp and expiration date so automation can find and remove them. Use [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) to set per-account or per-team spending thresholds and receive alerts when costs exceed expected levels, and monitor idle resources by using [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) and [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) recommendations. For sandbox and non-production environments that must stay available during business hours, use [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) to automatically stop [Amazon EC2](https://docs.aws.amazon.com/ec2/) and [Amazon RDS](https://docs.aws.amazon.com/rds/) instances during off-hours (for example, stop at 7 PM weekdays and all day weekends, start at 7 AM weekdays). 

1.  **Manage data safely in experimental environments:** Treat security and compliance as the first consideration when deciding what data to use in sandbox and ephemeral environments, not cost. Avoid copying production data into experimental environments when you can use synthetic data instead. When production-like data is truly needed, apply data masking or anonymization before it leaves production ([AWS Glue DataBrew](https://docs.aws.amazon.com/databrew/latest/dg/what-is.html) supports masking transforms), and make sure that the target environment meets the same regulatory obligations (for example, GDPR, HIPAA, PCI DSS) as the source. For transfers, use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) or [S3 Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) to keep encryption in transit and at rest consistent and manage egress costs. 

1.  **Use ephemeral environments for feature work and short-lived experiments:** Create short-lived environments on demand for pull request reviews, feature branch testing, or time-boxed experiments, and tear them down when the work is complete. Use a CI/CD pipeline to spin up resources from [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates or Terraform modules when a pull request opens, run the required tests, and delete the resources when the pull request merges or closes. For resources that outlive the pipeline run, schedule cleanup with [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules that invoke [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) after a defined idle period. Tag ephemeral resources with a creation timestamp and an expiration date so that automation can find and remove them reliably, and set [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) alerts per team to catch runaway spend from environments that fail to clean up. 

1.  **Keep load, destructive, and chaos testing out of production:** Treat production as off-limits for load testing, destructive failure testing, and unbounded chaos experiments until changes have been validated in pre-production environments. Use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or other infrastructure as code tools so the test environment mirrors production architecture, instance types, database configurations, and network topology, with environment-specific parameters for endpoint URLs, database connection strings, and scaling limits. Advanced teams practicing chaos engineering might run carefully scoped experiments in production with impact radius controls, emergency stop mechanisms, and rollback paths, but this requires high operational maturity and must not be the first place a failure mode is tested. 

1.  **Provide a dedicated space for testing organization-wide foundation changes:** Changes to service control policies, AWS Control Tower configurations, or custom landing zone components can affect every account in the organization if they go wrong. For most organizations, a dedicated non-production OU or account inside the production AWS Organization is enough to test these changes before promoting them. Consider a separate AWS Organization only when you manage hundreds of accounts, change organization-wide policies often, or cannot accept the risk that a misconfigured SCP or landing zone upgrade breaks deployments across the whole organization. When the need is real, [create a new AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) that mirrors production structure but hosts no customer workloads, follow the guidance on [testing changes to your overall AWS environment](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/multiple-organizations.html#test-changes-to-your-overall-aws-environment), and promote validated changes to the production organization through automated pipelines with all organization-level configuration (SCPs, controls, baselines) stored in version control. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) 
+  [FND01-BP02 Establish ownership for billing, security, and operations](fnd01-bp02.md) 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 

 **Related documents:** 
+  [Organizing your AWS environment whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 
+  [Test changes to your overall AWS environment](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/multiple-organizations.html#test-changes-to-your-overall-aws-environment) 
+  [AWS Organizations best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html) 
+  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) 

 **Related examples:** 
+  [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) 
+  [Innovation Sandbox on AWS](https://docs.aws.amazon.com/solutions/innovation-sandbox-on-aws/) 
+  [Customizations for AWS Control Tower (CfCT)](https://docs.aws.amazon.com/controltower/latest/userguide/customize-landing-zone.html) 
+  [Landing Zone Accelerator on AWS](https://docs.aws.amazon.com/solutions/landing-zone-accelerator-on-aws/) 

 **Related workshops:** 
+  [AWS Control Tower Workshop](https://catalog.workshops.aws/control-tower) 

 **Related services:** 
+  [AWS Control Tower](https://aws.amazon.com/controltower/) 
+  [AWS Control Tower Account Factory for Terraform (AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html) 
+  [AWS Organizations](https://aws.amazon.com/organizations/) 
+  [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) 
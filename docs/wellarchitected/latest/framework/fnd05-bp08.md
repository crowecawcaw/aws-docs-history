

# FND05-BP08 Employ vulnerability and patch management controls

 Establish centralized vulnerability and patch management so your organization can identify, assess, and remediate security weaknesses consistently across workloads. A shared foundation reduces duplicated effort and creates clear accountability. 

 **Desired outcome:** 
+  You have established centralized capabilities for vulnerability management that include standardized tools, processes, and policies for scanning, patch management, and security monitoring. 
+  You have clear governance structures in place for security control implementation, exception management, and compliance reporting. 
+  Your automated systems continuously monitor the security posture across all workloads, with centralized dashboards providing real-time visibility into risks and their remediation status. 
+  Teams across your organization understand how to use these foundational services and can address workload-specific security requirements. 

 **Common anti-patterns:** 
+  Letting each team implement their own vulnerability management tools and processes, leading to inconsistent security coverage and duplicated effort. 
+  Implementing centralized tools without providing clear guidance, support, or training for workload teams to use them. 
+  Enforcing rigid security controls without a defined exception process, causing teams to create workarounds. 
+  Focusing solely on tool deployment without establishing supporting processes, policies, and governance structures, and setting policies without input from workload teams. 
+  Rolling out foundational security services without considering different workload requirements (for example, development and production environments) and treating all workloads with the same security requirements regardless of data sensitivity. 
+  Deploying multiple overlapping security scanning tools that create alert fatigue, without establishing clear ownership and processes for remediation. 

 **Benefits of establishing this best practice:** 
+  Consistent security controls and processes across the organization provide full vulnerability management coverage and standardized security practices. 
+  Foundational services and processes that workload teams can consume reduce duplication of effort, so teams can focus on their core objectives while meeting security standards. 
+  Centralized security tooling and processes remove redundant tool deployments and reduce operational overhead across workload teams. 
+  Standardized vulnerability management practices and automated monitoring provide consistent and reliable security coverage across all workloads. 
+  Well-defined policies, processes, and accountability for security control implementation and exception management are established across the organization. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Before cloud technologies, establishing a strong vulnerability management foundation across an enterprise was challenging because of diverse systems, inconsistent tooling, and limited visibility. Organizations faced siloed security efforts and the heavy manual effort associated with deploying and maintaining security infrastructure. The cloud now supports centralized management, automated scanning, and scalable security services that can be consistently applied across diverse workloads. 

 A unified vulnerability management foundation provides standardized tools, processes, and policies for the entire organization. Where possible, adopt immutable infrastructure to reduce risk exposure and simplify patch management. Deploy new instances with the latest updates and retire the old ones instead of patching in place. Use [EC2 Image Builder](https://aws.amazon.com/image-builder/) to build and maintain pre-patched machine images. 

 Use [Amazon Inspector](https://aws.amazon.com/inspector/) to assess vulnerabilities in EC2 instances, container images, and Lambda functions. For systems that require in-place patching, configure [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) centrally to manage patches across compute resources. 

 Use [AWS Organizations](https://aws.amazon.com/organizations/) and [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to enforce security standards across accounts, including policies that require approved, up-to-date AMIs. [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) shows security alerts and compliance status across accounts and routes its findings automatically to [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html). Security Hub CSPM correlates them with findings from Amazon Inspector and other services to produce exposure findings that prioritize the most critical risks. AWS [recommends enabling both services](https://docs.aws.amazon.com/securityhub/latest/userguide/what-are-securityhub-services.html). 

 Integrating these services with broader organizational monitoring and ticketing systems enables tracking and remediation of identified vulnerabilities. Balance centralized controls with workload team autonomy. While the foundation provides standardized tools and processes, it should also allow flexibility to address unique workload requirements, and clear processes for exception management help the centralized foundation accommodate diverse compliance requirements across different business units or geographical regions. 

 Pair the tools that discover vulnerabilities with governance that defines severity thresholds, remediation SLAs, escalation paths, and the exception management process. Send findings into the tools teams already use (ticketing, change management, and chat) so remediation fits their existing workflows. Automate responses where judgment is not required, such as blocking deployment of container images with critical vulnerabilities. Route the rest to the appropriate owners with enough context to act. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Prioritize immutable infrastructure:** Start by adopting an immutable infrastructure approach where possible, deploying workloads in verified known-good states rather than patching in place. Use [EC2 Image Builder](https://aws.amazon.com/image-builder/) to create and maintain pipelines for building standardized AMIs and container images. See [Create an image pipeline](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html). This approach substantially reduces the need for ongoing patch management and provides consistent, tested environments across your organization. 

1.  **Implement automated vulnerability scanning:** Configure [Amazon Inspector](https://aws.amazon.com/inspector/) to automatically scan your compute resources, including [Amazon EC2](https://aws.amazon.com/ec2/) instances, container images in [Amazon ECR](https://aws.amazon.com/ecr/) repositories, and [AWS Lambda](https://aws.amazon.com/lambda/) functions. See [Getting started with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html). Amazon Inspector provides enhanced container image scanning that supersedes basic [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) with deeper vulnerability analysis and continual monitoring, so Inspector is the preferred choice when both are available. Centralize findings in [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/), and use [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to maintain an inventory of resources that require scanning. 

1.  **Assess patch management requirements and constraints:** Before implementing patch management processes, assess requirements across different workload types. Identify systems that require in-place patching compared with those that can adopt immutable infrastructure patterns. Document regulatory and compliance requirements that dictate patch timelines, and understand operational constraints such as maintenance windows and change control processes. Review [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) capabilities and determine which operating systems and applications in your environment are supported. 

1.  **Establish centralized patch management:** For resources that require in-place patching, use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to define organization-wide patch baselines. See [Working with custom patch baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-predefined-and-custom-patch-baselines.html). Configure [Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html) to schedule patching during approved windows. Set up automated patch compliance reporting. Implement automated rollback procedures using [Systems Manager Automation runbooks](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.html) for failed patches. Create emergency patch deployment procedures for zero-day vulnerabilities. 

1.  **Create an exception management process:** Develop standardized exception request templates specifically for vulnerability management exceptions (delayed patching, scan exclusions). Define clear approval workflows based on risk levels, with stricter requirements for production environments. Use [AWS Organizations](https://aws.amazon.com/organizations/) to track and enforce exception policies through [SCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html). Implement automated exception tracking through [AWS Security Hub CSPM custom insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html), and set up regular reviews of granted exceptions. 

1.  **Establish vulnerability monitoring and reporting:** Centralize security findings in [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) from various sources including [Amazon Inspector](https://aws.amazon.com/inspector/), [Amazon GuardDuty](https://aws.amazon.com/guardduty/), and [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html). Create custom [Security Hub CSPM insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html) for vulnerability trending and aging. Enable [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) alongside Security Hub CSPM so vulnerability findings are correlated with threat and posture signals to generate exposure findings that identify the most critical risks. Apply risk-based prioritization that goes beyond raw severity scores. Take into account whether systems are internet-facing, the presence of compensating controls, and the business criticality of affected workloads. Use Security Hub CSPM [finding attributes](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings.html) and [custom actions](https://docs.aws.amazon.com/securityhub/latest/userguide/) to enrich findings with this environmental context. Configure [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rules to automate responses to critical vulnerabilities. See [Automated response and remediation](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html). Integrate with third-party ticketing systems for automated remediation tracking. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP04 Implement mechanisms for patch management](fnd04-bp04.md) 
+  [FND05-BP01 Shift compliance checks left with proactive controls](fnd05-bp01.md) 
+  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md) 
+  [SEC06-BP02 Provision compute from hardened images](sec06-bp02.md) 
+  [SEC06-BP04 Validate software integrity](sec06-bp04.md) 
+  [SEC06-BP05 Automate compute protection](sec06-bp05.md) 

 **Related documents:** 
+  [Security OU - Security Tooling account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) 
+  [Solutions for Cloud Foundations](https://aws.amazon.com/solutions/cloud-foundations/) 

 **Related videos:** 
+  [AWS re:Inforce 2023 - Vulnerability management at scale drives enterprise transformation (TDR203)](https://www.youtube.com/watch?v=BRRBVe8R2Vg) 

 **Related examples:** 
+  [Amazon Inspector suppression rules best practices for AWS Organizations](https://aws.amazon.com/blogs/security/amazon-inspector-suppression-rules-best-practices-for-aws-organizations/) 
+  [Beyond compute: Shifting vulnerability detection left with Amazon Inspector code security capabilities](https://aws.amazon.com/blogs/security/shifting-vulnerability-detection-left-with-amazon-inspector-code-security-capabilities/) 

 **Related services:** 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/features/) 
+  [Amazon GuardDuty](https://aws.amazon.com/guardduty/) 
+  [EC2 Image Builder](https://aws.amazon.com/image-builder/) 
+  [AWS Config](https://aws.amazon.com/config/) 
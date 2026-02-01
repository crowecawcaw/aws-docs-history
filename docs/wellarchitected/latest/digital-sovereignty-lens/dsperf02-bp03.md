# DSPERF02-BP03 Validate open-source components for sovereignty

compliance

Open-source solutions can provide essential transparency for
demonstrating compliance and managing risk in highly regulated
industries. These solutions offer inspectable, verifiable
components. However, they require rigorous validation to verify that
they meet regulatory requirements and security standards. Unvetted
components could introduce vulnerabilities or compliance gaps
leading to operational or regulatory issues.

**Desired outcome:** Open-source
components meet security and regulatory standards before deployment.
Audit trails provide complete traceability for sovereignty
verification. Automated validation pipelines and continuous
monitoring detect vulnerabilities before they impact production.

**Common anti-patterns:**

- Failing to audit third-party libraries, nested dependencies, and
  maintaining updated versions of open-source components.
- Not establishing automated processes for security scanning,
  vulnerability management, and compliance verification.
- Lacking clear records of component versions, sources,
  modifications, and compliance certifications.
- Overlooking licensing requirements and depending on single
  maintainers or small communities without backup plans.
- Relying on manual checks instead of systematic, automated
  validation procedures for open-source components.

**Benefits of establishing this best
practice:**

- Full access to source code enables comprehensive security
  reviews, vulnerability management, and complete visibility into
  codebases.
- Demonstrate due diligence and control effectiveness through
  auditable solutions aligned with industry frameworks.
- Use collective expertise for rapid vulnerability response and
  continuous improvement.
- Avoid vendor dependency while maintaining ability to customize
  solutions for specific requirements.
- Reducing compliance penalties through proactive risk management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Develop a comprehensive open-source adoption strategy that begins
with technology stack inventory and establishes governance
processes for evaluating and maintaining components.

Key implementation elements:

- Create evaluation criteria aligned with security and
  regulatory requirements
- Implement software composition analysis (SCA) tools for
  dependency scanning
- Integrate automated compliance checks and security testing
  into CI/CD pipelines
- Use Infrastructure as Code (IaC) to enforce consistency across
  environments
- Establish continuous monitoring for vulnerabilities and
  updates
- Develop internal expertise for ongoing evaluation and
  maintenance

This approach supports safe adoption of open-source solutions
while improving security and regulatory standard adherence.

### Implementation steps

1. Conduct a technology stack assessment. Document current
   components, dependencies, licensing requirements, and
   security implications. Create an inventory database and map
   component dependencies. Open source option to assist with
   creation is
   [OCS
   Inventory NG](https://github.com/ocsinventory-ng "https://github.com/ocsinventory-ng") or consider
   [AWS Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md") can be used to expedite the
   process.
2. Implement security scanning with open source services like
   [Trivy](https://trivy.dev/latest/ "https://trivy.dev/latest/") or
   AWS services including
   [Amazon CodeGuru](../../../codeguru/latest/reviewer-ug/welcome.md "../../../codeguru/latest/reviewer-ug/welcome.md") and
   [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md"). Set up automated scanning and integrate
   security checks into the CI/CD pipeline with
   [AWS CodePipeline](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md").
3. Develop infrastructure as code using open source options
   like
   [Terraform](https://developer.hashicorp.com/terraform "https://developer.hashicorp.com/terraform")
   or [OpenTofu](https://opentofu.org/ "https://opentofu.org/")
   or AWS services including
   [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md") and
   [AWS CDK](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md") to create standard templates, security controls,
   and compliance checks.
4. Configure vulnerability monitoring with open source options
   like [Wazuh](https://wazuh.com/ "https://wazuh.com/") or
   [Falco](https://github.com/falcosecurity/falco "https://github.com/falcosecurity/falco")
   or AWS service
   including[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md"),
   [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md"), and
   [Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md"), setting up alerts for detected
   vulnerabilities.
5. Implement configuration management using either
   [Ansible](https://docs.ansible.com/ "https://docs.ansible.com/")
   or
   [AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") for version control, change
   management, update tracking, and patch management, ensuring
   consistent and secure configurations across the environment.

## Resources

**Related best practices:**

- [ADVPERF01-BP05
  Evaluate the choice of open source-based software
  (self-managed) against using fully managed service](../video-streaming-advertising-lens/advperf01-bp05.md "../video-streaming-advertising-lens/advperf01-bp05.md")
- [SEC04-BP02
  Capture logs, findings, and metrics in standardized
  locations](../security-pillar/sec_detect_investigate_events_logs.md "../security-pillar/sec_detect_investigate_events_logs.md")
- [SEC06-BP01
  Perform vulnerability management](../security-pillar/sec_protect_compute_vulnerability_management.md "../security-pillar/sec_protect_compute_vulnerability_management.md")

**Related documents:**

- [Open
  government methods, infrastructure, and tools](../government-lens/open-government-methods-infrastructure-and-tools.md "../government-lens/open-government-methods-infrastructure-and-tools.md")
- [Automate
  AWS resource assessment](../../../prescriptive-guidance/latest/patterns/automate-aws-resource-assessment.md "../../../prescriptive-guidance/latest/patterns/automate-aws-resource-assessment.md")
- [Define
  a vulnerability management plan](../security-pillar/sec_protect_compute_vulnerability_management.md "../security-pillar/sec_protect_compute_vulnerability_management.md")

**Related videos:**

- [AWS re:Inforce 2023 - Security in the Open: OSS and AWS
  (SEC201-L)](https://www.youtube.com/watch?v=Hblyw--Fnw4 "https://www.youtube.com/watch?v=Hblyw--Fnw4")
- [AWS re:Invent 2024 - How to maintain and automate compliance on
  AWS (SEC319)](https://www.youtube.com/watch?v=o93VHX4V7jY "https://www.youtube.com/watch?v=o93VHX4V7jY")

**Related services:**

- [Amazon CodeGuru](https://aws.amazon.com/codeguru/ "https://aws.amazon.com/codeguru/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/")
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")

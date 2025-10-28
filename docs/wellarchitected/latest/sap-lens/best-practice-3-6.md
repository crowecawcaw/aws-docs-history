# Best Practice 3.6 – Use automation to

perform SAP landscape operations

Create automation pipelines for your SAP environment builds and landscape operations.
Automation using Infrastructure as Code techniques (for example, CloudFormation, Launch
Wizard for SAP) allows repeatable and agile environment creation or extension. Automated
pipelines and landscape operations reduce errors caused by manual processes, reduce the
effort to deploy changes and improves speed to react to your business needs.

Create automated SAP landscape operational pipelines that allow you to perform common
environment tasks in an automated fashion (for example, System Copy, Start SAP, Stop SAP,
Scale SAP). Invoke these pipelines in response to operational events such as time-based
system shutdown or automatic scaling due to user load.

**Suggestion 3.6.1- Implement infrastructure as code techniques to
create repeatable and code-driven build pipelines for your SAP landscape**

Use tools such as AWS CloudFormation, AWS Cloud Development Kit (AWS CDK) or AWS Launch Wizard for SAP to create
repeatable, controlled and quick environment deployments.

- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/ "https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/")
- AWS Documentation: [AWS
  Launch Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/")

**Suggestion 3.6.2 - Implement common SAP landscape operations with
automation**

Use orchestration and infrastructure as code (IaC) tools in combination to perform
your common SAP landscape operations in an automated fashion. Tools such as AWS CloudFormation, AWS
Systems Manager – Run Automations, SAP Landscape Management (LaMa) and AWS Lambda can be
orchestrated to perform common SAP landscape operations in deployment pipelines.

Consider third-party automation tools where complex or deep integration between tools
is required (For example: Terraform, Ansible, Chef).

Consider using automated operations as responses to SAP workload events to allow a
self-healing and self-maintaining landscape.

- SAP Note: [2574820

* SAP Landscape Management Cloud Manager for Amazon Web Services (AWS)](https://launchpad.support.sap.com/#/notes/2574820 "https://launchpad.support.sap.com/#/notes/2574820")
  [Requires SAP Portal Access]

- AWS Documentation: [AWS
  Launch Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/")
- AWS Documentation: [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- AWS Marketplace: [Products and Tools for DevOps](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=sap&category=45c68cc2-ccd6-426b-94bd-92a791004dc2 "https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=sap&category=45c68cc2-ccd6-426b-94bd-92a791004dc2")

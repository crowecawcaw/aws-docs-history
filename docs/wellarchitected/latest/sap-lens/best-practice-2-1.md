# Best Practice 2.1 – Use version

control and configuration management

Configuration Management systems reduce errors caused by manual processes and reduce
the level of effort to deploy changes. Doing so supports tracking changes, deploying new
versions, detecting changes to existing versions, and reverting to prior versions (for
example, rolling back to a known good state in the event of a failure). Integrate the
version control capabilities of your configuration management systems into all your
procedures across SAP – the infrastructure, the database, the application, and SAP custom
code and developments (for example, ABAP, Java, and UI5/JavaScript).

Consider different version control systems for each type of configuration, but
consolidate metrics into a central release planning tool. Consider how non-transportable
configuration and binary versioning is managed across your environments (for example - how
do you know that your SAP Kernel versions are aligned across your landscape?).

**Suggestion 2.1.1 - Implement SAP change control or other third-party
tools for managing your SAP development code and versioning**

Ensure you implement change control for all development approaches and custom code
that support your SAP applications - ABAP, Java, UI5/JavaScript, and any other extensions
or scripting areas. Consider all your SAP applications and how you will orchestrate code
deployment across multiple SAP deployment patterns (for example, how will you
simultaneously release related developments hosted on AWS and SAP Business Technology
Platform).

- AWS Service: [AWS CodeCommit](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md")
- AWS Video: [Introduction to AWS CodeCommit](https://youtu.be/46PRLMW8otg?ref=wellarchitected "https://youtu.be/46PRLMW8otg?ref=wellarchitected")
- SAP on AWS Blog: [AWS DevOps tools for SAP, Part 1: Cloud Foundry](https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-1-cloud-foundry-apps/ "https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-1-cloud-foundry-apps/")
- SAP on AWS Blog: [AWS DevOps tools for SAP, Part 2: SAP Fiori Apps](https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-2-sap-fiori-apps/ "https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-2-sap-fiori-apps/")
- SAP Documentation: [SAP Change Control Management](https://help.sap.com/viewer/8b923a2175be4939816f0981b73856c7/LATEST/en-US/2b614e1cb8204f35b477eac703073589.html "https://help.sap.com/viewer/8b923a2175be4939816f0981b73856c7/LATEST/en-US/2b614e1cb8204f35b477eac703073589.html")
- SAP Documentation: [Best
  Practices for SAP BTP - Lifecycle Management](https://help.sap.com/viewer/df50977d8bfa4c9a8a063ddb37113c43/Cloud/en-US "https://help.sap.com/viewer/df50977d8bfa4c9a8a063ddb37113c43/Cloud/en-US")

**Suggestion 2.1.2 - Implement configuration management systems for
your SAP applications**

Implement configuration management tools for ABAP, Java, and other SAP technologies
and consider how non-transportable configuration and binary versioning is managed across
your landscape (for example - how do you know that your SAP Kernel versions are aligned
across your environment?). Use SAP Solution Manager to plan and implement configuration
and version changes to your SAP applications.

- SAP on AWS Blog: [Maintain an SAP landscape inventory with AWS Systems Manager and Amazon Athena](https://aws.amazon.com/blogs/awsforsap/maintain-an-sap-landscape-inventory-with-aws-systems-manager-and-amazon-athena/ "https://aws.amazon.com/blogs/awsforsap/maintain-an-sap-landscape-inventory-with-aws-systems-manager-and-amazon-athena/")
- SAP Documentation: [Enhanced Change & Transport System (CTS+)](https://support.sap.com/en/tools/software-logistics-tools/enhanced-change-and-transport-system.html "https://support.sap.com/en/tools/software-logistics-tools/enhanced-change-and-transport-system.html")
- SAP Documentation: [SAP Solution Manager: Planning Landscape Changes](https://www.sap.com/germany/documents/2016/08/8ea1d93a-857c-0010-82c7-eda71af511fa.html "https://www.sap.com/germany/documents/2016/08/8ea1d93a-857c-0010-82c7-eda71af511fa.html")

**Suggestion 2.1.3 - Implement configuration management systems for
operating systems**

Use AMI baking or in-place configuration management software such as Ansible, Chef or
Puppet to align configuration management across your SAP workload operating systems.
Consider security focused configuration management tools which will alert you to
vulnerabilities and prompt you to keep your operating systems patched and hardened.

- AWS Documentation: [AWS Systems Manager - State Manager](../../../systems-manager/latest/userguide/systems-manager-state.md "../../../systems-manager/latest/userguide/systems-manager-state.md")
- AWS Documentation: [Configuration management in Amazon EC2](../../../AWSEC2/latest/WindowsGuide/configuration-management.md "../../../AWSEC2/latest/WindowsGuide/configuration-management.md")
- AWS Documentation: [What is Amazon Inspector?](../../../inspector/latest/userguide/inspector_introduction.md "../../../inspector/latest/userguide/inspector_introduction.md")

**Suggestion 2.1.4 - Implement configuration management systems for
databases**

Work with your database software vendor to understand configuration management
approaches for your database.

- SAP Documentation: [SAP HANA Platform Lifecycle Management](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/571d0bb4b1b2402f8e7caf0fe0290b61.html "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/571d0bb4b1b2402f8e7caf0fe0290b61.html")

**Suggestion 2.1.5 - Implement configuration management systems for
infrastructure**

Use infrastructure as code (IaC) approaches to provision and manage AWS resources
supporting your SAP workloads. AWS CloudFormation and AWS Cloud Development Kit (AWS CDK) are tools you can use to provision
and manage configuration in AWS resources programmatically.

Consider configuration audit and control tools such as [AWS Config: Conformance Packs](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md") that allow you to deploy rules and policies to evaluate
your infrastructure periodically to assess compliance and resolve any problems with
applicable best practices and standards.

- AWS Documentation: [AWS
  Launch Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/")
- AWS Documentation: [AWS Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md")
- AWS Documentation: [AWS Systems Manager Change Manager](../../../systems-manager/latest/userguide/change-manager.md "../../../systems-manager/latest/userguide/change-manager.md")
- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/ "https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/")
- SAP Lens [Reliability]: [Best Practice 11.3 -
  Define an approach to restore service availability](best-practice-11-3.md "best-practice-11-3.md")

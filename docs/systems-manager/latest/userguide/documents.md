AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# AWS Systems Manager Documents

An AWS Systems Manager document (SSM document) defines the actions that Systems Manager performs on your
managed instances. Systems Manager includes more than 100 pre-configured documents that you can use by
specifying parameters at runtime. You can find pre-configured documents in the Systems Manager
Documents console by choosing the **Owned by Amazon** tab, or by specifying
Amazon for the `Owner` filter when calling the `ListDocuments` API
operation. Documents use JavaScript Object Notation (JSON) or YAML, and they include steps
and parameters that you specify.

For enhanced security, as of July 14th, 2025, SSM documents support environment variable
interpolation when processing parameters. This feature, available in schema version 2.2 and
with SSM Agent version 3.3.2746.0 or higher, helps prevent command injection attacks.

To get started with SSM documents, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/documents "https://console.aws.amazon.com/systems-manager/documents"). In the navigation pane, choose
**Documents**.

###### Important

In Systems Manager, an _Amazon-owned_ SSM document is a document created
and managed by Amazon Web Services itself. _Amazon-owned_ documents include a
prefix like `AWS-*` in the document name. The owner of the document is
considered to be Amazon, not a specific user account within AWS. These documents are
publicly available for all to use.

## How can the Documents tool benefit my

organization?

Documents, a tool in AWS Systems Manager, offers these benefits:

- **Document categories**

To help you find the documents you need, choose a category depending on the
type of document you're searching for. To broaden your search, you can choose
multiple categories of the same document type. Choosing categories of different
document types is not supported. Categories are only supported for documents
owned by Amazon.

- **Document versions**

You can create and save different versions of documents. You can then specify
a default version for each document. The default version of a document can be
updated to a newer version or reverted to an older version of the document. When
you change the content of a document, Systems Manager automatically increments the version
of the document. You can retrieve or use any version of a document by specifying
the document version in the console, AWS Command Line Interface (AWS CLI) commands, or API
calls.

- **Customize documents for your needs**

If you want to customize the steps and actions in a document, you can create
your own. The system stores the document with your AWS account in the
AWS Region you create it in. For more information about how to create an SSM
document, see [Creating SSM document content](documents-creating-content.md "documents-creating-content.md").

- **Tag documents**

You can tag your documents to help you quickly identify one or more documents
based on the tags you've assigned to them. For example, you can tag documents
for specific environments, departments, users, groups, or periods. You can also
restrict access to documents by creating an AWS Identity and Access Management (IAM) policy that
specifies the tags that a user or group can access.

- **Share documents**

You can make your documents public or share them with specific AWS accounts
in the same AWS Region. Sharing documents between accounts can be useful if,
for example, you want all of the Amazon Elastic Compute Cloud (Amazon EC2) instances that you supply to
customers or employees to have the same configuration. In addition to keeping
applications or patches on the instances up to date, you might want to restrict
customer instances from certain activities. Or you might want to ensure that the
instances used by employee accounts throughout your organization are granted
access to specific internal resources. For more information, see [Sharing SSM documents](documents-ssm-sharing.md "documents-ssm-sharing.md").

## Who should use Documents?

- Any AWS customer who wants to use Systems Manager tools to improve their operational
  efficiency at scale, reduce errors associated with manual intervention, and
  reduce time to resolution of common issues.
- Infrastructure experts who want to automate deployment and configuration
  tasks.
- Administrators who want to reliably resolve common issues, improve
  troubleshooting efficiency, and reduce repetitive operations.
- Users who want to automate a task they normally perform manually.

## What are the types of SSM documents?

The following table describes the different types of SSM documents and their
uses.

| Type                                                       | Use with                                                                                                                                                                                                                      | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ApplicationConfiguration<br>ApplicationConfigurationSchema | [AWS AppConfig](../../../appconfig/latest/userguide/what-is-appconfig.md "../../../appconfig/latest/userguide/what-is-appconfig.md")                                                                                          | AWS AppConfig, a tool in AWS Systems Manager, enables you to create, manage, and<br>quickly deploy application configurations. You can store<br>configuration data in an SSM document by creating a document that<br>uses the `ApplicationConfiguration` document type. For<br>more information, see [Freeform configurations](../../../appconfig/latest/userguide/appconfig-creating-configuration-and-profile.md#free-form-configurations "../../../appconfig/latest/userguide/appconfig-creating-configuration-and-profile.md#free-form-configurations") in the<br>_AWS AppConfig User Guide_.<br>If you create a configuration in an SSM document, then you must<br>specify a corresponding JSON Schema. The schema uses the<br>`ApplicationConfigurationSchema` document type and,<br>like a set of rules, defines the allowable properties for each<br>application configuration setting. For more information, see [About validators](../../../appconfig/latest/userguide/appconfig-creating-configuration-and-profile-validators.md "../../../appconfig/latest/userguide/appconfig-creating-configuration-and-profile-validators.md") in the<br>_AWS AppConfig User Guide_. |
| Automation runbook                                         | [Automation](systems-manager-automation.md "systems-manager-automation.md")<br>[State Manager](systems-manager-state.md "systems-manager-state.md")<br>[Maintenance Windows](maintenance-windows.md "maintenance-windows.md") | Use Automation runbooks when performing common maintenance and<br>deployment tasks such as creating or updating an Amazon Machine Image (AMI).<br>State Manager uses Automation runbooks to apply a configuration. These<br>actions can be run on one or more targets at any point during the<br>lifecycle of an instance. Maintenance Windows uses Automation runbooks to<br>perform common maintenance and deployment tasks based on the<br>specified schedule.<br>All Automation runbooks that are supported for Linux-based<br>operating systems are also supported on EC2 instances for<br>macOS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Change Calendar document                                   | [Change Calendar](systems-manager-change-calendar.md "systems-manager-change-calendar.md")                                                                                                                                    | Change Calendar, a tool in AWS Systems Manager, uses the<br>`ChangeCalendar` document type. A Change Calendar document<br>stores a calendar entry and associated events that can allow or<br>prevent Automation actions from changing your environment. In<br>Change Calendar, a document stores [iCalendar 2.0](https://icalendar.org/ "https://icalendar.org/") data in plaintext format.<br>Change Calendar isn't supported on EC2 instances for macOS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AWS CloudFormation template                                | [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")                                                                                         | AWS CloudFormation templates describe the resources that you want to<br>provision in your CloudFormation stacks. By storing CloudFormation templates<br>as Systems Manager documents, you can benefit from Systems Manager document features.<br>These include creating and comparing multiple versions of your<br>template, and sharing your template with other accounts in the same<br>AWS Region.<br>You can create and edit CloudFormation templates and stacks by using<br>Application Manager, a tool in Systems Manager. For more information, see [Working with AWS CloudFormation templates<br>and stacks in Application Manager](application-manager-working-stacks.md "application-manager-working-stacks.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Command document                                           | [Run Command](run-command.md "run-command.md")<br>[State Manager](systems-manager-state.md "systems-manager-state.md")<br>[Maintenance Windows](maintenance-windows.md "maintenance-windows.md")                              | Run Command, a tool in AWS Systems Manager, uses Command documents to run<br>commands. State Manager, a tool in AWS Systems Manager, uses command documents to<br>apply a configuration. These actions can be run on one or more<br>targets at any point during the lifecycle of an instance. Maintenance Windows,<br>a tool in AWS Systems Manager, uses Command documents to apply a configuration<br>based on the specified schedule.<br>Most Command documents are supported on all Linux and Windows Server<br>operating systems supported by Systems Manager. The following Command<br>documents are supported on EC2 instances for macOS:<br>• `AWS-ConfigureAWSPackage`<br>• `AWS-RunPatchBaseline`<br>• `AWS-RunPatchBaselineAssociation`<br>• `AWS-RunShellScript`                                                                                                                                                                                                                                                                                                                                                                                                        |
| AWS Config conformance pack template                       | [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")                                                                                                   | AWS Config conformance pack templates are YAML formatted documents<br>used to create conformance packs that contains the list of AWS Config<br>managed or custom rules and remediation actions.<br>For more information, see [Conformance Packs](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Package document                                           | [Distributor](distributor.md "distributor.md")                                                                                                                                                                                | In Distributor, a tool in AWS Systems Manager, a package is represented by an<br>SSM document. A package document includes attached ZIP archive<br>files that contain software or assets to install on managed<br>instances. Creating a package in Distributor creates the package<br>document.<br>Distributor isn't supported on Oracle Linux and macOS managed<br>instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Policy document                                            | [State Manager](systems-manager-state.md "systems-manager-state.md")                                                                                                                                                          | Inventory, a tool in AWS Systems Manager, uses the<br>`AWS-GatherSoftwareInventory` Policy document with a<br>State Manager association to collect inventory data from managed<br>instances. When creating your own SSM documents, Automation<br>runbooks and Command documents are the preferred method for<br>enforcing a policy on a managed instance.<br>Systems Manager Inventory and the `AWS-GatherSoftwareInventory`<br>Policy document are supported on all operating systems supported by<br>Systems Manager.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Post-incident analysis template                            | [Incident Manager post-incident analysis](../../../incident-manager/latest/userguide/analysis.md "../../../incident-manager/latest/userguide/analysis.md")                                                                    | Incident Manager uses the post-incident analysis template to create an<br>analysis based on AWS operations management best practices.<br>Use the template to create an analysis that your team can use to<br>identify improvements to your incident response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Session document                                           | [Session Manager](session-manager.md "session-manager.md")                                                                                                                                                                    | Session Manager, a tool in AWS Systems Manager, uses Session documents to determine<br>which type of session to start, such as a port forwarding session, a<br>session to run an interactive command, or a session to create an SSH<br>tunnel.<br>Session documents are supported on all Linux and Windows Server<br>operating systems supported by Systems Manager. The following Command<br>documents are supported on EC2 instances for macOS:<br>• `AWS-PasswordReset`<br>• `AWS-StartInteractiveCommand`<br>• `AWS-StartPortForwardingSession`<br>• `AWS-StartPortForwardingSessionToSocket`<br>• `AWS-StartSSHSession`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

###### SSM document quotas

For information about SSM document quotas, see [Systems Manager service quotas](../../../general/latest/gr/ssm.md#limits_ssm "../../../general/latest/gr/ssm.md#limits_ssm") in the
_Amazon Web Services General Reference_.

###### Topics

- [Document components](documents-components.md "documents-components.md")
- [Creating SSM document content](documents-creating-content.md "documents-creating-content.md")
- [Working with documents](documents-using.md "documents-using.md")
- [Troubleshooting parameter handling
  issues](parameter-troubleshooting.md "parameter-troubleshooting.md")



• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# AWS Systems Manager Documents
<a name="documents"></a>

An AWS Systems Manager document (SSM document) defines the actions that Systems Manager performs on your managed instances. Systems Manager includes more than 100 pre-configured documents that you can use by specifying parameters at runtime. You can find pre-configured documents in the Systems Manager Documents console by choosing the **Owned by Amazon** tab, or by specifying Amazon for the `Owner` filter when calling the `ListDocuments` API operation. Documents use JavaScript Object Notation (JSON) or YAML, and they include steps and parameters that you specify. 

For enhanced security, as of July 14th, 2025, SSM documents support environment variable interpolation when processing parameters. This feature, available in schema version 2.2 and with SSM Agent version 3.3.2746.0 or higher, helps prevent command injection attacks.

To get started with SSM documents, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/documents). In the navigation pane, choose **Documents**.

**Important**  
In Systems Manager, an *Amazon-owned* SSM document is a document created and managed by Amazon Web Services itself. *Amazon-owned* documents include a prefix like `AWS-*` in the document name. The owner of the document is considered to be Amazon, not a specific user account within AWS. These documents are publicly available for all to use.

## How can the Documents tool benefit my organization?
<a name="ssm-docs-benefits"></a>

Documents offers these benefits:
+ **Document categories**

  To help you find the documents you need, choose a category depending on the type of document you're searching for. To broaden your search, you can choose multiple categories of the same document type. Choosing categories of different document types is not supported. Categories are only supported for documents owned by Amazon.
+  **Document versions** 

  You can create and save different versions of documents. You can then specify a default version for each document. The default version of a document can be updated to a newer version or reverted to an older version of the document. When you change the content of a document, Systems Manager automatically increments the version of the document. You can retrieve or use any version of a document by specifying the document version in the console, AWS Command Line Interface (AWS CLI) commands, or API calls.
+  **Customize documents for your needs** 

  If you want to customize the steps and actions in a document, you can create your own. The system stores the document with your AWS account in the AWS Region you create it in. For more information about how to create an SSM document, see [Creating SSM document content](documents-creating-content.md).
+  **Tag documents** 

  You can tag your documents to help you quickly identify one or more documents based on the tags you've assigned to them. For example, you can tag documents for specific environments, departments, users, groups, or periods. You can also restrict access to documents by creating an AWS Identity and Access Management (IAM) policy that specifies the tags that a user or group can access.
+  **Share documents** 

  You can make your documents public or share them with specific AWS accounts in the same AWS Region. Sharing documents between accounts can be useful if, for example, you want all of the Amazon Elastic Compute Cloud (Amazon EC2) instances that you supply to customers or employees to have the same configuration. In addition to keeping applications or patches on the instances up to date, you might want to restrict customer instances from certain activities. Or you might want to make sure that the instances used by employee accounts throughout your organization are granted access to specific internal resources. For more information, see [Sharing SSM documents](documents-ssm-sharing.md).

## Who should use Documents?
<a name="documents-who"></a>
+ Any AWS customer who wants to use Systems Manager tools to improve their operational efficiency at scale, reduce errors associated with manual intervention, and reduce time to resolution of common issues.
+ Infrastructure experts who want to automate deployment and configuration tasks.
+ Administrators who want to reliably resolve common issues, improve troubleshooting efficiency, and reduce repetitive operations.
+ Users who want to automate a task they normally perform manually.

## What are the types of SSM documents?
<a name="what-are-document-types"></a>

The following table describes the different types of SSM documents and their uses.



| Type | Use with | Details | 
| --- | --- | --- | 
| ApplicationConfiguration<br />ApplicationConfigurationSchema |  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)  | AWS AppConfig lets you create, manage, and quickly deploy application configurations. You can store configuration data in an SSM document by creating a document that uses the `ApplicationConfiguration` document type. For more information, see [Freeform configurations](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#free-form-configurations) in the *AWS AppConfig User Guide*.<br />If you create a configuration in an SSM document, then you must specify a corresponding JSON Schema. The schema uses the `ApplicationConfigurationSchema` document type and, like a set of rules, defines the allowable properties for each application configuration setting. For more information, see [About validators](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile-validators.html) in the *AWS AppConfig User Guide*. | 
| Automation runbook |  [Automation](systems-manager-automation.md) <br /> [State Manager](systems-manager-state.md) <br /> [Maintenance Windows](maintenance-windows.md)  | Use Automation runbooks when performing common maintenance and deployment tasks such as creating or updating an Amazon Machine Image (AMI). State Manager uses Automation runbooks to apply a configuration. These actions can be run on one or more targets at any point during the lifecycle of an instance. Maintenance Windows uses Automation runbooks to perform common maintenance and deployment tasks based on the specified schedule.<br />All Automation runbooks that are supported for Linux-based operating systems are also supported on EC2 instances for macOS. | 
| Change Calendar document |  [Change Calendar](systems-manager-change-calendar.md)  | Change Calendar uses the `ChangeCalendar` document type. A Change Calendar document stores a calendar entry and associated events that can allow or prevent Automation actions from changing your environment. In Change Calendar, a document stores [iCalendar 2.0](https://icalendar.org/) data in plaintext format.<br />Change Calendar isn't supported on EC2 instances for macOS. | 
| AWS CloudFormation template |  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)  | AWS CloudFormation templates describe the resources that you want to provision in your CloudFormation stacks. By storing CloudFormation templates as Systems Manager documents, you can benefit from Systems Manager document features. These include creating and comparing multiple versions of your template, and sharing your template with other accounts in the same AWS Region.<br />You can create and edit CloudFormation templates and stacks by using Application Manager. For more information, see [Working with CloudFormation templates and stacks in Application Manager](application-manager-working-stacks.md). | 
| Command document |  [Run Command](run-command.md) <br /> [State Manager](systems-manager-state.md) <br /> [Maintenance Windows](maintenance-windows.md)  | Run Command uses Command documents to run commands. State Manager uses command documents to apply a configuration. These actions can be run on one or more targets at any point during the lifecycle of an instance. Maintenance Windows uses Command documents to apply a configuration based on the specified schedule.<br />Most Command documents are supported on all Linux and Windows Server operating systems supported by Systems Manager. The following Command documents are supported on EC2 instances for macOS:+  `AWS-ConfigureAWSPackage` <br />+  `AWS-RunPatchBaseline` <br />+  `AWS-RunPatchBaselineAssociation` <br />+  `AWS-RunShellScript`  | 
| AWS Config conformance pack template |  [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)  | AWS Config conformance pack templates are YAML formatted documents used to create conformance packs that contains the list of AWS Config managed or custom rules and remediation actions.<br />For more information, see [Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html). | 
| Package document |  [Distributor](distributor.md)  | In Distributor, a package is represented by an SSM document. A package document includes attached ZIP archive files that contain software or assets to install on managed instances. Creating a package in Distributor creates the package document.<br />Distributor isn't supported on Oracle Linux and macOS managed instances. | 
| Policy document |  [State Manager](systems-manager-state.md)  | Inventory uses the `AWS-GatherSoftwareInventory` Policy document with a State Manager association to collect inventory data from managed instances. When creating your own SSM documents, Automation runbooks and Command documents are the preferred method for enforcing a policy on a managed instance.<br />Systems Manager Inventory and the `AWS-GatherSoftwareInventory` Policy document are supported on all operating systems supported by Systems Manager. | 
| Post-incident analysis template |  [Incident Manager post-incident analysis](https://docs.aws.amazon.com/incident-manager/latest/userguide/analysis.html)  | Incident Manager uses the post-incident analysis template to create an analysis based on AWS operations management best practices.<br />Use the template to create an analysis that your team can use to identify improvements to your incident response.  | 
| Session document |  [Session Manager](session-manager.md)  | Session Manager uses Session documents to determine which type of session to start. Examples include port forwarding sessions, interactive command sessions, and SSH tunnels.<br />Session documents are supported on all Linux and Windows Server operating systems supported by Systems Manager. The following Command documents are supported on EC2 instances for macOS:+  `AWS-PasswordReset` <br />+  `AWS-StartInteractiveCommand` <br />+  `AWS-StartPortForwardingSession` <br />+  `AWS-StartPortForwardingSessionToSocket` <br />+  `AWS-StartSSHSession`  | 

**SSM document quotas**  
For information about SSM document quotas, see [Systems Manager service quotas](https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm) in the *Amazon Web Services General Reference*.

**Topics**
+ [How can the Documents tool benefit my organization?](#ssm-docs-benefits)
+ [Who should use Documents?](#documents-who)
+ [What are the types of SSM documents?](#what-are-document-types)
+ [Document components](documents-components.md)
+ [Creating SSM document content](documents-creating-content.md)
+ [Working with documents](documents-using.md)
+ [Troubleshooting parameter handling issues](parameter-troubleshooting.md)
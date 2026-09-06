

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Using AWS Systems Manager tools
<a name="systems-manager-tools"></a>

Systems Manager groups tools into four categories. The following documentation describes the various tools of AWS Systems Manager and how to set up and use these tools. Choose the tabs under each category to learn more about each tool.

## Node tools
<a name="capabilities-instances-and-nodes"></a>

A *managed node* is any machine configured for use with Systems Manager in [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environments.

------
#### [ Compliance ]

Use [Compliance](systems-manager-compliance.md) to scan your fleet of managed nodes for patch compliance and configuration inconsistencies. You can collect and aggregate data from multiple AWS accounts and AWS Regions, and then drill down into specific resources that aren’t compliant. By default, Compliance displays compliance data about Patch Manager patching and State Manager associations. You can also customize the service and create your own compliance types based on your IT or business requirements.

------
#### [ Distributor ]

Use [Distributor](distributor.md) to create and deploy packages to managed nodes. With Distributor, you can package your own software—or find AWS-provided agent software packages, such as **AmazonCloudWatchAgent**—to install on Systems Manager managed nodes. After you install a package for the first time, you can use Distributor to uninstall and reinstall a new package version, or perform an in-place update that adds new or changed files. Distributor publishes resources, such as software packages, to Systems Manager managed nodes.

------
#### [ Fleet Manager ]

[Fleet Manager](fleet-manager.md) is a unified user interface (UI) experience that helps you remotely manage your nodes. With Fleet Manager, you can view the health and performance status of your entire fleet from one console. You can also gather data from individual devices and instances to perform common troubleshooting and management tasks from the console. This includes viewing directory and file contents, Windows registry management, operating system user management, and more. 

------
#### [ Hybrid Activations ]

To set up non-EC2 machines in your hybrid and multicloud environment as managed nodes, create a [hybrid activation](systems-manager-hybrid-multicloud.md). After you complete the activation, you receive an activation code and ID. This code and ID combination functions like an Amazon Elastic Compute Cloud (Amazon EC2) access ID and secret key to provide secure access to the Systems Manager service from your managed instances.

You can also create an activation for edge devices if you want to manage them by using Systems Manager.

------
#### [ Inventory ]

[Inventory](systems-manager-inventory.md) automates the process of collecting software inventory from your managed nodes. You can use Inventory to gather metadata about applications, files, components, patches, and more.

------
#### [ Patch Manager ]

Use [Patch Manager](patch-manager.md) to automate the process of patching your managed nodes with both security related and other types of updates. You can use Patch Manager to apply patches for both operating systems and applications. (On Windows Server, application support is limited to updates for applications released by Microsoft.)

This tool lets you scan managed nodes for missing patches and apply missing patches individually or to large groups of managed nodes by using tags. Patch Manager uses *patch baselines*, which can include rules for auto-approving patches within days of their release, and a list of approved and rejected patches. You can install security patches on a regular basis by scheduling patching to run as a Systems Manager maintenance window task, or you can patch your managed nodes on demand at any time.

For Linux operating systems, you can define the repositories that should be used for patching operations as part of your patch baseline. This allows you to make sure that updates are installed only from trusted repositories regardless of what repositories are configured on the managed node. For Linux, you also can update any package on the managed node, not just those that are classified as operating system security updates. You can also generate patch reports that are sent to an S3 bucket of your choice. For a single managed node, reports include details of all patches for the machine. For a report on all managed nodes, only a summary of how many patches are missing is provided.

------
#### [ Run Command ]

Use [Run Command](run-command.md) to remotely and securely manage the configuration of your managed nodes at scale. Use Run Command to perform on-demand changes such as updating applications or running Linux shell scripts and Windows PowerShell commands on a target set of dozens or hundreds of managed nodes. 

------
#### [ Session Manager ]

Use [Session Manager](session-manager.md) to manage your edge devices and Amazon Elastic Compute Cloud (Amazon EC2) instances through an interactive single-step browser-based shell or through the AWS CLI. Session Manager provides secure and auditable edge device and instance management without needing to open inbound ports, maintain bastion hosts, or manage SSH keys. Session Manager also helps you comply with corporate policies that require controlled access to edge devices, strict security practices, and fully auditable logs with access details.

------
#### [ State Manager ]

Use [State Manager](systems-manager-state.md) to automate the process of keeping your managed nodes in a defined state. You can use State Manager to guarantee that your managed nodes are bootstrapped with specific software at startup, joined to a Windows domain (Windows Server nodes only), or patched with specific software updates. 

------

## Change Management tools
<a name="capabilities-actions-and-change"></a>

------
#### [ Automation ]

Use [Automation](systems-manager-automation.md) to automate common maintenance and deployment tasks. You can use Automation to create and update Amazon Machine Images (AMIs), apply driver and agent updates, reset passwords on Windows Server instance, reset SSH keys on Linux instances, and apply OS patches or application updates. 

------
#### [ Change Calendar ]

[Change Calendar](systems-manager-change-calendar.md) helps you set up date and time ranges when actions you specify (for example, in [Systems Manager Automation](systems-manager-automation.md) runbooks) can or can't be performed in your AWS account. In Change Calendar, these ranges are called *events*. When you create a Change Calendar entry, you're creating a [Systems Manager document](documents.md) of the type `ChangeCalendar`. In Change Calendar, the document stores [iCalendar 2.0](https://icalendar.org/) data in plaintext format. Events that you add to the Change Calendar entry become part of the document. You can add events manually in the Change Calendar interface or import events from a supported third-party calendar using an `.ics` file.

------
#### [ Change Manager ]

**Change Manager availability change**  
AWS Systems Manager Change Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Change Manager, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html). 

[Change Manager](change-manager.md) is an enterprise change management framework for requesting, approving, implementing, and reporting on operational changes to your application configuration and infrastructure. From a single *delegated administrator account*, if you use AWS Organizations, you can manage changes across multiple AWS accounts in multiple AWS Regions. Alternatively, using a *local account*, you can manage changes for a single AWS account. Use Change Manager for managing changes to both AWS resources and on-premises resources.

------
#### [ Documents ]

A [Systems Manager document](documents.md) (SSM document) defines the actions that Systems Manager performs. SSM document types include *Command* documents, which are used by State Manager and Run Command, and Automation runbooks, which are used by Systems Manager Automation. Systems Manager includes dozens of pre-configured documents that you can use by specifying parameters at runtime. Documents can be expressed in JSON or YAML, and include steps and parameters that you specify.

------
#### [ Maintenance Windows ]

Use [Maintenance Windows](maintenance-windows.md) to set up recurring schedules for managed instances to run administrative tasks such as installing patches and updates without interrupting business-critical operations. 

------
#### [ Quick Setup ]

Use [Quick Setup](systems-manager-quick-setup.md) to configure frequently used AWS services and features with recommended best practices. You can use Quick Setup in an individual AWS account or across multiple AWS accounts and AWS Regions by integrating with AWS Organizations. Quick Setup simplifies setting up services, including Systems Manager, by automating common or recommended tasks. These tasks include, for example, creating required AWS Identity and Access Management (IAM) instance profile roles and setting up operational best practices, such as periodic patch scans and inventory collection.

------

## Application tools
<a name="systems-manager-application-management"></a>

------
#### [ AppConfig ]

[AppConfig](appconfig.md) helps you create, manage, and deploy application configurations and feature flags. AppConfig supports controlled deployments to applications of any size. You can use AppConfig with applications hosted on Amazon EC2 instances, AWS Lambda containers, mobile applications, or edge devices. To prevent errors when deploying application configurations, AppConfig includes validators. A validator provides a syntactic or semantic check to verify that the configuration you want to deploy works as intended. During a configuration deployment, AppConfig monitors the application to verify that the deployment is successful. If the system encounters an error or if the deployment invokes an alarm, AppConfig rolls back the change to minimize impact for your application users.

------
#### [ Application Manager ]

[Application Manager](application-manager.md) helps DevOps engineers investigate and remediate issues with their AWS resources in the context of their applications and clusters. In Application Manager, an *application* is a logical group of AWS resources that you want to operate as a unit. This logical group can represent different versions of an application, ownership boundaries for operators, or developer environments, to name a few. Application Manager support for container clusters includes both Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon Elastic Container Service (Amazon ECS) clusters. Application Manager aggregates operations information from multiple AWS services and Systems Manager tools to a single AWS Management Console.

------
#### [ Parameter Store ]

[Parameter Store](systems-manager-parameter-store.md) lets you securely store, organize, and retrieve configuration data at scale. It supports a wide range of use cases, from managing plain-text configuration values – such as database connection strings and application settings – to handling sensitive data like secrets for low-risk environments. Parameter Store is designed to simplify configuration management across environments, allowing teams to standardize how applications access critical data without hardcoding values or relying on fragmented storage solutions.

If you manage credentials that require automatic rotation, cross-account access, or fine-grained audit logging, we recommend using [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

------

## Operations tools
<a name="capabilities-operations-management"></a>

------
#### [ CloudWatch Dashboards ]

[Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) are customizable pages in the CloudWatch console that you can use to monitor your resources in a single view, even those resources that are spread across different regions. You can use CloudWatch dashboards to create customized views of the metrics and alarms for your AWS resources. 

------
#### [ Explorer ]

[Explorer](Explorer.md) is a customizable operations dashboard that reports information about your AWS resources. Explorer displays an aggregated view of operations data (OpsData) for your AWS accounts and across AWS Regions. In Explorer, OpsData includes metadata about your Amazon EC2 instances, patch compliance details, and operational work items (OpsItems). Explorer provides context about how OpsItems are distributed across your business units or applications, how they trend over time, and how they vary by category. You can group and filter information in Explorer to focus on items that are relevant to you and that require action. When you identify high priority issues, you can use OpsCenter to run Automation runbooks and resolve those issues. 

------
#### [ Incident Manager ]

[Incident Manager](incident-manager.md) is an incident management console that helps users mitigate and recover from incidents affecting their AWS hosted applications.

Incident Manager increases incident resolution by notifying responders of impact, highlighting relevant troubleshooting data, and providing collaboration tools to get services back up and running. Incident Manager also automates response plans and allows responder team escalation. 

------
#### [ OpsCenter ]

[OpsCenter](OpsCenter.md) provides a central location where operations engineers and IT professionals can view, investigate, and resolve operational work items (OpsItems) related to AWS resources. OpsCenter is designed to reduce mean time to resolution for issues impacting AWS resources. This Systems Manager tool aggregates and standardizes OpsItems across services while providing contextual investigation data about each OpsItem, related OpsItems, and related resources. OpsCenter also provides Systems Manager Automation runbooks that you can use to resolve issues. You can specify searchable, custom data for each OpsItem. You can also view automatically generated summary reports about OpsItems by status and source. 

------
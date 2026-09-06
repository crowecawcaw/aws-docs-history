

# Document history
<a name="doc-history"></a>
+ **Latest documentation update:** December 30, 2025

The following table describes important changes to the *AWS Control Tower User Guide*. For notifications about documentation updates, you can subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Update to managed policy](#doc-history) | Updated [AWSControlTowerServiceRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html). | May 19, 2026 | 
| [Update to managed policy](#doc-history) | Updated [AWSControlTowerAccountServiceRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html). | May 19, 2026 | 
| [Update to managed policy](#doc-history) | Updated [AWSControlTowerAccountServiceRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html). | December 30, 2025 | 
| [AWS Control Tower landing zone version 4.0 with dedicated controls environment](#doc-history) |  AWS Control Tower landing zone version 4.0 is now available with optional service integrations and a dedicated controls environment  | November 17, 2025 | 
| [AWS Control Tower includes additional 279 AWS Config controls](#doc-history) | Updated Control Catalog to include additional 279 AWS Config controls. | November 14, 2025 | 
| [Update to managed policy](#doc-history) | Updated [AWSControlTowerAccountServiceRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html). | November 10, 2025 | 
| [Updated managed policy](#doc-history) | Updated [AWSControlTowerServiceRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerServiceRolePolicy) to support Landing Zone 4.0's optional AWS CloudTrail integration. The Amazon CloudWatch Logs resource pattern changed from `aws-controltower/CloudTrailLogs:*` to `aws-controltower/CloudTrailLogs*:*` to allow management of log groups with unique suffixes. This backward-compatible update enables customers to enable and disable AWS CloudTrail integration multiple times, with log groups recreated with unique suffixes each time to avoid naming conflicts. | November 5, 2025 | 
| [New managed policy](#doc-history) | Added documentation for [AWSControlTowerCloudTrailRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerCloudTrailRolePolicy) managed policy. This managed policy replaces the inline policy previously used by the AWSControlTowerCloudTrailRole, enabling AWS to update the policy without customer intervention. | November 5, 2025 | 
| [AWS Control Tower available in Asia Pacific (New Zealand) Region](#doc-history) | AWS Control Tower is available in the Auckland, New Zealand Region. | October 28, 2025 | 
| [AWS Control Tower supports automatic account enrollment](#doc-history) | Automatic account enrollment and moving between OUs. | October 15, 2025 | 
| [Update to managed policy, new managed policy](#doc-history) | Updated [AWSControlTowerServiceRolePolicy](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html) and added new [AWSControlTowerIdentityCenterManagementPolicy](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html). | October 14, 2025 | 
| [AWS Control Tower updates Python version](#doc-history) | Updated Python versions in AWS Control Tower environments | September 3, 2025 | 
| [AWS Control Tower supports IPv6](#doc-history) | AWS Control Tower adds support for IPv6 endpoints. | August 18, 2025 | 
| [Account Factory for Terraform version 1.15.0](#doc-history) | AFT version 1.15.0 is available. | July 28, 2025 | 
| [Updated controls with Nitro instance types](#doc-history) | Updated eight proactive controls to add new instance types. | July 24, 2025 | 
| [AWS Control Tower available in Asia Pacific (Taipei)](#doc-history) | AWS Control Tower adds support for Asia Pacific (Taipei). | July 23, 2025 | 
| [AWS Control Tower supports AWS PrivateLink](#doc-history) | AWS Control Tower adds support for AWS PrivateLink. | June 30, 2025 | 
| [Service-linked AWS Config controls](#doc-history) | AWS Control Tower deploys service-linked AWS Config controls. | June 12, 2025 | 
| [Enhanced metadata. additional controls, new frameworks](#doc-history) | AWS Control Tower introduces additional integrated controls from AWS Config, with enhanced metadata for all controls in the Control Catalog, and support for more industry frameworks.. | June 12, 2025 | 
| [Enabled controls view](#doc-history) | AWS Control Tower introduces a comprehensive console view of enabled controls. | May 21, 2025 | 
| [AFT supports new configurations](#doc-history) | AWS Control Tower AFT supports three additional optional configurations at deployment. | May 13, 2025 | 
| [Enhanced baselines](#doc-history) | AWS Control Tower now reports baseline drift. | May 12, 2025 | 
| [AWS Control Tower available in AWS Asia Pacific (Thailand) and Mexico (Central) Regions](#doc-history) | The following Regions are available: Asia Pacific (Thailand) and Mexico (Central). | May 9, 2025 | 
| [AWS Control Tower adds 233 AWS Config controls](#doc-history) | Added new Config controls, revamped metadata tables, Region tables, Global identifier page. | April 11, 2025 | 
| [AWS Control Tower updates a service-linked role](#doc-history) | Updates to `AWSControlTowerAccountServiceRolePolicy`. | December 10, 2024 | 
| [AWS Control Tower CfCT supports GitHub](#doc-history) | A new option for a third-party configuration source. | December 9, 2024 | 
| [AWS Control Tower preventive controls with declarative policies](#doc-history) | A new type of policy implements a new type of preventive control. | December 1, 2024 | 
| [AWS Control Tower integrates with AWS Backup](#doc-history) | You can set up plans to back up your AWS Control Tower resources. | November 25, 2024 | 
| [AWS Control Tower integrates AWS Config controls](#doc-history) | AWS Control Tower integrates selected AWS Config controls. | November 21, 2024 | 
| [AWS Control Tower improves hook management](#doc-history) | AWS Control Tower now manages hooks for proactive controls. | November 20, 2024 | 
| [Control policy drift reported](#doc-history) | AWS Control Tower reports a new type of drift. | November 15, 2024 | 
| [AWS Control Tower launches managed resource control policies](#doc-history) | A new type of preventive controls, implemented with RCPs. | November 15, 2024 | 
| [AWS Control Tower adds ResetEnabledControl API](#doc-history) | A new API for managing control drift. | November 14, 2024 | 
| [Updated `GetControl` API](#doc-history) | Two new control fields for `GetControl`. | November 8, 2024 | 
| [AWS Control Tower AFT supports Gitlab](#doc-history) | A new option for a third-party configuration source. | October 23, 2024 | 
| [AWS Control Tower available in AWS Asia Pacific (Malaysia) Region](#doc-history) | A new Region is available, Malaysia (Kuala Lumpur). | October 21, 2024 | 
| [AWS Control Tower supports up to 1000 accounts per OU](#doc-history) | An increase of the limit on accounts per OU.  | August 30, 2024 | 
| [AWS Control Tower adds landing zone version selection](#doc-history) | Update or repair your landing zone without moving to the latest version, if you run 3.1 or newer. | August 15, 2024 | 
| [GetControl and ListControls API operations available](#doc-history) | Two new Control Catalog operations help you find more information about controls. | August 6, 2024 | 
| [AWS Control Tower supports AFT and CfCT in opt-in Regions](#doc-history) | AFT and CfCT are available in additional AWS Regions. | July 18, 2024 | 
| [AWS Control Tower adds the `ListLandingZoneOperations` API](#doc-history) | A new API that allows you to retrieve recent operations for your landing zone. | June 26, 2024 | 
| [AWS Control Tower supports up to 100 concurrent control operations](#doc-history) | An increase of the concurrent control operations quota to 100.  | May 20, 2024 | 
| [AWS Control Tower available in AWS Calgary West (Canada) Region](#doc-history) | AWS Control Tower is available in Canada West (Calgary) Region. | May 3, 2024 | 
| [AWS Control Tower supports self-service quota adjustments](#doc-history) | AWS Control Tower is integrated with AWS Service Quotas in the console. | April 25, 2024 | 
| [Moved documentation for controls to a new guide](#doc-history) | AWS Control Tower published the *Controls Reference Guide*. | April 21, 2024 | 
| [Tagging `EnabledControl` resources in CloudFormation](#doc-history) | AWS Control Tower supports adding tags to `EnabledControl` resources, by means of CloudFormation templates. | February 22, 2024 | 
| [Baseline APIs available](#doc-history) | AWS Control Tower released new APIs for registering OUs programmatically. | February 14, 2024 | 
| [AWS Control Tower landing zone version 3.3](#doc-history) | AWS Control Tower landing zone version 3.3 available. | December 14, 2023 | 
| [AWS Control Tower announces controls to assist digital sovereignty](#doc-history) | AWS Control Tower released a group of controls to help customers with digital sovereignty requirements. | November 27, 2023 | 
| [AWS Control Tower supports landing zone APIs](#doc-history) | AWS Control Tower supports configuring and launching landing zones using new APIs. | November 26, 2023 | 
| [AWS Control Tower supports tagging enabled controls](#doc-history) | AWS Control Tower supports tagging enabled controls, in console and with new APIs. | November 10, 2023 | 
| [AWS Control Tower available in Asia Pacific (Melbourne) AWS Region](#doc-history) | Available in Asia Pacific (Melbourne) Region. | November 3, 2023 | 
| [New control API available](#doc-history) | AWS Control Tower released a new control API. | October 14, 2023 | 
| [AWS Control Tower launches new controls](#doc-history) | AWS Control Tower released new proactive and detective controls. | October 5, 2023 | 
| [AWS Control Tower reports drift from disabling trusted access](#doc-history) |  AWS Control Tower notifies customers when drift occurs, if customers turn off trusted access to AWS Control Tower in AWS Organizations.  | September 21, 2023 | 
| [AWS Control Tower available in four additional AWS Regions](#doc-history) | Available in Asia Pacific (Hyderabad), Europe (Spain and Zurich), and Middle East (UAE). | September 13, 2023 | 
| [AWS Control Tower available in Tel Aviv Region](#doc-history) | AWS Control Tower is available in the Tel Aviv Region, il-central-1. | August 28, 2023 | 
| [AWS Control Tower launches 28 new proactive controls](#doc-history) | AWS Control Tower released 28 new proactive controls. | July 24, 2023 | 
| [AWS Control Tower deprecates 2 controls](#doc-history) | AWS Control Tower will remove two controls from the controls library, effective August 18, 2023. | July 18, 2023 | 
| [AWS Control Tower landing zone 3.2 available](#doc-history) | AWS Control Tower landing zone version 3.2 is available. | June 16, 2023 | 
| [AWS Control Tower handles accounts based on ID](#doc-history) | AWS Control Tower tracks the AWS account ID, rather than the account's email address. | June 14, 2023 | 
| [Additional Security Hub CSPM detective controls available](#doc-history) | AWS Control Tower adds ten new controls to the controls library, for the Security Hub CSPM Service-Managed Standard: AWS Control Tower. | June 12, 2023 | 
| [AWS Control Tower publishes control metadata tables](#doc-history) | AWS Control Tower now provides tables of control metadata as part of the published documentation. | June 7, 2023 | 
| [Terraform support for Account Factory Customization](#doc-history) | Single-region support for Terraform open source blueprints in AFC. | June 6, 2023 | 
| [AWS IAM self-management available for landing zone](#doc-history) | AWS Control Tower now supports customers in choosing their identity provider for a landing zone. | June 6, 2023 | 
| [New role added](#doc-history) | AWS Control Tower added a new service-linked role, **AWSServiceRoleForAWSControlTower**, and associated policy, **AWSControlTowerAccountServiceRolePolicy**. | June 1, 2023 | 
| [Mixed governance update](#doc-history) | Update to advise customers regarding mixed governance. | June 1, 2023 | 
| [Additional proactive controls available](#doc-history) | New proactive controls assist you in governing your multi-account environment and meeting specific control objectives. | May 19, 2023 | 
| [Seven additional Regions available](#doc-history) | AWS Control Tower is now available in seven additional AWS Regions: Northern California (San Francisco), Asia Pacific (Hong Kong, Jakarta, and Osaka), Europe (Milan), Middle East (Bahrain), and Africa (Cape Town). | April 19, 2023 | 
| [Change to a managed policy](#doc-history) | We changed the **AWSControlTowerServiceRolePolicy** so that AWS Control Tower can call the `EnableRegion`, `ListRegions`, `GetRegionOptStatus` APIs that are implemented by the AWS Account Management service.  | April 6, 2023 | 
| [Account customization request tracing generally available](#doc-history) |  AWS Control Tower now supports the ability to trace account customization requests using the Account Factory for Terraform (AFT) workflow.  | February 16, 2023 | 
| [IAM best practices update](#doc-history) | Updated guide to align with the IAM best practices recommendations. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | February 15, 2023 | 
| [AWS Control Tower landing zone 3.1 available](#doc-history) | AWS Control Tower landing zone 3.1 is available. | February 9, 2023 | 
| [Proactive controls generally available](#doc-history) | Proactive controls are launched from preview status to general availability. | January 24, 2023 | 
| [Concurrent account operations](#doc-history) | AWS Control Tower now supports up to five (5) concurrent actions in account factory. You can create, update, or enroll up to five accounts at a time. | December 16, 2022 | 
| [Proactive controls assist in resource provisioning](#doc-history) | AWS Control Tower now supports proactive controls, implemented through CloudFormation hooks. | November 28, 2022 | 
| [Account factory customization available](#doc-history) | AWS Control Tower now supports account provisioning with customizable account templates, called blueprints, directly from the AWS Control Tower console. | November 28, 2022 | 
| [Compliance status viewable for all AWS Config rules](#doc-history) | AWS Control Tower now displays the compliance status of all AWS Config rules deployed into organizational units registered with AWS Control Tower. | November 18, 2022 | 
| [Change to a managed policy](#doc-history) | We changed the **AWSControlTowerServiceRolePolicy** so that AWS Control Tower can assume the `AWSControlTowerBlueprintAccess` role, which is needed for Account Factory customizations.  | October 28, 2022 | 
| [APIs for controls, CloudFormation resource](#doc-history) | AWS Control Tower now supports activation and deactivation of controls through a set of API calls, and a new CloudFormation resource. | September 1, 2022 | 
| [CfCT supports stack set deletion](#doc-history) | CfCT supports stack set deletion, by setting a parameter in the manifest file. | August 26, 2022 | 
| [Customized log retention](#doc-history) | You can customize the retention policy for Amazon S3 buckets that store your AWS Control Tower CloudTrail logs, in increments of days or years, up to a maximum of 15 years. | August 15, 2022 | 
| [Role drift repair available](#doc-history) | AWS Control Tower supports repair for role drift, without a full repair of the landing zone. | August 11, 2022 | 
| [Version 3.0 available](#doc-history) | AWS Control Tower landing zone version 3.0 changes from account-based AWS CloudTrail trails to organization-based trails, and it updates the managed policy to enable organization-level trails. It enables you to aggregate AWS Config information in your home Region only. Version 3.0 also includes an update to the Region deny control, and two new detective controls. | July 29, 2022 | 
| [The Organization page combines views of OUs and accounts](#doc-history) | The new **Organization** page in AWS Control Tower shows a hierarchical view of all Organizational units (OUs) and accounts.  | July 18, 2022 | 
| [Change to a managed policy](#doc-history) | We changed the **AWSControlTowerServiceRolePolicy** so that customers can have organization-level AWS CloudTrail trails to aggregate AWS CloudTrail logs. | June 20, 2022 | 
| [Easier enroll and update for member accounts](#doc-history) | AWS Control Tower now gives you the capability to to enroll and update member accounts individually, from within your landing zone. Each account shows when it is available for an update. We separated the **Enroll account** button from the **Create** account workflow in Account Factory. | May 31, 2022 | 
| [AFT supports customization for shared accounts](#doc-history) | AWS Control Tower Account Factory for Terraform now supports customization for the AWS Control Tower management account, log archive, and audit accounts. | May 27, 2022 | 
| [Concurrent operations for all optional controls](#doc-history) |  AWS Control Tower now allows you to apply and remove optional preventive guardails concurrently, as well as detective controls. | May 18, 2022 | 
| [Existing security and logging accounts](#doc-history) | AWS Control Tower now supports the ability to bring existing security and logging accounts, rather than creating new ones during landing zone setup. | May 16, 2022 | 
| [Version 2.9 available](#doc-history) | AWS Control Tower landing zone version 2.9 updates the notification forwarder Lambda to use the Python version 3.9 runtime. | April 22, 2022 | 
| [Updated support for AWS best practices, version 2.8 available](#doc-history) | AWS Control Tower landing zone version 2.8 provides additional support to ensure that your workloads and AWS accounts are in alignment with AWS best practices. | February 10, 2022 | 
| [Region deny control](#doc-history) | AWS Control Tower now includes a control that helps you restrict access to AWS Regions, to address compliance and regulatory concerns. | November 30, 2021 | 
| [Data residency controls](#doc-history) | AWS Control Tower now support controls that help you manage data residency with granular control. | November 30, 2021 | 
| [AWS Control Tower Account factory for Terraform](#doc-history) | AWS Control Tower now supports Terraform for automated account provisioning and updating. | November 29, 2021 | 
| [New lifecycle event available](#doc-history) | The `PrecheckOrganizationalUnit` event logs whether any resources block the **Extend governance** task from success, including resources in nested OUs. | November 18, 2021 | 
| [Nested OUs available](#doc-history) | AWS Control Tower now enables your landing zone to contain nested OU structures. | November 16, 2021 | 
| [Detective control concurrency](#doc-history) | AWS Control Tower detective controls now support concurrent enable and disable operations. | November 5, 2021 | 
| [Two new regions available](#doc-history) | AWS Control Tower is now available in two new AWS Regions, Europe (Paris) Region and South America (São Paulo) Region. | July 29, 2021 | 
| [Region deselection](#doc-history) | You can deselect AWS Regions that you no longer wish to govern through AWS Control Tower. | July 29, 2021 | 
| [KMS keys available](#doc-history) | You can optionally create or choose KMS keys that you manage, to encrypt your data and resources. | July 28, 2021 | 
| [Change to a managed policy](#doc-history) | We changed the **AWSControlTowerServiceRolePolicy** so that customers can use their own KMS encryption keys for AWS CloudTrail logs. | July 28, 2021 | 
| [Control names changed, functionality unchanged](#doc-history) | Certain control names and descriptions were updated to better reflect the policy intentions of the control, with no change in functionality. | July 26, 2021 | 
| [Automated scans of managed SCPs](#doc-history) | AWS Control Tower performs daily automated scans of managed SCPs to check for drift. | May 11, 2021 | 
| [Customized names for OUs and accounts](#doc-history) | AWS Control Tower allows you to provide customized names during the landing zone setup process, for essential OUs and accounts, without creating drift. | April 16, 2021 | 
| [Decommissioning a landing zone is self-service](#doc-history) |  AWS Control Tower now allows you to decommission a landing zone without contacting AWS Support. Decommissioning is a semi-automated process that cannot be undone. It is not the same as deleting all AWS Control Tower resources manually. | April 9, 2021 | 
| [Three additional Regions](#doc-history) | AWS Control Tower is now available in three additional AWS Regions: Asia Pacific (Tokyo) Region, Asia Pacific (Seoul) Region, and Asia Pacific (Mumbai) Region. | April 8, 2021 | 
| [New Log Archive controls, landing zone version 2.7 available](#doc-history) | Four new Log Archive controls provide Log Archive governance over AWS Control Tower resources, separately from governance of resources outside of AWS Control Tower. Guidance on four existing controls has changed from mandatory to elective. Version 2.7 of the AWS Control Tower landing zone includes a requirement for HTTPS, which cannot be undone after you update. | April 8, 2021 | 
| [Region selection](#doc-history) | AWS Control Tower Region selection provides better ability to manage the geographical footprint of your AWS Control Tower resources. To expand the number of Regions in which you host AWS resources or workloads – for compliance, regulatory, cost, or other reasons – you can now select the additional Regions to govern. | February 19, 2021 | 
| [Register an OU and govern all of its accounts with AWS Control Tower at one time](#doc-history) | AWS Control Tower adds the capability to register an OU, which is a way to bring multiple accounts into governance at the same time. | January 28, 2021 | 
| [Multiple account updates in registered OUs](#doc-history) | You can now update all accounts in any registered AWS Organizations organizational unit (OU) containing up to 300 accounts, with a single click, from the AWS Control Tower dashboard. The multiple account update feature, also referred to as bulk update, eliminates the need to update one account at a time, or to use an external script to perform the update on multiple accounts together. | January 28, 2021 | 
| [New role for aggregating unmanaged OUs and accounts](#doc-history) | A new role assists in detecting external AWS Config rules, so AWS Control Tower does not need to gain access to unmanaged accounts. | December 29, 2020 | 
| [AWS Control Tower is available in more AWS Regions.](#doc-history) | AWS Control Tower is now available to be deployed in the Asia Pacific (Singapore) Region, Europe (Frankfurt) Region, Europe (London) Region, Europe (Stockholm) Region, and Canada (Central) Region. With this launch AWS Control Tower is now available in 10 AWS Regions. This landing zone update includes all Regions listed, and it cannot be undone. After updating your landing zone to version 2.5, you must manually update all enrolled accounts for AWS Control Tower to govern in the 10 supported AWS Regions. | November 18, 2020 | 
| [Control update](#doc-history) | An updated version has been released for the mandatory control `AWS-GR_IAM_ROLE_CHANGE_PROHIBITED`. The updated control allows easier automated enrollment of accounts. | October 8, 2020 | 
| [Related information page is now available for AWS Control Tower](#doc-history) | The related information page makes it easier to find common tasks that may be helpful after setting up your AWS Control Tower landing zone. | September 18, 2020 | 
| [AWS Control Tower console shows more detail about OUs and accounts.](#doc-history) | Within the AWS Control Tower console, you can view more detail about your AWS accounts and organizational units (OUs). The ‘Accounts’ page now lists all accounts in your organization, regardless of OU or enrollment status in AWS Control Tower. You can now search, sort, and filter across all tables. | July 22, 2020 | 
| [AWS Control Tower allows existing organizations to set up a landing zone](#doc-history) | You can now launch a landing zone for AWS Control Tower in an existing organization, to bring the organization into governance. The **Quick account provisioning** capability in AWS Control Tower was renamed to **Enroll account** and it now permits enrollment of existing AWS accounts as well as creation of new accounts. | April 16, 2020 | 
| [AWS Control Tower is now available in Asia Pacific](#doc-history) | AWS Control Tower is now available to be deployed in the Asia Pacific (Sydney) AWS Region. This release requires manual updates to vended accounts, update only if you plan to run workloads in Asia Pacific (Sydney).  | March 3, 2020 | 
| [Decommissioning an AWS Control Tower landing zone is possible](#doc-history) | AWS Support can help you permanently decommission a landing zone through a mostly automated process that preserves your organizations, although some manual cleanup is required. | February 27, 2020 | 
| [Quick account provisioning is available in AWS Control Tower](#doc-history) | Quick account provisioning makes it easier to launch new member accounts when your landing zone is up to date, with the **Enroll account** feature. | February 20, 2020 | 
| [Lifecycle events are tracked in AWS Control Tower](#doc-history) | Lifecycle events provide additional details for certain AWS Control Tower events, to make some workflow automation easier. | December 12, 2019 | 
| [Settings and Activities pages are available for AWS Control Tower](#doc-history) | The Settings and Activities pages make it easier to update your landing zone and to view logged events. | November 30, 2019 | 
| [Additional preventive controls are available for AWS Control Tower](#doc-history) | Preventive controls in AWS Control Tower keep your organization and resources aligned with your environment.  | September 6, 2019 | 
| [Additional detective controls are available for AWS Control Tower](#doc-history) | Detective controls in AWS Control Tower give information about the state of your organization and resources.  | August 27, 2019 | 
| [AWS Control Tower is now generally available](#doc-history) | AWS Control Tower is a service that offers the easiest way to set up and govern your multi-account AWS environment at scale. | June 24, 2019 | 
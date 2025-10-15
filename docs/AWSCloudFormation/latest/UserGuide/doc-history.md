# Document history for the AWS CloudFormation User Guide

The following table describes important changes to the AWS CloudFormation User Guide content after May
 2018. To receive notifications about documentation updates, you can subscribe to an RSS
 feed.

###### Important

The table rows describing updates to the template reference content from May 2018 onward
 have moved to the new *AWS CloudFormation Template Reference*. For these updates
 and any future changes, see the [Document history for the AWS CloudFormation Template
 Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/doc-history.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/doc-history.html") in the *AWS CloudFormation Template Reference*.



| Change | Description | Date |
| --- | --- | --- |
| PDF guide available | You can now download the *AWS CloudFormation User Guide* as a PDF. | May 30, 2025 |
| Moved template reference content to a new guide | CloudFormation published the *AWS CloudFormation Template Reference Guide*. For
 details, see [The AWS CloudFormation Template Reference Guide](link-to-reference-guide.md "link-to-reference-guide.md"). | May 30, 2025 |
| IaC generator supports partial scanning | You can now choose specific resource types to scan for, making it easier to
 generate Infrastructure-as-Code (IaC) templates from your existing resources. For
 more information, see [Start a resource scan with
 CloudFormation IaC generator](iac-generator-start-resource-scan.md "iac-generator-start-resource-scan.md"). | March 27, 2025 |
| Stack refactoring | Stack refactoring simplifies reorganizing the resources in your CloudFormation stacks
 while still preserving the existing resource properties and data. For more
 information, see [Stack refactoring](stack-refactoring.md "stack-refactoring.md"). | February 6, 2025 |
| Troubleshoot stack deployments with Amazon Q Developer | You can now use Amazon Q Developer to troubleshoot common errors when deploying CloudFormation
 stacks. For more information, see [Troubleshoot unsuccessful
 CloudFormation stack deployments with Amazon Q Developer](cfn-troubleshooting-with-amazon-q.md "cfn-troubleshooting-with-amazon-q.md"). | November 22, 2024 |
| Stack deployment timeline graph | You can now see a visual representation of your stack deployment. The stack
 deployment timeline graph shows the stack deployment status, individual resource
 deployment statuses, and the times the deployment statuses changed. For more
 information, see [View a timeline of a
 CloudFormation stack deployment](stack-deployment-timeline-graph.md "stack-deployment-timeline-graph.md"). | November 11, 2024 |
| Visualize your scanned resources and generated templates | You can now streamline your Infrastructure as Code (IaC) generator workflows by
 visualizing scan summary details and previewing the generated templates before
 deploying your infrastructure stack. For more information, see [View the
 scan summary in the CloudFormation console](generate-IaC-view-scan-summary.md "generate-IaC-view-scan-summary.md") and [Create a
 CloudFormation stack from scanned resources](iac-generator-create-stack-from-scanned-resources.md "iac-generator-create-stack-from-scanned-resources.md"). | August 22, 2024 |
| Amazon EventBridge integration with AWS CloudFormation Git sync | AWS CloudFormation Git sync now publishes sync status changes as events to Amazon EventBridge. For more
 information, see [Repository Sync
 Status Change event detail](event-detail-respository-sync-status-change.md "event-detail-respository-sync-status-change.md") and [Resource Sync Status
 Change event detail](event-detail-resource-sync-status-change.md "event-detail-resource-sync-status-change.md"). | July 29, 2024 |
| Force delete stuck stacks | Two new options to force delete stacks is available for stack deletion operations
 that are stuck. You can now choose to force delete the stack but retain the resource,
 or the force delete the entire stack. For more information, see [Delete a stack
 from the CloudFormation console](cfn-console-delete-stack.md "cfn-console-delete-stack.md"). | May 22, 2024 |
| AWS CloudTrail event stack operation root causes | CloudFormation improves the troubleshooting experience for stack operations with a new
 AWS CloudTrail deep-link integration. This feature directly links stack operation events in
 the CloudFormation console to relevant CloudTrail events. For more information, see [Determine the cause of a stack failure](determine-root-cause-for-stack-failures.md "determine-root-cause-for-stack-failures.md"). | May 15, 2024 |
| Property level change sets | Property level change sets allow you to preview the changes that CloudFormation
 deployments will make to the property values of resources. For more information, see
 [View a change set
 for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md "using-cfn-updating-stacks-changesets-view.md"). | April 12, 2024 |
| CloudFormation introduces the CONFIGURATION\_COMPLETE event | You can now use the `CONFIGURATION_COMPLETE` event to enable faster
 workflows involving the creation of resources. For more information, see [Understand CloudFormation stack creation events](stack-resource-configuration-complete.md "stack-resource-configuration-complete.md"). | March 11, 2024 |
| Generate AWS CloudFormation templates and AWS CDK applications from existing AWS
 resources | You can now generate a template using resources provisioned in your account that
 are not already managed by CloudFormation. For more information, see [Generate templates from
 existing resources with IaC generator](generate-IaC.md "generate-IaC.md"). | February 2, 2024 |
| StackSets concurrency mode | Concurrency Mode is a parameter for `StackSetOperationPreferences` that
 allows you to choose how the concurrency level behaves during stack set operations.
 For more information, see [Choose the Concurrency Mode for CloudFormation
 StackSets](concurrency-mode.md "concurrency-mode.md"). | November 9, 2023 |
| Detailed StackSet drift information | The following APIs allow you to see which stack instances have drifted from the
 StackSet template and which resources have drifted.


[ListStackInstanceResourceDrifts](../APIReference/API_ListStackInstanceResourceDrifts.md "../APIReference/API_ListStackInstanceResourceDrifts.md")


Returns drift information for resources in a stack instance.


[StackInstanceResourceDriftsSummary](../APIReference/API_StackInstanceResourceDriftsSummary.md "../APIReference/API_StackInstanceResourceDriftsSummary.md")


The structure containing summary information about resource drifts for
 a stack instance.

 | July 24, 2023 |
| CloudFormation StackSets APIs to control AWS Organizations trust access | CloudFormation StackSets provides customers with the following APIs for managing
 AWS Organizations trust access:


[ActivateOrganizationsAccess](../APIReference/API_ActivateOrganizationsAccess.md "../APIReference/API_ActivateOrganizationsAccess.md")


Activate trusted access with AWS Organizations. With trusted access between
 StackSets and Organizations activated, the management account has permissions to
 create and manage StackSets for your organization.


[DeactivateOrganizationsAccess](../APIReference/API_DeactivateOrganizationsAccess.md "../APIReference/API_DeactivateOrganizationsAccess.md")


Deactivates trusted access with AWS Organizations. If trusted access is
 deactivated, the management account does not have permissions to create
 and manage service-managed StackSets for your organization.


[DescribeOrganizationsAccess](../APIReference/API_DescribeOrganizationsAccess.md "../APIReference/API_DescribeOrganizationsAccess.md")


Retrieves information about the account's
 `OrganizationAccess` status. This API can be called either
 by the management account or the delegated administrator by using the
 `CallAs` parameter. This API can also be called without the
 `CallAs` parameter by the management account.

 | June 5, 2023 |
| DescribeStackSet API | The `DescribeStackSet` API has a new parameter to the list of
 Regions where a given stack set is deployed. For more information,
 see [DescribeStackSet](../APIReference/API_DescribeStackSet.md "../APIReference/API_DescribeStackSet.md"). | February 1, 2023 |
| Managing StackSets events with CloudFormation and Amazon EventBridge | CloudFormation StackSets launch event notifications via Amazon EventBridge. You can trigger
 event-driven actions after creating, updating, or deleting your CloudFormation stack
 sets. For more information, see [Monitoring CloudFormation and Git
 sync events with EventBridge](eventbridge-integration.md "eventbridge-integration.md"). | November 16, 2022 |
| Improved insights on stack instances for stack set operations | CloudFormation StackSets provides more detailed information on stack instances for
 stack set operations:


[DescribeStackSetOperation](../APIReference/API_DescribeStackSetOperation.md "../APIReference/API_DescribeStackSetOperation.md")


You can now use `DescribeStackSetOperation` to provide the
 count of failed stack instances for stack set operations during
 deployment.


[ListStackInstances](../APIReference/API_ListStackInstances.md "../APIReference/API_ListStackInstances.md")


You can now use the filtering option `LastOperationID` to
 list stack instances for stack set operations.

 | November 4, 2022 |
| Managing events with CloudFormation and Amazon EventBridge | Receive notifications when specific CloudFormation events occur. For more information,
 see [Monitoring CloudFormation and Git sync events with EventBridge](eventbridge-integration.md "eventbridge-integration.md"). | July 20, 2022 |
| Account level | CloudFormation announces the general availability of *account filter
 type*, a feature that allows customers to limit deployment targets to
 individual accounts or include additional accounts with provided OUs. For more
 information, see [Account level targets for
 service-managed StackSets](account-level-targets.md "account-level-targets.md"). | July 7, 2022 |
| CloudFormation registry | CloudFormation announces the general availability of *Hooks*, a
 feature that allows customers to invoke custom logic to automate actions or inspect
 resource configurations prior to a create, update or delete stack operation. For more
 information, see the [AWS CloudFormation Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html "https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html"). | February 10, 2022 |
| Stack failure options | You can iteratively develop your applications when provisioning failures are
 encountered by starting from the point of failure without rolling back successfully
 provisioned resources. By specifying stack failure options, you can troubleshoot
 resources in a `CREATE_FAILED` or `UPDATE_FAILED` status. You
 can provision failure options for all stack deployments and change set operations.
 For more information, see [Choose how to handle failures when
 provisioning resources](stack-failure-options.md "stack-failure-options.md"). | August 30, 2021 |
| Import stacks to stack set | You can now import existing stacks into new or existing stack sets. For more
 information, see [Importing stacks into CloudFormation StackSets](stacksets-import.md "stacksets-import.md"). | July 28, 2021 |
| Increased quota | You can now declare a defaulted maximum of `2000` stacks in your
 AWS account. For more information, see [Understand CloudFormation
 quotas](cloudformation-limits.md "cloudformation-limits.md"). | July 15, 2021 |
| Publish public third-party extensions | You can now use public extensions provided by third-party publishers, just as you
 would extensions from AWS. For more information, see [Use third-party public extensions from the
 CloudFormation registry](registry-public.md "registry-public.md"). | June 21, 2021 |
| Reference macros in stack set templates | StackSets now supports creating or updating stack sets with self-managed
 permissions from templates that reference macros. For more information about macros,
 see [Perform custom
 processing on CloudFormation templates with template macros](template-macros.md "template-macros.md"). | April 14, 2021 |
| Use the latest value of a Systems Manager parameter in a dynamic reference | You can now have CloudFormation use the latest version of an Systems Manager parameter whenever
 you create or update a stack. You are no longer required to specify a specific
 version. For more details, see [Get a plaintext value from Systems Manager
 Parameter Store](dynamic-references-ssm.md "dynamic-references-ssm.md"). | April 13, 2021 |
| Modules support using period delimiters in resource names | You can now use a period as a delimiter in specifying the fully-qualified logical
 name for a resource contained in a module. For more information, see [Reference module
 resources in CloudFormation templates](module-ref-resources.md "module-ref-resources.md"). | April 8, 2021 |
| CloudFormation StackSets now supports parallel region deployment | You can now choose to deploy StackSets into Regions sequentially or in parallel.
 For more information, see [Stack set operation
 options](what-is-cfnstacksets.md#stackset-ops-options "what-is-cfnstacksets.md#stackset-ops-options"). | April 6, 2021 |
| CloudFormation StackSets now supports delegated administrator with AWS Organizations | In addition to the organization's management account, delegated administrator
 accounts can create and manage stack sets with service-managed permissions for their
 organization. For more information, see [Register a delegated
 administrator member account](stacksets-orgs-delegated-admin.md "stacksets-orgs-delegated-admin.md") and [Create CloudFormation
 StackSets with service-managed permissions](stacksets-orgs-associate-stackset-with-org.md "stacksets-orgs-associate-stackset-with-org.md"). | February 18, 2021 |
| CloudFormation StackSets Region availability | CloudFormation StackSets is now available in the Asia Pacific (Osaka) Region. For
 more information, see [Managing stacks across accounts and
 Regions with StackSets](what-is-cfnstacksets.md "what-is-cfnstacksets.md"). | February 10, 2021 |
| Modules | Modules are a way for you to package resource configurations for inclusion across
 stack templates, in a transparent, manageable, and repeatable way. Modules can
 encapsulate common service configurations and best practices as modular, customizable
 building blocks for you to include in your stack templates. For more information, see
 [Create reusable resource
 configurations that can be included across templates with CloudFormation
 modules](modules.md "modules.md"). | November 24, 2020 |
| Change sets for nested stacks | With change sets for nested stacks you can preview the changes to your application
 and infrastructure resources across the entire nested stack hierarchy and proceed
 with updates when you've confirmed that all the changes are as intended. For more
 information, see [Change sets for nested
 stacks](change-sets-for-nested-stacks.md "change-sets-for-nested-stacks.md"). | November 18, 2020 |
| Increased quotas | The following AWS CloudFormation quotas have been updated.
* You can now declare a maximum of `200` mappings in your
 AWS CloudFormation template.
* You can now declare a maximum of `200` mapping attributes for
 each mapping in your AWS CloudFormation template.
* You can now declare a maximum of `200` outputs in your
 AWS CloudFormation template.
* You can now declare a maximum of `200` parameters in your
 AWS CloudFormation template.
* You can now declare a maximum of `500` resources in your
 AWS CloudFormation template.
* You can now pass a template body with a maximum size of `1 MB`
 in an Amazon S3 object.
 | October 22, 2020 |
| Drift detection for private resources | CloudFormation now supports drift detection operations on an expanded list of AWS
 resources, as well as private resources that are defined as provisonable in the
 CloudFormation registry. For more information, see [Resource type
 support](resource-import-supported-resources.md "resource-import-supported-resources.md"). | October 1, 2020 |
| Updated permissions required for registering resource providers | Registering a resource provider in your account now requires you have permission
 to access the schema handler package uploaded to an S3 bucket for that resource
 provider. For more information, see [IAM
 permissions for registering a third-party private extension](registry-private.md#registry-register-permissions "registry-private.md#registry-register-permissions"). | August 7, 2020 |
| Resource import supports provisionable private resource types | Import operations now support private resource types that are
 *provisionable*; that is, whose provisioning type is either
 `FULLY_MUTABLE` or `IMMUTABLE`. For more information, see
 [Resources that support
 import operations](resource-import-supported-resources.md "resource-import-supported-resources.md"). | June 3, 2020 |
| ECS blue/green deployments through CodeDeploy | You can now use CloudFormation to perform ECS blue/green deployments through CodeDeploy.
 Blue/green deployments are a safe deployment strategy provided by AWS CodeDeploy for
 minimizing interruptions caused by changing application versions. For more
 information, see [Performing ECS blue/green deployments through CodeDeploy using
 CloudFormation](blue-green.md "blue-green.md"). | May 19, 2020 |
| CloudFormation StackSets Region availability | CloudFormation StackSets is now available in the AWS GovCloud (US-West)
 Region. | May 18, 2020 |
| AWS CloudFormation StackSets integrates with AWS Organizations | You can now use StackSets to centrally manage deployments to all the accounts in
 your organization or specific organizational units (OUs) in AWS Organizations. You can enable
 automatic deployments to any new accounts added to your organization or OUs. The
 permissions needed to deploy across accounts will automatically be handled by
 StackSets. For more information, see [Managing stacks across accounts and
 Regions with StackSets](what-is-cfnstacksets.md "what-is-cfnstacksets.md"). | February 11, 2020 |
| Drift Detection for StackSets | You can now run drift detection on a stack set and all the stack instances it
 includes. For more information, see [Performing drift detection on CloudFormation
 StackSets](stacksets-drift.md "stacksets-drift.md"). | November 19, 2019 |
| CloudFormation registry now available | You can now use the CloudFormation console to view private and public resources that
 are available for use in your account. For more information, see [View the available and
 activated extensions in the CloudFormation registry](registry-view.md "registry-view.md"). | November 18, 2019 |
| CloudFormation registry API actions | The following API actions for managing types in the CloudFormation registry are now
 available.


[DeregisterType](../APIReference/API_DeregisterType.md "../APIReference/API_DeregisterType.md")


Removes a type or type version from active use in the CloudFormation
 registry.


[DescribeType](../APIReference/API_DescribeType.md "../APIReference/API_DescribeType.md")


Returns detailed information about a registered type.


[DescribeTypeRegistration](../APIReference/API_DescribeTypeRegistration.md "../APIReference/API_DescribeTypeRegistration.md")


Returns information about a type's registration, including its current
 status and type and version identifiers.


[ListTypeRegistrations](../APIReference/API_ListTypeRegistrations.md "../APIReference/API_ListTypeRegistrations.md")


Returns a list of registration request identifiers for the specified
 type.


[ListTypes](../APIReference/API_ListTypes.md "../APIReference/API_ListTypes.md")


Returns summary information about types that have been registered with
 CloudFormation.


[ListTypeVersions](../APIReference/API_ListTypeVersions.md "../APIReference/API_ListTypeVersions.md")


Returns summary information about the versions of a type.


[RegisterType](../APIReference/API_RegisterType.md "../APIReference/API_RegisterType.md")


Registers a type with the CloudFormation registry. Registering a type
 makes it available for use in CloudFormation templates in your
 AWS account.


[SetTypeDefaultVersion](../APIReference/API_SetTypeDefaultVersion.md "../APIReference/API_SetTypeDefaultVersion.md")


Specify the default version of a type. The default version of a type
 will be used in CloudFormation operations.

For more information about the CloudFormation registry, see [Managing extensions with the
 CloudFormation registry](registry.md "registry.md") | November 18, 2019 |
| Resource import added | If you created an AWS resource outside of CloudFormation management, you can bring
 this existing resource into CloudFormation management using `resource import`.
 For more information, see [Import AWS resources into a CloudFormation
 stack with a resource import](resource-import.md "resource-import.md"). | November 11, 2019 |
| Stack set limit increases | You can now create a maximum of 100 stack sets in your administrator account,
 create a maximum of 2000 stack instances per stack set, and run a maximum of 3500
 stack instance operations in each region at the same time, per administrator account.
 For more information, see [Understand CloudFormation
 quotas](cloudformation-limits.md "cloudformation-limits.md"). | August 2, 2019 |
| Limit for resources in concurrent stack operations  | CloudFormation now enforces an account limit for the number of resources in concurrent
 stack operations. This limit is determined by region. For more information, see
 [Understand
 CloudFormation quotas](cloudformation-limits.md "cloudformation-limits.md"). | April 30, 2019 |
| Stack instance operation limit | For StackSets, you can now have a maximum of 1500 stack instance operations
 running in a given region at the same time, per administrator account. For more
 information, see [Understand CloudFormation
 quotas](cloudformation-limits.md "cloudformation-limits.md"). | December 13, 2018 |
| The CAPABILITY\_AUTO\_EXPAND capability is now available | You can now use the `CAPABILITY_AUTO_EXPAND` capability to create or
 update a stack directly from a stack template that contains macros, without first
 reviewing the resulting changes in a change set first. For more information, see
 [CreateStack](../APIReference/API_CreateStack.md "../APIReference/API_CreateStack.md")
 or [UpdateStack](../APIReference/API_UpdateStack.md "../APIReference/API_UpdateStack.md")
 in *AWS CloudFormation API Reference*. | December 7, 2018 |
| Stack drift detection added | You can now detect whether a stack's actual configuration has drifted from its
 expected template configuration as defined within CloudFormation. You can detect drift on
 an entire stack, or individual stack resources. For more information, see [Detect unmanaged
 configuration changes to stacks and resources with drift detection](using-cfn-stack-drift.md "using-cfn-stack-drift.md"). | November 13, 2018 |
| secretsmanager dynamic reference now available | You can now use the `secretsmanager` dynamic reference to retrieve
 entire secrets or secret values that are stored in AWS Secrets Manager. Secrets can be database
 credentials, passwords, third-party API keys, and even arbitrary text. Using the
 `secretsmanager` dynamic reference guarantees that neither Secrets Manager nor
 CloudFormation logs or persists any resolved secret value. For more information, see
 [Get a secret or secret value from Secrets Manager](dynamic-references-secretsmanager.md "dynamic-references-secretsmanager.md"). | November 9, 2018 |
| Macros now available | You can now use macros to perform custom processing on templates, from simple
 actions like find-and-replace operations to extensive transformations of entire
 templates. For more information, see [Perform custom processing on CloudFormation
 templates with template macros](template-macros.md "template-macros.md"). | September 6, 2018 |
| CloudFormation now supports VPC endpoints powered by PrivateLink | You can use a VPC endpoint to create a private connection between your VPC and
 CloudFormation without requiring access over the Internet, through a NAT instance, a VPN
 connection, or AWS Direct Connect. For more information, see [Access CloudFormation using an interface
 endpoint (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md"). | August 22, 2018 |
| Dynamic references support secure strings | You can now use new dynamic references to specify values that are stored and
 managed in other services, including Systems Manager Parameter Store `SecureString`
 type parameters, in your stack templates. For more information, see [Get a secure string value from Systems Manager Parameter Store](dynamic-references-ssm-secure-strings.md "dynamic-references-ssm-secure-strings.md"). | August 16, 2018 |
| Stack sets now support customized execution roles | You can now use customized execution roles in target accounts to control the stack
 resources that users or groups can include in their stack sets. For more information,
 see [Set up advanced permissions options for stack set operations](stacksets-prereqs-self-managed.md#stacksets-prereqs-advanced-perms "stacksets-prereqs-self-managed.md#stacksets-prereqs-advanced-perms"). | May 30, 2018 |
| Selective updates of stack instances | You can now use the optional `Accounts` and `Regions`
 parameters to specify the accounts and regions in which to update stack instances
 during a stack set update operation. For more information, see [UpdateStackSet](../APIReference/API_UpdateStackSet.md "../APIReference/API_UpdateStackSet.md")
 in the *AWS CloudFormation API Reference*. | May 30, 2018 |
| CloudFormation now creates S3 buckets with encryption enabled | For Amazon S3 buckets that CloudFormation creates to store uploaded stack templates,
 server-side encryption is now enabled by default, thereby encrypting all objects
 stored in those buckets. For more information, see [Create a stack from the CloudFormation
 console](cfn-console-create-stack.md "cfn-console-create-stack.md"). | May 24, 2018 |
| FIPS endpoints added | CloudFormation now offers new endpoints which use FIPS 140-2 validated cryptographic
 modules in the following public US regions: US-East-1, US-East-2, US-West-1, and
 US-West-2. See [AWS CloudFormation endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/cfn.html "https://docs.aws.amazon.com/general/latest/gr/cfn.html")
 in the *Amazon Web Services General Reference* for the new FIPS-compliant endpoint
 URLs. | May 17, 2018 |

For updates to the *AWS CloudFormation Hooks User Guide*, see [Document history for the AWS CloudFormation Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/doc-history.html "https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/doc-history.html") in the *AWS CloudFormation Hooks User
 Guide*.


## Archived updates


The following table describes important changes in each release of the AWS CloudFormation User Guide
 before May 2018.




| Change | Release Date | Description | API Version |
| --- | --- | --- | --- |
| Updated resources | July 22, 2019 | Use the `encryptionOptions` property to specify an
 AWS owned key or a customer managed key for Amazon MQ brokers. | 2010-05-15 |
| Stack set naming convention | April 10, 2018 | CloudFormation stacks created using stack sets now follow a new naming
 convention, in which the stack name contains the stack set name. | 2010-05-15 |
| New resources | April 10, 2018 | 

[AWS::AppSync::ApiKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-apikey.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-apikey.html")

Use the `AWS::AppSync::ApiKey` resource to create a
 unique key that you can distribute to clients who are executing
 GraphQL operations with AWS AppSync.

[AWS::AppSync::DataSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-datasource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-datasource.html")

Use the `AWS::AppSync::DataSource` resource to create
 data sources for resolvers in AWS AppSync.

[AWS::AppSync::GraphQLApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-graphqlapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-graphqlapi.html")

Use the `AWS::AppSync::GraphQLApi` resource to create
 a new AWS AppSync GraphQL API.

[AWS::AppSync::GraphQLSchema](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-graphqlschema.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-graphqlschema.html")

Use the `AWS::AppSync::GraphQLSchema` resource to
 create the data model for your AWS AppSync GraphQL API.

[AWS::AppSync::Resolver](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-resolver.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-resolver.html")

Use the `AWS::AppSync::Resolver` resource to define
 the logical GraphQL resolver that you will attach to fields in a
 schema.

 | 2010-05-15 |
| Updated resource | April 10, 2018 | 

[AWS::Config::ConfigurationAggregator](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationaggregator.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationaggregator.html")

Use the `OrganizationAggregationSource` property type
 to specify the regions of AWS Config data to aggregate into an
 AWS Config configuration aggregator and the IAM role to use to
 retrieve AWS Organizations details.

 | 2010-05-15 |
| New resources | April 4, 2018 | 

[AWS::Config::AggregationAuthorization](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-aggregationauthorization.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-aggregationauthorization.html")

Use the `AWS::Config::AggregationAuthorization`
 resource to grant permission to an aggregator account to collect
 your AWS Config data.

[AWS::Config::ConfigurationAggregator](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationaggregator.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationaggregator.html")

Use the `AWS::Config::ConfigurationAggregator`
 resource to create a configuration aggregator for AWS Config.

 | 2010-05-15 |
| Stack sets now support customized administrator roles | March 29, 2018 | Use customized administrator roles to control which users or groups can
 manage specific stack sets within the same administrator account. For more
 information, see [Set up advanced permissions options for stack set
 operations](stacksets-prereqs-self-managed.md#stacksets-prereqs-advanced-perms "stacksets-prereqs-self-managed.md#stacksets-prereqs-advanced-perms"). | 2010-05-15 |
| New resource | March 29, 2018 | 

[AWS::EC2::LaunchTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-launchtemplate.html")

Use the `AWS::EC2::LaunchTemplate` resource to create
 a launch template for an Amazon EC2 instance.

 | 2010-05-15 |
| Updated resources | March 29, 2018 | 

[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")

Use the `LaunchTemplate` property to specify the
 launch template to use to launch instances.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

In the [SpotFleetRequestConfigData](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html") property type, use the
 `LaunchTemplateConfigs` property to describe a launch
 template and overrides.

 | 2010-05-15 |
| New `Fn::Cidr` intrinsic function | March 6, 2018 | Returns the specified Cidr address block. For more information, see
 [Fn::Cidr](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-cidr.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-cidr.html"). | 2010-05-15 |
| New resources | March 6, 2018 | 

[AWS::ApiGateway::VpcLink](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-vpclink.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-vpclink.html")

Use the `AWS::ApiGateway::VpcLink` resource to
 specify an API Gateway VPC link for a
 `AWS::ApiGateway::RestApi` to access resources in an
 Amazon Virtual Private Cloud (VPC).

[AWS::GuardDuty::Master](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-master.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-master.html")

Use the `AWS::GuardDuty::Master` resource to create a
 GuardDuty primary account.

[AWS::GuardDuty::Member](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-member.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-member.html")

Use the `AWS::GuardDuty::Member` resource to create a
 GuardDuty member account.

[AWS::SES::ConfigurationSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-configurationset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-configurationset.html")

Use the `AWS::SES::ConfigurationSet` resource to
 create groups of rules that you can apply to the emails you
 send.

[AWS::SES::ConfigurationSetEventDestination](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-configurationseteventdestination.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-configurationseteventdestination.html")

Use the `AWS::SES::ConfigurationSetEventDestination`
 resource to specify a configuration set event destination.

[AWS::SES::ReceiptFilter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptfilter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptfilter.html")

Use the `AWS::SES::ReceiptFilter` resource to specify
 whether to accept or reject mail originating from an IP address or
 range of IP addresses.

[AWS::SES::ReceiptRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptrule.html")

Use the `AWS::SES::ReceiptRule` resource to specify
 which actions Amazon SES should take when it receives mail on behalf of
 one or more email addresses or domains that you own.

[AWS::SES::ReceiptRuleSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptruleset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-receiptruleset.html")

Use the `AWS::SES::ReceiptRuleSet` resource to
 specify an empty rule set for Amazon SES.

[AWS::SES::Template](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-template.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-template.html")

Use the `AWS::SES::Template` resource to specify the
 content of the email, composed of a subject line, an HTML part, and
 a text-only part.

 | 2010-05-15 |
| Updated resources | March 6, 2018 | 

[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")

Use the `AutoScalingGroupName` property to specify
 the name of the Auto Scaling group.

[AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html")

Use the `ApiKeySourceType` property to specify the
 source of the API key for metering requests according to a usage
 plan.
Use the `MinimumCompressionSize` property to specify
 a nullable integer that's used to enable compression or disable
 compression on an API.

[AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.html")

In the [TargetTrackingScalingPolicyConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-targettrackingscalingpolicyconfiguration.html") property type,
 use the `DisableScaleIn` property to specify whether
 scale in by the target tracking policy is disabled.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

In the [LaunchSpecifications](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetlaunchspecification.html") property type, use the
 `TagSpecifications` property to specify the tags to
 apply during SpotFleet creation.

[AWS::Elasticsearch::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html")

Use the `Arn` attribute to have
 `Fn::GetAtt` return the Amazon Resource Name (ARN) of
 the domain.
The `DomainArn` attribute of `Fn::GetAtt`
 has been deprecated.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html")

Use the `DBClusterIdentifier` property to specify the
 DB cluster identifier.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html")

Use the `DBClusterIdentifier` property to specify the
 DB cluster identifier.

[AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html")

Use the `ClusterIdentifier` property to specify the
 unique identifier of the cluster.

[AWS::Route53::HealthCheck](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html")

In the [HealthCheckConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthcheck-healthcheckconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthcheck-healthcheckconfig.html") property type, use the
 `Regions` property to specify the regions from which
 you want Route 53 health checkers to check the specified
 endpoint.

[AWS::SSM::Document](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-document.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-document.html")

Use the `Tags` property to specify the CloudFormation
 resource tags to apply to the document.

 | 2010-05-15 |
| Updated resource | February 19, 2018 | 

[AWS::CodeBuild::Project](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html")

Use the `Triggers` property to configure a webhook
 for the project to begin to automatically rebuild the source code
 every time a code change is pushed to the repository. This is
 available only for GitHub projects in CloudFormation. It's not
 available for GitHub Enterprise projects.

 | 2010-05-15 |
| Updated resource | February 8, 2018 | 

[AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html")

Use the `SSESpecification` property to specify the
 settings to enable server-side encryption.

 | 2010-05-15 |
| Updated resource | February 5, 2018 | 

[AWS::CodeBuild::Project](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html")

In the [Source](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-source.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-source.html")
`CodeBuild Project Source` property type:

* Use the `GitCloneDepth` property to specify the
 depth of history to download.
* Use the `InsecureSsl` property to specify
 whether to ignore SSL warnings while connecting to your
 GitHub Enterprise project repository.


 | 2010-05-15 |
| Updated resources | January 23, 2018 | 

[AWS::AutoScaling::LifecycleHook](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-lifecyclehook.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-lifecyclehook.html")

Use the `LifecycleHookName` property to specify the
 name of the lifecycle hook.

[AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html")

The `AttributeDefinitions` property now requires
 replacement when updated.

[AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")

Use the `CreditSpecification` property to specify the
 credit option for CPU usage of a T2 instance.
Use the `ElasticGpuSpecifications` property to
 specify Elastic GPUs, GPU resources that you can attach to your
 instance to accelerate the graphics performance of your
 applications.

[AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html")

The `InstanceTenancy` property now requires no
 interruption when updated from `"dedicated"` to
 `"default"`.

[AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html")

Use the `HealthCheckGracePeriodSeconds` property to
 specify the period of time, in seconds, that the Amazon ECS service
 scheduler ignores unhealthy Elastic Load Balancing target health checks after a task
 has first started.

[AWS::IoT::TopicRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html")

In the [DynamoDBAction](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-dynamodbaction.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-dynamodbaction.html") property type, the
 `RangeKeyField` and `RangeKeyValue`
 properties are no longer required.

[AWS::KinesisAnalytics::ApplicationOutput](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationoutput.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationoutput.html")

In the [ApplicationOutput](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationoutput.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationoutput.html") property type, use
 the `LambdaOutput` property to identify a Lambda function
 as the destination when configuring application output.

[AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html")

Use the `StreamEncryption` property to enable or
 update server-side encryption using an AWS KMS key for a
 specified stream.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `ReservedConcurrentExecutions` property to
 specify the maximum of concurrent executions you want reserved for
 the function.

[AWS::RDS::DBSubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsubnet-group.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsubnet-group.html")

Use the `DBSubnetGroupName` property to specify the
 name for the DB Subnet Group.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

Use the `BucketEncryption` property to specify
 default encryption for a bucket using server-side encryption with
 Amazon S3-managed keys SSE-S3 or AWS KMS keys (SSE-KMS)
 bucket.
In the [ReplicationRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationrule.html") property type, use
 the `SourceSelectionCriteria` property to specify
 additional filters in identifying source objects that you want to
 replicate.
In the [ReplicationDestination](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationdestination.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-replicationdestination.html") property
 type:

* Use the `AccessControlTranslation` property to
 specify replica ownership of the AWS account that owns the
 destination bucket.
* Use the `Account` property to specify
 destination bucket owner account ID.
* Use the `EncryptionConfiguration` property to
 specify encryption-related information for a bucket that is a
 destination for replicated objects.


[AWS::SSM::Association](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-association.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-association.html")

Use the `AssociationName` property to specify the
 name of the association between an SSM document and EC2 instances
 that contain a configuration agent to process the document.

 | 2010-05-15 |
| Rollback triggers added to the CloudFormation console. | January 15, 2018 | Rollback triggers enable you to have CloudFormation monitor the state of
 your application during stack creation and updating, and to roll back that
 operation if the application breaches the threshold of any of the alarms
 you've specified. For more information, see [Monitor and Roll
 Back Stack Operations](using-cfn-rollback-triggers.md "using-cfn-rollback-triggers.md"). | 2010-05-15 |
| Updated resource | January 12, 2018 | 

[AWS::SSM::Parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-parameter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-parameter.html")

Use the `AllowedPattern` property to specify a
 regular expression used to validate the parameter value.

 | 2010-05-15 |
| New resources | December 5, 2017 | 

[AWS::Inspector::AsssmentTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspector-assessmenttarget.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspector-assessmenttarget.html")

Use the `AWS::Inspector::AsssmentTarget` resource to
 create an Amazon Inspector assessment target.

[AWS::Inspector::AssessmentTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspector-assessmenttemplate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspector-assessmenttemplate.html")

Use the `AWS::Inspector::AssessmentTemplate` resource
 to create an Amazon Inspector assessment template.

[AWS::Inspector::ResourceGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspector-resourcegroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspector-resourcegroup.html")

Use the `AWS::Inspector::ResourceGroup` resource to
 create an Amazon Inspector resource group, which defines tags that identify
 AWS resources that make up an Amazon Inspector assessment target.

[AWS::ServiceDiscovery::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-instance.html")

Use the `AWS::ServiceDiscovery::Instance` resource to
 specify information about an instance that Amazon Route 53
 creates.

[AWS::ServiceDiscovery::PrivateDnsNamespace](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-privatednsnamespace.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-privatednsnamespace.html")

Use the `AWS::ServiceDiscovery::PrivateDnsNamespace`
 resource to specify information about a private namespace for
 Amazon Route 53.

[AWS::ServiceDiscovery::PublicDnsNamespace](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-publicdnsnamespace.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-publicdnsnamespace.html")

Use the `AWS::ServiceDiscovery::PublicDnsNamespace`
 resource to specify information about a public namespace for
 Amazon Route 53.

[AWS::ServiceDiscovery::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-servicediscovery-service.html")

Use the `AWS::ServiceDiscovery::Service` resource to
 define a template for up to five records and an optional health
 check that you want Amazon Route 53 to create when you register an
 instance.

 | 2010-05-15 |
| Updated resource | December 5, 2017 | 

[AWS::KinesisAnalytics::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-application.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-application.html")

In the [Input](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-application-input.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalytics-application-input.html") property type, use the
 `InputProcessingConfiguration` property to transform
 records as they're received from the stream.

 | 2010-05-15 |
| Updated resource | December 1, 2017 | 

[AWS::CodeBuild::Project](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html")

Use the `BadgeEnabled` property to generate a
 publicly accessible URL for a project's build badge.
Use the `Cache` property to configure cache settings
 for build dependencies.
Use the `VpcConfig` property to enable CodeBuild to
 access resources in an Amazon VPC.
In the [EnvironmentVariable](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-environmentvariable.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codebuild-project-environmentvariable.html") property type,
 use the `Type` property to specify the type of
 environment variable.

 | 2010-05-15 |
| New resource | November 30, 2017 | 

[AWS::Cloud9::EnvironmentEC2](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloud9-environmentec2.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloud9-environmentec2.html")

Use the `AWS::Cloud9::EnvironmentEC2` resource to
 create an Amazon EC2 development environment in AWS Cloud9.

 | 2010-05-15 |
| Updated resources | November 29, 2017 | 

[AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")

Use the `Cpu` property to specify the number of cpu
 units needed for the task.
Use the `ExecutionRoleArn` property to specify the
 ARN of the execution role.
Use the `Memory` property to specify the amount (in
 MiB) of memory needed for the task.
Use the `RequiresCompatibilities` property to specify
 the launch type the task requires.

[AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html")

Use the `LaunchType` property to specify the launch
 type on which to run your service.
Use the `NetworkConfiguration` property to specify
 the network configuration for the service.
Use the `PlatformVersion` property to specify the
 platform version on which to run your service.

 | 2010-05-15 |
| New resources | November 28, 2017 | 

[AWS::GuardDuty::Detector](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-detector.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-detector.html")

Use the `AWS::GuardDuty::Detector` resource to create
 a single Amazon GuardDuty detector.

[AWS::GuardDuty::IPSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-ipset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-ipset.html")

Use the `AWS::GuardDuty::IPSet` resource to create an
 Amazon GuardDutyIP set.

[AWS::GuardDuty::ThreatIntelSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-threatintelset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-guardduty-threatintelset.html")

Use the `AWS::GuardDuty::ThreatIntelSet` resource to
 create a ThreatIntelSet.

 | 2010-05-15 |
| Updated resources | November 28, 2017 | 

[AWS::CodeDeploy::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-application.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-application.html")

Use the `ComputePlatform` property to specify an
 AWS Lambda compute platform for CodeDeploy to deploy an application
 to.

[AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html")

In the [DeploymentStyle](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html") property type, use
 the `DeploymentType` property to specify a blue/green
 deployment on a Lambda compute platform.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

In the [SpotFleetRequestConfigData](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html") property
 type, the `SpotPrice` property is now optional.

[AWS::Lambda::Alias](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-alias.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-alias.html")


Use the `RoutingConfig` property to specify two
 different versions of an AWS Lambda function, allowing you to
 dictate what percentage of traffic will invoke each version.

 | 2010-05-15 |
| New `CodeDeployLambdaAliasUpdate` update policy | November 28, 2017 | Use the `CodeDeployLambdaAliasUpdate` update policy to perform
 an CodeDeploy deployment when the version changes on an
 `AWS::Lambda::Alias` resource. For more information, see
 [UpdatePolicy
 Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html"). | 2010-05-15 |
| New `SSM` parameter types | November 21, 2017 | Use `SSM` parameter types to use existing parameters from
 Systems Manager Parameter Store. **Note**: CloudFormation
 doesn't currently support the `SecureString` type. For more
 information, see [SSM
 Parameter Types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md"). | 2010-05-15 |
| New `ResolvedValue` field for `Parameter` data
 type | November 21, 2017 | The `ResolvedValue` field returns the value that's used in the
 stack definition for an `SSM` parameter. For more information,
 see the [Parameter](../APIReference/API_Parameter.md "../APIReference/API_Parameter.md") data type in the *AWS CloudFormation API
 Reference*. | 2010-05-15 |
| Updated resources | November 20, 2017 | 

[AWS::ApiGateway::ApiKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-apikey.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-apikey.html")

Use the `CustomerId` property to specify an AWS
 Marketplace customer identifier.
Use the `GenerateDistinctId` property to specify
 whether the key identifier is distinct from the created API key
 value.

[AWS::ApiGateway::Authorizer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-authorizer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-authorizer.html")

Use the `AuthType` property to specify a
 customer-defined field that's used in Swagger imports and exports
 without functional impact.

[AWS::ApiGateway::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-domainname.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-domainname.html")

Use the `EndpointConfiguration` property to specify
 the endpoint types of an API Gateway domain name.
Use the `RegionalCertificateArn` property to
 reference a certificate for use by the regional endpoint for a
 domain name.

[AWS::ApiGateway::Method](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html")

In the [Integration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apitgateway-method-integration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apitgateway-method-integration.html") and [IntegrationResponse](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apitgateway-method-integration-integrationresponse.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apitgateway-method-integration-integrationresponse.html") property types,
 use the `ContentHandling` property to specify how to
 handle request payload content type conversions.

[AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html")

Use the `EndpointConfiguration` property to specify
 the endpoint types of an API Gateway REST API.

[AWS::ApplicationAutoScaling::ScalableTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalabletarget.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalabletarget.html")

Use the `ScheduledActions` property to specify
 scheduled actions for an Application Auto Scaling scalable target.

[AWS::ECR::Repository](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-repository.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-repository.html")

Use the `LifecyclePolicy` property to specify a
 lifecycle policy for an Amazon ECR repository.

[AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")

In the [ContainerDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-containerdefinitions.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-taskdefinition-containerdefinitions.html") property type,
 use the `LinuxParameters` property to specify
 Linux-specific options for an Amazon ECS container.

[AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html")

Use the `AtRestEncryptionEnabled` property to enable
 encryption at rest.
Use the `AuthToken` property to specify a password
 that's used to access a password-protected server.
Use the `TransitEncryptionEnabled` property to enable
 in-transit encryption.

[AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html")

Use the `TargetGroupName` attribute with the
 `Fn::GetAtt` function to get the name of an Elastic Load Balancing
 target group.

[AWS::Elasticsearch::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html")

Use the `VPCOptions` property to specify a VPC
 configuration for the OpenSearch Service domain.

[AWS::EMR::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html")

Use the `EbsRootVolumeSize` property to specify the
 size of the EBS root volume for an Amazon EMR cluster.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

Use the `SourceRegion` and `KmsKeyId`
 properties to create an encrypted read replica from a cross-region
 source DB instance.

[AWS::Route53::HostedZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html")

Use the `QueryLoggingConfig` property to specify a
 configuration for DNS query logging.

 | 2010-05-15 |
| New `NoEcho` field for custom resource `Response`
 objects | November 20, 2017 | You can now use the optional `NoEcho` field to mask the output
 of a custom resource. For more information, see [Custom Resource Response
 Objects](crpg-ref-responses.md "crpg-ref-responses.md").
The corresponding `noEcho` parameter is supported by the
 `send` method. For more information, see [cfn-response Module](aws-properties-lambda-function-code.md#cfn-lambda-function-code-cfnresponsemodule "aws-properties-lambda-function-code.md#cfn-lambda-function-code-cfnresponsemodule"). | 2010-05-15 |
| Stack instance overrides added for stack sets. | November 17, 2017 | CloudFormation StackSets allows you to override parameter values in stack
 instances by account and region. You can override parameter values when you
 create the stack instances, or when updating existing stack instances. For
 more information, see [Override Parameters on Stack
 Instances](stackinstances-override.md "stackinstances-override.md"). | 2010-05-15 |
| Updated resource | November 15, 2017 | 

[AWS::StepFunctions::StateMachine](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-statemachine.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-statemachine.html")

You can use `AWS::StepFunctions::StateMachine` to
 specify a `StateMachineName` when creating a state
 machine, and both `DefinitionString` and
 `RoleArn` can be updated without replacing the state
 machine.

 | 2010-05-15 |
| StackSets now supports a maximum of 500 stack instances per stack
 set. | November 6, 2017 | You can now create up to a maximum of 500 stack instances per stack set.
 For more information about AWS CloudFormation limits, see [Understand CloudFormation
 quotas](cloudformation-limits.md "cloudformation-limits.md"). | 2010-05-15 |
| New resources | November 2, 2017 | 

[AWS::CloudFront::CloudFrontOriginAccessIdentity](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html")

Use the
 `AWS::CloudFront::CloudFrontOriginAccessIdentity`
 resource to specify the Amazon CloudFront origin access identity to
 associate with the origin of a CloudFront distribution.

[AWS::CloudFront::StreamingDistribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-streamingdistribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-streamingdistribution.html")

Use the `AWS::CloudFront::StreamingDistribution`
 resource to specify an Adobe Real-Time Messaging Protocol (RTMP)
 streaming distribution for CloudFront.

 | 2010-05-15 |
| Updated resources | November 2, 2017 | 

[AWS::ApiGateway::Deployment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-deployment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-deployment.html")

The `StageName` property has been deprecated on the
 [StageDescription](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-deployment-stagedescription.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apigateway-deployment-stagedescription.html") property
 type.

[AWS::ApiGateway::Method](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html")

Use the `OperationName` property to assign a friendly
 name to an API Gateway method.
Use the `RequestValidatorId` property to associate a
 request validator with a method.

[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")

Use the `LifecycleHookSpecificationList` property to
 specify actions to perform when Auto Scaling launches or terminates
 instances.

[AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html")


Use the `Tags` property to specify an arbitrary set
 of tags (key–value pairs) to associate with a CloudFront
 distribution.
In the [CacheBehavior](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-cachebehavior.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-cachebehavior.html") and [DefaultCacheBehavior](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-defaultcachebehavior.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-defaultcachebehavior.html") property types,
 use the `LambdaFunctionAssociations` property to specify
 Lambda function associations for a CloudFront distribution.
In the [CustomOriginConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-customoriginconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-customoriginconfig.html") property type, use
 the `OriginKeepaliveTimeout` property to specify a
 custom keep-alive timeout, and use the
 `OriginReadTimeout` property to specify a custom
 origin read timeout.
In the [DistributionConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-distributionconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-distributionconfig.html") property type, use
 the `IPV6Enabled` property to specify whether CloudFront
 responds to IPv6 DNS requests with an IPv6 address for your
 distribution.

[AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html")


In the [LoadBalancerInfo](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html") property type, use
 the `TargetGroupInfoList` property to specify
 information about a target group in Elastic Load Balancing to use in a
 deployment.

[AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html"), [AWS::EC2::SecurityGroupEgress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html"), and
 [AWS::EC2::SecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html")


Use the `Description` property to specify the
 description of a security group rule.

[AWS::EC2::Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html")


The `Ipv6CidrBlock` property now supports `No
 interruption` updates.

[AWS::EC2::VPNGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-gateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-gateway.html")


Use the `AmazonSideAsn` property to specify a private
 Autonomous System Number (ASN) for the Amazon side of a BGP
 session.

[AWS::EC2::VPNConnection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-connection.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-connection.html")


Use the `VpnTunnelOptionsSpecifications` property to
 configure tunnel options for a VPN connection.

[AWS::ElasticBeanstalk::ConfigurationTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-beanstalk-configurationtemplate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-beanstalk-configurationtemplate.html")
 and [AWS::ElasticBeanstalk::Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html")


In the [ConfigurationOptionSetting](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-configurationtemplate-configurationoptionsetting.html") and [OptionSetting](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-environment-optionsetting.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-environment-optionsetting.html") property types, use the
 `ResourceName` property to specify a resource name
 for a time-based scaling configuration option.

[AWS::EMR::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html")


Use the `CustomAmiId` property to specify a custom
 Amazon Linux AMI for a cluster.

[AWS::KinesisFirehose::DeliveryStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html")


Use the `Arn` attribute with the
 `Fn::GetAtt` function to get the Amazon Resource Name
 (ARN) of the delivery stream.

[AWS::KMS::Key](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-key.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-key.html")


Use the `Tags` property to specify an arbitrary set
 of tags (key–value pairs) to associate with a
 customer managed key.

[AWS::OpsWorks::Layer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html") and [AWS::OpsWorks::Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html")


Use the `Tags` property to specify an arbitrary set
 of tags (key–value pairs) to associate with an OpsWorks layer
 or stack.

[AWS::RDS::OptionGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-optiongroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-optiongroup.html")

In the [OptionConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-optiongroup-optionconfigurations.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-optiongroup-optionconfigurations.html") property type,
 use the `OptionVersion` property to specify a version
 for the option.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

Use the `AnalyticsConfigurations` property to
 configure an analysis filter for an Amazon S3 bucket.

 | 2010-05-15 |
| New resources | October 24, 2017 | 

[AWS::Glue::Classifier](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-classifier.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-classifier.html")

Use the `AWS::Glue::Classifier` resource to create an
 AWS Glue classifier.

[AWS::Glue::Connection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-connection.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-connection.html")

Use the `AWS::Glue::Connection` resource to specify
 an AWS Glue connection to a data source.

[AWS::Glue::Crawler](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-crawler.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-crawler.html")

Use the `AWS::Glue::Crawler` resource to specify an
 AWS Glue crawler.

[AWS::Glue::Database](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-database.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-database.html")

Use the `AWS::Glue::Database` resource to create an
 AWS Glue database.

[AWS::Glue::DevEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-devendpoint.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-devendpoint.html")

Use the `AWS::Glue::DevEndpoint` resource to specify
 a development endpoint for remotely debugging ETL scripts.

[AWS::Glue::Job](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-job.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-job.html")

Use the `AWS::Glue::Job` resource to specify an AWS Glue
 job in the data catalog.

[AWS::Glue::Partition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-partition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-partition.html")

Use the `AWS::Glue::Partition` resource to create an
 AWS Glue partition, which represents a slice of table data.

[AWS::Glue::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-table.html")

Use the `AWS::Glue::Table` resource to create an
 AWS Glue table.

[AWS::Glue::Trigger](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-trigger.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-glue-trigger.html")

Use the `AWS::Glue::Trigger` resource to specify
 triggers that run AWS Glue jobs.

 | 2010-05-15 |
| New resources | October 11, 2017 | 

[AWS::SSM::MaintenanceWindow](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-maintenancewindow.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-maintenancewindow.html")

Use the `AWS::SSM::MaintenanceWindow` resource to
 create an AWS Systems Manager Maintenance Window.

[AWS::SSM::MaintenanceWindowTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-maintenancewindowtarget.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-maintenancewindowtarget.html")

Use the `AWS::SSM::MaintenanceWindowTarget` resource
 to register a target with a Maintenance Window.

[AWS::SSM::MaintenanceWindowTask](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-maintenancewindowtask.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-maintenancewindowtask.html")

Use the `AWS::SSM::MaintenanceWindowTask` resource to
 define a Maintenance Window task.

[AWS::SSM::PatchBaseline](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-patchbaseline.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-patchbaseline.html")

Use the `AWS::SSM::PatchBaseline` resource to define
 a Systems Manager patch baseline.

 | 2010-05-15 |
| New resource | October 10, 2017 | 

[AWS::ElasticLoadBalancingV2::ListenerCertificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenercertificate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenercertificate.html")

Use the
 `AWS::ElasticLoadBalancingV2::ListenerCertificate`
 resource to specify certificates for an Elastic Load Balancing listener.

 | 2010-05-15 |
| New resource | September 27, 2017 | 

[AWS::Athena::NamedQuery](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-namedquery.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-athena-namedquery.html")

Use the `AWS::Athena::NamedQuery` resource to create
 an Amazon Athena query.

 | 2010-05-15 |
| Updated resources | September 27, 2017 | 

[AWS::EC2::NatGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-natgateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-natgateway.html")

Use the `Tags` property to specify resource tags for
 a NAT gateway.

[AWS::ElasticBeanstalk::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-application.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-application.html")

Use the `ResourceLifecycleConfig` property to define
 lifecycle settings for resources that belong to the application,
 and the service role that Elastic Beanstalk assumes in order to apply lifecycle
 settings.

[AWS::ElasticBeanstalk::ConfigurationTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-beanstalk-configurationtemplate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-beanstalk-configurationtemplate.html")
 and [AWS::ElasticBeanstalk::Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html")

Use the `PlatformArn` property to specify a custom
 platform for Elastic Beanstalk.

[AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html")

In the [TargetDescription](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-targetgroup-targetdescription.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-targetgroup-targetdescription.html") property type, use the
 `AvailabilityZone` property to specify the
 Availability Zone where the IP address is to be registered.

[AWS::Events::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-rule.html")

In the [Target](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-target.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-rule-target.html") property type, use the following properties for
 input transformation of events and setting Amazon ECS task and Kinesis
 stream targets.

* `EcsParameters`
* `InputTransformer`
* `KinesisParameters`
* `RunCommandParameters`


[AWS::KinesisFirehose::DeliveryStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html")


Use the `DeliveryStreamType` property to specify the
 stream type and the `KinesisStreamSourceConfiguration`
 property to specify the stream and role ARNs for a Kinesis stream
 used as the source for a delivery stream.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

For the `Engine` property, if you have specified
 `oracle-se` or `oracle-se1`, you can
 update to `oracle-se2` without the database instance
 being replaced.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

Use the `AccelerateConfiguration` property to
 configure the transfer acceleration state for an Amazon S3
 bucket.

 | 2010-05-15 |
| Termination protection added for stacks. | September 26, 2017 | Enabling termination protection on a stack prevents it from being
 accidentally deleted. A user can't delete a stack with termination
 protection enabled. For more information, see [Protecting a Stack From
 Being Deleted](using-cfn-protect-stacks.md "using-cfn-protect-stacks.md"). | 2010-05-15 |
| Changed default `umask` value from version 1.4-22
 onwards | September 14, 2017 | The default `umask` parameter value for the cfn-hup.conf
 configuration file is now `022`. For more information, see [cfn-hup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-hup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-hup.html")
 . |  |
| Updated resources | September 7, 2017 | 

[AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html")


Use the `SubnetMappings` property to specify the IDs
 of the subnets to attach to the load balancer.
Use the `Type` property to specify the type of load
 balancer to create.

[AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html")


Use the `TargetType` property to specify the
 registration type of the targets in this target group.

 | 2010-05-15 |
| Rollback triggers added to the CloudFormation API | August 31, 2017 | Rollback triggers enable you to have CloudFormation monitor the state of your
 application during stack creation and updating, and to roll back that
 operation if the application breaches the threshold of any of the alarms
 you've specified. For more information, see [RollbackConfiguration](../APIReference/API_RollbackConfiguration.md "../APIReference/API_RollbackConfiguration.md") in the *AWS CloudFormation API
 Reference*. | 2010-05-15 |
| New `umask` parameter for cfn-hup.conf file | August 31, 2017 | Use the `umask` parameter in the cfn-hup.conf configuration
 file to control file permissions used by the cfn-hup daemon (version
 1.4-21). For more information, see [cfn-hup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-hup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-hup.html"). |  |
| Updated resources for VPC Sizing support | August 29, 2017 | 

[AWS::EC2::VPCCidrBlock](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpccidrblock.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpccidrblock.html")

Use the `CidrBlock` property to associate an IPv4
 CIDR block with a VPC.

[AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html")

Use the `CidrBlockAssociations` attribute with the
 `Fn::GetAtt` function to get a list of IPv4 CIDR
 block association IDs associated with the VPC.

 | 2010-05-15 |
| Updated resources | August 23, 2017 | 

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")


In the [Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-rule.html") property type, use the
 `TagFilters` property to specify tags to use in
 identifying a subset of objects for an Amazon S3 bucket.
Use the `MetricsConfiguration` property to specify a
 metrics configuration for the CloudWatch request metrics from an Amazon S3
 bucket.

[AWS::IoT::TopicRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html")


In the [Action](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-action.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-action.html") property type, use the
 `DynamoDBv2Action` property to describe an AWS IoT
 action that writes data to a DynamoDB table.
In the [Action](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-action.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-action.html") property type, the
 `DynamoDBAction` property now supports the
 `HashKeyType` and `RangeKeyType`
 properties.

[AWS::Lambda::Permission](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-permission.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-permission.html")


Use the `EventSourceToken` property to specify a
 unique token that must be supplied by the principal invoking the
 function.

 | 2010-05-15 |
| New pseudo parameters | August 23, 2017 | Use the `AWS::Partition` pseudo parameter to return the
 partition that a resource is in.
Use the `AWS::URLSuffix` pseudo parameter to return the suffix
 for a domain.
For more information, see [Pseudo Parameters
 Reference](pseudo-parameter-reference.md "pseudo-parameter-reference.md"). | 2010-05-15 |
| New resources for DAX support | August 22, 2017 | 

[AWS::DAX::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dax-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dax-cluster.html")

Use the `AWS::DAX::Cluster` resource to create a
 DAX cluster for use with Amazon DynamoDB.

[AWS::DAX::ParameterGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dax-parametergroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dax-parametergroup.html")

Use the `AWS::DAX::ParameterGroup` resource to create
 a parameter group for use with Amazon DynamoDB.

[AWS::DAX::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dax-subnetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dax-subnetgroup.html")

Use the `AWS::DAX::SubnetGroup` resource to create a
 subnet group for use with DAX (DynamoDB Accelerator).

 | 2010-05-15 |
| New resources | August 18, 2017 | 

[AWS::ApiGateway::DocumentationPart](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-documentationpart.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-documentationpart.html") and
 [AWS::ApiGateway::DocumentationPart](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-documentationversion.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-documentationversion.html")

Use the `AWS::ApiGateway::DocumentationPart` and
 `AWS::ApiGateway::DocumentationVersion` resources to
 create documentation for your API Gateway API.

[AWS::ApiGateway::GatewayResponse](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-gatewayresponse.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-gatewayresponse.html")

Use the `AWS::ApiGateway::GatewayResponse` resource
 to create a custom response for your API Gateway API.

[AWS::ApiGateway::RequestValidator](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-requestvalidator.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-requestvalidator.html")

Use the `AWS::ApiGateway::RequestValidator` resource
 to set up validation rules for incoming requests to your API Gateway
 API.

[AWS::EC2::NetworkInterfacePermission](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkinterfacepermission.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkinterfacepermission.html")

Use the `AWS::EC2::NetworkInterfacePermission`
 resource to grant an AWS account permission to a network
 interface.

 | 2010-05-15 |
| Updated resources | August 18, 2017 | 

[AWS::ApiGateway::Stage](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-stage.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-stage.html")

Use the `DocumentationVersion` property to specify a
 versioned snapshot of the API documentation.

[AWS::AutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html")

Use the `TargetTrackingConfiguration` property to
 specify an Auto Scaling target tracking scaling policy
 configuration.

[AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html")

Use the `EventSelectors` property for Amazon S3 Data
 Events support.

[AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html")

Use the `LoadBalancerInfo` and
 `DeploymentStyle` properties to specify an Elastic Load Balancing load
 balancer for an in-place deployment.
Use the `AutoRollbackConfiguration` property to
 configure automatic rollback for the deployment.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

In the [SpotFleetRequestConfigData](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-spotfleetrequestconfigdata.html") property
 type, use the `ReplaceUnhealthyInstances` property to
 indicate whether the Spot fleet should replace unhealthy instances
 and the `Type` property to specify the type of
 request.

[AWS::EC2::Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html")

Use the `AssignIpv6AddressOnCreation` and
 `Ipv6CidrBlock` properties to create a subnet with an
 IPv6 CIDR block.

[AWS::KinesisFirehose::DeliveryStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html")

Use the `ExtendedS3DestinationConfiguration` property
 to configure a destination in Amazon S3.
Use the `ProcessingConfiguration` subproperty within
 each destination configuration to invoke Lambda functions that
 transform incoming source data and deliver the transformed data to
 destinations.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html") and [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

The default `DeletionPolicy` is now
 `Snapshot` for `AWS::RDS::DBCluster`
 resources and for `AWS::RDS::DBInstance` resources that
 don't specify the `DBClusterIdentifier` property. For
 more information, see [DeletionPolicy Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html").

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

In the [Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-rule.html") property type, use the
 `AbortIncompleteMultipartUpload` property to specify
 a lifecycle rule that aborts incomplete multipart uploads to an
 Amazon S3 bucket.

[AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html")

Use the `KmsMasterKeyId` and
 `KmsDataKeyReusePeriodSeconds` properties to
 configure server-side encryption for Amazon SQS.


Added the `Arn` attribute to the `Fn::GetAtt`
 intrinsic function for the following resources:

* [AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html"). Also added
 `SnsTopicArn`.
* [AWS::CloudWatch::Alarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html")
* [AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html")
* [AWS::ECS::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html")
* [AWS::IoT::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-policy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-policy.html")
* [AWS::IoT::TopicRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html")
* [AWS::Logs::Destination](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-destination.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-destination.html")
 | 2010-05-15 |
| Support for stack tags in CodePipeline artifacts | August 18, 2017 | You can now specify tags for stacks in template configuration files for
 use as artifacts for CodePipeline pipelines. Specified tags are applied to stacks
 created using the template configuration file. For more information, see
 [CloudFormation Artifacts](continuous-delivery-codepipeline-cfn-artifacts.md "continuous-delivery-codepipeline-cfn-artifacts.md"). | 2010-05-15 |
| Create encrypted file systems | August 14, 2017 | 

[AWS::EFS::FileSystem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-filesystem.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-filesystem.html")

Use the `Encrypted` property to encrypt an Amazon EFS file
 system during creation.
Use the `KmsKeyId` property to optionally specify a
 custom customer managed key to use to protect the encrypted file
 system.

 | 2010-05-15 |
| New resources for AWS Batch support | August 8, 2017 | 


[AWS::Batch::ComputeEnvironment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-computeenvironment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-computeenvironment.html")


Use the `AWS::Batch::ComputeEnvironment` resource to
 define your AWS Batch compute environment.


[AWS::Batch::JobDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-jobdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-jobdefinition.html")


Use the `AWS::Batch::JobDefinition` resource to
 specify the parameters for an AWS Batch job definition.


[AWS::Batch::JobQueue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-jobqueue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-batch-jobqueue.html")


Use the `AWS::Batch::JobQueue` resource to define
 your AWS Batch job queue.

 | 2010-05-15 |
| New resources for Amazon Managed Service for Apache Flink support | July 28, 2017 | 

[AWS::KinesisAnalytics::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-application.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-application.html")

Use the `AWS::KinesisAnalytics::Application` resource
 to create an Amazon Managed Service for Apache Flink application.

[AWS::KinesisAnalytics::ApplicationOutput](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationoutput.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationoutput.html")

Use the `AWS::KinesisAnalytics::ApplicationOutput`
 resource to add an external destination to your Amazon Managed Service for Apache Flink
 application.

[AWS::KinesisAnalytics::ApplicationReferenceDataSource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationreferencedatasource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalytics-applicationreferencedatasource.html")

Use the
 `AWS::KinesisAnalytics::ApplicationReferenceDataSource`
 resource to add a reference data source to an existing Amazon Managed Service for Apache Flink
 application.

 | 2010-05-15 |
| Use StackSets to centrally manage stacks across accounts and
 regions | July 25, 2017 | StackSets enables you to create, update, or delete stacks across multiple
 accounts and regions in a single operation. Using an administrator account,
 you define and manage a CloudFormation template, and use the template as the
 basis for provisioning stacks into selected target accounts across specified
 regions. For more information, see [Managing stacks across accounts
 and Regions with StackSets](what-is-cfnstacksets.md "what-is-cfnstacksets.md"). | 2010-05-15 |
| View stack events by client request token | July 14, 2017 | In the console, stack operations display the client request token on the
 **Events** tab. All events triggered by a given stack
 operation are assigned the same client request token, which you can use to
 track operations. For more information, see [Viewing
 CloudFormation Stack Data and Resources on the AWS Management Console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md") and [StackEvent](../APIReference/API_StackEvent.md "../APIReference/API_StackEvent.md")
 in the *AWS CloudFormation API Reference*. | 2010-05-15 |
| Use stack quick-create links | July 14, 2017 | Use quick-create links to get stacks up and running quickly. You can
 specify the template URL, stack name, and template parameters to prepopulate
 a single **Create Stack Wizard** page. For more
 information, see [Creating Quick-Create Links for Stacks](cfn-console-create-stacks-quick-create-links.md "cfn-console-create-stacks-quick-create-links.md"). | 2010-05-15 |
| New resources for AWS Database Migration Service support | July 12, 2017 | 

[AWS::DMS::Certificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-certificate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-certificate.html")

Use the `AWS::DMS::Certificate` resource to create an
 SSL certificate that encrypts connections between AWS DMS endpoints
 and the replication instance.

[AWS::DMS::Endpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-endpoint.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-endpoint.html")

Use the `AWS::DMS::Endpoint` resource to create an
 AWS DMS endpoint.

[AWS::DMS::EventSubscription](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-eventsubscription.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-eventsubscription.html")

Use the `AWS::DMS::EventSubscription` resource to get
 notifications for AWS DMS events through the Amazon Simple Notification Service.

[AWS::DMS::ReplicationInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationinstance.html")

Use the `AWS::DMS::ReplicationInstance` resource to
 create an AWS DMS replication instance.

[AWS::DMS::ReplicationSubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationsubnet-group.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationsubnet-group.html")

Use the `AWS::DMS::ReplicationSubnetGroup` resource
 to create an AWS DMS replication subnet group.

[AWS::DMS::ReplicationTask](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationtask.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dms-replicationtask.html")

Use the `AWS::DMS::ReplicationTask` resource to
 create an AWS DMS replication task.

 | 2010-05-15 |
| New resources | July 5, 2017 | 

[AWS::CloudWatch::Dashboard](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-dashboard.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-dashboard.html")

Use the `AWS::CloudWatch::Dashboard` resource to
 specify a custom CloudWatch dashboard for your CloudWatch console.

[AWS::ApiGateway::DomainName](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-domainname.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-domainname.html")

Use the `AWS::ApiGateway::DomainName` resource to
 specify a custom, friendly URL for your API that's deployed to
 Amazon API Gateway.

[AWS::EC2::EgressOnlyInternetGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-egressonlyinternetgateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-egressonlyinternetgateway.html")

Use the `AWS::EC2::EgressOnlyInternetGateway`
 resource to create an egress-only internet gateway for your
 VPC.

[InstanceFleetConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticmapreduce-instancefleetconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticmapreduce-instancefleetconfig.html")

Use the `InstanceFleetConfig` resource to configure a
 Spot Instance fleet for an Amazon EMR cluster.

 | 2010-05-15 |
| Updated resources | July 5, 2017 | 

[AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html")

Use the `BinaryMediaTypes` property to specify
 supported binary media types.

[AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.html")

Use the `TargetTrackingScalingPolicyConfiguration`
 property to specify a target tracking scaling policy
 configuration.

[AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html")

Use the `TrailName` property to specify a custom name
 for an AWS CloudTrail resource.
Use the `Tags` property to specify resource
 tags.

[AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html")

Use the `AlarmConfiguration` property to configure
 alarms for the deployment group.
Use the `TriggerConfigurations` property to configure
 notification triggers for the deployment group.

[AWS::EMR::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html")

Use the `CoreInstanceFleet` property and the
 `MasterInstanceFleet` property in the [JobFlowInstancesConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-jobflowinstancesconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-jobflowinstancesconfig.html") property type to configure the
 Spot Instance fleet for an Amazon EMR cluster.

[AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html")

Use the `TimeToLiveSpecification` property to specify
 the Time to Live (TTL) settings for an Amazon DynamoDB table.
Use the `Tags` property to specify resource tags for
 a DynamoDB table.

[AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")

The `IamInstanceProfile` property now supports
 `No interruption` updates.

[AWS::EC2::Route](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html")

Use the `EgressOnlyInternetGatewayId` property to
 specify an egress-only Internet gateway for an EC2 route.

[AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html")

Use the `RetentionPeriodHours` property to specify
 the number of hours that data records stored in shards remain
 accessible.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html")

Use the `ReplicationSourceIdentifier` property to
 create a DB cluster as a Read Replica of another DB cluster or an
 Amazon RDS MySQL DB instance.

[AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html")

Use the `LoggingProperties` property to create audit
 log files and store them in Amazon S3.

 | 2010-05-15 |
| New resources | June 6, 2017 | 

[AWS::EMR::SecurityConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-securityconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-securityconfiguration.html")

Use the `AWS::EMR::SecurityConfiguration` resource to
 create a security configuration, which is stored in the service and
 can be specified when a cluster is created.

 | 2010-05-15 |
| Updated resources | June 6, 2017 | 

[AWS::AutoScaling::LifecycleHook](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-lifecyclehook.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-lifecyclehook.html")

The `NotificationTargetARN` and `RoleARN`
 properties are now optional.

[AWS::CloudWatch::Alarm](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html")

You can now use the
 `EvaluateLowSampleCountPercentile`,
 `ExtendedStatistic`, and
 `TreatMissingData` properties when creating
 `AWS::CloudWatch::Alarm` resources.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

CloudFormation supports mutable changes to Spot fleet
 properties.
The following properties of the
 `SpotFleetRequestConfigData` property support
 `Replacement` updates:

* `AllocationStrategy`
* `IamFleetRole`
* `LaunchSpecifications`
* `SpotPrice`
* `TerminateInstancesWithExpiration`
* `ValidFrom`
* `ValidUntil`

The following properties of the
 `SpotFleetRequestConfigData` property support
 `No interruption` updates:

* `ExcessCapacityTerminationPolicy`
* `TargetCapacity`


[AWS::EMR::InstanceGroupConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-instancegroupconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-instancegroupconfig.html")

CloudFormation now supports Auto Scaling for Amazon EMR task instance
 groups.

[AWS::Events::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-rule.html")

The `RoleArn` property is deprecated on the
 `Rule` resource.
Use the `RoleArn` property on the `Target`
 property type to specify the IAM role to use for a target.

[AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html")

The `ShardCount` property now supports `No
 interruption` updates.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `TracingConfig` property to configure tracing
 settings for Lambda functions.

[AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html"), [AWS::Redshift::ClusterParameterGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clusterparametergroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clusterparametergroup.html"),
 [AWS::Redshift::ClusterSecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clustersecuritygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clustersecuritygroup.html"), and
 [AWS::Redshift::ClusterSubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clustersubnetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-clustersubnetgroup.html")

Use the `Tags` property to specify resource
 tags.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html")

Added the `ReadEndpoint.Address` attribute to the
 `Fn::GetAtt` intrinsic function.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

Added the `Arn` attribute to the
 `Fn::GetAtt` intrinsic function.

 | 2010-05-15 |
| New resources | May 11, 2017 | 
The following new resources support using AWS WAF with Elastic Load Balancing (ELB)
 Application Load Balancers.

[AWS::WAFRegional::ByteMatchSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-bytematchset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-bytematchset.html")

Use the `AWS::WAFRegional::ByteMatchSet` resource to
 identify a part of a web request that you want to inspect.

[AWS::WAFRegional::IPSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-ipset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-ipset.html")

Use the `AWS::WAFRegional::IPSet` resource to specify
 which web requests to permit or block based on the IP addresses
 from which the requests originate.

[AWS::WAFRegional::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-rule.html")

Use the `AWS::WAFRegional::Rule` resource to specify
 a combination of `IPSet`, `ByteMatchSet`, and
 `SqlInjectionMatchSet` objects that identify the web
 requests to allow, block, or count.

[AWS::WAFRegional::SizeConstraintSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-sizeconstraintset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-sizeconstraintset.html")

Use the `AWS::WAFRegional::SizeConstraintSet`
 resource to specify a size constraint used to check the size of a
 web request and which parts of the request to check.

[AWS::WAFRegional::SqlInjectionMatchSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-sqlinjectionmatchset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-sqlinjectionmatchset.html")

Use the `AWS::WAFRegional::SqlInjectionMatchSet`
 resource to allow, block, or count requests that contain malicious
 SQL code in a specific part of web requests.

[AWS::WAFRegional::WebACL](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-webacl.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-webacl.html")

Use the `AWS::WAFRegional::WebACL` resource to
 identify the web requests that you want to allow, block, or
 count.

[AWS::WAFRegional::WebACLAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-webaclassociation.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-webaclassociation.html")

Use the `AWS::WAFRegional::WebACLAssociation`
 resource to associate a web access control group (ACL) with a
 resource.

[AWS::WAFRegional::XssMatchSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-xssmatchset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wafregional-xssmatchset.html")

Use the `AWS::WAFRegional::XssMatchSet` resource to
 specify the parts of web requests that you want AWS WAF
 to inspect for cross-site scripting attacks and the name of the
 header to inspect.

 | 2010-05-15 |
| New resources | April 28, 2017 | 

[AWS::Cognito::IdentityPool](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-identitypool.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-identitypool.html")

Use the `AWS::Cognito::IdentityPool` resource to
 create an Amazon Cognito identity pool.

[AWS::Cognito::IdentityPoolRoleAttachment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-identitypoolroleattachment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-identitypoolroleattachment.html")

Use the `AWS::Cognito::IdentityPoolRoleAttachment`
 resource to manage the role configuration for an Amazon Cognito identity
 pool.

[AWS::Cognito::UserPool](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpool.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpool.html")

Use the `AWS::Cognito::UserPool` resource to create
 an Amazon Cognito user pool.

[AWS::Cognito::UserPoolClient](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolclient.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolclient.html")

Use the `AWS::Cognito::UserPoolClient` resource to
 create a user pool client.

[AWS::Cognito::UserPoolGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolgroup.html")

Use the `AWS::Cognito::UserPoolGroup` resource to
 create a user group in an Amazon Cognito user pool.

[AWS::Cognito::UserPoolUser](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpooluser.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpooluser.html")

Use the `AWS::Cognito::UserPoolUser` resource to
 create an Amazon Cognito user pool user.

[AWS::Cognito::UserPoolUserToGroupAttachment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolusertogroupattachment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolusertogroupattachment.html")

Use the `AWS::Cognito::UserPoolUserToGroupAttachment`
 resource to attach a user to an Amazon Cognito user pool group.

 | 2010-05-15 |
| Updated resources | April 28, 2017 | 

[SourceDetails](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configrule-source-sourcedetails.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-configrule-source-sourcedetails.html")

Use the `MaximumExecutionFrequency` subproperty of
 the `AWS::Config::ConfigRule` resource to run
 evaluations for a custom rule using a periodic trigger.

[AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")

We now support Elastic Volumes for Amazon Elastic Block Store (Amazon EBS) in
 CloudFormation. We now support `No interruption` updates on
 three properties: `VolumeType`, `Size`, and
 `Iops`.

[AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html")

Use the `GroupName` property to specify a name for
 your Amazon EC2 security group.

[AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html")

There are three new properties for
 `AWS::ECS::Service`:
 `PlacementConstraints`,
 `PlacementStrategies`, and
 `ServiceName`.

[AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")

Use the `PlacementConstraints` property to define
 placement constraints for tasks in the service.

[AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html")

Added the `ConfigurationEndPoint.Address` attribute
 and the `ConfigurationEndPoint.Port` attribute to the
 `Fn::GetAtt` intrinsic function.

[AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html")

Use the `IpAddressType` property to specify the type
 of IP addresses that are used by the load balancer's
 subnets.

[AWS::EMR::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html")

CloudFormation now supports Auto Scaling for Amazon EMR clusters.

[AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html")

Use the `ManagedPolicyName` property to specify a
 custom name for your IAM managed policy.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `Tags` property to add tags to your Lambda
 function.

[AWS::OpsWorks::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html")

Added the following attributes to the `Fn::GetAtt`
 intrinsic function: `AvailabilityZone`,
 `PrivateDnsName`, `PrivateIp`, and
 `PublicDnsName`.

[AWS::OpsWorks::UserProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-userprofile.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-userprofile.html")

Use the `SshUsername` property to specify a user's
 SSH name.
Added the `SshUsername` attribute to the
 `Fn::GetAtt` intrinsic function.

[AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html")

Use the `IamRoles` property to provide a list of one
 or more AWS Identity and Access Management roles that the Amazon Redshift cluster can use to access
 other AWS services.

 | 2010-05-15 |
| Edit templates in YAML and JSON using AWS CloudFormation Designer | April 6, 2017 | When you create CloudFormation templates using Designer, you can now
 edit your template in both YAML and JSON in the integrated editor. You can
 also convert JSON templates to YAML and vice-versa, depending on your
 preferred template authoring language. For more information, see [What Is
 CloudFormation Designer?](working-with-templates-cfn-designer.md "working-with-templates-cfn-designer.md"). | 2010-05-15 |
| New resource | April 6, 2017 | 

[AWS::SSM::Parameter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-parameter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-parameter.html")

Use the `AWS::SSM::Parameter` resource to create an
 SSM parameter in Parameter Store.

 | 2010-05-15 |
| `AWS::Include` transform | March 28, 2017 | Use the `AWS::Include` transform to reference reusable
 snippets stored in an Amazon S3 bucket. For more information, see [AWS::Include Transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-include.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-include.html"). | 2010-05-15 |
| Peer your Amazon VPC with another account | March 28, 2017 | You can now use CloudFormation to peer your Amazon VPC with a VPC in another AWS
 account. For more information, see [Peer with an Amazon
 VPC in Another AWS Account](peer-with-vpc-in-another-account.md "peer-with-vpc-in-another-account.md"). | 2010-05-15 |
| New resource | March 28, 2017 | 

[AWS::ApiGateway::UsagePlanKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-usageplankey.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-usageplankey.html")

Use the `AWS::ApiGateway::UsagePlanKey` resource to
 associate a usage plan key and determine which users the usage plan
 is applied to.

 | 2010-05-15 |
| Updated resources | March 28, 2017 | 

[AWS::EC2::VPCPeeringConnection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcpeeringconnection.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcpeeringconnection.html")

Use the `PeerOwnerId` property and the
 `PeerRoleArn` property to peer with a VPC in another
 AWS account.
For more information, see [Peer with
 an Amazon VPC in Another AWS Account](peer-with-vpc-in-another-account.md "peer-with-vpc-in-another-account.md").

[AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html")

Use the `InstanceProfileName` property to configure
 an instance profile.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `DeadLetterConfig` property to configure how
 AWS Lambda handles events that it can't process.
Node.js v0.10 is no longer supported for the
 `Runtime` property.

[AWS::Route53::HealthCheck](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html")

There are seven new resource subproperty types for the [HealthCheckConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthcheck-healthcheckconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-healthcheck-healthcheckconfig.html")
`HealthCheckConfig` property:
 `AlarmIdentifier`, `ChildHealthChecks`,
 `EnableSNI`, `HealthThreshold`,
 `InsufficientDataHealthStatus`,
 `Inverted`, and `MeasureLatency`.

[AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html")

Use the `ContentBasedDeduplication` and
 `FifoQueue` properties to create First-In-First-Out
 (FIFO) Amazon Simple Queue Service queues.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

You can now specify IPv6 domain names for your Amazon S3
 buckets.

 | 2010-05-15 |
| New resources  | February 10, 2017 | 

[AWS::StepFunctions::Activity](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-activity.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-activity.html")

Use the `AWS::StepFunctions::Activity` resource to
 create an AWS Step Functions activity.

[AWS::StepFunctions::StateMachine](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-statemachine.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-stepfunctions-statemachine.html")

Use the `AWS::StepFunctions::StateMachine` resource
 to create a Step Functions state machine.

 | 2010-05-15 |
| New intrinsic function | January 17, 2017 | Use the `Fn::Split` function to split a string into a list of
 string values. For more information, see [Fn::Split](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-split.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-split.html"). | 2010-05-15 |
| Console support for listing imports | January 17, 2017 | Use the CloudFormation console to see all of the stacks that are importing an
 exported output value. For more information, see [Listing Stacks That Import an Exported Output Value](using-cfn-stack-exports.md#using-cfn-stack-imports "using-cfn-stack-exports.md#using-cfn-stack-imports"). | 2010-05-15 |
| Updated resources | January 17, 2017 | 

[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")

The `LoadBalancerNames` property can be updated
 without replacing the Auto Scaling group.

[AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")

Added the `NetworkMode` and
 `MemoryReservation` properties.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html")

CloudFormation supports updates to the `Tags`
 property.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

Added the `Timezone` property.

[FirehoseAction](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-firehoseaction.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-topicrule-firehoseaction.html")

Added the `Separator` property.

[AWS::OpsWorks::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html")

Added the `PublicIp` attribute for the
 `Fn::GetAtt` intrinsic function.

 | 2010-05-15 |
| New resources | December 01, 2016 | 

[AWS::CodeBuild::Project](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codebuild-project.html")

Use the `AWS::CodeBuild::Project` resource to create
 an AWS CodeBuild project that defines how CodeBuild builds your source
 code.

[AWS::SSM::Association](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-association.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-association.html")

Use the `AWS::SSM::Association` resource to associate
 an Amazon EC2 Systems Manager document with EC2 instances.

[AWS::EC2::SubnetCidrBlock](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnetcidrblock.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnetcidrblock.html")

Use the `AWS::EC2::SubnetCidrBlock` resource to
 associate a single IPv6 CIDR block with an Amazon VPC subnet.

[AWS::EC2::VPCCidrBlock](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpccidrblock.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpccidrblock.html")

Use the `AWS::EC2::VPCCidrBlock` resource to
 associate a single Amazon-provided IPv6 CIDR block with an
 Amazon VPC.

 | 2010-05-15 |
| Updated resources for IPv6 support | December 01, 2016 | 

[AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")

Added the `Ipv6AddressCount` and
 `Ipv6Addresses` properties.

[AWS::EC2::NetworkAclEntry](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-acl-entry.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-acl-entry.html")

Added the `Ipv6CidrBlock` property.

[AWS::EC2::NetworkInterface](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-interface.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-interface.html")

Added the `Ipv6AddressCount` and
 `Ipv6Addresses` properties.

[AWS::EC2::Route](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html")

Added the `DestinationIpv6CidrBlock` property.

[AWS::EC2::SecurityGroupEgress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html")

Added the `CidrIpv6` property.

[AWS::EC2::SecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html")

Added the `CidrIpv6` property.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

Added the `Ipv6AddressCount` and
 `Ipv6Addresses` properties for the launch
 specification network interfaces.

[AWS::EC2::Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html")

Added the `Ipv6CidrBlocks` attribute for the
 `Fn::GetAtt` function.

[AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html")

Added the `Ipv6CidrBlocks` attribute for the
 `Fn::GetAtt` function.

[AWS::SSM::Document](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-document.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-document.html")

Added the `DocumentType` property.

 | 2010-05-15 |
| Resource specification | November 22, 2016 | Use the CloudFormation resource specification to builds tools that help you
 create CloudFormation templates. The specification is a machine-readable,
 JSON-formatted text file. For more information, see [CloudFormation Resource Specification](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-resource-specification.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-resource-specification.html"). | 2010-05-15 |
| New resources | November 22, 2016 | 

[AWS::OpsWorks::UserProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-userprofile.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-userprofile.html")

Use the `AWS::OpsWorks::UserProfile` resource to
 configure SSH access for users who require access to instances in
 an OpsWorks stack.

[AWS::OpsWorks::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-volume.html")

Use the `AWS::OpsWorks::Volume` resource to register
 an Amazon Elastic Block Store volume with an OpsWorks stack.

 | 2010-05-15 |
| Updated resources | November 22, 2016 | 

[AWS::OpsWorks::App](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-app.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-app.html")

Added the `DataSources` property.

[AWS::OpsWorks::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html")

Added the `BlockDeviceMappings`,
 `AgentVersion`, `ElasticIps`,
 `Hostname`, `Tenancy`, and
 `Volumes` properties.

[AWS::OpsWorks::Layer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html")

Added the `CustomJson` and
 `VolumeConfigurations` properties.

[AWS::OpsWorks::Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html")

Added the `ElasticIps`, `EcsClusterArn`,
 `RdsDbInstances`, `CloneAppIds`,
 `ClonePermissions`, and `SourceStackId`
 properties.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

Added the `CopyTagsToSnapshot` property.

 | 2010-05-15 |
| List imports | November 22, 2016 | List imports of an exported output value to track which CloudFormation stacks
 are importing the value. For more information, see [Listing Stacks That Import an Exported Output Value](using-cfn-stack-exports.md#using-cfn-stack-imports "using-cfn-stack-exports.md#using-cfn-stack-imports"). | 2010-05-15 |
| Transforms | November 17, 2016 | Specify the AWS Serverless Application Model (AWS SAM) that CloudFormation uses to process
 AWS SAM syntax for serverless applications. For more
 information, see [Transform](transform-section-structure.md "transform-section-structure.md"). | 2010-05-15 |
| New resource | November 17, 2016 | 

[AWS::SNS::Subscription](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html")

Use the `AWS::SNS::Subscription` resource to
 subscribe an endpoint to an Amazon Simple Notification Service topic.

 | 2010-05-15 |
| Updated resource | November 17, 2016 | 

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `Environment` property to specify key-value
 pairs (environment variables) that your AWS Lambda function can
 access.
Use the `KmsKeyArn` property to specify an KMS key
 that AWS Lambda uses to encrypt and decrypt environment
 variables.

 | 2010-05-15 |
| New CLI commands | November 17, 2016 | 

[Uploading Local
 Artifacts to an S3 Bucket](using-cfn-cli-package.md "using-cfn-cli-package.md")

Use the `package` command to upload local artifacts
 that are referenced in a CloudFormation template to an S3
 bucket.

[Quickly Deploying
 Templates with Transforms](service_code_examples.md "service_code_examples.md")

Use the `deploy` command to combine the create and
 execute change set actions into a single command. This command is
 useful for quickly creating or updating stacks that contain
 transforms.

 | 2010-05-15 |
| Updated resource | November 03, 2016 | 

[AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html")

For the [DistributionConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-distributionconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-distributionconfig.html") property, use the
 `HttpVersion` property to specify the latest HTTP
 version that viewers can use to communicate with Amazon CloudFront.
For the [ForwardedValues](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-forwardedvalues.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-forwardedvalues.html") property, use the
 `QueryStringCacheKeys` property to specify the query
 string parameters that CloudFront uses to determine which content to
 cache.

 | 2010-05-15 |
| List stack exports | November 03, 2016 | Use the CloudFormation console, API, or AWS CLI to see a list of all the
 exported output values for a region. For more information, see [Exporting Stack Output Values](using-cfn-stack-exports.md "using-cfn-stack-exports.md"). | 2010-05-15 |
| Continuous delivery with stacks | November 03, 2016 | Use AWS CodePipeline to build continuous delivery workflows with CloudFormation
 stacks. For more information, see [Continuous Delivery
 with CodePipeline](continuous-delivery-codepipeline.md "continuous-delivery-codepipeline.md"). | 2010-05-15 |
| Skip resources during rollback | November 03, 2016 | If you have a stack in the `UPDATE_ROLLBACK_FAILED` state, use
 the `ResourcesToSkip` parameter for the
 `ContinueUpdateRollback` action to skip resources that
 CloudFormation can't rollback. For more information, see the Troubleshooting
 section in [Update
 Rollback Failed](troubleshooting-errors-update-rollback-failed.md "troubleshooting-errors-update-rollback-failed.md"). | 2010-05-15 |
| Change sets enhancement | November 03, 2016 | You can [create a new stack using a change set](cfn-console-create-stack.md#cfn-console-create-stacks-changesets "cfn-console-create-stack.md#cfn-console-create-stacks-changesets"). | 2010-05-15 |
| Updated resource | October 12, 2016 | 

[AWS::ElastiCache::CacheCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html")

Update the `CacheNodeType` property without replacing
 the cluster.

[AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html")

You can create a Redis (cluster mode enabled) replication group
 that can contain multiple node groups (shards), each with a primary
 cluster and read replicas.

[AWS::ElastiCache::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-subnetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-subnetgroup.html")

Use the `CacheSubnetGroupName` property to specify a
 name for an Amazon ElastiCache subnet group.

 | 2010-05-15 |
| New resources | October 06, 2016 | 

[AWS::ApiGateway::UsagePlan](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-usageplan.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-usageplan.html")

Use the `AWS::ApiGateway::UsagePlan` resource to
 specify a usage plan for deployed Amazon API Gateway APIs.

[AWS::CodeCommit::Repository](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codecommit-repository.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codecommit-repository.html")

Use the `AWS::CodeCommit::Repository` resource to
 create an CodeCommit repository that's hosted by Amazon Web Services.

 | 2010-05-15 |
| Updated resources | October 06, 2016 | 

[AWS::ApiGateway::Authorizer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-authorizer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-authorizer.html")

Use the `ProviderARNs` property to use Amazon Cognito user
 pools as Amazon API Gateway API authorizers.

[AWS::ApiGateway::Deployment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-deployment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-deployment.html")

The `StageName` property is no longer
 required.

[AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html")

For the `GetAtt` function, use the
 `LoadBalancerArns` attribute to retrieve the Amazon
 Resource Names (ARNs) of the load balancers that route traffic to
 the target group.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

Use the `Domain` and `DomainIAMRoleName`
 properties to use Windows Authentication when users connect to the
 RDS DB instance.

[AWS::EC2::SecurityGroupEgress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html")

Use the `DestinationPrefixListId` property to specify
 the AWS service prefix of an Amazon VPC endpoint.

 | 2010-05-15 |
| Cross-stack reference enhancement | October 06, 2016 | Use intrinsic functions to customize the `Name` value of an
 [export](outputs-section-structure.md "outputs-section-structure.md") or to refer to a value in the `[ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html")` function. | 2010-05-15 |
| CloudFormation service role | September 26, 2016 | Use an AWS Identity and Access Management (IAM) service role for CloudFormation stack operations.
 CloudFormation uses the role's credentials to make calls to stack resources on
 your behalf. For more information, see [AWS CloudFormation service
 role](using-iam-servicerole.md "using-iam-servicerole.md"). | 2010-05-15 |
| New feature | September 19, 2016 | You can use the `Export` output field and the
 `Fn::ImportValue` intrinsic function to have one stack refer
 to resource outputs in another stack. For more information, see [Outputs](outputs-section-structure.md "outputs-section-structure.md"), [Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html"), and [Walkthrough: Refer to Resource Outputs in Another CloudFormation
 Stack](walkthrough-crossstackref.md "walkthrough-crossstackref.md"). | 2010-05-15 |
| YAML support | September 19, 2016 | You can use the YAML format to author CloudFormation templates. YAML also
 allows you to, for example, add comments to your templates or use the short
 form for intrinsic functions. For more information, see [CloudFormation
 template format](template-formats.md "template-formats.md"). | 2010-05-15 |
| New intrinsic function | September 19, 2016 | Use the `Fn::Sub` function to substitute variables in an input
 string with values that you specify. For more information, see [Fn::Sub](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-sub.html"). | 2010-05-15 |
| New resources | September 19, 2016 | 

[AWS::KMS::Alias](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-alias.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-alias.html")

Use the `AWS::KMS::Alias` resource to create an alias
 for an AWS KMS key.

 |  |
| Updated resources | September 19, 2016 | 

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

For the `LaunchSpecifications` property, use the
 `SpotPrice` property to specify a bid price for a
 specific instance type.

[AWS::ECS::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html")

Use the `ClusterName` property to specify a name for
 an Amazon Elastic Container Service cluster.

[AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")

Use the `TaskRoleArn` property to specify an
 AWS Identity and Access Management role that Amazon Elastic Container Service containers use to make AWS calls on
 your behalf.
Use the `Family` property to register a task
 definition to a specific family.

[AWS::Elasticsearch::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html")

Use the `ElasticsearchVersion` property to specify
 which version of Elasticsearch to use.

 | 2010-05-15 |
| New resources | August 11, 2016 | Use the following Elastic Load Balancing Application Load Balancer resources to distribute incoming
 application traffic to multiple targets, such as EC2 instances, in multiple
 Availability Zones:

* [AWS::ElasticLoadBalancingV2::Listener](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.html")
* [AWS::ElasticLoadBalancingV2::ListenerRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listenerrule.html")
* [AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html")
* [AWS::ElasticLoadBalancingV2::TargetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.html")
 | 2010-05-15 |
| Updated resource | August 11, 2016 | 

[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")

Use the `TargetGroupARNs` property to associate the
 Auto Scaling group with one or more Application Load Balancer target groups.

[AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html")

For the load `LoadBalancers` property, use the
 `TargetGroupArn` property to associate an Amazon Elastic Container Service
 service with an Application Load Balancer target group.

 | 2010-05-15 |
| New resources | August 09, 2016 | CloudFormation added the following resources:


[AWS::ApplicationAutoScaling::ScalableTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalabletarget.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalabletarget.html")
 and [AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationautoscaling-scalingpolicy.html")

Use an Application Auto Scaling scaling policy to define when and how a target
 resource scales.

[AWS::CertificateManager::Certificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-certificatemanager-certificate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-certificatemanager-certificate.html")

Provision an AWS Certificate Manager certificate that you can use with other
 AWS services to enable secure connections.

 | 2010-05-15 |
| Updated resources | August 09, 2016 | CloudFormation updated the following resources:


[AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html")

For the distribution configuration
 `ViewerCertificate` property, you can specify an
 AWS Certificate Manager certificate. For the distribution configuration
 `Origin` property, you can specify custom headers and
 the SSL protocols for custom origins.

[AWS::EFS::FileSystem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-filesystem.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-filesystem.html")

You can specify the performance mode for an Amazon Elastic File System file
 system.

 | 2010-05-15 |
| New resources | July 20, 2016 | 

AWS IoT

Use AWS IoT to declare an AWS IoT policy, an X.509 certificate, an
 association between a policy and a principal (an X.509 certificate
 or other credential), an AWS IoT thing, an association between a
 principal and a thing, or an AWS IoT rule.

* [AWS::IoT::Certificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-certificate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-certificate.html")
* [AWS::IoT::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-policy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-policy.html")
* [AWS::IoT::PolicyPrincipalAttachment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-policyprincipalattachment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-policyprincipalattachment.html")
* [AWS::IoT::Thing](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-thing.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-thing.html")
* [AWS::IoT::ThingPrincipalAttachment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-thingprincipalattachment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-thingprincipalattachment.html")
* [AWS::IoT::TopicRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iot-topicrule.html")


 | 2010-05-15 |
| Updated resources | July 20, 2016 | CloudFormation updated the following resources:


[AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html"), [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html"), [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html")

Use the name properties to specify a custom name for AWS Identity and Access Management
 (IAM) resources.

[AWS::ApiGateway::Method](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html")

For the `Integration`  property, you can use the
 `PassthroughBehavior` property to specify when
 Amazon API Gateway passes requests to the targeted back end.

[AWS::ApiGateway::Model](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-model.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-model.html") and [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html")

You can specify JSON objects for the `Schema` and
 `Body` properties.

 | 2010-05-15 |
| Auto Scaling group UpdatePolicy | June 9, 2016 | For the `UpdatePolicy` attribute, use the
 `AutoScalingReplacingUpdate` property to specify whether an
 Auto Scaling group and the instances it contains are replaced when you update the
 Auto Scaling group. During a replacement, CloudFormation retains the old Auto Scaling group
 until it creates the new one successfully so that CloudFormation can roll back
 to the old Auto Scaling group if the update fails. For more information, see [UpdatePolicy Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html"). | 2010-05-15 |
| New resource | June 9, 2016 | CloudFormation added the following resources:


[AWS::EC2::FlowLog](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-flowlog.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-flowlog.html")

Creates an Amazon Elastic Compute Cloud flow log that captures IP traffic for a
 specified network interface, subnet, or VPC.

[AWS::KinesisFirehose::DeliveryStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisfirehose-deliverystream.html")

Creates a delivery stream that delivers real-time streaming data
 to a destination, such as Amazon Simple Storage Service, Amazon Redshift, or Amazon OpenSearch Service.

 | 2010-05-15 |
| Updated resources | June 9, 2016 | CloudFormation updated the following resources:


[AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html")

Use the `Name` property to specify a name for an
 Amazon Kinesis stream.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

For the `Code` property, you can use the
 `ZipFile` property and cfn response module for
 `nodejs4.3` runtime environments.

[AWS::SNS::Topic](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html")

CloudFormation enabled updates for the Amazon Simple Notification Service topic
 resource.

 | 2010-05-15 |
| New resource | April 25, 2016 | Use the [AWS::EC2::Host](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-host.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-host.html") resource to allocate a fully
 dedicated physical server for launching EC2 instances. | 2010-05-15 |
| Updated resources | April 25, 2016 | 

[AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")

Use the `Affinity` and `HostId` properties
 to launch instances onto an Amazon Elastic Compute Cloud dedicated host.

[AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html")

Use the `DeploymentConfiguration` property to
 configure how many tasks can run during a deployment.

[AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html")

CloudFormation added support for additional Amazon Elastic Container Service container
 definition properties.

[AWS::GameLift::Fleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-fleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-fleet.html")

Use the `MaxSize` and `MinSize` properties
 to specify the maximum and minimum number of EC2 instances allowed
 in your Amazon GameLift Servers fleet.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `FunctionName` property to specify a name for
 your AWS Lambda function. You can also use Python 2.7 to specify an
 inline function.

 | 2010-05-15 |
| New resources | April 18, 2016 | 

Amazon API Gateway

Use the Amazon API Gateway resources to publish, maintain, and monitor
 APIs at any scale. You can create APIs that clients can call to
 access your back-end services, such as applications running EC2
 instances or code running on AWS Lambda.

* [AWS::ApiGateway::Account](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-account.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-account.html")
* [AWS::ApiGateway::ApiKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-apikey.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-apikey.html")
* [AWS::ApiGateway::Authorizer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-authorizer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-authorizer.html")
* [AWS::ApiGateway::BasePathMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-basepathmapping.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-basepathmapping.html")
* [AWS::ApiGateway::ClientCertificate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-clientcertificate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-clientcertificate.html")
* [AWS::ApiGateway::Deployment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-deployment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-deployment.html")
* [AWS::ApiGateway::Method](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-method.html")
* [AWS::ApiGateway::Model](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-model.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-model.html")
* [AWS::ApiGateway::Resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-resource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-resource.html")
* [AWS::ApiGateway::RestApi](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-restapi.html")
* [AWS::ApiGateway::Stage](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-stage.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigateway-stage.html")


[AWS::Events::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-events-rule.html")

Create an Amazon CloudWatch Events rule that monitors changes to AWS
 resources in your account (events). If an incoming event matches
 the conditions that you described in the rule, Amazon CloudWatch Events sends
 messages to and activates your specified targets, such as AWS Lambda
 functions or Amazon Simple Notification Service topics.

[AWS::WAF::SizeConstraintSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-sizeconstraintset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-sizeconstraintset.html") and [AWS::WAF::XssMatchSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-xssmatchset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-xssmatchset.html")

Use the two AWS WAF rules to check the size of a web request or to
 prevent cross-site scripting attacks.

 | 2010-05-15 |
| New resources | March 31, 2016 | Use the [AWS::Lambda::Alias](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-alias.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-alias.html") resource to create aliases
 for your AWS Lambda functions and the [AWS::Lambda::Version](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-version.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-version.html") resource to create
 versions of your functions. | 2010-05-15 |
| Updated resources | March 31, 2016 | CloudFormation updated the following resources:


[AWS::EMR::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html") and [AWS::EMR::InstanceGroupConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-instancegroupconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-instancegroupconfig.html")

Use the `EbsConfiguration` property to configure
 Amazon Elastic Block Store storage volumes for your Amazon EMR clusters or instance
 groups.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use the `VpcConfig` property to enable AWS Lambda
 functions to access resources in a VPC.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

For the Amazon Simple Storage Service life cycle rules, you can specify multiple
 transition rules that specify when objects transition to a
 specified storage class.

 | 2010-05-15 |
| Change sets | March 29, 2016 | Before updating stacks, use change sets to see how your changes might
 affect your running resources. For more information, see [Updating Stacks
 Using Change Sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md"). | 2010-05-15 |
| New resources | March 15, 2016 | Use the [AWS::GameLift::Alias](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-alias.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-alias.html"), [AWS::GameLift::Build](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-build.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-build.html"), and [AWS::GameLift::Fleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-fleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-gamelift-fleet.html") resources to deploy
 multiplayer game servers in AWS. | 2010-05-15 |
| New resources | February 26, 2016 | CloudFormation added the following resources:


[AWS::ECR::Repository](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-repository.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecr-repository.html")

Create Amazon Elastic Container Registry repositories where users can push and pull
 Docker images.

[AWS::EC2::NatGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-natgateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-natgateway.html")

Use the network address translator (NAT) gateway to enable EC2
 instances in a private subnet to connect to the Internet.

[AWS::Elasticsearch::Domain](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html")

Create Amazon OpenSearch Service domains that run legacy Elasticsearch OSS
 clusters.

[AWS::EMR::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-cluster.html"), [AWS::EMR::InstanceGroupConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-instancegroupconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-instancegroupconfig.html"), [AWS::EMR::Step](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-step.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emr-step.html")

Use the Amazon EMR resources to assist you analyze and process
 vast amounts of data. You can create clusters and then run jobs on
 them.

 | 2010-05-15 |
| Updated resources | February 26, 2016 | CloudFormation updated the following resources:


[AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html")

Use the `IsMultiRegionTrail` property to specify
 whether to create an AWS CloudTrail trail in the region in which you
 create a stack or in all regions.

[AWS::Config::ConfigurationRecorder](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationrecorder.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationrecorder.html")

For the recording group, use the
 `IncludeGlobalResourceTypes` property to record all
 global resource types.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html")

Use the `KmsKeyId` and `StorageEncrypted`
 properties to encrypt database instances in the cluster.

 | 2010-05-15 |
| Retain resources | February 26, 2016 | For stacks in the `DELETE_FAILED` state, use the
 `RetainResources` parameter to retain resources that
 CloudFormation can't delete. For more information, see [Delete Stack Fails](troubleshooting.md#troubleshooting-errors-delete-stack-fails "troubleshooting.md#troubleshooting-errors-delete-stack-fails"). | 2010-05-15 |
| Update stack tags | February 26, 2016 | You can add, modify, or remove stack tags when you update a stack. For
 more information, see [CloudFormation Stacks Updates](stacks.md "stacks.md"). | 2010-05-15 |
| Continue rolling back failed update rollbacks | January 25, 2016 | For a stack in the `UPDATE_ROLLBACK_FAILED` state, you can
 continue rolling back the update to get your stack in a working state. That
 way, you can return the stack to its original settings and try to update it
 again. For more information, see [Continue Rolling Back an Update](using-cfn-updating-stacks-continueupdaterollback.md "using-cfn-updating-stacks-continueupdaterollback.md"). | 2010-05-15 |
| New sample templates available for the Asia Pacific (Seoul)
 region. | January 7, 2016 | The following collection of CloudFormation sample templates are for the
 ap-northeast-2 region:

* Sample Solutions
* Application Frameworks
* Services

For more information, see [Working with CloudFormation
 templates](template-guide.md "template-guide.md"). | 2010-05-15 |
| New resources | December 28, 2015 | CloudFormation added the following resources:


[AWS::DirectoryService::MicrosoftAD](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directoryservice-microsoftad.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directoryservice-microsoftad.html")

Use the Microsoft Active Directory resource to create a
 Microsoft Active Directory directory in AWS.

[AWS::Logs::Destination](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-destination.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-destination.html") and [AWS::Logs::LogStream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-logstream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-logstream.html")

Use the Amazon CloudWatch Logs resources to create a destination for
 real-time processing of log data or to create log streams,
 respectively.

[AWS::WAF::ByteMatchSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-bytematchset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-bytematchset.html"), [AWS::WAF::IPSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-ipset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-ipset.html"), [AWS::WAF::Rule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-rule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-rule.html"), [AWS::WAF::SqlInjectionMatchSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-sqlinjectionmatchset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-sqlinjectionmatchset.html"), and
 [AWS::WAF::WebACL](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-webacl.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-waf-webacl.html")

Use the AWS WAF resources to control and monitor web requests
 to your content.

 | 2010-05-15 |
| Resource updates | December 28, 2015 | CloudFormation updated the following resources:


[AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html")

For the distribution configuration, use the
 `WebACLId` property to associate an AWS WAF web access
 control list (ACL) with an Amazon CloudFront distribution. For the cache
 behavior and default cache behavior, you can specify a default and
 maximum Time to Live (TTL) value.

[AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html")

You can create, update, or delete a global secondary index
 without replacing your Amazon DynamoDB table.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

Use the `ReplicationConfiguration` property to
 specify which objects to replicate and where they are
 stored.
Use the properties in the `NotificationConfiguration`
 property to specify filters so that Amazon Simple Storage Service sends notifications
 for objects that you specify.

 | 2010-05-15 |
| Parameter grouping and sorting | December 3, 2015 | Use the [AWS::CloudFormation::Interface](aws-cloudformation-interface.md "aws-cloudformation-interface.md") metadata key to
 group and sort parameters in the CloudFormation console when users create or
 update a stack with your template. | 2010-05-15 |
| Update policy attribute | December 3, 2015 | For an Auto Scaling [update policy
 attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html"), use the `MinSuccessfulInstancesPercent`
 property to specify the percentage of instances that must signal success for
 a successful update. | 2010-05-15 |
| New resources | December 3, 2015 | CloudFormation added the following resources:


[AWS::CodePipeline::Pipeline](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codepipeline-pipeline.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codepipeline-pipeline.html") and [AWS::CodePipeline::CustomActionType](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codepipeline-customactiontype.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codepipeline-customactiontype.html")

Use the CodePipeline resources to create a pipeline that describes how
 software changes go through a release process.

[AWS::Config::ConfigurationRecorder](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationrecorder.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configurationrecorder.html"),
 [AWS::Config::DeliveryChannel](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-deliverychannel.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-deliverychannel.html"), and [AWS::Config::ConfigRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configrule.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-config-configrule.html")

Use the AWS Config resources to monitor configuration changes to
 specific AWS resources.

[AWS::KMS::Key](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-key.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kms-key.html")

Use the AWS Key Management Service (AWS KMS) resource to create customer managed keys in
 AWS KMS that users can use to encrypt small amounts of data.

[AWS::SSM::Document](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-document.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-document.html")

Use the Amazon EC2 Systems Manager to create a document that specifies
 on-instance configurations.

 | 2010-05-15 |
| Resources update | December 3, 2015 | CloudFormation updated the following resources:


[AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html")

Specify whether EBS volumes are encrypted.

[AWS::AutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html")

You can use two different policy types (simple and step scaling)
 to specify how an Auto Scaling group scales when an Amazon CloudWatch (CloudWatch) alarm
 is breached.

[AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html")

Use the CloudWatch properties to send logs to a CloudWatch log group. You
 can add tags to a trail and specify an AWS KMS key that you want
 to use to encrypt logs.

[AWS::CodeDeploy::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-application.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-application.html"), [AWS::CodeDeploy::DeploymentConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentconfig.html"), and
 [AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html")

Use the `ApplicationName`,
 `DeploymentConfigName`, and
 `DeploymentGroupName` properties to specify custom
 names for CodeDeploy resources.

[AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html")

Use the `StreamSpecification` property to specify
 settings for capturing changes to items stored in an Amazon DynamoDB
 (DynamoDB) table.

[AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")

Use the `SsmAssociations` property to associate an
 Amazon EC2 Systems Manager document with an instance.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

Use the `AllocationStrategy` property to specify how
 to allocate target capacity across Spot pools. Use the
 `ExcessCapacityTerminationPolicy` property to specify
 how instances are terminated if the target capacity is below the
 size of the Spot fleet.

[AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html")

Use the `KmsKeyId` property to specify an
 AWS KMS key to encrypt data in an Amazon Redshift cluster.

[AWS::WorkSpaces::Workspace](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspace.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspace.html")

Use the encryption properties to encrypt data stored on
 volumes.

 | 2010-05-15 |
| Resource update | November 4, 2015 | For the [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html") resource, use the
 `AutoEnableIO` property to automatically resume I/O operations
 if a volume's data becomes inconsistent. | 2010-05-15 |
| New resources | October 1, 2015 | CloudFormation added the following resources:


[AWS::CodeDeploy::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-application.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-application.html"), [AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentgroup.html"), and
 [AWS::CodeDeploy::DeploymentConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-codedeploy-deploymentconfig.html")

Use the CodeDeploy resources to create and apply deployments to EC2
 or on-premises instances.

[AWS::DirectoryService::SimpleAD](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directoryservice-simplead.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-directoryservice-simplead.html")

Use the Simple Active Directory resource to create an AWS Directory Service
 Simple AD, which is a Microsoft Active Directory-compatible
 directory.

[AWS::EC2::PlacementGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-placementgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-placementgroup.html")

Use a placement group to create a cluster of instances in a
 low-latency network.

[AWS::EC2::SpotFleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-spotfleet.html")

Use a Spot fleet to launch a collection of Spot instances that
 run interruptible tasks.

[AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-eventsourcemapping.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-eventsourcemapping.html")

Use the event source mapping resource to specify a stream as an
 event source for an AWS Lambda (Lambda) function.

[AWS::Lambda::Permission](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-permission.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-permission.html")

Use a Lambda permission to add a statement to a Lambda function's
 policy.

[AWS::Logs::SubscriptionFilter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-subscriptionfilter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-subscriptionfilter.html")

Use the subscription filter to define which log events are
 delivered to your Kinesis stream.

[AWS::RDS::DBCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbcluster.html") and [AWS::RDS::DBClusterParameterGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbclusterparametergroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbclusterparametergroup.html")

Use the cluster and cluster parameter group resources to create
 an Amazon Aurora DB cluster.

[AWS::WorkSpaces::Workspace](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspace.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspace.html")

Use WorkSpaces to create cloud-based desktop experiences.

 | 2010-05-15 |
| Resource updates | October 1, 2015 | CloudFormation updated the following resources:


[AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html")

Use the `Fn::GetAtt` intrinsic function to get a list
 of read-only replica addresses and ports.

[AWS::OpsWorks::Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html")

Use the `AgentVersion` property to specify a
 particular OpsWorks agent.

[AWS::OpsWorks::App](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-app.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-app.html")

Use the `Environment` property to specify environment
 variables for an OpsWorks app.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

For the [NotificationConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-notificationconfig.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-notificationconfig.html") property, you can configure
 notification settings for Lambda functions and Amazon Simple Queue Service (Amazon SQS)
 queues.

 | 2010-05-15 |
| IAM condition keys | October 1, 2015 | For AWS Identity and Access Management (IAM) policies, use CloudFormation-specific condition keys to
 specify when an IAM policy takes effect. For more information, see [Controlling Access with AWS Identity and Access
 Management](control-access-with-iam.md "control-access-with-iam.md"). | 2010-05-15 |
| AWS CloudFormation Designer | October 1, 2015 | Use [AWS CloudFormation Designer](working-with-templates-cfn-designer.md "working-with-templates-cfn-designer.md") to create and modify templates using a drag-and-drop
 interface. | 2010-05-15 |
| New resource | August 24, 2015 | Use the [AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcendpoint.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcendpoint.html") resource to establish a
 private connection between your VPC and another AWS service. | 2010-05-15 |
| Resource updates | August 24, 2015 | CloudFormation updated the following resources:


[AWS::ElasticBeanstalk::Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html")

Use the `Tags` property to specify tags (key-value
 pairs) for an AWS Elastic Beanstalk (Elastic Beanstalk) environment.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

For the [Code](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-code.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-code.html") property, use the
 `ZipFile` property to write the source code of your
 Lambda function directly in a template. Currently, you can use the
 `ZipFile` property only for `nodejs`
 runtime environments. You can still point to a file in an S3 bucket
 for all runtime environments, such as `java8` and
 `nodejs`.

[AWS::OpsWorks::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html")

Use the `EbsOptimized` property to indicate whether
 an instance is optimized for Amazon Elastic Block Store (Amazon EBS) I/O.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

For the `SourceDBInstanceIdentifier` property, you
 can specify a database instance in another region to create a
 cross-region read replica.

 | 2010-05-15 |
| Amazon S3 template URL | August 24, 2015 | For versioning-enabled buckets, you can specify a version ID in an Amazon S3
 template URL when you create or update a stack, such as
 `https://s3.amazonaws.com/templates/myTemplate.template?versionId=123ab1cdeKdOW5IH4GAcYbEngcpTJTDW`. | 2010-05-15 |
| New resource | August 3, 2015 | Use the [AWS::EFS::FileSystem](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-filesystem.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-filesystem.html") resource to create an
 Amazon Elastic File System (Amazon EFS) file system and the [AWS::EFS::MountTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-mounttarget.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-efs-mounttarget.html") resource to create a
 mount point for a file system. | 2010-05-15 |
| Permission requirement change | June 11, 2015 | When you create or update an [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") resource, you must now
 also have permission to call the `ec2:DescribeAccountAttributes`
 action. | 2010-05-15 |
| New resources | June 11, 2015 | CloudFormation added the following resources:


[AWS::DataPipeline::Pipeline](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datapipeline-pipeline.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datapipeline-pipeline.html")

Use data pipelines to automate the movement and transformation
 of data.

Amazon Elastic Container Service resources

Use the [AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-service.html"), [AWS::ECS::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-cluster.html"), and [AWS::ECS::TaskDefinition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ecs-taskdefinition.html") resources to
 create Docker containers on a cluster of EC2 instances.

[AWS::ElastiCache::ReplicationGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html")

Use replication groups to create a collection of nodes with one
 primary read-write cluster and a maximum of five secondary
 read-only clusters.

[AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html")

Use managed policies to create policies in your AWS account
 that you can use to apply permissions to IAM users, groups, and
 roles.

[AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html")

Use Lambda functions to run code in response to events.

[AWS::RDS::OptionGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-optiongroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-optiongroup.html")

Use option groups to help you create and manage Amazon Relational Database Service
 (Amazon RDS) databases.

 | 2010-05-15 |
| Resource updates | June 11, 2015 | CloudFormation updated the following resources:


[AWS::EC2::Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html")

Use the `MapPublicIpOnLaunch` property to
 automatically assign public IP addresses to instances in a
 subnet.

[AWS::ElastiCache::CacheCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html")

Use the `SnapshotName` property to restore snapshot
 data into a new Redis cache cluster.

[AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html")

For the `LoginProfile` property, use the
 `PasswordResetRequired` property so that users are
 required to set a new password when they log in to the
 AWS Management Console.

[AWS::OpsWorks::Layer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html")

Use the `LifecycleEventConfiguration` property to
 configure lifecycle events for an OpsWorks layer.

[AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html")

For the `LifecycleConfiguration` property, use the
 `NoncurrentVersionExpirationInDays` and
 `NoncurrentVersionTransition` properties to specify
 lifecycle rules for non-current object versions.

 | 2010-05-15 |
| New parameter types | May 19, 2015 | Whenever you use the CloudFormation console to create or update a stack, you
 can search for AWS-specific parameter type values by ID, name, or Name tag
 value.
CloudFormation also added support for the following AWS-specific parameter
 types. For more information, see [Parameters](parameters-section-structure.md "parameters-section-structure.md").

* `AWS::EC2::AvailabilityZone::Name`
* `List<`AWS::EC2::AvailabilityZone`::Name>`
* `AWS::EC2::Instance::Id`
* `List<`AWS::EC2::Instance`::Id>`
* `AWS::EC2::Image::Id`
* List<`AWS::EC2::Image::Id`>
* `AWS::EC2::SecurityGroup::GroupName`
* List<`AWS::EC2::SecurityGroup::GroupName`>
* `AWS::EC2::Volume::Id`
* List<`AWS::EC2::Volume::Id`>
* `AWS::Route53::HostedZone::Id`
* `List<`AWS::Route53::HostedZone`::Id>`
 | 2010-05-15 |
| New resources | April 16, 2015 | CloudFormation added the following resources:


[AWS::AutoScaling::LifecycleHook](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-lifecyclehook.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-lifecyclehook.html")

Use Auto Scaling lifecycle hooks to control the state of an instance
 after it is launched or terminated.

[AWS::RDS::EventSubscription](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-eventsubscription.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-eventsubscription.html")

Use event subscriptions to get notifications about Amazon RDS
 events.

 | 2010-05-15 |
| Resource updates | April 16, 2015 | CloudFormation updated the following resources:


[AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")

Use the `NotificationConfigurations` property to
 specify multiple notifications.

[AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html")

Use the `PlacementTenancy` property to specify the
 tenancy of instances.
Use the `ClassicLinkVPCId` and
 `ClassicLinkVPCSecurityGroups` properties to link
 EC2-Classic instances to a ClassicLink-enabled VPC.

[AWS::AutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scalingpolicy.html")

Use the `MinAdjustmentStep` property to specify the
 minimum number of instances that are added or removed during a
 scaling event.

[AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html")

For viewer certificates, use the
 `MinimumProtocolVersion` property to specify a
 minimum protocol version. For cache behaviors, use the
 `CachedMethods` property to specify which methods
 Amazon CloudFront (CloudFront) caches responses for. For origins, use the
 `OriginPath` to specify a path that CloudFront uses to
 request content.

[AWS::ElastiCache::CacheCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html")

For Memcached cache clusters, use the `AZMode` and
 `PreferredAvailabilityZones` properties to specify
 nodes in multiple Availability Zones (AZs).

[AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html")

Use the `KmsKeyId` property to specify a customer managed key
 for encrypted volumes.

[AWS::OpsWorks::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-instance.html")

Use the `TimeBasedAutoScaling` property to
 automatically scale instances based on a schedule that you
 specify.

[AWS::OpsWorks::Layer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-layer.html")

Use the `LoadBasedAutoScaling` property to specify
 load-based scaling policies. For volume configurations, use the
 `VolumeType` and `Iops` properties to
 specify a volume type and the number of I/O operations per second,
 respectively.

[AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html")

Use the `CharacterSetName` property to specify a
 character set for supported database engines.
Use the `StorageEncrypted` property to indicate
 whether database instances will be encrypted and the
 `KmsKeyId` to specify a customer managed key for encrypted
 database instances.

[AWS::Route53::HealthCheck](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html")

Use the `HealthCheckTags` property to associate tags
 with health checks.

[AWS::Route53::HostedZone](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html")

Use the `VPCs` property to create private hosted
 zones.
Use the `HostedZoneTags` property to associate tags
 with hosted zones.

 | 2010-05-15 |
| New template section | April 16, 2015 | Add the [Metadata](metadata-section-structure.md "metadata-section-structure.md") section
 to your templates to include arbitrary JSON objects that describe your
 templates, such as the design or implementation details. | 2010-05-15 |
| Resource update | April 8, 2015 | For the [AWS::CloudFormation::CustomResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html") resource,
 you can specify Lambda function Amazon Resource Names (ARNs) in the
 `ServiceToken` property. | 2010-05-15 |
| Amazon RDS update | December 24, 2014 | CloudFormation added two new properties for RDS DB instances. You can
 associate an option group with a DB instance and specify the DB instance
 storage type. For more information, see [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html"). | 2010-05-15 |
| Elastic Load Balancing update | December 24, 2014 | You can use the `ConnectionSettings` property to specify how
 long connections can remain idle. For more information, see [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html"). | 2010-05-15 |
| Route 53 update | November 6, 2014 | You can now provision and manage Route 53 [hosted
 zones](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-hostedzone.html") , [health
 checks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-healthcheck.html"), [failover record
 sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordset.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordset.html") , and [geolocation record sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordset-geolocation.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-recordset-geolocation.html") . | 2010-05-15 |
| Auto Scaling rolling update enhancement | November 6, 2014 | During an update, you can use the `WaitOnResourceSignals` flag
 to instruct CloudFormation to wait for instances to signal success. That way,
 CloudFormation won't update the next batch of instances until the current batch
 is ready. For more information, see [UpdatePolicy
 Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html"). | 2010-05-15 |
| New VPC Fn:GetAtt attributes | November 6, 2014 | Given a VPC ID, you can retrieve the default security group and network
 ACL for that VPC. For more information, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html"). | 2010-05-15 |
| New AWS-specific parameter types | November 6, 2014 | You can specify AWS-specific parameter types in your CloudFormation
 templates. In the CloudFormation console, these parameter types provide a
 drop-down list of valid values. With the API or AWS CLI, CloudFormation can
 quickly validate values for these parameter types before creating or
 updating a stack. For more information, see [Parameters](parameters-section-structure.md "parameters-section-structure.md"). | 2010-05-15 |
| CreationPolicy attribute | November 6, 2014 | With the CreationPolicy attribute, you can instruct CloudFormation to wait
 until applications are ready on EC2 instances before proceeding with stack
 creation. You can use a creation policy instead of a wait condition and wait
 condition handle. For more information, see [CreationPolicy
 Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-creationpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-creationpolicy.html"). | 2010-05-15 |
| Amazon CloudFront forwarded values | September 29, 2014 | For cache behaviors, you can forward headers to the origin. See [ForwardedValues](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-forwardedvalues.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudfront-distribution-forwardedvalues.html"). | 2010-05-15 |
| AWS OpsWorks update | September 29, 2014 | For Chef 11.10, you can use the `ChefConfiguration` property
 to enable Berkshelf. You can also use the AWS OpsWorks built-in security groups
 with your AWS OpsWorks stacks. For more information, see [AWS::OpsWorks::Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html"). | 2010-05-15 |
| Elastic Load Balancing tagging support | September 29, 2014 | AWS CloudFormation tags Elastic Load Balancing load balancers with stack-level tags. You can
 also add your own tags to a load balancer. See [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html"). | 2010-05-15 |
| Amazon Simple Notification Service topic policy update | September 29, 2014 | You can now update Amazon SNS topic policies. For more information, see [AWS::SNS::TopicPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topicpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topicpolicy.html"). | 2010-05-15 |
| RDS DB instance update | September 5, 2014 | You can specify whether a DB instance is Internet-facing by using the
 `PubliclyAccessible` property in the [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") resource. | 2010-05-15 |
| UpdatePolicy attribute update | September 05, 2014 | You can specify an update policy for an Auto Scaling group that has an associated
 scheduled action. For more information, see [UpdatePolicy
 Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html"). | 2010-05-15 |
| Amazon CloudWatch support | July 10, 2014 | You can use CloudFormation to provision and manage Amazon CloudWatch Logs (CloudWatch Logs) log
 groups and metric filters. For more information, see [AWS::Logs::LogGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-loggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-loggroup.html") or [AWS::Logs::MetricFilter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-metricfilter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-metricfilter.html"). | 2010-05-15 |
| Amazon CloudFront distribution configuration update | June 17, 2014 | You can specify additional CloudFront distribution configuration
 properties:

* Custom error responses define custom error messages for 4xx and 5xx
 HTTP status codes.
* Price class defines the maximum price that you want to pay for the
 CloudFront service.
* Restrictions define who can view your content.
* Viewer certificate specifies the certificate to use when viewers
 use HTTPS.
* For cache behaviors, you can specify allowed HTTP methods and
 indicate whether to forward cookies.

For more information, see [AWS::CloudFront::Distribution](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudfront-distribution.html"). | 2010-05-15 |
| EC2 instance update | June 17, 2014 | You can specify whether an instance stops or terminates when you invoke
 the instance's operating system shutdown command. For more information, see
 [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html"). | 2010-05-15 |
| EBS volume update | June 17, 2014 | You can use encrypted EBS volumes with supported instance types. For more
 information, see [AWS::EC2::Volume](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-volume.html"). | 2010-05-15 |
| New Amazon VPC peering connection | June 17, 2014 | You can use CloudFormation to create an Amazon Virtual Private Cloud (Amazon VPC) peering connection,
 which establishes a network connection between two VPCs. For more
 information, see [AWS::EC2::VPCPeeringConnection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcpeeringconnection.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcpeeringconnection.html"). | 2010-05-15 |
| Amazon EC2 Auto Scaling group update | June 17, 2014 | You can specify an existing cluster placement group in which to launch
 instances for an Amazon EC2 Auto Scaling group. For more information, see [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html"). | 2010-05-15 |
| AWS CloudTrail support | June 17, 2014 | CloudFormation supports AWS CloudTrail, which can capture API calls made from your
 AWS account and publish the logs at a location you designate. For more
 information, see [AWS::CloudTrail::Trail](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudtrail-trail.html"). | 2010-05-15 |
| Update stack enhancements | May 12, 2014 | CloudFormation supports additional features for updating stacks:

* You can update CloudFormation stack parameters without resubmitting the
 stack's template.
* You can add or remove Amazon SNS notification topics for an CloudFormation
 stack.

For more information, see [CloudFormation Stacks Updates](stacks.md "stacks.md"). | 2010-05-15 |
| Amazon Kinesis support | May 6, 2014 | You can use CloudFormation to create Amazon Kinesis streams that capture and
 transport data records from data sources. For more information, see [AWS::Kinesis::Stream](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html"). | 2010-05-15 |
| New S3 bucket properties | May 5, 2014 | CloudFormation supports additional S3 bucket properties:

* Cross-origin resource sharing (CORS) defines cross-origin resource
 sharing of objects in a bucket.
* Lifecycle defines how Amazon S3 manages objects during their
 lifetime.
* Access logging policy captures information about requests made to
 your bucket.
* Notifications define which events to report and which Amazon SNS topic
 to send messages to.
* Versioning enables multiple variants of all objects in a
 bucket.
* Redirect and routing rules govern redirect behavior for requests
 made to a bucket's website endpoint.

For more information, see [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html"). | 2010-05-15 |
| Amazon EC2 Auto Scaling support | May 5, 2014 | CloudFormation supports metrics collection for an Auto Scaling group. For more
 information, see [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html"). | 2010-05-15 |
| `Fn::If` update | May 5, 2014 | You can use the `Fn::If` intrinsic function in the output
 section of a template. For more information, see [Condition
 Functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-conditions.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-conditions.html"). | 2010-05-15 |
| API logging with AWS CloudTrail | April 2, 2014 | You can use AWS CloudTrail (CloudTrail) to log CloudFormation requests. With CloudTrail you can
 get a history of CloudFormation API calls for your account. For more
 information, see [Logging CloudFormation API
 Calls with AWS CloudTrail](cfn-api-logging-cloudtrail.md "cfn-api-logging-cloudtrail.md"). | 2010-05-15 |
| Elastic Load Balancing update | March 20, 2014 | You can specify an access logging policy to capture information about
 requests made to your load balancer. You can also specify a connection
 draining policy that describes how to handle in-flight requests when
 instances are deregistered or become unhealthy. For more information, see
 [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html"). | 2010-05-15 |
| OpsWorks support | March 3, 2014 | You can use CloudFormation to provision and manage OpsWorks stacks. For more
 information, see [AWS::OpsWorks::Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opsworks-stack.html") or [AWS
 OpsWorks Template Snippets](quickref-opsworks.md "quickref-opsworks.md"). | 2010-05-15 |
| Amazon S3 template size limit increase | February 18, 2014 | You can specify template sizes up to 460,800 bytes in Amazon S3. | 2010-05-15 |
| Amazon Redshift support | February 10, 2014 | You can use CloudFormation to provision and manage Amazon Redshift clusters. For more
 information, see [Amazon Redshift Template
 Snippets](quickref-redshift.md "quickref-redshift.md") or [AWS::Redshift::Cluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-redshift-cluster.html"). | 2010-05-15 |
| S3 buckets and bucket policies update | February 10, 2014 | You can update some properties of the S3 bucket and bucket policy
 resources. For more information, see [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucket.html") or [AWS::S3::BucketPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucketpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucketpolicy.html"). | 2010-05-15 |
| Elastic Beanstalk environments and application versions update | February 10, 2014 | You can update Elastic Beanstalk environment configurations and application versions.
 For more information, see [AWS::ElasticBeanstalk::Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html"), [AWS::ElasticBeanstalk::ConfigurationTemplate](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-beanstalk-configurationtemplate.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-beanstalk-configurationtemplate.html"),
 or [AWS::ElasticBeanstalk::ApplicationVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-applicationversion.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-applicationversion.html"). | 2010-05-15 |
| Amazon SQS update | January 29, 2014 | You can specify a dead letter queue for an Amazon SQS queue. For more
 information, see [AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html"). | 2010-05-15 |
| Auto Scaling scheduled actions | January 27, 2014 | You can scale the number of EC2 instances in an Auto Scaling group based on a
 schedule. By using a schedule, you can scale applications in response to
 predictable load changes. For more information, see [AWS::AutoScaling::ScheduledAction](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scheduledaction.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-scheduledaction.html"). | 2010-05-15 |
| DynamoDB secondary indexes | January 27, 2014 | You can create local and global secondary indexes for DynamoDB databases. By
 using secondary indexes, you can efficiently access data with attributes
 other than the primary key. For more information, see [AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-table.html"). | 2010-05-15 |
| Auto Scaling update | January 2, 2014 | You can specify an instance ID for an Auto Scaling group or launch configuration.
 You can also specify additional Auto Scaling block device properties. For more
 information, see [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html") or [AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html"). | 2010-05-15 |
| Amazon SQS update | January 2, 2014 | You can update SQS queues and specify additional properties. For more
 information, see [AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sqs-queue.html"). | 2010-05-15 |
| Limit increases | January 2, 2014 | You can specify up to 60 parameters and 60 outputs in your CloudFormation
 templates. | 2010-05-15 |
| New console | December 19, 2013 | The new CloudFormation console adds features like auto-refreshing stack
 events and alphabetical ordering of stack parameters. | 2010-05-15 |
| Cross-zone load balancing | December 19, 2013 | With cross-zone load balancing, you can route traffic to back-end
 instances across all Availability Zones (AZs). For more information, see
 [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html"). | 2010-05-15 |
| AWS Elastic Beanstalk environment tiers | December 19, 2013 | You can specify whether AWS Elastic Beanstalk provisions resources to support a web
 server or to handle background processing tasks. For more information, see
 [AWS::ElasticBeanstalk::Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-environment.html"). | 2010-05-15 |
| Resource names | December 19, 2013 | You can assign names (physical IDs) to the following resources:

* ElastiCache clusters
* Elastic Load Balancing load balancers
* RDS DB instances

For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html"). | 2010-05-15 |
| VPN support | November 22, 2013 | You can enable a virtual private gateway (VGW) to propagate routes to the
 routing tables of a VPC. For more information, see [AWS::EC2::VPNGatewayRoutePropagation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-gatewayrouteprop.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-gatewayrouteprop.html"). | 2010-05-15 |
| Conditionally create resources and assign properties | November 8, 2013 | Using input parameters, you can control the creation and settings of
 designated stack resources by defining conditions in your CloudFormation
 templates. For example, you can use conditions to create stack resources for
 a production environment. Using the same template, you can create similar
 stack resources with lower capacity for a test environment. For more
 information, see [Condition
 Functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-conditions.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-conditions.html"). | 2010-05-15 |
| Prevent accidental updates to stack resources | November 8, 2013 | You can prevent stack updates that might result in unintentional changes
 to stack resources. For example, if you have a stack with a database layer
 that should rarely be updated, you can set a stack policy that prevents most
 users from updating that database layer. For more information, see [Prevent
 Updates to Stack Resources](protect-stack-resources.md "protect-stack-resources.md"). | 2010-05-15 |
| Name resources | November 8, 2013 | Instead of using CloudFormation-generated physical IDs, you can assign names
 to certain resources. The following CloudFormation resources support
 naming

* Amazon CloudWatch alarms
* DynamoDB tables
* AWS Elastic Beanstalk applications and environments
* Amazon S3 buckets
* Amazon SNS topics
* Amazon SQS queues

For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html"). | 2010-05-15 |
| Assign custom resource types | November 8, 2013 | In your templates, you can specify your own resource type for CloudFormation
 custom resources (`AWS::CloudFormation::CustomResource`). By
 using your own custom resource type name, you can quickly identify the type
 of custom resources that you have in your stack. For example, you can
 specify `"Type":
 "Custom::`MyCustomResource`"`. For more
 information, see [AWS::CloudFormation::CustomResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html"). | 2010-05-15 |
| Add pseudo parameter | November 8, 2013 | You can now refer to the AWS AccountID inside CloudFormation templates by
 referring to the `AWS::AccountID` pseudo parameter. For more
 information, see [Pseudo Parameters
 Reference](pseudo-parameter-reference.md "pseudo-parameter-reference.md"). | 2010-05-15 |
| Specify stacks in IAM policies | November 8, 2013 | You can allow or deny IAM users, groups, or roles to operate on
 specific CloudFormation stacks. For example, you can deny the delete stack
 action on a specific stack ID. For more information, see [Controlling Access with AWS Identity and Access
 Management](control-access-with-iam.md "control-access-with-iam.md"). | 2010-05-15 |
| Federation support | October 14, 2013 | CloudFormation supports temporary security credentials from IAM roles,
 which enable scenarios such as federation and single sign-on to the
 AWS Management Console. You can also make calls to CloudFormation from EC2 instances without
 embedding long-term security credentials by using IAM roles. For more
 information about CloudFormation and IAM, see [Controlling Access with
 AWS Identity and Access Management](control-access-with-iam.md "control-access-with-iam.md"). | 2010-05-15 |
| Amazon RDS read replica support | September 24, 2013 | You can now create Amazon RDS read replicas from a source DB instance. For
 more information, see the `SourceDBInstanceIdentifier` property
 in the [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") resource. | 2010-05-15 |
| Associate public IP address with instances in an Auto Scaling group | September 19, 2013 | You can now associate public IP addresses with instances in an Auto Scaling
 group. For more information, see [AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html"). | 2010-05-15 |
| Additional VPC support | September 17, 2013 | CloudFormation adds several enhancements to support VPC and VPN
 functionality

* You can associate a public IP address and multiple private IP
 addresses to Amazon EC2 network interfaces. For more information, see
 [AWS::EC2::NetworkInterface](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-interface.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-interface.html"). You can also
 associate a primary private IP address to an elastic IP address
 (EIP).
* You can enable DNS support and specify DNS host names. For more
 information, see [AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html").
* You can specify a static route between a virtual private gateway to
 your VPN gateway. For more information, see [AWS::EC2::VPNConnectionRoute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-connection-route.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-connection-route.html").
 | 2010-05-15 |
| Redis and VPC security groups support for Amazon ElastiCache | September 3, 2013 | You can now specify Redis as the cache engine for an Amazon ElastiCache (ElastiCache)
 cluster. You can also now assign VPC security groups to ElastiCache clusters. For
 more information, see [AWS::ElastiCache::CacheCluster](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-cachecluster.html"). | 2010-05-15 |
| Parallel stack creation, update and deletion, and nested stack updates
  | August 12, 2013 | AWS CloudFormation now creates, updates, and deletes resources in parallel,
 improving the operations' performance. If you update a top-level template,
 AWS CloudFormation automatically updates nested stacks that have changed. For more
 information, see [CloudFormation Stacks Updates](stacks.md "stacks.md"). | 2010-05-15 |
| VPC security groups can now be set in RDS DB instances | February 28, 2013 | You can now assign VPC security groups to an RDS DB instance with
 CloudFormation. For more information, see the [VPCSecurityGroups](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-vpcsecuritygroups "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-vpcsecuritygroups") property in [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html"). | 2010-05-15 |
| Rolling deployments for Amazon EC2 Auto Scaling groups | February 20, 2013 | CloudFormation now supports update policies on Amazon EC2 Auto Scaling groups, which
 describe how instances in the Amazon EC2 Auto Scaling group are replaced or modified when
 the Amazon EC2 Auto Scaling group adds or removes instances. You can modify these settings
 at stack creation or during a stack update.
For more information and an example, see [UpdatePolicy
 Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-updatepolicy.html"). | 2010-05-15 |
| Cancel and rollback action for stack updates | February 20, 2013 | CloudFormation supports the ability to cancel a stack update. The stack must
 be in the UPDATE\_IN\_PROGRESS state when the update request is made. More
 information is available in the following topics:

* [Canceling a
 Stack Update](using-cfn--stack-update-cancel.md "using-cfn--stack-update-cancel.md")
* [cancel-update-stack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/cancel-update-stack.html "https://docs.aws.amazon.com/cli/latest/reference/cloudformation/cancel-update-stack.html")
* [CancelUpdateStack](../APIReference/API_CancelUpdateStack.md "../APIReference/API_CancelUpdateStack.md") in the
 *CloudFormation API Reference*
 | 2010-05-15 |
| EBS-optimized instances for Amazon EC2 Auto Scaling groups | February 20, 2013 | You can now provision EBS-optimized instances in Amazon EC2 Auto Scaling groups for
 dedicated throughput to Amazon Elastic Block Store (Amazon EBS) in autoscaled instances. The
 implementation is similar to that of the previously released support for
 optimized Amazon EBS EC2 instances.
For more information, see the new `EbsOptimized` property in
 [AWS::AutoScaling::LaunchConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-launchconfiguration.html"). | 2010-05-15 |
| New documentation | December 21, 2012 | [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html") now provides a
 `BlockDeviceMappings` property to allow you to set block
 device mappings for your EC2 instance.
With this change, two new types have been added:

* [BlockDeviceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-blockdevicemapping.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-blockdevicemapping.html")
* [Block
 Device](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-ebs.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-ebs.html")
 | 2010-05-15 |
| New documentation | December 21, 2012 | New sections have been added to describe the procedures for creating and
 viewing stacks using the recently redesigned AWS Management Console. You can find them
 here:

* [Creating a Stack from
 the CloudFormation console](cfn-console-create-stack.md "cfn-console-create-stack.md")
* [View
 stack information from the CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md")
 | 2010-05-15 |
| New documentation | November 15, 2012 | Information about custom resources is provided in the following
 topics:

* [Custom
 Resources](template-custom-resources.md "template-custom-resources.md")
* [AWS::CloudFormation::CustomResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html")
* [Custom
 Resource Reference](crpg-ref.md "crpg-ref.md")
 | 2010-05-15 |
| Updated documentation | November 15, 2012 | CloudFormation now supports specifying provisioned I/O operations per second
 (IOPS) for RDS DB instances. You can set this value from 1000–10,000
 in 1000 IOPS increments by using the new [Iops](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-iops "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html#cfn-rds-dbinstance-iops") property in [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html") .
For more information about specifying IOPS for RDS DB instances, see
 [Provisioned
 IOPS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html") in the *Amazon Relational Database Service User
 Guide*. | 2010-05-15 |
| New and updated documentation | August 27, 2012 | Topics have been reorganized to more clearly provide specific information
 about using the AWS Management Console and using the CloudFormation command line interface
 (CLI).
Information about tagging CloudFormation stacks has been added, including new
 guides and updated reference topics:

* New topic: [Configure stack options](cfn-console-create-stack.md#configure-stack-options "cfn-console-create-stack.md#configure-stack-options").
* New information about tags in the *CloudFormation API
 reference*: [CreateStack](../APIReference/API_CreateStack.md "../APIReference/API_CreateStack.md"), [Stack](../APIReference/API_Stack.md "../APIReference/API_Stack.md"), and [Tag](../APIReference/API_Tag.md "../APIReference/API_Tag.md").

New information about [working with Windows
 stacks](cfn-windows-stacks.md "cfn-windows-stacks.md"):

* [Microsoft Windows Amazon Machine Images (AMIs) and AWS CloudFormation
 templates](cfn-windows-stacks-amis-and-templates.md "cfn-windows-stacks-amis-and-templates.md")
* [Bootstrapping
 AWS CloudFormation Windows stacks](cfn-windows-stacks-bootstrapping.md "cfn-windows-stacks-bootstrapping.md")

New topic: [Using regular expressions in CloudFormation templates](cfn-regexes.md "cfn-regexes.md"). | 2010-05-15 |
| New feature | April 25, 2012 | CloudFormation now provides full support for Virtual Private Cloud (VPC)
 security with Amazon EC2. You can now create and populate an entire VPC with
 every type of VPC resource (subnets, gateways, network ACLs, route tables,
 and so forth) using a single CloudFormation template.
Documentation for the following resource types has been updated:

* [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html")
* [AWS::EC2::SecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html")
* [AWS::EC2::SecurityGroupEgress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html")
* [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html")
* [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html")
* [AWS::EC2::EIP](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html")
* [AWS::EC2::EIPAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html")
* [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html")

New resource types have been added to the documentation:

* [AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpc.html")
* [AWS::EC2::InternetGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-internetgateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-internetgateway.html")
* [AWS::EC2::DHCPOptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-dhcp-options.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-dhcp-options.html")
* [AWS::EC2::DHCPOptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route-table.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route-table.html")
* [AWS::EC2::RouteTable](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-route.html")
* [AWS::EC2::NetworkAcl](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-acl.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-acl.html")
* [AWS::EC2::NetworkAclEntry](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-acl-entry.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-network-acl-entry.html")
* [AWS::EC2::Subnet](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html")
* [AWS::EC2::VPNGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-gateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpn-gateway.html")
* [AWS::EC2::CustomerGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-customer-gateway.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-customer-gateway.html")
 | 2010-05-15 |
| New feature | April 13, 2012 | CloudFormation now allows you to add or remove elements from a stack when
 updating it. [CloudFormation Stacks Updates](stacks.md "stacks.md") has been updated, and a new section
 has been added to the walkthrough: [Change the Stack's
 Resources](updating.stacks.md "updating.stacks.md"), which describes how to add and remove resources when
 updating the stack. | 2010-05-15 |
| New feature | February 2, 2012 | CloudFormation now provides support for resources in an existing Amazon Virtual Private Cloud
 (Amazon VPC). With this release, you can:

* Launch an EC2 Dedicated instance into an existing Amazon VPC. For more
 information, see [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html").
* Set the `SourceDestCheck` attribute of an EC2 instance
 that resides in an existing Amazon VPC. For more information, see [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-instance.html").
* Create Elastic IP addresses in an existing Amazon VPC. For more
 information, see [AWS::EC2::EIP](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eip.html").
* Use CloudFormation to create Amazon VPC security groups and ingress/egress
 rules in an existing VPC. For more information, see [AWS::EC2::SecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroup.html").
* Associate an Auto Scaling group with an existing Amazon VPC by setting the
 `VPCZoneIdentifier` property of your
 `AWS::AutoScaling::AutoScalingGroup` resource. For more
 information, see [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-autoscaling-autoscalinggroup.html").
* Attach an Elastic Load Balancing load balancer to a Amazon VPC subnet and create security
 groups for the load balancer. For more information, see [AWS::ElasticLoadBalancing::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancing-loadbalancer.html").
* Create an RDS DB instance in an existing Amazon VPC. For more
 information, see [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html").
 | 2010-05-15 |
| New feature | February 2, 2012 | You can now update properties for the following resources in an existing
 stack:

* [AWS::EC2::SecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupingress.html")
* [AWS::EC2::SecurityGroupEgress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupegress.html")
* [AWS::EC2::EIPAssociation](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-eipassociation.html")
* [AWS::RDS::DBSubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsubnet-group.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsubnet-group.html")
* [AWS::RDS::DBSecurityGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsecuritygroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbsecuritygroup.html")
* [AWS::RDS::DBSecurityGroupIngress](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-security-group-ingress.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-security-group-ingress.html")
* [AWS::Route53::RecordSetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetgroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53-recordsetgroup.html")

For a complete list of updatable resources and details about what to
 consider when updating a stack, see [CloudFormation Stacks Updates](stacks.md "stacks.md"). | 2010-05-15 |
| Restructured guide | February 2, 2012 | Reorganized existing sections into new sections: [Working with
 CloudFormation Templates](template-guide.md "template-guide.md") and **Managing
 Stacks**. Moved [Template Reference](template-reference.md "template-reference.md") to the
 top level of the Table of Contents. Moved [Estimating the Cost of Your CloudFormation
 Stack](Welcome.md "Welcome.md") to the Getting Started section. | 2010-05-15 |
| New content | February 2, 2012 | Added new sections:

* [Walkthrough: Updating a
 Stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/updating.stacks.walkthrough "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/updating.stacks.walkthrough") is a tutorial that walks through the process of
 updating a LAMP stack.
* [Deploying Applications
 on Amazon EC2 with AWS CloudFormation](deploying.md "deploying.md") describes how to
 use CloudFormation helper scripts to deploy applications using metadata
 stored in your template.
* [CloudFormation
 Helper Scripts Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-helper-scripts-reference.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-helper-scripts-reference.html") provides reference material for
 the CloudFormation helper scripts (cfn-init, cfn-get-metadata, cfn-signal,
 and cfn-hup).
 | 2010-05-15 |
| New feature | May 26, 2011 | CloudFormation now provides the `list-stacks` command, which
 enables you to list stacks filtered by stack status. Deleted stacks can be
 listed for up to 90 days after they have been deleted. For more information,
 see [Describing and Listing Your Stacks](service_code_examples.md "service_code_examples.md"). | 2010-05-15 |
| New features | May 26, 2011 | The `describe-stack-resources` and `get-template`
 commands now enable you to get information from stacks that have been
 deleted for 90 days after they have been deleted. For more information, see
 [Listing Resources](service_code_examples.md "service_code_examples.md") and [Retrieving a
 Template](service_code_examples.md "service_code_examples.md"). | 2010-05-15 |
| New link | March 1, 2011 | CloudFormation endpoint information is now located in the AWS General Reference. For
 more information, go to Regions and Endpoints in [AWS General
 Reference](https://docs.aws.amazon.com/general/latest/gr/Welcome.html "https://docs.aws.amazon.com/general/latest/gr/Welcome.html"). | 2010-05-15 |
| Initial release | February 25, 2011 | The initial public release of CloudFormation. | 2010-05-15 |

# CloudFormation best practices

Best practices are recommendations that can help you use CloudFormation more effectively and
adopt safe practices throughout its entire workflow. Learn how to plan and organize your stacks, create
templates that describe your resources and the software applications that run on them, and
manage your stacks and their resources. The following best practices are based on real-world
experience from current CloudFormation customers.

**Planning and organizing**

- [Shorten the feedback loop to improve development
  velocity](#shortenfeedbackloop "#shortenfeedbackloop")
- [Organize your stacks by lifecycle and ownership](#organizingstacks "#organizingstacks")
- [Use cross-stack references to return the value of an output exported by another stack](#cross-stack "#cross-stack")
- [Use AWS CloudFormation StackSets for multi-account and multi-region deployments](#stack-sets "#stack-sets")
- [Reuse templates to replicate stacks in multiple environments](#reuse "#reuse")
- [Verify quotas for all resource types](#limits "#limits")
- [Use modules to reuse resource configurations](#modules-reuse "#modules-reuse")
- [Adopt infrastructure as code practices](#infrastructure-as-code "#infrastructure-as-code")

**Creating templates**

- [Don't embed credentials in your templates](#credentials "#credentials")
- [Use AWS-specific parameter types](#parmtypes "#parmtypes")
- [Use parameter constraints](#parmconstraints "#parmconstraints")
- [Use pseudo parameters to promote portability](#pseudoparameters "#pseudoparameters")
- [Use AWS::CloudFormation::Init to deploy software
  applications on Amazon EC2 instances](#cfninit "#cfninit")
- [Use the latest helper scripts](#helper-scripts "#helper-scripts")
- [Validate templates before using them](#validate "#validate")
- [Using YAML or JSON for template authoring](#use-yaml-json "#use-yaml-json")
- [Implement a comprehensive tagging strategy](#resource-tags "#resource-tags")
- [Leverage template macros for advanced transformations](#template-macros-advanced-transformations "#template-macros-advanced-transformations")

**Managing stacks**

- [Manage all stack resources through CloudFormation](#donttouch "#donttouch")
- [Create change sets before updating your
  stacks](#cfn-best-practices-changesets "#cfn-best-practices-changesets")
- [Use stack policies to protect resources](#stackpolicy "#stackpolicy")
- [Use AWS CloudTrail to log CloudFormation calls](#cloudtrail-logging "#cloudtrail-logging")
- [Use code reviews and revision controls to manage your templates](#code "#code")
- [Update your Amazon EC2 instances regularly](#update-ec2-linux "#update-ec2-linux")
- [Use drift detection regularly](#drift-detection "#drift-detection")
- [Configure rollback triggers for automatic recovery](#rollback-triggers "#rollback-triggers")
- [Implement effective stack refactoring strategies](#stack-refactoring-bp "#stack-refactoring-bp")
- [Use CloudFormation Hooks for lifecycle management](#cloudformation-hooks "#cloudformation-hooks")

**Authoring tools**

- [Use IaC Generator to create templates from existing resources](#iac-generator "#iac-generator")
- [Use AWS Infrastructure Composer for visual template design](#infrastructure-composer "#infrastructure-composer")
- [Consider using AWS Cloud Development Kit (AWS CDK) for complex infrastructure](#cdk-integration "#cdk-integration")

**Security and compliance**

- [Use IAM to control access](#use-iam-permissions-to-control-access "#use-iam-permissions-to-control-access")
- [Apply the principle of least privilege](#least-privilege "#least-privilege")
- [Secure sensitive parameters](#secure-parameters "#secure-parameters")
- [Implement policy as code with AWS CloudFormation Guard](#cfn-guard "#cfn-guard")

## Shorten the feedback loop to improve development

velocity

Adopt practices and tools that help you shorten the feedback loop for your infrastructure
you describe with CloudFormation templates. This includes performing early linting and testing of
your templates in your workstation; when you do, you have the opportunity to discover
potential syntax and configuration issues even before you submit your contributions to a
source code repository. Early discovery of such issues helps with preventing them from
reaching formal lifecycle environments, such as development, quality assurance, and
production. This early-testing, fail-fast approach gives you the benefits of reducing rework
wait time, reducing potential areas of impact, and increasing your level of confidence in
having successful provisioning operations.

Tooling choices that help you achieve fail-fast practices include the [AWS CloudFormation Linter](https://github.com/aws-cloudformation/cfn-lint "https://github.com/aws-cloudformation/cfn-lint")
(`cfn-lint`) and [TaskCat](https://github.com/aws-ia/taskcat "https://github.com/aws-ia/taskcat")
command line tools. The `cfn-lint` tool gives you the ability to validate your
CloudFormation templates against the [AWS CloudFormation Resource Specification](../TemplateReference/cfn-resource-specification.md "../TemplateReference/cfn-resource-specification.md"). This
includes checking valid values for resource properties, as well as best practices. Plugins for
`cfn-lint` are [available for a number
of code editors](https://github.com/aws-cloudformation/cfn-lint#editor-plugins "https://github.com/aws-cloudformation/cfn-lint#editor-plugins"); this gives you the ability to visualize issues within your editor
and to get direct linter feedback. You can also choose to integrate `cfn-lint` in
your source code repository’s configuration, so that you can perform template validation when
you commit your contributions. For more information, see [Git pre-commit validation of AWS CloudFormation templates with `cfn-lint`](https://aws.amazon.com/blogs/mt/git-pre-commit-validation-of-aws-cloudformation-templates-with-cfn-lint/ "https://aws.amazon.com/blogs/mt/git-pre-commit-validation-of-aws-cloudformation-templates-with-cfn-lint/"). Once you
have performed your initial linting—and fixed any issues `cfn-lint` might have
raised—you can use TaskCat to test your templates by programmatically creating stacks in the
AWS Regions you choose. TaskCat also generates a report with a pass/fail grades for each
Region you chose.

For a step-by-step, hands-on walkthrough on how to use both tools to shorten the feedback
loop, follow the [Linting and Testing lab](https://catalog.workshops.aws/cfn101/en-US/basics/templates/linting-and-testing "https://catalog.workshops.aws/cfn101/en-US/basics/templates/linting-and-testing") of the [AWS CloudFormation Workshop](https://catalog.workshops.aws/cfn101/en-US "https://catalog.workshops.aws/cfn101/en-US").

## Organize your stacks by lifecycle and ownership

Use the lifecycle and ownership of your AWS resources to help you decide what resources
should go in each stack. Initially, you might put all your resources in one stack, but as your
stack grows in scale and broadens in scope, managing a single stack can be cumbersome and time
consuming. By grouping resources with common lifecycles and ownership, owners can make changes
to their set of resources by using their own process and schedule without affecting other
resources.

For example, imagine a team of developers and engineers who own a website that's hosted on
Amazon EC2 Auto Scaling instances behind a load balancer. Because the website has its own lifecycle and is
maintained by the website team, you can create a stack for the website and its resources. Now
imagine that the website also uses back-end databases, where the databases are in a separate
stack that are owned and maintained by database administrators. Whenever the website team or
database team needs to update their resources, they can do so without affecting each other's
stack. If all resources were in a single stack, coordinating, and communicating updates can be
difficult.

For additional guidance about organizing your stacks, you can use two common frameworks: a
multi-layered architecture and service-oriented architecture (SOA).

A layered architecture organizes stacks into multiple horizontal layers that build on top
of one another, where each layer has a dependency on the layer directly below it. You can have
one or more stacks in each layer, but within each layer, your stacks should have AWS
resources with similar lifecycles and ownership.

With a service-oriented architecture, you can organize big business problems into
manageable parts. Each of these parts is a service that has a clearly defined purpose and
represents a self-contained unit of functionality. You can map these services to a stack,
where each stack has its own lifecycle and owners. These services (stacks) can be wired
together so that they can interact with one another.

## Use cross-stack references to return the value of an output exported by another stack

When you organize your AWS resources based on lifecycle and ownership, you might want to
build a stack that uses resources that are in another stack. You can hardcode values or use
input parameters to pass resource names and IDs. However, these methods can make templates
difficult to reuse or can increase the overhead to get a stack running. Instead, use
cross-stack references to return the value of an output exported by another stack so that other stacks can use them.
Stacks can use the exported resources by calling them using the `Fn::ImportValue`
function.

For example, you might have a network stack that includes a VPC, a security group, and a
subnet. You want all public web applications to use these resources. By exporting the
resources, you allow all stacks with public web applications to use them. For more
information, see [Get exported outputs from a deployed CloudFormation
stack](using-cfn-stack-exports.md "using-cfn-stack-exports.md").

## Use AWS CloudFormation StackSets for multi-account and multi-region deployments

AWS CloudFormation StackSets extend the capability of stacks by enabling you to create, update,
or delete stacks across multiple accounts and regions with a single operation. Use StackSets
for deploying common infrastructure components, compliance controls, or shared services across
your organization.

When using StackSets, implement service-managed permissions with AWS Organizations for
simplified permission management. This approach allows you to deploy StackSets to accounts
within your organization without the need to manually configure IAM roles in each account.

For more information on StackSets see [StackSets concepts](stacksets-concepts.md "stacksets-concepts.md").

## Verify quotas for all resource types

Before launching a stack, ensure that you can create all the resources that you want
without hitting your AWS account limits. If you hit a limit, CloudFormation won't create your
stack successfully until you increase your quota or delete extra resources. Each service can
have various limits that you should be aware of before launching a stack. For example, by
default, you can only launch 2000 CloudFormation stacks per Region in your AWS account. For more
information about limits and how to increase the default limits, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_AWS General Reference_.

## Reuse templates to replicate stacks in multiple environments

After you have your stacks and resources set up, you can reuse your templates to replicate
your infrastructure in multiple environments. For example, you can create environments for
development, testing, and production so that you can test changes before implementing them
into production. To make templates reusable, use the parameters, mappings, and conditions
sections so that you can customize your stacks when you create them. For example, for your
development environments, you can specify a lower-cost instance type compared to your
production environment, but all other configurations and settings remain the same. For more
information about parameters, mappings, and conditions, see [CloudFormation template sections](template-anatomy.md "template-anatomy.md").

## Use modules to reuse resource configurations

As your infrastructure grows, common patterns can emerge in which you declare the same
components in each of your templates. _Modules_ are a way for you to
package resource configurations for inclusion across stack templates, in a transparent,
manageable, and repeatable way. Modules can encapsulate common service configurations and best
practices as modular, customizable building blocks for you to include in your stack
templates.

These building blocks can be for a single resource, like best practices for defining an
Amazon Elastic Compute Cloud (Amazon EC2) instance, or they can be for multiple resources, to define common patterns
of application architecture. These building blocks can be nested into other modules, so you
can stack your best practices into higher-level building blocks. CloudFormation modules are
available in the [CloudFormation registry](registry.md "registry.md"), so you can use them just
like a native resource. When you use a CloudFormation module, the module template is expanded into
the consuming template, which makes it possible for you to access the resources inside the
module using a [Ref](../TemplateReference/intrinsic-function-reference-ref.md "../TemplateReference/intrinsic-function-reference-ref.md") or [Fn::GetAtt](../TemplateReference/intrinsic-function-reference-getatt.md "../TemplateReference/intrinsic-function-reference-getatt.md"). For more information, see [Create reusable resource configurations that can be included across
templates with CloudFormation modules](modules.md "modules.md").

## Adopt infrastructure as code practices

Treat your CloudFormation templates as code by implementing infrastructure as code (IaC) practices.
Store your templates in version control systems, implement code reviews, and use automated testing
to validate changes. This approach ensures consistency, improves collaboration, and provides an
audit trail for infrastructure changes.

Consider implementing CI/CD pipelines for your infrastructure code to automate the testing
and deployment of your CloudFormation templates. Tools like AWS CodePipeline, AWS CodeBuild,
and AWS CodeDeploy can be used to create automated workflows for your infrastructure deployments.

For more information on implementing IaC best practices, see [Using AWS CloudFormation as an IaC tool](../../../prescriptive-guidance/latest/choose-iac-tool/cloudformation.md "../../../prescriptive-guidance/latest/choose-iac-tool/cloudformation.md").

For more information on using continuous delivery with CloudFormation, see [Continuous delivery with CodePipeline](continuous-delivery-codepipeline.md "continuous-delivery-codepipeline.md").

## Don't embed credentials in your templates

Rather than embedding sensitive information in your CloudFormation templates, we recommend you use
_dynamic references_ in your stack template.

Dynamic references provide a compact, powerful way for you to reference external values
that are stored and managed in other services, such as the AWS Systems Manager Parameter Store or
AWS Secrets Manager. When you use a dynamic reference, CloudFormation retrieves the value of the
specified reference when necessary during stack and change set operations, and passes the
value to the appropriate resource. However, CloudFormation never stores the actual reference
value. For more information, see [Using dynamic references to
specify template values](dynamic-references.md "dynamic-references.md").

[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") helps you to securely encrypt, store, and retrieve credentials for your databases and other services. The [AWS Systems Manager Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") provides secure, hierarchical storage for configuration data management.

For more information on defining template parameters, see
[CloudFormation template Parameters
syntax](parameters-section-structure.md "parameters-section-structure.md").

## Use AWS-specific parameter types

If your template requires inputs for existing AWS-specific values, such as existing
Amazon Virtual Private Cloud IDs or an Amazon EC2 key pair name, use AWS-specific parameter types. For example, you
can specify a parameter as type `AWS::EC2::KeyPair::KeyName`, which takes an
existing key pair name that's in your AWS account and in the Region where you are creating
the stack. CloudFormation can quickly validate values for AWS-specific parameter types before
creating your stack. Also, if you use the CloudFormation console, CloudFormation shows a drop down
list of valid values, so you don't have to look up or memorize the correct VPC IDs or key pair
names. For more information, see [Specify existing resources at
runtime with CloudFormation-supplied parameter types](cloudformation-supplied-parameter-types.md "cloudformation-supplied-parameter-types.md").

## Use parameter constraints

With constraints, you can describe allowed input values so that CloudFormation catches any not
valid values before creating a stack. You can set constraints such as a minimum length,
maximum length, and allowed patterns. For example, you can set constraints on a database user
name value so that it must be a minimum length of eight character and contain only
alphanumeric characters. For more information, see [CloudFormation template Parameters
syntax](parameters-section-structure.md "parameters-section-structure.md").

## Use pseudo parameters to promote portability

You can use [pseudo parameters](pseudo-parameter-reference.md "pseudo-parameter-reference.md") in your
templates as arguments for [intrinsic functions](../TemplateReference/intrinsic-function-reference.md "../TemplateReference/intrinsic-function-reference.md"), such as
`Ref` and `Fn::Sub`. Pseudo parameters are parameters that are
predefined by CloudFormation. You don't declare them in your template. Using pseudo parameters in
intrinsic functions increases the portability of your stack templates across Regions and
accounts.

For example, imagine you wanted to create a template where, for a given resource property,
you need to specify the [Amazon Resource Name](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") (ARN) of another
existing resource. In this case, the existing resource is an [AWS Systems Manager
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") resource with the following ARN:
`arn:aws:ssm:us-east-1:123456789012:parameter/MySampleParameter`. You will need
to adapt the [ARN format](../../../IAM/latest/UserGuide/reference-arns.md#arns-syntax "../../../IAM/latest/UserGuide/reference-arns.md#arns-syntax") to your target
AWS partition, Region, and account ID. Instead of hard-coding these values, you can use
`AWS::Partition`, `AWS::Region`, and `AWS::AccountId`
pseudo parameters to make your template more portable. In this case, the following example
shows you how to concatenate elements in an ARN with CloudFormation: `!Sub
 'arn:${AWS::Partition}:ssm:${AWS::Region}:${AWS::AccountId}:parameter/MySampleParameter`.

For another example, assume you want to share resources or configurations across multiple
stacks. In this example, assume you have created a [subnet](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md") for your VPC, and then
exported its ID for use with other stacks in the same AWS account and Region. In another
stack, you reference the exported value of the subnet ID when describing an Amazon EC2 instance.
For a detailed example of using the `Export` output field and
`Fn::ImportValue` intrinsic function, see [Refer to resource outputs in another CloudFormation
stack](walkthrough-crossstackref.md "walkthrough-crossstackref.md").

Stack exports must be unique per account and Region. So, in this case, you can use the
`AWS::StackName` pseudo parameter to create a prefix for your export. Since stack
names must also be unique per account and Region, the usage of this pseudo parameter as a
prefix increases the possibility of having a unique export name while also promoting a
reusable approach across stacks from where you export values. Alternatively, you can use a
prefix of your own choice.

## Use `AWS::CloudFormation::Init` to deploy software

applications on Amazon EC2 instances

When you launch stacks, you can install and configure software applications on Amazon EC2
instances by using the `cfn-init` helper script and the
`AWS::CloudFormation::Init` resource. By using
`AWS::CloudFormation::Init`, you can describe the configurations that you want
rather than scripting procedural steps. You can also update configurations without recreating
instances. And if anything goes wrong with your configuration, CloudFormation generates logs that
you can use to investigate issues.

In your template, specify installation and configuration states in the
`AWS::CloudFormation::Init` resource. For a walkthrough that shows how to use
`cfn-init` and `AWS::CloudFormation::Init`, see [Deploy applications on Amazon EC2](deploying.md "deploying.md").

## Use the latest helper scripts

The CloudFormation helper scripts are updated periodically. Be sure you include the following
command in the `UserData` property of your template before you call the helper
scripts to ensure that your launched instances get the latest helper scripts:

```
`yum install -y aws-cfn-bootstrap`
```

For more information about getting the latest helper scripts, see the [CloudFormation helper
scripts reference](../TemplateReference/cfn-helper-scripts-reference.md "../TemplateReference/cfn-helper-scripts-reference.md") in the _AWS CloudFormation Template Reference Guide_.

## Validate templates before using them

Before you use a template to create or update a stack, you can use CloudFormation to validate
it. Validating a template can help you catch syntax and some semantic errors, such as circular
dependencies, before CloudFormation creates any resources. If you use the CloudFormation console, the
console automatically validates the template after you specify input parameters. For the AWS CLI
or CloudFormation API, use the [validate-template](../../../cli/latest/reference/cloudformation/validate-template.md "../../../cli/latest/reference/cloudformation/validate-template.md") CLI command or [ValidateTemplate](../APIReference/API_ValidateTemplate.md "../APIReference/API_ValidateTemplate.md") API
operation.

During validation, CloudFormation first checks if the template is valid JSON. If it isn't,
CloudFormation checks if the template is valid YAML. If both checks fail, CloudFormation returns a
template validation error.

### Validate templates for organization policy

compliance

You can also validate your template for compliance to organization policy guidelines.
AWS CloudFormation Guard (`cfn-guard`) is an open-source command line interface (CLI) tool
that provides a policy-as-code language to define rules that can check for both required and
prohibited resource configurations. It then enables you to validate your templates against
those rules. For example, administrators can create rules to ensure that users always create
encrypted Amazon S3 buckets.

You can use `cfn-guard` either locally, while editing templates, or
automatically as part of a CI/CD pipeline to stop deployment of non-compliant
resources.

Additionally, `cfn-guard` includes a feature, `rulegen`, that
enables you to extract rules from existing compliant CloudFormation templates.

For more information, see the [cfn-guard](https://github.com/aws-cloudformation/cloudformation-guard "https://github.com/aws-cloudformation/cloudformation-guard")
repository on GitHub.

## Using YAML or JSON for template authoring

CloudFormation supports both YAML and JSON formats for templates. Each has its advantages, and the choice depends on your specific needs:

Use YAML when

- You prioritize human readability and maintainability
- You want to include comments to document your template
- You're working on complex templates with nested structures
- You want to use YAML-specific features like anchors and aliases to reduce repetition

Use JSON when:

- You need to integrate with tools or systems that prefer JSON
- You're working with programmatic template generation or manipulation
- You require strict data validation

YAML is generally recommended for manual template authoring due to its readability and comment support. It's particularly useful for complex
templates where the indentation-based structure helps visualize resource hierarchies. JSON can be advantageous in automated workflows or when
working with APIs that expect JSON input. It's also beneficial when you need to ensure strict adherence to a specific structure. Regardless of
the format you choose, focus on creating well-structured, documented, and maintainable templates. If using YAML, leverage its features like
anchors and aliases to reduce repetition and improve maintainability.

## Implement a comprehensive tagging strategy

Implement a consistent tagging strategy for all resources created by your CloudFormation templates.
Tags help with resource organization, cost allocation, access control, and automation. Consider
including tags for environment, owner, cost center, application, and purpose.

Use the `AWS::CloudFormation::Stack` resource's `Tags` property to
apply tags to all supported resources in a stack. You can also use the `TagSpecifications`
property available on many resource types to apply tags during resource creation.

For more information on tagging, see [Resource tag](../TemplateReference/aws-properties-resource-tags.md "../TemplateReference/aws-properties-resource-tags.md").

## Leverage template macros for advanced transformations

CloudFormation macros enable you to perform custom processing on templates, from simple actions
like find-and-replace operations to complex transformations that generate additional resources.
Use macros to extend the capabilities of CloudFormation templates and implement reusable patterns
across your organization.

The AWS Serverless Application Model is an example of a macro that simplifies the
development of serverless applications. Consider creating custom macros for organization-specific
patterns and requirements.

For more information on using macros in your templates, see [Overview of CloudFormation macros](template-macros-overview.md "template-macros-overview.md").

## Manage all stack resources through CloudFormation

After you launch a stack, use the CloudFormation [console](https://console.aws.amazon.com/cloudformation/home "https://console.aws.amazon.com/cloudformation/home"), [API](../APIReference.md "../APIReference.md"), or [AWS CLI](../../../cli/latest/reference/cloudformation/index.md "../../../cli/latest/reference/cloudformation/index.md") to update resources in your
stack. Don't make changes to stack resources outside of CloudFormation. Doing so can create a
mismatch between your stack's template and the current state of your stack resources, which
can cause errors if you update or delete the stack. This is known as drift. If a change is
made to a resource outside of the CloudFormation template and you update the stack, the changes
made directly to the resource will be discarded, and the resource configuration will revert to
the configuration in the template.

For more information on drift, see [What is drift?](using-cfn-stack-drift.md#what-is-drift "using-cfn-stack-drift.md#what-is-drift").

For more information on updating stacks, see [Updating a stack](updating.stacks.md "updating.stacks.md").

## Create change sets before updating your

stacks

Change sets allow you to see how proposed changes to a stack might impact your running
resources before you implement them. CloudFormation doesn't make any changes to your stack until
you run the change set, allowing you to decide whether to proceed with your proposed changes
or create another change set.

Use change sets to check how your changes might impact your running resources, especially
for critical resources. For example, if you change the name of an Amazon RDS database instance,
CloudFormation will create a new database and delete the old one; you will lose the data in the
old database unless you've already backed it up. If you generate a change set, you will see
that your change will replace your database. This can help you plan before you update your
stack. For more information, see [Update CloudFormation stacks using change
sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md").

## Use stack policies to protect resources

Stack policies help protect critical stack resources from unintentional updates that could
cause resources to be interrupted or even replaced. A stack policy is a JSON document that
describes what update actions can be performed on designated resources. Specify a stack policy
whenever you create a stack that has critical resources.

During a stack update, you must explicitly specify the protected resources that you want
to update; otherwise, no changes are made to protected resources. For more information, see
[Prevent updates to stack resources](protect-stack-resources.md "protect-stack-resources.md").

## Use AWS CloudTrail to log CloudFormation calls

AWS CloudTrail tracks anyone making CloudFormation API calls in your AWS account. API calls are logged
whenever anyone uses the CloudFormation API, the CloudFormation console, a back-end console, or CloudFormation AWS CLI
commands. Enable logging and specify an Amazon S3 bucket to store the logs. That way, if you ever
need to, you can audit who made what CloudFormation call in your account.

For more information, see
[Logging AWS CloudFormation API calls with AWS CloudTrail](cfn-api-logging-cloudtrail.md "cfn-api-logging-cloudtrail.md").

## Use code reviews and revision controls to manage your templates

Your stack templates describe the configuration of your AWS resources, such as their
property values. To review changes and to keep an exact history of your resources, use code
reviews and revision controls. These methods can help you track changes between different
versions of your templates, which can help you track changes to your stack resources. Also, by
maintaining a history, you can always revert your stack to a certain version of your
template.

## Update your Amazon EC2 instances regularly

On all your Amazon EC2 Windows instances and Amazon EC2 Linux instances created with CloudFormation,
regularly run the `yum update` command to update the RPM package. This ensures that
you get the latest fixes and security updates.

## Use drift detection regularly

Regularly use the CloudFormation drift detection feature to identify resources that have been
modified outside of CloudFormation management. Detecting and resolving drift helps maintain the
integrity of your infrastructure as code approach and ensures that your templates accurately
reflect the state of your deployed resources.

Consider implementing automated drift detection as part of your operational procedures.
You can use AWS Lambda functions triggered by Amazon EventBridge rules to periodically check
for drift and notify your team when discrepancies are detected.

For more information on drift, see [Detect unmanaged configuration changes to stacks and resources with drift detection](using-cfn-stack-drift.md "using-cfn-stack-drift.md").

## Configure rollback triggers for automatic recovery

Use rollback triggers to specify Amazon CloudWatch alarms that CloudFormation should monitor
during stack creation and update operations. If any of the specified alarms go into the
`ALARM` state, CloudFormation automatically rolls back the entire stack operation,
helping to ensure that your infrastructure remains in a stable state.

Configure rollback triggers for critical metrics such as application error rates, system
resource utilization, or custom business metrics that indicate the health of your application
and infrastructure.

For more information on rollback triggers, see [Roll back your stack on alarm breach](using-cfn-rollback-triggers.md "using-cfn-rollback-triggers.md").

## Implement effective stack refactoring strategies

As your infrastructure evolves, you may need to refactor your CloudFormation stacks to improve
maintainability, reduce complexity, or adapt to changing requirements. Stack refactoring involves
restructuring your templates and resources while preserving their external behavior and
functionality. Stack refactoring is beneficial to use with CloudFormation in the following ways:

- _Splitting monolithic stacks_: Breaking down large, complex stacks
  into smaller, more manageable stacks organized by lifecycle or ownership
- _Consolidating related resources_: Combining related resources from
  multiple stacks into a single, cohesive stack to simplify management
- _Extracting reusable components_: Moving common patterns into modules
  or nested stacks to promote reuse and consistency
- _Improving resource organization_: Restructuring resources within a
  stack to better reflect their relationships and dependencies

For more information on refactoring your CloudFormation stacks, see [Stack refactoring](stack-refactoring.md "stack-refactoring.md").

## Use CloudFormation Hooks for lifecycle management

CloudFormation Hooks provide code that proactively inspects the configuration of your AWS resources before provisioning,
and perform complex validation checks. Hooks check if your resources, stacks, and changes sets are compliant with your
organization's security, operational, and cost optimization needs. They providing warnings before a resource provisioning,
or failing the operation and stopping it altogether, depending on how it has been configured. Violations and warnings are
logged in Amazon CloudWatch to provide visibility into non-compliant deployments.

For more information on these best practices for Hooks see, [AWS CloudFormation Hooks concepts](../../../cloudformation-cli/latest/hooks-userguide/hooks-concepts.md "../../../cloudformation-cli/latest/hooks-userguide/hooks-concepts.md").

For more information on what Hooks can do for your CloudFormation resources see, [What are AWS CloudFormation Hooks?](../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md "../../../cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.md")

## Use IaC Generator to create templates from existing resources

The CloudFormation IaC (infrastructure as code) Generator helps you create CloudFormation templates from your existing AWS resources.
This capability is particularly useful when you need to replicate existing infrastructure, document
manually created resources, or bring previously unmanaged resources under CloudFormation management. IaC generator is useful for creating
your CloudFormation templates in the following ways:

- _Accelerated template creation_: Generate templates from existing resources
  instead of writing them from scratch
- _Consistent infrastructure_: Ensure new environments match existing ones
  by using generated templates as a starting point
- _Migration to infrastructure as code_: Gradually bring manually created
  resources under CloudFormation management
- _Documentation_: Create a record of your existing infrastructure in
  template form

For more information on IaC Generator, see [Generate templates from existing resources with IaC generator](generate-IaC.md "generate-IaC.md").

## Use AWS Infrastructure Composer for visual template design

AWS Infrastructure Composer is a visual design tool that helps you create, visualize,
and modify CloudFormation templates using a drag-and-drop interface. It can be particularly beneficial when using CloudFormation in the
following ways:

- _Architecture planning_: Design and validate infrastructure
  architectures before implementation
- _Template modernization_: Visualize existing templates to
  understand their structure and identify opportunities for improvement
- _Training and onboarding_: Help new team members understand
  CloudFormation concepts and AWS service relationships through visual learning
- _Stakeholder communication_: Present infrastructure designs
  to non-technical stakeholders using clear visual representations
- _Compliance reviews_: Use visual diagrams to facilitate
  security and compliance reviews of your infrastructure designs
- _Compliance reviews_: Use visual diagrams to facilitate
  security and compliance reviews of your infrastructure designs

For more information on Infrastructure Composer, see [What is AWS Infrastructure Composer?](../../../infrastructure-composer/latest/dg/what-is-composer.md "../../../infrastructure-composer/latest/dg/what-is-composer.md").

## Consider using AWS Cloud Development Kit (AWS CDK) for complex infrastructure

For complex infrastructure requirements, consider using the CDK
to define your cloud resources using familiar programming languages like TypeScript, Python, Java,
and .NET. AWS CDK generates CloudFormation templates from your code, allowing you to leverage the
full capabilities of CloudFormation while using the abstractions and programming constructs of your
preferred language.

The AWS CDK provides high-level constructs that encapsulate best practices and simplify
the definition of common infrastructure patterns. This can significantly reduce the amount of
code needed to define your infrastructure while ensuring adherence to best practices.

For more information on the CDK, see [AWS Cloud Development Kit (AWS CDK)](../../../cdk/api/v2.md "../../../cdk/api/v2.md").

## Use IAM to control access

IAM is an AWS service that you can use to manage users and their permissions in AWS. You
can use IAM with CloudFormation to specify what CloudFormation actions users can perform, such as viewing
stack templates, creating stacks, or deleting stacks. Furthermore, anyone managing CloudFormation
stacks will require permissions to resources within those stacks. For example, if users want
to use CloudFormation to launch, update, or terminate Amazon EC2 instances, they must have permission to
call the relevant Amazon EC2 actions.

In most cases, users require full access to manage all of the resources in a template.
CloudFormation makes calls to create, modify, and delete those resources on their behalf. To separate
permissions between a user and the CloudFormation service, use a service role. CloudFormation uses the service
role's policy to make calls instead of the user's policy. For more information, see
[AWS CloudFormation service role](using-iam-servicerole.md "using-iam-servicerole.md").

## Apply the principle of least privilege

When configuring IAM roles for CloudFormation service roles or for resources created by your
templates, always apply the principle of least privilege. Grant only the permissions necessary
for the intended functionality, and avoid using wildcard permissions whenever possible.

Use IAM Access Analyzer to review the permissions granted to your CloudFormation service roles
and identify unused permissions that can be removed. Regularly review and update IAM policies
to ensure they remain aligned with your security requirements.

## Secure sensitive parameters

For sensitive information such as passwords, API keys, and other secrets, use AWS Systems Manager
Parameter Store or AWS Secrets Manager instead of embedding them directly in your
templates. Use dynamic references in your templates to securely retrieve these values during
stack operations.

When using parameters in your templates, set the `NoEcho` property to `true`
for sensitive parameters to prevent their values from being displayed in the console, API responses,
or CLI output. Be aware that `NoEcho` doesn't prevent the value from being logged if
it's passed to other services or resources that might log the value.

For more information on using AWS Systems Manager Parameter Store with CloudFormation see [Get a plaintext value from AWS Systems Manager
Parameter Store](dynamic-references-ssm.md "dynamic-references-ssm.md").

For more information on using the `NoEcho` property, see [CloudFormation
template Parameters syntax](parameters-section-structure.md#parameters-section-structure-properties "parameters-section-structure.md#parameters-section-structure-properties").

For more information on using AWS Secrets Manager with CloudFormation see [Create AWS Secrets Manager secrets in AWS CloudFormation](../../../secretsmanager/latest/userguide/cloudformation.md "../../../secretsmanager/latest/userguide/cloudformation.md").

## Implement policy as code with AWS CloudFormation Guard

AWS CloudFormation Guard (`cfn-guard`) is an open-source policy-as-code tool that allows
you to define and enforce rules for your CloudFormation templates. Use `cfn-guard` to
ensure that your templates comply with organizational policies, security best practices, and
governance requirements.

Integrate `cfn-guard` into your CI/CD pipelines to automatically validate templates
against your policy rules before deployment. This helps prevent non-compliant resources from
being deployed to your environment and provides early feedback to developers about policy
violations.

For more information on Guard see [What is AWS CloudFormation Guard?](../../../cfn-guard/latest/ug/what-is-guard.md "../../../cfn-guard/latest/ug/what-is-guard.md")

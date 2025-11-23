# AWS CloudFormation language server

The AWS CloudFormation language server provides capabilities to accelerate authoring
infrastructure-as-code (IaC) and deploying AWS resources safely and with confidence. It
follows the [language
server protocol](https://microsoft.github.io/language-server-protocol/ "https://microsoft.github.io/language-server-protocol/") (LSP) to provide documentation on hover, auto-completion,
diagnostics via static validation, go to definition and code actions. In addition to these
traditional language server capabilities, the server adds online features to explore and
deploy AWS resources via CloudFormation. This includes the ability to validate and deploy
templates using change sets; view stack diffs, events, resources, and outputs; list stacks
and browse resources by type; and insert live resource state directly into CloudFormation
templates. Developer tooling and integrated development environments (IDE) can leverage the
language server capabilities to enhance the experience of IaC developers on
CloudFormation.

###### Topics

- [IDEs integrating with the AWS CloudFormation
  language server](#ide-extension-supported-ides "#ide-extension-supported-ides")
- [Getting started](#ide-extension-getting-started "#ide-extension-getting-started")
- [Initializing a CloudFormation project in
  the IDE](#ide-extension-initialize-project "#ide-extension-initialize-project")
- [Open source](#ide-extension-open-source "#ide-extension-open-source")
- [Need help?](#ide-extension-need-help "#ide-extension-need-help")

## IDEs integrating with the AWS CloudFormation

language server

The [AWS Toolkit](../../../toolkit-for-vscode/latest/userguide/welcome.md "../../../toolkit-for-vscode/latest/userguide/welcome.md") extension integrates the CloudFormation language server to
enhance the authoring experience. This integration is currently supported in VS Code
based IDEs, including:

- [Visual Studio](https://code.visualstudio.com/ "https://code.visualstudio.com/") Code
- [Kiro](https://kiro.dev/downloads/ "https://kiro.dev/downloads/")
- [Cursor](https://cursor.com/ "https://cursor.com/")

## Getting started

###### Topics

- [Prerequisites](#ide-extension-prerequisites "#ide-extension-prerequisites")
- [Step 1: Install or upgrade the AWS
  Toolkit](#ide-extension-install-toolkit "#ide-extension-install-toolkit")
- [Step 2: Access CloudFormation in
  the AWS Toolkit panel](#ide-extension-access-toolkit-panel "#ide-extension-access-toolkit-panel")
- [Step 3: Validate, test, and
  refine your template](#ide-extension-validate-test-refine "#ide-extension-validate-test-refine")
- [Step 4: Navigate through the
  template](#ide-extension-navigate-template "#ide-extension-navigate-template")
- [Step 5: Validate and deploy](#ide-extension-validate-deploy "#ide-extension-validate-deploy")

### Prerequisites

Before you begin, make sure that:

- You are using a VS Code-based IDE on a supported operation system
  (macOS, Windows, or
  Linux).
- You have installed or upgraded to the latest version of the [AWS Toolkit](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode "https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode") for your IDE.

Some features in the AWS CloudFormation language server require an active AWS account and
configured credentials. You must be signed in to your AWS account through the
AWS Toolkit using valid credentials.

### Step 1: Install or upgrade the AWS

Toolkit

- Open your IDE's Extensions or Plugin Manager.
- Search for AWS Toolkit.
- Install or update to version 3.85.0 or later of the AWS Toolkit for your
  IDE.
- Restart your IDE after installation.

Note: After installation, the AWS Toolkit automatically enables CloudFormation IDE
support. When you first install or upgrade the AWS Toolkit with the AWS CloudFormation
language server extension, you're prompted to grant permission for AWS to collect
anonymous usage data. This data helps AWS improve the CloudFormation language server
and enhances the authoring experience. No sensitive information is collected and
AWS does not record or store template content, resource configurations, or any
identifiable customer data. You can change your telemetry preferences at any time
from the IDE settings. The usage data collected focuses only on feature interactions
and performance metrics. These insights help AWS identify and prioritize
improvements such as faster validation, enhanced autocomplete, and better error
diagnostics.

### Step 2: Access CloudFormation in

the AWS Toolkit panel

In your IDE, open the AWS Toolkit panel from the activity bar. Under AWS
Toolkit, choose **CLOUDFORMATION**.

Panel sections:

- **Region**: Displays the current AWS Region. You can
  change it by selecting the Region name or by using the **AWS CloudFormation:
  Select Region** command from the command palette.
- **Environment**: Indicates the environment you selected
  during CFN init (for example, dev, test, or prod). This value
  appears only after completing the environment selection step.
- **Stacks**: Displays a paginated list of CloudFormation
  stacks in your account.
  - Click on the refresh icon to update the list of stacks.
  - Use the **+** icon to deploy a new template as a
    stack.
  - Each stack entry includes:
    - **Overview**: Displays stack summary and
      status
    - **Stack ID**
    - **Description**
    - **Created time** and **Updated
      time**
    - **Status** and **Status
      reason**
    - **Events**, **Outputs**,
      and **Resources**

  - **Change set**

- **Resources**: After you select a resource type, the
  panel displays the AWS resources of that type in your account. You can
  view, refresh, copy, or import them into your template.

### Step 3: Validate, test, and

refine your template

As you write your CloudFormation template, the IDE provides intelligent authoring
assistance to help you create accurate and compliant infrastructure faster. The
CloudFormation language server runs in the background and provides the following
authoring features:

- Code completion: Suggests resource types, parameters, and properties based
  on CloudFormation schemas.
- Add existing AWS resources: Allows you to import existing resources from
  your AWS account into your template. The IDE uses the [AWS Cloud Control API (CCAPI)](../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md "../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md") to retrieve the live configuration and
  properties of the resource, helping you clone or reuse existing
  infrastructure within your template.

#### To add resources to

your template

- **Expand the CloudFormation Resources
  panel**: In the AWS Toolkit side panel, expand
  **CloudFormation**, then under
  **Resources**, click the **Add +**
  icon.
- **Search for a resource type**: To find a
  specific AWS resource type, in the search bar type the specific AWS
  resource type you want to add. Example:

      + `AWS::S3::Bucket`
      + `AWS::Lambda::Function`

  You can select resource type using **AWS CloudFormation: Add Resource
  Types** in the command palette.

- **Adding resources to your template**:
  Under the **Resources** panel, a paginated list of
  detected AWS resources in your account is displayed. If you have many
  resources, only first page is shown. Use the navigation controls at the
  bottom of the panel to move through additional pages and view all
  available resources.
- Choose the resource you want to include in your template.
- You can insert a resource into your template in two ways, depending on
  your goal:
  - **Clone an existing resource**:
    Create a new resource in your template using the live
    configuration and properties of an existing AWS
    resource.
  - **Import an existing resource**:
    Insert the actual resource into your stack by adding it to your
    template using its live state.

**Tips**

- You can refresh the **Resources** panel at any time
  to view the latest list of resources available in your account or
  Region.
- If you are importing resources, do not add a resource that already
  belongs to an existing CloudFormation stack in the same account.
- To confirm if a resource is already managed by CloudFormation, click the
  **i** (information) icon next to the resource
  name.
- Alternatively, you can use the command **AWS CloudFormation: Get Stack
  Management Info** to check whether a resource belongs to a
  stack.

##### Add related

resources

You can add related resources to the selected resource by using the
command **AWS CloudFormation: Add Related Resources by Type**. Once
you select a resource type from the ones already defined in your template,
the IDE displays a list of resources that are typically associated with or
dependent on that type. For example, if you select an
`AWS::EC2::Instance`, the IDE may suggest adding related
resources such as `AWS::EC2::SecurityGroup` or
`AWS::EC2::Subnet`. This feature helps you quickly build
connected infrastructure components without manually searching for
compatible resource types.

#### Static validation

The CloudFormation IDE provides built-in static validation powered by [AWS CloudFormation
Linter (cfn-lint)](https://aws.amazon.com/blogs/devops/aws-cloudformation-linter-v1/ "https://aws.amazon.com/blogs/devops/aws-cloudformation-linter-v1/") and [AWS CloudFormation Guard](../../../cfn-guard/latest/ug/what-is-guard.md "../../../cfn-guard/latest/ug/what-is-guard.md"). These
validations run behind the scenes as you author templates, helping you identify
syntax errors, compliance gaps, and best practice issues before
deployment.

**Static validation overview**

You will see two types of real-time static validations in the IDE:

- CloudFormation Linter (`cfn-lint`): Validates your template
  against CloudFormation resource specifications and schema rules.
- Guard (`cfn-guard`): Validates your template
  against compliance rules and organizational policy packs.

##### CloudFormation Linter

(cfn-lint)

The CloudFormation Linter is integrated into the IDE to automatically check
your template syntax and structure as you type.

- **Schema validation**: Detects syntax
  and schema errors to ensure your templates conform to CloudFormation
  resource schema.
- **Error highlighting**: Displays red
  or yellow squiggly lines under issues, representing deployment
  blockers or warnings.
- **Hover over help**: When you hover
  over an error, the IDE shows the diagnostic message associated with
  that issue. If a quick fix is available, it will also be offered in
  the hover panel.

##### Guard

integration

Guard validates your templates against rule sets that define
compliance and security policies. The IDE runs Guard validations
in real time through the CloudFormation language server, giving you immediate
feedback while you author templates.

- **Default rule packs**: The IDE
  includes a pre-registered set of Guard rules focused on
  foundational best practices for resource security and configuration
  hygiene. To learn more link to [the guard rule registry](https://github.com/aws-cloudformation/aws-guard-rules-registry "https://github.com/aws-cloudformation/aws-guard-rules-registry").
- **Adding rule packs**: To add or
  modify rule sets, open Settings, Guard and select or
  upload additional Guard rule packs.

**Tips**: Understanding squiggly line
indicators

- Blue squiggles: Best practice hints or optimization
  recommendations.
- Yellow squiggles: Warnings for non-blocking issues (for example,
  missing tags or parameters).
- Red squiggles: Deployment blockers such as invalid property names,
  missing required fields, or schema mismatches.

### Step 4: Navigate through the

template

When you click on a template file in the **Explorer**, the
**Outline** panel automatically displays a structured,
hierarchical view of your CloudFormation template. It organizes the template into
sections such as `Parameters`, `Resources`,
`Outputs`, and `Mappings`, and shows each resource type
and logical ID. This makes it easy to quickly locate and navigate to specific
resources or parameters within large templates.

You can use **Go to Definition** for intrinsic functions such as
`GetAtt` and `Ref`, allowing you to jump directly to the
referenced resource or parameter in your template. This helps you trace
dependencies, understand resource relationships, and make edits more
efficiently.

### Step 5: Validate and deploy

When you're ready to deploy your CloudFormation template, open the command palette and
run **AWS CloudFormation: Validate and Deploy**. The command validates your
template, and if no blocking errors are found, it proceeds to the deployment phase.
Before confirming, the IDE shows a [drift-aware change set](drift-aware-change-sets.md "drift-aware-change-sets.md") summary and a diff view so you can review all
proposed changes.

#### How validation

works

The IDE automatically performs a [validation check before deployment](validate-stack-deployments.md "validate-stack-deployments.md") and validates your template
against common failure causes, including:

- Invalid property syntax or schema mismatches: These issues are
  typically caught by `cfn-lint` during authoring, but if a
  user proceeds to deploy without addressing them, CloudFormation's
  deployment-time validation will surface the same errors before the stack
  is created or updated.
- Resource name conflicts with existing resources in your
  account.
- Service-specific constraints, such as S3 bucket name conflicts or
  missing encryption.

If the validation detects errors, the IDE highlights the issues directly in
your template using red or yellow squiggly lines and lists the errors in the
**PROBLEMS** panel. Each issue includes the specific
property or resource that caused the failure, along with a suggested fix. If
there are no blocking errors, you can proceed to the deployment phase.

If warnings are found (non-blocking issues), a dialog appears allowing you to
either proceed with deployment or cancel and make corrections.

The IDE opens a [drift-aware change
set](drift-aware-change-sets.md "drift-aware-change-sets.md") that displays any differences between your current template and
the deployed stack configuration. This allows you to review, confirm, or cancel
the change set before execution.

Note: Drift-aware change sets enhance the CloudFormation deployment process by
allowing you to handle stack drift safely. Stack drift occurs when the actual
state of your resources differs from what's defined in your CloudFormation template,
often due to manual changes made through the AWS Management Console, CLI, or SDK. CloudFormation
[drift-aware change set](drift-aware-change-sets.md "drift-aware-change-sets.md")
compare your processed stack configuration with the live resource state, and the
IDE surfaces these differences so you can bring resources back into compliance
before deployment.

#### View stack events

When the deployment starts, you can navigate to the
**CloudFormation** tab in the panel to monitor progress in real
time. Under **Stack Events**, you'll see a list of operations
performed during the deployment. Each event includes details such as:

- **Timestamp**: The time the event occurred
- **Resource**: The specific AWS resource being
  created, updated, or deleted
- **Status**: The current state of the operation (for
  example, `CREATE_IN_PROGRESS`, `UPDATE_COMPLETE`,
  or `ROLLBACK_IN_PROGRESS`)
- **Reason**: Additional context or error messages, if
  applicable

You can also view the stack's **Resources** and
**Outputs** from this panel. If you want to open the stack
in the AWS Management Console, use the external-link icon next to the stack name. The
**Stack Events** view helps you track deployment progress,
identify potential issues, and confirm when your stack has completed
successfully.

## Initializing a CloudFormation project in

the IDE

Initializing a CloudFormation project in the IDE helps you set up a structured workspace
with the correct folders, environment configuration, and AWS credentials so you can
validate and deploy your templates reliably. You can initialize a new CloudFormation project
directly from the IDE to create this recommended setup.

**To initialize a CloudFormation project:**

- **Open the command palette**
  - From your IDE, open the command palette (`Ctrl+Shift+P` or
    `Cmd+Shift+P` on macOS).
  - Choose **AWS CloudFormation: CFN Init: Initialize
    Project**.

- **Choose a project directory**
  - By default, the IDE uses your current working directory.
  - You can change this path to any folder where you want to store your
    CloudFormation templates.

- **Select your AWS credential profile**
  - You'll be prompted to choose an AWS credential profile. The selected
    profile will be used for environment detection, validations, and
    deployments.

- **Set up your environment**
  - You'll be prompted to create or select an environment.
  - Environments define where and how your templates will be deployed or
    validated (for example, dev, beta, or production). You can use
    **AWS CloudFormation: CFN Init: Add Environment** to select
    or change your environment.
  - You can use **AWS CloudFormation: CFN Init: Remove
    Environment** to remove the environment you've
    selected.

- **(Optional) Import parameter files**
  - If you already have existing parameter files, the IDE allows you to
    import them during initialization.
  - The IDE automatically detects compatible files and links them to your
    project for use in template validation and deployment.

- **Name and finalize the project**
  - Provide a project name, such as beta-environment, and complete the
    setup.
  - The IDE creates the initial project structure and configuration file
    for you.

You can run validations, preview deployments, or switch between environments directly
from the IDE.

## Open source

The AWS CloudFormation language server is open-sourced under the Apache-2.0
License, giving customers full transparency into how template diagnostics, schema
validation, and static analysis are performed. This reduces security and compliance
friction for customers who require source-level visibility before adopting
tooling.

The code base is publicly available on GitHub: [https://github.com/aws-cloudformation/cloudformation-languageserver/](https://github.com/aws-cloudformation/cloudformation-languageserver/ "https://github.com/aws-cloudformation/cloudformation-languageserver/").

## Need help?

Try the [CloudFormation
community](https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w "https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w") on AWS re:Post.

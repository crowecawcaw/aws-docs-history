

# AWS CloudFormation Language Server
<a name="ide-extension"></a>

The AWS CloudFormation Language Server provides capabilities to accelerate authoring infrastructure-as-code (IaC) and deploying AWS resources safely and with confidence. It follows the [language server protocol](https://microsoft.github.io/language-server-protocol/) (LSP) to provide documentation on hover, auto-completion, diagnostics via static validation, go to definition and code actions. In addition to these traditional language server capabilities, the server adds online features to explore and deploy AWS resources via CloudFormation. This includes the ability to validate and deploy templates using change sets; view stack diffs, events, resources, and outputs; list stacks and browse resources by type; and insert live resource state directly into CloudFormation templates.

**Topics**
+ [IDEs integrating with the AWS CloudFormation Language Server](#ide-extension-supported-ides)
+ [Getting started](#ide-extension-getting-started)
+ [Initializing a CloudFormation project in the IDE (VS Code only)](#ide-extension-initialize-project)
+ [Open source](#ide-extension-open-source)
+ [Need help?](#ide-extension-need-help)

## IDEs integrating with the AWS CloudFormation Language Server
<a name="ide-extension-supported-ides"></a>

AWS provides off-the-shelf integration with the CloudFormation Language Server through the AWS Toolkit for the following IDEs:
+ [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-toolkit-vscode)
+ [JetBrains IDEs](https://plugins.jetbrains.com/plugin/11349-aws-toolkit) (version 2025.3 or later), including IntelliJ IDEA, WebStorm, and PyCharm

The following IDEs also support the CloudFormation Language Server:
+ [Kiro](https://kiro.dev/downloads/)
+ [Cursor](https://cursor.com/)
+ Most VS Code forks and distributions

The CloudFormation Language Server adheres to the [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP) and therefore other integrations are configurable. For instructions on integrating the language server with other editors, see the [installation guide](https://github.com/aws-cloudformation/cloudformation-languageserver/blob/main/INSTALLATION.md).

## Getting started
<a name="ide-extension-getting-started"></a>

**Topics**
+ [Prerequisites](#ide-extension-prerequisites)
+ [Step 1: Install or upgrade the AWS Toolkit](#ide-extension-install-toolkit)
+ [Step 2: Access CloudFormation in the AWS Toolkit](#ide-extension-access-toolkit-panel)
+ [Step 3: Validate, test, and refine your template](#ide-extension-validate-test-refine)
+ [Step 4: Navigate through the template](#ide-extension-navigate-template)
+ [Step 5: Validate and deploy](#ide-extension-validate-deploy)

### Prerequisites
<a name="ide-extension-prerequisites"></a>

Before you begin, make sure that:
+ You are using a supported IDE on a supported operating system (macOS, Windows, or Linux).
+ You have installed or upgraded to the latest version of the AWS Toolkit for your IDE.

Some features in the AWS CloudFormation Language Server require an active AWS account and configured credentials. You must be signed in to your AWS account through the AWS Toolkit using valid credentials.

### Step 1: Install or upgrade the AWS Toolkit
<a name="ide-extension-install-toolkit"></a>

Install or update to the latest version of the AWS Toolkit from your IDE's extension or plugin manager, then restart your IDE.

After installation, the AWS Toolkit automatically enables CloudFormation IDE support. When you first install or upgrade the AWS Toolkit with the AWS CloudFormation Language Server, you are prompted to grant permission for AWS to collect anonymous usage data. This data helps AWS improve the CloudFormation Language Server and enhances the authoring experience. No sensitive information is collected and AWS does not record or store template content, resource configurations, or any identifiable customer data. You can change your telemetry preferences at any time from the IDE settings. Restart the IDE for the changes to take effect. The usage data collected focuses only on feature interactions and performance metrics. These insights help AWS identify and prioritize improvements such as faster validation, enhanced autocomplete, and better error diagnostics.

### Step 2: Access CloudFormation in the AWS Toolkit
<a name="ide-extension-access-toolkit-panel"></a>

After installing the AWS Toolkit, open the CloudFormation panel in your IDE. In VS Code, open the AWS Toolkit panel from the activity bar and choose **CLOUDFORMATION**. In JetBrains IDEs, open the **AWS Toolkit** tool window from the side bar and select the **CloudFormation** tab.

The CloudFormation panel contains the following sections:
+ **Region**: Displays the current AWS Region. In VS Code, you can change it by selecting the Region name or by using the **AWS CloudFormation: Select Region** command from the command palette. In JetBrains IDEs, the Region is configured through the AWS Toolkit connection settings.
+ **Stacks**: Displays a paginated list of CloudFormation stacks in your account. Expand a stack to view its **Change Sets** node, which lists the change sets associated with that stack. Use the View Stack Detail action to open the stack detail view, which displays the stack overview, events, outputs, and resources.
+ **Resources**: After you add a resource type, the panel displays the AWS resources of that type in your account. You can view, refresh, copy, or import them into your template.

In JetBrains IDEs, the toolbar above the tree provides quick access to common actions including **Validate and Deploy**, **Rerun Validate and Deploy**, **Add Resource Type**, and **Refresh**. Actions are also available through right-click context menus on tree nodes.

### Step 3: Validate, test, and refine your template
<a name="ide-extension-validate-test-refine"></a>

As you write your CloudFormation template, the IDE provides intelligent authoring assistance to help you create accurate and compliant infrastructure faster. The CloudFormation Language Server runs in the background and provides the following authoring features:
+ Code completion: Suggests resource types, parameters, and properties based on CloudFormation schemas.
+ Add existing AWS resources: Allows you to import existing resources from your AWS account into your template. The IDE uses the [AWS Cloud Control API (CCAPI)](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.html) to retrieve the live configuration and properties of the resource, helping you clone or reuse existing infrastructure within your template.
+ Extract to parameter: When your cursor is on a literal value in a template (for example, a string like `t2.micro`), the IDE offers a refactoring action to extract the value into the `Parameters` section and replace the literal with a `!Ref` to the new parameter. If the same literal value appears in multiple places, you can choose to extract all occurrences at once.

#### To add resources to your template
<a name="ide-extension-add-resources-to-template"></a>
+ **Add a resource type**: In the AWS Toolkit CloudFormation panel, under **Resources**, add a resource type to browse. In VS Code, click the **Add \+** icon or use the **AWS CloudFormation: Add Resource Types** command from the command palette. In JetBrains, click the **Add Resource Type** button in the toolbar or right-click the **Resources** node.
+ **Search for a resource type**: In the search dialog, type the AWS resource type you want to add. Example:
  + `AWS::S3::Bucket`
  + `AWS::Lambda::Function`
+ **Browse resources**: Under the **Resources** section, a paginated list of detected AWS resources in your account is displayed. If you have many resources, only the first page is shown. Use the navigation controls to move through additional pages and view all available resources.
+ Choose the resource you want to include in your template.
+ You can insert a resource into your template in two ways, depending on your goal:
  + **Clone an existing resource**: Create a new resource in your template using the live configuration and properties of an existing AWS resource.
  + **Import an existing resource**: Insert the actual resource into your stack by adding it to your template using its live state.

**Tips**
+ You can refresh the **Resources** section at any time to view the latest list of resources available in your account or Region.
+ If you are importing resources, do not add a resource that already belongs to an existing CloudFormation stack in the same account.
+ To confirm if a resource is already managed by CloudFormation, use the information action next to the resource. In VS Code, click the **i** icon. In JetBrains IDEs, right-click the resource and choose **Get Stack Management Info**.

##### Add related resources
<a name="ide-extension-add-related-resources"></a>

In VS Code, you can add related resources to the selected resource by using the command **AWS CloudFormation: Add Related Resources by Type**. Once you select a resource type from the ones already defined in your template, the IDE displays a list of resources that are typically associated with or dependent on that type. For example, if you select an `AWS::EC2::Instance`, the IDE may suggest adding related resources such as `AWS::EC2::SecurityGroup` or `AWS::EC2::Subnet`. This feature helps you quickly build connected infrastructure components without manually searching for compatible resource types. This feature is currently not supported in JetBrains IDEs.

#### Static validation
<a name="ide-extension-static-validation"></a>

The CloudFormation Language Server provides built-in static validation powered by [AWS CloudFormation Linter (cfn-lint)](https://github.com/aws-cloudformation/cfn-lint) and [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html). These validations run behind the scenes as you author templates, helping you identify syntax errors, compliance gaps, and best practice issues before deployment.

**Static validation overview**

You will see two types of real-time static validations in the IDE:
+ CloudFormation Linter (`cfn-lint`): Validates your template against CloudFormation resource specifications and schema rules.
+ Guard (`cfn-guard`): Validates your template against compliance rules and organizational policy packs.

##### CloudFormation Linter (cfn-lint)
<a name="ide-extension-cfn-linter-details"></a>

The CloudFormation Linter is integrated into the IDE to automatically check your template syntax and structure as you type.
+ **Schema validation**: Detects syntax and schema errors to ensure your templates conform to CloudFormation resource schema.
+ **Error highlighting**: Displays inline markers under issues, representing deployment blockers or warnings.
+ **Hover help**: When you hover over an error, the IDE shows the diagnostic message associated with that issue. If a quick fix is available, it is also offered.

##### Guard integration
<a name="ide-extension-cfn-guard-integration"></a>

Guard validates your templates against rule sets that define compliance and security policies. The IDE runs Guard validations in real time through the CloudFormation Language Server, giving you immediate feedback while you author templates.
+ **Default rule packs**: The IDE includes a pre-registered set of Guard rules focused on foundational best practices for resource security and configuration hygiene. To learn more, see [the guard rule registry](https://github.com/aws-cloudformation/aws-guard-rules-registry).
+ **Adding rule packs**: To add or modify rule sets, open your IDE settings and navigate to the Guard configuration section to select or upload additional Guard rule packs.

**Tips**: Understanding diagnostic indicators
+ Blue indicators: Best practice hints or optimization recommendations.
+ Yellow indicators: Warnings for non-blocking issues (for example, missing tags or parameters).
+ Red indicators: Deployment blockers such as invalid property names, missing required fields, or schema mismatches.

### Step 4: Navigate through the template
<a name="ide-extension-navigate-template"></a>

The IDE provides a structured, hierarchical view of your CloudFormation template, organized into sections such as `Parameters`, `Resources`, `Outputs`, and `Mappings`, showing each resource type and logical ID. This makes it easy to quickly locate and navigate to specific resources or parameters within large templates. In VS Code, the **Outline** panel in the **Explorer** sidebar displays this structure. In JetBrains IDEs, open the **Structure** tool window to view the template structure for the currently open file.

You can use **Go to Definition** for intrinsic functions such as `GetAtt` and `Ref`, allowing you to jump directly to the referenced resource or parameter in your template. This helps you trace dependencies, understand resource relationships, and make edits more efficiently.

### Step 5: Validate and deploy
<a name="ide-extension-validate-deploy"></a>

When you are ready to deploy your CloudFormation template, use the Validate and Deploy feature to create a change set. The IDE validates your template, and if no blocking errors are found, it proceeds to create a [drift-aware change set](drift-aware-change-sets.md). The IDE then shows a diff view so you can review all proposed changes before executing the change set.

In VS Code, open the command palette and run **AWS CloudFormation: Validate and Deploy**. The command palette guides you through selecting a template, stack name, parameters, capabilities, and other deployment options step by step. In JetBrains IDEs, use the **Validate and Deploy** toolbar button, right-click a template file in the editor, or right-click a stack in the tree. JetBrains presents a wizard dialog where you configure all deployment options including template selection, stack name, parameters, capabilities, tags, and advanced options.

#### How validation works
<a name="ide-extension-how-validation-works"></a>

The IDE automatically performs a [validation check before deployment](validate-stack-deployments.md) and validates your template against common failure causes, including:
+ Invalid property syntax or schema mismatches: These issues are typically caught by `cfn-lint` during authoring, but if you proceed to deploy without addressing them, CloudFormation's deployment-time validation surfaces the same errors before the stack is created or updated.
+ Resource name conflicts with existing resources in your account.
+ Service-specific constraints, such as S3 bucket name conflicts or missing encryption.

If the validation detects errors, the IDE highlights the issues directly in your template and lists the errors in the diagnostics panel. Each issue includes the specific property or resource that caused the failure, along with a suggested fix. If there are no blocking errors, you can proceed to the deployment phase.

If warnings are found (non-blocking issues), a dialog appears allowing you to either proceed with deployment or cancel and make corrections.

The IDE opens a [drift-aware change set](drift-aware-change-sets.md) that displays any differences between your current template and the deployed stack configuration. This allows you to review, confirm, or cancel the change set before execution. Cancelling the deployment deletes the change set.

Drift-aware change sets enhance the CloudFormation deployment process by allowing you to handle stack drift safely. Stack drift occurs when the actual state of your resources differs from what is defined in your CloudFormation template, often due to manual changes made through the AWS Management Console, CLI, or SDK. CloudFormation [drift-aware change sets](drift-aware-change-sets.md) compare your processed stack configuration with the live resource state, and the IDE surfaces these differences so you can bring resources back into compliance before deployment.

#### View stack events
<a name="ide-extension-view-stack-events"></a>

When the deployment starts, you can monitor progress in real time from the CloudFormation panel. Under **Stack Events**, you see a list of operations performed during the deployment. Each event includes details such as:
+ **Timestamp**: The time the event occurred
+ **Resource**: The specific AWS resource being created, updated, or deleted
+ **Status**: The current state of the operation (for example, `CREATE_IN_PROGRESS`, `UPDATE_COMPLETE`, or `ROLLBACK_IN_PROGRESS`)
+ **Reason**: Additional context or error messages, if applicable

You can also view the stack's **Resources** and **Outputs** from this panel. The **Stack Events** view helps you track deployment progress, identify potential issues, and confirm when your stack has completed successfully.

## Initializing a CloudFormation project in the IDE (VS Code only)
<a name="ide-extension-initialize-project"></a>

Initializing a CloudFormation project in the IDE helps you set up a structured workspace with the correct folders, environment configuration, and AWS credentials so you can validate and deploy your templates reliably. You can initialize a new CloudFormation project directly from the IDE to create this recommended setup. This feature is currently available in VS Code only and is not supported in JetBrains IDEs.

**To initialize a CloudFormation project:**
+ **Open the command palette**
  + From VS Code, open the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
  + Choose **AWS CloudFormation: CFN Init: Initialize Project**.
+ **Choose a project directory**
  + By default, the IDE uses your current working directory.
  + You can change this path to any folder where you want to store your CloudFormation templates.
+ **Select your AWS credential profile**
  + You are prompted to choose an AWS credential profile. The selected profile is used for environment detection, validations, and deployments.
+ **Set up your environment**
  + You are prompted to create or select an environment.
  + Environments define where and how your templates are deployed or validated (for example, dev, beta, or production). You can use **AWS CloudFormation: CFN Init: Add Environment** to select or change your environment.
  + You can use **AWS CloudFormation: CFN Init: Remove Environment** to remove the environment you have selected.
+ **(Optional) Import parameter files**
  + If you already have existing parameter files, the IDE allows you to import them during initialization.
  + The IDE automatically detects compatible files and links them to your project for use in template validation and deployment.
+ **Name and finalize the project**
  + Provide a project name, such as beta-environment, and complete the setup.
  + The IDE creates the initial project structure and configuration file for you.

You can run validations, preview deployments, or switch between environments directly from the IDE.

## Open source
<a name="ide-extension-open-source"></a>

The AWS CloudFormation Language Server is open-sourced under the Apache-2.0 License, giving customers full transparency into how template diagnostics, schema validation, and static analysis are performed. This reduces security and compliance friction for customers who require source-level visibility before adopting tooling.

The code base is publicly available on GitHub: [https://github.com/aws-cloudformation/cloudformation-languageserver/](https://github.com/aws-cloudformation/cloudformation-languageserver/).

## Need help?
<a name="ide-extension-need-help"></a>

Try the [CloudFormation community](https://repost.aws/tags/TAm3R3LNU3RfSX9L23YIpo3w) on AWS re:Post.
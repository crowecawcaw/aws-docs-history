# Creating your own runbooks

An Automation runbook defines the _actions_ that
Systems Manager performs on your managed instances and other AWS resources when an automation
runs. Automation is a tool in AWS Systems Manager. A runbook contains one or more steps that run
in sequential order. Each step is built around a single action. Output from one step can
be used as input in a later step.

The process of running these actions and their steps is called the _automation_.

Action types supported for runbooks let you automate a wide variety of operations in
your AWS environment. For example, using the `executeScript` action type,
you can embed a python or PowerShell script directly in your runbook. (When you create a
custom runbook, you can add your script inline, or attach it from an S3 bucket or from
your local machine.) You can automate management of your AWS CloudFormation resources by using
the `createStack` and `deleteStack` action types. In addition,
using the `executeAwsApi` action type, a step can run _any_ API operation in any AWS service, including creating or deleting
AWS resources, starting other processes, initiating notifications, and many more.

For a list of all 20 supported action types for Automation, see [Systems Manager Automation actions reference](automation-actions.md "automation-actions.md").

AWS Systems Manager Automation provides several runbooks with pre-defined steps that you can use
to perform common tasks like restarting one or more Amazon Elastic Compute Cloud (Amazon EC2) instances or
creating an Amazon Machine Image (AMI). You can also create your own runbooks and share them with
other AWS accounts, or make them public for all Automation users.

Runbooks are written using YAML or JSON. Using the **Document
Builder** in the Systems Manager Automation console, however, you can create a
runbook without having to author in native JSON or YAML.

###### Important

If you run an automation workflow that invokes other services by using an AWS Identity and Access Management
(IAM) service role, be aware that the service role must be configured with permission
to invoke those services. This requirement applies to all AWS Automation runbooks
(`AWS-*` runbooks) such as the `AWS-ConfigureS3BucketLogging`,
`AWS-CreateDynamoDBBackup`, and `AWS-RestartEC2Instance`
runbooks, to name a few. This requirement also applies to any custom Automation runbooks
you create that invoke other AWS services by using actions that call other services.
For example, if you use the `aws:executeAwsApi`,
`aws:createStack`, or `aws:copyImage` actions, configure the
service role with permission to invoke those services. You can give permissions to other
AWS services by adding an IAM inline policy to the role. For more information, see
[(Optional) Add an Automation inline
policy or customer managed policy to invoke other AWS services](automation-setup-iam.md#add-inline-policy "automation-setup-iam.md#add-inline-policy").

For information about the actions that you can specify in a runbook, see [Systems Manager Automation actions reference](automation-actions.md "automation-actions.md").

For information about using the AWS Toolkit for Visual Studio Code to create runbooks, see [Working with Systems Manager Automation documents](../../../toolkit-for-vscode/latest/userguide/systems-manager-automation-docs.md "../../../toolkit-for-vscode/latest/userguide/systems-manager-automation-docs.md") in the
_AWS Toolkit for Visual Studio Code User Guide_.

For information about using the visual designer to create a custom runbook, see [Visual design experience for Automation runbooks](automation-visual-designer.md "automation-visual-designer.md").

###### Contents

- [Visual design experience for Automation runbooks](automation-visual-designer.md "automation-visual-designer.md")
  - [Before you begin](automation-visual-designer.md#visual-designer-prerequisites "automation-visual-designer.md#visual-designer-prerequisites")
  - [Overview of the visual design experience
    interface](visual-designer-interface-overview.md "visual-designer-interface-overview.md")
    - [Actions browser](visual-designer-interface-overview.md#visual-designer-actions "visual-designer-interface-overview.md#visual-designer-actions")
    - [Canvas](visual-designer-interface-overview.md#visual-designer-canvas "visual-designer-interface-overview.md#visual-designer-canvas")
    - [Form](visual-designer-interface-overview.md#visual-designer-form "visual-designer-interface-overview.md#visual-designer-form")
    - [Keyboard shortcuts](visual-designer-interface-overview.md#visual-designer-keyboard-shortcuts "visual-designer-interface-overview.md#visual-designer-keyboard-shortcuts")

  - [Using the visual design experience](visual-designer-use.md "visual-designer-use.md")
    - [Create a runbook workflow](visual-designer-use.md#visual-designer-create-runbook-workflow "visual-designer-use.md#visual-designer-create-runbook-workflow")
    - [Design a runbook](visual-designer-use.md#visual-designer-build "visual-designer-use.md#visual-designer-build")
    - [Update your runbook](visual-designer-use.md#visual-designer-update-runbook "visual-designer-use.md#visual-designer-update-runbook")
    - [Export your runbook](visual-designer-use.md#visual-designer-export-runbook "visual-designer-use.md#visual-designer-export-runbook")

  - [Configuring inputs and outputs for
    your actions](visual-designer-action-inputs-outputs.md "visual-designer-action-inputs-outputs.md")
    - [Provide input data for an action](visual-designer-action-inputs-outputs.md#providing-input "visual-designer-action-inputs-outputs.md#providing-input")
    - [Define output data for an action](visual-designer-action-inputs-outputs.md#defining-output "visual-designer-action-inputs-outputs.md#defining-output")

  - [Error handling with the visual design
    experience](visual-designer-error-handling.md "visual-designer-error-handling.md")
    - [Retry action on error](visual-designer-error-handling.md#retry-actions "visual-designer-error-handling.md#retry-actions")
    - [Timeouts](visual-designer-error-handling.md#timeout-seconds "visual-designer-error-handling.md#timeout-seconds")
    - [Failed actions](visual-designer-error-handling.md#failure-actions "visual-designer-error-handling.md#failure-actions")
    - [Canceled actions](visual-designer-error-handling.md#cancel-actions "visual-designer-error-handling.md#cancel-actions")
    - [Critical actions](visual-designer-error-handling.md#critical-actions "visual-designer-error-handling.md#critical-actions")
    - [Ending actions](visual-designer-error-handling.md#end-actions "visual-designer-error-handling.md#end-actions")

  - [Tutorial: Create a runbook using the
    visual design experience](visual-designer-tutorial.md "visual-designer-tutorial.md")
    - [Step 1: Navigate to the visual design experience](visual-designer-tutorial.md#navigate-console "visual-designer-tutorial.md#navigate-console")
    - [Step 2: Create a workflow](visual-designer-tutorial.md#create-workflow "visual-designer-tutorial.md#create-workflow")
    - [Step 3: Review the auto-generated code](visual-designer-tutorial.md#view-generated-code "visual-designer-tutorial.md#view-generated-code")
    - [Step 4: Run your new runbook](visual-designer-tutorial.md#use-tutorial-runbook "visual-designer-tutorial.md#use-tutorial-runbook")
    - [Step 5: Clean up](visual-designer-tutorial.md#cleanup-tutorial-runbook "visual-designer-tutorial.md#cleanup-tutorial-runbook")

- [Authoring Automation
  runbooks](automation-authoring-runbooks.md "automation-authoring-runbooks.md")
  - [Identify your use
    case](automation-authoring-runbooks.md#automation-authoring-runbooks-use-case "automation-authoring-runbooks.md#automation-authoring-runbooks-use-case")
  - [Set up your
    development environment](automation-authoring-runbooks.md#automation-authoring-runbooks-environment "automation-authoring-runbooks.md#automation-authoring-runbooks-environment")
  - [Develop
    runbook content](automation-authoring-runbooks.md#automation-authoring-runbooks-developing-content "automation-authoring-runbooks.md#automation-authoring-runbooks-developing-content")
  - [Example 1:
    Creating parent-child runbooks](automation-authoring-runbooks-parent-child-example.md "automation-authoring-runbooks-parent-child-example.md")
    - [Create the
      child runbook](automation-authoring-runbooks-parent-child-example.md#automation-authoring-runbooks-child-runbook "automation-authoring-runbooks-parent-child-example.md#automation-authoring-runbooks-child-runbook")
    - [Create the
      parent runbook](automation-authoring-runbooks-parent-child-example.md#automation-authoring-runbooks-parent-runbook "automation-authoring-runbooks-parent-child-example.md#automation-authoring-runbooks-parent-runbook")

  - [Example 2:
    Scripted runbook](automation-authoring-runbooks-scripted-example.md "automation-authoring-runbooks-scripted-example.md")
  - [Additional runbook
    examples](automation-document-examples.md "automation-document-examples.md")
    - [Deploy
      VPC architecture and Microsoft Active Directory domain
      controllers](automation-document-architecture-deployment-example.md "automation-document-architecture-deployment-example.md")
    - [Restore a
      root volume from the latest snapshot](automation-document-instance-recovery-example.md "automation-document-instance-recovery-example.md")
    - [Create an
      AMI and cross-Region copy](automation-document-backup-maintenance-example.md "automation-document-backup-maintenance-example.md")

- [Creating input parameters that
  populate AWS resources](populating-input-parameters.md "populating-input-parameters.md")
- [Using Document Builder to create
  runbooks](automation-document-builder.md "automation-document-builder.md")
  - [Create a runbook using Document Builder](automation-document-builder.md#create-runbook "automation-document-builder.md#create-runbook")
  - [Create a runbook that runs
    scripts](automation-document-builder.md#create-runbook-scripts "automation-document-builder.md#create-runbook-scripts")

- [Using scripts in
  runbooks](automation-document-script-considerations.md "automation-document-script-considerations.md")
  - [Permissions for using runbooks](automation-document-script-considerations.md#script-permissions "automation-document-script-considerations.md#script-permissions")
  - [Adding scripts to runbooks](automation-document-script-considerations.md#adding-scripts "automation-document-script-considerations.md#adding-scripts")
  - [Script constraints for runbooks](automation-document-script-considerations.md#script-constraints "automation-document-script-considerations.md#script-constraints")

- [Using conditional statements in
  runbooks](automation-branch-condition.md "automation-branch-condition.md")
  - [Working with the
    aws:branch action](automation-branch-condition.md#branch-action-explained "automation-branch-condition.md#branch-action-explained")
    - [Creating an aws:branch
      step in a runbook](automation-branch-condition.md#create-branch-action "automation-branch-condition.md#create-branch-action")
      - [About creating the output
        variable](automation-branch-condition.md#branch-action-output "automation-branch-condition.md#branch-action-output")

    - [Example aws:branch
      runbooks](automation-branch-condition.md#branch-runbook-examples "automation-branch-condition.md#branch-runbook-examples")
    - [Creating complex branching automations
      with operators](automation-branch-condition.md#branch-operators "automation-branch-condition.md#branch-operators")

  - [Examples of how to use conditional
    options](automation-branch-condition.md#conditional-examples "automation-branch-condition.md#conditional-examples")

- [Using action outputs as
  inputs](automation-action-outputs-inputs.md "automation-action-outputs-inputs.md")
  - [Using JSONPath in runbooks](automation-action-outputs-inputs.md#automation-action-json-path "automation-action-outputs-inputs.md#automation-action-json-path")

- [Creating webhook integrations for
  Automation](creating-webhook-integrations.md "creating-webhook-integrations.md")
  - [Creating integrations
    (console)](creating-webhook-integrations.md#creating-integrations-console "creating-webhook-integrations.md#creating-integrations-console")
  - [Creating integrations
    (command line)](creating-webhook-integrations.md#creating-integrations-commandline "creating-webhook-integrations.md#creating-integrations-commandline")
  - [Creating webhooks for integrations](creating-webhook-integrations.md#creating-webhooks "creating-webhook-integrations.md#creating-webhooks")

- [Handling timeouts in runbooks](automation-handling-timeouts.md "automation-handling-timeouts.md")

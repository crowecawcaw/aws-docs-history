Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Approval' gate YAML

The following is the YAML definition of the **Approval** gate. To learn how to use this gate, see [Requiring approvals on workflow runs](workflows-approval.md "workflows-approval.md").

This action definition exists as a section within a broader workflow definition file. For more
information about this file, see [Workflow YAML definition](workflow-reference.md "workflow-reference.md").

###### Note

Most of the YAML properties that follow have corresponding UI elements in the visual
editor. To look up a UI element, use **Ctrl+F**. The element will be
listed with its associated YAML property.

```
# The workflow definition starts here.
# See Top-level properties for details.

Name: MyWorkflow
SchemaVersion: 1.0
Actions:

# The 'Approval' gate definition starts here.
  `Approval`:
    Identifier: aws/approval@v1
    DependsOn:
      - `another-action`
    Configuration:
      ApprovalsRequired: `number`
```

## Approval

(Required)

Specify the name you want to give the gate. All gate names must be unique within the workflow. Gate names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in gate names.

Default: `Approval_nn`.

Corresponding UI: Configuration tab/**Gate name**

## Identifier

(`Approval`/**Identifier**)

(Required)

Identifies the gate. The **Approval** gate supports version
`1.0.0`. Do not change this property unless you want to shorten the version. For more
information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Default: `aws/approval@v1`.

Corresponding UI: Workflow
diagram/Approval_nn/**aws/approval@v1**
label

## DependsOn

(`Approval`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this gate
to run. By default, when you add a gate to a workflow, the gate is set to depend on the last
action in your workflow. If you remove this property, the gate will not depend on anything,
and will run first, before other actions.

###### Note

A gate must be configured to run before or after an action, action group, or gate. It
cannot be set up to run in parallel with other actions, action groups, and gates.

For more information about the **Depends on** functionality, see [Sequencing gates and actions](workflows-gates-depends-on.md "workflows-gates-depends-on.md").

Corresponding UI: Inputs tab/**Depends on**

## Configuration

(`Approval`/**Configuration**)

(Optional)

A section where you can define the configuration properties of the gate.

Corresponding UI: **Configuration** tab

## ApprovalsRequired

(`Approval`/Configuration/**ApprovalsRequired**)

(Optional)

Specify the minimum number of approvals required to unlock the **Approval**
gate. The minimum is `1`. The maximum is `2`. If omitted, the default is
`1`.

###### Note

If you want to omit the `ApprovalsRequired` property, remove the gate's
`Configuration` section from the workflow definition file.

Corresponding UI: Configuration tab/**Number of approvals**

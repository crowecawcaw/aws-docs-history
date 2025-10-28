Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Workflow YAML definition

The following is the reference documentation for the workflow definition file.

A _workflow definition file_ is a YAML file that describes your workflow.
By default, the file is stored in a `~/.codecatalyst/workflows/` folder in the root of
your [source repository](source-repositories.md "source-repositories.md"). The file can have a .yml or
.yaml extension, and the extension must be lowercase.

To create and edit the workflow definition file, you can use an editor such as vim, or you
can use the CodeCatalyst console's visual editor or YAML editor. For more information, see [Using the CodeCatalyst console's visual and YAML editors](workflow.md#workflow.editors "workflow.md#workflow.editors").

###### Note

Most of the YAML properties that follow have corresponding UI elements in the visual
editor. To look up a UI element, use **Ctrl+F**. The
element will be listed with its associated YAML property.

###### Topics

- [Example of a workflow definition file](#workflow.anatomy "#workflow.anatomy")
- [Syntax guidelines and conventions](#workflow.terms.syntax.conv "#workflow.terms.syntax.conv")
- [Top-level properties](#workflow.top.level "#workflow.top.level")

## Example of a workflow definition file

The following is an example of a simple workflow definition file. It includes a few
top-level properties, a `Triggers` section, and an `Actions`
section with two actions: `Build` and `Test`. For more
information, see [About the workflow definition file](workflow.md#workflow.example "workflow.md#workflow.example").

```
Name: MyWorkflow
SchemaVersion: 1.0
RunMode: QUEUED
Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  Build:
    Identifier: aws/build@v1
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: docker build -t MyApp:latest .
  Test:
    Identifier: aws/managed-test@v1
    DependsOn:
      - Build
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: npm install
        - Run: npm run test
```

## Syntax guidelines and conventions

This section describes the syntax rules for the workflow definition file, as well as
the naming conventions used in this reference documentation.

### YAML syntax guidelines

The workflow definition file is written in YAML and follows the [YAML 1.1 specification](https://yaml.org/spec/ "https://yaml.org/spec/"), so whatever is
allowed in that specification is also allowed in the workflow YAML. If you're new to
YAML, here are some quick guidelines to ensure you're supplying valid YAML
code.

- **Case-sensitivity**: The workflow definition
  file is case-sensitive, so make sure you use the casing shown in this
  documentation.
- **Special characters**: We recommend using
  quotes or double-quotes around property values that include any of the
  following special characters: `{`, `}` ,
  `[` , `]` , &, `*` , `#`
  , `?` , `|` , `-` , < , >,
  `=` , `!` , `%` , `@` ,
  `:` , ```and`,`

If you don't include the quotes, the special characters listed previously
may be interpreted in an unexpected way.

- **Property names**: Property
  _names_ (as opposed to property
  _values_) are limited to alphanumeric characters
  (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
  You cannot use quotes or double-quotes to enable special characters and
  spaces in property names.

Not permitted:

`'My#Build@action'`

`My#Build@action`

`My Build Action`

Permitted:

`My-Build-Action_1`

- **Escape codes**: If your property value
  includes escape codes (for example, `\n` or `\t`),
  follow these guidelines:
  - Use single quotes to return the escape code as a string. For
    example, `'my string \n my string'`, returns the string
    `my string \n my string`.
  - Use double quotes to parse the escape code. For example, `"my
string \n my new line"`, returns:

  ```
  my string
  my new line
  ```

- **Comments**: Preface comments with
  `#`.

Example:

```
Name: MyWorkflow
# This is a comment.
SchemaVersion: 1.0
```

- **Triple dash (`---`)**: Do not
  use `---` in your YAML code. CodeCatalyst ignores everything after the
  `---`.

### Naming conventions

In this guide, we use the terms _property_ and
_section_ to refer to the main items in a workflow definition
file.

- A _property_ is any item that includes a colon
  (`:`). For example, in the following code snippet, all of the
  following are properties: `Name`, `SchemaVersion`,
  `RunMode`, `Triggers`, `Type`, and
  `Branches`.
- A _section_ is any property that has sub-properties. In
  the following code snippet, there is one `Triggers`
  section.

###### Note

In this guide, 'sections' are sometimes referred to as 'properties',
and vise versa, depending on the context.

```
Name: MyWorkflow
SchemaVersion: 1.0
RunMode: QUEUED
Triggers:
  - Type: PUSH
    Branches:
      - main
```

## Top-level properties

The following is the reference documentation for the top-level properties in the
workflow definition file.

```
# Name
Name: `workflow-name`

# Schema version
SchemaVersion: 1.0

# Run mode
RunMode: `QUEUED|SUPERSEDED|PARALLEL`

# Compute
Compute:
...

# Triggers
Triggers:
...

# Actions
Actions:
...


```

### Name

(Required)

The name of the workflow. The workflow name is shown in the workflows list and mentioned in
notifications and logs. The workflow name and workflow definition file name can match, or you can
name them differently. Workflow names do not need to be unique. Workflow names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in workflow names.

Corresponding UI: visual editor/Workflow properties/**Workflow
name**

### SchemaVersion

(Required)

The schema version of the workflow definition. Currently, the only valid value
is `1.0`.

Corresponding UI: _none_

### RunMode

(Optional)

How CodeCatalyst handles multiple runs. You can use one of the following values:

- `QUEUED` – Multiple runs are queued and run one after the other. You
  can have up to 50 runs in a queue.
- `SUPERSEDED` – Multiple runs are queued and run one after the other. A
  queue can only have one run, so if two runs end up together in the same queue, the later run
  supersedes (takes over from) the earlier run, and the earlier run is canceled.
- `PARALLEL` – Multiple runs occur simultaneously.

If this property is omitted, the default is
`QUEUED`.

For more information, see [Configuring the queuing behavior of runs](workflows-configure-runs.md "workflows-configure-runs.md").

Corresponding UI: visual editor/Workflow properties/Advanced/**Run
mode**

### Compute

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

For more information about compute, see [Configuring compute and runtime images](workflows-working-compute.md "workflows-working-compute.md").

Corresponding UI: _none_

```
Name: MyWorkflow
SchemaVersion: 1.0
...
Compute:
  Type: `EC2 | Lambda`
  Fleet: `fleet-name`
  SharedInstance: `true | false`
```

#### Type

(Compute/**Type**)

(Required if `Compute` is set)

The type of compute engine. You can use one of the following values:

- **EC2** (visual editor) or `EC2` (YAML editor)

Optimized for flexibility during action runs.

- **Lambda** (visual editor) or `Lambda` (YAML
  editor)

Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

Corresponding UI: visual editor/Workflow properties/Advanced/**Compute type**

#### Fleet

(Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

For more information about compute fleets, see [Compute fleets](workflows-working-compute.md#compute.fleets "workflows-working-compute.md#compute.fleets").

Corresponding UI: visual editor/Workflow properties/Advanced/**Compute fleet**

#### SharedInstance

(Compute/**SharedInstance**)

(Optional)

Specify the compute sharing capability for your actions. With compute sharing, actions in a
workflow run on the same instance (runtime environment image). You can use one of the following values:

- `TRUE` means that the runtime environment image is shared between workflow actions.
- `FALSE` means that a separate runtime environment image is started and used for each action
  in a workflow, so you can't share resources such as artifacts and variables without extra configuration.

For more information about compute sharing, see [Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

### Triggers

(Optional)

A sequence of one or more triggers for this workflow. If a trigger is not specified,
then you must manually start your workflow.

For more information about triggers, see [Starting a workflow run automatically using
triggers](workflows-add-trigger.md "workflows-add-trigger.md").

Corresponding UI: visual editor/workflow diagram/**Triggers**

```
Name: MyWorkflow
SchemaVersion: 1.0
...
Triggers:
  - Type: PUSH
    Branches:
      - `branch-name`
    FilesChanged:
      - folder1/file
      - folder2/

  - Type: PULLREQUEST
    Events:
      - `OPEN`
      - `CLOSED`
      - `REVISION`
    Branches:
      - `branch-name`
    FilesChanged:
      - file1.txt

  - Type: SCHEDULE
    # Run the workflow at 10:15 am (UTC+0) every Saturday
    Expression: "15 10 ? * 7 *"
    Branches:
      - `branch-name`
```

#### Type

(Triggers/**Type**)

(Required if `Triggers` is set)

Specify the type of trigger. You can use one of the following values:

- **Push** (visual editor) or `PUSH` (YAML editor)

A push trigger starts a workflow run when a change is pushed to your source repository.
The workflow run will use the files in the branch that you're pushing
_to_ (that is, the destination branch).

- **Pull request** (visual editor) or `PULLREQUEST` (YAML
  editor)

A pull request trigger starts a workflow run when a pull request is opened, updated, or
closed in your source repository. The workflow run will use the files in the branch that
you're pulling _from_ (that is, the source branch).

- **Schedule** (visual editor) or `SCHEDULE` (YAML
  editor)

A schedule trigger starts workflow runs on a schedule defined by a cron expression that
you specify. A separate workflow run will start for each branch in your source repository
using the branch's files. (To limit the branches that the trigger activates on, use the
**Branches** field (visual editor) or `Branches` property
(YAML editor).)

When configuring a schedule trigger, follow these guidelines:

    + Only use one schedule trigger per workflow.
    + If you've defined multiple workflows in your CodeCatalyst space, we
     recommend that you schedule no more than 10 of them to start
     concurrently.
    + Make sure you configure the trigger's cron expression with adequate time between
     runs. For more information, see [Expression](#workflow.triggers.expression "#workflow.triggers.expression").

For examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md").

Corresponding UI: visual editor/workflow diagram/Triggers/**Trigger
type**

#### Events

(Triggers/**Events**)

(Required if the trigger `Type` is set to `PULLREQUEST`)

Specify the type of pull request events that will start a workflow run. The following are
the valid values:

- **Pull request is created** (visual editor) or `OPEN` (YAML
  editor)

The workflow run is started when a pull request is created.

- **Pull request is closed** (visual editor) or `CLOSED` (YAML
  editor)

The workflow run is started when a pull request is closed. The `CLOSED`
event's behavior is tricky, and is best understood through an example. See [Example: A trigger
with a pull, branches, and a 'CLOSED' event](workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-pull-close "workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-pull-close") for more
information.

- **New revision is made to pull request** (visual editor) or
  `REVISION` (YAML editor)

The workflow run is started when a revision to a pull request is created. The first
revision is created when the pull request is created. After that, a new revision is created
every time someone pushes a new commit to the source branch specified in the pull
request. If you include the `REVISION` event in your pull request trigger, you
can omit the `OPEN` event, since `REVISION` is a superset of
`OPEN`.

You can specify multiple events in the same pull request trigger.

For examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md").

Corresponding UI: visual editor/workflow diagram/Triggers/**Events for pull
request**

#### Branches

(Triggers/**Branches**)

(Optional)

Specify the branches in your source repository that the trigger monitors in order to know
when to start a workflow run. You can use regex patterns to define your branch names. For
example, use `main.*` to match all branches beginning with
`main`.

The branches to specify are different depending on the trigger type:

- For a push trigger, specify the branches you're pushing _to_,
  that is, the _destination_ branches. One workflow run will start
  per matched branch, using the files in the matched branch.

Examples: `main.*`, `mainline`

- For a pull request trigger, specify the branches you're pushing
  _to_, that is, the _destination_ branches.
  One workflow run will start per matched branch, using the workflow definition file
  and source files in the **source** branch
  (_not_ the matched branch).

Examples: `main.*`, `mainline`, `v1\-.*` (matches
branches that start with `v1-`)

- For a schedule trigger, specify the branches that contain the files that you want
  your scheduled run to use. One workflow run will start per matched branch, using the
  the workflow definition file and source files in the matched branch.

Examples: `main.*`, `version\-1\.0`

###### Note

If you _don't_ specify branches, the trigger monitors all branches
in your source repository, and will start a workflow run using the workflow definition
file and source files in:

- The branch you're pushing _to_ (for push triggers). For
  more information, see [Example: A simple code
  push trigger](workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-simple "workflows-add-trigger-examples.md#workflows-add-trigger-examples-push-simple").
- The branch you're pulling _from_ (for pull request
  triggers). For more information, see [Example: A simple pull
  request trigger](workflows-add-trigger-examples.md#workflows-add-trigger-examples-pull-simple "workflows-add-trigger-examples.md#workflows-add-trigger-examples-pull-simple").
- All branches (for schedule triggers). One workflow run will start per branch
  in your source repository. For more information, see [Example: A simple
  schedule trigger](workflows-add-trigger-examples.md#workflows-add-trigger-examples-schedule-simple "workflows-add-trigger-examples.md#workflows-add-trigger-examples-schedule-simple").

For more information about branches and triggers, see [Usage guidelines for triggers and
branches](workflows-add-trigger-considerations.md "workflows-add-trigger-considerations.md").

For more examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md").

Corresponding UI: visual editor/workflow
diagram/Triggers/**Branches**

#### FilesChanged

(Triggers/**FilesChanged**)

(Optional if the trigger `Type` is set to `PUSH`, or
`PULLREQUEST`. Not supported if the trigger `Type` is set to
`SCHEDULE`.)

Specify the files or folders in your source repository that the trigger monitors in order to
know when to start a workflow run. You can use regular expressions to match file names or
paths.

For examples, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md").

Corresponding UI: visual editor/workflow diagram/Triggers/**Files
changed**

#### Expression

(Triggers/**Expression**)

(Required if the trigger `Type` is set to `SCHEDULE`)

Specify the cron expression that describes when you want your scheduled workflow runs to
occur.

Cron expressions in CodeCatalyst use the following six-field syntax, where each field is separated
by a space:

`minutes`
`hours`
`days-of-month`
`month`
`days-of-week`
`year`

**Examples of cron expressions**

| Minutes | Hours | Days of month | Month | Days of week | Year      | Meaning                                                                                                                                 |
| ------- | ----- | ------------- | ----- | ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0       | 0     | ?             | \*    | MON-FRI      | \*        | Runs a workflow at midnight (UTC+0) every Monday through Friday.                                                                        |
| 0       | 2     | \*            | \*    | ?            | \*        | Runs a workflow at 2:00 am (UTC+0) every day.                                                                                           |
| 15      | 22    | \*            | \*    | ?            | \*        | Runs a workflow at 10:15 pm (UTC+0) every day.                                                                                          |
| 0/30    | 22-2  | ?             | \*    | SAT-SUN      | \*        | Runs a workflow every 30 minutes Saturday through Sunday between 10:00 pm on the starting day and 2:00 am on the following day (UTC+0). |
| 45      | 13    | L             | \*    | ?            | 2023-2027 | Runs a workflow at 1:45 pm (UTC+0) on the last day of the month between the years 2023 and 2027 inclusive.                              | When specifying cron expressions in CodeCatalyst, make sure you follow these guidelines: <br>• Specify a single cron expression per `SCHEDULE` trigger. <br>• Enclose the cron expression in double-quotes (`"`) in the YAML editor. <br>• Specify the time in Coordinated Universal Time (UTC). Other time zones are not supported. <br>• Configure at least 30 minutes between runs. A faster cadence is not supported. <br>• Specify the `days-of-month` or `days-of-week` field, but not both. If you specify a value or an asterisk (`*`) in one of the fields, you must use a question mark (`?`) in the other. The asterisk means 'all' and the question mark means 'any'. For more examples of cron expressions and information about wildcards like `?`, `*`, and `L`, see the [Cron expressions reference](../../../eventbridge/latest/userguide/eb-cron-expressions.md "../../../eventbridge/latest/userguide/eb-cron-expressions.md") in the _Amazon EventBridge User Guide_. Cron expressions in EventBridge and CodeCatalyst work exactly the same way. For examples of schedule triggers, see [Examples: Triggers in workflows](workflows-add-trigger-examples.md "workflows-add-trigger-examples.md"). Corresponding UI: visual editor/workflow diagram/Triggers/**Schedule** ### Actions A sequence of one or more actions for this workflow. CodeCatalyst supports several action types, such as build and test actions, which offer different types of functionality. Each action type has: <br>• an `Identifier` property that indicates the action's unique, hard-coded ID. For example, `aws/build@v1` identifies the build action. <br>• a `Configuration` section that contains properties that are specific to the action. For more information about each action type, see [Action types](workflows-actions.md#workflows-actions-types "workflows-actions.md#workflows-actions-types"). The [Action types](workflows-actions.md#workflows-actions-types "workflows-actions.md#workflows-actions-types") topic has links into the documentation for each action. The following is the YAML reference for actions and action groups in the workflow definition file. ``Name: MyWorkflow SchemaVersion: 1.0 ... Actions: action-or-gate-name: Identifier: `identifier` Configuration: ... #Action groups action-group-name: Actions: ...`` #### action-or-gate-name (Actions/`action-or-gate-name`) (Required) Replace `action-name` with a name you want to give the action. Action names must be unique within the workflow, and must only include alphanumeric characters, hyphens, and underscores. For more information about syntax rules, see [YAML syntax guidelines](#workflow.syntax.conv "#workflow.syntax.conv"). For more information about naming practices for actions, including restrictions, see the action-or-gate-name. Corresponding UI: visual editor/`action-name`/Configuration tab/**Action name** or **Action display name** #### action-group-name (Actions/`action-group-name`) (Optional) An _action group_ contains one or more actions. Grouping actions into action groups helps you keep your workflow organized, and also allows you to configure dependencies between different groups. Replace `action-group-name` with a name you want to give the action group. Action group names must be unique within the workflow, and must only include alphanumeric characters, hyphens, and underscores. For more information about syntax rules, see [YAML syntax guidelines](#workflow.syntax.conv "#workflow.syntax.conv"). For more information about action groups, see [Grouping actions into action groups](workflows-group-actions.md "workflows-group-actions.md"). Corresponding UI: _none_ |

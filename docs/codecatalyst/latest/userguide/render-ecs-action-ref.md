Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Render Amazon ECS task definition' action YAML

The following is the YAML definition of the **Render Amazon ECS task
definition** action. To learn how to use this action, see [Modifying an Amazon ECS task definition](render-ecs-action.md "render-ecs-action.md").

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

# The action definition starts here.
  `ECSRenderTaskDefinition_nn`:
    Identifier: aws/ecs-render-task-definition@v1
    DependsOn:
      - `build-action`
    Compute:
      Type: `EC2 | Lambda`
      Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Inputs:
      # Specify a source or an artifact, but not both.
      Sources:
        - `source-name-1`
      Artifacts:
        - `task-definition-artifact`
      Variables:
        - Name: `variable-name-1`
          Value: `variable-value-1`
        - Name: `variable-name-2`
          Value: `variable-value-2`
    Configuration
      task-definition: `task-definition-path`
      container-definition-name: `container-definition-name`
      image: `docker-image-name`
      environment-variables:
        - `variable-name-1=variable-value-1`
        - `variable-name-2=variable-value-2`
    Outputs:
      Artifacts:
        - Name: `TaskDefArtifact`
          Files: "task-definition*"
      Variables:
        - `task-definition`

```

## ECSRenderTaskDefinition

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `ECSRenderTaskDefinition_nn`.

Corresponding UI: Configuration tab/**Action name**

## Identifier

(`ECSRenderTaskDefinition`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For
more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Default: `aws/ecs-render-task-definition@v1`.

Corresponding UI: Workflow
diagram/ECSRenderTaskDefinition_nn/**aws/ecs-render-task-definition@v1**
label

## DependsOn

(`ECSRenderTaskDefinition`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`ECSRenderTaskDefinition`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`ECSRenderTaskDefinition`/Compute/**Type**)

(Required if [Compute](#render.ecs.computename "#render.ecs.computename") is included)

The type of compute engine. You can use one of the following values:

- **EC2** (visual editor) or `EC2` (YAML editor)

Optimized for flexibility during action runs.

- **Lambda** (visual editor) or `Lambda` (YAML
  editor)

Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

Corresponding UI: Configuration tab/**Compute type**

## Fleet

(`ECSRenderTaskDefinition`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/**Compute fleet**

## Timeout

(`ECSRenderTaskDefinition`/**Timeout**)

(Optional)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Inputs

(`ECSRenderTaskDefinition`/**Inputs**)

(Optional)

The `Inputs` section defines the data that the
`ECSRenderTaskDefinition` needs during a workflow run.

###### Note

Only one input (either a source or an artifact) is allowed per **Render
Amazon ECS task definition** action. Variables do not count towards this
total.

Corresponding UI: **Inputs** tab

## Sources

(`ECSRenderTaskDefinition`/Inputs/**Sources**)

(Required if your task definition file is stored in a source repository)

If your task definition file is stored in a source repository, specify the label of that
source repository. Currently, the only supported label is `WorkflowSource`.

If your task definition file is not contained within a source repository, it must
reside in an artifact generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input

(`ECSRenderTaskDefinition`/Inputs/**Artifacts**)

(Required if your task definition file is stored in an [output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md") from a previous
action)

If the task definition file that you want to deploy is contained in an artifact generated by
a previous action, specify that artifact here. If your task definition file is not contained
within an artifact, it must reside in your source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Configuration tab/**Artifacts - optional**

## Variables - input

(`ECSRenderTaskDefinition`/Inputs/**Variables**)

(Required)

Specify a sequence of name/value pairs that define the input variables that you want to make
available to the action. Variable names are limited to alphanumeric characters (a-z, A-Z, 0-9),
hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to
enable special characters and spaces in variable names.

For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Inputs tab/**Variables - optional**

## Configuration

(`ECSRenderTaskDefinition`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## task-definition

(`ECSRenderTaskDefinition`/Configuration/**task-definition**)

(Required)

Specify the path to an existing task definition file. If the file resides in your
source repository, the path is relative to the source repository root folder. If your
file resides in an artifact from a previous workflow action, the path is relative to the
artifact root folder. For more
information about task definition files, see [Task
definitions](../../../AmazonECS/latest/developerguide/Welcome.md#welcome-task-definitions "../../../AmazonECS/latest/developerguide/Welcome.md#welcome-task-definitions") in the _Amazon Elastic Container Service Developer Guide_.

Corresponding UI: Configuration tab/**Task definition**

## container-definition-name

(`ECSRenderTaskDefinition`/Configuration/**container-definition-name**)

(Required)

Specify the name of the container where your Docker image will run. You can find this name in the
`containerDefinitions`, `name` field in your task definition file. For
more information, see [Name](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_name "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_name") in the _Amazon Elastic Container Service Developer Guide_.

Corresponding UI: Configuration tab/**Container name**

## image

(`ECSRenderTaskDefinition`/Configuration/**image**)

(Required)

Specify the name of the Docker image that you want the **Render Amazon
ECS task definition** action to add to your task definition file. The action adds
this name to the `containerDefinitions`, `image` field in your task
definition file. If a value already exists in the `image` field, then the action
overwrites it. You can include variables in the image name.

Examples:

If you specify `MyDockerImage:${WorkflowSource.CommitId}`, the action adds
`MyDockerImage:`commit-id``to the task definition file,
 where`commit-id` is a commit ID generated at runtime by the
workflow.

If you specify `my-ecr-repo/image-repo:$(date +%m-%d-%y-%H-%m-%s)`, the action
adds `my-ecr-repo`/image-repo:`date
 +%m-%d-%y-%H-%m-%s` to the task definition file, where
`my-ecr-repo` is the URI of an Amazon Elastic Container Registry (ECR) and `date
 +%m-%d-%y-%H-%m-%s` is a timestamp in the format
`month-day-year-hour-minute-second` generated at runtime by the workflow.

For more information about the `image` field, see [Image](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_image "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_image") in the _Amazon Elastic Container Service Developer Guide_. For more information about variables,
see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Configuration tab/**Image name**

## environment-variables

(`ECSRenderTaskDefinition`/Configuration/**environment-variables**)

(Required)

Specify environment variables that you want the **Render Amazon ECS task
definition** action to add to your task definition file. The action adds the variables
to the `containerDefinitions`, `environment` field in your task definition
file. If variables already exist in the file, the action overwrites the values of existing
variables and adds any new variables. For more information about Amazon ECS environment variables, see
[Specifying environment variables](../../../AmazonECS/latest/developerguide/taskdef-envfiles.md "../../../AmazonECS/latest/developerguide/taskdef-envfiles.md") in the _Amazon Elastic Container Service Developer Guide_.

Corresponding UI: Configuration tab/**Environment variables -
optional**

## Outputs

(`ECSRenderTaskDefinition`/**Outputs**)

(Required)

Defines the data that is output by the action during a workflow run.

Corresponding UI: **Outputs** tab

## Artifacts

(`ECSRenderTaskDefinition`/Outputs/**Artifacts**)

(Required)

Specify the artifacts generated by the action. You can reference these artifacts as input in
other actions.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Outputs tab/**Artifacts**

## Name

(`ECSRenderTaskDefinition`/Outputs/Artifacts/**Name**)

(Required)

Specify the name of the artifact that will contain the updated task definition file. The
default value is `MyTaskDefinitionArtifact`. You must then specify this artifact as
input into the **Deploy to Amazon ECS** action. To understand how to add this artifact
as input to the **Deploy to Amazon ECS** action, see [Example: Modify an Amazon ECS taskdef](render-ecs-action-example-workflow.md "render-ecs-action-example-workflow.md").

Corresponding UI: Outputs tab/Artifacts/**Name**

## Files

(`ECSRenderTaskDefinition`/Outputs/Artifacts/**Files**)

(Required)

Specify the files to include in the artifact. You must specify
`task-definition-*` so that the updated task definition file, which starts with
`task-definition-`, will be included.

Corresponding UI: Outputs tab/Artifacts/**Files**

## Variables

(`ECSRenderTaskDefinition`/Outputs/**Variables**)

(Required)

Specify the name of a variable to be set by the render action. The render action will set
this variable's value to the name of the updated task definition file (for example,
`task-definition-*random-string*.json`). You must then
specify this variable in the **Deploy to Amazon ECS** action's **Task
definition** (visual editor) or `task-definition` (yaml editor) property.
To understand how to add this variable to the **Deploy to Amazon ECS** action, see
[Example: Modify an Amazon ECS taskdef](render-ecs-action-example-workflow.md "render-ecs-action-example-workflow.md") .

Default: `task-definition`

Corresponding UI: Outputs tab/Variables/**Name** field

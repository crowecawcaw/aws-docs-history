Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'AWS Lambda invoke' action YAML

The following is the YAML definition of the **AWS Lambda invoke** action.
To learn how to use this action, see [Invoking a Lambda function using a workflow](lam-invoke-action.md "lam-invoke-action.md").

This action definition exists as a section within a broader workflow definition file. For
more information about this file, see [Workflow YAML definition](workflow-reference.md "workflow-reference.md").

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
  `LambdaInvoke_nn`:
    Identifier: aws/lambda-invoke@v1
    DependsOn:
      - `dependent-action`
    Compute:
      Type: `EC2 | Lambda`
      Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Inputs:
      # Specify a source or an artifact, but not both.
      Sources:
        - `source-name-1`
      Artifacts:
        - `request-payload`
      Variables:
        - Name: `variable-name-1`
          Value: `variable-value-1`
        - Name: `variable-name-2`
          Value: `variable-value-2`
    Environment:
      Name: `environment-name`
      Connections:
        - Name: `account-connection-name`
          Role: `iam-role-name`
    Configuration:
      Function: `my-function|function-arn`
      AWSRegion: `us-west-2`
      # Specify RequestPayload or RequestPayloadFile, but not both.
      RequestPayload: `'{"firstname": "Li", lastname: "Jean", "company": "ExampleCo", "team": "Development"}'`
      RequestPayloadFile: `my/request-payload.json`
      ContinueOnError: `true|false`
      LogType: `Tail|None`
      ResponseFilters: `'{"name": ".name", "company": ".department.company"}'`
    Outputs:
      Artifacts:
        - Name: `lambda_artifacts`
          Files:
            - "lambda-response.json"

```

## LambdaInvoke

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `Lambda_Invoke_Action_Workflow_nn`.

Corresponding UI: Configuration tab/**Action name**

## Identifier

(`LambdaInvoke`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For
more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Default: `aws/lambda-invoke@v1`.

Corresponding UI: Workflow
diagram/LambdaInvoke_nn/**aws/lambda-invoke@v1**
label

## DependsOn

(`LambdaInvoke`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`LambdaInvoke`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`LambdaInvoke`/Compute/**Type**)

(Required if [Compute](#lam.invoke.computename "#lam.invoke.computename") is included)

The type of compute engine. You can use one of the following values:

- **EC2** (visual editor) or `EC2` (YAML editor)

Optimized for flexibility during action runs.

- **Lambda** (visual editor) or `Lambda` (YAML
  editor)

Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

Corresponding UI: Configuration tab/**Compute type**

## Fleet

(`LambdaInvoke`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/**Compute fleet**

## Timeout

(`LambdaInvoke`/**Timeout**)

(Required)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Inputs

(`LambdaInvoke`/**Inputs**)

(Required)

The `Inputs` section defines the data that the **AWS Lambda
invoke** action needs during a workflow run.

###### Note

Only one input (either a source or an artifact) is allowed per **AWS Lambda
invoke** action. Variables do not count towards this total.

Corresponding UI: **Inputs** tab

## Sources

(`LambdaInvoke`/Inputs/**Sources**)

(Required if [RequestPayloadFile](#lam.invoke.request.payload.file "#lam.invoke.request.payload.file")
is provided)

If you want to pass a request payload JSON file to the **AWS Lambda invoke**
action, and this payload file is stored in a source repository, specify the label of that
source repository. Currently, the only supported label is `WorkflowSource`.

If your request payload file is not contained within a source repository, it must reside in
an artifact generated by another action.

For more information about the payload file, see [RequestPayloadFile](#lam.invoke.request.payload.file "#lam.invoke.request.payload.file").

###### Note

Instead of specifying a payload file, you can add the payload's JSON code
directly to the action using the `RequestPayload` property. For more information,
see [RequestPayload](#lam.invoke.request.payload "#lam.invoke.request.payload").

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input

(`LambdaInvoke`/Inputs/**Artifacts**)

(Required if [RequestPayloadFile](#lam.invoke.request.payload.file "#lam.invoke.request.payload.file")
is provided)

If you want to pass a request payload JSON file to the **AWS Lambda invoke**
action, and this payload file is contained in an [output
artifact](build-action-ref.md#build.outputs.artifacts "build-action-ref.md#build.outputs.artifacts") from a previous action, specify that artifact here.

For more information about the payload file, see [RequestPayloadFile](#lam.invoke.request.payload.file "#lam.invoke.request.payload.file").

###### Note

Instead of specifying a payload file, you can add the payload's JSON code
directly to the action using the `RequestPayload` property. For more information,
see [RequestPayload](#lam.invoke.request.payload "#lam.invoke.request.payload").

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Configuration tab/**Artifacts - optional**

## Variables - input

(`LambdaInvoke`/Inputs/**Variables**)

(Optional)

Specify a sequence of name/value pairs that define the input variables that you want to make
available to the action. Variable names are limited to alphanumeric characters (a-z, A-Z, 0-9),
hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to
enable special characters and spaces in variable names.

For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Inputs tab/**Variables - optional**

## Environment

(`LambdaInvoke`/**Environment**)

(Required)

Specify the CodeCatalyst environment to use with the action. The action connects to
the AWS account and optional Amazon VPC specified in the chosen environment. The action uses the
default IAM role specified in the environment to connect to the AWS account, and uses the
IAM role specified in the [Amazon VPC connection](../adminguide/managing-vpcs.md "../adminguide/managing-vpcs.md") to
connect to the Amazon VPC.

###### Note

If the default IAM role does not have the permissions required by the action, you can
configure the action to use a different role. For more information, see [Changing the IAM role of an action](deploy-environments-switch-role.md "deploy-environments-switch-role.md").

For more information about environments, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md") and [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

Corresponding UI: Configuration tab/**Environment**

## Name

(`LambdaInvoke`/Environment/**Name**)

(Required if [Environment](#lam.invoke.environment "#lam.invoke.environment") is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections

(`LambdaInvoke`/Environment/**Connections**)

(Optional in newer versions of the action; required in older versions)

Specify the account connection to associate with the action. You can specify a maximum of
one account connection under `Environment`.

If you do not specify an account connection:

- The action uses the AWS account connection and default IAM role specified in the
  environment in the CodeCatalyst console. For information about adding an account connection and
  default IAM role to environment, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").
- The default IAM role must include the policies and permissions required by the action.
  To determine what those policies and permissions are, see the description of the **Role** property in the action's YAML definition documentation.

For more information about account connections, see [Allowing access to AWS resources with connected
AWS accounts](ipa-connect-account.md "ipa-connect-account.md"). For information about adding an account connection to
an environment, see [Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Name

(`LambdaInvoke`/Environment/Connections/**Name**)

(Required if [Connections](#lam.invoke.environment.connections "#lam.invoke.environment.connections") is included)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Role

(`LambdaInvoke`/Environment/Connections/**Role**)

(Required if [Connections](#lam.invoke.environment.connections "#lam.invoke.environment.connections") is included)

Specify the name of the IAM role that the **AWS Lambda invoke** action
uses to access AWS and invoke your Lambda function. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"), and that
the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use the default role in the environment, make sure it has the
following policies.

- The following permissions policy:

###### Warning

Limit the permissions to those shown in the following policy. Using a role with
broader permissions might pose a security risk.

- The following custom trust policy:

###### Note

You can use the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role with this action, if you'd like.
 For more information about this role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has
full access permissions which may pose a security risk. We recommend that you only use this
role in tutorials and scenarios where security is less of a concern.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration
  tab/'Environment/account/role'/**Role**

## Configuration

(`LambdaInvoke`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## Function

(`LambdaInvoke`/Configuration/**Function**)

(Required)

Specify the AWS Lambda function that this action will invoke. You can specify the name of the
function, or its Amazon Resource Name (ARN). You can find the name or ARN in the Lambda
console.

###### Note

The AWS account where the Lambda function resides can be different from the account
specified under `Connections:`.

Corresponding UI: Configuration tab/**Function**

## AWSRegion

(`LambdaInvoke`/Configuration/**AWSRegion**)

(Required)

Specify the AWS Region where your AWS Lambda function resides. For a list of Region codes,
see [Regional
endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in the _AWS General Reference_.

Corresponding UI: Configuration tab/**Destination bucket -
optional**

## RequestPayload

(`LambdaInvoke`/Configuration/**RequestPayload**)

(Optional)

If you want to pass a request payload to the **AWS Lambda invoke**
action, specify the request payload here, in JSON format.

Example request payload:

```
'{ "key": "value" }'
```

If you do not want to pass a request payload to your Lambda function, then omit this
property.

###### Note

You can specify either `RequestPayload` or `RequestPayloadFile`, but
not both.

For more information about the request payload, see the [Invoke](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md") topic in the
_AWS Lambda API Reference_.

Corresponding UI: Configuration tab/**Request payload -
optional**

## RequestPayloadFile

(`LambdaInvoke`/Configuration/**RequestPayloadFile**)

(Optional)

If you want to pass a request payload to the **AWS Lambda invoke** action,
specify the path to this request payload file here. The file must be in JSON format.

The request payload file can reside in a source repository or an artifact from a previous
action. The file path is relative to the source repository or artifact root.

If you do not want to pass a request payload to your Lambda function, then omit this
property.

###### Note

You can specify either `RequestPayload` or `RequestPayloadFile`, but
not both.

For more information about the request payload file, see the [Invoke](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md") topic in the
_AWS Lambda API Reference_.

Corresponding UI: Configuration tab/**Request payload file -
optional**

## ContinueOnError

(`LambdaInvoke`/Configuration/**RequestPayloadFile**)

(Optional)

Specify whether you want to mark the **AWS Lambda invoke** action as succeeded even if the invoked
AWS Lambda function fails. Consider setting this property to `true` to allow
subsequent actions in your workflow to start despite the Lambda failure.

The default is to fail the action if the Lambda function fails ("off" in the visual editor or
`false` in the YAML editor).

Corresponding UI: Configuration tab/**Continue on error**

## LogType

(`LambdaInvoke`/Configuration/**LogType**)

(Optional)

Specify whether you want to include error logs in the response from the Lambda function after
it is invoked. You can view these logs in the **Lambda invoke** action's
**Logs** tab in the CodeCatalyst console. Possible values are:

- `Tail` – return logs
- `None` – do not return logs

The default is **Tail**.

For more information about the log type, see the [Invoke](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md") topic in the
_AWS Lambda API Reference_.

For more information about viewing logs, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").

Corresponding UI: Configuration tab/**Log type**

## ResponseFilters

(`LambdaInvoke`/Configuration/**ResponseFilters**)

(Optional)

Specify which keys in the Lambda response payload you want to convert to output
variables. You can then reference the output variables in subsequent actions in your
workflow. For more information about variables in CodeCatalyst, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

For example, if your response payload looks like this:

```
responsePayload = {
  "name": "Saanvi",
  "location": "Seattle",
  "department": {
    "company": "Amazon",
    "team": "AWS"
  }
}
```

...and your response filters look like this:

```
Configuration:
  ...
  ResponseFilters: '{"name": ".name", "company": ".department.company"}'
```

...then the action generates the following output variables:

| Key     | Value  |
| ------- | ------ |
| name    | Saanvi |
| company | Amazon |

You can then reference the `name` and `company` variables in
subsequent actions.

If you do not specify any keys in `ResponseFilters`, then the action
converts each top-level key in the Lambda response into an output variable. For more information,
see ['AWS Lambda invoke' variables](lam-invoke-action-variables.md "lam-invoke-action-variables.md").

Consider using response filters to limit the generated output variables to only those you
actually want to use.

Corresponding UI: Configuration tab/**Response filters -
optional**

## Outputs

(`LambdaInvoke`/**Outputs**)

(Optional)

Defines the data that is output by the action during a workflow run.

Corresponding UI: **Outputs** tab

## Artifacts

(`LambdaInvoke`/Outputs/**Artifacts**)

(Optional)

Specify the artifacts generated by the action. You can reference these artifacts as input in
other actions.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Outputs tab/Artifacts/**Build artifact
name**

## Name

(`LambdaInvoke`/Outputs/Artifacts/**Name**)

(Optional)

Specify the name of the artifact that will contain the Lambda response payload that is returned
by the Lambda function. The default value is `lambda_artifacts`. If you do not specify
an artifact, then the Lambda response payload can be viewed in the action's logs, which are
available on the **Logs** tab for the action in the CodeCatalyst console. For more
information about viewing logs, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md").

Corresponding UI: Outputs tab/Artifacts/**Build artifact
name**

## Files

(`LambdaInvoke`/Outputs/Artifacts/**Files**)

(Optional)

Specify the files to include in the artifact. You must specify
`lambda-response.json` so that the Lambda response payload file will be
included.

Corresponding UI: Outputs tab/Artifacts/**Files produced by
build**

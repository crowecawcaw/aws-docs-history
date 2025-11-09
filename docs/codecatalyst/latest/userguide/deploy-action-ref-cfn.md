Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Deploy AWS CloudFormation stack' action YAML

The following is the YAML definition of the **Deploy AWS CloudFormation stack**
action. To learn how to use this action, see [Deploying an AWS CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md").

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
  `DeployCloudFormationStack:`
    Identifier: aws/cfn-deploy@v1
    DependsOn:
      - `build-action`
    Compute:
      Type: `EC2 | Lambda`
      Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Environment:
      Name: `environment-name`
      Connections:
        - Name: `account-connection-name`
          Role: `DeployRole`
    Inputs:
      Sources:
        - `source-name-1`
      Artifacts:
        - `CloudFormation-artifact`
    Configuration:
      name: `stack-name`
      region: `us-west-2`
      template: `template-path`
      role-arn: `arn:aws:iam::123456789012:role/StackRole`
      capabilities: `CAPABILITY_IAM,CAPABILITY_NAMED_IAM,CAPABILITY_AUTO_EXPAND`
      parameter-overrides: `KeyOne=ValueOne,KeyTwo=ValueTwo | path-to-JSON-file`
      no-execute-changeset: `1|0`
      fail-on-empty-changeset: `1|0`
      disable-rollback: `1|0`
      termination-protection: `1|0`
      timeout-in-minutes: `minutes`
      notification-arns: `arn:aws:sns:us-east-1:123456789012:MyTopic,arn:aws:sns:us-east-1:123456789012:MyOtherTopic`
      monitor-alarm-arns: `arn:aws:cloudwatch::123456789012:alarm/MyAlarm,arn:aws:cloudwatch::123456789012:alarm/MyOtherAlarm`
      monitor-timeout-in-minutes: `minutes`
      tags: `'[{"Key":"MyKey1","Value":"MyValue1"},{"Key":"MyKey2","Value":"MyValue2"}]'`
```

## DeployCloudFormationStack

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `DeployCloudFormationStack_nn`.

Corresponding UI: Configuration tab/**Action display name**

## Identifier

(`DeployCloudFormationStack`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For
more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Default: `aws/cfn-deploy@v1`.

Corresponding UI: Workflow
diagram/DeployCloudFormationStack_nn/**aws/cfn-deploy@v1**
label

## DependsOn

(`DeployCloudFormationStack`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`DeployCloudFormationStack`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`DeployCloudFormationStack`/Compute/**Type**)

(Required if [Compute](#deploy.action.cfn.computename "#deploy.action.cfn.computename") is included)

The type of compute engine. You can use one of the following values:

- **EC2** (visual editor) or `EC2` (YAML editor)

Optimized for flexibility during action runs.

- **Lambda** (visual editor) or `Lambda` (YAML
  editor)

Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

Corresponding UI: Configuration tab/Advanced - optional/**Compute
type**

## Fleet

(`DeployCloudFormationStack`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/Advanced - optional/**Compute
fleet**

## Timeout

(`DeployCloudFormationStack`/**Timeout**)

(Optional)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout in minutes - optional**

## Environment

(`DeployCloudFormationStack`/**Environment**)

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

(`DeployCloudFormationStack`/Environment/**Name**)

(Required if [Environment](#deploy.action.cfn.environment "#deploy.action.cfn.environment") is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections

(`DeployCloudFormationStack`/Environment/**Connections**)

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

(`DeployCloudFormationStack`/Environment/Connections/**Name**)

(Required if [Connections](#deploy.action.cfn.environment.connections "#deploy.action.cfn.environment.connections") is included)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Role

(`DeployCloudFormationStack`/Environment/Connections/**Role**)

(Required if [Connections](#deploy.action.cfn.environment.connections "#deploy.action.cfn.environment.connections") is included)

Specify the name of the IAM role that the **Deploy AWS CloudFormation stack** action
uses to access AWS and the AWS CloudFormation service. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"), and that
the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use the default role in the environment, make sure it has the
following policies.

- The following permissions policy:

###### Warning

Limit the permissions to those shown in the following policy. Using a role with
broader permissions might pose a security risk.

###### Note

The first time the role is used, use the following wildcard in the resource policy
statement and then scope down the policy with the resource name after it is
available.

```
"Resource": "*"
```

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

## Inputs

(`DeployCloudFormationStack`/**Inputs**)

(Optional)

The `Inputs` section defines the data that the
`DeployCloudFormationStack` needs during a workflow run.

###### Note

A maximum of four inputs (one source and three artifacts) are allowed per
**Deploy AWS CloudFormation stack** action.

If you need to refer to files residing in different inputs (say a source and an
artifact), the source input is the primary input, and the artifact is the secondary
input. References to files in secondary inputs take a special prefix to distiguish them
from the primary. For details, see [Example: Referencing files
in multiple artifacts](workflows-working-artifacts-ex.md#workflows-working-artifacts-ex-ref-file "workflows-working-artifacts-ex.md#workflows-working-artifacts-ex-ref-file").

Corresponding UI: **Inputs** tab

## Sources

(`DeployCloudFormationStack`/Inputs/**Sources**)

(Required if your CloudFormation or AWS SAM template is stored in a source
repository)

If your CloudFormation or AWS SAM template is stored in a source repository, specify the label of
that source repository. Currently, the only supported label is `WorkflowSource`.

If your CloudFormation or AWS SAM template is not contained within a source repository, it must
reside in an artifact generated by another action, or in an Amazon S3 bucket.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts -

input

(`DeployCloudFormationStack`/Inputs/**Artifacts**)

(Required if your CloudFormation or AWS SAM template is stored in an [output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md") from a previous
action)

If the CloudFormation or AWS SAM template that you want to deploy is contained in an artifact
generated by a previous action, specify that artifact here. If your CloudFormation template is not
contained within an artifact, it must reside in your source repository or in an Amazon S3
bucket.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Configuration tab/**Artifacts - optional**

## Configuration

(`DeployCloudFormationStack`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## name

(`DeployCloudFormationStack`/Configuration/**name**)

(Required)

Specify a name for the CloudFormation stack that the **Deploy AWS CloudFormation
stack** action creates or updates.

Corresponding UI: Configuration tab/**Stack name**

## region

(`DeployCloudFormationStack`/Configuration/**region**)

(Required)

Specify the AWS Region into which the stack will be deployed. For a list of Region
codes, see [Regional
endpoints](../../../general/latest/gr/rande.md#region-names-codes "../../../general/latest/gr/rande.md#region-names-codes").

Corresponding UI: Configuration tab/**Stack region**

## template

(`DeployCloudFormationStack`/Configuration/**template**)

(Required)

Specify the name and path to your CloudFormation or AWS SAM template file. The template can be in
JSON or YAML format, and can reside in a source repository, an artifact from a previous action,
or an Amazon S3 bucket. If the template file is in a source repository or artifact, the path is
relative to the source or artifact root. If the template is in an Amazon S3 bucket, the path is the
template's **Object URL** value.

Examples:

`./MyFolder/MyTemplate.json`

`MyFolder/MyTemplate.yml`

`https://MyBucket.s3.us-west-2.amazonaws.com/MyTemplate.yml`

###### Note

You may need to add a prefix to the template's file path to indicate which artifact or
source to find it in. For more information, see [Referencing source repository
files](workflows-sources-reference-files.md "workflows-sources-reference-files.md") and [Referencing files in an
artifact](workflows-working-artifacts-refer-files.md "workflows-working-artifacts-refer-files.md").

Corresponding UI: Configuration tab/**Template**

## role-arn

(`DeployCloudFormationStack`/Configuration/**role-arn**)

(Required)

Specify the Amazon Resource Name (ARN) of the stack role. CloudFormation uses this role to
access and modify resources in your stack. For example:
`arn:aws:iam::123456789012:role/StackRole`.

Make sure the stack role includes:

- One or more permissions policies. The policies depend on the resources you have in your
  stack. For example, if your stack includes an AWS Lambda function, you need to add
  permissions that grant access to Lambda. If you followed the tutorial described in [Tutorial: Deploy a serverless application](deploy-tut-lambda.md "deploy-tut-lambda.md"), it includes a procedure
  titled, [To create a stack role](deploy-tut-lambda.md#deploy-tut-lambda-cfn-roles-stack "deploy-tut-lambda.md#deploy-tut-lambda-cfn-roles-stack") that lists the permissions that the
  stack role needs if you're deploying a typical serverless application stack.

###### Warning

Limit the permissions to those required by the CloudFormation service to access resources
in your stack. Using a role with broader permissions might pose a security risk.

- The following trust policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "cloudformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Optionally, associate this role with your account connection. To learn more about
associating an IAM role with an account connection, see [Adding IAM roles to account
connections](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"). If you
do not associate the stack role with the account connection, then the stack role will not appear
in the **Stack role** drop-down list in the visual editor; however, the role
ARN can still be specified in the `role-arn` field using the YAML editor.

###### Note

You can use the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role with this action, if you'd like.
 For more information about this role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has
full access permissions which may pose a security risk. We recommend that you only use this
role in tutorials and scenarios where security is less of a concern.

Corresponding UI: Configuration tab/**Stack role - optional**

## capabilities

(`DeployCloudFormationStack`/Configuration/**capabilities**)

(Required)

Specify a list of IAM capabilities that are required to allow AWS CloudFormation to create certain stacks. In
most cases, you can leave `capabilities` with the default value of
`CAPABILITY_IAM,CAPABILITY_NAMED_IAM,CAPABILITY_AUTO_EXPAND`.

If you see `##[error] requires capabilities:
 [`capability-name`]` in your **Deploy AWS CloudFormation
stack** action's logs, see [How do I fix IAM capabilities
errors?](troubleshooting-workflows.md#troubleshooting-workflows-capabilities "troubleshooting-workflows.md#troubleshooting-workflows-capabilities") for information about how to fix the
problem.

For more information about IAM capabilities, see [Acknowledging IAM resources in AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md#using-iam-capabilities "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md#using-iam-capabilities") in the
_IAM User Guide_.

Corresponding UI: Configuration tab/Advanced/**Capabilities**

## parameter-overrides

(`DeployCloudFormationStack`/Configuration/**parameter-overrides**)

(Optional)

Specify parameters in your AWS CloudFormation or AWS SAM template that don't have default values, or for
which you want to specify non-default values. For more information about parameters, see [Parameters](../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md "../../../AWSCloudFormation/latest/UserGuide/parameters-section-structure.md")
in the _AWS CloudFormation User Guide_.

The `parameter-overrides` property accepts:

- A JSON file containing the parameters and values.
- A comma-separate list of parameters and values.

###### To specify a JSON file

1. Make sure the JSON file uses one of the following syntaxes:

```
{
  "Parameters": {
    "Param1": "Value1",
    "Param2": "Value2",
    ...
  }
}
```

Or...

```
[
  {
     "ParameterKey": "Param1",
     "ParameterValue": "Value1"
  },
  ...
]
```

(There are other syntaxes, but they are not supported by CodeCatalyst at the time of writing.)
For more information about specifying CloudFormation parameters in a JSON file, see [Supported JSON syntax](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy/index.html#supported-json-syntax "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/deploy/index.html#supported-json-syntax") in the _AWS CLI Command Reference_. 2. Specify the path to the JSON file using one of the following formats:

    * If your JSON file resides in an output artifact from a previous action, use:


    `file:///artifacts/`current-action-name`/`output-artifact-name`/`path-to-json-file``


    See **Example 1** for details.
    * If your JSON file resides in your source repository, use:


    `file:///sources/WorkflowSource/`path-to-json-file``


    See **Example 2** for details.


    **Example 1** – The JSON file resides in an
     output artifact



    ```
    ##My workflow YAML
    ...
    Actions:
      MyBuildAction:
        Identifier: aws/build@v1
        Outputs:
          Artifacts:
            - Name: ParamArtifact
              Files:
                - params.json
        Configuration:
        ...
      MyDeployCFNStackAction:
        Identifier: aws/cfn-deploy@v1
        Configuration:
          `parameter-overrides: file:///artifacts/MyDeployCFNStackAction/ParamArtifact/params.json`

    ```

    **Example 2** – The JSON file resides in your
     source repository, in a folder called `my/folder`



    ```
    ##My workflow YAML
    ...
    Actions:
      MyDeployCloudFormationStack:
        Identifier: aws/cfn-deploy@v1
        Inputs:
          Sources:
            - WorkflowSource
        Configuration:
          `parameter-overrides: file:///sources/WorkflowSource/my/folder/params.json`

    ```

###### To use a comma-separate list of parameters

- Add parameter name-value pairs in the
  `parameter-overrides` property using the following format:

``param-1`=`value-1`,`param-2`=`value-2``

For example, assuming the following AWS CloudFormation template:

```
##My CloudFormation template

Description: My AWS CloudFormation template

Parameters:
  InstanceType:
    Description: Defines the Amazon EC2 compute for the production server.
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - t2.small
      - t3.medium

Resources:
...
```

...you might set the `parameter-overrides` property as follows:

```
##My workflow YAML
...
Actions:
...
  DeployCloudFormationStack:
    Identifier: aws/cfn-deploy@v1
    Configuration:
      `parameter-overrides: InstanceType=t3.medium,UseVPC=true`

```

###### Note

You can specify a parameter name without a corresponding value using
`undefined` as the value. For example:

`parameter-overrides: MyParameter=undefined`

The effect is that during a stack update, CloudFormation uses the existing parameter
value for the given parameter name.

Corresponding UI:

- Configuration tab/Advanced/**Parameter overrides**
- Configuration tab/Advanced/Parameter overrides/**Specify overrides
  using a file**
- Configuration tab/Advanced/Parameter overrides/**Specify overrides
  using a value set**

## no-execute-changeset

(`DeployCloudFormationStack`/Configuration/**no-execute-changeset**)

(Optional)

Specify whether you want CodeCatalyst to create the CloudFormation change set and then stop before
running it. This gives you the opportunity to review the change set in the CloudFormation console. If
you determine that the change set looks good, disable this option and then re-run the workflow so
that CodeCatalyst can create and run the change set without stopping. The default is to create and run
the change set without stopping. For more information, see the AWS CloudFormation [deploy](../../../cli/latest/reference/cloudformation/deploy/index.md "../../../cli/latest/reference/cloudformation/deploy/index.md") parameter in the
_AWS CLI Command Reference_. For more information about viewing change sets, see [Viewing
a change set](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-view.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets-view.md") in the _AWS CloudFormation User Guide_.

Corresponding UI: Configuration tab/Advanced/**No execute change
set**

## fail-on-empty-changeset

(`DeployCloudFormationStack`/Configuration/**fail-on-empty-changeset**)

(Optional)

Specify whether you want CodeCatalyst to fail the **Deploy AWS CloudFormation stack**
action if the CloudFormation change set is empty. (If a change set is empty, it means there were no
changes made to the stack during the latest deployment.) The default is to allow the action to
proceed if the change set is empty, and to return an `UPDATE_COMPLETE` message even
though the stack was not updated.

For more information about this setting, see the AWS CloudFormation [deploy](../../../cli/latest/reference/cloudformation/deploy/index.md "../../../cli/latest/reference/cloudformation/deploy/index.md") parameter in the
_AWS CLI Command Reference_. For more information about change sets, see [Updating
stacks using change sets](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.md") in the _AWS CloudFormation User Guide_.

Corresponding UI: Configuration tab/Advanced/**Fail on empty
changeset**

## disable-rollback

(`DeployCloudFormationStack`/Configuration/**disable-rollback**)

(Optional)

Specify whether you want CodeCatalyst to roll back the stack deployment if it fails. The rollback
returns the stack to the last known stable state. The default is to enable rollbacks. For more
information about this setting, see the AWS CloudFormation [deploy](../../../cli/latest/reference/cloudformation/deploy/index.md "../../../cli/latest/reference/cloudformation/deploy/index.md") parameter in the
_AWS CLI Command Reference_.

For more information about how the **Deploy AWS CloudFormation stack** action handles
rollbacks, see [Configuring rollbacks](deploy-consumption-enable-alarms.md "deploy-consumption-enable-alarms.md").

For more information about rolling back a stack, see [Stack failure
options](../../../AWSCloudFormation/latest/UserGuide/stack-failure-options.md "../../../AWSCloudFormation/latest/UserGuide/stack-failure-options.md") in the _AWS CloudFormation User Guide_.

Corresponding UI: Configuration tab/Advanced/**Disable
rollback**

## termination-protection

(`DeployCloudFormationStack`/Configuration/**termination-protection**)

(Optional)

Specify whether you want the **Deploy AWS CloudFormation stack** to add termination
protection to the stack that it is deploying. If a user attempts to delete a stack with termination protection
enabled, the deletion fails and the stack, including its status, remains unchanged. The default is
to disable termination protection. For more information, see [Protecting a
stack from being deleted](../../../AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.md") in the _AWS CloudFormation User Guide_.

Corresponding UI: Configuration tab/Advanced/**Termination
protection**

## timeout-in-minutes

(`DeployCloudFormationStack`/Configuration/**timeout-in-minutes**)

(Optional)

Specify the amount of time, in minutes, that CloudFormation should allot before timing out stack
creation operations and setting the stack status to `CREATE_FAILED`. If CloudFormation
can't create the entire stack in the time allotted, it fails the stack creation due to timeout
and rolls back the stack.

By default, there is no timeout for stack creation. However,
individual resources may have their own timeouts based on the nature of the service they
implement. For example, if an individual resource in your stack times out, stack creation also
times out even if the timeout you specified for stack creation hasn't yet been reached.

Corresponding UI: Configuration tab/Advanced/**CloudFormation
timeout**

## notification-arns

(`DeployCloudFormationStack`/Configuration/**notification-arns**)

(Optional)

Specify the ARN of an Amazon SNS topic that you want CodeCatalyst to send notification messages to. For
example, `arn:aws:sns:us-east-1:111222333:MyTopic`. When the **Deploy
AWS CloudFormation stack** action runs, CodeCatalyst coordinates with CloudFormation to send one
notification per AWS CloudFormation event that occurs during the stack creation or update process. (The events
are visible in the AWS CloudFormation console's **Events** tab for the stack.) You can specify
up to five topics. For more information, see [What is Amazon SNS?](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md").

Corresponding UI: Configuration tab/Advanced/**Notification
ARNs**

## monitor-alarm-arns

(`DeployCloudFormationStack`/Configuration/**monitor-alarm-arns**)

(Optional)

Specify the Amazon Resource Name (ARN) of an Amazon CloudWatch alarm to use as a rollback trigger.
For example, `arn:aws:cloudwatch::123456789012:alarm/MyAlarm`. You can have a maximum
of five rollback triggers.

###### Note

If you specify a CloudWatch alarm ARN, you'll also need to configure additional permissions to
enable the action to access CloudWatch. For more information, see [Configuring rollbacks](deploy-consumption-enable-alarms.md "deploy-consumption-enable-alarms.md").

Corresponding UI: Configuration tab/Advanced/**Monitor alarm ARNs**

## monitor-timeout-in-minutes

(`DeployCloudFormationStack`/Configuration/**monitor-timeout-in-minutes**)

(Optional)

Specify an amount of time, from 0 to 180 minutes, during which CloudFormation monitors the
specified alarms. Monitoring begins _after_ all the stack resources have been
deployed. If the alarm occurs within the specified monitoring time, then the deployment fails,
and CloudFormation rolls back the entire stack operation.

Default: 0. CloudFormation only monitors alarms while the stack resources are being
deployed, not after.

Corresponding UI: Configuration tab/Advanced/**Monitoring
time**

## tags

(`DeployCloudFormationStack`/Configuration/**tags**)

(Optional)

Specify tags to attach to your CloudFormation stack. Tags are arbitrary key-value pairs that you can use to
identify your stack for purposes such as cost allocation. For more information about what tags
are and how they can be used, see [Tagging your
resources](../../../index.md "../../../index.md") in the _Amazon EC2 User Guide_. For more information about
tagging in CloudFormation, see [Setting AWS CloudFormation stack
options](../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.md") in the _AWS CloudFormation User Guide_.

A key can have alphanumeric characters or spaces, and can have up to 127 characters. A value
can have alphanumeric characters or spaces, and can have up to 255 characters.

You can add up to 50 unique tags for each stack.

Corresponding UI: Configuration tab/Advanced/**Tags**

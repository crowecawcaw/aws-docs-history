Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'AWS CDK bootstrap' action YAML

The following is the YAML definition of the **AWS CDK bootstrap** action.
To learn how to use this action, see [Bootstrapping an AWS CDK app with a workflow](cdk-boot-action.md "cdk-boot-action.md").

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
  `CDKBootstrapAction_nn`:
    Identifier: aws/cdk-bootstrap@v2
    DependsOn:
      - `action-name`
    Compute:
      Type: `EC2 | Lambda`
      Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Inputs:
      # Specify a source or an artifact, but not both.
      Sources:
        - `source-name-1`
      Artifacts:
        - `artifact-name`
    Outputs:
      Artifacts:
        - Name: cdk_bootstrap_artifacts
          Files:
            - "cdk.out/**/*"
    Environment:
      Name: `environment-name`
      Connections:
        - Name: `account-connection-name`
          Role: `iam-role-name`
    Configuration:
      Region: `us-west-2`
      CdkCliVersion: `version`
```

## CDKBootstrapAction

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `CDKBootstrapAction_nn`.

Corresponding UI: Configuration tab/**Action display name**

## Identifier

(`CDKBootstrapAction`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version.
For more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

###### Note

Specifying `aws/cdk-bootstrap@v2` causes the action to run on the [March 2024 image](build-images.md#build.default-image "build-images.md#build.default-image") which includes newer tooling such as
Node.js 18. Specifying `aws/cdk-bootstrap@v1` causes the action to run on the [November 2022 image](build-images.md#build.previous-image "build-images.md#build.previous-image") which includes older tooling such
as Node.js 16.

Default: `aws/cdk-bootstrap@v2`.

Corresponding UI: Workflow
diagram/CDKBootstrapAction_nn/**aws/cdk-bootstrap@v2**
label

## DependsOn

(`CDKBootstrapAction`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`CDKBootstrapAction`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`CDKBootstrapAction`/Compute/**Type**)

(Required if [Compute](#cdk.boot.computename "#cdk.boot.computename") is included)

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

(`CDKBootstrapAction`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/Advanced - optional/**Compute
fleet**

## Timeout

(`CDKBootstrapAction`/**Timeout**)

(Required)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Inputs

(`CDKBootstrapAction`/**Inputs**)

(Optional)

The `Inputs` section defines the data that the **AWS CDK
bootstrap** action needs during a workflow run.

Corresponding UI: **Inputs** tab

###### Note

Only one input (either a source or an artifact) is allowed for each
**AWS CDK bootstrap** action.

## Sources

(`CDKBootstrapAction`/Inputs/**Sources**)

(Required if your AWS CDK app is stored in a source repository)

If your AWS CDK app is stored in a source repository, specify the label of that source
repository. The **AWS CDK bootstrap** action synthesizes the app in this
repository before starting the bootstrapping process. Currently, the only supported repository
label is `WorkflowSource`.

If your AWS CDK app is not contained within a source repository, it must reside in an artifact
generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input

(`CDKBootstrapAction`/Inputs/**Artifacts**)

(Required if your AWS CDK app is stored in an [output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md") from a previous
action)

If your AWS CDK app is contained in an artifact generated by a previous action, specify that
artifact here. The **AWS CDK bootstrap** action synthesizes the app in the
specified artifact into a CloudFormation template before starting the bootstrapping process. If your
AWS CDK app is not contained within an artifact, it must reside in your source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Inputs tab/**Artifacts - optional**

## Outputs

(`CDKBootstrapAction`/**Outputs**)

(Optional)

Defines the data that is output by the action during a workflow run.

Corresponding UI: **Outputs** tab

## Artifacts - output

(`CDKBootstrapAction`/Outputs/**Artifacts**)

(Optional)

Specify the artifacts generated by the action. You can reference these artifacts as input in
other actions.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Outputs tab/**Artifacts**

## Name

(`CDKBootstrapAction`/Outputs/Artifacts/**Name**)

(Required if [Artifacts - output](#cdk.boot.outputs.artifacts "#cdk.boot.outputs.artifacts") is included)

Specify the name of the artifact that will contain the AWS CloudFormation template that is synthesized by
the **AWS CDK bootstrap** action at runtime. The default value is
`cdk_bootstrap_artifacts`. If you do not specify an artifact, then the action
synthesizes the template, but won't save it in an artifact.
Consider saving the
synthesized template in an artifact to preserve a record of it for testing or troubleshooting
purposes.

Corresponding UI: Outputs tab/Artifacts/Add artifact/**Build
artifact name**

## Files

(`CDKBootstrapAction`/Outputs/Artifacts/**Files**)

(Required if [Artifacts - output](#cdk.boot.outputs.artifacts "#cdk.boot.outputs.artifacts") is included)

Specify the files to include in the artifact. You must specify
`"cdk.out/**/*"` to include your AWS CDK app's synthesized AWS CloudFormation template.

###### Note

`cdk.out` is the default directory into which
synthesized files are saved. If you specified an output directory other than `cdk.out` in your
`cdk.json` file, specify that directory here instead of
`cdk.out`.

Corresponding UI: Outputs tab/Artifacts/Add artifact/**Files
produced by build**

## Environment

(`CDKBootstrapAction`/**Environment**)

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

(`CDKBootstrapAction`/Environment/**Name**)

(Required if [Environment](#cdk.boot.environment "#cdk.boot.environment") is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections

(`CDKBootstrapAction`/Environment/**Connections**)

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

(`CDKBootstrapAction`/Environment/Connections/**Name**)

(Required if [Connections](#cdk.boot.environment.connections "#cdk.boot.environment.connections") is included)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Role

(`CDKBootstrapAction`/Environment/Connections/**Role**)

(Required if [Connections](#cdk.boot.environment.connections "#cdk.boot.environment.connections") is included)

Specify the name of the IAM role that the **AWS CDK bootstrap** action uses
to access AWS and add the bootstrap stack. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"), and that
the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use the
default role in the environment, make sure it has the appropriate policies.

You can use the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role with this action, if you'd like. For more information
 about this role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has
full access permissions which may pose a security risk. We recommend that you only use this role
in tutorials and scenarios where security is less of a concern.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration
  tab/'Environment/account/role'/**Role**

## Configuration

(`CDKBootstrapAction`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## Region

(`CDKBootstrapAction`/Configuration/**Region**)

(Required)

Specify the AWS Region into which the bootstrap stack will be deployed. This Region should
match the one into which your AWS CDK app is deployed. For a list of Region codes, see [Regional
endpoints](../../../general/latest/gr/rande.md#region-names-codes "../../../general/latest/gr/rande.md#region-names-codes").

Corresponding UI: Configuration tab/**Region**

## CdkCliVersion

(`CDKBootstrapAction`/Configuration/**CdkCliVersion**)

(Optional)

This property is available with version 1.0.13 or later of the **AWS CDK
deploy** action, and version 1.0.8 or later of the **AWS CDK
bootstrap** action.

Specify one of the following:

- The full version of the AWS Cloud Development Kit (AWS CDK) Command Line Interface (CLI) (also called the AWS CDK
  Toolkit) that you want this action to use. Example: `2.102.1`. Consider
  specifying a full version to ensure consistency and stability when building and deploying
  your application.

Or

- `latest`. Consider specifying `latest` to take advantage of the
  latest features and fixes of the CDK CLI.

The action will download the specified version (or the latest version) of the AWS CDK CLI to
the CodeCatalyst [build image](build-images.md "build-images.md"), and then use this version to run the
commands necessary to deploy your CDK application or bootstrap your AWS
environment.

For a list of supported CDK CLI versions you can use, see [AWS CDK Versions](../../../cdk/api/versions.md "../../../cdk/api/versions.md").

If you omit this property, the action uses a default AWS CDK CLI version described in one of
the following topics:

- [CDK CLI versions used by the 'AWS CDK
  deploy' action](cdk-dep-action.md#cdk-dep-action-cdk-version "cdk-dep-action.md#cdk-dep-action-cdk-version")
- [CDK CLI versions used by the "AWS CDK
  bootstrap" action](cdk-boot-action.md#cdk-boot-action-cdk-version "cdk-boot-action.md#cdk-boot-action-cdk-version")

Corresponding UI: Configuration tab/**AWS CDK CLI version**

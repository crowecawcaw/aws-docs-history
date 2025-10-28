Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'AWS CDK deploy' action YAML

The following is the YAML definition of the **AWS CDK deploy** action. To
learn how to use this action, see [Deploying an AWS CDK app with a workflow](cdk-dep-action.md "cdk-dep-action.md").

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
  `CDKDeploy_nn`:
    Identifier: aws/cdk-deploy@v2
    DependsOn:
      - `CDKBootstrap`
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
        - Name: cdk_artifact
          Files:
            - "cdk.out/**/*"
    Environment:
      Name: `environment-name`
      Connections:
        - Name: `account-connection-name`
          Role: `iam-role-name`
    Configuration:
      StackName: `my-cdk-stack`
      Region: `us-west-2`
      Tags: `'{"key1": "value1", "key2": "value2"}'`
      Context: `'{"key1": "value1", "key2": "value2"}'`
      CdkCliVersion: `version`
      CdkRootPath: `directory-containing-cdk.json-file`
      CfnOutputVariables: `'["CnfOutputKey1","CfnOutputKey2","CfnOutputKey3"]'`
      CloudAssemblyRootPath: `path-to-cdk.out`
```

## CDKDeploy

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `CDKDeploy_nn`.

Corresponding UI: Configuration tab/**Action name**

## Identifier

(`CDKDeploy`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version.
For more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

###### Note

Specifying `aws/cdk-deploy@v2` causes the action to run on the [March 2024 image](build-images.md#build.default-image "build-images.md#build.default-image") which includes newer tooling such as
Node.js 18. Specifying `aws/cdk-deploy@v1` causes the action to run on the [November 2022 image](build-images.md#build.previous-image "build-images.md#build.previous-image") which includes older tooling such
as Node.js 16.

Default: `aws/cdk-deploy@v2`.

Corresponding UI: Workflow
diagram/CDKDeploy_nn/**aws/cdk-deploy@v2**
label

## DependsOn

(`CDKDeploy`/**DependsOn**)

(Optional)

Specify an action or action group that must run successfully in order for the
**AWS CDK deploy** action to run. We recommend specifying the
**AWS CDK bootstrap** action in the `DependsOn` property, like
this:

```
CDKDeploy:
  Identifier: aws/cdk-deploy@v2
  DependsOn:
    - CDKBootstrap
```

###### Note

[Bootstrapping](../../../cdk/v2/guide/bootstrapping.md "../../../cdk/v2/guide/bootstrapping.md") is
a mandatory prerequisite for deploying an AWS CDK app. If you do not include the **AWS CDK
Bootstrap** action in your workflow, then you must find another way to deploy the
AWS CDK bootstrap stack before running your **AWS CDK deploy** action. For
more information, see [Adding the 'AWS CDK deploy' action](cdk-dep-action-add.md "cdk-dep-action-add.md") in [Deploying an AWS CDK app with a workflow](cdk-dep-action.md "cdk-dep-action.md").

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`CDKDeploy`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`CDKDeploy`/Compute/**Type**)

(Required if [Compute](#cdk.dep.computename "#cdk.dep.computename")
is included)

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

(`CDKDeploy`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/Advanced - optional/**Compute
fleet**

## Timeout

(`CDKDeploy`/**Timeout**)

(Required)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Inputs

(`CDKDeploy`/**Inputs**)

(Optional)

The `Inputs` section defines the data that the
`CDKDeploy` needs during a workflow run.

###### Note

Only one input (either a source or an artifact) is allowed for each
**AWS CDK deploy** action.

Corresponding UI: **Inputs** tab

## Sources

(`CDKDeploy`/Inputs/**Sources**)

(Required if the AWS CDK app you want to deploy is stored in a source repository)

If your AWS CDK app is stored in a source repository, specify the label of that source
repository. The **AWS CDK deploy** action synthesizes the app in this
repository before starting the deployment process. Currently, the only supported label is
`WorkflowSource`.

If your AWS CDK app is not contained within a source repository, it must reside in an artifact
generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input

(`CDKDeploy`/Inputs/**Artifacts**)

(Required if the AWS CDK app you want to deploy is stored in an [output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md") from a previous
action)

If your AWS CDK app is contained in an artifact generated by a previous action, specify that
artifact here. The **AWS CDK deploy** action synthesizes the app in the specified artifact into a CloudFormation
template before starting the deployment process. If your AWS CDK app is not contained within an artifact, it must reside in your
source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Inputs tab/**Artifacts - optional**

## Outputs

(`CDKDeploy`/**Outputs**)

(Optional)

Defines the data that is output by the action during a workflow run.

Corresponding UI: **Outputs** tab

## Artifacts - output

(`CDKDeploy`/Outputs/**Artifacts**

(Optional)

Specify the artifacts generated by the action. You can reference these artifacts as input in
other actions.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Outputs tab/**Artifacts**

## Name

(`CDKDeploy`/Outputs/Artifacts/**Name**)

(Required if [Artifacts - output](#cdk.dep.outputs.artifacts "#cdk.dep.outputs.artifacts") is included)

Specify the name of the artifact that will contain the AWS CloudFormation template that is synthesized by
the **AWS CDK deploy** action at runtime. The default value is
`cdk_artifact`. If you do not specify an artifact, then the action synthesizes the
template but won't save it in an artifact. Consider saving the synthesized template in an artifact
to preserve a record of it for testing or troubleshooting purposes.

Corresponding UI: Outputs tab/Artifacts/Add artifact/**Build
artifact name**

## Files

(`CDKDeploy`/Outputs/Artifacts/**Files**)

(Required if [Artifacts - output](#cdk.dep.outputs.artifacts "#cdk.dep.outputs.artifacts") is included)

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

(`CDKDeploy`/**Environment**)

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

(`CDKDeploy`/Environment/**Name**)

(Required if [Environment](#cdk.dep.environment "#cdk.dep.environment")
is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections

(`CDKDeploy`/Environment/**Connections**)

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

(`CDKDeploy`/Environment/Connections/**Name**)

(Required if [Connections](#cdk.dep.environment.connections "#cdk.dep.environment.connections") is included)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Role

(`CDKDeploy`/Environment/Connections/**Role**)

(Required if [Connections](#cdk.dep.environment.connections "#cdk.dep.environment.connections") is included)

Specify the name of the account connection.

Specify the name of the IAM role that the **AWS CDK deploy** action
uses to access AWS and deploy the AWS CDK application stack. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"), and that
the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use the default role in the environment, make sure it has the
following policies.

- The following permissions policy:

###### Warning

Limit the permissions to those shown in the following policy.
Using a role with broader permissions might pose a security risk.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "cloudformation:DescribeStackEvents",
 "cloudformation:DescribeChangeSet",
 "cloudformation:DescribeStacks",
 "cloudformation:ListStackResources"
 ],
 "Resource": "*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": "sts:AssumeRole",
 "Resource": "arn:aws:iam::`111122223333`:role/cdk-*"
 }
 ]
}`

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

## Configuration

(`CDKDeploy`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## StackName

(`CDKDeploy`/Configuration/**StackName**)

(Required)

The name of your AWS CDK app stack, as it appears in the entrypoint file in your AWS CDK app's
`bin` directory. The following example shows the contents of a
TypeScript
entrypoint file, with the stack name highlighted in `red italics`. If
your entrypoint file is in a different language, it will look similar.

```
import * as cdk from 'aws-cdk-lib';
import { CdkWorksopTypescriptStack } from '../lib/cdk_workshop_typescript-stack';

const app = new cdk.App();
new CdkWorkshopTypescriptStack(app, '`CdkWorkshopTypescriptStack`');
```

You can only specify one stack.

###### Tip

If you have multiple stacks, you can create a parent stack with nested stacks. You can
then specify the parent stack in this action to deploy all stacks.

Corresponding UI: Configuration tab/**Stack name**

## Region

(`CDKDeploy`/Configuration/**Region**)

(Optional)

Specify the AWS Region into which the AWS CDK application stack will be deployed. For a list
of Region codes, see [Regional endpoints](../../../general/latest/gr/rande.md#region-names-codes "../../../general/latest/gr/rande.md#region-names-codes").

If you do not specify a Region, the **AWS CDK deploy** action deploys into
the Region specified in your AWS CDK code. For more information, see [Environments](../../../cdk/v2/guide/environments.md "../../../cdk/v2/guide/environments.md") in the
_AWS Cloud Development Kit (AWS CDK) Developer Guide_.

Corresponding UI: Configuration tab/**Region**

## Tags

(`CDKDeploy`/Configuration/**Tags**)

(Optional)

Specify tags that you want to apply to the AWS resources in the AWS CDK application stack.
Tags are applied to the stack itself as well as to individual resources in the stack. For more
information about tagging, see [Tagging](../../../cdk/v2/guide/tagging.md "../../../cdk/v2/guide/tagging.md") in the _AWS Cloud Development Kit (AWS CDK) Developer Guide_.

Corresponding UI: Configuration tab/Advanced -
optional/**Tags**

## Context

(`CDKDeploy`/Configuration/**Context**)

(Optional)

Specify contexts, in the form of key-value pairs, to associate with the AWS CDK application
stack. For more information about contexts, see [Runtime contexts](../../../cdk/v2/guide/context.md "../../../cdk/v2/guide/context.md") in the
_AWS Cloud Development Kit (AWS CDK) Developer Guide_.

Corresponding UI: Configuration tab/Advanced -
optional/**Context**

## CdkCliVersion

(`CDKDeploy`/Configuration/**CdkCliVersion**)

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

## CdkRootPath

(`CDKDeploy`/Configuration/**CdkRootPath**)

(Optional)

The path to the directory that contains your AWS CDK project's
`cdk.json` file. The **AWS CDK deploy** action
runs from this folder, and any outputs created by the action will be added to this
directory. If unspecified, the **AWS CDK deploy** action assumes that the
`cdk.json` file is in the root of your AWS CDK project.

Corresponding UI: Configuration tab/**Directory where the cdk.json
resides**

## CfnOutputVariables

(`CDKDeploy`/Configuration/**CfnOutputVariables**)

(Optional)

Specify which `CfnOutput` constructs in your AWS CDK application code you want to
expose as workflow output variables. You can then reference the workflow output variables in
subsequent actions in your workflow. For more information about variables in CodeCatalyst, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

For example, if your AWS CDK application code looks like this:

```
import { Duration, Stack, StackProps, CfnOutput, RemovalPolicy} from 'aws-cdk-lib';
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as s3 from 'aws-cdk-lib/aws-s3';
import { Construct } from 'constructs';
import * as cdk from 'aws-cdk-lib';
export class HelloCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const bucket = new s3.Bucket(this, 'amzn-s3-demo-bucket', {
      removalPolicy: RemovalPolicy.DESTROY,
    });
    **`new CfnOutput(this, 'bucketName', {`**
      value: bucket.bucketName,
      description: 'The name of the s3 bucket',
      exportName: 'amzn-s3-demo-bucket',
    });
    const table = new dynamodb.Table(this, 'todos-table', {
      partitionKey: {name: 'todoId', type: dynamodb.AttributeType.NUMBER},
      billingMode: dynamodb.BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY,
    })
    **`new CfnOutput(this, 'tableName', {`**
      value: table.tableName,
      description: 'The name of the dynamodb table',
      exportName: 'myDynamoDbTable',
    });
    ...
  }
}
```

...and your `CfnOutputVariables` property looks like this:

```
Configuration:
  ...
  CfnOutputVariables: '["bucketName","tableName"]'
```

...then the action generates the following workflow output variables:

| Key        | Value               |
| ---------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bucketName | `bucket.bucketName` |
| tableName  | `table.tableName`   | You can then reference the `bucketName` and `tableName` variables in subsequent actions. To learn how to reference workflow output variables in subsequent actions, see [Referencing a predefined variable](workflows-working-with-variables-reference-output-vars.md "workflows-working-with-variables-reference-output-vars.md"). If you do not specify any `CfnOutput` constructs in the `CfnOutputVariables` property, then the action exposes the first four (or fewer) CloudFormation output variables it finds as workflow output variables. For more information, see ['AWS CDK deploy' variables](cdk-dep-action-variables.md "cdk-dep-action-variables.md"). ###### Tip To obtain a list of all the CloudFormation output variables the action produces, run the workflow containing the **AWS CDK deploy** action once, and then look in the action's **Logs** tab. The logs contain a list of all the CloudFormation output variables associated with your AWS CDK app. Once you know what all the CloudFormation variables are, you can specify which ones you want to convert to workflow output variables using the `CfnOutputVariables` property. For more information about AWS CloudFormation output variables, see the documentation for the `CfnOutput` construct, available at [class CfnOutput (construct)](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md") in the _AWS Cloud Development Kit (AWS CDK) API Reference_. Corresponding UI: Configuration tab/**AWS CloudFormation output variables** ## CloudAssemblyRootPath (`CDKDeploy`/Configuration/**CloudAssemblyRootPath**) (Optional) If you have already synthesized your AWS CDK app's stack into a cloud assembly (using the `cdk synth` operation), specify the root path of the cloud assembly directory (`cdk.out`). The AWS CloudFormation template located in the specified cloud assembly directory will be deployed by the **AWS CDK deploy** action into your AWS account using the `cdk deploy --app` command. When the `--app` option is present, the `cdk synth` operation does not occur. If you do not specify a cloud assembly directory, then the **AWS CDK deploy** action will run the `cdk deploy` command without the `--app` option. Without the `--app` option, the `cdk deploy` operation will both synthesize (`cdk synth`) and deploy your AWS CDK app into your AWS account. **Why would I specify an existing, synthesized cloud assembly when the "AWS CDK deploy" action can do the synthesis at run time?** You might want to specify an existing, synthesized cloud assembly to: <br>• **Ensure that the exact same set of resources are deployed every time the "AWS CDK deploy" action runs** If you don't specify a cloud assembly, it's possible for the **AWS CDK deploy** action to synthesize and deploy different files depending on when it is run. For example, the **AWS CDK deploy** action might synthesize a cloud assembly with one set of dependencies during a testing stage, and another set of dependencies during a production stage (if those dependencies changed between stages). To guarantee exact parity between what is tested and what is deployed, we recommend synthesizing once and then using the **Path to cloud assembly directory** field (visual editor) or `CloudAssemblyRootPath` property (YAML editor) to specify the already-synthesized cloud assembly. <br>• **Use non-standard package managers and tooling with the AWS CDK app** During a `synth` operation, the **AWS CDK deploy** action tries to run your app using standard tools such as npm or pip. If the action can't successfully run your app using those tools, the synthesis will not occur and the action will fail. To work around this issue, you can specify the exact commands needed to run your app successfully in the AWS CDK app's `cdk.json` file, and then synthesize your app using a method that does not involve the **AWS CDK deploy** action. After the cloud assembly has been generated, you can specify it in the **Path to cloud assembly directory** field (visual editor) or `CloudAssemblyRootPath` property (YAML editor) of the **AWS CDK deploy** action. For information about configuring the `cdk.json` file to include commands for installing and running your AWS CDK app, see [Specifying the app command](../../../cdk/v2/guide/cli.md#cli-app-command "../../../cdk/v2/guide/cli.md#cli-app-command"). For information about the `cdk deploy` and `cdk synth` commands, as well as the `--app` option, see [Deploying stacks](../../../cdk/v2/guide/cli.md#cli-deploy "../../../cdk/v2/guide/cli.md#cli-deploy"), [Synthesizing stacks](../../../cdk/v2/guide/cli.md#cli-synth "../../../cdk/v2/guide/cli.md#cli-synth") and [Skipping synthesis](../../../cdk/v2/guide/cli.md#cli-deploy-nosynth "../../../cdk/v2/guide/cli.md#cli-deploy-nosynth") in the _AWS Cloud Development Kit (AWS CDK) Developer Guide_. For information about cloud assemblies, see [Cloud Assembly](../../../cdk/api/v2/docs/cloud-assembly-schema-readme.md "../../../cdk/api/v2/docs/cloud-assembly-schema-readme.md") in the _AWS Cloud Development Kit (AWS CDK) API Reference_. Corresponding UI: Configuration tab/**Path to cloud assembly directory** |

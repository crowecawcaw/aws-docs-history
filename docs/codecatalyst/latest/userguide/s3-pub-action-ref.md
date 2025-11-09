Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# 'Amazon S3 publish' action YAML

The following is the YAML definition of the **Amazon S3 publish** action. To
learn how to use this action, see [Publishing files to Amazon S3 with a workflow](s3-pub-action.md "s3-pub-action.md").

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
  `S3Publish_nn`:
    Identifier: aws/s3-publish@v1
    DependsOn:
      - `build-action`
    Compute:
      Type: `EC2 | Lambda`
      Fleet: `fleet-name`
    Timeout: `timeout-minutes`
    Inputs:
      Sources:
        - `source-name-1`
      Artifacts:
        - `artifact-name`
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
      SourcePath: `my/source`
      DestinationBucketName: `amzn-s3-demo-bucket`
      TargetPath: `my/target`
```

## S3Publish

(Required)

Specify the name of the action. All action names must be unique within the workflow. Action names are limited to
alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and underscores (\_). Spaces are not allowed.
You cannot use quotation marks to enable special characters and spaces in action names.

Default: `S3Publish_nn`.

Corresponding UI: Configuration tab/**Action name**

## Identifier

(`S3Publish`/**Identifier**)

(Required)

Identifies the action. Do not change this property unless you want to change the version. For
more information, see [Specifying the action version to use](workflows-action-versions.md "workflows-action-versions.md").

Default: `aws/s3-publish@v1`.

Corresponding UI: Workflow
diagram/S3Publish_nn/**aws/s3-publish@v1**
label

## DependsOn

(`S3Publish`/**DependsOn**)

(Optional)

Specify an action, action group, or gate that must run successfully in order for this action to
run.

For more information about the 'depends on' functionality, see [Sequencing actions](workflows-depends-on.md "workflows-depends-on.md").

Corresponding UI: Inputs tab/**Depends on - optional**

## Compute

(`S3Publish`/**Compute**)

(Optional)

The computing engine used to run your workflow actions. You can specify compute either at the workflow level or at the action level,
but not both. When specified at the workflow level, the compute configuration applies to all actions defined in the workflow. At the workflow
level, you can also run multiple actions on the same instance. For more information, see
[Sharing compute across actions](compute-sharing.md "compute-sharing.md").

Corresponding UI: _none_

## Type

(`S3Publish`/Compute/**Type**)

(Required if [Compute](#s3.pub.computename "#s3.pub.computename")
is included)

The type of compute engine. You can use one of the following values:

- **EC2** (visual editor) or `EC2` (YAML editor)

Optimized for flexibility during action runs.

- **Lambda** (visual editor) or `Lambda` (YAML
  editor)

Optimized action start-up speeds.

For more information about compute types, see [Compute types](workflows-working-compute.md#compute.types "workflows-working-compute.md#compute.types").

Corresponding UI: Configuration tab/**Compute type**

## Fleet

(`S3Publish`/Compute/**Fleet**)

(Optional)

Specify the machine or fleet that will run your workflow or workflow actions. With on-demand fleets, when an action starts, the workflow provisions the resources it needs, and the machines are destroyed when the action finishes. Examples of on-demand fleets: `Linux.x86-64.Large`, `Linux.x86-64.XLarge`. For more information about on-demand fleets, see [On-demand fleet properties](workflows-working-compute.md#compute.on-demand "workflows-working-compute.md#compute.on-demand").

With provisioned fleets, you configure a set of dedicated machines to run your workflow actions. These machines remain idle, ready to process actions immediately. For more information about provisioned fleets, see [Provisioned fleet properties](workflows-working-compute.md#compute.provisioned-fleets "workflows-working-compute.md#compute.provisioned-fleets").

If `Fleet` is omitted, the default is `Linux.x86-64.Large`.

Corresponding UI: Configuration tab/**Compute fleet**

## Timeout

(`S3Publish`/**Timeout**)

(Required)

Specify the amount of time in minutes (YAML editor), or hours and minutes (visual editor),
that the action can run before CodeCatalyst ends the action. The minimum is 5 minutes and the maximum is
described in [Quotas for workflows in CodeCatalyst](workflows-quotas.md "workflows-quotas.md"). The default timeout is
the same as the maximum timeout.

Corresponding UI: Configuration tab/**Timeout - optional**

## Inputs

(`S3Publish`/**Inputs**)

(Optional)

The `Inputs` section defines the data that the
`S3Publish` needs during a workflow run.

###### Note

A maximum of four inputs (one source and three artifacts) are allowed for each
**AWS CDK deploy** action. Variables do not count towards this
total.

If you need to refer to files residing in different inputs (say a source and an
artifact), the source input is the primary input, and the artifact is the secondary
input. References to files in secondary inputs take a special prefix to distiguish them
from the primary. For details, see [Example: Referencing files
in multiple artifacts](workflows-working-artifacts-ex.md#workflows-working-artifacts-ex-ref-file "workflows-working-artifacts-ex.md#workflows-working-artifacts-ex-ref-file").

Corresponding UI: **Inputs** tab

## Sources

(`S3Publish`/Inputs/**Sources**)

(Required if the files you want to publish to Amazon S3 are stored in a source
repository)

If the files that you want to publish to Amazon S3 are stored in a source repository, specify the
label of that source repository. Currently, the only supported label is
`WorkflowSource`.

If the files that you want to publish to Amazon S3 are not contained within a source repository, they must reside in
an artifact generated by another action.

For more information about sources, see [Connecting source repositories to workflows](workflows-sources.md "workflows-sources.md").

Corresponding UI: Inputs tab/**Sources - optional**

## Artifacts - input

(`S3Publish`/Inputs/**Artifacts**)

(Required if the files you want to publish to Amazon S3 are stored in an [output artifact](workflows-working-artifacts-output.md "workflows-working-artifacts-output.md") from a previous
action)

If the files that you want to publish to Amazon S3 are contained in an artifact
generated by a previous action, specify that artifact here. If your files are not
contained within an artifact, they must reside in your source repository.

For more information about artifacts, including examples, see [Sharing artifacts and files between
actions](workflows-working-artifacts.md "workflows-working-artifacts.md").

Corresponding UI: Configuration tab/**Artifacts - optional**

## Variables - input

(`S3Publish`/Inputs/**Variables**)

(Optional)

Specify a sequence of name/value pairs that define the input variables that you want to make
available to the action. Variable names are limited to alphanumeric characters (a-z, A-Z, 0-9),
hyphens (-), and underscores (\_). Spaces are not allowed. You cannot use quotation marks to
enable special characters and spaces in variable names.

For more information about variables, including examples, see [Using variables in workflows](workflows-working-with-variables.md "workflows-working-with-variables.md").

Corresponding UI: Inputs tab/**Variables - optional**

## Environment

(`S3Publish`/**Environment**)

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

(`S3Publish`/Environment/**Name**)

(Required if [Environment](#s3.pub.environment "#s3.pub.environment")
is included)

Specify the name of an existing environment that you want to associate with the action.

Corresponding UI: Configuration tab/**Environment**

## Connections

(`S3Publish`/Environment/**Connections**)

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

(`S3Publish`/Environment/Connections/**Name**)

(Required if [Connections](#s3.pub.environment.connections "#s3.pub.environment.connections") is included)

Specify the name of the account connection.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration tab/'Environment/account/role'/**AWS
  account connection**

## Role

(`S3Publish`/Environment/Connections/**Role**)

(Required if [Connections](#s3.pub.environment.connections "#s3.pub.environment.connections") is included)

Specify the name of the IAM role that the **Amazon S3 publish** action uses
to access AWS and to copy files to Amazon S3. Make sure that you have [added the role to your CodeCatalyst space](ipa-connect-account-addroles.md "ipa-connect-account-addroles.md"), and that
the role includes the following policies.

If you do not specify an IAM role, then the action uses the default IAM role listed in
the [environment](deploy-environments.md "deploy-environments.md") in the CodeCatalyst console. If you use
the default role in the environment, make sure it has the following policies.

- The following permissions policy:

###### Warning

Limit the permissions to those shown in the following policy. Using a role
with broader permissions might pose a security risk.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:ListBucket",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket-name`",
 "arn:aws:s3:::`bucket-name`/*"
 ]
 }
 ]
}`

```

- The following custom trust policy:

###### Note

You can use the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role with this action, if you'd like. For more
 information about this role, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create"). Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName``
role has full access permissions which may pose a security risk. We recommend that you
only use this role in tutorials and scenarios where security is less of a concern.

Corresponding UI: One of the following depending on the action version:

- (Newer versions) Configuration tab/Environment/What's in
  `my-environment`?/three dot menu/**Switch
  role**
- (Older versions) Configuration
  tab/'Environment/account/role'/**Role**

## Configuration

(`S3Publish`/**Configuration**)

(Required)

A section where you can define the configuration properties of the action.

Corresponding UI: **Configuration** tab

## SourcePath

(`S3Publish`/Configuration/**SourcePath**)

(Required)

Specify the name and path of a directory or file that you want to publish to Amazon S3. The
directory or file can reside in a source repository or an artifact from a previous action, and
is relative to the source repository or artifact root.

Examples:

Specifying `./myFolder/` copies the contents of `/myFolder` to
Amazon S3, and preserves the underlying directory structure.

Specifying `./myFolder/myfile.txt` copies _just_ `myfile.txt` to Amazon S3. (The directory structure is removed.)

You cannot use wildcards.

###### Note

You may need to add a prefix to the directory or file path to indicate which artifact or
source to find it in. For more information, see [Referencing source repository
files](workflows-sources-reference-files.md "workflows-sources-reference-files.md") and [Referencing files in an
artifact](workflows-working-artifacts-refer-files.md "workflows-working-artifacts-refer-files.md").

Corresponding UI: Configuration tab/**Source path**

## DestinationBucketName

(`S3Publish`/Configuration/**DestinationBucketName**)

(Required)

Specify the name of the Amazon S3 bucket where you want to publish files.

Corresponding UI: Configuration tab/**Destination bucket -
optional**

## TargetPath

(`S3Publish`/Configuration/**TargetPath**)

(Optional)

Specify the name and path of the directory in Amazon S3 where you want to publish your files. If
the directory does not exist, it will be created. The directory path must not include
the bucket name.

Examples:

`myS3Folder`

`./myS3Folder/myS3Subfolder`

Corresponding UI: Configuration tab/**Destination directory -
optional**

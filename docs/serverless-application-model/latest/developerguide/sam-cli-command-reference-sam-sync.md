# sam sync

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam sync` command.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI, see [AWS SAM CLI](using-sam-cli.md "using-sam-cli.md").
  The `sam sync` command syncs local application changes to the AWS Cloud.

## Usage

```
`$` `sam sync `<options>``
```

## Options

`--base-dir, -s `DIRECTORY``

Resolves relative paths to the function's or layer's source code with respect to this directory. Use this option
to change how relative paths to source code folders are resolved. By default, relative paths are resolved with respect to the AWS SAM template's
location.

In addition to the resources in the root application or stack that you're building, this option also applies to
nested applications or stacks. Additionally, this option applies to the following resource types and
properties:

- Resource type: `AWS::Serverless::Function` Property:
  `CodeUri`
- Resource type: `AWS::Serverless::Function` Resource attribute:
  `Metadata` Entry: `DockerContext`
- Resource type: `AWS::Serverless::LayerVersion` Property:
  `ContentUri`
- Resource type: `AWS::Lambda::Function` Property:
  `Code`
- Resource type: `AWS::Lambda::LayerVersion` Property:
  `Content`

`--build-image `TEXT``

The URI for the [container image](serverless-image-repositories.md#serverless-image-repository-uris "serverless-image-repositories.md#serverless-image-repository-uris") that you want to use when
building your application. By default, AWS SAM uses the container image repository URI from [Amazon Elastic Container Registry (Amazon ECR) Public](../../../AmazonECR/latest/public/what-is-ecr.md "../../../AmazonECR/latest/public/what-is-ecr.md"). Specify this option to use a
different image.

You can use this option multiple times in a single command. Each option accepts a string or a key-value
pair.

- **String** – Specify the URI of the container image that all resources
  in your application will use. The following is an example:

```
`$` `sam sync --build-image `amazon/aws-sam-cli-build-image-python3.8``
```

- **Key-value pair** – Specify the resource name as the key and the
  container image URI to be used with that resource as the value. Use this format to specify a different
  container image URI for each resource in your application. The following is an example:

```
`$` `sam sync --build-image `Function1=amazon/aws-sam-cli-build-image-python3.8``
```

This option only applies if the `--use-container` option is specified, otherwise an error will
result.

`--build-in-source | --no-build-in-source`

Provides `--build-in-source` to build your project directly in the source folder.

The `--build-in-source` option supports the following runtimes and build methods:

- **Runtimes** – Any Node.js runtime supported by the
  `sam init --runtime` option.
- **Build methods** – `Makefile`, `esbuild`.

The `--build-in-source` option is not compatible with the following options:

- `--use-container`

_Default_: `--no-build-in-source`

`--capabilities `LIST``

A list of capabilities that you specify to allow AWS CloudFormation to create certain stacks. Some stack templates might
include resources that can affect permissions in your AWS account. For example, by creating new AWS Identity and Access Management (IAM)
users. Specify this option to override the default values. Valid values include the following:

- CAPABILITY_IAM
- CAPABILITY_NAMED_IAM
- CAPABILITY_RESOURCE_POLICY
- CAPABILITY_AUTO_EXPAND

_Default_: `CAPABILITY_NAMED_IAM` and `CAPABILITY_AUTO_EXPAND`

`--code`

By default, AWS SAM syncs all resources in your application. Specify this option to sync only code resources, which
include the following:

- `AWS::Serverless::Function`
- `AWS::Lambda::Function`
- `AWS::Serverless::LayerVersion`
- `AWS::Lambda::LayerVersion`
- `AWS::Serverless::Api`
- `AWS::ApiGateway::RestApi`
- `AWS::Serverless::HttpApi`
- `AWS::ApiGatewayV2::Api`
- `AWS::Serverless::StateMachine`
- `AWS::StepFunctions::StateMachine`

To sync code resources, AWS SAM uses AWS service APIs directly, instead of deploying through AWS CloudFormation. To
update your AWS CloudFormation stack, run **sam sync --watch** or **sam deploy**.

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration
file to use. The default value is "default". For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is "`samconfig.toml`" in the root of
the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--dependency-layer | --no-dependency-layer`

Specifies whether to separate dependencies of individual functions into another layer to speed up the sync
process.

_Default_: `--dependency-layer`

`--image-repository `TEXT``

The name of the Amazon Elastic Container Registry (Amazon ECR) repository where this command uploads your function's image. Required for
functions declared with the `Image` package type.

`--image-repositories `TEXT``

A mapping of functions to their Amazon ECR repository URI. Reference functions by their logical ID. The following
is an example:

```
`$` `sam sync --image-repositories `Function1=123456789012.dkr.ecr.us-east-1.amazonaws.com/my-repo``
```

You can specify this option multiple times in a single command.

`--kms-key-id `TEXT``

The ID of an AWS Key Management Service (AWS KMS) key used to encrypt artifacts that are at rest in the Amazon S3 bucket. If you don't
specify this option, then AWS SAM uses Amazon S3-managed encryption keys.

`--metadata`

A map of metadata to attach to all artifacts that you reference in your template.

`--notification-arns `LIST``

A list of Amazon Simple Notification Service (Amazon SNS) topic ARNs that AWS CloudFormation associates with the stack.

`--no-use-container`

An option that allows you to use the IDE toolkit to set default behavior.

`--parameter-overrides`

A string that contains AWS CloudFormation parameter overrides encoded as key-value pairs. Use
the same format as the AWS Command Line Interface (AWS CLI). The AWS SAM CLI format is explicit key and value keywords, each override is separated by a space. Here are two examples:

- `--parameter-overrides ParameterKey=hello,ParameterValue=world`
- `--parameter-overrides ParameterKey=hello,ParameterValue=world ParameterKey=example1,ParameterValue=example2 ParameterKey=apple,ParameterValue=banana`

`--resource `TEXT``

Specifies the resource type to sync. To sync multiple resources, you can specify this option multiple times.
This option is supported with the `--code` option. The value must be one of the listed resources under
`--code`. For example,
`--resource AWS::Serverless::Function --resource AWS::Serverless::LayerVersion`.

`--resource-id `TEXT``

Specifies the resource ID to sync. To sync multiple resources, you can specify this option multiple times. This
option is supported with the `--code` option. For example,
`--resource-id Function1 --resource-id Function2`.

`--role-arn `TEXT``

The Amazon Resource Name (ARN) of an IAM role that AWS CloudFormation assumes when applying the changeset.

``--s3-bucket `TEXT```

The name of the Amazon Simple Storage Service (Amazon S3) bucket where this command uploads your AWS CloudFormation template. If your template is
larger than 51,200 bytes, then either the `--s3-bucket` or the `--resolve-s3` option is
required. If you specify both the `--s3-bucket` and `--resolve-s3` options, then an
error occurs.

`--s3-prefix `TEXT``

The prefix added to the names of the artifacts that you upload to the Amazon S3 bucket. The prefix name is a path
name (folder name) for the Amazon S3 bucket. This applies only to functions declared with the `Zip` package
type.

`--save-params`

Saves the parameters that you provide at the command line to the AWS SAM configuration file.

`--skip-deploy-sync | --no-skip-deploy-sync`

Specifies `--skip-deploy-sync` to skip the initial infrastructure sync if it isn't required. The
AWS SAM CLI will compare your local AWS SAM template with the deployed AWS CloudFormation template and perform a deployment only if a
change is detected.

Specifies `--no-skip-deploy-sync` to perform an AWS CloudFormation deployment every time `sam sync` is
run.

To learn more, see [Skip the initial AWS CloudFormation deployment](using-sam-cli-sync.md#using-sam-cli-sync-options-skip-deploy-sync "using-sam-cli-sync.md#using-sam-cli-sync-options-skip-deploy-sync").

_Default_: `--skip-deploy-sync`

`--stack-name `TEXT``

The name of the AWS CloudFormation stack for your application.

This option is required.

`--tags `LIST``

A list of tags to associate with the stack that is created or updated. AWS CloudFormation also propagates these tags to
resources in the stack that support it.

`--template-file, --template, -t `PATH``

The path and file name where your AWS SAM template is located.

###### Note

If you specify this option, then AWS SAM deploys only the template and the local resources that it points
to.

`--use-container, -u`

If your functions depend on packages that have natively compiled dependencies, use this option to build your
function inside an AWS Lambda-like Docker container.

###### Note

Currently, this option is not compatible with `--dependency-layer`. If you use
`--use-container` with `--dependency-layer`, the AWS SAM CLI informs you and continues with
`--no-dependency-layer`.

`--watch`

Starts a process that watches your local application for changes and automatically syncs them to the AWS Cloud.
By default, when you specify this option, AWS SAM syncs all resources in your application as you update them. With this
option, AWS SAM performs an initial AWS CloudFormation deployment. Then, AWS SAM uses AWS service APIs to update code resources.
AWS SAM uses AWS CloudFormation to update infrastructure resources when you update your AWS SAM template.

`--watch-exclude `TEXT``

Excludes a file or folder from being observed for file changes. To use this option, `--watch` must also be provided.

This option receives a key-value pair:

- **Key** – The logical ID of a Lambda function in your application.
- **Value** – The associated file name or folder to exclude.

When you update any files or folders specified with the `--watch-exclude` option, the AWS SAM CLI will not initiate a sync. However, when an
update to other files or folders initiates a sync, these files or folders will be included in that sync.

You can provide this option multiple times in a single command.

## Examples

For examples on using this command, refer to [Options for the sam sync command](using-sam-cli-sync.md#using-sam-cli-sync-options "using-sam-cli-sync.md#using-sam-cli-sync-options").

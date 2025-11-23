# sam deploy

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam deploy` command.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI `sam deploy` command, see [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md "using-sam-cli-deploy.md").
  The `sam deploy` command deploys an application to the AWS Cloud using AWS CloudFormation.

## Usage

```
`$ `<environment variables>`` `sam deploy `<options>``
```

## Environment variables

`SAM_CLI_POLL_DELAY`

Set the `SAM_CLI_POLL_DELAY` environment variable with a value of seconds in your shell
to configure how often the AWS SAM CLI checks the CloudFormation stack state, which is useful when seeing throttling from CloudFormation.
This env variable is used for polling `describe_stack` API calls, which are made while running `sam deploy`.

The following is an example of this variable:

```
`$` `SAM_CLI_POLL_DELAY=`5` sam deploy`
```

## Options

`--capabilities `LIST``

A list of capabilities that you must specify to allow CloudFormation to create certain
stacks. Some stack templates might include resources that affect permissions in your
AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks,
you must explicitly acknowledge their capabilities by specifying this option. The only
valid values are `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`. If
you have IAM resources, then you can specify either capability. If you have IAM
resources with custom names, then you must specify `CAPABILITY_NAMED_IAM`. If
you don't specify this option, then the operation returns an
`InsufficientCapabilities` error.

When you deploy an application that contains nested applications, you must use `CAPABILITY_AUTO_EXPAND`
to acknowledge the application contains nested applications. For more information,
see [Deploying
nested applications](serverless-sam-template-nested-applications.md#serverless-sam-templates-nested-applications-deploying "serverless-sam-template-nested-applications.md#serverless-sam-templates-nested-applications-deploying").

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration
file to use. The default value is `default`. For more information about
configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is `samconfig.toml` in the root of
the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--confirm-changeset | --no-confirm-changeset`

Prompt to confirm whether the AWS SAM CLI deploys the computed changeset.

`--debug`

Turn on debug logging to print the debug message that the AWS SAM CLI generates and
to display timestamps.

`--disable-rollback | --no-disable-rollback`

Specify whether to roll back your CloudFormation stack if an error occurs during a
deployment. By default, if there's an error during a deployment, your CloudFormation stack rolls
back to the last stable state. If you specify `--disable-rollback` and an
error occurs during a deployment, then resources that were created or updated before the
error occurred aren't rolled back.

`--fail-on-empty-changeset | --no-fail-on-empty-changeset`

Specify whether to return a non-zero exit code if there are no changes to make to
the stack. The default behavior is to return a non-zero exit code.

`--force-upload`

Specify this option to upload artifacts even if they match existing artifacts in
the Amazon S3 bucket. Matching artifacts are overwritten.

`--guided, -g`

Specify this option to have the AWS SAM CLI use prompts to guide you through the
deployment.

`--help`

Show this message and exit.

`--image-repositories `TEXT``

A mapping of functions to their Amazon ECR repository URI. Reference functions by their logical ID. The following
is an example:

```
`$` `sam deploy --image-repositories `Function1=123456789012.dkr.ecr.us-east-1.amazonaws.com/my-repo``
```

You can specify this option multiple times in a single command.

`--image-repository `TEXT``

The name of the Amazon ECR repository where this command uploads your function's image.
This option is required for functions declared with the `Image` package
type.

`--kms-key-id `TEXT``

The ID of an AWS Key Management Service (AWS KMS) key used to encrypt artifacts that are at rest in
the Amazon S3 bucket. If you don't specify this option, then AWS SAM uses Amazon S3-managed
encryption keys.

`--metadata`

A map of metadata to attach to all artifacts that are referenced in your
template.

`--no-execute-changeset`

Indicates whether to apply the changeset. Specify this option if you want to view
your stack changes before applying the changeset. This command creates an CloudFormation
changeset and then exits without applying the changeset. To apply the changeset, run the
same command without this option.

`--no-progressbar`

Do not display a progress bar when uploading artifacts to Amazon S3.

`--notification-arns `LIST``

A list of Amazon Simple Notification Service (Amazon SNS) topic ARNs that CloudFormation associates with the
stack.

`--on-failure [ROLLBACK | DELETE | DO_NOTHING]`

Specify the action to take when a stack fails to create.

The following options are available:

- `ROLLBACK` – Rolls back the stack to a previous known
  good state.
- `DELETE` – Rolls back the stack to a previous known
  good state, if one exists. Otherwise, deletes the stack.
- `DO_NOTHING` – Neither rolls back nor deletes the
  stack. The effect is the same as that of `--disable-rollback`.

The default behavior is `ROLLBACK`.

###### Note

You can specify either the
`--disable-rollback` option or the `--on-failure` option, but
not both.

`--parameter-overrides `LIST``

A string that contains CloudFormation parameter overrides encoded as key-value pairs. Each override uses the format `ParameterKey=name,ParameterValue=value`. Multiple overrides are separated by spaces. Here are two examples:

```
`$` `sam deploy --parameter-overrides `ParameterKey=value1,ParameterValue=value2``
```

```
`$` `sam deploy --parameter-overrides `ParameterKey=value1,ParameterValue=value2 ParameterKey=hello,ParameterValue=world ParameterKey=apple,ParameterValue=banana``
```

`--profile `TEXT``

The specific profile from your credential file that gets AWS credentials.

`--region `TEXT``

The AWS Region to deploy to. For example, us-east-1.

`--resolve-image-repos`

Automatically create Amazon ECR repositories to use for packaging and deploying for
non-guided deployments. This option applies only to functions and layers with
`PackageType: Image` specified. If you specify the `--guided`
option, then the AWS SAM CLI ignores `--resolve-image-repos`.

###### Note

If AWS SAM automatically creates any Amazon ECR repositories for
functions or layers with this option, and you later delete those functions or layers
from your AWS SAM template, then the corresponding Amazon ECR repositories are automatically
deleted.

`--resolve-s3`

Automatically create an Amazon S3 bucket to use for packaging and deploying for
non-guided deployments. If you specify the `--guided` option, then the AWS SAM
CLI ignores `--resolve-s3`. If you specify both the `--s3-bucket`
and `--resolve-s3` options, then an error occurs.

`--role-arn `TEXT``

The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when applying
the changeset.

`--s3-bucket `TEXT``

The name of the Amazon S3 bucket where this command uploads your CloudFormation template. If your
template is larger than 51,200 bytes, then either the `--s3-bucket` option or
the `--resolve-s3` option is required. If you specify both the
`--s3-bucket` and `--resolve-s3` options, then an error
occurs.

`--s3-prefix `TEXT``

The prefix added to the names of the artifacts that are uploaded to the Amazon S3
bucket. The prefix name is a path name (folder name) for the Amazon S3 bucket.

`--save-params`

Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--signing-profiles `LIST``

The list of signing profiles to sign your deployment packages with. This option
takes a list of key-value pairs, where the key is the name of the function or layer to
sign, and the value is the signing profile, with an optional profile owner delimited
with `:`. For example, `FunctionNameToSign=SigningProfileName1
 LayerNameToSign=SigningProfileName2:SigningProfileOwner`.

`--stack-name `TEXT``

(Required) The name of the CloudFormation stack that you're deploying to. If you specify an
existing stack, then the command updates the stack. If you specify a new stack, then the
command creates it.

`--tags `LIST``

A list of tags to associate with the stack that is created or updated. CloudFormation also
propagates these tags to resources in the stack that support it.

`--template-file, --template, -t `PATH``

The path and file name where your AWS SAM template is located.

###### Note

If you specify this option, then AWS SAM deploys only the
template and the local resources that it points to.

`--use-json`

Output JSON for the CloudFormation template. The default output is YAML.

## Example

For a detailed example and in-depth walkthrough on using the `sam deploy` subcommand, refer to [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md "using-sam-cli-deploy.md").

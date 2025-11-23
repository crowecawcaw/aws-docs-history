# sam build

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam build` command.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI `sam build` command, see [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md").
  The `sam build` command prepares an application for subsequent steps in the developer workflow, such as
  local testing or deploying to the AWS Cloud.

## Usage

```
`$` `sam build `<arguments>` `<options>``
```

## Arguments

**Resource ID**

Optional. Instructs AWS SAM to build a single resource declared in an [AWS SAM
template](what-is-sam-overview.md#what-is-sam-template "what-is-sam-overview.md#what-is-sam-template"). The build artifacts for the specified resource will be the only ones available
for subsequent commands in the workflow, i.e. `sam package` and `sam
 deploy`.

## Options

`--base-dir, -s `DIRECTORY``

Resolves relative paths to the function's or layer's source code with respect to
this directory. Use this option if you want to change how relative paths to source code
folders are resolved. By default, relative paths are resolved with respect to the AWS SAM
template's location.

In addition to the resources in the root application or stack
you are building, this option also applies nested applications or
stacks.

This option applies to the following resource types and
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

`--beta-features | --no-beta-features`

Allow or deny beta features.

`--build-dir, -b `DIRECTORY``

The path to a directory where the built artifacts are stored. This directory and
all of its content are removed with this option.

`--build-image `TEXT``

The URI of the container image that you want to pull for the build. By default,
AWS SAM pulls the container image from Amazon ECR Public. Use this option to pull the image
from another location.

You can specify this option multiple times. Each instance of this option can take
either a string or a key-value pair. If you specify a string, it is the URI of the
container image to use for all resources in your application. For example, `sam
 build --use-container --build-image amazon/aws-sam-cli-build-image-python3.8`.
If you specify a key-value pair, the key is the resource name, and the value is the
URI of the container image to use for that resource. For example `sam build
 --use-container --build-image
 Function1=amazon/aws-sam-cli-build-image-python3.8`. With key-value pairs, you
can specify different container images for different resources.

This option only applies if the `--use-container` option is specified,
otherwise an error will result.

`--build-in-source | --no-build-in-source`

Provide `--build-in-source` to build your project directly in the source folder.

The `--build-in-source` option supports the following runtimes and build methods:

- **Runtimes** – Any Node.js runtime supported by the
  `sam init --runtime` option.
- **Build methods** – `Makefile`, `esbuild`.

The `--build-in-source` option is not compatible with the following options:

- `--hook-name`
- `--use-container`

_Default_: `--no-build-in-source`

`--cached | --no-cached`

Enable or disable cached builds. Use this option to reuse build artifacts that
haven't changed from previous builds. AWS SAM evaluates whether you've changed any files
in your project directory. By default, builds are not cached. If the
`--no-cached` option is invoked, it overrides the `cached =
 true` setting in samconfig.toml.

###### Note

AWS SAM
doesn't evaluate whether you've changed third-party modules that your project depends
on, where you haven't provided a specific version. For example, if your Python function
includes a `requirements.txt` file with the entry
`requests=1.x`, and the latest request module version changes from
`1.1` to `1.2`, then AWS SAM doesn't pull the latest version until
you run a non-cached build.

`--cache-dir`

The directory where the cache artifacts are stored when `--cached` is
specified. The default cache directory is `.aws-sam/cache`.

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration
file to use. The default value is "default". For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is "`samconfig.toml`" in the root of
the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--container-env-var, -e `TEXT``

Environment variables to pass to the build container. You can specify this option
multiple times. Each instance of this option takes a key-value pair, where the key is
the resource and environment variable, and the value is the environment variable's
value. For example: `--container-env-var Function1.GITHUB_TOKEN=TOKEN1
 --container-env-var Function2.GITHUB_TOKEN=TOKEN2`.

This option only
applies if the `--use-container` option is specified, otherwise an error
will result.

`--container-env-var-file, -ef `PATH``

The path and file name of a JSON file that contains values for the container's
environment variables. For more information about container environment variable files,
see [Container environment
variable file](serverless-sam-cli-using-build.md#serverless-sam-cli-using-container-environment-file "serverless-sam-cli-using-build.md#serverless-sam-cli-using-container-environment-file").

This
option only applies if the `--use-container` option is specified, otherwise
an error will result.

`--debug`

Turns on debug logging to print debug messages that the AWS SAM CLI generates, and to
display timestamps.

`--docker-network `TEXT``

Specifies the name or ID of an existing Docker network that Lambda Docker containers
should connect to, along with the default bridge network. If not specified, the Lambda
containers connect only to the default bridge Docker network.

`--exclude, -x`

The Name of the resource(s) to exclude from the `sam build`. For example, if your
template contains `Function1`, `Function2`, and
`Function3` and you run `sam build --exclude Function2`, only
`Function1` and `Function3` will be built.

`--help`

Shows this message and exits.

`--hook-name `TEXT``

The name of the hook that is used to extend AWS SAM CLI functionality.

Accepted values: `terraform`.

`--manifest , -m `PATH``

The path to a custom dependency manifest file (for example, package.json) to use
instead of the default.

`--mount-symlinks`

Ensures the AWS SAM CLI always mounts symlinks that are present in the files to build or invoke. This applies only to symlinks on the top level directory (that is, symlinks that are directly on the function's root).
By default, symlinks are not mounted except for those needed to use `build-in-source` for `node_modules` in NodeJS.

`--no-use-container`

An option that allows you to use the IDE toolkit to set default behavior. You can also use
`sam build --no-use-container` to run a build in your local machine instead of a docker container.

`--parallel`

Enables parallel builds. Use this option to build your AWS SAM template's functions
and layers in parallel. By default, the functions and layers are built in
sequence.

`--parameter-overrides`

(Optional) A string that contains CloudFormation parameter overrides encoded as key-value
pairs. Uses the same format as the AWS Command Line Interface (AWS CLI). For example:
'`ParameterKey`=`KeyPairName`,
`ParameterValue`=`MyKey`
`ParameterKey`=`InstanceType`,
`ParameterValue`=`t1.micro`'. This option is not compatible with
`--hook-name`.

`--profile `TEXT``

The specific profile from your credential file that gets AWS credentials.

`--region `TEXT``

The AWS Region to deploy to. For example, us-east-1.

`--save-params`

Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--skip-prepare-infra`

Skips the preparation stage if no infrastructure changes have been made. Use with the `--hook-name` option.

`--skip-pull-image`

Specifies whether the command should skip pulling down the latest Docker image for
the Lambda runtime.

`--template-file, --template, -t `PATH``

The path and file name of AWS SAM template file `[default:
 template.[yaml|yml]]`. This option is not compatible with
`--hook-name`.

`--terraform-project-root-path`

The relative or absolute path to the top-level directory containing your Terraform configuration files or function source code.
If these files are located outside of the directory containing your Terraform root module, use this option to specify its absolute or relative path.
This option requires that `--hook-name` be set to `terraform`.

`--use-container`, `-u`

If your functions depend on packages that have natively compiled dependencies, use
this option to build your function inside a Lambda-like Docker container.

## Example

For a detailed example and in-depth walkthrough on using the `sam build` subcommand, refer to [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md").

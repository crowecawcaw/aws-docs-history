# sam init

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam init` command.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI `sam init` command, see [Create your application in AWS SAM](using-sam-cli-init.md "using-sam-cli-init.md").
  The `sam init` command provides options to initialize a new serverless application.

## Usage

```
`$` `sam init `<options>``
```

## Options

`--app-template `TEXT``

The identifier of the managed application template that you want to use. If you're
not sure, call `sam init` without options for an interactive
workflow.

This parameter is required if `--no-interactive` is specified and
`--location` is not provided.

This parameter is available only in AWS SAM CLI version 0.30.0 and later. Specifying
this parameter with an earlier version results in an error.

`--application-insights | --no-application-insights`

Activate Amazon CloudWatch Application Insights monitoring for your application. To learn more, see
[Using CloudWatch Application Insights to monitor your AWS SAM serverless applications](monitor-app-insights.md "monitor-app-insights.md").

The default option is `--no-application-insights`.

`--architecture, -a `[ x86_64 | arm64 ]``

The instruction set architecture for your application's Lambda functions. Specify
one of `x86_64` or `arm64`.

`--base-image `[ amazon/dotnet8-base | amazon/dotnet6-base |
amazon/java21-base | amazon/java17-base | amazon/java11-base |
amazon/nodejs22.x-base | amazon/nodejs20.x-base | amazon/nodejs18.x-base
| amazon/nodejs16.x-base | amazon/python3.13-base |
amazon/python3.12-base | amazon/python3.11-base | amazon/python3.10-base
| amazon/python3.9-base | amazon/python3.8-base | amazon/ruby3.4-base |
amazon/ruby3.3-base | amazon/ruby3.2-base ]``

The base image of your application. This option applies only when the package type
is `Image`.

This parameter is required if `--no-interactive` is specified,
`--package-type` is specified as `Image`, and
`--location` is not specified.

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration
file to use. The default value is "default". For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is "samconfig.toml" in the root of the project
directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--debug`

Turns on debug logging to print debug messages that the AWS SAM CLI generates, and to
display timestamps.

`--dependency-manager, -d `[ gradle | mod | maven | bundler | npm | cli-package
| pip ]``

The dependency manager of your Lambda runtime.

`--extra-content`

Override any custom parameters in the template's `cookiecutter.json`
configuration, for example, `{"customParam1": "customValue1",
 "customParam2":"customValue2"}`.

`--help, -h`

Shows this message and exits.

`--location, -l `TEXT``

The template or application location (Git, Mercurial, HTTP/HTTPS, .zip file,
path).

This parameter is required if `--no-interactive` is specified and
`--runtime`, `--name`, and `--app-template` are not
provided.

For Git repositories, you must use the location of the root of the
repository.

For local paths, the template must be in either .zip file or [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html "https://cookiecutter.readthedocs.io/en/latest/README.html")
format.

`--name, -n `TEXT``

The name of your project to be generated as a directory.

This parameter is required if `--no-interactive` is specified and
`--location` is not provided.

`--no-input`

Disables Cookiecutter prompting and accepts the vcfdefault values that are defined
in the template configuration.

`--no-interactive`

Disable interactive prompting for init parameters, and fail if any required values
are missing.

`--output-dir, -o `PATH``

The location where the initialized application is output.

`--package-type `[ Zip | Image ]``

The package type of the example application. `Zip` creates a .zip file
archive, and `Image` creates a container image.

`--runtime, -r `[ dotnet8 | dotnet6 | java21 | java17 | java11 |
nodejs22.x | nodejs20.x | nodejs18.x | nodejs16.x | python3.13 |
python3.12 | python3.11 | python3.10 | python3.9 | python3.8 | ruby3.4 |
ruby3.3 | ruby3.2 ]``

The Lambda runtime of your application. This option applies only when the package
type is `Zip`.

This parameter is required if `--no-interactive` is specified,
`--package-type` is specified as `Zip`, and
`--location` is not specified.

`--save-params`

Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--tracing | --no-tracing`

Activate AWS X-Ray tracing for your Lambda functions.

## Example

For a detailed example and in-depth walkthrough on using the `sam init` subcommand, refer to [Create your application in AWS SAM](using-sam-cli-init.md "using-sam-cli-init.md").

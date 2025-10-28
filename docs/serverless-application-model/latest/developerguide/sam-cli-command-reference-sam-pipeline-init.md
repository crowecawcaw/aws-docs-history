# sam pipeline init

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam pipeline init` subcommand.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")

The `sam pipeline init` subcommand generates a pipeline configuration file that your CI/CD system can use to deploy
serverless applications using AWS SAM.

Before using **sam pipeline init**, you must bootstrap the necessary resources
for each stage in your pipeline. You can do this by running **sam pipeline init --bootstrap** to be guided through the setup and configuration file generation process,
or refer to resources you have previously created with the **sam pipeline bootstrap** command.

## Usage

```
`$` `sam pipeline init `<options>``
```

## Options

`--bootstrap`

Enable interactive mode that walks the user through creating necessary AWS infrastructure
resources.

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration file
to use. The default value is `default`. For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `TEXT``

The path and file name of the configuration file containing default parameter values to
use. The default value is `samconfig.toml` in the project root directory. For more
information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--debug`

Turns on debug logging to print debug messages that the AWS SAM CLI generates, and to
display timestamps.

`--help, -h`

Shows this message and exits.

`--save-params`

Save the parameters that you provide at the command line to the AWS SAM configuration file.

## Example

The following example shows you how to use the `--bootstrap` option to allow you to walkthrough an interactive mode that walks you through creating necessary AWS infrastructure resources:

```
`$` `sam pipeline init --bootstrap`
```

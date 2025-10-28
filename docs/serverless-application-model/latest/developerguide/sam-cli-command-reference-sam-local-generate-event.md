# sam local

generate-event

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local generate-event` subcommand.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI `sam local generate-event` command, see [Introduction to testing with sam local generate-event](using-sam-cli-local-generate-event.md "using-sam-cli-local-generate-event.md").
  The `sam local generate-event` subcommand generates event payload samples for supported AWS services.

## Usage

```
`$` `sam local generate-event `<options> <service> <event> <event-options>``
```

## Options

`--config-env TEXT`

The environment name specifying the default parameter values in the configuration
file to use. The default value is "default". For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is `samconfig.toml` in the root of the project
directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--help`

Shows this message and exits.

## Service

To see a list of supported services, run the following:

```
`$` `sam local generate-event`
```

## Event

To see a list of supported events that can be generated for each service, run the following:

```
`$` `sam local generate-event `<service>``
```

## Event options

To see a list of supported event options that you can modify, run the following:

```
`$` `sam local generate-event `<service> <event>` --help`
```

## Examples

For examples on using the `sam local generate-event` subcommand, refer to [Generate sample events](using-sam-cli-local-generate-event.md#using-sam-cli-local-generate-event-generate "using-sam-cli-local-generate-event.md#using-sam-cli-local-generate-event-generate").

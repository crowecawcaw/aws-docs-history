# sam remote test-event put

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote test-event put` subcommand.

- For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")
- For documentation on using the AWS SAM CLI `sam remote test-event` command, see
  [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md "using-sam-cli-remote-test-event.md").
  The `sam remote test-event put` subcommand saves a shareable test event from your local machine to the Amazon EventBridge schema registry.

## Usage

```
`$` `sam remote test-event put `<arguments> <options>``
```

## Arguments

**Resource ID**

The ID of the AWS Lambda function associated with the shareable test event.

If you provide a logical ID, you must also provide a value for the AWS CloudFormation stack associated with the Lambda function using the `--stack-name` option.

_Valid values_: The resource's logical ID or resource ARN.

## Options

`--config-env `TEXT``

The environment name specifying the default parameter values in the configuration
file to use. The default value is "default". For more information about configuration
files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--config-file `PATH``

The path and file name of the configuration file containing default parameter
values to use. The default value is "`samconfig.toml`" in the root of
the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md "serverless-sam-cli-config.md").

`--file `FILENAME``

The file path and name to the event to on your local machine.

Provide `-` as the file name value to read from `stdin`.

This option is required.

`--force`, `-f`

Overwrite a shareable test event with the same name.

`--help, -h`

Show the help message and exit.

`--name `TEXT``

The name to save the shareable test event as.

If a shareable test event with the same name exists in the EventBridge schema registry, the AWS SAM CLI will not overwrite it. To overwrite, add the
`--force` option.

`--output-file `FILENAME``

The file path and name to save the event to on your local machine.

If you don’t provide this option, the AWS SAM CLI will output the contents of the shareable test event to your console.

`--stack-name `TEXT``

The name of the AWS CloudFormation stack associated with the Lambda function.

This option is required if you are providing the Lambda function logical ID as an argument.

## Example

For an example on using this command, refer to [Saving shareable test events](using-sam-cli-remote-test-event.md#using-sam-cli-remote-test-event-use-put "using-sam-cli-remote-test-event.md#using-sam-cli-remote-test-event-use-put").

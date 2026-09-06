

# sam remote test-event delete
<a name="sam-cli-command-reference-remote-test-event-delete"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam remote test-event delete` subcommand.
+ For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)
+ For documentation on using the AWS SAM CLI `sam remote test-event` command, see [Introduction to cloud testing with sam remote test-event](using-sam-cli-remote-test-event.md).

The `sam remote test-event delete` subcommand deletes a shareable test event from the Amazon EventBridge schema registry.

## Usage
<a name="sam-cli-command-reference-remote-test-event-delete-usage"></a>

```
$ sam remote test-event delete {{<arguments> <options>}}
```

## Arguments
<a name="sam-cli-command-reference-remote-test-event-delete-args"></a>

**Resource ID**  <a name="sam-cli-command-reference-remote-test-event-delete-args-resource-id"></a>
The ID of the AWS Lambda function associated with the shareable test event.  
If you provide a logical ID, you must also provide a value for the AWS CloudFormation stack associated with the Lambda function using the `--stack-name` option.  
*Valid values*: The resource's logical ID or resource ARN.

## Options
<a name="sam-cli-command-reference-remote-test-event-delete-options"></a>

`--config-env {{TEXT}}`  <a name="sam-cli-command-reference-remote-test-event-delete-options-config-env"></a>
The environment name specifying the default parameter values in the configuration file to use. The default value is "default". For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="sam-cli-command-reference-remote-test-event-delete-options-config-file"></a>
The path and file name of the configuration file containing default parameter values to use. The default value is "`samconfig.toml`" in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--help, -h`  <a name="sam-cli-command-reference-remote-test-event-delete-options-help"></a>
Show the help message and exit.

`--name {{TEXT}}`  <a name="sam-cli-command-reference-remote-test-event-delete-options-name"></a>
The name of the shareable test event to delete.

`--stack-name {{TEXT}}`  <a name="sam-cli-command-reference-remote-test-event-delete-options-stack-name"></a>
The name of the CloudFormation stack associated with the Lambda function.  
This option is required if you are providing the Lambda function logical ID as an argument.
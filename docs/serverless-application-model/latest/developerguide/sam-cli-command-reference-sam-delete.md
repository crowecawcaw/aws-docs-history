

# sam delete
<a name="sam-cli-command-reference-sam-delete"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam delete` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam delete` command deletes an AWS SAM application by deleting the CloudFormation stack, the artifacts that were packaged and deployed to Amazon S3 and Amazon ECR, and the AWS SAM template file.

This command also checks whether there is an Amazon ECR companion stack deployed, and if so prompts the user about deleting that stack and Amazon ECR repositories. If `--no-prompts` is specified, then companion stacks and Amazon ECR repositories are deleted by default.

## Usage
<a name="sam-cli-command-reference-sam-delete-usage"></a>

```
$ sam delete {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-delete-options"></a>

`--config-env {{TEXT}}`  <a name="sam-cli-command-reference-sam-delete-options-config-env"></a>
The environment name specifying the default parameter values in the configuration file to use. The default value is `default`. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="sam-cli-command-reference-sam-delete-options-config-file"></a>
The path and file name of the configuration file containing default parameter values to use. The default value is `samconfig.toml` in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--debug`  <a name="sam-cli-command-reference-sam-delete-options-debug"></a>
Turns on debug logging to print the debug message that the AWS SAM CLI generates and to display timestamps.

`--help`  <a name="sam-cli-command-reference-sam-delete-options-help"></a>
Shows this message and exits.

`--no-prompts`  <a name="sam-cli-command-reference-sam-delete-options-no-prompts"></a>
Specify this option to have AWS SAM operate in non-interactive mode. The stack name must be provided, either with the `--stack-name` option, or in the configuration `toml` file.

`--profile {{TEXT}}`  <a name="sam-cli-command-reference-sam-delete-options-profile"></a>
The specific profile from your credential file that gets AWS credentials.

`--region {{TEXT}}`  <a name="sam-cli-command-reference-sam-delete-options-region"></a>
The AWS Region to deploy to. For example, us-east-1.

`--s3-bucket`  <a name="sam-cli-command-reference-sam-delete-options-s3-bucket"></a>
The path of the Amazon S3 bucket you want to delete.

`--s3-prefix`  <a name="sam-cli-command-reference-sam-delete-options-s3-prefix"></a>
The prefix of the Amazon S3 bucket you want to delete.

`--save-params`  <a name="sam-cli-command-reference-sam-delete-options-save-params"></a>
Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--stack-name {{TEXT}}`  <a name="sam-cli-command-reference-sam-delete-options-stack-name"></a>
The name of the CloudFormation stack that you want to delete.

## Examples
<a name="sam-cli-command-reference-sam-delete-examples"></a>

The following command deletes the stack `MY-STACK`. 

```
$ sam delete --stack-name MY-STACK
```

The following command deletes the stack `MY-STACK` and the S3 bucket `sam-s3-demo-bucket`:

```
$ sam delete \
    --stack-name MyStack \
    --s3-bucket MySAMBucket
```
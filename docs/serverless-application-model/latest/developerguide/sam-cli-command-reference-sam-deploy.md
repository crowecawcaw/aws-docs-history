

# sam deploy
<a name="sam-cli-command-reference-sam-deploy"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam deploy` command.
+ For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)
+ For documentation on using the AWS SAM CLI `sam deploy` command, see [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md).

The `sam deploy` command deploys an application to the AWS Cloud using AWS CloudFormation.

## Usage
<a name="ref-sam-cli-deploy-usage"></a>

```
$ {{<environment variables>}} sam deploy {{<options>}}
```

## Environment variables
<a name="ref-sam-cli-deploy-env"></a>

`SAM_CLI_POLL_DELAY`  <a name="ref-sam-cli-deploy-env-sam-cli-poll-delay"></a>
Set the `SAM_CLI_POLL_DELAY` environment variable with a value of seconds in your shell to configure how often the AWS SAM CLI checks the CloudFormation stack state, which is useful when seeing throttling from CloudFormation. This env variable is used for polling `describe_stack` API calls, which are made while running `sam deploy`.   
The following is an example of this variable:  

```
$ SAM_CLI_POLL_DELAY={{5}} sam deploy
```

## Options
<a name="ref-sam-cli-deploy-options"></a>

`--capabilities {{LIST}}`  <a name="ref-sam-cli-deploy-options-capabilities"></a>
A list of capabilities that you must specify to allow CloudFormation to create certain stacks. Some stack templates might include resources that affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge their capabilities by specifying this option. The only valid values are `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`. If you have IAM resources, then you can specify either capability. If you have IAM resources with custom names, then you must specify `CAPABILITY_NAMED_IAM`. If you don't specify this option, then the operation returns an `InsufficientCapabilities` error.  
When you deploy an application that contains nested applications, you must use `CAPABILITY_AUTO_EXPAND` to acknowledge the application contains nested applications. For more information, see [Deploying nested applications](serverless-sam-template-nested-applications.md#serverless-sam-templates-nested-applications-deploying).

`--config-env {{TEXT}}`  <a name="ref-sam-cli-deploy-options-config-env"></a>
The environment name specifying the default parameter values in the configuration file to use. The default value is `default`. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="ref-sam-cli-deploy-options-config-file"></a>
The path and file name of the configuration file containing default parameter values to use. The default value is `samconfig.toml` in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--confirm-changeset | --no-confirm-changeset`  <a name="ref-sam-cli-deploy-options-confirm-changeset"></a>
Prompt to confirm whether the AWS SAM CLI deploys the computed changeset.

`--debug`  <a name="ref-sam-cli-deploy-options-debug"></a>
Turn on debug logging to print the debug message that the AWS SAM CLI generates and to display timestamps.

`--disable-rollback | --no-disable-rollback`  <a name="ref-sam-cli-deploy-options-disable-rollback"></a>
Specify whether to roll back your CloudFormation stack if an error occurs during a deployment. By default, if there's an error during a deployment, your CloudFormation stack rolls back to the last stable state. If you specify `--disable-rollback` and an error occurs during a deployment, then resources that were created or updated before the error occurred aren't rolled back.

`--express | --no-express`  <a name="ref-sam-cli-deploy-options-express"></a>
Specifies whether to use CloudFormation Express mode. When active, stack operations complete once resource configuration is applied. Resources continue becoming ready in the background. Deployment time can be reduced by up to 4x.  
The AWS SAM CLI passes the rollback behavior to the CloudFormation `DeploymentConfig` parameter when you also specify `--disable-rollback`.  
The default value is `--no-express`.

`--fail-on-empty-changeset | --no-fail-on-empty-changeset`  <a name="ref-sam-cli-deploy-options-fail-on-empty-changeset"></a>
Specify whether to return a non-zero exit code if there are no changes to make to the stack. The default behavior is to return a non-zero exit code.

`--force-upload`  <a name="ref-sam-cli-deploy-options-force-upload"></a>
Specify this option to upload artifacts even if they match existing artifacts in the Amazon S3 bucket. Matching artifacts are overwritten.

`--guided, -g`  <a name="ref-sam-cli-deploy-options-guided"></a>
Specify this option to have the AWS SAM CLI use prompts to guide you through the deployment.

`--help`  <a name="ref-sam-cli-deploy-options-help"></a>
Show this message and exit.

`--image-repositories {{TEXT}}`  <a name="ref-sam-cli-deploy-options-image-repositories"></a>
A mapping of functions to their Amazon ECR repository URI. Reference functions by their logical ID. The following is an example:  

```
$ sam deploy --image-repositories {{Function1=123456789012.dkr.ecr.us-east-1.amazonaws.com/my-repo}}
```
You can specify this option multiple times in a single command.

`--image-repository {{TEXT}}`  <a name="ref-sam-cli-deploy-options-image-repository"></a>
The name of the Amazon ECR repository where this command uploads your function's image. This option is required for functions declared with the `Image` package type.

`--kms-key-id {{TEXT}}`  <a name="ref-sam-cli-deploy-options-kms-key-id"></a>
The ID of an AWS Key Management Service (AWS KMS) key used to encrypt artifacts that are at rest in the Amazon S3 bucket. If you don't specify this option, then AWS SAM uses Amazon S3-managed encryption keys.

`--metadata`  <a name="ref-sam-cli-deploy-options-metadata"></a>
A map of metadata to attach to all artifacts that are referenced in your template.

`--no-execute-changeset`  <a name="ref-sam-cli-deploy-options-no-execute-changeset"></a>
Indicates whether to apply the changeset. Specify this option if you want to view your stack changes before applying the changeset. This command creates an CloudFormation changeset and then exits without applying the changeset. To apply the changeset, run the same command without this option.

`--no-progressbar`  <a name="ref-sam-cli-deploy-options-no-progressbar"></a>
Do not display a progress bar when uploading artifacts to Amazon S3.

`--notification-arns {{LIST}}`  <a name="ref-sam-cli-deploy-options-notification-arns"></a>
A list of Amazon Simple Notification Service (Amazon SNS) topic ARNs that CloudFormation associates with the stack.

`--on-failure [ROLLBACK | DELETE | DO_NOTHING]`  <a name="ref-sam-cli-deploy-options-on-failure"></a>
Specify the action to take when a stack fails to create.  
The following options are available:  
+ `ROLLBACK` – Rolls back the stack to a previous known good state.
+ `DELETE` – Rolls back the stack to a previous known good state, if one exists. Otherwise, deletes the stack.
+ `DO_NOTHING` – Neither rolls back nor deletes the stack. The effect is the same as that of `--disable-rollback`.
The default behavior is `ROLLBACK`.  
You can specify either the `--disable-rollback` option or the `--on-failure` option, but not both.

`--output {{[ text | json ]}}`  <a name="ref-sam-cli-deploy-options-output"></a>
The format of the command output:  
+ `text` – Prints regular, human-readable output. This is the default value.
+ `json` – Prints structured, machine-readable output. Use this format when you want to consume the output programmatically, such as in CI/CD pipelines, IDE extensions, and AI-assisted tools.
A deployment runs over a period of time. When you specify `--output json`, the AWS SAM CLI prints a stream of JSON objects, one per line, as the deployment progresses. Each object includes a `type` field that identifies the kind of information it contains, such as the changeset, deployment events, stack outputs, and the final result. On failure, the final object includes an `error` object that describes what went wrong.  
The `--output json` option isn't compatible with options that require interactive prompts, such as `--guided` and `--confirm-changeset`.

`--parameter-overrides {{LIST}}`  <a name="ref-sam-cli-deploy-options-parameter-overrides"></a>
A string that contains CloudFormation parameter overrides encoded as key-value pairs. Each override uses the format `ParameterKey=name,ParameterValue=value`. Multiple overrides are separated by spaces. Here are two examples:  

```
$ sam deploy --parameter-overrides {{ParameterKey=value1,ParameterValue=value2}}
```

```
$ sam deploy --parameter-overrides {{ParameterKey=value1,ParameterValue=value2 ParameterKey=hello,ParameterValue=world ParameterKey=apple,ParameterValue=banana}}
```

`--profile {{TEXT}}`  <a name="ref-sam-cli-deploy-options-profile"></a>
The specific profile from your credential file that gets AWS credentials.

`--region {{TEXT}}`  <a name="ref-sam-cli-deploy-options-region"></a>
The AWS Region to deploy to. For example, us-east-1.

`--resolve-image-repos`  <a name="ref-sam-cli-deploy-options-resolve-image-repos"></a>
Automatically create Amazon ECR repositories to use for packaging and deploying for non-guided deployments. This option applies only to functions and layers with `PackageType: Image` specified. If you specify the `--guided` option, then the AWS SAM CLI ignores `--resolve-image-repos`.  
If AWS SAM automatically creates any Amazon ECR repositories for functions or layers with this option, and you later delete those functions or layers from your AWS SAM template, then the corresponding Amazon ECR repositories are automatically deleted.

`--resolve-s3`  <a name="ref-sam-cli-deploy-options-resolve-s3"></a>
Automatically create an Amazon S3 bucket to use for packaging and deploying for non-guided deployments. If you specify the `--guided` option, then the AWS SAM CLI ignores `--resolve-s3`. If you specify both the `--s3-bucket` and `--resolve-s3` options, then an error occurs.

`--role-arn {{TEXT}}`  <a name="ref-sam-cli-deploy-options-role-arn"></a>
The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when applying the changeset.

`--s3-bucket {{TEXT}}`  <a name="ref-sam-cli-deploy-options-s3-bucket"></a>
The name of the Amazon S3 bucket where this command uploads your CloudFormation template. If your template is larger than 51,200 bytes, then either the `--s3-bucket` option or the `--resolve-s3` option is required. If you specify both the `--s3-bucket` and `--resolve-s3` options, then an error occurs.

`--s3-prefix {{TEXT}}`  <a name="ref-sam-cli-deploy-options-s3-prefix"></a>
The prefix added to the names of the artifacts that are uploaded to the Amazon S3 bucket. The prefix name is a path name (folder name) for the Amazon S3 bucket.

`--save-params`  <a name="ref-sam-cli-deploy-options-save-params"></a>
Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--signing-profiles {{LIST}}`  <a name="ref-sam-cli-deploy-options-signing-profiles"></a>
The list of signing profiles to sign your deployment packages with. This option takes a list of key-value pairs, where the key is the name of the function or layer to sign, and the value is the signing profile, with an optional profile owner delimited with `:`. For example, `FunctionNameToSign=SigningProfileName1 LayerNameToSign=SigningProfileName2:SigningProfileOwner`.

`--stack-name {{TEXT}}`  <a name="ref-sam-cli-deploy-options-stack-name"></a>
(Required) The name of the CloudFormation stack that you're deploying to. If you specify an existing stack, then the command updates the stack. If you specify a new stack, then the command creates it.

`--tags {{LIST}}`  <a name="ref-sam-cli-deploy-options-tags"></a>
A list of tags to associate with the stack that is created or updated. CloudFormation also propagates these tags to resources in the stack that support it.

`--template-file, --template, -t {{PATH}}`  <a name="ref-sam-cli-deploy-options-template-file"></a>
The path and file name where your AWS SAM template is located.  
If you specify this option, then AWS SAM deploys only the template and the local resources that it points to.

`--use-json`  <a name="ref-sam-cli-deploy-options-use-json"></a>
Output JSON for the CloudFormation template. The default output is YAML.

## Example
<a name="sam-cli-command-reference-sam-deploy-examples"></a>

For a detailed example and in-depth walkthrough on using the `sam deploy` subcommand, refer to [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md).
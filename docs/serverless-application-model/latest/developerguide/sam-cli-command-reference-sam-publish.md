

# sam publish
<a name="sam-cli-command-reference-sam-publish"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam publish` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam publish` command publishes an AWS SAM application to the AWS Serverless Application Repository. This command takes a packaged AWS SAM template and publishes the application to the specified AWS Region.

The `sam publish` command expects the AWS SAM template to include a `Metadata` section that contains application metadata required for publishing. In the `Metadata` section, the `LicenseUrl` and `ReadmeUrl` properties must refer to Amazon Simple Storage Service (Amazon S3) buckets, not local files. For more information about the `Metadata` section of the AWS SAM template, see [Publishing your application with the AWS SAM CLI](serverless-sam-template-publishing-applications.md).

By default, `sam publish` creates the application as private. Before other AWS accounts are allowed to view and deploy your application, you must share it. For information on sharing applications, see [AWS Serverless Application Repository Resource-Based Policy Examples](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/security_iam_resource-based-policy-examples.html) in the *AWS Serverless Application Repository Developer Guide*.

**Note**  
Currently `sam publish` doesn't support publishing nested applications that are specified locally. If your application contains nested applications, you must publish them separately to the AWS Serverless Application Repository before publishing your parent application.

## Usage
<a name="sam-cli-command-reference-sam-publish-usage"></a>

```
$ sam publish {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-publish-options"></a>

`--config-env {{TEXT}}`  <a name="sam-cli-command-reference-sam-publish-options-config-env"></a>
The environment name specifying the default parameter values in the configuration file to use. The default value is "default". For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="sam-cli-command-reference-sam-publish-options-config-file"></a>
The path and file name of the configuration file containing default parameter values to use. The default value is "`samconfig.toml`" in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--debug`  <a name="sam-cli-command-reference-sam-publish-options-debug"></a>
Turns on debug logging to print debug messages that the AWS SAM CLI generates, and to display timestamps.

`--help`  <a name="sam-cli-command-reference-sam-publish-options-help"></a>
Shows this message and exits.

`--profile {{TEXT}}`  <a name="sam-cli-command-reference-sam-publish-options-profile"></a>
The specific profile from your credential file that gets AWS credentials.

`--region {{TEXT}}`  <a name="sam-cli-command-reference-sam-publish-options-region"></a>
The AWS Region to deploy to. For example, us-east-1.

`--save-params`  <a name="sam-cli-command-reference-sam-publish-options-save-params"></a>
Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--semantic-version {{TEXT}}`  <a name="sam-cli-command-reference-sam-publish-options-semantic-version"></a>
(Optional) Use this option to provide a semantic version of your application that overrides the `SemanticVersion` property in the `Metadata` section of the template file. For more information about semantic versioning, see the [Semantic Versioning specification](https://semver.org/).

`--template, -t {{PATH}}`  <a name="sam-cli-command-reference-sam-publish-options-template"></a>
The path of AWS SAM template file `[default: template.[yaml|yml]]`.

## Examples
<a name="sam-cli-command-reference-sam-publish-examples"></a>

To publish an application:

```
$ sam publish --template {{packaged.yaml}} --region {{us-east-1}}
```
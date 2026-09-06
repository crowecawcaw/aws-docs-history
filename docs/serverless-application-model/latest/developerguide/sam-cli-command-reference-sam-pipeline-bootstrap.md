

# sam pipeline bootstrap
<a name="sam-cli-command-reference-sam-pipeline-bootstrap"></a>

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local pipeline bootstrap` subcommand.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli)

The `sam pipeline bootstrap` subcommand generates the required AWS infrastructure resources to connect to your CI/CD system. This step must be run for each deployment stage in your pipeline prior to running the **sam pipeline init** command.

This subcommand sets up the following AWS infrastructure resources:
+ Option of configuring pipeline permissions through:
  + A pipeline IAM user with access key ID and secret key access credentials to be shared with the CI/CD system.
**Note**  
We recommend rotating access keys regularly. For more information, see [ Rotate access keys regularly for use cases that require long-term credentials ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) in the *IAM User Guide*.
  + Supported CI/CD platforms through OIDC. For an introduction on using OIDC with AWS SAM pipeline, go to [How to use OIDC authentication with AWS SAM pipelines](deploying-with-oidc.md).
+ An CloudFormation execution IAM role assumed by CloudFormation to deploy the AWS SAM application.
+ An Amazon S3 bucket to hold the AWS SAM artifacts.
+ Optionally, an Amazon ECR image repository to hold container image Lambda deployment packages (if you have a resource that is of package type `Image`).

## Usage
<a name="sam-cli-command-reference-sam-pipeline-bootstrap-usage"></a>

```
$ sam pipeline bootstrap {{<options>}}
```

## Options
<a name="sam-cli-command-reference-sam-pipeline-bootstrap-options"></a>

`--bitbucket-repo-uuid {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-bitbucket-repo-uuid"></a>
 The UUID of the Bitbucket repository. This option is specific to using Bitbucket OIDC for permissions.  
This value can be found at https://bitbucket.org/{{workspace}}/{{repository}}/admin/addon/admin/pipelines/openid-connect 

`--bucket {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-bucket"></a>
The ARN of the Amazon S3 bucket that holds the AWS SAM artifacts.

`--cicd-provider {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-cicd-provider"></a>
The CI/CD platform for the AWS SAM pipeline.

`--cloudformation-execution-role {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-cloudformation-execution-role"></a>
The ARN of the IAM role to be assumed by CloudFormation while deploying the application's stack. Provide only if you want to use your own role. Otherwise, the command will create a new role.

`--config-env {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-config-env"></a>
The environment name that specifies the default parameter values in the configuration file to use. The default value is **default**. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--config-file {{PATH}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-config-file"></a>
The path and file name of the configuration file containing the default parameter values to use. The default value is `samconfig.toml` in the root of the project directory. For more information about configuration files, see [AWS SAM CLI configuration file](serverless-sam-cli-config.md).

`--confirm-changeset | --no-confirm-changeset`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-confirm-changeset"></a>
Prompt to confirm the deployment of your resources.

`--create-image-repository | --no-create-image-repository`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-create-image-repository"></a>
Specify whether to create an Amazon ECR image repository if none is provided. The Amazon ECR repository holds the container images of Lambda functions, or layers having a package type of `Image`. The default is `--no-create-image-repository`.

`--debug`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-debug"></a>
Turns on debug logging and prints debug messages that the AWS SAM CLI generates, and to display timestamps.

`--deployment-branch {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-deployment-branch"></a>
Name of the branch that deployments will occur from. This option is specific to using GitHub Actions OIDC for permissions.

`--github-org {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-github-org"></a>
The GitHub organization that the repository belongs to. If no organization exists, enter the user name of the repository owner. This option is specific to using GitHub Actions OIDC for permissions.

`--github-repo {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-github-repo"></a>
Name of the GitHub repository that deployments will occur from. This option is specific to using GitHub Actions OIDC for permissions.

`--gitlab-group {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-gitlab-group"></a>
The GitLab group that the repository belongs to. This option is specific to using GitLab OIDC for permissions.

`--gitlab-project {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-gitlab-project"></a>
The GitLab project name. This option is specific to using GitLab OIDC for permissions.

`--help, -h`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-help"></a>
Shows this message and exits.

`--image-repository {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-image-repository"></a>
The ARN of an Amazon ECR image repository that holds the container images of Lambda functions, or layers that have a package type of `Image`. If provided, the `--create-image-repository` options is ignored. If not provided and `--create-image-repository` is specified, the command creates one.

`--interactive | --no-interactive`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-interactive"></a>
Disable interactive prompting for bootstrap parameters and fail if any required parameters are missing. The default value is `--interactive`. For this command, `--stage` is the only required parameter.  
If `--no-interactive` is specified along with `--use-oidc-provider`, all required parameters for your OIDC provider must be included.

`--oidc-client-id {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-oidc-client-id"></a>
The client ID configured for use with your OIDC provider.

`--oidc-provider {{[github-actions | gitlab | bitbucket-pipelines]}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-oidc-provider"></a>
Name of the CI/CD provider that will be used for OIDC permissions. GitLab, GitHub, and Bitbucket are supported.

`--oidc-provider-url {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-oidc-provider-url"></a>
The URL for the OIDC provider. Value must begin with **https://**.

`--permissions-provider {{[oidc | iam]}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-permissions-provider"></a>
Choose a permissions provider to assume the pipeline execution role. The default value is **iam**.

`--pipeline-execution-role {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-pipeline-execution-role"></a>
The ARN of the IAM role to be assumed by the pipeline user to operate on this stage. Provide only if you want to use your own role. If not provided, this command will create a new role.

`--pipeline-user {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-pipeline-user"></a>
The Amazon Resource Name (ARN) of the IAM user having its access key ID and secret access key shared with the CI/CD system. It is used to grant this IAM user permission to access the corresponding AWS account. If not provided, the command will create an IAM user along with the access key ID and secret access key credentials.

`--profile {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-profile"></a>
The specific profile from your credential file that gets AWS credentials.

`--region {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-region"></a>
The AWS Region to deploy to. For example, `us-east-1`.

`--save-params`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-save-params"></a>
Save the parameters that you provide at the command line to the AWS SAM configuration file.

`--stage {{TEXT}}`  <a name="sam-cli-command-reference-sam-pipeline-bootstrap-options-stage"></a>
The name of the corresponding deployment stage. It is used as a suffix for the created AWS infrastructure resources.

## Troubleshooting
<a name="sam-cli-command-reference-sam-pipeline-bootstrap-troubleshooting"></a>

### Error: Missing required parameter
<a name="sam-cli-command-reference-sam-pipeline-bootstrap-troubleshooting-example1"></a>

When `--no-interactive` is specified along with `--use-oidc-provider` and any of the required parameters are not provided, this error message will be displayed along with a description of the missing parameters.

## Example
<a name="sam-cli-command-reference-sam-pipeline-bootstrap-examples"></a>

The following example creates the AWS resources required to create your CI/CD system, and it turns on debug logging and prints debug messages generated by the AWS SAM CLI: uses a generated event for local testing by using an `s3.json` event to invoke a Lambda function locally

```
$ sam pipeline bootstrap --debug
```
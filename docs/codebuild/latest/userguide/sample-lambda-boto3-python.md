# Update a Lambda function configuration with CodeBuild Lambda Python

The following Python sample uses [Boto3](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/") and CodeBuild Lambda Python to
update a Lambda function’s configuration. This sample can be extended to manage other AWS resources programmatically. For more
information, see [Boto3 documentation](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").

## Prerequisites

Create or find a Lambda function in your account.

This sample assumes that you have already created a Lambda function in your account and
will use CodeBuild to update the Lambda function’s environment variables. For more information on setting up a Lambda function through CodeBuild, see the
[Deploy a Lambda function using AWS SAM with CodeBuild Lambda Java](sample-lambda-sam-gradle.md "sample-lambda-sam-gradle.md") sample or visit [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/").

## Set up your source repository

Create a source repository to store your Boto3 python script.

###### To set up the source repository

1. Copy the following python script to a new file called `update_lambda_environment_variables.py`.

```
import boto3
from os import environ


def update_lambda_env_variable(lambda_client):
    lambda_function_name = environ['LAMBDA_FUNC_NAME']
    lambda_env_variable = environ['LAMBDA_ENV_VARIABLE']
    lambda_env_variable_value = environ['LAMBDA_ENV_VARIABLE_VALUE']
    print("Updating lambda function " + lambda_function_name + " environment variable "
          + lambda_env_variable + " to " + lambda_env_variable_value)
    lambda_client.update_function_configuration(
        FunctionName=lambda_function_name,
        Environment={
            'Variables': {
                lambda_env_variable: lambda_env_variable_value
            }
        },
    )


if __name__ == "__main__":
    region = environ['AWS_REGION']
    client = boto3.client('lambda', region)
    update_lambda_env_variable(client)
```

2. Upload the python file to a supported source repository. For a list of supported
   source types, see [ProjectSource](../APIReference/API_ProjectSource.md "../APIReference/API_ProjectSource.md").

## Create a CodeBuild Lambda Python project

Create a CodeBuild Lambda Python project.

###### To create your CodeBuild Lambda Java project

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. If a CodeBuild information page is displayed, choose **Create build project**. Otherwise, on the navigation pane, expand **Build**,
   choose **Build projects**, and then choose **Create build project**.
3. In **Project name**, enter
   a name for this build project. Build project names must be unique across each AWS account. You can also include an optional description of the build project to
   help other users understand what this project is used for.
4. In **Source**, select the source repository
   where your AWS SAM project is located.
5. In **Environment**:
   - For **Compute**, select **Lambda**.
   - For **Runtime(s)**, select **Python**.
   - For **Image**, select **aws/codebuild/amazonlinux-x86_64-lambda-standard:python3.12**.
   - For **Service role**, leave **New service role** selected. Make a note of the
     **Role name**. This will be required when you update the project’s IAM permissions later in this sample.

6. Choose **Create build project**.
7. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
8. In the navigation pane, choose **Roles** and select the service role associated with your project.
   You can find your project role in CodeBuild by selecting your build project, choosing **Edit**,
   **Environment**, and then **Service role**.
9. Choose the **Trust relationships** tab, and then choose **Edit trust policy**.
10. Add the following inline policy to your IAM role. This will be used to deploy your AWS SAM infrastructure later on. For more
    information, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "UpdateLambdaPermissions",
 "Effect": "Allow",
 "Action": [
 "lambda:UpdateFunctionConfiguration"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Set up the project buildspec

In order to update the Lambda function, the script reads environment variables from the buildspec to find
the Lambda function’s name, environment variable name, and environment variable value.

###### To set up your project buildspec

1. In the CodeBuild console, select your build project, then choose **Edit** and **Buildspec**.
2. In **Buildspec**, choose **Insert build commands** and then **Switch to editor**.
3. Delete the pre-filled build commands and paste in the following buildspec.

```
version: 0.2
env:
  variables:
    LAMBDA_FUNC_NAME: "`<lambda-function-name>`"
    LAMBDA_ENV_VARIABLE: "FEATURE_ENABLED"
    LAMBDA_ENV_VARIABLE_VALUE: "true"
phases:
  install:
    commands:
       - pip3 install boto3
  build:
    commands:
       - python3 update_lambda_environment_variables.py
```

4. Choose **Update buildspec**.

## Update your Lambda configuration

Use CodeBuild Lambda Python to automatically update your Lambda function’s configuration.

###### To update your Lambda function’s configuration

1. Choose **Start build**.
2. Once the build has finished, navigate to your Lambda function.
3. Select **Configuration** and then **Environment** variables. You should see
   a new environment variable with key `FEATURE_ENABLED` and value `true`.

## Clean up your infrastructure

To avoid further charges for resources you used during this tutorial, delete the resources created for your CodeBuild project.

###### To clean up your infrastructure

1. Navigate to the CloudWatch console and delete the CloudWatch log groups associated with your CodeBuild project.
2. Navigate to the CodeBuild console and delete your CodeBuild project by choosing **Delete build project**.
3. If you created a Lambda function for the purpose of this sample, choose **Actions** and **Delete function**
   to clean up your Lambda function.

## Extensions

If you want to extend this sample to manage other AWS resources using AWS CodeBuild Lambda Python:

- Update the Python script to modify the new resources using Boto3.
- Update the IAM role associated with your CodeBuild project to have permissions for the new resources.
- Add any new environment variables associated with the new resources to your buildspec.

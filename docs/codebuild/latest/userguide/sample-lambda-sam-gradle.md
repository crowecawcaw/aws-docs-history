# Deploy a Lambda function using AWS SAM with CodeBuild Lambda Java

The AWS Serverless Application Model (AWS SAM) is an open-source framework for building serverless applications. For more information,
see the [AWS Serverless Application Model repository](https://github.com/aws/serverless-application-model "https://github.com/aws/serverless-application-model") on GitHub.
The following Java sample uses Gradle to build and test a AWS Lambda function. After which, the AWS SAM CLI is used to
deploy the AWS CloudFormation template and deployment bundle. By using CodeBuild Lambda, the build, test, and deployment steps are all
handled automatically, allowing for infrastructure to be quickly updated without manual intervention in a single build.

## Set up your AWS SAM repository

Create an AWS SAM `Hello World` project using the AWS SAM CLI.

###### To create your AWS SAM Project

1. Follow the instructions in the _AWS Serverless Application Model Developer Guide_ for
   [Installing the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/install-sam-cli.md "../../../serverless-application-model/latest/developerguide/install-sam-cli.md") on your local machine.
2. Run `sam init` and select the following project configuration.

```
Which template source would you like to use?: 1 - AWS Quick Start Templates
Choose an AWS Quick Start application template: 1 - Hello World Example
Use the most popular runtime and package type? (Python and zip) [y/N]: N
Which runtime would you like to use?: 8 - java21
What package type would you like to use?: 1 - Zip
Which dependency manager would you like to use?: 1 - gradle
Would you like to enable X-Ray tracing on the function(s) in your application? [y/N]: N
Would you like to enable monitoring using CloudWatch Application Insights? [y/N]: N
Would you like to set Structured Logging in JSON format on your Lambda functions? [y/N]:  N
Project name [sam-app]: <insert project name>
```

3. Upload the AWS SAM project folder to a supported source repository. For a list of supported
   source types, see [ProjectSource](../APIReference/API_ProjectSource.md "../APIReference/API_ProjectSource.md").

## Create a CodeBuild Lambda Java project

Create an AWS CodeBuild Lambda Java project and set up the IAM permissions needed for the build.

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
   - For **Runtime(s)**, select **Java**.
   - For **Image**, select **aws/codebuild/amazonlinux-x86_64-lambda-standard:corretto21**.
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
 "Sid": "",
 "Effect": "Allow",
 "Action": [
 "cloudformation:*",
 "lambda:*",
 "iam:*",
 "apigateway:*",
 "s3:*"
 ],
 "Resource": "`arn:aws:iam::*:role/Service*`"
 }
 ]
}`

```

## Set up the project buildspec

In order to build, test, and deploy your Lambda function, CodeBuild reads and executes build commands from a buildspec.

###### To set up your project buildspec

1. In the CodeBuild console, select your build project, then choose **Edit** and **Buildspec**.
2. In **Buildspec**, choose **Insert build commands** and then **Switch to editor**.
3. Delete the pre-filled build commands and paste in the following buildspec.

```
version: 0.2
env:
  variables:
    GRADLE_DIR: "HelloWorldFunction"
phases:
  build:
    commands:
      - echo "Running unit tests..."
      - cd $GRADLE_DIR; gradle test; cd ..
      - echo "Running build..."
      - sam build --template-file template.yaml
      - echo "Running deploy..."
      - sam package --output-template-file packaged.yaml --resolve-s3 --template-file template.yaml
      - yes | sam deploy
```

4. Choose **Update buildspec**.

## Deploy your AWS SAM Lambda infrastructure

Use CodeBuild Lambda to automatically deploy your Lambda infrastructure

###### To deploy your Lambda infrastructure

1. Choose **Start build**. This will automatically build, test, and deploy your AWS SAM application to AWS Lambda using AWS CloudFormation.
2. Once the build has finished, navigate to the AWS Lambda console and search for your new Lambda function under the AWS SAM project name.
3. Test your Lambda function by selecting **API Gateway** under the **Function** overview, then clicking the **API endpoint** URL. You should see a page open with the message `"message": "hello world"`.

## Clean up your infrastructure

To avoid further charges for resources you used during this tutorial, delete the resources created by your AWS SAM template and CodeBuild.

###### To clean up your infrastructure

1. Navigate to the AWS CloudFormation console and select the `aws-sam-cli-managed-default`.
2. In **Resources**, empty the deployment bucket `SamCliSourceBucket`.
3. Delete the `aws-sam-cli-managed-default` stack.
4. Delete the AWS CloudFormation stack associated with your AWS SAM project. This stack should have the same name as your AWS SAM project.
5. Navigate to the CloudWatch console and delete the CloudWatch log groups associated with your CodeBuild project.
6. Navigate to the CodeBuild console and delete your CodeBuild project by choosing **Delete build project**.

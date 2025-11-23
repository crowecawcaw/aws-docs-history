Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Tutorial: Deploy a serverless application

In this tutorial, you learn how to build, test, and deploy a serverless application as a
CloudFormation stack using a workflow.

The application in this tutorial is a simple web application that outputs a 'Hello World'
message. It consists of an AWS Lambda function and an Amazon API Gateway, and you build it using the
[AWS Serverless Application Model
(AWS SAM)](../../../serverless-application-model/latest/developerguide/what-is-sam.md "../../../serverless-application-model/latest/developerguide/what-is-sam.md"), which is an extension of [CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

###### Topics

- [Prerequisites](#deploy-tut-lambda-cfn-prereqs "#deploy-tut-lambda-cfn-prereqs")
- [Step 1: Create a source repository](#deploy-tut-lambda-cfn-source "#deploy-tut-lambda-cfn-source")
- [Step 2: Create AWS roles](#deploy-tut-lambda-cfn-roles "#deploy-tut-lambda-cfn-roles")
- [Step 3: Add AWS roles to CodeCatalyst](#deploy-tut-lambda-cfn-roles-add "#deploy-tut-lambda-cfn-roles-add")
- [Step 4: Create an Amazon S3 bucket](#deploy-tut-lambda-cfn-s3 "#deploy-tut-lambda-cfn-s3")
- [Step 5: Add source files](#deploy-tut-lambda-cfn-files "#deploy-tut-lambda-cfn-files")
- [Step 6: Create and run a workflow](#deploy-tut-lambda-cfn-workflow "#deploy-tut-lambda-cfn-workflow")
- [Step 7: Make a change](#deploy-tut-lambda-cfn-change "#deploy-tut-lambda-cfn-change")
- [Clean up](#deploy-tut-lambda-cfn-clean-up "#deploy-tut-lambda-cfn-clean-up")

## Prerequisites

Before you begin:

- You need a CodeCatalyst **space** with a connected AWS account. For
  more information, see [Creating a space](spaces-create.md "spaces-create.md").
- In your space, you need an empty project called:

```
codecatalyst-cfn-project
```

Use the **Start from scratch** option to create this project.

For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty "projects-create.md#projects-create-empty").

- In your project, you need a CodeCatalyst **environment** called:

```
codecatalyst-cfn-environment
```

Configure this environment as follows:

    + Choose any type, such as **Non-production**.
    + Connect your AWS account to it.
    + For the **Default IAM role**, choose any role. You'll specify a
     different role later.

For more information, see [Deploying into AWS accounts and VPCs](deploy-environments.md "deploy-environments.md").

## Step 1: Create a source repository

In this step, you create a source repository in CodeCatalyst. This repository is used to store
the tutorial's source files, such as the Lambda function file.

For more information about source repositories, see [Creating a source repository](source-repositories-create.md "source-repositories-create.md").

###### To create a source repository

1. In CodeCatalyst, in the navigation pane, choose **Code**, and then choose
   **Source repositories**.
2. Choose **Add repository**, and then choose **Create
   repository**.
3. In **Repository name**, enter:

```
`codecatalyst-cfn-source-repository`
```

4. Choose **Create**.

You have now created a repository called
`codecatalyst-cfn-source-repository`.

## Step 2: Create AWS roles

In this step, you create the following AWS IAM roles:

- **Deploy role** – Grants the CodeCatalyst **Deploy CloudFormation stack** action permission to access your AWS account and
  CloudFormation service where you’ll deploy your serverless application. The **Deploy CloudFormation stack** action is part of your workflow.
- **Build role** – Grants the CodeCatalyst build action permission to
  access your AWS account and write to Amazon S3 where your serverless application package will
  be stored. The build action is part of your workflow.
- **Stack role** – Grants CloudFormation permission to read and
  modify the resources specified in the AWS SAM template that you will provide later. Also
  grants permission to CloudWatch.

For more information about IAM roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _AWS Identity and Access Management User
Guide_.

###### Note

To save time, you can create a single role, called the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role, instead of
 the three roles listed previously. For more information, see [Creating the CodeCatalystWorkflowDevelopmentRole-spaceName role for your account
 and space](ipa-iam-roles.md#ipa-iam-roles-service-create "ipa-iam-roles.md#ipa-iam-roles-service-create").
 Understand that the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role has very broad permissions that may pose a security
risk. We recommend that you only use this role in tutorials and scenarios where security is
less of a concern. This tutorial assumes you are creating the three roles listed
previously.

###### Note

A [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") is also required, but you don't need to create it now
because the `sam-template.yml` file creates it for you when you run the
workflow in step 5.

###### To create a deploy role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement and then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-deploy-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the deploy role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. In **Permissions policies**, search for `codecatalyst-deploy-policy` and select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-deploy-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst deploy role`
   ```

   10. Choose **Create role**.You have now created a deploy role with a trust policy and permissions policy.

3. Obtain the deploy role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-deploy-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the deploy role with the appropriate permissions, and obtained
   its ARN.

###### To create a build role

1. Create a policy for the role, as follows:
   1. Sign in to AWS.
   2. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   3. In the navigation pane, choose **Policies**.
   4. Choose **Create policy**.
   5. Choose the **JSON** tab.
   6. Delete the existing code.
   7. Paste the following code:

   ###### Note

   The first time the role is used to run workflow actions, use the wildcard
   in the resource policy statement and then scope down the policy with the
   resource name after it is available.

   ```
   "Resource": "*"
   ```

   8. Choose **Next: Tags**.
   9. Choose **Next: Review**.
   10. In **Name**, enter:

   ```
   `codecatalyst-build-policy`
   ```

   11. Choose **Create policy**.

   You have now created a permissions policy.

2. Create the build role, as follows:
   1. In the navigation pane, choose **Roles**, and then choose
      **Create role**.
   2. Choose **Custom trust policy**.
   3. Delete the existing custom trust policy.
   4. Add the following custom trust policy:
   5. Choose **Next**.
   6. In **Permissions policies**, search for
      `codecatalyst-build-policy` and select its check box.
   7. Choose **Next**.
   8. For **Role name**, enter:

   ```
   `codecatalyst-build-role`
   ```

   9. For **Role description**, enter:

   ```
   `CodeCatalyst build role`
   ```

   10. Choose **Create role**.You have now created a build role with a trust policy and permissions policy.

3. Obtain the build role ARN, as follows:
   1. In the navigation pane, choose **Roles**.
   2. In the search box, enter the name of the role you just created
      (`codecatalyst-build-role`).
   3. Choose the role from the list.

   The role's **Summary** page appears. 4. At the top, copy the **ARN** value.You have now created the build role with the appropriate permissions, and obtained its
   ARN.

###### To create a stack role

1.  Sign in to AWS using the account where you want to deploy your stack.
2.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
3.  Create the stack role as follows:
    1. In the navigation pane, choose **Roles**.
    2. Choose **Create role**.
    3. Choose **AWS service**.
    4. In the **Use case** section, choose
       **CloudFormation** from the drop-down list.
    5. Select the **CloudFormation** radio button.
    6. At the bottom, choose **Next**.
    7. Using the search box, find the following permissions policies, and then select
       their respective check boxes.

    ###### Note

    If you search for a policy and it doesn't appear, make sure to choose
    **Clear filters** and try again.

        * **CloudWatchFullAccess**
        * **AWSCloudFormationFullAccess**
        * **IAMFullAccess**
        * **AWSLambda\_FullAccess**
        * **AmazonAPIGatewayAdministrator**
        * **AmazonS3FullAccess**
        * **AmazonEC2ContainerRegistryFullAccess**

    The first policy allows access to CloudWatch to enable stack rollbacks when an alarm
    occurs.

    The remaining policies allow AWS SAM to access the services and resources in the
    stack that will be deployed in this tutorial. For more information, see [Permissions](../../../serverless-application-model/latest/developerguide/sam-permissions.md "../../../serverless-application-model/latest/developerguide/sam-permissions.md") in the _AWS Serverless Application Model Developer Guide_. 8. Choose **Next**. 9. For **Role name**, enter:

    ```
    `codecatalyst-stack-role`
    ```

    10. Choose **Create role**.

4.  Obtain the stack role's ARN, as follows:
    1. In the navigation pane, choose **Roles**.
    2. In the search box, enter the name of the role you just created
       (`codecatalyst-stack-role`).
    3. Choose the role from the list.
    4. In the **Summary** section, copy the **ARN**
       value. You need it later.You have now created the stack role with the appropriate permissions, and you have
       obtained its ARN.

## Step 3: Add AWS roles to CodeCatalyst

In this step, you add the build role (`codecatalyst-build-role`) and deploy role
(`codecatalyst-deploy-role`) to the CodeCatalyst account connection in your
space.

###### Note

You don't need to add the stack role (`codecatalyst-stack-role`) to the
connection. This is because the stack role is used by _CloudFormation_ (not
CodeCatalyst), _after_ a connection is already established between CodeCatalyst and
AWS using the deploy role. Since the stack role is not used by CodeCatalyst to gain access to
AWS, it does not need to be associated with an account connection.

###### To add build and deploy roles to your account connection

1. In CodeCatalyst, navigate to your space.
2. Choose **AWS accounts**. A list of account connections
   appears.
3. Choose the account connection that represents the AWS account where you created your
   build and deploy roles.
4. Choose **Manage roles from AWS management console**.

The **Add IAM role to Amazon CodeCatalyst space** page appears. You
might need to sign in to access the page. 5. Select **Add an existing role you have created in IAM**.

A drop-down list appears. The list displays all IAM roles with a trust policy that
includes the `codecatalyst-runner.amazonaws.com` and
`codecatalyst.amazonaws.com` service principals. 6. In the drop-down list, choose `codecatalyst-build-role`, and choose
**Add role**. 7. Choose **Add IAM role**, choose **Add an existing role you
have created in IAM**, and in the drop-down list, choose
`codecatalyst-deploy-role`. Choose **Add role**.

You have now added the build and deploy roles to your space. 8. Copy the value of the **Amazon CodeCatalyst display name**. You'll need this
value later, when creating your workflow.

## Step 4: Create an Amazon S3 bucket

In this step, you create an Amazon S3 bucket where you store your serverless application's
deployment package .zip file.

###### To create an Amazon S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the main pane, choose **Create bucket**.
3. For **Bucket name**, enter:

```
`codecatalyst-cfn-s3-bucket`
```

4. For **AWS Region**, choose a Region. This tutorial assumes you
   chose **US West (Oregon) us-west-2**. For information about Regions
   supported by Amazon S3, see [Amazon Simple Storage Service endpoints and quotas](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in the _AWS General Reference_.
5. At the bottom of the page, choose **Create bucket**.

You have now created a bucket called `codecatalyst-cfn-s3-bucket`
in the US West (Oregon) us-west-2 Region.

## Step 5: Add source files

In this step, you add several application source files to your CodeCatalyst source repository.
The `hello-world` folder contains the application files that you'll deploy.
The `tests` folder contains unit tests. The folder
structure is as follows:

```
.
|— hello-world
|  |— tests
|     |— unit
|        |— test-handler.js
|  |— app.js
|— .npmignore
|— package.json
|— sam-template.yml
|— setup-sam.sh
```

### .npmignore file

The `.npmignore` file indicates which files and folders npm should
exclude from the application package. In this tutorial, npm excludes the
`tests` folder because it is not part of the application.

###### To add the .npmignore file

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Choose your project, `codecatalyst-cfn-project`
3. In the navigation pane, choose **Code**, and then choose
   **Source repositories**.
4. From the list of source repositories, choose your repository,
   `codecatalyst-cfn-source-repository`.
5. In **Files**, choose **Create file**.
6. For **File name**, enter:

```
`.npmignore`
```

7. In the text box, enter the following code:

```
tests/*
```

8. Choose **Commit**, and then choose **Commit**
   again.

You have now created a file called `.npmignore` in the root of
your repository.

### package.json file

The `package.json` file contains important metadata
about your Node project such as the project name, version number, description, dependencies, and other
details that describe how to interact with and run your application.

The `package.json` in this tutorial includes a list of dependencies
and a `test` script. The test script does the following:

- Using [mocha](https://mochajs.org/ "https://mochajs.org/"), the test script runs the unit
  tests specified in `hello-world/tests/unit/` and writes the results
  to a `junit.xml` file using the xunit
  reporter.
- Using [Istanbul (nyc)](https://istanbul.js.org/ "https://istanbul.js.org/"), the test script
  generates a code coverage report (`clover.xml`) using the [clover](https://openclover.org/doc/manual/4.2.0/general--about-openclover.html "https://openclover.org/doc/manual/4.2.0/general--about-openclover.html") reporter. For more information, see [Using
  alternative reporters](https://istanbul.js.org/docs/advanced/alternative-reporters/#clover "https://istanbul.js.org/docs/advanced/alternative-reporters/#clover") in the Istanbul documentation.

###### To add the package.json file

1. In your repository, in **Files**, choose **Create
   file**.
2. For **File name**, enter:

```
`package.json`
```

3. In the text box, enter the following code:

```
{
  "name": "hello_world",
  "version": "1.0.0",
  "description": "hello world sample for NodeJS",
  "main": "app.js",
  "repository": "https://github.com/awslabs/aws-sam-cli/tree/develop/samcli/local/init/templates/cookiecutter-aws-sam-hello-nodejs",
  "author": "SAM CLI",
  "license": "MIT",
  "dependencies": {
    "axios": "^0.21.1",
    "nyc": "^15.1.0"
  },
  "scripts": {
    "test": "nyc --reporter=clover mocha hello-world/tests/unit/ --reporter xunit --reporter-option output=junit.xml"
  },
  "devDependencies": {
    "aws-sdk": "^2.815.0",
    "chai": "^4.2.0",
    "mocha": "^8.2.1"
  }
}
```

4. Choose **Commit**, and then choose **Commit**
   again.

You have now added a file called `package.json` to the root of
the repository.

### sam-template.yml file

The `sam-template.yml` file contains the instructions for deploying
the Lambda function and API Gateway and configuring them together. It follows the [AWS Serverless Application Model
template specification](../../../serverless-application-model/latest/developerguide/sam-specification.md "../../../serverless-application-model/latest/developerguide/sam-specification.md"), which extends the CloudFormation template specification.

You use an AWS SAM template in this tutorial instead of a regular CloudFormation template because
AWS SAM offers a helpful [AWS::Serverless::Function](../../../serverless-application-model/latest/developerguide/sam-resource-function.md "../../../serverless-application-model/latest/developerguide/sam-resource-function.md") resource type. This type performs much
behind-the-scenes configuration that you normally have to write out to use the basic
CloudFormation syntax. For example, the `AWS::Serverless::Function` creates a Lambda
function, Lambda execution role, and event source mappings that start the function. You have
to code all of this if you want to write it using basic CloudFormation.

Although this tutorial uses a pre-written template, you can generate one as part of your
workflow using a build action. For more information, see [Deploying an CloudFormation stack](deploy-action-cfn.md "deploy-action-cfn.md").

###### To add the sam-template.yml file

1. In your repository, in **Files**, choose **Create
   file**.
2. For **File name**, enter:

```
`sam-template.yml`
```

3. In the text box, enter the following code:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  serverless-api

  Sample SAM Template for serverless-api

# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Timeout: 3

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function # For details on this resource type, see https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      CodeUri: hello-world/
      Handler: app.lambdaHandler
      Runtime: nodejs12.x
      Events:
        HelloWorld:
          Type: Api # For details on this event source type, see https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /hello
            Method: get

Outputs:
  # ServerlessRestApi is an implicit API created out of the events key under Serverless::Function
  # Find out about other implicit resources you can reference within AWS SAM at
  # https://github.com/awslabs/serverless-application-model/blob/master/docs/internals/generated_resources.rst#api
  HelloWorldApi:
    Description: "API Gateway endpoint URL for the Hello World function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/hello/"
  HelloWorldFunction:
    Description: "Hello World Lambda function ARN"
    Value: !GetAtt HelloWorldFunction.Arn
  HelloWorldFunctionIamRole:
    Description: "Implicit Lambda execution role created for the Hello World function"
    Value: !GetAtt HelloWorldFunctionRole.Arn

```

4. Choose **Commit**, and then choose **Commit**
   again.

You have now added a file called `sam-template.yml` under the
root folder of your repository.

### setup-sam.sh file

The `setup-sam.sh` file contains the instructions for downloading and
installing the AWS SAM CLI utility. The workflow uses this utility to package the
`hello-world` source.

###### To add the setup-sam.sh file

1. In your repository, in **Files**, choose **Create
   file**.
2. For **File name**, enter:

```
`setup-sam.sh`
```

3. In the text box, enter the following code:

```
#!/usr/bin/env bash
echo "Setting up sam"

yum install unzip -y

curl -LO https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip -qq aws-sam-cli-linux-x86_64.zip -d sam-installation-directory

./sam-installation-directory/install; export AWS_DEFAULT_REGION=`us-west-2`
```

In the preceding code, replace `us-west-2` with your AWS
Region. 4. Choose **Commit**, and then choose **Commit**
again.

You have now added a file called `setup-sam.sh` to the root of
the repository.

### app.js file

The `app.js` contains the Lambda function code. In this tutorial, the
code returns the text `hello world`.

###### To add the app.js file

1. In your repository, in **Files**, choose **Create
   file**.
2. For **File name**, enter:

```
`hello-world/app.js`
```

3. In the text box, enter the following code:

```
// const axios = require('axios')
// const url = 'http://checkip.amazonaws.com/';
let response;

/**
 *
 * Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
 * @param {Object} event - API Gateway Lambda Proxy Input Format
 *
 * Context doc: https://docs.aws.amazon.com/lambda/latest/dg/nodejs-prog-model-context.html
 * @param {Object} context
 *
 * Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
 * @returns {Object} object - API Gateway Lambda Proxy Output Format
 *
 */
exports.lambdaHandler = async (event, context) => {
    try {
        // const ret = await axios(url);
        response = {
            'statusCode': 200,
            'body': JSON.stringify({
                message: 'hello world',
                // location: ret.data.trim()
            })
        }
    } catch (err) {
        console.log(err);
        return err;
    }

    return response
};
```

4. Choose **Commit**, and then choose **Commit**
   again.

You have now created a folder called `hello-world` and a file
called `app.js`.

### test-handler.js file

The `test-handler.js` file contains unit tests for the Lambda
function.

###### To add the test-handler.js file

1. In your repository, in **Files**, choose **Create
   file**.
2. For **File name**, enter:

```
`hello-world/tests/unit/test-handler.js`
```

3. In the text box, enter the following code:

```
'use strict';

const app = require('../../app.js');
const chai = require('chai');
const expect = chai.expect;
var event, context;

describe('Tests index', function () {
    it('verifies successful response', async () => {
        const result = await app.lambdaHandler(event, context)

        expect(result).to.be.an('object');
        expect(result.statusCode).to.equal(200);
        expect(result.body).to.be.an('string');

        let response = JSON.parse(result.body);

        expect(response).to.be.an('object');
        expect(response.message).to.be.equal("hello world");
        // expect(response.location).to.be.an("string");
    });
});
```

4. Choose **Commit**, and then choose **Commit**
   again.

You have now added a file called `test-handler.js` under the
`hello-world/tests/unit` folder.

You have now added all your source files.

Take a moment to double-check your work and make sure you placed all the files in the
correct folders. The folder structure is as follows:

```
.
|— hello-world
|  |— tests
|     |— unit
|        |— test-handler.js
|  |— app.js
|— .npmignore
|— README.md
|— package.json
|— sam-template.yml
|— setup-sam.sh
```

## Step 6: Create and run a workflow

In this step, you create a workflow that packages your Lambda source code and deploys it.
The workflow consists of the following building blocks that run sequentially:

- A trigger – This trigger starts the workflow run automatically when you push a
  change to your source repository. For more information about triggers, see [Starting a workflow run automatically using
  triggers](workflows-add-trigger.md "workflows-add-trigger.md").
- A test action (`Test`) – On trigger, this action installs [Node package manager (npm)](https://www.npmjs.com/ "https://www.npmjs.com/"), and then runs the
  `npm run test` command. This command tells npm to run the `test`
  script defined in the `package.json` file. The `test`
  script, in turn, runs the unit tests and generates two reports: a test report
  (`junit.xml`) and a code coverage report
  (`clover.xml`). For more information, see [package.json file](#deploy-tut-lambda-cfn-files-package-json "#deploy-tut-lambda-cfn-files-package-json").

Next, the test action transforms the XML reports into CodeCatalyst reports and displays them
in the CodeCatalyst console, under the **Reports** tab of the test
action.

For more information about the test action, see [Testing with workflows](test-workflow-actions.md "test-workflow-actions.md").

- A build action (`BuildBackend`) – On completion of the test action,
  the build action downloads and installs the AWS SAM CLI, packages the
  `hello-world` source, and copies the package to your Amazon S3 bucket,
  where the Lambda service expects it to be. The action also outputs a new AWS SAM template
  file called `sam-template-packaged.yml` and places it in an output
  artifact called `buildArtifact`.

For more information about the build action, see [Building with workflows](build-workflow-actions.md "build-workflow-actions.md").

- A deploy action (`DeployCloudFormationStack`) – On completion of the
  build action, the deploy action looks for the output artifact generated by the build
  action (`buildArtifact`), finds the AWS SAM template inside of it, and then runs
  the template. The AWS SAM template creates a stack that deploys the serverless
  application.

###### To create a workflow

1. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
2. Choose **Create workflow**.
3. For **Source repository**, choose
   `codecatalyst-cfn-source-repository`.
4. For **Branch**, choose `main`.
5. Choose **Create**.
6. Delete the YAML sample code.
7. Add the following YAML code:

###### Note

In the YAML code that follows, you can omit the `Connections:` sections
if you want. If you omit these sections, you must ensure that the role specified in the
**Default IAM role** field in your environment includes the
permissions and trust policies of both roles described in [Step 2: Create AWS roles](#deploy-tut-lambda-cfn-roles "#deploy-tut-lambda-cfn-roles").
For more information about setting up an environment with a default IAM role, see
[Creating an environment](deploy-environments-creating-environment.md "deploy-environments-creating-environment.md").

```
Name: codecatalyst-cfn-workflow
SchemaVersion: 1.0

Triggers:
  - Type: PUSH
    Branches:
      - main
Actions:
  Test:
    Identifier: aws/managed-test@v1
    Inputs:
      Sources:
        - WorkflowSource
    Outputs:
      Reports:
        CoverageReport:
          Format: CLOVERXML
          IncludePaths:
            - "coverage/*"
        TestReport:
          Format: JUNITXML
          IncludePaths:
            - junit.xml
    Configuration:
      Steps:
        - Run: npm install
        - Run: npm run test
  BuildBackend:
    Identifier: aws/build@v1
    DependsOn:
      - Test
    Environment:
      Name: `codecatalyst-cfn-environment`
      Connections:
        - Name: `codecatalyst-account-connection`
          Role: `codecatalyst-build-role`
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
        - Run: . ./setup-sam.sh
        - Run: sam package --template-file sam-template.yml --s3-bucket `codecatalyst-cfn-s3-bucket` --output-template-file sam-template-packaged.yml --region `us-west-2`
    Outputs:
      Artifacts:
        - Name: buildArtifact
          Files:
            - "**/*"
  DeployCloudFormationStack:
    Identifier: aws/cfn-deploy@v1
    DependsOn:
      - BuildBackend
    Environment:
      Name: `codecatalyst-cfn-environment`
      Connections:
        - Name: `codecatalyst-account-connection`
          Role: `codecatalyst-deploy-role`
    Inputs:
      Artifacts:
        - buildArtifact
      Sources: []
    Configuration:
      name: codecatalyst-cfn-stack
      region: `us-west-2`
      role-arn: `arn:aws:iam::111122223333:role/StackRole`
      template: ./sam-template-packaged.yml
      capabilities: CAPABILITY_IAM,CAPABILITY_AUTO_EXPAND
```

In the preceding code, replace:

    * Both instances of `codecatalyst-cfn-environment` with
     the name of your environment.
    * Both instances of `codecatalyst-account-connection`
     with the display name of your account connection. The display name might be a number.
     For more information, see [Step 3: Add AWS roles to CodeCatalyst](#deploy-tut-lambda-cfn-roles-add "#deploy-tut-lambda-cfn-roles-add").
    * `codecatalyst-build-role` with the name of the build role
     that you created in [Step 2: Create AWS roles](#deploy-tut-lambda-cfn-roles "#deploy-tut-lambda-cfn-roles").
    * `codecatalyst-cfn-s3-bucket` with the name of the Amazon S3
     bucket you created in [Step 4: Create an Amazon S3 bucket](#deploy-tut-lambda-cfn-s3 "#deploy-tut-lambda-cfn-s3").
    * Both instances of `us-west-2` with the Region where your
     Amazon S3 bucket resides (first instance) and where your stack will be deployed (second
     instance). These Regions can be different. This tutorial assumes that both Regions are
     set to `us-west-2`. For details about Regions supported by Amazon S3 and CloudFormation,
     see [Service endpoints and quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md") in the
     *AWS General Reference*.
    * `codecatalyst-deploy-role` with the name of the deploy
     role that you created in [Step 2: Create AWS roles](#deploy-tut-lambda-cfn-roles "#deploy-tut-lambda-cfn-roles").
    * `codecatalyst-cfn-environment` with the name of the
     environment that you created in [Prerequisites](#deploy-tut-lambda-cfn-prereqs "#deploy-tut-lambda-cfn-prereqs").
    * `arn:aws:iam::111122223333:role/StackRole` with
     the Amazon Resource Name (ARN) of the stack role that you created in [Step 2: Create AWS roles](#deploy-tut-lambda-cfn-roles "#deploy-tut-lambda-cfn-roles").


    ###### Note

    If you decided not to create build, deploy, and stack roles, replace
     `codecatalyst-build-role`,
     `codecatalyst-deploy-role`, and
     `arn:aws:iam::111122223333:role/StackRole` with
     the name or ARN of the `CodeCatalystWorkflowDevelopmentRole-`spaceName`` role. For more information about this role,
     see [Step 2: Create AWS roles](#deploy-tut-lambda-cfn-roles "#deploy-tut-lambda-cfn-roles").

For information about the properties in the code shown previously, see the ['Deploy CloudFormation stack' action YAML](deploy-action-ref-cfn.md "deploy-action-ref-cfn.md"). 8. (Optional) Choose **Validate** to make sure the YAML code is valid
before committing. 9. Choose **Commit**. 10. On the **Commit workflow** dialog box, enter the following:

    1. For **Workflow file name**, keep the default,
     `codecatalyst-cfn-workflow`.
    2. For **Commit message**, enter:



    ```
    `add initial workflow file`
    ```
    3. For **Repository**, choose
     **codecatalyst-cfn-source-repository**.
    4. For **Branch name**, choose **main**.
    5. Choose **Commit**.You have now created a workflow. A workflow run starts automatically because of the

trigger defined at the top of the workflow. Specifically, when you committed (and pushed)
the `codecatalyst-cfn-workflow.yaml` file to your source repository,
the trigger started the workflow run.

###### To view the workflow run in progress

1. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
2. Choose the workflow you just created:
   `codecatalyst-cfn-workflow`.
3. Choose the **Runs** tab.
4. In the **Run ID** column, choose the run ID.
5. Choose **Test** to see the tests progress.
6. Choose **BuildBackend** to see the build progress.
7. Choose **DeployCloudFormationStack** to see the deployment
   progress.

For more information about viewing run details, see [Viewing workflow run status and details](workflows-view-run.md "workflows-view-run.md"). 8. When the **DeployCloudFormationStack** action finishes, do the
following:

    * If the workflow run succeeded, go to the next procedure.
    * If the workflow run failed on the **Test** or
     **BuildBackend** action, choose **Logs** to
     troubleshoot the issue.
    * If the workflow run failed on the **DeployCloudFormationStack**
     action, choose the deploy action, and then choose the **Summary**
     tab. Scroll to the **CloudFormation events** section to view the detailed
     error message. If a rollback occurred, delete the
     `codecatalyst-cfn-stack` stack through the CloudFormation console in AWS
     before re-running the workflow.

###### To verify the deployment

1. After a successful deployment, choose **Variables (7)** from the
   horizontal menu bar near the top. (Do not choose **Variables** in the
   pane on the right.)
2. Next to **HelloWorldApi**, paste the `https://` URL into a
   browser.

A **hello world** JSON message from the Lambda function is displayed,
indicating that the workflow deployed and configured the Lambda function and API Gateway
successfully.

###### Tip

You can have CodeCatalyst display this URL in the workflow diagram with a few small
configurations. For more information, see [Displaying the app URL in the workflow diagram](deploy-app-url.md "deploy-app-url.md").

###### To verify unit test results and code coverage

1. In the workflow diagram, choose **Test**, and then choose
   **Reports**.
2. Choose **TestReport** to view the unit test results, or choose
   **CoverageReport** to view the code coverage details of the files being
   tested, in this case, `app.js` and
   `test-handler.js`.

###### To verify deployed resources

1. Sign in to the AWS Management Console and open
   the API Gateway console at
   [https://console.aws.amazon.com/apigateway/](https://console.aws.amazon.com/apigateway/ "https://console.aws.amazon.com/apigateway/").
2. Observe the **codecatalyst-cfn-stack** API that the AWS SAM template
   created. The API name comes from the `Configuration/name` value in the workflow
   definition file (`codecatalyst-cfn-workflow.yaml`).
3. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
4. In the navigation pane, choose **Functions**.
5. Choose your Lambda function,
   `codecatalyst-cfn-stack-HelloWorldFunction-`string``.
6. You can see how the API Gateway is a trigger for the function. This integration was
   automatically configured by the AWS SAM `AWS::Serverless::Function` resource
   type.

## Step 7: Make a change

In this step, you make a change to your Lambda source code and commit it. This commit
starts a new workflow run. This run deploys the new Lambda function in a blue-green scheme that
uses the default traffic shifting configuration specified in the Lambda console.

###### To make a change to your Lambda source

1. In CodeCatalyst, navigate to your project.
2. In the navigation pane, choose **Code**, and then choose
   **Source repositories**.
3. Choose your source repository
   `codecatalyst-cfn-source-repository`.
4. Change the application file:
   1. Choose the `hello-world` folder.
   2. Choose the `app.js` file.
   3. Choose **Edit**.
   4. On line 23, change `hello world` to `Tutorial
complete!`.
   5. Choose **Commit**, and then choose **Commit**
      again.

   The commit causes a workflow run to start. This run will fail because you haven't
   updated the unit tests to reflect the name change.

5. Update the unit tests:
   1. Choose `hello-world\tests\unit\test-handler.js`.
   2. Choose **Edit**.
   3. On line 19, change `hello world` to `Tutorial
complete!`.
   4. Choose **Commit**, and then choose **Commit**
      again.

   The commit causes another workflow run to start. This run will succeed.

6. In the navigation pane, choose **CI/CD**, and then choose
   **Workflows**.
7. Choose `codecatalyst-cfn-workflow`, and then choose
   **Runs**.
8. Choose the run ID of the latest run. It should still be in progress.
9. Choose **Test**, **BuildBackend**, and
   **DeployCloudFormationStack** to see the workflow run progress.
10. When the workflow finishes, choose **Variables (7)** near the
    top.
11. Next to **HelloWorldApi**, paste the `https://` URL into a
    browser.

A `Tutorial complete!` message appears in the browser, indicating that your
new application was deployed successfully.

## Clean up

Clean up the files and services used in this tutorial to avoid being charged for
them.

###### To clean up in the CodeCatalyst console

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Delete `codecatalyst-cfn-workflow`.
3. Delete `codecatalyst-cfn-environment`.
4. Delete `codecatalyst-cfn-source-repository`.
5. Delete `codecatalyst-cfn-project`.

###### To clean up in the AWS Management Console

1. Clean up in CloudFormation, as follows:
   1. Open the CloudFormation console at
      [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
   2. Delete the `codecatalyst-cfn-stack`.

   Deleting the stack removes all tutorial resources from the API Gateway and Lambda
   services.

2. Clean up in Amazon S3, as follows:
   1. Open the Amazon S3 console at
      [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
   2. Choose the `codecatalyst-cfn-s3-bucket`.
   3. Delete the bucket contents.
   4. Delete the bucket.

3. Clean up in IAM, as follows:
   1. Open the IAM console at
      [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
   2. Delete the `codecatalyst-deploy-policy`.
   3. Delete the `codecatalyst-build-policy`.
   4. Delete the `codecatalyst-stack-policy`.
   5. Delete the `codecatalyst-deploy-role`.
   6. Delete the `codecatalyst-build-role`.
   7. Delete the `codecatalyst-stack-role`.

In this tutorial, you learned how to deploy a serverless application as a CloudFormation stack
using a CodeCatalyst workflow and a **Deploy CloudFormation stack** action.

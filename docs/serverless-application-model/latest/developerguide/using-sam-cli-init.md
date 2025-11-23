# Create your application in AWS SAM

After completing [Getting started](serverless-getting-started.md "serverless-getting-started.md")
and reading [How to use AWS Serverless Application Model (AWS SAM)](chapter-using-sam.md "chapter-using-sam.md"), you will be ready to create an
AWS SAM project in your developer environment. Your AWS SAM project will serve as the
starting point for writing your serverless application. For a list of AWS SAM CLI `sam init` command options, see [sam init](sam-cli-command-reference-sam-init.md "sam-cli-command-reference-sam-init.md").

The AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam init` command provides options to initialize a new
serverless application that consists of:

- An AWS SAM template to define your infrastructure code.
- A folder structure that organizes your application.
- Configuration for your AWS Lambda functions.
  To create an AWS SAM project, refer to the topics in this sections.

###### Topics

- [Initialize a new serverless application](#using-sam-cli-init-new "#using-sam-cli-init-new")
- [Options for sam init](#using-sam-cli-init-options "#using-sam-cli-init-options")
- [Troubleshooting](#using-sam-cli-init-troubleshooting "#using-sam-cli-init-troubleshooting")
- [Examples](#using-sam-cli-init-examples "#using-sam-cli-init-examples")
- [Learn more](#using-sam-cli-init-learn "#using-sam-cli-init-learn")
- [Next steps](#w2aac18c11c37 "#w2aac18c11c37")

## Initialize a new serverless application

###### To initialize a new serverless application using the AWS SAM CLI

1. `cd` to a starting directory.
2. Run the following at the command line:

```
`$` `sam init`
```

3. The AWS SAM CLI will guide you through an interactive flow to create a new serverless application.

###### Note

As detailed in [Tutorial: Deploy a Hello World application with AWS SAM](serverless-getting-started-hello-world.md "serverless-getting-started-hello-world.md"), this command
initializes your serverless application, creating your project directory. This directory will contain several files and folders. The most important
file is `template.yaml`. This is your AWS SAM template. Your version of python must match the version of python listed in the
`template.yaml` file that the **sam init** command created.

### Choose a starting template

A _template_ consists of the following:

1.  An AWS SAM template for your infrastructure code.
2.  A starting project directory that organizes your project files. For example, this may include:

        1. A structure for your Lambda function code and their dependencies.
        2. An `events` folder that contains test events for local testing.
        3. A `tests` folder to support unit testing.
        4. A `samconfig.toml` file to configure project settings.
        5. A `ReadMe` file and other basic starting project files.

    The following is an example of a starting project directory:

```
sam-app
├── README.md
├── __init__.py
├── events
│   └── event.json
├── hello_world
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── samconfig.toml
├── template.yaml
└── tests
    ├── __init__.py
    ├── integration
    │   ├── __init__.py
    │   └── test_api_gateway.py
    ├── requirements.txt
    └── unit
        ├── __init__.py
        └── test_handler.py
```

You can select from a list of available _AWS Quick Start Templates_ or provide your own
_Custom Template Location_.

###### To choose an AWS Quick Start Template

1. When prompted, select **AWS Quick Start Templates**.
2. Select an AWS Quick Start template to begin with. The following is an example:

```
Which template source would you like to use?
    1 - AWS Quick Start Templates
    2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
    1 - Hello World Example
    2 - Multi-step workflow
    3 - Serverless API
    4 - Scheduled task
    5 - Standalone function
    6 - Data processing
    7 - Hello World Example With Powertools
    8 - Infrastructure event management
    9 - Serverless Connector Hello World Example
    10 - Multi-step workflow with Connectors
    11 - Lambda EFS example
    12 - DynamoDB Example
    13 - Machine Learning
Template: 4
```

###### To choose your own custom template location

1. When prompted, select the **Custom Template Location**.

```
Which template source would you like to use?
    1 - AWS Quick Start Templates
    2 - Custom Template Location
Choice: 2
```

2. The AWS SAM CLI will prompt you to provide a template location.

```
Template location (git, mercurial, http(s), zip, path):
```

Provide any of the following locations to your template .zip file archive:

    * **GitHub repository** – The path to the
     .zip file in your GitHub repository. The file must be in the root of your
     repository.
    * **Mercurial repository** – The path to the
     .zip file in your Mercurial repository. The file must be in the root of your repository.
    * **.zip path** – An HTTPS or local path to your .zip file.

3. The AWS SAM CLI will initialize your serverless application using your custom template.

### Choose a runtime

When you choose an _AWS Quick Start Template_, the AWS SAM CLI prompts you to select a runtime
for your Lambda functions. The list of options displayed by the AWS SAM CLI are the runtimes supported natively by
Lambda.

- The [runtime](../../../lambda/latest/dg/gettingstarted-concepts.md#gettingstarted-concepts-runtime "../../../lambda/latest/dg/gettingstarted-concepts.md#gettingstarted-concepts-runtime") provides a
  language-specific environment that runs in an execution environment.
- When deployed to the AWS Cloud, the Lambda service invokes your function in an [execution environment](../../../lambda/latest/dg/lambda-runtime-environment.md "../../../lambda/latest/dg/lambda-runtime-environment.md").

You can use any other programming language with a custom runtime. To do this, you need to manually create your
starting application structure. You can then use `sam init` to quickly initialize your application by
configuring a custom template location.

From your selection, the AWS SAM CLI creates the starting directory for your Lambda function code and
dependencies.

If Lambda supports multiple dependency managers for your runtime, you will be prompted to choose your preferred
dependency manager.

### Choose a package type

When you choose an _AWS Quick Start Template_ and a _runtime_, the
AWS SAM CLI prompts you to select a _package type_. The package type determines how your Lambda
functions are deployed to use with the Lambda service. The two supported package types are:

1. **Container image** – Contains the base operating system, the runtime,
   Lambda extensions, your application code, and its dependencies.
2. **.zip file archive** – Contains your application code and its
   dependencies.

To learn more about deployment package types, see [Lambda deployment packages](../../../lambda/latest/dg/gettingstarted-package.md "../../../lambda/latest/dg/gettingstarted-package.md") in the
_AWS Lambda Developer Guide_.

The following is an example directory structure of an application with a Lambda function packaged as a container
image. The AWS SAM CLI downloads the image and creates a `Dockerfile` in the function's directory to
specify the image.

```
sam-app
├── README.md
├── __init__.py
├── events
│   └── event.json
├── hello_world
│   ├── Dockerfile
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── samconfig.toml
├── template.yaml
└── tests
    ├── __init__.py
    └── unit
        ├── __init__.py
        └── test_handler.py
```

The following is an example directory structure of an application with a function packaged as a .zip file
archive.

```
sam-app
├── README.md
├── __init__.py
├── events
│   └── event.json
├── hello_world
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
├── samconfig.toml
├── template.yaml
└── tests
    ├── __init__.py
    ├── integration
    │   ├── __init__.py
    │   └── test_api_gateway.py
    ├── requirements.txt
    └── unit
        ├── __init__.py
        └── test_handler.py
```

### Configure AWS X-Ray tracing

You can choose to activate AWS X-Ray tracing. To learn more, see [What is AWS X-Ray?](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md") in the
_AWS X-Ray Developer Guide_.

If you activate, the AWS SAM CLI configures your AWS SAM template. The following is an example:

```
Globals:
  Function:
    ...
    Tracing: Active
  Api:
    TracingEnabled: True
```

### Configure monitoring with Amazon CloudWatch Application Insights

You can choose to activate monitoring using Amazon CloudWatch Application Insights. To learn more, see [Amazon CloudWatch
Application Insights](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.md") in the _Amazon CloudWatch User Guide_.

If you activate, the AWS SAM CLI configures your AWS SAM template. The following is an example:

```
Resources:
  ApplicationResourceGroup:
    Type: AWS::ResourceGroups::Group
    Properties:
      Name:
        Fn::Join:
        - ''
        - - ApplicationInsights-SAM-
          - Ref: AWS::StackName
      ResourceQuery:
        Type: CLOUDFORMATION_STACK_1_0
  ApplicationInsightsMonitoring:
    Type: AWS::ApplicationInsights::Application
    Properties:
      ResourceGroupName:
        Fn::Join:
        - ''
        - - ApplicationInsights-SAM-
          - Ref: AWS::StackName
      AutoConfigurationEnabled: 'true'
    DependsOn: ApplicationResourceGroup
```

### Name your application

Provide a name for your application. The AWS SAM CLI creates a top-level folder for your application using this
name.

## Options for sam init

The following are some of the main options you can use with the `sam init` command. For a list of all
options, see [sam init](sam-cli-command-reference-sam-init.md "sam-cli-command-reference-sam-init.md").

### Initialize an application using a custom template location

Use the `--location` option and provide a supported custom template location. The following is an
example:

```
`$` `sam init --location `https://github.com/aws-samples/sessions-with-aws-sam/raw/master/starter-templates/web-app.zip``
```

### Initialize an application without the interactive

flow

Use the `--no-interactive` option and provide your configuration choices at the command line to skip
the interactive flow. The following is an example:

```
`$` `sam init --no-interactive `--runtime go1.x --name go-demo --dependency-manager mod --app-template hello-world``
```

## Troubleshooting

To troubleshoot the AWS SAM CLI, see [AWS SAM CLI troubleshooting](sam-cli-troubleshooting.md "sam-cli-troubleshooting.md").

## Examples

### Initialize a new serverless application using the

Hello World AWS Starter Template

For this example, see [Step 1: Initialize the sample Hello World application](serverless-getting-started-hello-world.md#serverless-getting-started-hello-world-init "serverless-getting-started-hello-world.md#serverless-getting-started-hello-world-init") in _Tutorial: Deploying a Hello World
application_.

### Initialize a new serverless application with a custom

template location

The following are examples of providing a GitHub location to your custom template:

```
`$` `sam init --location `gh:aws-samples/cookiecutter-aws-sam-python``
`$` `sam init --location `git+sh://git@github.com/aws-samples/cookiecutter-aws-sam-python.git``
`$` `sam init --location `hg+ssh://hg@bitbucket.org/repo/template-name``
```

The following is an example of a local file path:

```
`$` `sam init --location `/path/to/template.zip``
```

The following is an example of a path reachable by HTTPS:

```
`$` `sam init --location `https://github.com/aws-samples/sessions-with-aws-sam/raw/master/starter-templates/web-app.zip``
```

## Learn more

To learn more about using the `sam init` command, see the following:

- **[Learning AWS SAM: sam init](https://www.youtube.com/watch?v=9m3R-leD5Xo "https://www.youtube.com/watch?v=9m3R-leD5Xo")** – Serverless Land "Learning AWS SAM" series on YouTube.
- **[Structuring serverless
  applications for use with the AWS SAM CLI (Sessions with SAM S2E7)](https://www.youtube.com/watch?v=k9IRdgze9fQ "https://www.youtube.com/watch?v=k9IRdgze9fQ")** – Sessions with AWS SAM
  series on YouTube.

## Next steps

Now that you have created your AWS SAM project, you are ready to start authoring your application.
See [Define your infrastructure with AWS SAM](serverless-authoring.md "serverless-authoring.md") for detailed instructions on the tasks you need to complete to do this.

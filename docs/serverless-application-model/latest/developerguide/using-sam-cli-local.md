# Introduction to testing with the sam local command

Use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) `sam local` command to test your serverless
applications locally.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli").

To use `sam local`, install the AWS SAM CLI by completing the following:

- [AWS SAM prerequisites](prerequisites.md "prerequisites.md").
- [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md").
  Before using `sam local`, we recommend a basic understanding of the following:

- [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md").
- [Create your application in AWS SAM](using-sam-cli-init.md "using-sam-cli-init.md").
- [Introduction to building with AWS SAM](using-sam-cli-build.md "using-sam-cli-build.md").
- [Introduction to deploying with AWS SAM](using-sam-cli-deploy.md "using-sam-cli-deploy.md").

## Using the sam local command

Use the `sam local` command with any of its subcommands to perform different types of local testing for
your application.

```
`$` `sam local `<subcommand>``
```

To learn more about each subcommand, see the following:

- **[Intro to sam local generate-event](using-sam-cli-local-generate-event.md "using-sam-cli-local-generate-event.md")** – Generate AWS service events for local
  testing.
- **[Intro to sam local invoke](using-sam-cli-local-invoke.md "using-sam-cli-local-invoke.md")** – Initiate a one-time invocation of an AWS Lambda
  function locally.
- **[Intro to sam local start-api](using-sam-cli-local-start-api.md "using-sam-cli-local-start-api.md")** – Run your Lambda functions using a local
  HTTP server.
- **[Intro to sam local start-lambda](using-sam-cli-local-start-lambda.md "using-sam-cli-local-start-lambda.md")** – Run your Lambda functions using a local
  HTTP server for use with the AWS CLI or SDKs.

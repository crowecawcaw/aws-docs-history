# AWS SAM CLI

AWS Serverless Application Model Command Line Interface (AWS SAM CLI) is a command-line tool for local development and testing of serverless applications. The AWS SAM CLI allows you to build, transform, deploy, debug, package, initialize, and sync your serverless applications locally before deploying to the cloud.

AWS SAM CLI works with serverless applications that are defined using different frameworks and infrastructure as code (IaC) tools, with varying levels of support:

- **AWS SAM templates** – Provides native support with the full feature set, including local testing, debugging, packaging, and deployment capabilities.
- **AWS CDK applications** – Supports local testing of Lambda functions after you synthesize the AWS CDK application to AWS CloudFormation templates using the cdk synth command.
- **AWS CloudFormation templates** – Offers direct compatibility because AWS SAM extends AWS CloudFormation, supporting serverless resources that are defined in standard AWS CloudFormation templates.
- **Terraform applications** – Provides limited support for building and local testing of Lambda functions. Requires you to generate AWS SAM template artifacts that represent your Terraform-defined Lambda functions.
  For the most comprehensive feature support and streamlined developer experience, we recommend using native AWS SAM templates.

###### Topics

- [How AWS SAM CLI commands are documented](#using-sam-cli-documentation "#using-sam-cli-documentation")
- [Configuring the AWS SAM CLI](using-sam-cli-configure.md "using-sam-cli-configure.md")
- [AWS SAM CLI core commands](using-sam-cli-corecommands.md "using-sam-cli-corecommands.md")
- [Local testing with AWS SAM CLI](using-sam-cli-local-testing.md "using-sam-cli-local-testing.md")

## How AWS SAM CLI commands are documented

AWS SAM CLI commands are documented using the following format:

- **Prompt** – The Linux prompt is documented by default and is
  displayed as (`$` ). For commands that are Windows specific, (`>` ) is used as
  the prompt. Do not include the prompt when you type commands.
- **Directory** – When commands must be executed from a specific directory, the
  directory name is shown before the prompt symbol.
- **User input** – Command text that you enter at the command line is formatted
  as `user input`.
- **Replaceable text** – Variable text, such as file names and parameters are
  formatted as `replaceable text`. In multiple-line commands or commands where specific
  keyboard input is required, keyboard input can also be shown as replaceable text. For example,
  `ENTER`.
- **Output** – Output returned as a response to the command is formatted as
  `computer output`.

The following `sam deploy` command and output is an example:

```
`$` `sam deploy --guided --template `template.yaml``

Configuring SAM deploy
======================

    Looking for config file [samconfig.toml] :  Found
    Reading default arguments  :  Success

    Setting default arguments for 'sam deploy'
    =========================================
    Stack Name [sam-app]: `ENTER`
    AWS Region [us-west-2]: `ENTER`
    #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
    Confirm changes before deploy [y/N]: `ENTER`
    #SAM needs permission to be able to create roles to connect to the resources in your template
    Allow SAM CLI IAM role creation [Y/n]: `ENTER`
    #Preserves the state of previously provisioned resources when an operation fails
    Disable rollback [y/N]: `ENTER`
    HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: `y`
    Save arguments to configuration file [Y/n]: `ENTER`
    SAM configuration file [samconfig.toml]: `ENTER`
    SAM configuration environment [default]: `ENTER`
```

1. `sam deploy --guided --template template.yaml` is the command you enter at the command line.
2. `sam deploy --guided --template` should be provided as is.
3. `template.yaml` can be replaced with your specific file name.
4. The output starts at `Configuring SAM deploy`.
5. In the output, `ENTER` and `y` indicate replaceable values that
   you provide.

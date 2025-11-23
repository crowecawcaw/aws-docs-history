# sam list

This page provides reference information for the AWS Serverless Application Model Command Line Interface (AWS SAM CLI)
`sam list` command.

For an introduction to the AWS SAM CLI, see [What is the AWS SAM CLI?](what-is-sam-overview.md#what-is-sam-cli "what-is-sam-overview.md#what-is-sam-cli")

The `sam list` command outputs important information about the resources in your serverless application and the state of your serverless
application. Use **sam list** before and after deployment to assist during local and cloud
development.

## Usage

```
`$` `sam list `<options>` `<subcommand>``
```

## Options

`--help, -h`

Show this message and exit.

## Subcommands

`endpoints`

Displays a list of cloud and local endpoints from your CloudFormation stack. For more information, see
[sam list endpoints](sam-cli-command-reference-sam-list-endpoints.md "sam-cli-command-reference-sam-list-endpoints.md").

`resources`

Displays the resources in your AWS Serverless Application Model (AWS SAM) template that are created in AWS CloudFormation at deployment. For more
information, see [sam list resources](sam-cli-command-reference-sam-list-resources.md "sam-cli-command-reference-sam-list-resources.md").

`stack-outputs`

Displays the outputs of your CloudFormation stack from an AWS SAM or CloudFormation template. For more information, see
[sam list stack-outputs](sam-cli-command-reference-sam-list-stack-outputs.md "sam-cli-command-reference-sam-list-stack-outputs.md").

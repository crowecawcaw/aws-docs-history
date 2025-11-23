# Set up and manage resource access in your AWS SAM template

For your AWS resources to interact with one another, the proper access and permissions
must be configured between your resources. Doing this requires the configuration of AWS Identity and Access Management (IAM)
users, roles, and policies to accomplish your interaction in a secure manner.

The topics in this section are all related to setting up access to the resources defined in your template. This section starts with general best practices.
The next two topics review two options you have for setting up access and permissions between the resources referenced in your serverless application:
AWS SAM connectors and AWS SAM policy templates. The last topic provides details for managing user access using the same mechanics CloudFormation uses for managing users.

To learn more, see
[Controlling access with AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md") in the
_AWS CloudFormation User Guide_.

The AWS Serverless Application Model (AWS SAM) provides two options that simplify management of access and
permissions for your serverless applcations.

1. AWS SAM connectors
2. AWS SAM policy templates

## AWS SAM connectors

Connectors are a way of provisioning permissions between two resources. You do this by describing how they should
interact with each other in your AWS SAM template. They can be defined using either the `Connectors` resource
attribute or `AWS::Serverless::Connector` resource type. Connectors support the provisioning of
`Read` and `Write` access of data and events between a combination of AWS resources. To learn
more about AWS SAM connectors, see [Managing resource permissions with AWS SAM
connectors](managing-permissions-connectors.md "managing-permissions-connectors.md").

## AWS SAM policy templates

AWS SAM policy templates are pre-defined sets of permissions that you can add to your AWS SAM
templates to manage access and permissions between your AWS Lambda functions, AWS Step Functions state
machines and the resources they interact with. To learn more about AWS SAM policy templates, see
[AWS SAM policy templates](serverless-policy-templates.md "serverless-policy-templates.md").

## AWS CloudFormation mechanisms

CloudFormation mechanisms include the configuring of IAM users, roles, and policies to manage
permissions between your AWS resources. To learn more, see [Managing AWS SAM permissions with CloudFormation mechanisms](sam-permissions-cloudformation.md "sam-permissions-cloudformation.md").

## Best practices

Throughout your serverless applications, you can use multiple methods to configure
permissions between your resources. Therefore, you can select the best option for each
scenario and use multiple options together throughout your applications. Here are a few things
to consider when choosing the best option for you:

- AWS SAM connectors and policy templates both reduce the IAM expertise required to
  facilitate secure interactions between your AWS resources. Use connectors and policy
  templates when supported.
- AWS SAM connectors provide a simple and intuitive short-hand syntax to define
  permissions in your AWS SAM templates and require the least amount of IAM expertise. When
  both AWS SAM connectors and policy templates are supported, use AWS SAM connectors.
- AWS SAM connectors can provision `Read` and `Write` access of data
  and events between supported AWS SAM source and destination resources. For a list of
  supported resources, see [AWS SAM connector reference](reference-sam-connector.md "reference-sam-connector.md"). When supported, use AWS SAM connectors.
- While AWS SAM policy templates are limited to permissions between your Lambda functions,
  Step Functions state machines and the AWS resources they interact with, policy templates do
  support all CRUD operations. When supported, and when an AWS SAM policy template for your
  scenario is available, use AWS SAM policy templates. For a list of available policy
  templates, see [AWS SAM policy templates](serverless-policy-templates.md "serverless-policy-templates.md").
- For all other scenarios, or when granularity is required, use CloudFormation mechanisms.

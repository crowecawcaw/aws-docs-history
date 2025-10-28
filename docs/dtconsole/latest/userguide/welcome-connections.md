# What are connections?

You can use the _connections_ feature in the Developer Tools console to connect AWS
resources such as AWS CodePipeline to external code repositories. This feature has its own API, the
[AWS CodeConnections
API reference](../../../codeconnections/latest/APIReference/Welcome.md "../../../codeconnections/latest/APIReference/Welcome.md"). Each connection is a resource that you can give to AWS services to
connect to a third-party repository, such as
Bitbucket.
For example, you can add the connection in CodePipeline so that it triggers your pipeline when a code
change is made to your third-party code repository. Each connection is named and associated with
a unique Amazon Resource Name (ARN) that is used to reference the connection.

###### Important

The service name AWS CodeStar Connections has been renamed. Resources created with the
previous namespace codestar-connections will still be supported.

## What can I do with connections?

You can use connections to integrate third-party provider resources with your AWS
resources in developer tools, including:

- Connect to a third-party provider, such as Bitbucket, and use the third-party
  connection as a source integration with your AWS resources, such as CodePipeline.
- Uniformly manage access to your connection across your resources in CodeBuild build
  projects, CodeDeploy applications, and pipelines in CodePipeline for your third-party provider.
- Use a connection ARN in your stack templates for CodeBuild build projects, CodeDeploy
  applications, and pipelines in CodePipeline, without the need to reference stored secrets or
  parameters.

## What AWS services integrate with

connections?

You can use connections to integrate your third-party repository with other
AWS services. To view the service integrations for connections, see [Product and service integrations with
AWS CodeConnections](integrations-connections.md "integrations-connections.md").

## How do I get started with

connections?

To get started, here are some useful topics to review:

- **Learn** about the [concepts](concepts-connections.md "concepts-connections.md") for connections.
- **Set up** the [resources you need](setting-up-connections.md "setting-up-connections.md") to start working with connections.
- **Get started** with your [first connections](getting-started-connections.md "getting-started-connections.md") and connect them to a
  resource.

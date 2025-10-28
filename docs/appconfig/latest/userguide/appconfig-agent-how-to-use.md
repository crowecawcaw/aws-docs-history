# How to use AWS AppConfig Agent to retrieve configuration

data

The AWS AppConfig Agent is the recommended method for retrieving AWS AppConfig feature flags or free
form configuration data. The agent is supported on all forms of AWS Compute including Amazon EC2,
Amazon ECS, Amazon EKS, and Lambda. After you complete the initial agent set up, using the agent to
retrieve configuration data is simpler than directly calling AWS AppConfig APIs. The agent
automatically implements best practices and may lower your cost of using AWS AppConfig as a result of
fewer API calls to retrieve configurations.

###### Note

Retrieving configuration data from a separate AWS account isn't supported.

**Topics**

- [Using AWS AppConfig Agent with
  AWS Lambda](appconfig-integration-lambda-extensions.md "appconfig-integration-lambda-extensions.md")
- [Using AWS AppConfig Agent with Amazon EC2 and on-premises
  machines](appconfig-integration-ec2.md "appconfig-integration-ec2.md")
- [Using AWS AppConfig Agent with Amazon ECS and
  Amazon EKS](appconfig-integration-containers-agent.md "appconfig-integration-containers-agent.md")
- [Retrieving basic and
  multi-variant feature flags](appconfig-integration-retrieving-feature-flags.md "appconfig-integration-retrieving-feature-flags.md")
- [Using a manifest to enable
  additional retrieval features](appconfig-agent-how-to-use-additional-features.md "appconfig-agent-how-to-use-additional-features.md")
  - [Configuring
    AWS AppConfig Agent to retrieve configurations from multiple accounts](appconfig-agent-how-to-use-additional-features-multi-account.md "appconfig-agent-how-to-use-additional-features-multi-account.md")
  - [Configuring
    AWS AppConfig Agent to write configuration copies to disk](appconfig-agent-how-to-use-additional-features-write-to-disk.md "appconfig-agent-how-to-use-additional-features-write-to-disk.md")

- [Generating a client using the OpenAPI
  specification](appconfig-integration-OpenAPI.md "appconfig-integration-OpenAPI.md")
- [Working with AWS AppConfig Agent
  local development mode](appconfig-agent-how-to-use-local-development.md "appconfig-agent-how-to-use-local-development.md")

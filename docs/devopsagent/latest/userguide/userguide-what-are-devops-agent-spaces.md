# What are DevOps Agent Spaces?

A DevOps Agent Space is a logical container that defines the tools and infrastructure that
AWS DevOps Agent has access to. Each Agent Space operates independently with its own AWS
account access, third-party integrations, and user permissions. An Agent Space represents the
boundary of what AWS DevOps Agent can access and investigate during incident response.

When you create an Agent Space, you define which AWS accounts the agent can access, which
external tools it can connect to, and which users in your organization can interact with the
agent. Each Agent Space functions as an independent deployment of AWS DevOps Agent.

You configure the Agent Space through the AWS Management Console, while your operations
teams use the Agent Space’s web app to conduct investigations and review recommendations within
that space.

## How Agent Spaces are isolated

Agent Spaces maintain isolation to ensure security and prevent unintended access across different environments or teams:

- **AWS account isolation** – Each Agent Space uses dedicated IAM roles that grant access only to specific AWS accounts and resources. The agent cannot access AWS resources outside of those explicitly configured for the Agent Space.
- **Integration isolation** – Connections to observability platforms, code repositories, and communication tools are scoped to each Agent Space. The exception is third-party connections, such as GitHub apps, OAuth tokens, API keys, and other credentials are stored at the account level and shared among Agent Spaces in the account. See [AWS DevOps Agent Security](aws-devops-agent-security.md "aws-devops-agent-security.md") to learn more.
- **User access isolation** – You control which users or groups can access each Agent Space. This allows you to align access permissions with your organizational structure, ensuring teams only interact with their designated Agent Spaces.
- **Data isolation** – Investigation data, incident history, and recommendations are maintained separately within each Agent Space. Information from one Agent Space is not visible or accessible from another Agent Space.

## Agent Space Web App

Each Agent Space has a dedicated web app that is accessible outside of the AWS Management Console. See [What is a DevOps Agent Web App?](userguide-what-is-a-devops-agent-web-app.md "userguide-what-is-a-devops-agent-web-app.md") to learn more about the web app.

## When to use multiple Agent Spaces

Consider creating multiple Agent Spaces to support different organizational needs:

- **Team separation** – Create dedicated Agent Spaces for different application teams or business units to maintain clear ownership boundaries in the Agent Space.
- **Environment isolation** – Separate production and non-production environments into different Agent Spaces to prevent accidental cross-environment access.
- **Service boundaries** – Align Agent Spaces with specific services or application boundaries to keep investigations focused and relevant.
- **Compliance requirements** – Configure separate Agent Spaces with different access controls or data residency settings to meet regulatory requirements.

###### Note

When connecting ticketing and alarm systems to an Agent Space, ensure that the resources
the DevOps Agent will need to effectively investigate an incident or alarm are available to it.

For example, if an alarm you want your DevOps Agent to be able to respond to is connected to
metrics and resources contained in a particular AWS account, make sure to add that account to
your Agent Space as a secondary cloud account.

# Connecting to CI/CD pipelines

CI/CD pipeline integration enables AWS DevOps Agent to monitor deployments and correlate code changes with operational incidents during investigations. By connecting your CI/CD providers, the agent can track deployment events and associate them with AWS resources to help identify potential root causes during incident response.

AWS DevOps Agent supports integration with popular CI/CD platforms through a two-step process:

1. **Account-level registration** – Register your CI/CD provider at the AWS account level. You can create more than one registration per provider, for example, one per organization or group.
2. **Agent Space connection** – Connect specific projects or repositories to individual Agent Spaces based on your organizational needs
   This approach allows you to share CI/CD provider registrations across multiple Agent Spaces while maintaining granular control over which projects are monitored by each space.

## Supported CI/CD providers

AWS DevOps Agent supports the following CI/CD platforms:

- **GitHub** – Connect repositories from [GitHub.com](http://GitHub.com "http://GitHub.com") using the AWS DevOps Agent GitHub app.
- **GitLab** – Connect projects from [GitLab.com](http://gitlab.com "http://gitlab.com"), managed GitLab instances, or GitLab Self-Managed deployments. A GitLab Self-Managed deployment can be publicly accessible, or reachable through an AWS DevOps Agent private connection (see: [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md")).

**Topics**

- [Connecting GitHub](connecting-to-cicd-pipelines-connecting-github.md "connecting-to-cicd-pipelines-connecting-github.md")
- [Connecting GitLab](connecting-to-cicd-pipelines-connecting-gitlab.md "connecting-to-cicd-pipelines-connecting-gitlab.md")

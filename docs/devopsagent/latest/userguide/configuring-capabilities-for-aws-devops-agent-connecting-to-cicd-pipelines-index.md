# Connecting to CI/CD pipelines

CI/CD pipeline integration enables AWS DevOps Agent to monitor deployments and correlate code changes with operational incidents during investigations. By connecting your CI/CD providers, the agent can track deployment events and associate them with AWS resources to help identify potential root causes during incident response.

AWS DevOps Agent supports integration with popular CI/CD platforms through a two-step process:

1. **Account-level registration** – Register your CI/CD provider once at the AWS account level
2. **Agent Space connection** – Connect specific projects or repositories to individual Agent Spaces based on your organizational needs
   This approach allows you to share CI/CD provider registrations across multiple Agent Spaces while maintaining granular control over which projects are monitored by each space.

## Supported CI/CD providers

AWS DevOps Agent supports the following CI/CD platforms:

- **GitHub** – Connect repositories from [GitHub.com](http://GitHub.com "http://GitHub.com") using the AWS DevOps Agent GitHub app.
- **GitLab** – Connect projects from [GitLab.com,](http://gitlab.com "http://gitlab.com") managed GitLab instances, or publicly accessible self-hosted GitLab deployments.

**Topics**

- [Connecting GitHub](configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-connecting-github.md "configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-connecting-github.md")
- [Connecting GitLab](configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-connecting-gitlab.md "configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-connecting-gitlab.md")
- [Associating AWS resources with project deployments](configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-associating-aws-resources-with-project-deployments.md "configuring-capabilities-for-aws-devops-agent-connecting-to-cicd-pipelines-associating-aws-resources-with-project-deployments.md")

# Understand the resource hierarchy and lifecycle

AWS Security Agent organizes security testing resources in a hierarchical structure that determines what’s shared across your organization and what’s scoped per application. Understanding this structure helps you configure AWS Security Agent effectively and know where to find and manage different resources.

## What’s shared across your organization

Some resources in AWS Security Agent are configured once at the organizational level and apply across all your applications and Agent Spaces. These tenant-level resources provide consistency and reduce duplicate configuration work.

| Resource                               | What it is                                                                                                     | Why it’s shared                                                                                                     |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Security requirements**              | Organizational security standards that define what AWS Security Agent validates during design and code reviews | Your security policies apply to all applications. Define them once and AWS Security Agent enforces them everywhere. |
| **GitHub integrations**                | Registered GitHub organizations or user accounts authorized to connect with AWS Security Agent                 | Register your GitHub organization once, then connect specific repositories to any Agent Space as needed.            |
| **IAM Identity Center configurations** | SSO settings that control how users access AWS Security Agent                                                  | Centralized identity management applies across all Agent Spaces in your organization.                               |

###### Important

Changes to security requirements affect all future design reviews and code reviews across all Agent Spaces. Existing reviews are not affected.

## What’s scoped per Agent Space

Each Agent Space represents a distinct application or project you want to secure. Resources at the Agent Space level are scoped to that specific application, allowing different teams to work independently with their own configurations and assessments.

| Resource                                  | What it is                                                                                                             | Why it’s scoped per application                                                                                                 |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Penetration test configurations**       | Test configurations for specific features, API endpoints, or functionality within your application                     | Each application has unique targets, authentication methods, and scope boundaries specific to that application.                 |
| **Design reviews**                        | Individual architectural security assessments of design documents                                                      | Each application has its own architecture and design documents that are assessed independently.                                 |
| **Connected repositories**                | GitHub repositories linked to this Agent Space                                                                         | Different applications use different repositories. Connecting them at the Agent Space level keeps application boundaries clear. |
| **Code review settings**                  | Configuration of which connected repositories have automated code review enabled                                       | Teams control which repositories receive automated security feedback based on their application’s needs.                        |
| **Penetration test remediation settings** | Configuration of which connected repositories can receive automated fix pull requests for penetration testing findings | Teams control where AWS Security Agent can submit code changes based on their application’s workflow.                           |
| **User assignments**                      | Users who have access to this specific Agent Space                                                                     | Teams only see security assessments for applications they’re responsible for, keeping work organized and focused.               |

###### Tip

We recommend creating one Agent Space per application or project to maintain clear boundaries between teams and organize security assessments effectively.

## How GitHub repositories fit into the hierarchy

GitHub repositories are integrated through a multi-step process that connects organizational resources to specific applications:

1. **Register at the tenant level** - Authorize the AWS Security Agent GitHub App for your GitHub organization or user account once
2. **Connect at the Agent Space level** - Select specific repositories to connect to each Agent Space
3. **Configure usage per repository** - Enable specific capabilities for each connected repository:
   - **Code review** - Automated security analysis of pull requests
   - **Penetration testing context** - Application understanding from source code during penetration tests
   - **Penetration test remediation** - Automated pull requests with vulnerability fixes for penetration testing findings

A single repository can be connected to multiple Agent Spaces with different capabilities enabled in each one.

## Key differences between security capabilities

Each security capability in AWS Security Agent follows a different workflow model based on how security teams use it.

### Penetration testing: Reusable configurations with independent executions

Penetration tests use a configuration-and-run model that supports iterative security testing:

- **Create once, execute many times** - Define a configuration for a specific target (API endpoint, feature area) with scope boundaries, authentication, and test parameters
- **Independent executions** - Execute the same configuration multiple times as you improve security. Each execution is independent and generates new findings

This model supports continuous security validation as you develop and deploy improvements.

### Design reviews: One-off assessments with cloning

Design reviews are independent assessments that don’t follow a reusable configuration model:

- **Single assessment** - Each design review analyzes uploaded documents once against your organization’s security requirements
- **Cannot re-run** - Design reviews are not reusable. You cannot re-run the same review
- **Clone for updates** - Clone an existing design review to create a new review with the original documents pre-loaded, allowing you to update documents and run a new analysis

This model supports point-in-time architectural security assessments.

### Code reviews: Automatic and independent

Code reviews integrate into your GitHub workflow without manual configuration per review:

- **Automatic trigger** - AWS Security Agent automatically analyzes pull requests in repositories where code review is enabled
- **Independent reviews** - Each pull request receives its own independent security analysis
- **Findings in GitHub** - Security findings appear as comments on pull requests, not in the Security Agent Web Application

This model embeds security feedback directly into your development workflow.

## Understanding resource relationships

The hierarchy determines where you configure and access different resources:

**In the AWS Management Console:**

- Configure tenant-level resources (security requirements, GitHub integrations, IAM Identity Center)
- Create and manage Agent Spaces
- Configure Agent Space settings (connected repositories, code review enablement, penetration test remediation)

**In the Security Agent Web Application:**

- Create and manage penetration test configurations and test executions
- Create and manage design reviews
- View findings from penetration tests and design reviews

**In GitHub:**

- View code review findings as pull request comments
- Receive automated remediation pull requests for penetration testing findings (when enabled in the Agent Space)

###### Note

Code review findings and penetration test remediation pull requests appear in GitHub. Penetration test and design review findings appear in the Security Agent Web Application.

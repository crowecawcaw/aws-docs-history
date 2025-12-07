# Configuring capabilities for AWS DevOps Agent

AWS DevOps Agent capabilities extend your agent's functionality by connecting it to your existing tools and infrastructure. Configure these capabilities to enable comprehensive incident investigation, automated response workflows, and seamless integration with your DevOps ecosystem.

The following capabilities help you maximize your DevOps Agent's effectiveness:

- **AWS EKS Access Setup** - Enable introspection of Kubernetes clusters, pod logs, and cluster events for both public and private EKS environments
- **CI/CD Pipeline Integration** - Connect GitHub and GitLab pipelines to correlate deployments with incidents and track code changes during investigations
- **MCP Server Connections** - Extend investigation capabilities by connecting external observability tools and custom monitoring systems through Model Context Protocol
- **Multi-Account AWS Access** - Configure secondary AWS accounts to investigate resources across your entire organization during incident response
- **Telemetry Source Integration** - Connect monitoring platforms like Datadog, New Relic, and Splunk for comprehensive observability data access
- **Ticketing and Chat Integration** - Connect ServiceNow, PagerDuty, and Slack to automate incident response workflows and enable team collaboration
- **Webhook Configuration** - Allow external systems to automatically trigger DevOps Agent investigations through HTTP requests
  You can configure each capability independently based on your team's specific needs and existing tool stack. Start with the integrations most critical to your incident response workflow, then expand to additional capabilities as needed.

###### Topics

- [AWS EKS access setup](configuring-capabilities-aws-eks-access-setup.md "configuring-capabilities-aws-eks-access-setup.md")
- [Connecting to CI/CD pipelines](configuring-capabilities-connecting-ci-cd-pipelines-index.md "configuring-capabilities-connecting-ci-cd-pipelines-index.md")
- [Connecting MCP Servers](configuring-capabilities-connecting-mcp-servers.md "configuring-capabilities-connecting-mcp-servers.md")
- [Connecting multiple AWS Accounts](configuring-capabilities-connecting-multiple-aws-accounts.md "configuring-capabilities-connecting-multiple-aws-accounts.md")
- [Connecting telemetry sources](configuring-capabilities-connecting-telemetry-sources-index.md "configuring-capabilities-connecting-telemetry-sources-index.md")
- [Connecting to ticketing and chat](configuring-capabilities-connecting-ticketing-and-chat-index.md "configuring-capabilities-connecting-ticketing-and-chat-index.md")
- [Invoking DevOps Agent through
  Webhook](configuring-capabilities-webhook-configuration.md "configuring-capabilities-webhook-configuration.md")

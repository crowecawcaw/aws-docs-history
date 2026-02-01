# Agent SOPs

Agent SOPs are pre-built, tested workflows that guide AI assistants through complex multi-step AWS tasks.
These automated procedures eliminate the guesswork from common AWS operations by providing step-by-step instructions
that follow AWS best practices and security guidelines.

- Proven workflows that have been tested in real AWS environments
- Security considerations included in procedures
- AWS Well-Architected principles applied consistently
- Error handling guidance for common issues
- Success validation criteria to ensure tasks complete correctly
  For example, when you ask to "create a production-ready VPC," the **Create Production VPC Multi-AZ** Agent SOP guides your
  AI assistant through each step. It creates subnets across multiple availability zones, configures route tables, sets up NAT gateways, and applies
  proper security groups—all following AWS networking best practices.

## Available Agent SOPs

The AWS MCP Server includes Agent SOPs for common AWS tasks. Here are some examples:

- **[Deployment](agent-sops-deployment.md "agent-sops-deployment.md")** — Creates, prepares and deploys production-ready infrastructure as code for existing web applications
- **Infrastructure setup** — Create production-ready VPCs with multi-AZ subnets and NAT gateways
- **Security configuration** — Apply comprehensive security controls and audit logging to S3 buckets
- **Database management** — Create Aurora database clusters with managed credentials and best practices
- **Monitoring setup** — Configure SNS notifications for CloudWatch alarms and monitoring alerts
- **Application management** — Build and deploy full-stack web and mobile applications with AWS Amplify's
  framework and hosting capabilities

You can see which Agent SOPs are available by asking your AI assistant: `What Agent SOPs do you have available?`

If you're unsure how to complete a task, ask the agent to develop a plan with the current tools available.

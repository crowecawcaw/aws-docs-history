# About AWS DevOps Agent

AWS DevOps Agent is a frontier agent that resolves and proactively prevents incidents, continuously improving reliability and performance.

AWS DevOps Agent investigates incidents and identifies operational improvements as an experienced DevOps engineer.

The agent works by:

- Learning your resources and their relationships.
- Working with your observability tools, runbooks, code repositories, and CI/CD pipelines.
- Correlating telemetry, code, and deployment data to understand relationships between your application resources.
- Supporting applications in multicloud and hybrid environments.

## Key features

AWS DevOps Agent provides comprehensive incident response and prevention capabilities through the following features:

### Always-on, autonomous incident response

AWS DevOps Agent autonomously investigates issues the moment they occur:

- **Automated incident investigation** – Begins investigating immediately when an alert or support ticket comes in
- **Interactive investigation chat** – Initiate and guide investigations using natural language in the Dev Op Agent Space web app
- **Detailed mitigation plans** – Provides specific actions to resolve incidents, validate success, and revert changes if needed
- **Automated incident coordination** – Routes observations, findings, and mitigation steps through your preferred communication channels like Slack and ServiceNow
- **AWS Support integration** – Create AWS Support cases directly from an investigation with immediate context provided to AWS Support experts

### Prevent future incidents

AWS DevOps Agent analyzes patterns across historical incidents to help you move from reactive firefighting to proactive operational improvement:

- **Targeted recommendations** – Delivers specific, actionable improvements that strengthen four key areas: observability (monitoring, alerting, logging), infrastructure optimization (autoscaling, capacity tuning), and deployment pipeline enhancement (testing, validation).
- **Continuous learning** – Refines recommendations based on your team's feedback

### Get more from your DevOps tools

AWS DevOps Agent integrates with your existing tools without changing your workflows:

- **Application resource mapping** – Builds a topology graph of your application resources and their relationships
- **Built-in integrations** – Works with popular observability tools (Amazon CloudWatch, Dynatrace, Datadog, New Relic, and Splunk), code repositories, and CI/CD pipelines (GitHub Actions and repositories, GitLab workflows and repositories)
- **Custom tool integration** – Extend capabilities by connecting to your own Model Context Protocol (MCP) servers for additional tools

## How AWS DevOps Agent works

AWS DevOps Agent operates through a dual-console architecture. Administrators use the AWS Management Console to create and manage Agent Spaces, configure integrations, and set up access controls. Operations teams use the AWS DevOps Agent web app for day-to-day incident response and investigation activities. The web app is where operators can interact with agent investigations, browse cross-account application topology, and learn about preventative improvements to observability, code, pipelines, and infrastructure architectures. To learn more, see [Preventing future incidents](devops-agent-incident-response-preventing-future-incidents.md "devops-agent-incident-response-preventing-future-incidents.md").

The service is organized around Agent Spaces, which are logical containers that define what AWS DevOps Agent can access and investigate. Each Agent Space contains your AWS account configurations, third-party tool integrations, and access permissions. To learn more, see [What are DevOps Agent Spaces?](about-aws-devops-agent-what-are-devops-agent-spaces.md "about-aws-devops-agent-what-are-devops-agent-spaces.md").

AWS DevOps Agent automatically builds an application topology that maps your resources and their relationships. This topology helps the service understand your application architecture during investigations. To learn more, see [What is a DevOps Agent Topology?](about-aws-devops-agent-what-is-a-devops-agent-topology.md "about-aws-devops-agent-what-is-a-devops-agent-topology.md").

## Benefits

- **Reduce mean time to resolution (MTTR)** – Autonomous investigation starts immediately, accelerating incident resolution from hours to minutes
- **Prevent recurring incidents** – Targeted recommendations address root causes and strengthen system resilience
- **Improve operational efficiency** – Free your team from repetitive investigation tasks to focus on innovation
- **Work within existing workflows** – Integrates with your existing tools and processes without disruption

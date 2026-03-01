# Enable your applications on Amazon ECS

Enable CloudWatch Application Signals on Amazon ECS by using the custom setup steps described in this section.

For applications running on Amazon ECS, you install and configure the CloudWatch agent and AWS Distro for OpenTelemetry yourself. On these architectures enabled with a custom Application Signals setup, Application Signals
doesn't autodiscover the names of your services or the hosts or clusters they run on. You must specify these names during the custom setup, and the names that you specify are what is displayed on Application Signals dashboards.

## Use a custom setup to enable Application Signals on Amazon ECS

Use these custom setup instructions to onboard your applications on Amazon ECS to CloudWatch Application Signals.
You install and configure the CloudWatch agent and AWS Distro for OpenTelemetry yourself.

There are two methods for deploying Application Signals on Amazon ECS. Choose the one that is best for your
environment.

- [Deploy using the sidecar strategy](CloudWatch-Application-Signals-ECS-Sidecar.md "CloudWatch-Application-Signals-ECS-Sidecar.md") – You add a CloudWatch agent sidecar container
  to each task definition in the cluster.

Advantages:

    + Supports both the `ec2` and `Fargate` launch types.
    + You can always use `localhost` as the IP address when you set up environment variables.

Disadvantages:

    + You must set up the CloudWatch agent sidecar container for each service task that runs in the cluster.
    + Only the `awsvpc` network mode is supported.

- [Deploy using the daemon strategy](CloudWatch-Application-Signals-ECS-Daemon.md "CloudWatch-Application-Signals-ECS-Daemon.md") – You add a CloudWatch agent task only once
  in the cluster, and the [Amazon ECS daemon scheduling strategy](../../../AmazonECS/latest/developerguide/ecs_services.md#service_scheduler_daemon "../../../AmazonECS/latest/developerguide/ecs_services.md#service_scheduler_daemon") deploys it as needed. The ensures that each instance continuously receives traces and metrics, providing
  centralized visibility without the need for the agent to run as a sidecar with each application task definition.

Advantages:

    + You need to set up the daemon service for the CloudWatch agent only once in the cluster.

Disadvantages:

    + Doesn't support the Fargate launch type.
    + If you use the `awsvpc` or `bridge` network mode, you have to manually
     specify each container instance's private IP address in the environment variables.

With either method, on Amazon ECS clusters Application Signals doesn't autodiscover the names of your services. You must
specify your service names during the custom setup, and the names that you specify are what is displayed on
Application Signals dashboards.

## Enable Application Signals on Amazon ECS using Model Context Protocol (MCP)

You can use the CloudWatch Application Signals Model Context Protocol (MCP) server to enable Application Signals on your Amazon ECS clusters through conversational AI interactions. This provides a natural language interface for setting up Application Signals monitoring.

The MCP server automates the enablement process by understanding your requirements and generating the appropriate configuration. Instead of manually following console steps or writing CDK code, you can simply describe what you want to enable.

### Prerequisites

Before using the MCP server to enable Application Signals, ensure you have:

- A Development Environment that supports MCP (such as Kiro, Claude Desktop, VSCode with MCP extensions, or other MCP-compatible tools)
- The CloudWatch Application Signals MCP server configured in your IDE. For detailed setup instructions, see [CloudWatch Application Signals MCP Server documentation](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server").

### Using the MCP server

Once you have configured the CloudWatch Application Signals MCP server in your IDE, you can request enablement guidance using natural language prompts. While the coding assistant can infer context from your project structure, providing specific details in your prompts helps ensure more accurate and relevant guidance. Include information such as your application language, Amazon ECS cluster name, deployment strategy (sidecar or daemon), and absolute paths to your infrastructure and application code.

**Best practice prompts (specific and complete):**

```
"Enable Application Signals for my Python service running on ECS.
My app code is in /home/user/flask-api and IaC is in /home/user/flask-api/terraform"

"I want to add observability to my Node.js application on ECS cluster 'production-cluster' using sidecar deployment.
The application code is at /Users/dev/checkout-service and
the task definitions are at /Users/dev/checkout-service/ecs"

"Help me instrument my Java Spring Boot application on ECS with Application Signals using daemon strategy.
Application directory: /opt/apps/payment-api
CDK infrastructure: /opt/apps/payment-api/cdk"
```

**Less effective prompts:**

```
"Enable monitoring for my app"
→ Missing: platform, language, paths

"Enable Application Signals. My code is in ./src and IaC is in ./infrastructure"
→ Problem: Relative paths instead of absolute paths

"Enable Application Signals for my ECS service at /home/user/myapp"
→ Missing: programming language, deployment strategy
```

**Quick template:**

```
"Enable Application Signals for my [LANGUAGE] service on ECS.
Deployment strategy: [sidecar/daemon]
App code: [ABSOLUTE_PATH_TO_APP]
IaC code: [ABSOLUTE_PATH_TO_IAC]"
```

### Benefits of using the MCP server

Using the CloudWatch Application Signals MCP server offers several advantages:

- **Natural language interface:** Describe what you want to enable without memorizing commands or configuration syntax
- **Context-aware guidance:** The MCP server understands your specific environment and provides tailored recommendations
- **Reduced errors:** Automated configuration generation minimizes manual typing errors
- **Faster setup:** Get from intention to implementation more quickly
- **Learning tool:** See the generated configurations and understand how Application Signals works

### Additional resources

For more information about configuring and using the CloudWatch Application Signals MCP server, see the [MCP server documentation](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server").

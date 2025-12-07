# Using the

Troubleshooting Agent

## Supported Deployment Modes

Apache Spark Troubleshooting Agent for Amazon EMR supports comprehensive analysis
capabilities for failed Spark workloads, including automated error diagnosis,
performance bottleneck identification, code recommendations and actionable
suggestions for improved application performance for the following Spark deployment
mode:

- EMR on EC2
- EMR Serverless
- AWS Glue

Please refer to [Features and Capabilities](spark-troubleshooting-features.md "spark-troubleshooting-features.md") to
understand the detailed features, capacities and limitations.

## Supported Interfaces

### Troubleshooting Cells within

Amazon SageMaker Notebooks

A demonstration of troubleshooting experience with Amazon SageMaker Notebooks. For
any Notebook cell failure, you can ask the Amazon SageMaker Notebook Agent to
troubleshoot the failure to request the analysis followed by possible code fix if
the error resulted from code, by clicking the `Fix with AI` button.

### Troubleshooting Glue and EMR

Spark applications with Kiro CLI

Start Kiro CLI or your AI Assistant and verify the loaded tools for the
troubleshooting process.

```

...
 sagemaker-unified-studio-mcp-code-rec (MCP)
 - spark_code_recommendation    not trusted

 sagemaker-unified-studio-mcp-troubleshooting (MCP)
 - analyze_spark_workload       not trusted
...

```

Now you are ready to start the Spark troubleshooting agent workflow.

A demonstration of the troubleshooting experience with Kiro CLI. You can simply
start the Troubleshooting process with the following prompt:

```

Analyze my Glue job. The job name is "xxx" and the job run id is "xxx"

```

### Integration With Other MCP Clients

The configuration described in [Setup for Troubleshooting Agent](spark-troubleshooting-agent-setup.md "spark-troubleshooting-agent-setup.md") can also be used in other MCP Clients and IDEs to connect
to the Managed MCP server:

- **Integration With Cline** - To use the MCP
  Server with Cline, modify the `cline_mcp_settings.json`
  and add the configuration above. Consult [Cline's
  documentation](https://docs.cline.bot/mcp/configuring-mcp-servers "https://docs.cline.bot/mcp/configuring-mcp-servers") for more information on how to manage MCP
  configuration.
- **Integration With Claude Code** To use the
  MCP Server with Claude Code, modify the configuration file to include the
  MCP configuration. The file path varies depending on your operating system.
  Refer to [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp "https://code.claude.com/docs/en/mcp") for detailed setup.
- **Integration With GitHub Copilot** - To use
  the MCP server with GitHub Copilot, follow the instruction in [https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp "https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp")
  to modify the corresponding configuration file and follow the instructions
  per each IDE to activate the setup.

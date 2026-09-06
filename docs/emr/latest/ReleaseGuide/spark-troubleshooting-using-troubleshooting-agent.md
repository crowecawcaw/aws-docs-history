

# Using the Troubleshooting Agent
<a name="spark-troubleshooting-using-troubleshooting-agent"></a>

## Supported Deployment Modes
<a name="supported-deployment-modes"></a>

Apache Spark Troubleshooting Agent for Amazon EMR supports comprehensive analysis capabilities for failed Spark workloads, including automated error diagnosis, performance bottleneck identification, code recommendations and actionable suggestions for improved application performance for the following Spark deployment mode:
+ EMR on EC2
+ EMR Serverless
+ EMR on EKS
+ AWS Glue

Please refer to [Features and Capabilities](spark-troubleshooting-features.md) to understand the detailed features, capacities and limitations.

## Supported Interfaces
<a name="supported-interfaces"></a>

### Troubleshooting Cells within Amazon SageMaker Notebooks
<a name="troubleshooting-sagemaker-notebooks"></a>

A demonstration of troubleshooting experience with Amazon SageMaker Notebooks. For any Notebook cell failure, you can ask the Amazon SageMaker Notebook Agent to troubleshoot the failure to request the analysis followed by possible code fix if the error resulted from code, by clicking the `Fix with AI` button.

[![AWS Videos](http://img.youtube.com/vi/btW8hwio0tE/0.jpg)](http://www.youtube.com/watch?v=btW8hwio0tE)


### Troubleshooting Glue and EMR Spark applications with Kiro CLI
<a name="troubleshooting-glue-emr-applications"></a>

Start Kiro CLI or your AI Assistant and verify the loaded tools for the troubleshooting process.

```
...
 sagemaker-unified-studio-mcp-code-rec (MCP)
 - spark_code_recommendation    not trusted
 
 sagemaker-unified-studio-mcp-troubleshooting (MCP)
 - analyze_spark_workload       not trusted
...
```

Now you are ready to start the Spark troubleshooting agent workflow.

A demonstration of the troubleshooting experience with Kiro CLI. You can simply start the Troubleshooting process with the following prompt:

```
Analyze my Glue job. The job name is "xxx" and the job run id is "xxx"
```

[![AWS Videos](http://img.youtube.com/vi/YLwV_EenJXY/0.jpg)](http://www.youtube.com/watch?v=YLwV_EenJXY)


### Integration With Other MCP Clients
<a name="integration-other-mcp-clients"></a>

The configuration described in [Setup for Troubleshooting Agent](spark-troubleshooting-agent-setup.md) can also be used in other MCP Clients and IDEs to connect to the Managed MCP server:
+ **Integration With Cline** - To use the MCP Server with Cline, modify the `cline_mcp_settings.json` and add the configuration above. Consult [Cline's documentation](https://docs.cline.bot/mcp/configuring-mcp-servers) for more information on how to manage MCP configuration.
+ **Integration With Claude Code** To use the MCP Server with Claude Code, modify the configuration file to include the MCP configuration. The file path varies depending on your operating system. Refer to [ https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) for detailed setup.
+ **Integration With GitHub Copilot** - To use the MCP server with GitHub Copilot, follow the instruction in [ https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/extend-copilot-chat-with-mcp) to modify the corresponding configuration file and follow the instructions per each IDE to activate the setup.

## Troubleshoot with AI button for Amazon EMR console
<a name="troubleshoot-ai-button-console"></a>

You can use the **Troubleshoot with AI** button directly on the Amazon EMR console to start the troubleshooting agent.

### Troubleshoot with AI button for EMR on EC2 console
<a name="troubleshoot-ai-button-emr-ec2"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home). Choose **EMR on EC2** and select your cluster. Open the **Steps** tab. For any failed Spark step, select the **Failed** button. This reveals the **Troubleshoot with AI** button in the popover. Alternatively, select the checkbox next to the failed step and choose **Troubleshoot with AI** at the top.

The following video shows how to use the **Troubleshoot with AI** button for EMR on EC2.

[![AWS Videos](http://img.youtube.com/vi/BPOlS55EqR8/0.jpg)](http://www.youtube.com/watch?v=BPOlS55EqR8)


### Troubleshoot with AI button for EMR Serverless console
<a name="troubleshoot-ai-button-emr-serverless"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home) and navigate to **EMR Studio**. Open your EMR Studio URL. Navigate to **Applications** and select the application to troubleshoot. Open the **Batch job runs** tab. Select the **Failed** button to reveal the **Troubleshoot with AI** button in the popover. Alternatively, select the checkbox next to the failed job run and choose **Troubleshoot with AI** at the top.

The following video shows how to use the **Troubleshoot with AI** button for EMR Serverless.

[![AWS Videos](http://img.youtube.com/vi/ELgM9DA2Ung/0.jpg)](http://www.youtube.com/watch?v=ELgM9DA2Ung)


### Troubleshoot with AI button for EMR on EKS console
<a name="troubleshoot-ai-button-emr-eks"></a>

Open the Amazon EMR console at [https://console.aws.amazon.com/elasticmapreduce/home](https://console.aws.amazon.com/elasticmapreduce/home). Choose **EMR on EKS virtual clusters** and select your cluster. For any failed Spark job run, select the **Failed** button. This reveals the **Troubleshoot with AI** button in the popover.

The following video shows how to use the **Troubleshoot with AI** button for EMR on EKS.

[![AWS Videos](http://img.youtube.com/vi/UqCVYpG_NuM/0.jpg)](http://www.youtube.com/watch?v=UqCVYpG_NuM)

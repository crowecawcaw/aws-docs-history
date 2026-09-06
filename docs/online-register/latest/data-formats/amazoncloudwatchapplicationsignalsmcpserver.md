

# Data retrieval APIs for Amazon CloudWatch Application Signals MCP Server
<a name="amazoncloudwatchapplicationsignalsmcpserver"></a>

Amazon CloudWatch Application Signals MCP Server provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="application-signals-mcp-CallReadOnlyTool"></a>[CallReadOnlyTool](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html) | Invoke read-only Application Signals MCP tools (list\_monitored\_services, get\_service\_detail, query\_service\_metrics, list\_service\_operations, get\_slo, list\_slos, search\_transaction\_spans, query\_sampled\_traces, list\_slis, get\_enablement\_guide, list\_change\_events, list\_group\_services, audit\_group\_health, get\_group\_dependencies, get\_group\_changes, list\_grouping\_attribute\_definitions, audit\_services, audit\_slos, audit\_service\_operations, analyze\_canary\_failures) | Read | 
| <a name="application-signals-mcp-InvokeMcp"></a>[InvokeMcp](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html) | Connect to and interact with the Application Signals MCP server (initialize, list tools, list resources, list prompts) | Read | 
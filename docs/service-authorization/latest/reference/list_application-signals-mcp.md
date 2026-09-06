

# Actions, resources, and condition keys for Amazon CloudWatch Application Signals MCP Server
<a name="list_application-signals-mcp"></a>

Amazon CloudWatch Application Signals MCP Server (service prefix: `application-signals-mcp`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/application-signals-mcp/application-signals-mcp.json) for this service.

**Topics**
+ [Actions defined by Amazon CloudWatch Application Signals MCP Server](#list_application-signals-mcp-actions-as-permissions)
+ [Resource types defined by Amazon CloudWatch Application Signals MCP Server](#list_application-signals-mcp-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Application Signals MCP Server](#list_application-signals-mcp-policy-keys)

## Actions defined by Amazon CloudWatch Application Signals MCP Server
<a name="list_application-signals-mcp-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CallReadOnlyTool](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html)  **
  - **Description:** Grants permission to invoke read-only Application Signals MCP tools (list\_monitored\_services, get\_service\_detail, query\_service\_metrics, list\_service\_operations, get\_slo, list\_slos, search\_transaction\_spans, query\_sampled\_traces, list\_slis, get\_enablement\_guide, list\_change\_events, list\_group\_services, audit\_group\_health, get\_group\_dependencies, get\_group\_changes, list\_grouping\_attribute\_definitions, audit\_services, audit\_slos, audit\_service\_operations, analyze\_canary\_failures)
  - **Resource types (\*required):** [mcp-server\*](#list_application-signals-mcp-resource-mcp-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-mcp-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InvokeMcp](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html)  **
  - **Description:** Grants permission to connect to and interact with the Application Signals MCP server (initialize, list tools, list resources, list prompts)
  - **Resource types (\*required):** [mcp-server\*](#list_application-signals-mcp-resource-mcp-server)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_application-signals-mcp-aws_ResourceTag___TagKey_)
  - **Access level:** Read



## Resource types defined by Amazon CloudWatch Application Signals MCP Server
<a name="list_application-signals-mcp-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [mcp-server](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals.html)  | arn:${Partition}:application-signals-mcp:${Region}:${Account}:mcp-server/\* | [aws:ResourceTag/${TagKey}](#list_application-signals-mcp-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CloudWatch Application Signals MCP Server
<a name="list_application-signals-mcp-policy-keys"></a>

Amazon CloudWatch Application Signals MCP Server defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
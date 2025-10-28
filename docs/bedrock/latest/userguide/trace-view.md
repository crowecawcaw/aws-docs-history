# View the trace

The following describes how to view the trace. Choose the tab for your preferred method, and then follow the steps:

Console

###### To view the trace during a conversation with an agent

Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at
[https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").

1. In the **Agents** section, select the link for the agent that you want to test from the list of agents.
2. The **Test** window appears in a pane on the right.
3. Enter a message and choose **Run**. While the response is generating or after it finishes generating, select **Show trace**.
4. You can view the trace for each **Step** in real-time as your agent performs orchestration.

API
To view the trace, send an [InvokeAgent](../APIReference/API_agent-runtime_InvokeAgent.md "../APIReference/API_agent-runtime_InvokeAgent.md") request with a [Agents for Amazon Bedrock runtime endpoint](../../../general/latest/gr/bedrock.md#bra-rt "../../../general/latest/gr/bedrock.md#bra-rt")
and set the `enableTrace` field to `TRUE`. By
default, the trace is disabled. or example code, see [Invoke an agent from your application](agents-invoke-agent.md "agents-invoke-agent.md").

If you enable the trace, in the [InvokeAgent](../APIReference/API_agent-runtime_InvokeAgent.md "../APIReference/API_agent-runtime_InvokeAgent.md") response, each
`chunk` in the stream is accompanied by a
`trace` field that maps to a [TracePart](../APIReference/API_agent-runtime_TracePart.md "../APIReference/API_agent-runtime_TracePart.md") object. Within
the [TracePart](../APIReference/API_agent-runtime_TracePart.md "../APIReference/API_agent-runtime_TracePart.md") is a `trace` field that maps to a [Trace](../APIReference/API_agent-runtime_Trace.md "../APIReference/API_agent-runtime_Trace.md")
object.

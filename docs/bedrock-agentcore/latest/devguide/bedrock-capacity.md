# Amazon Bedrock capacity for built-in

with overrides strategies

When configuring [built-in with overrides](memory-custom-strategy.md "memory-custom-strategy.md") strategies with [CreateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateMemory.md") or [UpdateMemory](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateMemory.md"), you must provide an IAM exeecution role
(`memoryExecutionRoleArn`). The AgentCore Memory service assumes this role
to perform Amazon Bedrock operations (such as LLM calls for memory extraction and/or
consolidation) within your AWS account.

Since Amazon Bedrock usage is attributed to your account, it consumes your allocated capacity
and is subject to your Bedrock service quotas. If Amazon Bedrock calls are throttled due to
quota limits, memory ingestion operations might fail.

###### Note

Amazon Bedrock usage is attributed to customer account only for custom memory
strategies.

To monitor and troubleshoot these issues, enable log delivery on your memory
configuration to observe error logs when ingestion failures occur. You can also request
quota increases for the Bedrock models you're using to prevent throttling issues.

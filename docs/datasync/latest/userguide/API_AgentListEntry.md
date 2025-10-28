# AgentListEntry

Represents a single entry in a list (or array) of AWS DataSync agents when
you call the [ListAgents](API_ListAgents.md "API_ListAgents.md") operation.

## Contents

**AgentArn**

The Amazon Resource Name (ARN) of a DataSync agent.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: No

**Name**

The name of an agent.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Pattern: `^[a-zA-Z0-9\s+=._:@/-]+$`

Required: No

**Platform**

The platform-related details about the agent, such as the version number.

Type: [Platform](API_Platform.md "API_Platform.md") object

Required: No

**Status**

The status of an agent.

- If the status is `ONLINE`, the agent is configured properly and ready to
  use.
- If the status is `OFFLINE`, the agent has been out of contact with
  DataSync for five minutes or longer. This can happen for a few reasons. For
  more information, see [What do I do if my agent is offline?](troubleshooting-datasync-agents.md#troubleshoot-agent-offline "troubleshooting-datasync-agents.md#troubleshoot-agent-offline")

Type: String

Valid Values: `ONLINE | OFFLINE`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/AgentListEntry.md "../../../goto/SdkForCpp/datasync-2018-11-09/AgentListEntry.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/AgentListEntry.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/AgentListEntry.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/AgentListEntry.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/AgentListEntry.md")

# OnPremConfig

The AWS DataSync agents that can connect to your Network File System (NFS)
file server.

## Contents

**AgentArns**

The Amazon Resource Names (ARNs) of the DataSync agents that can connect to
your NFS file server.

You can specify more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents "do-i-need-datasync-agent.md#multiple-agents").

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 4 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/OnPremConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/OnPremConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/OnPremConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/OnPremConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/OnPremConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/OnPremConfig.md")



# bedrock-agentcore-memory-event-expiry-duration
<a name="bedrock-agentcore-memory-event-expiry-duration"></a>

Checks whether Amazon Bedrock AgentCore Memory event expiry duration meets the minimum required days. The rule is NON\_COMPLIANT if AgentCore Memory has EventExpiryDuration set to less than the minimum required value. 



**Identifier:** BEDROCK\_AGENTCORE\_MEMORY\_EVENT\_EXPIRY\_DURATION

**Resource Types:** AWS::BedrockAgentCore::Memory

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

minEventExpiryDuration (Optional)Type: intDefault: 7  
Minimum number of days for the event expiry duration. Default is 7 days.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d295c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
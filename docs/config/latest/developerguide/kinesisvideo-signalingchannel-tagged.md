# kinesisvideo-signalingchannel-tagged

Checks if AWS KinesisVideo signaling channel resources have tags. Optionally, required tag keys can be specified. The rule is NON_COMPLIANT if there are no tags or if the specified tag keys are not present. It does not check for tags starting with 'aws:'.

**Identifier:** KINESISVIDEO_SIGNALINGCHANNEL_TAGGED

**Resource Types:** AWS::KinesisVideo::SignalingChannel

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

requiredKeyTags (Optional)
Type: CSV

Comma-separated list of tag keys for the rule to check. If provided, the rule is NON_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

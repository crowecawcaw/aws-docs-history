# appflow-flow-trigger-type-check

Checks if an Amazon AppFlow flow runs using the specified trigger type. The rule is NON_COMPLAINT if the flow does not run using the flow type specified in the required rule parameter.

**Identifier:** APPFLOW_FLOW_TRIGGER_TYPE_CHECK

**Resource Types:** AWS::AppFlow::Flow

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Africa (Cape Town), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

triggerType
Type: CSV

Comma-separated list of trigger types for the rule to check. Valid values include: 'Scheduled', 'Event', and 'OnDemand'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

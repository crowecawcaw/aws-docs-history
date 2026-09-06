

# appflow-flow-trigger-type-check
<a name="appflow-flow-trigger-type-check"></a>

Checks if an Amazon AppFlow flow runs using the specified trigger type. The rule is NON\_COMPLAINT if the flow does not run using the flow type specified in the required rule parameter. 



**Identifier:** APPFLOW\_FLOW\_TRIGGER\_TYPE\_CHECK

**Resource Types:** AWS::AppFlow::Flow

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Africa (Cape Town), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

triggerTypeType: CSV  
Comma-separated list of trigger types for the rule to check. Valid values include: 'Scheduled', 'Event', and 'OnDemand'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d117c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
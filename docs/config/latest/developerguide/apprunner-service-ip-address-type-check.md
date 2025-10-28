# apprunner-service-ip-address-type-check

Checks if an AWS App Runner service is configured with the specified IP address type for incoming public network configuration. The rule is NON_COMPLIANT if the service is not configured with the IP address type specified in the required rule parameter.

**Identifier:** APPRUNNER_SERVICE_IP_ADDRESS_TYPE_CHECK

**Resource Types:** AWS::AppRunner::Service

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney) Region

**Parameters:**

ipAddressType
Type: String

The IP address type value for the rule to check. The rule is NON_COMPLIANT if an AWS App Runner service is configured with a value that does not match this value. Valid values include: 'IPV4', 'DUAL_STACK'.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

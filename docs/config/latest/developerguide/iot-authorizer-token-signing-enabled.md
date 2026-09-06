

# iot-authorizer-token-signing-enabled
<a name="iot-authorizer-token-signing-enabled"></a>

Checks if an AWS IoT Core authorizer has not disabled the signing requirements for validating the token signature in an authorization request. The rule is NON\_COMPLIANT if the authorizer has configuration.SigningDisabled set to True. 



**Identifier:** IOT\_AUTHORIZER\_TOKEN\_SIGNING\_ENABLED

**Resource Types:** AWS::IoT::Authorizer

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Middle East (UAE), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1017c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
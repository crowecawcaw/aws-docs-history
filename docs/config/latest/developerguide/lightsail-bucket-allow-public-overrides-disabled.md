

# lightsail-bucket-allow-public-overrides-disabled
<a name="lightsail-bucket-allow-public-overrides-disabled"></a>

Checks if Amazon Lightsail buckets have allow public overrides disabled. The rule is NON\_COMPLIANT if AllowPublicOverrides is true. Note: AllowPublicOverrides has no effect if GetObject is public, see lightsail-bucket-get-object-private. 



**Identifier:** LIGHTSAIL\_BUCKET\_ALLOW\_PUBLIC\_OVERRIDES\_DISABLED

**Resource Types:** AWS::Lightsail::Bucket

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1079c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
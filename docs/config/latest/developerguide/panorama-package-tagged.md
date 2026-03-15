# panorama-package-tagged

Checks if AWS Panorama package resources have tags. Optionally, required tag keys can be specified. The rule is NON_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'.

**Identifier:** PANORAMA_PACKAGE_TAGGED

**Resource Types:** AWS::Panorama::Package

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Ireland), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

requiredKeyTags (Optional)
Type: CSV

Comma-separated list of tag keys for the rule to check. If provided, the rule is NON_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").

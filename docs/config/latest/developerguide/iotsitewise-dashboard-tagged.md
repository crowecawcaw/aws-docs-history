

# iotsitewise-dashboard-tagged
<a name="iotsitewise-dashboard-tagged"></a>

Checks if AWS IoT SiteWise dashboards have tags. Optionally, you can specify tag keys for the rule. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not check for tags starting with 'aws:'. 



**Identifier:** IOTSITEWISE\_DASHBOARD\_TAGGED

**Resource Types:** AWS::IoTSiteWise::Dashboard

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV  
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d993c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).
# Querying Compliance

History for Conformance Packs for AWS Config

Query
the compliance history using get-resource-config-history using the resource type
`AWS::Config::ConformancePackCompliance`.

```
aws configservice get-resource-config-history --resource-type AWS::Config::ConformancePackCompliance --resource-id `conformance-pack-ID`
```

You should see output similar to the
following:

```
{
    "configurationItems": [
        {
            "version": "1.3",
            "accountId": "`Account ID`",
            "configurationItemCaptureTime": 1614641951.442,
            "configurationItemStatus": "OK",
            "configurationStateId": "1614641951442",
            "configurationItemMD5Hash": "",
            "arn": "arn:aws:config:us-east-1:`Account ID`:conformance-pack/`MyConformancePack1`/`conformance-pack-ID`",
            "resourceType": "AWS::Config::ConformancePackCompliance",
            "resourceId": "`conformance-pack-ID`",
            "resourceName": "`MyConformancePack1`",
            "awsRegion": "us-east-1",
            "tags": {},
            "relatedEvents": [],
            "relationships": [],
            "configuration": "{\"compliantRuleCount\":1,\"configRuleList\":[{\"configRuleName\":\"`RuleName1`-`conformance-pack-ID`\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:`Account ID`:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-nnnnnn\",\"complianceType\":\"INSUFFICIENT_DATA\"},{\"configRuleName\":\"`RuleName2`-`conformance-pack-ID`\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:`Account ID`:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-mmmmmm\",\"complianceType\":\"COMPLIANT\"},{\"configRuleName\":\"`RuleName3`-`conformance-pack-ID`\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:`Account ID`:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-pppppp\",\"complianceType\":\"INSUFFICIENT_DATA\"}],\"totalRuleCount\":3,\"nonCompliantRuleCount\":0,\"complianceType\":\"COMPLIANT\"}",
            "supplementaryConfiguration": {}
        },
        {
            "version": "1.3",
            "accountId": "768311917693",
            "configurationItemCaptureTime": 1605551029.515,
            "configurationItemStatus": "ResourceDiscovered",
            "configurationStateId": "1605551029515",
            "configurationItemMD5Hash": "",
            "resourceType": "AWS::Config::ConformancePackCompliance",
            "resourceId": "`conformance-pack-ID`",
            "resourceName": "`MyConformancePack1`",
            "awsRegion": "us-east-1",
            "tags": {},
            "relatedEvents": [],
            "relationships": [],
            "configuration": "{\"compliantRuleCount\":1,\"configRuleList\":[{\"configRuleName\":\"`RuleName1`-`conformance-pack-ID`\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:`Account ID`:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-nnnnnn\",\"complianceType\":\"INSUFFICIENT_DATA\"},{\"configRuleName\":\"`RuleName2`-`conformance-pack-ID`\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:`Account ID`:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-mmmmmm\",\"complianceType\":\"COMPLIANT\"},{\"configRuleName\":\"`RuleName3`-`conformance-pack-ID`\",\"controls\":[],\"configRuleArn\":\"arn:aws:config:us-east-1:`Account ID`:config-rule/aws-service-rule/config-conforms.amazonaws.com/config-rule-pppppp\",\"complianceType\":\"INSUFFICIENT_DATA\"}],\"totalRuleCount\":3,\"nonCompliantRuleCount\":0,\"complianceType\":\"COMPLIANT\"}",
            "supplementaryConfiguration": {}
        }
    ]
}
```

For more information, see [Supported Resource Types
(AWS Config)](resource-config-reference.md#awsconfig "resource-config-reference.md#awsconfig") and [GetResourceConfigHistory](../APIReference/API_GetResourceConfigHistory.md "../APIReference/API_GetResourceConfigHistory.md") in the API reference.

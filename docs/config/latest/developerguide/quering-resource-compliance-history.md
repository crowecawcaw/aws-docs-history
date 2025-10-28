# Querying Compliance History for your AWS Resources

Query the resource compliance history using get-resource-config-history using the
resource type `AWS::Config::ResourceCompliance`.

```
aws configservice get-resource-config-history --resource-type AWS::Config::ResourceCompliance --resource-id AWS::S3::Bucket/configrules-bucket
```

You should see output similar to the following:

```
{
	"configurationItems": [
		{
			"configurationItemCaptureTime": 1539799966.921,
			"relationships": [
				{
					"resourceType": "AWS::S3::Bucket",
					"resourceId": "configrules-bucket",
					"relationshipName": "Is associated with "
				}
			]
			"tags": {},
			"resourceType": "AWS::Config::ResourceCompliance",
			"resourceId": "AWS::S3::Bucket/configrules-bucket",
			"ConfigurationStateId": "1539799966921",
			"relatedEvents": [];
			"awsRegion": "us-west-2",
			"version": "1.3",
			"configurationItemMD5Hash": "",
			"supplementaryConfiguration": {},
			"configuration": "{\"complianceType\":\"COMPLIANT\",\"targetResourceId\":\"configrules-bucket\",\"targetResourceType\":\"AWS::S3::Bucket\",\configRuleList"\":[{\"configRuleArn\":\"arn:aws:config:us-west-2:`AccountID`:config-rule/config-rule-w1gogw\",\"configRuleId\":\"config-rule-w1gogw\",\"configRuleName\":\"s3-bucket-logging-enabled\",\"complianceType\":\"COMPLIANT\"}]}",

			"configurationItemStatus": "ResourceDiscovered",
			"accountId": "`AccountID`"
		}
	]
}
```

# AwsCloudFormation resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsCloudFormation` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsCloudFormationStack

The `AwsCloudFormationStack` object provides details about an AWS CloudFormation
stack that is nested as a resource in a top-level template.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsCloudFormationStack` object. To view descriptions of
`AwsCloudFormationStack` attributes, see [AwsCloudFormationStackDetails](../../1.0/APIReference/API_AwsCloudFormationStackDetails.md "../../1.0/APIReference/API_AwsCloudFormationStackDetails.md") in the
_AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsCloudFormationStack": {
	"Capabilities": [
		"CAPABILITY_IAM",
		"CAPABILITY_NAMED_IAM"
	],
	"CreationTime": "2022-02-18T15:31:53.161Z",
	"Description": "AWS CloudFormation Sample",
	"DisableRollback": true,
	"DriftInformation": {
		"StackDriftStatus": "DRIFTED"
	},
	"EnableTerminationProtection": false,
	"LastUpdatedTime": "2022-02-18T15:31:53.161Z",
	"NotificationArns": [
		"arn:aws:sns:us-east-1:978084797471:sample-sns-cfn"
	],
	"Outputs": [{
		"Description": "URL for newly created LAMP stack",
		"OutputKey": "WebsiteUrl",
		"OutputValue": "http://ec2-44-193-18-241.compute-1.amazonaws.com"
	}],
	"RoleArn": "arn:aws:iam::012345678910:role/exampleRole",
	"StackId": "arn:aws:cloudformation:us-east-1:978084797471:stack/sample-stack/e5d9f7e0-90cf-11ec-88c6-12ac1f91724b",
	"StackName": "sample-stack",
	"StackStatus": "CREATE_COMPLETE",
	"StackStatusReason": "Success",
	"TimeoutInMinutes": 1
}
```

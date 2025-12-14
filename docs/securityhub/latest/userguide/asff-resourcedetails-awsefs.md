# AwsEfs resources in ASFF

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsEfs` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see
[AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

## AwsEfsAccessPoint

The `AwsEfsAccessPoint` object provides details about files stored in
Amazon Elastic File System.

The following example shows the AWS Security Finding Format (ASFF) for the
`AwsEfsAccessPoint` object. To view descriptions of
`AwsEfsAccessPoint` attributes, see [AwsEfsAccessPointDetails](../../1.0/APIReference/API_AwsEfsAccessPointDetails.md "../../1.0/APIReference/API_AwsEfsAccessPointDetails.md") in the
_AWS Security Hub CSPM API Reference_.

**Example**

```
"AwsEfsAccessPoint": {
	"AccessPointId": "fsap-05c4c0e79ba0b118a",
	"Arn": "arn:aws:elasticfilesystem:us-east-1:863155670886:access-point/fsap-05c4c0e79ba0b118a",
	"ClientToken": "AccessPointCompliant-ASk06ZZSXsEp",
	"FileSystemId": "fs-0f8137f731cb32146",
	"PosixUser": {
		"Gid": "1000",
		"SecondaryGids": ["0", "4294967295"],
		"Uid": "1234"
	},
	"RootDirectory": {
		"CreationInfo": {
			"OwnerGid": "1000",
			"OwnerUid": "1234",
			"Permissions": "777"
		},
		"Path": "/tmp/example"
	}
}
```

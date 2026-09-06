

End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html). 

# AWS managed policies for AWS re:Post Private
<a name="security-with-iam-managed-policy"></a>

Using AWS managed policies makes adding permissions to users, groups, and roles easier than writing policies yourself. It takes time and expertise to create [ IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. Use AWS managed policies to get started quickly. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services might occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services don't remove permissions from an AWS managed policy, so policy updates don't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Topics**
+ [AWS managed policy: AWSRepostSpaceSupportOperationsPolicy](#support-case-manpol)
+ [AWS managed policy: AWSrePostPrivateCloudWatchAccess](#cloudwatch-metric-manpol)
+ [AWS re:Post Private updates to AWS managed policies](#security-iam-awsmanpol-updates)

## AWS managed policy: AWSRepostSpaceSupportOperationsPolicy
<a name="support-case-manpol"></a>

This policy allows the AWS re:Post Private service to create, manage, and resolve Support cases that are created through the re:Post Private web application.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "RepostSpaceSupportOperations",
			"Effect": "Allow",
			"Action": [
				"support:AddAttachmentsToSet",
				"support:AddCommunicationToCase",
				"support:CreateCase",
				"support:DescribeCases",
				"support:DescribeCommunications",
				"support:ResolveCase"
			],
			"Resource": "*"
		}
	]
}
```

------

## AWS managed policy: AWSrePostPrivateCloudWatchAccess
<a name="cloudwatch-metric-manpol"></a>

This policy allows the re:Post Private service to publish data to CloudWatch.

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "CloudWatchPublishMetrics",
			"Effect": "Allow",
			"Action": [
				"cloudwatch:PutMetricData"
			],
			"Resource": "*",
			"Condition": {
				"StringEquals": {
					"cloudwatch:namespace": [
						"AWS/rePostPrivate",
						"AWS/Usage"
					]
				}
			}
		}
	]
}
```

------

## AWS re:Post Private updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for re:Post Private since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history](doc-history.md) page.



The following table describes important updates to the re:Post Private managed policies since November 26, 2023.


| Change | Description | Date | 
| --- | --- | --- | 
| New policy - [AWSrePostPrivateCloudWatchAccess](https://docs.aws.amazon.com/repostprivate/latest/caguide/security-with-iam-managed-policy.html#cloudwatch-metric-manpol) | New managed policy for publishing data to CloudWatch | November 26, 2023 | 
| New policy - [AWSRepostSpaceSupportOperationsPolicy](https://docs.aws.amazon.com/repostprivate/latest/caguide/security-with-iam-managed-policy.html#support-case-manpol) | New managed policy for the AWS Support feature in AWS re:Post Private | November 26, 2023 | 
| re:Post Private started tracking changes | re:Post Private started tracking changes for its AWS managed policies | November 26, 2023 | 
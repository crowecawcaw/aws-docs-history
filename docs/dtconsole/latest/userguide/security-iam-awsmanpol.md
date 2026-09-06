

# AWS managed policies for AWS CodeConnections
<a name="security-iam-awsmanpol"></a>





An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Note**  
Actions for resources that are created under the new service prefix `codeconnections` are available. Creating a resource under the new service prefix will use `codeconnections` in the resource ARN. Actions and resources for the `codestar-connections` service prefix remain available. When specifying a resource in the IAM policy, the service prefix needs to match that of the resource.













## AWS managed policy: AWSGitSyncServiceRolePolicy
<a name="security-iam-awsmanpol-AWSGitSyncServiceRolePolicy"></a>



You can't attach AWSGitSyncServiceRolePolicy to your IAM entities. This policy is attached to a service-linked role that allows AWS CodeConnections to perform actions on your behalf. For more information, see [Using service-linked roles for AWS CodeConnections](service-linked-role-connections.md).



This policy allows customers to access Git-based repositories for use with connections. Customers will access these resources after using the CreateRepositoryLink API.



**Permissions details**

This policy includes the following permissions.




+ `codeconnections` – Grants permissions to allow users to create connections to external Git-based repositories.



------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "AccessGitRepos",
			"Effect": "Allow",
			"Action": [
				"codestar-connections:UseConnection",
				"codeconnections:UseConnection"
			],
			"Resource": [
				"arn:aws:codestar-connections:*:*:connection/*",
				"arn:aws:codeconnections:*:*:connection/*"
			],
			"Condition": {
				"StringEquals": {
					"aws:ResourceAccount": "${aws:PrincipalAccount}"
				}
			}
		}
	]
}
```

------

## AWS CodeConnections updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for AWS CodeConnections since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS CodeConnections [Document history](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AWSGitSyncServiceRolePolicy](#security-iam-awsmanpol-AWSGitSyncServiceRolePolicy) – Updated policy | AWS CodeStar Connections service name changed to AWS CodeConnections. Updated the policy for resources with ARNs that contain both service prefixes. | April 26, 2024 | 
| [AWSGitSyncServiceRolePolicy](#security-iam-awsmanpol-AWSGitSyncServiceRolePolicy) – New policy | AWS CodeStar Connections added the policy.<br />Grants permissions to allow connections users to use Git sync with connected Git-based repositories. | November 26, 2023 | 
| AWS CodeConnections started tracking changes | AWS CodeConnections started tracking changes for its AWS managed policies. | November 26, 2023 | 


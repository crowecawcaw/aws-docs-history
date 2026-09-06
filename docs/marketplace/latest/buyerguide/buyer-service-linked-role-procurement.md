

# Service-linked role to share procurement data
<a name="buyer-service-linked-role-procurement"></a>

AWS Marketplace uses the `AWSServiceRoleForProcurementInsightsPolicy` service-linked role to access and describe the data in your AWS organization. You must create this role to use the [Procurement insights dashboard](procurement-insights.md).

The `AWSServiceRoleForProcurementInsightsPolicy` service-linked role trusts the following services to assume the role:
+ `procurement-insights.marketplace.amazonaws.com`

The `AWSServiceRoleForProcurementInsightsPolicy` allows AWS Marketplace to perform the following actions on specified resources.

**Note**  
For more information about AWS Marketplace managed policies, see [AWS managed policies for AWS Marketplace buyers](buyer-security-iam-awsmanpol.md).

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Sid": "ProcurementInsightsPermissions",
			"Effect": "Allow",
			"Action": [
				"organizations:DescribeAccount",
				"organizations:DescribeOrganization",
				"organizations:ListAccounts"
			],
			"Resource": [
				"*"
			]
		}
	]
}
```

------

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.
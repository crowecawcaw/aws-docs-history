

# AWS managed policy
<a name="mwaa-serverless-aws-managed-policy"></a>

 An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles. 

 Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases. 

 You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services. 

 For more information, see AWS managed policies in the [ IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies). 

## AWS managed policy: AmazonMWAAServerlessServiceRolePolicy
<a name="aws-managed-policy-AmazonMWAAServerlessServiceRolePolicy"></a>

 The `AWSServiceRoleForAmazonMWAAServerless` service-linked role used by Amazon MWAA Serverless to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles. 

 This policy grants administrative permissions that allow the service-linked role full access to perform tasks required to manage network configuration for your Amazon EC2 instances. 

### Permission details
<a name="policy-permission-details"></a>

 This policy includes the following permissions: 
+  `ec2` - Allows users to perform actions to manage network configuration of EC2 such as Attach, Create, Delete etc. 

 To review the permissions for this policy, see [ AmazonMWAAServerlessServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonMWAAServerlessServiceRolePolicy.html) in the AWS Managed Policy Reference Guide. 

## Amazon MWAA Serverless updates to AWS managed policies
<a name="aws-managed-policy-updates"></a>

 The following table provides details about updates to AWS managed policies for Amazon MWAA Serverless since this service began tracking these changes. For automatic alerts about updates to the policies, subscribe to the RSS feed on the Amazon MWAA Serverless [document history page](doc-history.md). 


| Change | Description | Date | 
| --- | --- | --- | 
|  Amazon MWAA Serverless update its service-linked role permission policy  |  [ AmazonMWAAServerlessServiceRolePolicy](#aws-managed-policy-AmazonMWAAServerlessServiceRolePolicy) – Amazon MWAA updates the permission policy for its service-linked role to grant Amazon MWAA Serverless permission to perform actions on all Amazon MWAA Serverless-supported AWS resources  | November 17, 2025 | 
|  Amazon MWAA Serverless started tracking changes  |  Amazon MWAA Serverless started tracking changes for its AWS-managed service-linked role permission policy.  | November 17, 2025 | 
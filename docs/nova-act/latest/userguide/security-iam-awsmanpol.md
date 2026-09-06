

# AWS managed policies for Amazon Nova Act
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they’re available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

 AWS addresses many common use cases by providing standalone IAM policies that are created and administered by AWS. These AWS managed policies grant necessary permissions for common use cases so that you can avoid having to investigate which permissions are needed. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: NovaActServiceRolePolicy
<a name="shared_aws_managed_policy_novaactservicerolepolicy"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

This policy grants permissions that Amazon Nova Act to publish operational metrics to Amazon CloudWatch under the AWS/NovaAct namespace. These metrics provide visibility into agent performance and operational health.

Amazon Nova Act uses this AWS managed policy to publish metrics that help you monitor the service. The policy grants the `cloudwatch:PutMetricData` permission with a condition that restricts metric publication to the AWS/NovaAct namespace only, ensuring that the service can only publish its own operational metrics.

For the JSON policy document for NovaActServiceRolePolicy, see [NovaActServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/NovaActServiceRolePolicy.html) in the * AWS Managed Policy Reference Guide*.

## Customer managed policy: NovaActFullAccess
<a name="_customer_managed_policy_novaactfullaccess"></a>

**Note**  
Amazon Nova Act does not yet define a managed policy which grants access to the Nova Act service. You will need to define a customer-managed policy for this purpose.

For example:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "nova-act:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "nova-act.amazonaws.com"
                 }
            }
        }
    ]
}
```

**Note**  
If you use the `exportConfig` parameter in `CreateWorkflowDefinition` to export Agent Trajectory Data to an S3 bucket, the calling identity requires additional S3 permissions. For details, see [Configure access to an Amazon S3 bucket for data export](security-iam-s3-export-permissions.md).

## AWS managed policy updates
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Amazon Nova Act since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| NovaActServiceRolePolicy | Amazon Nova Act added a new policy. This policy allows Amazon Nova Act to publish operational metrics to CloudWatch using the cloudwatch:PutMetricData action, scoped to the AWS/NovaAct namespace through a condition statement. | December 2, 2025 | 
| Amazon Nova Act started tracking changes | Amazon Nova Act started tracking changes for its AWS managed policies. | December 2, 2025 | 
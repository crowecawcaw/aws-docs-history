

# AWSTrustedAdvisorPriorityReadOnlyAccess
<a name="AWSTrustedAdvisorPriorityReadOnlyAccess"></a>

**Description**: Provides read-only access to AWS Trusted Advisor Priority. This includes permission to view the delegated administrator accounts.

`AWSTrustedAdvisorPriorityReadOnlyAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSTrustedAdvisorPriorityReadOnlyAccess-how-to-use"></a>

You can attach `AWSTrustedAdvisorPriorityReadOnlyAccess` to your users, groups, and roles.

## Policy details
<a name="AWSTrustedAdvisorPriorityReadOnlyAccess-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: August 16, 2022, 16:35 UTC 
+ **Edited time:** August 16, 2022, 16:35 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWSTrustedAdvisorPriorityReadOnlyAccess`

## Policy version
<a name="AWSTrustedAdvisorPriorityReadOnlyAccess-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSTrustedAdvisorPriorityReadOnlyAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "trustedadvisor:DescribeAccount*",
        "trustedadvisor:DescribeOrganization",
        "trustedadvisor:DescribeRisk*",
        "trustedadvisor:DownloadRisk",
        "trustedadvisor:DescribeNotificationConfigurations"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "organizations:DescribeOrganization",
        "organizations:ListAWSServiceAccessForOrganization"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListDelegatedAdministrators"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "organizations:ServicePrincipal" : [
            "reporting.trustedadvisor.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSTrustedAdvisorPriorityReadOnlyAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
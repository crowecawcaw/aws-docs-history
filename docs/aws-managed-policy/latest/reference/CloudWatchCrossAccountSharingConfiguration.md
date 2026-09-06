

# CloudWatchCrossAccountSharingConfiguration
<a name="CloudWatchCrossAccountSharingConfiguration"></a>

**Description**: Provides capabilities to manage Observability Access Manager links and establish sharing of CloudWatch resources

`CloudWatchCrossAccountSharingConfiguration` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CloudWatchCrossAccountSharingConfiguration-how-to-use"></a>

You can attach `CloudWatchCrossAccountSharingConfiguration` to your users, groups, and roles.

## Policy details
<a name="CloudWatchCrossAccountSharingConfiguration-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 27, 2022, 14:01 UTC 
+ **Edited time:** November 27, 2022, 14:01 UTC
+ **ARN**: `arn:aws:iam::aws:policy/CloudWatchCrossAccountSharingConfiguration`

## Policy version
<a name="CloudWatchCrossAccountSharingConfiguration-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CloudWatchCrossAccountSharingConfiguration-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "cloudwatch:Link",
        "oam:ListLinks"
      ],
      "Resource" : "*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "oam:DeleteLink",
        "oam:GetLink",
        "oam:TagResource"
      ],
      "Resource" : "arn:aws:oam:*:*:link/*"
    },
    {
      "Effect" : "Allow",
      "Action" : [
        "oam:CreateLink",
        "oam:UpdateLink"
      ],
      "Resource" : [
        "arn:aws:oam:*:*:link/*",
        "arn:aws:oam:*:*:sink/*"
      ]
    }
  ]
}
```

## Learn more
<a name="CloudWatchCrossAccountSharingConfiguration-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
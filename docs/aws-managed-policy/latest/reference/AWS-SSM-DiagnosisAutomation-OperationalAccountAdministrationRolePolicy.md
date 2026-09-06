

# AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy
<a name="AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy"></a>

**Description**: Provides permissions for operational accounts to diagnose unmanaged nodes by providing Organisation specific permissions required by SSM automation to pull the list of member accounts within a root of an Organisation to trigger cross-account cross-region execution by allowing assuming Execution roles in target account/region.

`AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy-how-to-use"></a>

You can attach `AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy-details"></a>
+ **Type**: AWS managed policy 
+ **Creation time**: November 16, 2024, 00:11 UTC 
+ **Edited time:** November 16, 2024, 00:11 UTC
+ **ARN**: `arn:aws:iam::aws:policy/AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy`

## Policy version
<a name="AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowReadOnlyAccessOrganization",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListRoots",
        "organizations:ListChildren"
      ],
      "Resource" : "*"
    },
    {
      "Sid" : "AllowAssumeDiagnosisExecutionRoleWithinOrg",
      "Effect" : "Allow",
      "Action" : "sts:AssumeRole",
      "Resource" : "arn:aws:iam::*:role/AWS-SSM-DiagnosisExecutionRole*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceOrgId" : "${aws:PrincipalOrgId}"
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
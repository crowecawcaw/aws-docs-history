

# AWSIPAMOutboundServiceRolePolicy
<a name="AWSIPAMOutboundServiceRolePolicy"></a>

**Description**: Grants permissions to request web identity tokens for outbound federation

`AWSIPAMOutboundServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AWSIPAMOutboundServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="AWSIPAMOutboundServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: October 28, 2026, 15:07 UTC 
+ **Edited time:** October 28, 2026, 15:07 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/AWSIPAMOutboundServiceRolePolicy`

## Policy version
<a name="AWSIPAMOutboundServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AWSIPAMOutboundServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowGetWebIdentityTokenForAzure",
      "Effect" : "Allow",
      "Action" : "sts:GetWebIdentityToken",
      "Resource" : "*",
      "Condition" : {
        "Null" : {
          "sts:IdentityTokenAudience" : "false"
        },
        "ForAllValues:StringLike" : {
          "sts:IdentityTokenAudience" : [
            "api://AzureADTokenExchange"
          ]
        }
      }
    },
    {
      "Sid" : "AllowGetWebIdentityTokenForGcp",
      "Effect" : "Allow",
      "Action" : "sts:GetWebIdentityToken",
      "Resource" : "*",
      "Condition" : {
        "Null" : {
          "sts:IdentityTokenAudience" : "false"
        },
        "ForAllValues:StringLike" : {
          "sts:IdentityTokenAudience" : [
            "//iam.googleapis.com/projects/*/locations/*/workloadIdentityPools/*/providers/*"
          ]
        }
      }
    }
  ]
}
```

## Learn more
<a name="AWSIPAMOutboundServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)


# GreengrassOTAUpdateArtifactAccess
<a name="GreengrassOTAUpdateArtifactAccess"></a>

**Description**: Provides read access to the Greengrass OTA Update artifacts in all Greengrass regions

`GreengrassOTAUpdateArtifactAccess` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="GreengrassOTAUpdateArtifactAccess-how-to-use"></a>

You can attach `GreengrassOTAUpdateArtifactAccess` to your users, groups, and roles.

## Policy details
<a name="GreengrassOTAUpdateArtifactAccess-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: November 29, 2017, 18:11 UTC 
+ **Edited time:** December 18, 2018, 00:59 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/GreengrassOTAUpdateArtifactAccess`

## Policy version
<a name="GreengrassOTAUpdateArtifactAccess-version"></a>

**Policy version:** v2 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="GreengrassOTAUpdateArtifactAccess-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "AllowsIotToAccessGreengrassOTAUpdateArtifacts",
      "Effect" : "Allow",
      "Action" : [
        "s3:GetObject"
      ],
      "Resource" : [
        "arn:aws:s3:::*-greengrass-updates/*"
      ]
    }
  ]
}
```

## Learn more
<a name="GreengrassOTAUpdateArtifactAccess-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
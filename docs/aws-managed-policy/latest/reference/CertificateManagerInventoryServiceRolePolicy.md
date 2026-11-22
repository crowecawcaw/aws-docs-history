

# CertificateManagerInventoryServiceRolePolicy

**Description**: Allows AWS Certificate Manager to read certificate, AWS Private CA, and AWS Organizations data in your account for organization-wide certificate inventory, and to manage the AWS Config service-linked recorder it uses to collect that data, and to create AWS Config's service-linked role.

`CertificateManagerInventoryServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="CertificateManagerInventoryServiceRolePolicy-how-to-use"></a>

This policy is attached to a service-linked role that allows the service to perform actions on your behalf. You cannot attach this policy to your users, groups, or roles.

## Policy details
<a name="CertificateManagerInventoryServiceRolePolicy-details"></a>
+ **Type**: Service-linked role policy 
+ **Creation time**: November 19, 2026, 20:47 UTC 
+ **Edited time:** November 19, 2026, 20:47 UTC
+ **ARN**: `arn:aws:iam::aws:policy/aws-service-role/CertificateManagerInventoryServiceRolePolicy`

## Policy version
<a name="CertificateManagerInventoryServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="CertificateManagerInventoryServiceRolePolicy-json"></a>

```json
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Sid" : "ManageServiceLinkedConfigurationRecorder",
      "Effect" : "Allow",
      "Action" : [
        "config:PutServiceLinkedConfigurationRecorder",
        "config:DeleteServiceLinkedConfigurationRecorder"
      ],
      "Resource" : "arn:aws:config:*:*:configuration-recorder/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}",
          "config:ConfigurationRecorderServicePrincipal" : "inventory.acm.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "CreateConfigServiceLinkedRole",
      "Effect" : "Allow",
      "Action" : "iam:CreateServiceLinkedRole",
      "Resource" : "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig",
      "Condition" : {
        "StringEquals" : {
          "iam:AWSServiceName" : "config.amazonaws.com"
        }
      }
    },
    {
      "Sid" : "ListEnabledRegions",
      "Effect" : "Allow",
      "Action" : "account:ListRegions",
      "Resource" : "arn:aws:account::*:account",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ReadACMCertificateMetadata",
      "Effect" : "Allow",
      "Action" : [
        "acm:GetCertificate",
        "acm:DescribeCertificate"
      ],
      "Resource" : "arn:aws:acm:*:*:certificate/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ListAndSearchACMCertificates",
      "Effect" : "Allow",
      "Action" : [
        "acm:ListCertificates",
        "acm:SearchCertificates"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ReadPrivateCertificateAuthorityCertificate",
      "Effect" : "Allow",
      "Action" : [
        "acm-pca:GetCertificateAuthorityCertificate",
        "acm-pca:DescribeCertificateAuthority"
      ],
      "Resource" : "arn:aws:acm-pca:*:*:certificate-authority/*",
      "Condition" : {
        "StringEquals" : {
          "aws:ResourceAccount" : "${aws:PrincipalAccount}"
        }
      }
    },
    {
      "Sid" : "ReadOrganizationAccount",
      "Effect" : "Allow",
      "Action" : "organizations:DescribeAccount",
      "Resource" : "arn:aws:organizations::*:account/o-*/*"
    },
    {
      "Sid" : "ReadOrganizationStructure",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListChildren",
        "organizations:ListParents"
      ],
      "Resource" : [
        "arn:aws:organizations::*:root/o-*/r-*",
        "arn:aws:organizations::*:ou/o-*/ou-*",
        "arn:aws:organizations::*:account/o-*/*"
      ]
    },
    {
      "Sid" : "ReadOrganizationData",
      "Effect" : "Allow",
      "Action" : [
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:DescribeOrganization",
        "organizations:ListAccounts",
        "organizations:ListRoots",
        "organizations:ListDelegatedAdministrators"
      ],
      "Resource" : "*"
    }
  ]
}
```

## Learn more
<a name="CertificateManagerInventoryServiceRolePolicy-learn-more"></a>
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)
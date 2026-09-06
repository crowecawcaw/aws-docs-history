

# AWS managed policies for IAM Roles Anywhere
<a name="security-iam-awsmanpol"></a>





An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.









## AWS managed policy: AWSRolesAnywhereServicePolicy
<a name="security-iam-awsmanpol-AWSServiceRoleForRolesAnywhere"></a>

 AWSRolesAnywhereServicePolicy provides the required permissions to publish metrics data to CloudWatch namespaces (`AWS/RolesAnywhere` and `AWS/Usage`).  This policy also grants permissions to list information about your private certificate authority (CA) and retrieve the certificate and certificate chain for your private CA from AWS Private CA. 

 You can't attach AWSRolesAnywhereServicePolicy to your IAM entities. This policy is attached to a service-linked role that allows IAM Roles Anywhere to perform actions on your behalf. For more information, see [ Service-linked role permissions for IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/using-service-linked-roles.html#slr-permissions). 



 This policy grants administrative permissions that allow IAM Roles Anywhere to publish CloudWatch metrics  and check the configuration of AWS Private CA.

**Permissions details**

This policy includes the following permissions.
+ `cloudwatch` – Allows principals to publish metric data points to the `AWS/RolesAnywhere` and `AWS/Usage` namespaces.
+ `acm-pca` – Allows principals to list information about your private certificate authority (CA) and retrieve the certificate and certificate chain for your private CA from AWS Private CA.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "cloudwatch:PutMetricData"
        ],
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "cloudwatch:namespace": [
              "AWS/RolesAnywhere",
              "AWS/Usage"
            ]
          }
        }
      },
      {
        "Effect": "Allow",
        "Action": [
          "acm-pca:GetCertificateAuthorityCertificate",
          "acm-pca:DescribeCertificateAuthority"
        ],
        "Resource": "arn:aws:acm-pca:*:*:*"
      }
    ]
  }
```

------

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "cloudwatch:PutMetricData"
        ],
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "cloudwatch:namespace": [
              "AWS/RolesAnywhere",
              "AWS/Usage"
            ]
          }
        }
      }
    ]
  }
```

------

For more information and definition of this policy, see: [AWSRolesAnywhereServicePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSRolesAnywhereServicePolicy.html).

## AWS managed policy: AWSRolesAnywhereFullAccess
<a name="security-iam-awsmanpol-AWSRolesAnywhereFullAccess"></a>

 This policy provides all permissions to IAM Roles Anywhere resources, including but not limited to: CreateProfile, DeleteTrustAnchor, DisableCRL, ResetNotificationSettings. 

 You can attach the AWSRolesAnywhereFullAccess policy to your IAM identities. 

 This policy grants full access permissions that allow users to view, create, update, and delete all IAM Roles Anywhere resources. 

**Permissions details**

This policy includes the following permissions:
+ `rolesanywhere` – Allows principals to perform all actions on IAM Roles Anywhere resources including trust anchors, profiles, CRLs, subjects, and notification settings.
+ `iam:PassRole` – Allows principals to pass a role to IAM Roles Anywhere.
+ `iam:CreateServiceLinkedRole` – Allows principals to create the service-linked role for IAM Roles Anywhere. This permission is needed when the service-linked role doesn't exist in the account yet.

For more information and definition of this policy, see [AWSRolesAnywhereFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSRolesAnywhereFullAccess.html).

## AWS managed policy: AWSRolesAnywhereReadOnly
<a name="security-iam-awsmanpol-AWSRolesAnywhereReadOnly"></a>

 This policy provides read-only permissions to IAM Roles Anywhere resources, including but not limited to: GetTrustAnchor, ListProfiles, GetCRL. 

 You can attach the AWSRolesAnywhereReadOnly policy to your IAM identities. 

 This policy grants read-only permissions that allow users to view IAM Roles Anywhere resources but not modify them. 

**Permissions details**

This policy includes the following permissions:
+ `rolesanywhere` – Allows principals to view all IAM Roles Anywhere resources including trust anchors, profiles, CRLs, and subjects.

For more information and definition of this policy, see [AWSRolesAnywhereReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSRolesAnywhereReadOnly.html).





## IAM Roles Anywhere updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for IAM Roles Anywhere since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the IAM Roles Anywhere [ Document history](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/doc-history.html) page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AWSRolesAnywhereFullAccess](#security-iam-awsmanpol-AWSRolesAnywhereFullAccess) – New policy | IAM Roles Anywhere added a new policy to allow users to grant full access IAM Roles Anywhere permissions to principals in a standardized way. | July 16, 2025 | 
| [AWSRolesAnywhereReadOnly](#security-iam-awsmanpol-AWSRolesAnywhereReadOnly) – New policy | IAM Roles Anywhere added a new policy to allow users to grant read only IAM Roles Anywhere permissions to principals in a standardized way. | July 16, 2025 | 
| IAM Roles Anywhere started tracking changes | IAM Roles Anywhere started tracking changes for its AWS managed policies. | February 27, 2023 | 
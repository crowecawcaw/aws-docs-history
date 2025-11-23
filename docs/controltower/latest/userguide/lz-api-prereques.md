# Step 1: Configure your landing zone

The process of setting up your AWS Control Tower landing zone has multiple steps. Certain aspects of your AWS Control Tower landing zone are configurable,
but other choices cannot be changed after setup. To learn more about these important considerations prior to launching your landing zone,
review [Expectations for landing zone configuration](getting-started-configure.md "getting-started-configure.md").

Before using the AWS Control Tower landing zone APIs, you must first call APIs from other AWS services to configure your landing zone prior to
launch. The process includes three main steps:

1. creating a new AWS Organizations organization,
2. setting up your service integration accounts,
3. and creating an IAM role or IAM Identity Center user with the required permissions to call the landing zone APIs.

## Step 1. Create the organization that will contain your landing zone:

Call the AWS Organizations `CreateOrganization` API and enable all features to create the **Foundational OU**. AWS Control Tower
also recommends creating a designated **Security OU**. This Security OU should contain all of your service integration accounts.
These would be the **log archive** account and the **audit** account for previous Landing Zone versions.

```

aws organizations create-organization --feature-set ALL

```

AWS Control Tower can set up one or more **Additional OUs**. We recommend that you provision at least one Additional OU in your
landing zone, besides the Security OU. If this Additional OU is intended for development projects, we recommend that you name it the **Sandbox OU**,
as given in the [AWS multi-account strategy for your AWS Control Tower landing zone](aws-multi-account-landing-zone.md "aws-multi-account-landing-zone.md").

## Step 2. Provision service integration accounts if needed:

To set up your landing zone, AWS Control Tower allows customers to configure AWS service integrations. Each of these service integrations may require one or more service integration central accounts.
If you are using landing zone APIs to set up AWS Control Tower for the first time, you must provide the central integration account for each enabled AWS service integration.
You can use existing AWS accounts or provision these accounts through the AWS Control Tower console or AWS Organizations APIs.
**Ensure these service integration accounts are in the designated Security OU that is at the root level in your organization.**

1. Call the AWS Organizations `CreateAccount` API to create the **Log archive** account and **Audit** account in the **Security OU**.

```

                            aws organizations create-account --email mylog@example.com --account-name "Logging Account"
                            aws organizations create-account --email mysecurity@example.com --account-name "Security Account"

```

(Optional) Check the status of the `CreateAccount` operation using the AWS Organizations `DescribeAccount` API. 2. Move the provisioned service integration accounts into the designated **Security OU**

```

                            aws organizations move-account --account-id 0123456789012 --source-parent-id r-examplerootid111 --destination-parent-id ou-examplerootid111-security

```

## Step 3. Create the required service roles

Create the following IAM service roles in the `/service-role/` IAM path that enable AWS Control Tower to perform the API calls required to set up your landing zone:

- [`AWSControlTowerAdmin`](access-control-managing-permissions.md#AWSControlTowerAdmin "access-control-managing-permissions.md#AWSControlTowerAdmin")
- [`AWSControlTowerCloudTrailRole`](access-control-managing-permissions.md#AWSControlTowerCloudTrailRole "access-control-managing-permissions.md#AWSControlTowerCloudTrailRole")
- [`AWSControlTowerStackSetRole`](access-control-managing-permissions.md#AWSControlTowerStackSetRole "access-control-managing-permissions.md#AWSControlTowerStackSetRole")
- [`AWSControlTowerConfigAggregatorRoleForOrganizations`](roles-how.md#config-role-for-organizations "roles-how.md#config-role-for-organizations")

For more information about these roles and their policies, see
[Using identity-based policies (IAM
policies) for AWS Control Tower](access-control-managing-permissions.md "access-control-managing-permissions.md").

### To create an IAM role:

Create an IAM role with the necessary permissions to call all landing zone APIs. Alternatively, you can create an IAM
Identity Center user and assign the necessary permissions.

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "backup:UpdateGlobalSettings",
                "controltower:CreateLandingZone",
                "controltower:UpdateLandingZone",
                "controltower:ResetLandingZone",
                "controltower:DeleteLandingZone",
                "controltower:GetLandingZoneOperation",
                "controltower:GetLandingZone",
                "controltower:ListLandingZones",
                "controltower:ListLandingZoneOperations",
                "controltower:ListTagsForResource",
                "controltower:TagResource",
                "controltower:UntagResource",
                "servicecatalog:*",
                "organizations:*",
                "organizations:RegisterDelegatedAdministrator",
                "organizations:EnableAWSServiceAccess",
                "organizations:DeregisterDelegatedAdministrator",
                "organizations:ListDelegatedAdministrators",
                "sso:*",
                "sso-directory:*",
                "logs:*",
                "cloudformation:*",
                "kms:*",
                "iam:GetRole",
                "iam:CreateRole",
                "iam:GetSAMLProvider",
                "iam:CreateSAMLProvider",
                "iam:CreateServiceLinkedRole",
                "iam:ListRolePolicies",
                "iam:PutRolePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:AttachRolePolicy",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy"
            ],
            "Resource": "*"
        }
    ]
}

```

###### Note

When upgrading to landing zone version 4.0 with AWS Config integration enabled, customers need to have `organizations:ListDelegatedAdministrators` permissions.

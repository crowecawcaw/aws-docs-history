

# Getting started with account access manager
<a name="account-access-manager-getting-started"></a>

The following outlines how you can get started with account access manager. This assumes the IAM roles you want to assign already exist in their respective AWS accounts. If these roles do not exist, see [Create a role using custom trust policies](id_roles_create_for-custom.md) for information about how to create new roles.

**To get started with account access manager**

1. Make sure you have an organization instance of IAM Identity Center enabled and your workforce users and groups provisioned there. See the [Getting started with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) section in the AWS IAM Identity Center User Guide for more information. See [Prerequisites and considerations](#aam-prerequisites-and-considerations) later in this topic for more details.
**Note**  
If you are using IAM Identity Center replicated to multiple AWS Regions or with a customer managed key (CMK), you must add `kms:Decrypt` permission for account access manager to use this CMK when connecting to IAM Identity Center. For more information, see [Baseline KMS key policy](https://docs.aws.amazon.com/singlesignon/latest/userguide/baseline-KMS-key-policy.html) in the *AWS IAM Identity Center User Guide*.

1. Make sure you have permissions to enable account access manager and manage account assignments in it. For more information, see [Identity and access management for account access manager](aam-security.md#aam-security-iam).

1. [Enable account access manager](#enable-aam) through the console or API.

1. [Update your firewalls and gateways](#aam-update-firewalls-and-gateways) for access to the account access portal.

1. [Grant account access manager access to IAM roles](aam-prepare-roles.md#aam-identify-and-update-roles) by updating their trust policy.

1. [Start assigning account access](aam-assign-remove-access.md#aam-assign-account-access) to your workforce users and groups from IAM Identity Center.

1. [Let your users know how to access AWS accounts](aam-get-started-with-aam-portal.md#aam-workforce-access-communicate-to-users) using account access manager role assignments.

## Prerequisites and considerations
<a name="aam-prerequisites-and-considerations"></a>

The following prerequisites and considerations apply:
+ Account access manager is available in AWS Commercial Regions enabled by default. Opt-in Commercial Regions, GovCloud (US), China, and other non-commercial Regions are not supported.
+ At enablement, account access manager connects to a single organization instance of IAM Identity Center. You must enable an AWS organization and an organization instance of IAM Identity Center beforehand. Account instances of IAM Identity Center are not supported.
+ We recommend enabling account access manager in the same AWS Region where you enabled your IAM Identity Center instance. If you haven't done it already, see [Considerations for choosing an AWS Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-region-considerations.html) in the AWS IAM Identity Center User Guide.
+ Both the organization instance of IAM Identity Center and account access manager must be enabled in your organization's management account.

## Enable account access manager
<a name="enable-aam"></a>

After creating an organization instance of IAM Identity Center, you can enable account access manager through its console or API. You must do this in the same AWS account and Region as your IAM Identity Center instance.

Before enabling account access manager, run the following command from the AWS organization management account to grant account access manager access to your organization:

```
aws organizations enable-aws-service-access --service-principal account-access.amazonaws.com
```

**Note**  
While the account access manager console is part of the IAM console, its API lives in a separate namespace.

Use one of the following methods to enable account access manager:

------
#### [ Console ]

**To enable account access manager**

1. Sign in to your organization's management account.

1. In the AWS Identity and Access Management console navigation pane, choose **Account access manager**.

1. Confirm the console Region is set to the primary Region of your IAM Identity Center instance.

1. If there is no organization instance of IAM Identity Center, you will be prompted to enable one now before continuing. Otherwise, choose **Enable account access manager**.

------
#### [ AWS CLI ]

First find the ARN of the IAM Identity Center instance and confirm the Region code matches the primary Region of IAM Identity Center. Then, run the following command:

```
aws account-access create-application \
  --region <Region> \
  --identity-source '{
    "identityCenter": {
      "instanceArn": "<IAM_IDENTITY_CENTER_INSTANCE_ARN>"
    }
  }'
```

------

## Update firewalls and gateways
<a name="aam-update-firewalls-and-gateways"></a>

The account access portal provides your users with single sign-on access to the AWS accounts assigned to them through account access manager.

If you filter access to specific AWS domains or URL endpoints by using a web content filtering solution such as next-generation firewalls (NGFW) or Secure Web Gateways (SWG), you must allowlist the domains and URL endpoints associated with the account access portal.

The following list provides the dual-stack domains and URL endpoints to add to your web-content filtering solution allowlists. Account access manager has no IPv4-only endpoints.

**Dual-stack allow list**

The account access portal URL:
+ `https://[Tenant-ID].account-access.[Region].app.aws`

The APIs that the account access portal calls:
+ `[Tenant-ID].account-access.[Region].app.aws/api/*`
+ `[Tenant-ID].account-access.[Region].app.aws/auth/*`

Tenant-ID is a unique random identifier associated with account access manager. To find its value, navigate to the **Settings** tab in the account access manager console, and look up the **Application URL** in the **Instance details** section. Tenant-ID is the first subdomain in the URL.

The account access manager service endpoints:
+ Control-plane: `account-access.[Region].api.aws`
+ Runtime: `account-access-runtime.[Region].api.aws`
+ Console: `console.aws.amazon.com/account-access`

If you use the AWS CLI, you can find the tenant ID by running the following CLI command in your organization's management or delegated administrator account.

```
aws account-access list-applications
```

The response contains information about account access manager including the application ARN and the tenant ID.

```
{
    "applications": [
        {
            "applicationArn": "arn:aws:account-access:us-west-2:123456789012:application/1234567890abcdef",
            "tenantId": "aa-gyxmap389",
            "createdAt": "2026-03-27T18:31:19+00:00",
            "updatedAt": "2026-03-27T18:31:19+00:00"
        }
    ]
}
```

### Considerations for allowlisting domains and URL endpoints
<a name="aam-allowlisting-considerations"></a>

In addition to the allowlist requirements for the account access portal, the other services and applications you use might require allowlisting of domains.
+ You need to allowlist the AWS access portal and its dependencies. For more information, see [Updating firewalls and gateways to allow access to the AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-identity-center-portal-access.html) in the AWS IAM Identity Center User Guide.
+ To access AWS accounts, the AWS Management Console, and the account access manager console, you must allowlist additional domains. Refer to [Troubleshooting](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/troubleshooting.html) in the *AWS Management Console Getting Started Guide* for a list of AWS Management Console domains.

## Delete account access manager
<a name="aam-delete-instance"></a>

When account access manager is deleted, all the data in it is deleted and cannot be recovered.

Use the following procedure to delete account access manager.

------
#### [ Console ]

**To delete your account access manager instance**

1. Sign in to your organization's management account.

1. In the AWS Identity and Access Management console navigation pane, choose **Account access manager**.

1. Confirm the console Region is set to the primary Region of your account access manager instance.

1. Choose the **Settings** tab.

1. In the **Delete account access manager** section, choose **Delete**.

1. The dialog box prompts you to confirm. When ready, choose **Delete**.

------
#### [ AWS CLI ]

Run the following command to delete account access manager:

```
aws account-access delete-application \
  --region "<Region>" \
  --application-arn "<account_access_manager_ARN>"
```

------

**Warning**  
Deleting account access manager is irreversible and has the following consequences:  
All role assignments are permanently removed. Your users immediately lose the ability to access AWS accounts with IAM roles assigned through account access manager.
Account access manager is removed from the AWS access portal for all users.
Active sessions of IAM roles assigned through account access manager continue until they expire, but users cannot start new sessions.
If you re-enable account access manager later, you must recreate all assignments from scratch. Previous assignments are not recoverable.
Before deleting, consider disabling user access in individual accounts to temporarily restrict access.
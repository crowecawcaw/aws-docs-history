

# Getting started with the account access portal
<a name="aam-get-started-with-aam-portal"></a>

## Finding the account access portal URL
<a name="aam-find-aam-portal-url"></a>

To find the account access portal URL, choose the **Settings** tab in the account access manager console. Look up the **Application URL** in the **Instance details** section. The URL follows the pattern `https://[Tenant-ID].account-access.[Region].app.aws`. Tenant-ID is a unique random identifier associated with account access manager.

If you use the AWS CLI, you can find the tenant ID by running the following CLI command in your organization's management or delegated administrator account.

```
aws account-access list-applications
```

The response contains information about account access manager including the application ARN and the tenant ID. Use the tenant ID and the Region code of account access manager to construct the application URL. Follow the pattern provided earlier in this section.

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

## Setting up a vanity portal URL
<a name="aam-vanity-portal-url-setup"></a>

For instructions on implementing custom vanity domains, see [Regional routing for AWS access portals: Implementing custom vanity domains for IAM Identity Center](https://aws.amazon.com/blogs/security/regional-routing-for-aws-access-portals-implementing-custom-vanity-domains-for-iam-identity-center/) on the AWS Security Blog. You can adapt these instructions to the URL pattern of the account access portal.

## Communicating with your users
<a name="aam-workforce-access-communicate-to-users"></a>

Communicate the following to your workforce users:
+ The account access portal URL.
+ The account access portal is available to your users also as an application in the **Applications** tab in the AWS access portal.
+ If you enabled launching the account access portal from an external identity provider portal or another portal outside AWS, include this information in the communication.
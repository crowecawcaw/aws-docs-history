# Creating an organization with AWS Organizations

You can create an organization with your AWS account as the management
account. When you create an organization, you can choose whether the organization supports
[all features (recommended)](orgs_getting-started_concepts.md#feature-set-all "orgs_getting-started_concepts.md#feature-set-all") or only [consolidated billing](orgs_getting-started_concepts.md#feature-set-cb-only "orgs_getting-started_concepts.md#feature-set-cb-only"). By default, an organization you create supports all features.

## Create an organization

You can create an organization by using either the AWS Management Console or by using a command
from the AWS CLI or one of the SDK APIs.

###### Minimum permissions

To create an organization with your current AWS account, you must have the
following permissions:

- `organizations:CreateOrganization`
- `iam:CreateServiceLinkedRole`

You can restrict this permission to only the service principal
`organizations.amazonaws.com`.

###### To create an organization

1.  Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
    sign in as the root user ([not
    recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2.  By default, the organization is created with all features enabled.
    However, you can choose either of the following steps:

        * To create an organization with all features enabled, on
         the introduction page, choose **Create an
         organization**.
        * To create an organization with Consolidated Billing
         features only, on the introduction page and under
         **Create an organization**, choose
         **consolidated billing features**, and
         then in the confirmation dialog box, choose **Create
         an organization**.

    If you accidentally choose the wrong option, you can immediately
    go to the **[Settings](https://console.aws.amazon.com/organizations/v2/home/settings "https://console.aws.amazon.com/organizations/v2/home/settings")** page, and then choose **Delete
    organization** and start over.

3.  The organization is created and the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page appears. The
    only account present is your management account, and it's currently
    stored in the [root organizational unit
    (OU)](orgs_getting-started_concepts.md#root "orgs_getting-started_concepts.md#root").

If required, Organizations automatically sends a verification email to the
address that is associated with your management account. There might
be a delay before you receive the verification email. Verify your
email address within 24 hours. For more information, see [Email address verification with AWS Organizations](about-email-verification.md "about-email-verification.md"). You can create
accounts to grow your organization without verifying your management
account's email address. However, to invite existing accounts, you
must first complete email verification.

###### Note

If this account previously verified its email address, then it
doesn't happen again when you use the account to create an
organization.

The following code examples show how to use `CreateOrganization`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Organizations#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.Organizations;
    using Amazon.Organizations.Model;

    /// <summary>
    /// Creates an organization in AWS Organizations.
    /// </summary>
    public class CreateOrganization
    {
        /// <summary>
        /// Creates an Organizations client object and then uses it to create
        /// a new organization with the default user as the administrator, and
        /// then displays information about the new organization.
        /// </summary>
        public static async Task Main()
        {
            IAmazonOrganizations client = new AmazonOrganizationsClient();

            var response = await client.CreateOrganizationAsync(new CreateOrganizationRequest
            {
                FeatureSet = "ALL",
            });

            Organization newOrg = response.Organization;

            Console.WriteLine($"Organization: {newOrg.Id} Main Accoount: {newOrg.MasterAccountId}");
        }
    }



```

- For API details, see
  [CreateOrganization](../../../goto/DotNetSDKV3/organizations-2016-11-28/CreateOrganization.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/CreateOrganization.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**Example 1: To create a new organization**

Bill wants to create an organization using credentials from account 111111111111. The following example shows that the account becomes the master account in the new organization. Because he does not specify a features set, the new organization defaults to all features enabled and service control policies are enabled on the root.

```
`aws organizations create-organization`

```

The output includes an organization object with details about the new organization:

```
{
        "Organization": {
                "AvailablePolicyTypes": [
                        {
                                "Status": "ENABLED",
                                "Type": "SERVICE_CONTROL_POLICY"
                        }
                ],
                "MasterAccountId": "111111111111",
                "MasterAccountArn": "arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111",
                "MasterAccountEmail": "bill@example.com",
                "FeatureSet": "ALL",
                "Id": "o-exampleorgid",
                "Arn": "arn:aws:organizations::111111111111:organization/o-exampleorgid"
        }
}
```

**Example 2: To create a new organization with only consolidated billing features enabled**

The following example creates an organization that supports only the consolidated billing features:

```
`aws organizations create-organization --feature-set `CONSOLIDATED_BILLING``

```

The output includes an organization object with details about the new organization:

```
{
        "Organization": {
                "Arn": "arn:aws:organizations::111111111111:organization/o-exampleorgid",
                "AvailablePolicyTypes": [],
                "Id": "o-exampleorgid",
                "MasterAccountArn": "arn:aws:organizations::111111111111:account/o-exampleorgid/111111111111",
                "MasterAccountEmail": "bill@example.com",
                "MasterAccountId": "111111111111",
                "FeatureSet": "CONSOLIDATED_BILLING"
        }
}
```

For more information, see Creating an Organization in the _AWS Organizations Users Guide_.

- For API details, see
  [CreateOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-organization.html")
  in _AWS CLI Command Reference_.

After you have created an organization, you can add accounts to your organization in these ways
from the management account:

- [Create other AWS accounts](orgs_manage_accounts_create.md "orgs_manage_accounts_create.md")
  that are automatically added to your organization as member accounts
- After [verifying your email address](about-email-verification.md "about-email-verification.md"), [invite existing
  AWS accounts](orgs_manage_accounts_invite-account.md "orgs_manage_accounts_invite-account.md") to join your organization as member accounts.

# Creating a member account in an organization

with AWS Organizations

This topic describes how to create AWS accounts within your organization in AWS Organizations.
For information about creating a single AWS account, see the [Getting Started Resource Center](https://aws.amazon.com/getting-started/ "https://aws.amazon.com/getting-started/").

## Considerations before

creating a member account

**Organizations automatically creates the IAM role
`OrganizationAccountAccessRole` for the member
account**

When you create a member account in your organization, Organizations automatically creates the
IAM role `OrganizationAccountAccessRole` in the member account that enables
users and roles in the management account to exercise full administrative control over
the member account. Any additional accounts attached to the same managed policy will be
updated automatically whenever the policy gets updated. This role is subject to any
[service control policies (SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md")
that apply to the member account.

**Organizations automatically creates the service-linked role
`AWSServiceRoleForOrganizations` for the member account**

When you create a member account in your organization, Organizations automatically creates
service-linked role `AWSServiceRoleForOrganizations` in the member account that enables
integration with select AWS services. You must configure the other services to allow
the integration. For more information, see [AWS Organizations and service-linked
roles](orgs_integrate_services.md#orgs_integrate_services-using_slrs "orgs_integrate_services.md#orgs_integrate_services-using_slrs").

**Member accounts can only be created in the root of an
organization**

Member accounts in an organization can only be created in the root of an organization.
After you create a member account root of an organization, you can move it between OUs.
For more information, see [Moving accounts to an organizational unit (OU) or between the root and
OUs with AWS Organizations](move_account_to_ou.md "move_account_to_ou.md").

**Policies attached to the root immediately
apply**

If you have any policies attached to the root, those policies immediately apply to all
users and roles in the created account.

If you have [enabled service trust for
another AWS service](orgs_integrate_services_list.md "orgs_integrate_services_list.md") for your organization, that trusted service can create
service-linked roles or perform actions in any member account in the organization,
including your created account.

**Member accounts must opt in to receive marketing emails**

Member accounts that you create as part of an organization are not automatically
subscribed to AWS marketing emails. To opt-in your accounts to receive marketing
emails, see [https://pages.awscloud.com/communication-preferences](https://pages.awscloud.com/communication-preferences "https://pages.awscloud.com/communication-preferences").

**Member accounts for organizations managed by AWS Control Tower should be created in
AWS Control Tower**

If your organization is managed by AWS Control Tower, we recommend that you create your
member accounts using the AWS Control Tower account factory in the AWS Control Tower console or using the
AWS Control Tower APIs.

If you create an member account in Organizations when the organization is managed by AWS Control Tower,
the account won't be enrolled with AWS Control Tower. For more information, see [Referring to Resources Outside of AWS Control Tower](../../../controltower/latest/userguide/external-resources.md#ungoverned-resources "../../../controltower/latest/userguide/external-resources.md#ungoverned-resources") in the _AWS Control Tower User
Guide_.

## Create a member account

After you sign in to the organization's management account, you can create member
accounts that are part of your organization.

When you create an account using the following procedure, AWS Organizations automatically
copies the following **Primary contact** information from the
management account to the new member account:

- Phone number
- Company name
- Website URL
- Address

Organizations also copies the communication language and Marketplace information (vendor of the
account in some AWS Regions) from the management account.

###### Minimum permissions

To create a member account in your organization, you must have the following
permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:CreateAccount`

###### To create an AWS account that is automatically part of your

organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, choose **Add an
   AWS account**.
3. On the **[Add an AWS account](https://console.aws.amazon.com/organizations/v2/home/accounts/add/create "https://console.aws.amazon.com/organizations/v2/home/accounts/add/create")** page, choose **Create an
   AWS account** (it is chosen by default).
4. On the **[Create an AWS account](https://console.aws.amazon.com/organizations/v2/home/accounts/add/create "https://console.aws.amazon.com/organizations/v2/home/accounts/add/create")** page, for **AWS account
   name** enter the name that you want to assign to the
   account. This name helps you distinguish the account from all other
   accounts in the organization and is separate from the IAM alias or the
   email name of the owner.
5. For **Email address of the account's owner**, enter
   the email address of the account's owner. This email address cannot
   already be associated with another AWS account because it becomes the
   user name credential for the root user of the account.
6. (Optional) Specify the name to assign to the IAM role that is
   automatically created in the new account. This role grants the
   organization's management account permission to access the newly created
   member account. If you don't specify a name, AWS Organizations gives the role a
   default name of `OrganizationAccountAccessRole`. We recommend
   that you use the default name across all of your accounts for
   consistency.

###### Important

Remember this role name. You need it later to grant access to the
new account for users and roles in the management account. 7. (Optional) In the **Tags** section, add one or more
tags to the new account by choosing **Add tag** and
then entering a key and an optional value. Leaving the value blank sets
it to an empty string; it isn't `null`. You can attach up to
50 tags to an account. 8. Choose **Create AWS account**.

    * If you get an error that indicates that you exceeded your
     account quota for the organization, see [I get a "quota exceeded"
     message when I try to add an account to my organization](orgs_troubleshoot.md#troubleshoot_general_error-adding-account "orgs_troubleshoot.md#troubleshoot_general_error-adding-account").
    * If you get an error that indicates that you can't add an
     account because your organization is still initializing, wait
     one hour and try again.
    * You can also check the AWS CloudTrail log for information on whether
     the account creation was successful. For more information, see
     [Logging and monitoring in AWS Organizations](orgs_security_incident-response.md "orgs_security_incident-response.md").
    * If the error persists, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

The **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page appears, with your new account added to the
list. 9. Now that the account exists and has an IAM role that grants
administrator access to users in the management account, you can access
the account by following the steps in [Accessing member accounts in an
organization with AWS Organizations](orgs_manage_accounts_access.md "orgs_manage_accounts_access.md").

The following code examples show how to use `CreateAccount`.

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
    /// Creates a new AWS Organizations account.
    /// </summary>
    public class CreateAccount
    {
        /// <summary>
        /// Initializes an Organizations client object and uses it to create
        /// the new account with the name specified in accountName.
        /// </summary>
        public static async Task Main()
        {
            IAmazonOrganizations client = new AmazonOrganizationsClient();
            var accountName = "ExampleAccount";
            var email = "someone@example.com";

            var request = new CreateAccountRequest
            {
                AccountName = accountName,
                Email = email,
            };

            var response = await client.CreateAccountAsync(request);
            var status = response.CreateAccountStatus;

            Console.WriteLine($"The staus of {status.AccountName} is {status.State}.");
        }
    }



```

- For API details, see
  [CreateAccount](../../../goto/DotNetSDKV3/organizations-2016-11-28/CreateAccount.md "../../../goto/DotNetSDKV3/organizations-2016-11-28/CreateAccount.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To create a member account that is automatically part of the organization**

The following example shows how to create a member account in an organization. The member account is configured with the name Production Account and the email address of susan@example.com. Organizations automatically creates an IAM role using the default name of OrganizationAccountAccessRole because the roleName parameter is not specified. Also, the setting that allows IAM users or roles with sufficient permissions to access account billing data is set to the default value of ALLOW because the IamUserAccessToBilling parameter is not specified. Organizations automatically sends Susan a "Welcome to AWS" email:

```
`aws organizations create-account --email `susan@example.com` --account-name `"Production Account"``

```

The output includes a request object that shows that the status is now `IN_PROGRESS`:

```
{
        "CreateAccountStatus": {
                "State": "IN_PROGRESS",
                "Id": "car-examplecreateaccountrequestid111"
        }
}
```

You can later query the current status of the request by providing the Id response value to the describe-create-account-status command as the value for the create-account-request-id parameter.

For more information, see Creating an AWS Account in Your Organization in the _AWS Organizations Users Guide_.

- For API details, see
  [CreateAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/create-account.html")
  in _AWS CLI Command Reference_.

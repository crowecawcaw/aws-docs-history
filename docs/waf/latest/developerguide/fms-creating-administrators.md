**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Creating a Firewall Manager administrator account

The following procedure describes how to create a Firewall Manager administrator account using the Firewall Manager console.

###### Note

Only an organization's managment account can create
Firewall Manager administrator accounts.

###### To create a Firewall Manager administrator account

1.  Sign in to the Firewall Manager AWS Management Console using an existing AWS Organizations management account.
2.  Open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2 "https://console.aws.amazon.com/wafv2/fmsv2").
3.  In the navigation pane, choose **Settings**.
4.  Choose **Create administrator account**.
5.  In the **Details** pane, for **AWS account ID** type the
    AWS ID of a member account that you'd like to add as a Firewall Manager
    administrator.
6.  For **Administrative scope**, choose one of the following options:
    - **Full** – This grants the administrator the ability to apply policies to all accounts and organizational units (OUs) within the organization, take actions in all Regions, and apply all Firewall Manager policy types, except for third-party firewalls. Only the default administrator can create and manage third-party firewalls. Take caution if granting this level of permissions to the administrator. In the spirit of least privilege, we recommend only granting the administrator the permissions they need to perform the duties of their role.
    - **Restricted** – If applying a **Restricted** scope, then in **Configure administrative scope** configure the accounts and organizational units, Regions, and policy types that the account can manage.

    For **Accounts and organizational units**, choose the options as follows:

        + If you want to apply policies to all accounts or organizational units in your
         organization, choose **Include all
         accounts under my AWS organization**.
        + If you want to apply policies only to specific accounts or
         accounts that are in specific AWS Organizations organizational units
         (OUs), choose **Include only the specified accounts and
         organizational units**, and then add the accounts and
         OUs that you want to include. Specifying an OU is the equivalent of
         specifying all accounts in the OU and in any of its child OUs,
         including any child OUs and accounts that are added at a later time.
        + If you want to apply policies to all but a specific set of
         accounts or AWS Organizations organizational units (OUs), choose
         **Exclude the specified accounts and organizational
         units, and include all others**, and then add the
         accounts and OUs that you want to exclude. Specifying an OU is the
         equivalent of specifying all accounts in the OU and in any of its
         child OUs, including any child OUs and accounts that are added at a
         later time.

    For **Regions**, choose the options as follows:

        + If you want to allow the administrator to perform actions in all available Regions, choose **Include all
         Regions**.
        + If you want the administrator to perform actions only in specific Regions, choose **Include only the specified Regions**, and then specify the Regions that you want to include.



        ###### Note

        To include a Region that is disabled by default, you must enable the Region for both the AWS Organizations organization management account and the default administration account. For information about enabling Regions for an account, see [Enable a Region](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable") in the *Amazon Web Services General Reference*.

    For **Policy types**, choose the options as follows:.

        + If you want to allow the administrator to manage all policy types, choose **Include all
         policy types**.
        + If you want the administrator to manage only specific policy types, choose **Include only the specified policy types**, and then specify the policy types that you want to include.

7.  Choose **Create administrator account** to create the administrator
    account. Upon creation, Firewall Manager calls AWS Organizations to see if the administrator is
    already a delegated administrator for your organization. If not, Firewall Manager will
    designate the account as a delegated administrator. For information about
    delegated administrators in Organizations see [AWS Organizations terminology and concepts](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md") in the
    _AWS Organizations User Guide_.
    If you apply **Restricted** administrative scope, Firewall Manager automatically evaluates any new resources against your settings. For example, if you include only specific accounts,
    Firewall Manager doesn't apply the policy to any new accounts. As another example, if you include an OU,
    when you add an account to the OU or to any of its child OUs, Firewall Manager automatically includes the account within the administrative scope.

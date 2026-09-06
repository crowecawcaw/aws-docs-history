

# Disabling Macie integration with AWS Organizations
<a name="accounts-mgmt-ao-disable"></a>

After an AWS Organizations organization is integrated with Amazon Macie, the AWS Organizations management account can subsequently disable the integration. As a user of the AWS Organizations management account, you can do this by disabling trusted service access for Macie in AWS Organizations.

When you disable trusted service access for Macie, the following occurs:
+ Macie loses its status as a trusted service in AWS Organizations.
+ The organization's Macie administrator account loses access to all Macie settings, data, and resources for all Macie member accounts in all AWS Regions.
+ All Macie member accounts become standalone Macie accounts. If Macie was enabled for a member account in one or more Regions, Macie continues to be enabled for the account in those Regions. However, the account is no longer associated with a Macie administrator account in any Region. In addition, the account loses access to statistical data, inventory data, and other information that Macie produced and directly provided while performing automated sensitive data discovery for the account.

For additional information about the results of disabling trusted service access, see [Using AWS Organizations with other AWS services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the *AWS Organizations User Guide*. 

**To disable trusted service access for Macie**  
To disable trusted service access, you can use the AWS Organizations console or the AWS Organizations API. Only a user of the AWS Organizations management account can disable trusted service access for Macie. For details about the permissions that you need, see [Permissions required to disable trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_trusted_access_disable_perms) in the *AWS Organizations User Guide*.

Before you disable trusted service access, optionally work with the delegated Macie administrator for your organization to suspend or disable Macie for member accounts and to clean up Macie resources for the accounts.

------
#### [ Console ]

To disable trusted service access by using the AWS Organizations console, follow these steps.

**To disable trusted service access**

1. Sign in to the AWS Management Console using your AWS Organizations management account.

1. Open the AWS Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/).

1. In the navigation pane, choose **Services**.

1. Under **Integrated services**, choose **Amazon Macie**.

1. Choose **Disable trusted access**.

1. Confirm that you want to disable trusted access.

------
#### [ API ]

To disable trusted service access programmatically, use the [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html) operation of the AWS Organizations API. For the `ServicePrincipal` parameter, specify the Macie service principal (`macie.amazonaws.com`).

To disable trusted service access by using the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), run the [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html) command of the AWS Organizations API. For the `service-principal` parameter, specify the Macie service principal (`macie.amazonaws.com`). For example:

```
C:\> aws organizations disable-aws-service-access --service-principal macie.amazonaws.com
```

------
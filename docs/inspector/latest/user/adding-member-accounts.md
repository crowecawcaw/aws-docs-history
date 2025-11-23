# Activating Amazon Inspector scans for member accounts

You can activate Amazon Inspector for member accounts in your organization through multiple methods.
The method you choose depends on your governance requirements and organizational structure.

**AWS Organizations policies (Recommended for centralized governance)**

Use AWS Organizations policies to automatically enable Amazon Inspector across your organization with centralized control.
This approach ensures consistent scanning coverage and automatically applies to new accounts.
For detailed instructions, see the AWS Organizations documentation for creating Amazon Inspector policies.

**Delegated administrator activation**

As the delegated administrator, you can manually activate Amazon Inspector for specific member accounts or all member accounts through the Amazon Inspector console or API.
This approach provides flexibility when organization policies are not in use.

**Member account self-activation**

Member accounts can activate Amazon Inspector for their own account when not restricted by organization policies.
Once activated, the account becomes associated with the delegated administrator.

## Activate scanning for member accounts

The following procedures describe how to activate scanning for member accounts using the delegated administrator and member account methods.
For information about Amazon Inspector scanning types, see [Automated scan types in Amazon Inspector](scanning-resources.md "scanning-resources.md").

###### To automatically activate scanning for all member accounts

1. Sign in using the delegated administrator account credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the region selector to choose the AWS Region where you want to activate scanning for all member accounts.
3. From the navigation pane, choose **Account management**.
   The **Accounts** tab displays all member accounts associated with the AWS Organizations management account.
4. Under **Organization**, select the box next to **Account number**.
   Then choose **Activate** to select which scanning options you want to apply to member accounts.
   You can select the following scanning types:
   - Amazon EC2 scanning
   - Amazon ECR scanning
   - Lambda standard scanning
   - Lambda code scanning
   1. After you select your preferred scanning types, choose **Save**.###### Note

If you have multiple pages of accounts, you must repeat this step on each page.
You can choose the gear icon to change the number of accounts displayed on each page. 5. Turn on the **Automatically activate Inspector for new member accounts** setting, and select which scanning options you want to apply to new member accounts added to your organization.
You can select the following scanning types:

    * Amazon EC2 scanning
    * Amazon ECR scanning
    * Lambda standard scanning
    * Lambda code scanning
    1. After you select your preferred scanning types, choose **Activate**.###### Note

The **Automatically activate Inspector for new member accounts** setting activates Amazon Inspector for all future members of your organization.

If the number of member accounts is more than 5,000, this setting is automatically turned off.
If the total number of member accounts decreases to less than 5,000, the setting is automatically reactivated. 6. (Recommended) Repeat each of these steps in each AWS Region where you want to activate scanning for member accounts.

###### To activate scanning for specific member accounts

1. Sign in using the delegated administrator account credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the region selector to choose the AWS Region where you want to activate scanning for all member accounts.
3. From the navigation pane, choose **Account management**.
   The **Accounts** tab displays all member accounts associated with the AWS Organizations management account.
4. Under **Organization**, select the box next to each member account number you want to activate scanning for.
   Then choose **Activate** to select which scanning options you want to apply to member accounts.
   You can select the following scanning types:
   - Amazon EC2 scanning
   - Amazon ECR scanning
   - Lambda standard scanning
   - Lambda code scanning
   1. After you select your preferred scanning types, choose **Save**.###### Note

If you have multiple pages of accounts, you must repeat this step on each page.
You can choose the gear icon to change the number of accounts displayed on each page. 5. (Recommended) Repeat each of these steps in each AWS Region where you want to activate scanning for specific members.

###### To activate scanning as a member account

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the region selector to choose the AWS Region where you want to activate scanning for all member accounts.
3. From the navigation pane, choose **Account management**.
   The **Accounts** tab displays all member accounts associated with the AWS Organizations management account.
4. Under **Organization**, select the box next to your account number.
   Then choose **Activate** to select which scanning options you want to apply.
   You can select the following scanning types:
   - Amazon EC2 scanning
   - Amazon ECR scanning
   - Lambda standard scanning
   - Lambda code scanning
   1. After you select your preferred scanning types, choose **Save**.

5. (Recommended) Repeat these steps in each Region where you want to activate scanning for your member account.

###### Note

If your AWS Organizations management account has a delegated administrator account for Amazon Inspector, you can activate your account as a member account to view scan details.

###### Important

If organization policies are managing Amazon Inspector enablement for your accounts, the delegated administrator and member accounts cannot modify policy-managed scan types using Amazon Inspector enablement/disablement APIs.
API requests will fail with an error indicating the resource is managed by organization policy.
You can still enable additional scan types not managed by the policy.

# Administrator configuration

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                                                             |
| --------------------------------------------------------------------------- |
| Intended audience:<br>System administrators and Amazon Quick administrators |

As a Amazon Quick administrator, you can configure various settings for user-driven license upgrades, including enabling the feature, setting approval policies, and configuring custom permissions profiles.

## Enabling user-driven upgrades

Before users can request license upgrades, you must enable the user-driven upgrade feature in your Amazon Quick account settings.

### Access Administrator Settings

- Log in to your Amazon Amazon Quick administrator account
- Navigate to the 'Manage Account' section of the console
- Check for User upgrades Section
- Use the toggle button to Enable/Disable - Automatically approve upgrades

### Configuring approval settings

Administrators can configure three types of upgrade governance:

- **Turned off altogether** — Users cannot request upgrades
- **Admin Approval** (default for IAM Identity Center and AD) — Users can request upgrades that require administrator approval
- **User Driven Upgrades** (default for IdP) — Users can upgrade automatically without approval

## Creating a custom permissions profile for Amazon Amazon Quick account that is integrated with IAM Identity Center or Active Directory

Amazon Amazon Quick account administrators can use the following procedure to create a custom permissions profile for an Amazon Amazon Quick account that is integrated with IAM Identity Center or Active Directory.

### To create a custom permissions profile for an Amazon Amazon Quick account that is integrated with IAM Identity Center or Active Directory

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. Open Amazon Amazon Quick.
3. The Amazon Amazon Quick Admin console opens. Choose **Custom Permissions**.
4. The **Manage custom permissions** page opens. Choose one of the following options.
5. To create a new custom permissions profile, choose **Create**.
6. To edit or view an existing custom permissions profile, choose the ellipses (three dots) next to the profile that you want, and then choose **Edit**.
7. If you want to create or update a custom permissions profile, make selections for the following items.
8. For **Name**, enter a name for the custom permissions profile.
9. For **Restrictions**, choose "Allow users to upgrade or request upgrades" under "User Upgrades". Choose any other options that you want to deny. Any option that you don't choose is allowed.
10. Choose **Create** or **Update** to confirm your choices. To go back without making any changes, choose **Back**.
11. Once you are done making changes, record the name of the custom permissions profile. Provide the name of the custom permissions profile to API users so that they can apply the custom permissions profile to roles or users.

## Creating a custom permissions profile for an Amazon Amazon Quick account that uses Amazon Amazon Quick managed users

Amazon Amazon Quick account administrators can use the following procedure to create a custom permissions profile for an Amazon Amazon Quick account that uses Amazon Amazon Quick managed users.

### To create a custom permissions profile for Amazon Amazon Quick managed users

1. Open the [Amazon Quick console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. From any page in the Amazon Amazon Quick console, choose **Manage Amazon Quick** at the top right corner.
3. Only Amazon Amazon Quick administrators have access to the **Manage Amazon Quick** menu option. If you don't have access to the **Manage Amazon Quick** menu, contact your Amazon Amazon Quick administrator for assistance.
4. Choose **Custom permissions**. You can also choose the **Manage users** section and then choose **Manage custom permissions**.
5. The **Manage custom permissions** page opens. Choose one of the following options.
6. To create a new custom permissions profile, choose **Create**.
7. To edit or view an existing custom permissions profile, choose the ellipses (three dots) next to the profile that you want, and then choose **Edit**.
8. If you want to create or update a custom permissions profile, make selections for the following items.
9. For **Name**, enter a name for the custom permissions profile.
10. For **Restrictions**, choose "Allow users to upgrade or request upgrades" under "User Upgrades". Choose any other options that you want to deny. Any option that you don't choose is allowed.
11. Choose **Create** or **Update** to confirm your choices. To go back without making any changes, choose **Back**.
12. Once you are done making changes, record the name of the custom permissions profile. Provide the name of the custom permissions profile to API users so that they can apply the custom permissions profile to roles or users.

## Applying custom permissions profiles

### Apply a custom permissions profile to an Amazon Amazon Quick role with the Amazon Amazon Quick API

For more information, see [Apply custom permissions profile to role](../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-role.md#customizing-permissions-to-the-quicksight-console-apply-role "../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-role.md#customizing-permissions-to-the-quicksight-console-apply-role").

### Apply a custom permissions profile to a user with the Amazon Amazon Quick API

For more information, see [Apply custom permissions profile to user](../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-iam-user.md#customizing-permissions-to-the-quicksight-console-apply-iam-user "../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-iam-user.md#customizing-permissions-to-the-quicksight-console-apply-iam-user").

### Apply a custom permissions profile to an account

For more information, see [Apply custom permissions profile to account](../../../quicksuite/latest/userguide/create-custom-permisions-profile.md#customizing-permissions-to-the-quicksight-console-apply-account "../../../quicksuite/latest/userguide/create-custom-permisions-profile.md#customizing-permissions-to-the-quicksight-console-apply-account").

### Apply a custom permissions profile to an account using the Amazon Quick APIs

For more information, see [Apply custom permissions profile using APIs](../../../quicksuite/latest/userguide/create-custom-permisions-profile.md#customizing-permissions-to-the-quicksight-console-apply-account-with-apis "../../../quicksuite/latest/userguide/create-custom-permisions-profile.md#customizing-permissions-to-the-quicksight-console-apply-account-with-apis").

# Check MFA status

Use the IAM console to check whether an AWS account root user or IAM user has a valid MFA device
enabled.

###### To check the MFA status of a root user

1. Sign in to the AWS Management Console with your root user credentials and then open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation bar on the upper right, choose your user name, and then choose
   **Security credentials**.
3. Check under **Multi-factor Authentication (MFA)** to see whether MFA is
   enabled or disabled. If MFA has not been activated, an alert symbol (
   ![Alert icon](images/console-alert-icon.console.png)
   ) is displayed.
   If you want to enable MFA for the account, see one of the following:

- [Enable a virtual MFA device for the root user
  (console)](enable-virt-mfa-for-root.md "enable-virt-mfa-for-root.md")
- [Enable a passkey or security key for the root user
  (console)](enable-fido-mfa-for-root.md "enable-fido-mfa-for-root.md")
- [Enable a hardware TOTP token for the root user
  (console)](enable-hw-mfa-for-root.md "enable-hw-mfa-for-root.md")

###### To check the MFA status of IAM users

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. If necessary, add the **MFA** column to the users table by completing
   the following steps:
   1. Above the table on the far right, choose the settings icon (
      ![Settings icon](images/console-settings-icon.console.png)
      ).
   2. In **Manage Columns**, select **MFA**.
   3. (Optional) Clear the checkbox for any column headings that you do not want to
      appear in the users table.
   4. Choose **Close** to return to the list of users.

4. The **MFA** column tells you about the MFA device that is enabled. If
   no MFA device is active for the user, the console displays **None**. If the
   user has an MFA device enabled, the **MFA** column shows the type of device
   that is enabled with a value of **Virtual**, **Security
   key**, **Hardware**, or **SMS**.

###### Note

AWS ended support for enabling SMS multi-factor authentication (MFA). We recommend
that customers who have IAM users that use SMS text message-based MFA switch to one of
the following alternative methods: [virtual (software-based) MFA device](id_credentials_mfa_enable_virtual.md "id_credentials_mfa_enable_virtual.md"), [FIDO security key](id_credentials_mfa_enable_fido.md "id_credentials_mfa_enable_fido.md"), or [hardware MFA device](id_credentials_mfa_enable_physical.md "id_credentials_mfa_enable_physical.md"). You can
identify the users in your account with an assigned SMS MFA device. To do so, go to the
IAM console, choose **Users** from the navigation pane, and look for
users with **SMS** in the **MFA** column of the
table. 5. To view additional information about the MFA device for a user, choose the name of the
user whose MFA status you want to check. Then choose the **Security
credentials** tab. 6. If no MFA device is active for the user, the console displays **No MFA devices.
Assign an MFA device to improve the security of your AWS environment** in the
**Multi-factor authentication (MFA)** section. If the user has MFA
devices enabled, the **Multi-factor authentication (MFA)** section shows
details about the devices:

    * The device name
    * The device type
    * The identifier for the device, such as a serial number for a physical device or the
     ARN in AWS for a virtual device
    * When the device was created

To remove or resync a device, choose the radio button next to the device and choose
**Remove** or **Resync**.

For more information on enabling MFA, see the following:

- [Assign a virtual MFA device in the
  AWS Management Console](id_credentials_mfa_enable_virtual.md "id_credentials_mfa_enable_virtual.md")
- [Assign a passkey or security key in the
  AWS Management Console](id_credentials_mfa_enable_fido.md "id_credentials_mfa_enable_fido.md")
- [Assign a hardware TOTP token in the
  AWS Management Console](id_credentials_mfa_enable_physical.md "id_credentials_mfa_enable_physical.md")

# Enable a hardware TOTP token for the root user

(console)

You can configure and enable a physical MFA device for your root user from the AWS Management Console
only, not from the AWS CLI or AWS API.

###### Note

You might see different text, such as **Sign in using
MFA** and **Troubleshoot your authentication
device**. However, the same features are provided. In either case, if you
cannot verify your account email address and phone number using alternative factors of
authentication, contact [AWS Support](https://aws.amazon.com/forms/aws-mfa-support "https://aws.amazon.com/forms/aws-mfa-support") to delete your MFA setting.

###### To enable a hardware TOTP token for your root user (console)

1. Open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and sign in using your root user credentials.

For instructions, see [Sign in
to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") in the _AWS Sign-In User
Guide_. 2. On the right side of the navigation bar, choose your account name, and then choose
**Security credentials**.

![Security credentials in the navigation menu](images/security-credentials-root.shared.console.png) 3. Expand the **Multi-factor authentication (MFA)** section. 4. Choose **Assign MFA device**. 5. In the wizard, type a **Device name**, choose **Hardware
TOTP token**, and then choose **Next**. 6. In the **Serial number** box, type the serial number that is found
on the back of the MFA device. 7. In the **MFA code 1** box, type the six-digit number displayed by
the MFA device. You might need to press the button on the front of the device to display
the number.

![IAM Dashboard, MFA Device](images/MFADevice.png) 8. Wait 30 seconds while the device refreshes the code, and then type the next
six-digit number into the **MFA code 2** box. You might need to press
the button on the front of the device again to display the second number. 9. Choose **Add MFA**. The MFA device is now associated with the
AWS account.

###### Important

Submit your request immediately after generating the authentication codes. If you
generate the codes and then wait too long to submit the request, the MFA device
successfully associates with the user but the MFA device becomes out of sync. This
happens because time-based one-time passwords (TOTP) expire after a short period of
time. If this happens, you can [resync the
device](id_credentials_mfa_sync.md "id_credentials_mfa_sync.md").

The next time you use your root user credentials to sign in, you must type a code from
the MFA device.

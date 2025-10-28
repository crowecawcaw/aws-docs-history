# MFA enabled sign-in

Users who are configured with [multi-factor authentication
(MFA)](id_credentials_mfa.md "id_credentials_mfa.md") devices must use their MFA devices to sign in to the AWS Management Console. After the user
enters their sign-in credentials, AWS checks the user's account to see if MFA is required for
that user.

###### Important

If you use access key and secret key credentials for direct AWS Management Console access with the AWS STS
[`GetFederationToken`](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md") API call, MFA will NOT be required. For more
information, see [Using access keys and secret key
credentials for console access](securing_access-keys.md#console-access-security-keys "securing_access-keys.md#console-access-security-keys").

The following topics provide information on how users complete signing in when MFA is
required.

###### Topics

- [Multiple MFA devices enabled](#console_sign-in-multiple-mfa "#console_sign-in-multiple-mfa")
- [FIDO security key](#console_sign-in-mfa-fido "#console_sign-in-mfa-fido")
- [Virtual MFA device](#console_sign-in-mfa-virtual "#console_sign-in-mfa-virtual")
- [Hardware TOTP token](#console_sign-in-mfa-hardware "#console_sign-in-mfa-hardware")

## Multiple MFA devices enabled

If a user signs in to the AWS Management Console as an AWS account root user or IAM user with multiple
MFA devices enabled for that account, they only need to use one MFA device to sign in. After
the user authenticates with the user’s password, they select which MFA device type they would
like to use to finish authenticating. Then the user is prompted to authenticate with the type
of device that they selected.

## FIDO security key

If MFA is required for the user, a second sign-in page appears. The user needs to tap the
FIDO security key.

###### Note

Google Chrome users should not choose any of the available options on the pop-up
that asks to **Verify your identity with amazon.com**. You only need to tap on the security key.

Unlike other MFA devices, FIDO security keys do not go out of sync. Administrators can
deactivate a FIDO security key if it's lost or broken. For more information, see [Deactivating MFA devices (console)](id_credentials_mfa_disable.md#deactive-mfa-console "id_credentials_mfa_disable.md#deactive-mfa-console").

For information on browsers that support WebAuthn and FIDO-compliant devices that AWS supports, see
[Supported configurations
for using passkeys and security keys](id_credentials_mfa_fido_supported_configurations.md "id_credentials_mfa_fido_supported_configurations.md").

## Virtual MFA device

If MFA is required for the user, a second sign-in page appears. In the **MFA
code** box, the user must enter the numeric code provided by the MFA
application.

If the MFA code is correct, the user can access the AWS Management Console. If the code is incorrect,
the user can try again with another code.

A virtual MFA device can go out of sync. If a user cannot sign in to the AWS Management Console after
several tries, the user is prompted to synchronize the virtual MFA device. The user can follow
the on-screen prompts to synchronize the virtual MFA device. For information about how you can
synchronize a device on behalf of a user in your AWS account, see [Resynchronize virtual and hardware MFA
devices](id_credentials_mfa_sync.md "id_credentials_mfa_sync.md").

## Hardware TOTP token

If MFA is required for the user, a second sign-in page appears. In the **MFA
code** box, the user must enter the numeric code provided by a hardware TOTP token.

If the MFA code is correct, the user can access the AWS Management Console. If the code is incorrect,
the user can try again with another code.

A hardware TOTP token can go out of sync. If a user can't sign in to the AWS Management Console after
several tries, the user is prompted to synchronize the MFA token device. The user can follow
the on-screen prompts to synchronize the MFA token device. For information about how you can
synchronize a device on behalf of a user in your AWS account, see [Resynchronize virtual and hardware MFA
devices](id_credentials_mfa_sync.md "id_credentials_mfa_sync.md").

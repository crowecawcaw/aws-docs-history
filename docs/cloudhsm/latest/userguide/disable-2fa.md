# Disable 2FA for HSM users using AWS CloudHSM Management Utility

Use the AWS CloudHSM Management Utility (CMU) to disable two-factor authentication (2FA) for hardware security module HSM) users in AWS CloudHSM.

###### To disable 2FA for CO users with 2FA enabled

1. Use CMU to log in to the HSM as a CO with 2FA enabled.
2. Use **changePswd** to remove 2FA from CO users with 2FA enabled.

```
`aws-cloudhsm >` **changePswd** CO example-user `<new password>`
```

CMU prompts you to confirm the change password operation.

###### Note

If you remove the 2FA requirement or change the password for a 2FA user that is also a
quorum authentication user, you will also remove the registration of the quorum user as an
MofN user. For more information about quorum users and 2FA, see [Quorum authentication and 2FA in AWS CloudHSM clusters using AWS CloudHSM
Management Utility](quorum-2fa.md "quorum-2fa.md"). 3. Type `y`.

CMU confirms the change password operation.

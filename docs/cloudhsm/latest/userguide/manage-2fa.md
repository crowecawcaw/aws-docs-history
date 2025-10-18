# Manage 2FA for users using AWS CloudHSM Management Utility

For increased security, you can configure two-factor authentication (2FA) to help protect the
 AWS CloudHSM cluster. You can only enable 2FA for crypto officers (CO). 

When you log in to a cluster with a 2FA-enabled hardware service module (HSM) account, you
 provide cloudhsm\_mgmt\_util (CMU) with your password—the first factor, what you know—and CMU
 provides you with a token and prompts you to have the token signed. To provide the second
 factor—what you have—you sign the token with a private key from a key pair you've
 already created and associated with the HSM user. To access the cluster, you provide the signed
 token to CMU.

###### Note

You cannot enable 2FA for crypto users (CU) or applications. Two-factor authentication (2FA)
 is only for CO users.

###### Topics

* [Quorum authentication](quorum-2fa.md "quorum-2fa.md")
* [Key pair requirements](enable-2fa-kms.md "enable-2fa-kms.md")
* [Create users](create-2fa.md "create-2fa.md")
* [Manage user 2FA](rotate-2fa.md "rotate-2fa.md")
* [Disable 2FA](disable-2fa.md "disable-2fa.md")
* [Configuration reference](reference-2fa.md "reference-2fa.md")

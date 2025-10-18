# Using CloudHSM Management Utility (CMU) to manage quorum authentication (M of N access
 control)

The HSMs in your AWS CloudHSM cluster support quorum authentication, which is also known as M of N
 access control. With quorum authentication, no single user on the HSM can do quorum-controlled
 operations on the HSM. Instead, a minimum number of HSM users (at least 2) must cooperate to do
 these operations. With quorum authentication, you can add an extra layer of protection by
 requiring approvals from more than one HSM user.

Quorum authentication can control the following operations:


* HSM user management by [crypto officers (COs)](understanding-users-cmu.md#crypto-officer "understanding-users-cmu.md#crypto-officer")
 – Creating and deleting HSM users, and changing a different HSM user's password. For
 more information, see [User management with quorum
 authentication enabled for AWS CloudHSM Management Utility](quorum-authentication-crypto-officers.md "quorum-authentication-crypto-officers.md").
Note the following additional information about using quorum authentication in
 AWS CloudHSM.


* An HSM user can sign their own quorum token—that is, the requesting user
 can provide one of the required approvals for quorum authentication.
* You choose the minimum number of quorum approvers for quorum-controlled operations.
 The smallest number you can choose is two (2), and the largest number you can choose is eight (8).
* The HSM can store up to 1024 quorum tokens. If the HSM already has 1024 tokens when
 you try to create a new one, the HSM purges one of the expired tokens. By default, tokens
 expire ten minutes after their creation.
* The cluster uses the same key for quorum authentication and for two-factor
 authentication (2FA). For more information about using quorum authentication and 2FA, see
 [Quorum Authentication and 2FA](quorum-2fa.md "quorum-2fa.md").
The following topics provide more information about quorum authentication in AWS CloudHSM.

###### Topics

* [Quorum authentication process](quorum-authentication-overview.md "quorum-authentication-overview.md")
* [First time
 setup](quorum-authentication-crypto-officers-first-time-setup.md "quorum-authentication-crypto-officers-first-time-setup.md")
* [User management with quorum
 (M of N)](quorum-authentication-crypto-officers.md "quorum-authentication-crypto-officers.md")
* [Change
 the minimum value](quorum-authentication-crypto-officers-change-minimum-value.md "quorum-authentication-crypto-officers-change-minimum-value.md")

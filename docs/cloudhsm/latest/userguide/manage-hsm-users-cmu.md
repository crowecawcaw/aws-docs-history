

# HSM user management with CloudHSM Management Utility (CMU)
<a name="manage-hsm-users-cmu"></a>

 To manage hardware security module (HSM) users in AWS CloudHSM, you must log in to the HSM with the user name and password of a [cryptographic officer](understanding-users-cmu.md#crypto-officer) (CO). Only COs can manage users. The HSM contains a default CO named admin. You set the password for admin when you [activated the cluster](activate-cluster.md). 

This topic provides step-by-step instruction on and detail about managing HSM users with AWS CloudHSM Management Utility (CMU). 

**Topics**
+ [Prerequisites](understand-users.md)
+ [User types](understanding-users-cmu.md)
+ [Permissions table](user-permissions-table-cmu.md)
+ [Create users](create-users-cmu.md)
+ [List all users](list-users.md)
+ [Change passwords](change-user-password-cmu.md)
+ [Delete users](delete-user.md)
+ [Manage user 2FA](manage-2fa.md)
+ [Using CMU to manage quorum authentication](quorum-authentication.md)
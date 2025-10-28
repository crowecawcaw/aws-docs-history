# AWS CloudHSM user management best practices

Follow the best practices in this section to effectively manage users in your AWS CloudHSM cluster.
HSM users are distinct from IAM users. IAM users and entities that have an identity-based policy with the appropriate permissions can create HSMs by interacting with resources through the AWS API.
After the HSM is created, you must use HSM user credentials to authenticate operations on the HSM.
For a detailed guide of HSM users, see [HSM users in AWS CloudHSM](manage-hsm-users.md "manage-hsm-users.md").

## Protect your HSM users' credentials

It is imperative to keep the credentials of your HSM users securely protected as HSM users are the entities that can access and perform cryptographic and management operations on your HSM.
AWS CloudHSM does not have access to your HSM user credentials, and will be unable to assist you if you lose access to them.

## Have at least two admins to prevent lockout

To avoid being locked out of your cluster, we recommend you have at least two admins in case one admin password is lost. In the event this happens, you can use the other admin to reset the password.

###### Note

_Admins_ in Client SDK 5 are synonymous with _crypto officers_ (COs) in Client SDK 3.

## Enable quorum for all user management operations

Quorum allows you to set a min number of admins that must approve a user management operation before that operation can take place.
Due to the privilege that admins have, we recommend that you enable quorum for all user management operations.
This can limit the potential for impact if one of your admin passwords is compromised. For more information, see [Managing Quorum](quorum-auth-chsm-cli.md "quorum-auth-chsm-cli.md").

## Create multiple crypto users, each with limited permissions

By separating the responsibilities of crypto users, no one user has total control over the entire system.
For this reason, we recommend you create multiple crypto users and limit the permissions of each.
Typically, this is done by giving different crypto users distinctly different responsibilities and actions they perform
(for example, having one crypto user who is responsible for generating and sharing keys with other crypto users who then utilize them in your application).

Related resources:

- [Share a key using CloudHSM CLI](cloudhsm_cli-key-share.md "cloudhsm_cli-key-share.md")
- [Unshare a key using CloudHSM CLI](cloudhsm_cli-key-unshare.md "cloudhsm_cli-key-unshare.md")

# HSM user types for AWS CloudHSM Management Utility

Most operations that you perform on the hardware security module (HSM) require the
credentials of an AWS CloudHSM _HSM user_. The HSM authenticates each HSM user and
each HSM user has a _type_ that determines which operations you can perform
on the HSM as that user.

###### Note

HSM users are distinct from IAM users. IAM users who have the correct credentials can create HSMs by interacting with resources through the AWS API. After the HSM is created,
you must use HSM user credentials to authenticate operations on the HSM.

###### User types

- [Precrypto officer (PRECO)](#preco "#preco")
- [Crypto officer (CO)](#crypto-officer "#crypto-officer")
- [Crypto user (CU)](#crypto-user-cmu "#crypto-user-cmu")
- [Appliance user (AU)](#appliance-user-cmu "#appliance-user-cmu")

## Precrypto officer (PRECO)

In both the cloud management utility (CMU) and the key management utility (KMU), the PRECO is a temporary user that exists only on the first HSM in an
AWS CloudHSM cluster. The first HSM in a new cluster contains an PRECO user indicating that this cluster has never been activated.
To [activate a cluster](activate-cluster.md "activate-cluster.md"), you execute the cloudhsm-cli and run the **cluster activate** command. Log in to the
HSM and change the PRECO's password. When you change the password, this user becomes
the crypto officer (CO).

## Crypto officer (CO)

In both the cloud management utility (CMU) and the key management utility (KMU), a crypto officer (CO) can perform user management operations. For example, they can create
and delete users and change user passwords. For more information about CO users, see the [HSM user permissions table for AWS CloudHSM Management Utility](user-permissions-table-cmu.md "user-permissions-table-cmu.md"). When you activate a new cluster, the user changes from a [Precrypto Officer](#preco "#preco") (PRECO) to a crypto officer (CO).-->

## Crypto user (CU)

A crypto user (CU) can perform the following key management and cryptographic
operations.

- **Key management** – Create, delete, share,
  import, and export cryptographic keys.
- **Cryptographic operations** – Use cryptographic
  keys for encryption, decryption, signing, verifying, and more.

For more information, see the [HSM user permissions table for AWS CloudHSM Management Utility](user-permissions-table-cmu.md "user-permissions-table-cmu.md").

## Appliance user (AU)

The appliance user (AU) can perform cloning and synchronization operations on your cluster's
HSMs. AWS CloudHSM uses the
AU to synchronize the HSMs in an AWS CloudHSM cluster. The AU exists on all HSMs provided by AWS CloudHSM,
and has limited permissions. For more information, see the [HSM user permissions table for AWS CloudHSM Management Utility](user-permissions-table-cmu.md "user-permissions-table-cmu.md").

AWS cannot perform any operations on your HSMs . AWS cannot view or modify your users or keys and cannot perform any
cryptographic operations using those keys.

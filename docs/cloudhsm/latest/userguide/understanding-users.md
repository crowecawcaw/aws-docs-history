

# HSM user types for CloudHSM CLI
<a name="understanding-users"></a>

 Most operations that you perform on the hardware security module (HSM) require the credentials of an AWS CloudHSM *HSM user*. The HSM authenticates each HSM user and each HSM user has a *type* that determines which operations you can perform on the HSM as that user. 

**Note**  
HSM users are distinct from IAM users. IAM users who have the correct credentials can create HSMs by interacting with resources through the AWS API. After the HSM is created, you must use HSM user credentials to authenticate operations on the HSM.

**Topics**
+ [Unactivated admin](#unactivated-admin)
+ [Admin](#admin)
+ [Crypto user (CU)](#crypto-user-chsm-cli)
+ [Appliance user (AU)](#appliance-user-chsm-cli)

## Unactivated admin
<a name="unactivated-admin"></a>

In CloudHSM CLI, The unactivated admin is a temporary user that exists only on the first HSM in an AWS CloudHSM cluster that has never been activated. To [activate a cluster](activate-cluster.md), run the **cluster activate** command in CloudHSM CLI. After running this command, unactivated admin are prompted to change the password. After changing the password, the unactivated admin becomes an admin. 

## Admin
<a name="admin"></a>

In CloudHSM CLI, admin can perform user management operations. For example, they can create and delete users and change user passwords. For more information about admins, see the [HSM user permissions table for CloudHSM CLI](user-permissions-table-chsm-cli.md). 

## Crypto user (CU)
<a name="crypto-user-chsm-cli"></a>

A crypto user (CU) can perform the following key management and cryptographic operations.
+ **Key management** – Create, delete, share, import, and export cryptographic keys.
+ **Cryptographic operations** – Use cryptographic keys for encryption, decryption, signing, verifying, and more.

For more information, see the [HSM user permissions table for CloudHSM CLI](user-permissions-table-chsm-cli.md).

## Appliance user (AU)
<a name="appliance-user-chsm-cli"></a>

The appliance user (AU) can perform cloning and synchronization operations on your cluster's HSMs. AWS CloudHSM uses the AU to synchronize the HSMs in an AWS CloudHSM cluster. The AU exists on all HSMs provided by AWS CloudHSM, and has limited permissions. For more information, see the [HSM user permissions table for CloudHSM CLI](user-permissions-table-chsm-cli.md).

AWS cannot perform any operations on your HSMs . AWS cannot view or modify your users or keys and cannot perform any cryptographic operations using those keys.
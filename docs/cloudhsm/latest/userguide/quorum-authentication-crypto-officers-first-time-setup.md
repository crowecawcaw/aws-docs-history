# Set up quorum

authentication for AWS CloudHSM crypto officers

The following topics describe the steps that you must complete to configure your hardware
security module (HSM) so that AWS CloudHSM [crypto officers (COs)](understanding-users-cmu.md#crypto-officer "understanding-users-cmu.md#crypto-officer")
can use quorum authentication. You need to do these steps only once when you first configure
quorum authentication for COs. After you complete these steps, see [User management with quorum
authentication enabled for AWS CloudHSM Management Utility](quorum-authentication-crypto-officers.md "quorum-authentication-crypto-officers.md").

###### Topics

- [Prerequisites](#quorum-crypto-officers-prerequisites "#quorum-crypto-officers-prerequisites")
- [Step 1. Create and register a
  key for signing](#quorum-crypto-officers-create-and-register-key "#quorum-crypto-officers-create-and-register-key")
- [Step 2. Set the quorum
  minimum value on the HSM](#quorum-crypto-officers-set-quorum-minimum-value "#quorum-crypto-officers-set-quorum-minimum-value")

## Prerequisites

To understand this example, you should be familiar with the [cloudhsm_mgmt_util (CMU) command line
tool](cloudhsm_mgmt_util.md "cloudhsm_mgmt_util.md"). In this example, the AWS CloudHSM cluster has two HSMs, each with the same COs, as
shown in the following output from the **listUsers** command. For more
information about creating users, see [HSM users](manage-hsm-users.md "manage-hsm-users.md").

```
`aws-cloudhsm >` `listUsers``Users on server 0(10.0.2.14):
Number of users found:7

 User Id User Type User Name MofnPubKey LoginFailureCnt 2FA
 1 PRECO admin NO 0 NO
 2 AU app_user NO 0 NO
 3 CO officer1 NO 0 NO
 4 CO officer2 NO 0 NO
 5 CO officer3 NO 0 NO
 6 CO officer4 NO 0 NO
 7 CO officer5 NO 0 NO
Users on server 1(10.0.1.4):
Number of users found:7

 User Id User Type User Name MofnPubKey LoginFailureCnt 2FA
 1 PRECO admin NO 0 NO
 2 AU app_user NO 0 NO
 3 CO officer1 NO 0 NO
 4 CO officer2 NO 0 NO
 5 CO officer3 NO 0 NO
 6 CO officer4 NO 0 NO
 7 CO officer5 NO 0 NO`
```

## Step 1. Create and register a

key for signing

To use quorum authentication, each CO must do _all_ of
the following steps:

###### Topics

- [Create an RSA key pair](#mofn-key-pair-create "#mofn-key-pair-create")
- [Create and sign a registration token](#mofn-registration-token "#mofn-registration-token")
- [Register the public key with the HSM](#mofn-register-key "#mofn-register-key")

### Create an RSA key pair

There are many different ways to create and protect a key pair. The following examples
show how to do it with [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/").

###### Example– Create a private key with OpenSSL

The following example demonstrates how to use OpenSSL to create a 2048-bit RSA key
that is protected by a pass phrase. To use this example, replace
`officer1.key` with the name of the file where you want to
store the key.

```
`$` `openssl genrsa -out `<officer1.key>` -aes256 2048``Generating RSA private key, 2048 bit long modulus
.....................................+++
.+++
e is 65537 (0x10001)
Enter pass phrase for officer1.key:
Verifying - Enter pass phrase for officer1.key:`
```

Next, generate the public key using the private key that you just created.

###### Example– Create a public key with OpenSSL

The following example demonstrates how to use OpenSSL to create a public key from the
private key you just created.

```
`$` `openssl rsa -in officer1.key -outform PEM -pubout -out officer1.pub``Enter pass phrase for officer1.key:
writing RSA key`
```

### Create and sign a registration token

You create a token and sign it with the private key you just generated in the previous
step.

###### Example– Create a token

The registration token is just a file with any random data that doesn't exceed the
maximum size of 245 bytes. You sign the token with the private key to demonstrate that you
have access to the private key. The following command uses echo to redirect a string to a
file.

```
`$` `echo `<token to be signed>` > `officer1.token``
```

Sign the token and save it to a signature file. You will need the signed token, the
unsigned token, and the public key to register the CO as an MofN user with the HSM.

###### Example– Sign the token

Use OpenSSL and the private key to sign the registration token and create the
signature file.

```
`$` `openssl dgst -sha256 \
 -sign `officer1.key` \
 -out `officer1.token.sig` `officer1.token``
```

### Register the public key with the HSM

After creating a key, the CO must register the public part of the key (the public key)
with the HSM.

###### To register a public key with the HSM

1. Use the following command to start the cloudhsm_mgmt_util command
   line tool.

```
`$` `/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`
```

2. Use the **loginHSM** command to log in to the HSM as a CO. For more information, see [HSM user management with CloudHSM Management Utility
   (CMU)](manage-hsm-users-cmu.md "manage-hsm-users-cmu.md").
3. Use the **[registerQuorumPubKey](cloudhsm_mgmt_util-registerQuorumPubKey.md "cloudhsm_mgmt_util-registerQuorumPubKey.md")** command to register the public key. For more
   information, see the following example or use the **help
   registerQuorumPubKey** command.

###### Example– Register a public key with the HSM

The following example shows how to use the **registerQuorumPubKey**
command in the cloudhsm_mgmt_util command line tool to register a CO's
public key with the HSM. To use this command, the CO must be logged in to the HSM. Replace
these values with your own:

````
`aws-cloudhsm >` `registerQuorumPubKey CO `<officer1>` `<officer1.token>` `<officer1.token.sig>` `<officer1.pub>```*************************CAUTION********************************
This is a CRITICAL operation, should be done on all nodes in the
cluster. AWS does NOT synchronize these changes automatically with the
nodes on which this operation is not executed or failed, please
ensure this operation is executed on all nodes in the cluster.
****************************************************************

Do you want to continue(y/n)? `y`
registerQuorumPubKey success on server 0(10.0.2.14)`
````

**<officer1.token>**

The path to a file that contains an unsigned registration token. Can have any
random data of max file size of 245 bytes.

Required: Yes

**<officer1.token.sig>**

The path to a file that contains the SHA256_PKCS mechanism signed hash of the
registration token.

Required: Yes

**<officer1.pub>**

The path to the file that contains the public key of an asymmetric RSA-2048 key
pair. Use the private key to sign the registration token.

Required: Yes

After all COs register their public keys, the output from the
**listUsers** command shows this in the `MofnPubKey` column,
as shown in the following example.

```
`aws-cloudhsm >` `listUsers``Users on server 0(10.0.2.14):
Number of users found:7

 User Id User Type User Name MofnPubKey LoginFailureCnt 2FA
 1 PRECO admin NO 0 NO
 2 AU app_user NO 0 NO
 3 CO officer1 YES 0 NO
 4 CO officer2 YES 0 NO
 5 CO officer3 YES 0 NO
 6 CO officer4 YES 0 NO
 7 CO officer5 YES 0 NO
Users on server 1(10.0.1.4):
Number of users found:7

 User Id User Type User Name MofnPubKey LoginFailureCnt 2FA
 1 PRECO admin NO 0 NO
 2 AU app_user NO 0 NO
 3 CO officer1 YES 0 NO
 4 CO officer2 YES 0 NO
 5 CO officer3 YES 0 NO
 6 CO officer4 YES 0 NO
 7 CO officer5 YES 0 NO`
```

## Step 2. Set the quorum

minimum value on the HSM

To use quorum authentication for COs, a CO must log in to the HSM and then set the
_quorum minimum value_, also known as the _m value_.
This is the minimum number of CO approvals that are required to perform HSM user management
operations. Any CO on the HSM can set the quorum minimum value, including COs that have not
registered a key for signing. You can change the quorum minimum value at any time; for more
information, see [Change
the minimum value](quorum-authentication-crypto-officers-change-minimum-value.md "quorum-authentication-crypto-officers-change-minimum-value.md").

###### To set the quorum minimum value on the HSM

1. Use the following command to start the cloudhsm_mgmt_util command
   line tool.

```
`$` `/opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg`
```

2. Use the **loginHSM** command to log in to the HSM as a CO. For more information, see [HSM user management with CloudHSM Management Utility
   (CMU)](manage-hsm-users-cmu.md "manage-hsm-users-cmu.md").
3. Use the **setMValue** command to set the quorum minimum value. For
   more information, see the following example or use the **help setMValue**
   command.

###### Example– Set the quorum minimum value on the HSM

This example uses a quorum minimum value of two. You can choose any value from two (2) to
eight (8), up to the total number of COs on the HSM. In this example, the HSM has six COs, so the maximum possible
value is six.

To use the following example command, replace the final number
(`2`) with the preferred quorum minimum value.

````
`aws-cloudhsm >` `setMValue 3 `<2>```*************************CAUTION********************************
This is a CRITICAL operation, should be done on all nodes in the
cluster. AWS does NOT synchronize these changes automatically with the
nodes on which this operation is not executed or failed, please
ensure this operation is executed on all nodes in the cluster.
****************************************************************

Do you want to continue(y/n)? `y`
Setting M Value(2) for 3 on 2 nodes`
````

In the preceding example, the first number (3) identifies the _HSM
service_ whose quorum minimum value you are setting.

The following table lists the HSM service identifiers along with their names,
descriptions, and the commands that are included in the service.

| Service Identifier | Service Name | Service Description      | HSM Commands                                                                                                                  |
| ------------------ | ------------ | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| 3                  | `USER_MGMT`  | HSM user management      | • **createUser**<br>• **deleteUser**<br>• **changePswd** (applies only when changing the password of a<br>different HSM user) |
| 4                  | `MISC_CO`    | Miscellaneous CO service | • **setMValue**                                                                                                               |

To get the quorum minimum value for a service, use the **getMValue**
command, as in the following example.

```
`aws-cloudhsm >` `getMValue 3``MValue of service 3[USER_MGMT] on server 0 : [2]
MValue of service 3[USER_MGMT] on server 1 : [2]`
```

The output from the preceding **getMValue** command shows that the quorum
minimum value for HSM user management operations (service 3) is now two.

After you complete these steps, see [User management with quorum
authentication enabled for AWS CloudHSM Management Utility](quorum-authentication-crypto-officers.md "quorum-authentication-crypto-officers.md").

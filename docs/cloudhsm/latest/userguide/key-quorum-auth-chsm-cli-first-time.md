# Set up quorum authentication for AWS CloudHSM

crypto-users using CloudHSM CLI

These topics describe how to configure your CloudHSM for quorum authentication by
[crypto-users](understanding-users.md#crypto-user-chsm-cli "understanding-users.md#crypto-user-chsm-cli"). Perform these steps once during
initial setup. For subsequent key management and usage, refer to [Key management and usage with quorum
authentication enabled for AWS CloudHSM using CloudHSM CLI](key-quorum-auth-chsm-cli-crypto-user.md "key-quorum-auth-chsm-cli-crypto-user.md").

###### Topics

- [Prerequisites](#key-quorum-crypto-user-prerequisites "#key-quorum-crypto-user-prerequisites")
- [Step 1. Create and register a key for
  signing](#key-quorum-crypto-user-create-and-register-key "#key-quorum-crypto-user-create-and-register-key")
- [Step 2. Set the key quorum values during key generation](#key-quorum-admin-set-quorum-minimum-value-chsm-cli "#key-quorum-admin-set-quorum-minimum-value-chsm-cli")

## Prerequisites

- Familiarity with the [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md")

## Step 1. Create and register a key for

signing

To use quorum authentication, each crypto-user must complete _all_ of
the following steps:

###### Topics

- [Create an RSA key pair](#key-mofn-key-pair-create-chsm-cli "#key-mofn-key-pair-create-chsm-cli")
- [Create a registration token](#key-mofn-registration-token-chsm-cli "#key-mofn-registration-token-chsm-cli")
- [Sign the unsigned registration token](#key-mofn-sign-registration-token-chsm-cli "#key-mofn-sign-registration-token-chsm-cli")
- [Register the public key with the HSM](#key-mofn-register-key-chsm-cli "#key-mofn-register-key-chsm-cli")

### Create an RSA key pair

There are many different ways to create and protect a key pair. The following examples
show how to do it with [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/").

###### Example– Create a private key with OpenSSL

The following example demonstrates how to use OpenSSL to create a 2048-bit RSA key. To use this example, replace
`<crypto_user1.key>` with the name of the file where you want to store the key.

````
`$` `openssl genrsa -out `<crypto_user1.key>```Generating RSA private key, 2048 bit long modulus
.....................................+++
.+++
e is 65537 (0x10001)`
````

Next, generate the public key using the private key that you just created.

###### Example– Create a public key with OpenSSL

The following example demonstrates how to use OpenSSL to create a public key from the
private key you just created.

```
`$` `openssl rsa -in crypto_user1.key -outform PEM -pubout -out crypto_user1.pub``writing RSA key`
```

### Create a registration token

You create a token and sign it with the private key you just generated in the previous
step.

###### Create a registration token

1. Use the following command to start the CloudHSM CLI:

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Create a registration token by running the [quorum token-sign generate](cloudhsm_cli-qm-token-gen.md "cloudhsm_cli-qm-token-gen.md") command:

```
`aws-cloudhsm >` `quorum token-sign generate --service registration --token /path/tokenfile``{
 "error_code": 0,
 "data": {
 "path": "/path/tokenfile"
 }
}`
```

3. The [quorum token-sign generate](cloudhsm_cli-qm-token-gen.md "cloudhsm_cli-qm-token-gen.md") command generates a registration token at the specified file path. Inspect the token file:

```
`$` `cat /path/tokenfile``{
 "version": "2.0",
 "tokens": [
 {
 "approval_data": `<approval data in base64 encoding>`,
 "unsigned": `<unsigned token in base64 encoding>`,
 "signed": ""
 }
 ]
}`
```

The token file consists of the following:

    * **approval\_data**: A base64 encoded randomized data token whose raw data doesn’t exceed the maximum of 245 bytes.
    * **unsigned**: A base64 encoded and SHA256 hashed token of the approval\_data.
    * **signed**: A base64 encoded signed token (signature) of the unsigned token, using the RSA 2048-bit private key previously generated with OpenSSL.

You sign the unsigned token with the private key to demonstrate that you have access to the private key. You will need the registration token file fully populated with a signature and
the public key to register the crypto-user as a quorum user with the AWS CloudHSM cluster.

### Sign the unsigned registration token

1. Decode the base64 encoded unsigned token and place it into a binary file:

```
`$` `echo -n '6BMUj6mUjjko6ZLCEdzGlWpR5sILhFJfqhW1ej3Oq1g=' | base64 -d > crypto_user.bin`
```

2. Use OpenSSL and the private key to sign the now binary unsigned registration token and create a binary signature file:

```
`$` `openssl pkeyutl -sign \
-inkey crypto_user1.key \
-pkeyopt digest:sha256 \
-keyform PEM \
-in crypto_user.bin \
-out crypto_user.sig.bin`
```

3. Encode the binary signature into base64:

```
`$` `base64 -w0 crypto_user.sig.bin > crypto_user.sig.b64`
```

4. Copy and paste the base64 encoded signature into the token file:

```
`{
 "version": "2.0",
 "tokens": [
 {
 "approval_data": `<approval data in base64 encoding>`,
 "unsigned": `<unsigned token in base64 encoding>`,
 "signed": `<signed token in base64 encoding>`
 }
 ]
}`
```

### Register the public key with the HSM

After creating a key, the crypto-user must register the public key with the AWS CloudHSM cluster.

1. Start CloudHSM CLI:

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Sign in as the crypto-user whose public key you want to register.

```
`aws-cloudhsm >` `login --username crypto_user1 --role crypto-user``Enter password:
{
 "error_code": 0,
 "data": {
 "username": "crypto_user1",
 "role": "crypto-user"
 }
}`
```

3. Register the public key with the **[Register a user's token-sign quorum strategy
   using CloudHSM CLI](cloudhsm_cli-user-chqm-token-reg.md "cloudhsm_cli-user-chqm-token-reg.md")**. For more
   information, see the following example or use the **help user change-quorum token-sign register** command.

###### Example– Register a public key with AWS CloudHSM cluster

The following example shows how to use the **user change-quorum token-sign register**
command in CloudHSM CLI to register a crypto-user public key with the HSM. To use this command, the crypto-user must be logged in to the HSM. Replace
these values with your own:

````
`aws-cloudhsm >` `user change-quorum token-sign register --public-key `</path/crypto_user.pub>` --signed-token `</path/tokenfile>```{
 "error_code": 0,
 "data": {
 "username": "crypto_user1",
 "role": "crypto-user"
 }
}`
````

###### Note

**/path/crypto_user.pub**: The filepath to the public key PEM file

**Required**: Yes

**/path/token_file**: The filepath with token signed by user private key

**Required**: Yes 4. After all crypto-users register their public keys, the output from the **user list** command shows this in the quorum field, stating the enabled quorum strategy in use.

In this example, the AWS CloudHSM cluster has two HSMs, each with the same crypto-users, as
shown in the following output from the **user list** command. For more
information about creating users, see [User management with
CloudHSM CLI](manage-hsm-users-chsm-cli.md "manage-hsm-users-chsm-cli.md").

```
`aws-cloudhsm >` `user list``{
 "error_code": 0,
 "data": {
 "users": [
 {
 "username": "admin",
 "role": "admin",
 "locked": "false",
 "mfa": [],
 "quorum": [],
 "cluster-coverage": "full"
 },
 {
 "username": "crypto_user1",
 "role": "crypto-user",
 "locked": "false",
 "mfa": [],
 "quorum": [
 {
 "strategy": "token-sign",
 "status": "enabled"
 }
 ],
 "cluster-coverage": "full"
 },
 {
 "username": "crypto_user2",
 "role": "crypto-user",
 "locked": "false",
 "mfa": [],
 "quorum": [
 {
 "strategy": "token-sign",
 "status": "enabled"
 }
 ],
 "cluster-coverage": "full"
 },
 {
 "username": "crypto_user3",
 "role": "crypto-user",
 "locked": "false",
 "mfa": [],
 "quorum": [
 {
 "strategy": "token-sign",
 "status": "enabled"
 }
 ],
 "cluster-coverage": "full"
 },
 {
 "username": "app_user",
 "role": "internal(APPLIANCE_USER)",
 "locked": "false",
 "mfa": [],
 "quorum": [],
 "cluster-coverage": "full"
 }
 ]
 }
}`
```

## Step 2. Set the key quorum values during key generation

To use quorum authentication, a crypto-user must log in to the HSM and then set the associated
_key quorum values_. This is the minimum number of crypto-user approvals that
are required to perform HSM key management/usage operations. For more information about the associated key commands associated with either key management or key usage,
see [Supported services and types](key-quorum-auth-chsm-cli-service-names.md "key-quorum-auth-chsm-cli-service-names.md").

###### Generate a key pair with key quorum values set

1. Use the following command to start CloudHSM CLI:

Linux

```
`$` `/opt/cloudhsm/bin/cloudhsm-cli interactive`
```

Windows

```
`PS C:\>` `& "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive`
```

2. Using CloudHSM CLI, log in as a crypto-user.

```
`aws-cloudhsm >` `login --username crypto_user1 --role crypto-user``Enter password:
{
 "error_code": 0,
 "data": {
 "username": "crypto_user1",
 "role": "crypto-user"
 }
}`
```

This example generates an RSA key pair which has key quorum values of two (2) set for both
key-management and key-usage operations. You can choose any value from zero (0) to eight (8),
up to the total number of crypto-users on the HSM. In this example, the HSM has three (3)
crypto-users, so the maximum possible value is three (3). Note that in this example we are
sharing the key with `<crypto_user2>` during key generation.
Also note that public keys do not have quorum values.

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
--public-exponent 65537 \
--modulus-size-bits 2048 \
--public-label rsa-public-key-example \
--private-label rsa-private-key-example \
--public-attributes verify=true \
--private-attributes sign=true
--share-crypto-users crypto_user2 \
--manage-private-key-quorum-value 2 \
--use-private-key-quorum-value 2``{
 "error_code": 0,
 "data": {
 "public_key": {
 "key-reference": "0x0000000000640006",
 "key-info": {
 "key-owners": [
 {
 "username": "crypto_user",
 "key-coverage": "full"
 }
 ],
 "shared-users": [],
 "key-quorum-values": {
 "manage-key-quorum-value": 0,
 "use-key-quorum-value": 0
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "rsa-public-key-example",
 "id": "0x",
 "check-value": "0x218f50",
 "class": "public-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": false,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": false,
 "sign": false,
 "trusted": false,
 "unwrap": false,
 "verify": true,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 512,
 "public-exponent": "0x010001",
 "modulus": "0xbdf471a3d2a869492f51c767bece8780730ae6479a9a75efffe7cea3594fb28ca518630e7b1d988b45d2fedc830b7ab848448c24c476cacb73d1523278aed289551e07af0fbfabe4811cc4601678bd097b5c0a578249ed1eb0e4878a80ba1ed85ac46eb1fee60d2a8bdd322075196dec4b57fa2cd82af44ad068115ac219bc073ec65c19c97bd883cf26931408d7bc51e237626b8b9b8f2485425907a0eb42f2f4c40018c8dac7ceeb1b646305a2e537ab904346883e41d568264abee0137048e4657d2cf72801810f3212f662b7a7ae134848b922771f6a30aa76718008d9cc74ff8ddcd8d867b05c3d40020d1514999af96889911467191b9f390d8de07f83",
 "modulus-size-bits": 2048
 }
 },
 "private_key": {
 "key-reference": "0x0000000000640007",
 "key-info": {
 "key-owners": [
 {
 "username": "crypto_user",
 "key-coverage": "full"
 }
 ],
 "shared-users": [
 {
 "username": "crypto_user2",
 "key-coverage": "full"
 }
 ],
 "key-quorum-values": {
 "manage-key-quorum-value": 2,
 "use-key-quorum-value": 2
 },
 "cluster-coverage": "full"
 },
 "attributes": {
 "key-type": "rsa",
 "label": "rsa-private-key-example",
 "id": "0x",
 "check-value": "0x218f50",
 "class": "private-key",
 "encrypt": false,
 "decrypt": false,
 "token": true,
 "always-sensitive": true,
 "derive": false,
 "destroyable": true,
 "extractable": true,
 "local": true,
 "modifiable": true,
 "never-extractable": false,
 "private": true,
 "sensitive": true,
 "sign": true,
 "trusted": false,
 "unwrap": false,
 "verify": false,
 "wrap": false,
 "wrap-with-trusted": false,
 "key-length-bytes": 1216,
 "public-exponent": "0x010001",
 "modulus": "0xbdf471a3d2a869492f51c767bece8780730ae6479a9a75efffe7cea3594fb28ca518630e7b1d988b45d2fedc830b7ab848448c24c476cacb73d1523278aed289551e07af0fbfabe4811cc4601678bd097b5c0a578249ed1eb0e4878a80ba1ed85ac46eb1fee60d2a8bdd322075196dec4b57fa2cd82af44ad068115ac219bc073ec65c19c97bd883cf26931408d7bc51e237626b8b9b8f2485425907a0eb42f2f4c40018c8dac7ceeb1b646305a2e537ab904346883e41d568264abee0137048e4657d2cf72801810f3212f662b7a7ae134848b922771f6a30aa76718008d9cc74ff8ddcd8d867b05c3d40020d1514999af96889911467191b9f390d8de07f83",
 "modulus-size-bits": 2048
 }
 }
 }
}`
```

When generating a key with quorum controls, the key must be associated with a minimum number of users equal to the largest key quorum value.
Associated users include the key owner and Crypto Users with whom the key is shared with. To determine the number of minimum users to share the key with,
get the largest quorum value between the key usage quorum value and the key management quorum value and subtract 1 to account for the key owner,
who is by default associated with the key. To share the key with more users, use
the **[Share a key using CloudHSM CLI](cloudhsm_cli-key-share.md "cloudhsm_cli-key-share.md")** command.

Failure to share the key with enough users at key generation will result in failure, as
shown below.

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
--public-exponent 65537 \
--modulus-size-bits 2048 \
--public-label rsa-public-key-example \
--private-label rsa-private-key-example \
--public-attributes verify=true \
--private-attributes sign=true
--share-crypto-users crypto_user2 crypto_user3 \
--manage-private-key-quorum-value 3 \
--use-private-key-quorum-value 4``{
 "error_code": 1,
 "data": "Invalid quorum value provided."
}`
```

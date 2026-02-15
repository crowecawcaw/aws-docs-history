# Generate asymmetric keys using

CloudHSM CLI

Use the commands listed in **[The generate-asymmetric-pair
category in CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair.md "cloudhsm_cli-key-generate-asymmetric-pair.md")** to generate
asymmetric key pairs for AWS CloudHSM clusters.

## Generate an RSA key

Use the **key generate-asymmetric-pair rsa** command to generate an RSA key pair. To see all available options, use the **help key generate-asymmetric-pair rsa** command.

###### Example

The following example generates an RSA 2048-bit key pair.

```
`aws-cloudhsm >` `key generate-asymmetric-pair rsa \
 --public-exponent 65537 \
 --modulus-size-bits 2048 \
 --public-label rsa-public-example \
 --private-label rsa-private-example`
```

### Arguments

**`<PUBLIC_LABEL>`**

Specifies a user-defined label for the public-key.

Required: Yes

**`<PRIVATE_LABEL>`**

Specifies a user-defined label for the private-key.

Required: Yes

**`<MODULUS_SIZE_BITS>`**

Specifies the length of the modulus in bits. The minimum value is 2048.

Required: Yes

**`<PUBLIC_EXPONENT>`**

Specifies the public exponent. The value must be an odd number greater than or equal to 65537.

Required: Yes

**`<PUBLIC_KEY_ATTRIBUTES>`**

Specifies a space-separated list of key attributes to set for the generated RSA public key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`).

For a list of supported AWS CloudHSM key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends.
Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key.
Do not use a session key to encrypt data that you might need to decrypt after the session ends.

To change a session key to a persistent (token) key, use [key set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md").

By default, when keys are generated they are persistent/token keys. Using <SESSION> changes this, ensuring a key generated with this argument is a session/ephemeral

Required: No

### Generate EC (elliptic curve cryptography) key pairs

Use the **key generate-asymmetric-pair ec** command to generate an EC key pair.
To see all available options,including a list of the supported elliptic curves, use the **help key generate-asymmetric-pair ec** command.

###### Example

The following example generates an EC key pair using the Secp384r1 elliptic curve.

```
`aws-cloudhsm >` `key generate-asymmetric-pair ec \
 --curve secp384r1 \
 --public-label ec-public-example \
 --private-label ec-private-example`
```

#### Arguments

**`<PUBLIC_LABEL>`**

Specifies a user-defined label for the public-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.

Required: Yes

**`<PRIVATE_LABEL>`**

Specifies a user-defined label for the private-key. The maximum size allowable for `label` is 127 characters for Client SDK 5.11 and after. Client SDK 5.10 and before has a limit of 126 characters.

Required: Yes

**`<CURVE>`**

Specifies the identifier for the elliptic curve.

Valid values:

- prime256v1
- secp256r1
- secp224r1
- secp384r1
- secp256k1
- secp521r1
- ed25519 (only supported on hsm2m.medium instances in non-FIPS mode)

Required: Yes

**`<PUBLIC_KEY_ATTRIBUTES>`**

Specifies a space-separated list of key attributes to set for the generated EC public key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `verify=true`).

For a list of supported AWS CloudHSM key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<PRIVATE_KEY_ATTRIBUTES>`**

Specifies a space-separated list of key attributes to set for the generated EC private key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`).

For a list of supported AWS CloudHSM key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").

Required: No

**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends.
Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key.
Do not use a session key to encrypt data that you might need to decrypt after the session ends.

To change a session key to a persistent (token) key, use [key set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md").

By default, keys that are generated are persistent (token) keys. Passing in <SESSION> changes this, ensuring a key generated with this argument is a session (ephemeral) key.

Required: No

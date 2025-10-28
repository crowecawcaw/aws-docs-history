# How to use trusted keys to wrap data keys in AWS CloudHSM

To use a trusted key to wrap a data key in AWS CloudHSM, you must complete three basic steps:

1. For the data key you plan to wrap with a trusted key, set its `CKA_WRAP_WITH_TRUSTED` attribute to true.
2. For the trusted key you plan to wrap the data key with, set its `CKA_TRUSTED` attribute to true.
3. Use the trusted key to wrap the data key.

## Step 1: Set the data key's `CKA_WRAP_WITH_TRUSTED` to true

For the data key you want to wrap, choose one of the following options to set the key’s `CKA_WRAP_WITH_TRUSTED`
attribute to true. Doing this restricts the data key so applications can only use trusted keys to wrap it.

### Option 1: If generating a new key, set `CKA_WRAP_WITH_TRUSTED` to true

Generate a key using [PKCS #11](pkcs11-library.md "pkcs11-library.md"), [JCE](java-library.md "java-library.md"), or [CloudHSM CLI](cloudhsm_cli.md "cloudhsm_cli.md"). See the following examples for more details.

PKCS #11
To generate a key with PKCS #11, you need to set the key's `CKA_WRAP_WITH_TRUSTED` attribute to true. As shown in the following example, do this by including this attribute in the key’s `CK_ATTRIBUTE template`
and then setting the attribute to true:

```
CK_BYTE_PTR label = "test_key";
CK_ATTRIBUTE template[] = {
        {CKA_WRAP_WITH_TRUSTED, &true_val,         sizeof(CK_BBOOL)},
        {CKA_LABEL,             label,             strlen(label)},
        ...
};
```

For more information, see [our public samples demonstrating key generation with PKCS #11](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/generate "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/generate").

JCE
To generate a key with JCE, you need to set the key's `WRAP_WITH_TRUSTED` attribute to true. As shown in the following example, do this by including this attribute in the key’s `KeyAttributesMap`
and then setting the attribute to true:

```
final String label = "test_key";
final KeyAttributesMap keySpec = new KeyAttributesMap();
keySpec.put(KeyAttribute.WRAP_WITH_TRUSTED, true);
keySpec.put(KeyAttribute.LABEL, label);
...
```

For more information, see [our public samples demonstrating key generation with JCE](java-samples.md#java-samples-code_5 "java-samples.md#java-samples-code_5").

CloudHSM CLI
To generate a key with CloudHSM CLI, you need to set the key's `wrap-with-trusted` attribute to true. Do this by including `wrap-with-trusted=true` in the appropriate argument for the key generation command:

- For symmetric keys, add `wrap-with-trusted` to the `attributes` argument.
- For public keys, add `wrap-with-trusted` to the `public-attributes` argument.
- For private keys, add `wrap-with-trusted` to the `private-attributes` argument.

For more information on key pair generation, see [The generate-asymmetric-pair
category in CloudHSM CLI](cloudhsm_cli-key-generate-asymmetric-pair.md "cloudhsm_cli-key-generate-asymmetric-pair.md").

For more information on symmetric key generation, see [The generate-symmetric category in
CloudHSM CLI](cloudhsm_cli-key-generate-symmetric.md "cloudhsm_cli-key-generate-symmetric.md").

### Option 2: If using an existing key, use CloudHSM CLI to set its `CKA_WRAP_WITH_TRUSTED` to true

To set an existing key's `CKA_WRAP_WITH_TRUSTED` attribute to true, follow these steps:

1. Use the [Log in to an HSM using CloudHSM CLI](cloudhsm_cli-login.md "cloudhsm_cli-login.md") command to log in as a crypto user (CU).
2. Use the [Set the attributes of keys with
   CloudHSM CLI](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md") command to set the key's `wrap-with-trusted` attribute to true.

```
`aws-cloudhsm >` `key set-attribute --filter attr.label=test_key --name wrap-with-trusted --value true`
`{
 "error_code": 0,
 "data": {
 "message": "Attribute set successfully"
 }
}`
```

## Step 2: Set the trusted key's `CKA_TRUSTED` to true

To make a key a trusted key, its `CKA_TRUSTED` attribute must be set to true. You can either use CloudHSM CLI or the CloudHSM Management Utility (CMU) to do this.

- If using CloudHSM CLI to set a key's `CKA_TRUSTED` attribute, see [Mark a key as trusted using
  CloudHSM CLI](manage-keys-cloudhsm-cli-trusted.md "manage-keys-cloudhsm-cli-trusted.md").
- If using the CMU to set a key's `CKA_TRUSTED` attribute, see [How to mark a key as trusted with
  the AWS CloudHSM Management Utility](cloudhsm_using_trusted_keys_control_key_wrap.md "cloudhsm_using_trusted_keys_control_key_wrap.md").

## Step 3. Use the trusted key to wrap the data key

To wrap the data key referenced in Step 1 with the trusted key you set in Step 2, refer to the following links for code samples. Each demonstrates how to wrap keys.

- [AWS CloudHSM PKCS #11 examples](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/wrapping "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/tree/master/src/wrapping")
- [AWS CloudHSM JCE examples](https://github.com/aws-samples/aws-cloudhsm-jce-examples/tree/sdk5/src/main/java/com/amazonaws/cloudhsm/examples "https://github.com/aws-samples/aws-cloudhsm-jce-examples/tree/sdk5/src/main/java/com/amazonaws/cloudhsm/examples")

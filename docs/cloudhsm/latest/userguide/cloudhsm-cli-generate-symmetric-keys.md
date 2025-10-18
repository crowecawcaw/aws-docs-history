# Generate symmetric keys with
 CloudHSM CLI

Use the commands listed in **[The generate-symmetric category in
 CloudHSM CLI](cloudhsm_cli-key-generate-symmetric.md "cloudhsm_cli-key-generate-symmetric.md")** to generate symmetric keys
 for AWS CloudHSM. To see all available options, use the **help key
 generate-symmetric** command.


## Generate an AES key


Use the **key generate-symmetric aes** command to generate AES keys. To see all available options, use the **help key generate-symmetric aes** command.


The following example generates a 32-byte AES key.


```
`aws-cloudhsm >` `key generate-symmetric aes \
 --label aes-example \
 --key-length-bytes 32`
```

### Arguments




**`<LABEL>`**

Specifies a user-defined label for the AES key.


Required: Yes



**`<KEY-LENGTH-BYTES>`**

Specifies the key length in bytes.


Valid values:


* 16, 24, and 32

Required: Yes



**`<KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated AES key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`)


For a list of supported AWS CloudHSM key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").


Required: No



**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends. 
 Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key. 
 Do not use a session key to encrypt data that you might need to decrypt after the session ends.


To change a session key to a persistent (token) key, use [key set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md").


By default, when keys are generated they are persistent/token keys. Using <SESSION> changes this, ensuring a key generated with this argument is a session/ephemeral


Required: No




### Generate generic secret key


Use the **key generate-symmetric generic-secret** command to generate generic secret keys. To see all available options, use the **help key generate-symmetric generic-secret** command.


The following example generates a 32-byte generic secret key.


```
`aws-cloudhsm >` `key generate-symmetric generic-secret \
 --label generic-secret-example \
 --key-length-bytes 32`
```

#### Arguments




**`<LABEL>`**

Specifies a user-defined label for the generic secret key.


Required: Yes



**`<KEY-LENGTH-BYTES>`**

Specifies the key length in bytes.


Valid values:


* 1 to 800

Required: Yes



**`<KEY_ATTRIBUTES>`**

Specifies a space separated list of key attributes to set for the generated generic secret key in the form of `KEY_ATTRIBUTE_NAME=KEY_ATTRIBUTE_VALUE` (for example, `sign=true`)


For a list of supported AWS CloudHSM key attributes, see [Key attributes for CloudHSM CLI](cloudhsm_cli-key-attributes.md "cloudhsm_cli-key-attributes.md").


Required: No



**`<SESSION>`**

Creates a key that exists only in the current session. The key cannot be recovered after the session ends. 
 Use this parameter when you need a key only briefly, such as a wrapping key that encrypts, and then quickly decrypts, another key. 
 Do not use a session key to encrypt data that you might need to decrypt after the session ends.


To change a session key to a persistent (token) key, use [key set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md").


By default, when keys are generated they are persistent/token keys. Using <SESSION> changes this, ensuring a key generated with this argument is a session/ephemeral


Required: No

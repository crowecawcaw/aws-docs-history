# Mark a key as trusted using

CloudHSM CLI

The content in this section provides instructions on using CloudHSM CLI to mark a key as trusted.

1. Using the [CloudHSM CLI login command](cloudhsm_cli-login.md "cloudhsm_cli-login.md"), log in as a crypto user (CU).
2. Use the **key list** command to identify the key reference of the key you want to mark as trusted. The following example lists the key with the label `key_to_be_trusted`.

```
`aws-cloudhsm >` `key list --filter attr.label=test_aes_trusted``{
 "error_code": 0,
 "data": {
 "matched_keys": [
 {
 "key-reference": "0x0000000000200333",
 "attributes": {
 "label": "test_aes_trusted"
 }
 }
 ],
 "total_key_count": 1,
 "returned_key_count": 1
 }
}`
```

3. Using the [Log out of an HSM using CloudHSM CLI](cloudhsm_cli-logout.md "cloudhsm_cli-logout.md") command, log out as a crypto user (CU).
4. Using the [Log in to an HSM using CloudHSM CLI](cloudhsm_cli-login.md "cloudhsm_cli-login.md") command, log in as an admin.
5. Using the [key set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md") command with the key reference you identified in step 2, set the key's trusted value to true:

```
`aws-cloudhsm >` `key set-attribute --filter key-reference=`<Key Reference>` --name trusted --value true``{
 "error_code": 0,
 "data": {
 "message": "Attribute set successfully"
 }
}`
```

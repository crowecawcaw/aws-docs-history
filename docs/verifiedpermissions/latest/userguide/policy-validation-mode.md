

# Enabling Amazon Verified Permissions policy validation mode
<a name="policy-validation-mode"></a>

You can set the policy validation mode in Verified Permissions to control whether policy changes are validated against the [schema](schema.md) in your policy store.

**Important**  
When you turn on policy validation, all attempts to create or update a policy or policy template are validated against the schema in the policy store. Verified Permissions rejects the request attempt if validation fails. For this reason, we recommend leaving validation off while you're developing your application and turning it on for testing and leaving it on while your application is in production.

------
#### [ AWS Management Console ]

**To set the policy validation mode for a policy store**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. Choose **Settings**.

1. In the **Policy validation mode** section, choose **Modify**.

1. Do one of the following:
   + To activate policy validation and enforce that all policy changes must be validated against your schema, choose the **Strict (recommended)** radio button. 
   + To turn off policy validation for policy changes, choose the **Off** radio button. Type `confirm` to confirm that updates to policies will no longer be validated against your schema.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To set the validation mode for a policy store**  
You can change the validation mode for a policy store by using the [UpdatePolicyStore](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html) operation and specifying a different value for the [ValidationSettings](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html#amazonverifiedpermissions-UpdatePolicyStore-request-ValidationSettings) parameter.

```
$ aws verifiedpermissions update-policy-store \
    --validation-settings "mode=OFF",
    --policy-store-id PSEXAMPLEabcdefg111111
{
    "createdDate": "2023-05-17T18:36:10.134448+00:00",
    "lastUpdatedDate": "2023-05-17T18:36:10.134448+00:00",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "validationSettings": {
        "Mode": "OFF"
    }
}
```

------

For more information, see [Policy validation](https://docs.cedarpolicy.com/policies/validation.html) in the *Cedar policy language Reference Guide*.
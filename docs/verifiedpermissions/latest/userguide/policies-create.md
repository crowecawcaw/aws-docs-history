

# Creating Amazon Verified Permissions static policies
<a name="policies-create"></a>

You can create a static policy for principals to permit or forbid them from performing specified actions on specified resources for your application. A static policy has specific values included for the `principal` and `resource` and are ready to be used in authorization decisions. 

------
#### [ AWS Management Console ]

**To create a static policy**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. In the navigation pane on the left, choose **Policies**.

1. Choose **Create policy** and then choose **Create static policy**.
**Note**  
If you have a policy statement you'd like to use, skip to **Step 8** and paste the policy into the **Policy** section on the next page.

1. In the **Policy effect** section, choose whether the policy will **Permit** or **Forbid** when a request matches the policy. If you choose **Permit**, the policy allows the principals to perform the actions on the resources. Conversely, if you choose **Forbid**, the policy doesn't allow the principals to perform the actions on the resources.

1. In the **Principals scope** field, choose the scope of the principals that the policy will apply to.
   + Choose **Specific principal** to apply the policy to a specific principal. Specify the entity type and identifier for the principal that will be permitted or forbidden to take the actions specified in the policy.
   + Choose **Group of principals** to apply the policy to a group of principals. Type the principal group name in the **Group of principals** field.
   + Choose **All principals** to apply the policy to all principals in your policy store.

1. In the **Resources scope** field, choose the scope of the resources that the policy will apply to.
   + Choose **Specific resources** to apply the policy to a specific resource. Specify the entity type and identifier for the resource that the policy should apply to.
   + Choose **Group of resources** to apply the policy to a group of resources. Type the resource group name in the **Group of resources** field.
   + Choose **All resources** to apply the policy to all resources in your policy store.

1. In the **Actions scope** section, choose the scope of the resources that the policy will apply to.
   + Choose **Specific set of actions** to apply the policy to a set of actions. Select the check boxes next to the actions to apply the policy.
   + Choose **All actions** to apply the policy to all actions in your policy store.

1. Choose **Next**.

1. In the **Policy** section, review your Cedar policy. You can choose **Format** to format the syntax of your policy with the recommended spacing and indentation. For more information, see [Basic policy construction in Cedar](https://docs.cedarpolicy.com/policies/syntax-policy.html) in the Cedar policy language Reference Guide.

1. In the **Details** section, type an optional description of the policy.

1. Choose **Create policy**.

------
#### [ AWS CLI ]

**To create a static policy**  
You can create a static policy by using the [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) operation. The following example creates a simple static policy.

```
$ aws verifiedpermissions create-policy \
    --definition "{ \"static\": { \"Description\": \"MyTestPolicy\", \"Statement\": \"permit(principal,action,resource) when {principal.owner == resource.owner};\"}}" \
    --policy-store-id PSEXAMPLEabcdefg111111
{
"Arn": "arn:aws:verifiedpermissions::123456789012:policy/PSEXAMPLEabcdefg111111/SPEXAMPLEabcdefg111111",
    "createdDate": "2023-05-16T20:33:01.730817+00:00",
    "lastUpdatedDate": "2023-05-16T20:33:01.730817+00:00",
    "policyId": "SPEXAMPLEabcdefg111111",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyType": "STATIC"
}
```

**To create a policy with a policy name**  
You can optionally specify a policy name when creating a policy. The name must be unique for all policies within the policy store and prefixed with `name/`. You can use the name in place of the policy ID.

```
$ aws verifiedpermissions create-policy \
    --definition "{ \"static\": { \"Statement\": \"permit(principal, action, resource in Album::\\\"public_folder\\\");\"}}" \
    --policy-store-id PSEXAMPLEabcdefg111111 \
    --name name/example-policy
{
    "createdDate": "2023-06-12T20:33:37.382907+00:00",
    "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00",
    "policyId": "SPEXAMPLEabcdefg111111",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyType": "STATIC",
    "resource": {
        "entityId": "public_folder",
        "entityType": "Album"
    }
}
```

**Note**  
If you specify a name that is already associated with another policy in the policy store, you receive a `ConflictException` error.

------
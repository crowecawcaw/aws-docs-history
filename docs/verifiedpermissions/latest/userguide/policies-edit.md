# Editing Amazon Verified Permissions static policies

You can edit an existing static policy in your policy store. You can only directly update static policies. To change
a template-linked policy, you must update the policy template. For more information, see [Editing Amazon Verified Permissions policy templates](policy-templates-edit.md "policy-templates-edit.md").

You can change the following elements of a static policy:

- The `action` referenced by the policy.
- A condition clause, such as `when` and `unless`.
  You can't change the following elements of a static policy. To change any of these elements you
  will need to delete and re-created the policy.

- A policy from a static policy to a template-linked policy.
- The effect of a static policy from `permit` or
  `forbid`.
- The `principal` referenced by a static policy.
- The `resource` referenced by a static policy.

AWS Management Console

###### To edit a static policy

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose
   **Policies**.
3. Choose the radio button next to the static policy to edit and then choose
   **Edit**.
4. In the **Policy body** section, update the
   `action` or condition clause of your static policy. You can't
   update the policy effect, `principal`, or
   `resource` of the policy.
5. Choose **Update policy**.

###### Note

If [policy validation](policy-validation-mode.md "policy-validation-mode.md")
is enabled in the policy store, then updating a static policy causes Verified Permissions to
validate the policy against the schema in the policy store. If the updated
static policy doesn't pass validation, the operation fails and the update
isn't saved.

AWS CLI

###### To edit a static policy

You can edit a static policy by using the [UpdatePolicy](../apireference/API_UpdatePolicy.md "../apireference/API_UpdatePolicy.md")
operation. The following example edits a simple static policy.

The example uses the file `definition.txt` to contain the policy
definition.

```
{
    "static": {
        "description":  "Grant everyone of janeFriends UserGroup access to the vacationFolder Album",
        "statement": "permit(principal in UserGroup::\"janeFriends\", action, resource in Album::\"vacationFolder\" );"
    }
}
```

The following command references that file.

```
`$` `aws verifiedpermissions create-policy \
 --definition file://definition.txt \
 --policy-store-id PSEXAMPLEabcdefg111111``{
 "createdDate": "2023-06-12T20:33:37.382907+00:00",
 "lastUpdatedDate": "2023-06-12T20:33:37.382907+00:00",
 "policyId": "SPEXAMPLEabcdefg111111",
 "policyStoreId": "PSEXAMPLEabcdefg111111",
 "policyType": "STATIC",
 "principal": {
 "entityId": "janeFriends",
 "entityType": "UserGroup"
 },
 "resource": {
 "entityId": "vacationFolder",
 "entityType": "Album"
 }
}`
```

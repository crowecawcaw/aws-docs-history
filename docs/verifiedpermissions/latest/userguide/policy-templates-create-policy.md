# Creating Amazon Verified Permissions template-linked policies

You can create template-linked policies, or policies that are based on a policy template, using the AWS Management Console,
AWS CLI, or the AWS SDKs. Template-linked policies stay linked to their policy templates. If you change the policy
statement in the policy template, any policies linked to that template automatically use the new
statement for all authorization decisions made from that moment forward.

For template-linked policy examples, see [Amazon Verified Permissions example template-linked policies](policy-templates-example-policies.md "policy-templates-example-policies.md").

AWS Management Console

###### To create a template-linked policy by instantiating a policy template

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose
   **Policies**.
3. Choose **Create policy** and then choose
   **Create template-linked policy**.
4. Choose the radio button next to the policy template to use and then choose
   **Next**.
5. Type the **Principal** and
   **Resource** to be used for this specific instance
   of the template-linked policy. The specified values are displayed in the **Policy
   statement preview** field.

###### Note

The **Principal** and
**Resource** values must have the same
formatting as static policies. For example, to specify the
`AdminUsers` group for the principal, type
`Group::"AdminUsers"`. If you type
`AdminUsers`, a validation error is displayed. 6. Choose **Create template-linked policy**.

The new template-linked policy is displayed under **Policies**.

AWS CLI

###### To create a template-linked policy by instantiating a policy template

You can create a template-linked policy that references an existing policy template and that specifies
values for any placeholders used by the template.

The following example creates a template-linked policy that uses a template with the
following statement:

```
permit(
    principal in ?principal,
    action == PhotoFlash::Action::"view",
    resource == PhotoFlash::Photo::"VacationPhoto94.jpg"
);
```

It also uses the following `definition.txt` file to supply
the value for the `definition` parameter:

```
{
    "templateLinked": {
        "policyTemplateId": "PTEXAMPLEabcdefg111111",
        "principal": {
            "entityType": "PhotoFlash::User",
            "entityId": "alice"
        }
    }
}
```

The output shows both the resource, which it gets from the template, and the
principal, which it gets from the definition parameter

```
`$` `aws verifiedpermissions create-policy \
 --definition file://definition.txt
 --policy-store-id PSEXAMPLEabcdefg111111``{
 "createdDate": "2023-05-22T18:57:53.298278+00:00",
 "lastUpdatedDate": "2023-05-22T18:57:53.298278+00:00",
 "policyId": "TPEXAMPLEabcdefg111111",
 "policyStoreId": "PSEXAMPLEabcdefg111111",
 "policyType": "TEMPLATELINKED",
 "principal": {
 "entityId": "alice",
 "entityType": "PhotoFlash::User"
 },
 "resource": {
 "entityId": "VacationPhoto94.jpg",
 "entityType": "PhotoFlash::Photo"
 }
}`
```

# Creating Amazon Verified Permissions policy templates

You can create policy templates in Verified Permissions using the AWS Management Console, the AWS CLI, or the
AWS SDKs. Policy templates allow a policy to be defined once and then used with multiple
principals and resources. Once you create a policy template you can then create
template-linked policies to use the policy templates with specific principals and resources.
For more information, see [Creating Amazon Verified Permissions template-linked policies](policy-templates-create-policy.md "policy-templates-create-policy.md").

AWS Management Console

###### To create a policy template

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose
   **Policy templates**.
3. Choose **Create policy template**.
4. In the **Details** section, type a **Policy template
   description**.
5. In the **Policy template body** section, use placeholders
   `?principal` and `?resource` to allow policies
   created based on this template to customize permissions they grant. You
   can choose **Format** to format the syntax of your policy template
   with the recommended spacing and indentation.
6. Choose **Create policy template**.

AWS CLI

###### To create a policy template

You can create a policy template by using the [CreatePolicyTemplate](../apireference/API_CreatePolicyTemplate.md "../apireference/API_CreatePolicyTemplate.md") operation. The following example creates a
policy template with a placeholder for the principal.

The file `template1.txt` contains the following.

```
"VacationAccess"
permit(
    principal in ?principal,
    action == Action::"view",
    resource == Photo::"VacationPhoto94.jpg"
);
```

```
`$` `aws verifiedpermissions create-policy-template \
 --description "Template for vacation picture access"
 --statement file://template1.txt
 --policy-store-id PSEXAMPLEabcdefg111111``{
 "createdDate": "2023-05-18T21:17:47.284268+00:00",
 "lastUpdatedDate": "2023-05-18T21:17:47.284268+00:00",
 "policyStoreId": "PSEXAMPLEabcdefg111111",
 "policyTemplateId": "PTEXAMPLEabcdefg111111"
}`
```

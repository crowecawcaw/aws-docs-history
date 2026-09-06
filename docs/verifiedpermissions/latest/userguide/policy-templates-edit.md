

# Editing Amazon Verified Permissions policy templates
<a name="policy-templates-edit"></a>

You can edit, or update, policy templates in Verified Permissions using the AWS Management Console, the AWS CLI, or the AWS SDKs. Editing a policy template will automatically update the policies that are linked to, or based on, the template so take care when editing the policy templates and make sure you don’t accidentally introduce a change that breaks your application.

You can change the following elements of a policy template:
+ The `action` referenced by the policy template
+ A condition clause, such as `when` and `unless`

You can't change the following elements of a policy template. To change any of these elements you will need to delete and re-created the policy template.
+ The effect of a policy template from `permit` or `forbid`
+ The `principal` referenced by a policy template
+ The `resource` referenced by a policy template

------
#### [ AWS Management Console ]

**To edit your policy templates**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. In the navigation pane on the left, choose **Policy templates**. The console displays all of the policy templates you created in the current policy store.

1. Choose the radio button next to a policy template to display details about the policy template, such as when the policy template was created, updated, and the policy template contents.

1. Choose **Edit** to edit your policy template. Update the **Policy description** and **Policy body** as necessary and then choose **Update policy template**.

1. You can delete a policy template by choosing the radio button next to a policy template and then choosing **Delete**. Choose **OK** to confirm deleting the policy template.

------
#### [ AWS CLI ]

**To edit a policy template**  
You can create a static policy by using the [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html) operation. The following example updates the specified policy template by replacing its policy body with a new policy defined in a file.

Contents of file `template1.txt`:

```
permit(
    principal in ?principal,
    action == Action::"view",
    resource in ?resource)
when {
    principal has department && principal.department == "research"
};
```

```
$ aws verifiedpermissions update-policy-template \
    --policy-template-id PTEXAMPLEabcdefg111111 \
    --description "My updated template description" \
    --statement file://template1.txt \ 
    --policy-store-id PSEXAMPLEabcdefg111111
{
    "createdDate": "2023-05-17T18:58:48.795411+00:00",
    "lastUpdatedDate": "2023-05-17T19:18:48.870209+00:00",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyTemplateId": "PTEXAMPLEabcdefg111111"
}
```

**To update the name of a policy template**  
You can set or update a policy template name when updating a policy template. The name must be unique for all policy templates within the policy store and prefixed with `name/`. If you don't include the name field in the update request, the existing name is unchanged. To remove a name, set it to an empty string.

```
$ aws verifiedpermissions update-policy-template \
    --policy-template-id PTEXAMPLEabcdefg111111 \
    --statement file://template1.txt \
    --policy-store-id PSEXAMPLEabcdefg111111 \
    --name name/example-policy-template
{
    "createdDate": "2023-05-17T18:58:48.795411+00:00",
    "lastUpdatedDate": "2023-05-17T19:18:48.870209+00:00",
    "policyStoreId": "PSEXAMPLEabcdefg111111",
    "policyTemplateId": "PTEXAMPLEabcdefg111111"
}
```

------
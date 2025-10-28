# Edit a workgroup

Editing a workgroup requires permissions to `UpdateWorkgroup` API
operations. See [Configure access to workgroups and tags](workgroups-access.md "workgroups-access.md")
and [Use IAM policies to control workgroup
access](workgroups-iam-policy.md "workgroups-iam-policy.md"). If
you are adding or editing tags, you also need to have permissions to
`TagResource`. See [Tag policy examples for
workgroups](tags-access-control.md#tag-policy-examples-workgroups "tags-access-control.md#tag-policy-examples-workgroups").

###### To edit a workgroup in the

console

1. In the Athena console navigation pane, choose
   **Workgroups**.
2. On the **Workgroups** page, select the button for the
   workgroup that you want to edit.
3. Choose **Actions**, **Edit**.
4. Change the fields as needed. For the list of fields, see [Create workgroup](creating-workgroups.md "creating-workgroups.md"). You can change all
   fields except for the workgroup's name. If you need to change the name, create
   another workgroup with the new name and the same settings.
5. Choose **Save changes**. The updated workgroup appears in the
   list on the **Workgroups** page.

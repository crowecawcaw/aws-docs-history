# Delete a workgroup

You can delete a workgroup if you have permissions to do so. The primary workgroup
cannot be deleted.

If you have permissions, you can delete an empty workgroup at any time. You can also
delete a workgroup that contains saved queries. In this case, before proceeding to
delete a workgroup, Athena warns you that saved queries are deleted.

If you delete a workgroup while you are in it, the console switches focus to the
primary workgroup. If you have access to it, you can run queries and view its
settings.

If you delete a workgroup, its settings and per-query data limit controls are deleted.
The workgroup-wide data limit controls remain in CloudWatch, and you can delete them there if
needed.

###### Important

Before deleting a workgroup, ensure that its users also belong to other workgroups
where they can continue to run queries. If the users' IAM policies allowed them to
run queries _only_ in this workgroup, and you delete it, they no
longer have permissions to run queries. For more information, see [Example policy for running queries in the primary workgroup](example-policies-workgroup.md#example4-run-in-primary-access "example-policies-workgroup.md#example4-run-in-primary-access").

###### To delete a workgroup in the

console

1. In the Athena console navigation pane, choose
   **Workgroups**.
2. On the **Workgroups** page, select the button for the
   workgroup that you want to delete.
3. Choose **Actions**, **Delete**.
4. At the **Delete workgroup** confirmation prompt, enter the
   name of the workgroup, and then choose **Delete**.
   To delete a workgroup with the API operation, use the `DeleteWorkGroup`
   action.

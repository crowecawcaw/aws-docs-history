# Use saved queries

You can use the Athena console to save, edit, run, rename, and delete the queries that you
create in the query editor.

## Considerations and limitations

- You can update the name, description, and query text of saved queries.
- You can only update the queries in your own account.
- You cannot change the workgroup or database to which the query belongs.
- Athena does not keep a history of query modifications. If you want to keep a
  particular version of a query, save it with a different name.

###### Note

Amazon Athena resources can now be accessed within Amazon SageMaker Unified Studio
(Preview), which helps you access your organization's data and act on it with the best tools. You can migrate saved queries from an Athena workgroup to a SageMaker Unified
Studio project, configure projects with existing Athena workgroups, and maintain
necessary permissions through IAM role updates. For more information, see [Migrating Amazon Athena resources to Amazon SageMaker Unified Studio
(Preview)](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena").

###### Topics

- [Save a query with a name](saved-queries-name.md "saved-queries-name.md")
- [Run a saved query](saved-queries-run.md "saved-queries-run.md")
- [Edit a saved query](saved-queries-edit.md "saved-queries-edit.md")
- [Rename or delete a saved query](saved-queries-rename-or-delete.md "saved-queries-rename-or-delete.md")
- [Rename an undisplayed saved query](saved-queries-rename-not-displayed.md "saved-queries-rename-not-displayed.md")
- [Delete an undisplayed saved query](saved-queries-delete-not-displayed.md "saved-queries-delete-not-displayed.md")
- [Use the Athena API to update saved queries](saved-queries-update-with-api.md "saved-queries-update-with-api.md")

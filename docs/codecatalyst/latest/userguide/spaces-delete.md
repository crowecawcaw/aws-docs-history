Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting a space

You can delete a space to remove access to all of the space's resources. You must
have the **Space administrator** role to delete a space.

###### Note

You cannot undo a space deletion.

After you have deleted a space, all space members will be unable to access
space resources. Billing for space resources will also stop, and any workflows that are
prompted by third-party source repositories will be stopped.

###### Note

Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

The information in this guide is provided for deleting spaces in CodeCatalyst that support
AWS Builder ID users. To learn more about the steps to set up and administer a space that
supports identity federation, see [Setup and administration for
CodeCatalyst spaces](../adminguide/what-is.md "../adminguide/what-is.md") in the _Amazon CodeCatalyst Administrator
Guide_.

###### To delete a space

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space.

###### Tip

If you belong to more than one space, choose a space in the top navigation
bar. 3. Choose **Settings**, and then choose **Delete**. 4. Type `delete` to confirm the deletion. 5. Choose **Delete**.

###### Note

If you belong to more than one space, you're redirected to the space overview
page. If you belong to one space, you're redirected to the space creation
page.

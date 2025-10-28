Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deleting account connections (in

CodeCatalyst)

You can delete an account connection that you no longer need. For this procedure, you
will use CodeCatalyst to delete an account connection that you have previously added to your
space. This deletes the account connection from your space, provided that the
account is not the billing account for the space.

###### Important

After an account connection is deleted, you cannot reconnect it. You must create a
new account connection and then associate
IAM
roles and environments, or set up billing, as needed.

A billing account must be designated for your CodeCatalyst space, even if usage for the
space will not exceed the Free tier. Before you can remove a space for an
account that is a designated billing account, you will need to add another account for
your space. See [Managing
billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the Amazon CodeCatalyst Administrator Guide.

###### Important

While you can use these steps to remove an account, this is not recommended. The
account might also be set up to support workflows in CodeCatalyst.

To manage account connections for your space, you must have the
**Space administrator** or **Power user**
role.

An account that has been removed can be added again later, but you must create a new
connection between the account and the space. You will need to re-associate any
IAM roles to the added account.

###### To delete an account connection

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your CodeCatalyst space. Choose **Settings**, and
   then choose **AWS accounts**.
3. Under **Amazon CodeCatalyst display name**, choose the selector next
   to the account connection that you want to remove.
4. Choose **Remove AWS account**. Confirm the deletion by
   entering the name in the field, and then choose
   **Remove**.

A success banner displays, and the account connection is removed from the list
of connections.

# Assign or add users or groups to a Transfer Family

web app

After you create a Transfer Family web app, you can assign users and groups who can then
access the web app. You can either retrieve users that are already created and
stored in IAM Identity Center, or you can [add new users directly](../../../singlesignon/latest/userguide/addusers.md "../../../singlesignon/latest/userguide/addusers.md")
(if you're using an IAM Identity Center directory as your identity provider). If you add new
users, they are also added to your IAM Identity Center instance.

Note the following:

- You can only add new users if you are using the IAM Identity Center directory as your
  identity source and have the proper permissions. If you are a member of an
  organization instance, you might not have the necessary permissions to add
  users.

###### Note

If you don't assign users or groups to your application, your users
will get an error when they attempt to log into your web app.

- If you create a new user, you must also create an S3 access grant for this
  user so that they can access data on your web app.
- After you create a new user, that user receives an onboarding email from
  IAM Identity Center with directions for how to proceed.

###### To assign users to a Transfer Family web app

1. Navigate to your web app list, and choose the one that you want to
   edit.
2. Choose **Assign users and groups**.

![Screen showing the details for a selected web app.](images/webapp-transfer-details.png) 3. To assign users that you previously created in IAM Identity Center, select
**Assign existing users and groups**. To create new
users, skip ahead to step 4.

    1. An information screen appears. Choose **Get
     started** to continue.
    2. Search for the user. Note that no users appear until you begin
     entering your search criteria. You must search by the
     *display name*, not the
     *username*, if different. Only exact matches
     are returned. If you can't find your user, navigate to the IAM Identity Center
     management console, find the user, then copy and paste their display
     name here.



    ![Screen showing the search dialog for adding users and groups to your web app.](images/webapp-transfer-add-user.png)
    3. Choose the users and groups to add, then choose
     **Assign**.

4. To create a new user, select **Add and assign new
   users**.
   1. An information screen appears. Choose **Get
      started** to continue.
   2. Choose **Add new users**.
   3. Enter the following user details into the dialog box: username,
      first and last name, and an email address.

   ![Screen showing the Add new users dialog.](images/webapp-transfer-add-user-new.png) 4. Choose **Next**, then choose
   **Add** to add the user and close the dialog
   box, or **Add new user** to create another
   user.

# Delete users in IAM Identity Center

When you delete a user in your IAM Identity Center directory, it removes their access to
 AWS accounts and applications. After you delete a user, you cannot undo this action.
 Use the
 following procedure to delete a user in your Identity Center directory.

###### Note

When you disable user access or delete a user in IAM Identity Center, that user will immediately
 be prevented from signing in to the AWS access portal and will not be able to create new
 sign in sessions. For more information, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").

###### Important

The instructions on this page apply to [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/"). They do not
 apply to [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM). IAM Identity Center
 users, groups, and user credentials are different from IAM users, groups, and
 IAM user credentials. If you are looking for instructions on deleting users in
 IAM, see [Deleting
 an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting") in the *AWS Identity and Access Management User
 Guide*.


Console
###### To delete a user

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Users**.
3. There are two ways you can delete a user:




	* On the **Users** page, you can select
	 multiple users for deletion. Select the username that you
	 want to delete and choose **Delete
	 users**.
	* Choose the username that you want to delete. On the user
	 details page, choose **Delete user**.
4. If you delete multiple users at once, confirm your intent by
 typing `Delete` in the **Delete user**
 dialog box.
5. Choose **Delete user**. If you selected multiple
 users for deletion, choose **Delete *#*
 users**.


AWS CLI
###### To delete a user


The following `delete-user` command deletes a user from
 your Identity Center directory.



```
aws identitystore delete-user \
    --identity-store-id d-1234567890 \
    --user-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

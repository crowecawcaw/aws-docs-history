# Delete groups in IAM Identity Center

When you delete a group in your IAM Identity Center directory, it removes access to AWS accounts
 and applications for all users who are members of this group. After a group is deleted
 it cannot be undone. Use the following procedure to delete a group in your Identity Center
 directory.

###### Important

The instructions on this page apply to [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/"). They do not
 apply to [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM). IAM Identity Center
 users, groups, and user credentials are different from IAM users, groups, and
 IAM user credentials. If you are looking for instructions on deleting groups in
 IAM, see [Deleting
 an IAM user group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_delete.html") in the *AWS Identity and Access Management User
 Guide*.


Console
###### To delete a group

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Groups**.
3. There are two ways you can delete a group:




	* On the **Groups** page, you can select
	 multiple groups for deletion. Select the group name that you
	 want to delete and choose **Delete group**.
	* Choose the group name that you want to delete. On the
	 group details page, choose **Delete group**
	 .
4. You might be asked to confirm your intent to delete the group.



	* If you delete multiple groups at once, confirm your intent
	 by typing `Delete` in the **Delete
	 group** dialog box.
	* If you delete a single group that contains users, confirm
	 your intent by typing the name of the group you want to
	 delete in the **Delete
	 group** dialog box.
5. Choose **Delete group**. If you selected multiple
 groups for deletion, choose **Delete *#*
 groups**.


AWS CLI
###### To delete a group


The following `delete-group` command deletes the specified
 group from your Identity Center directory.



```
aws identitystore delete-group \
    --identity-store-id d-1234567890 \
    --group-id a1b2c3d4-5678-90ab-cdef-EXAMPLE22222
```

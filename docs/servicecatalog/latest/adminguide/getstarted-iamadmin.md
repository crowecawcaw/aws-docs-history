# Grant permissions to AWS Service Catalog administrators

As a catalog administrator, you require access to the AWS Service Catalog administrator console view and
IAM permissions that allow you to perform tasks such as the following:

- Creating and managing portfolios
- Creating and managing products
- Adding template constraints to control the options that are available to end users when
  launching a product
- Adding launch constraints to define the IAM roles that AWS Service Catalog assumes when end users
  launch products
- Granting end users access to your products
  You, or an administrator who manages your IAM permissions, must attach policies to your IAM user,
  group, or role that are required to complete this tutorial.

######

To grant permissions
to a catalog administrator

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane,
   choose **Access management**,
   and then choose **Users**.
   If you already created
   an IAM user
   that you would like
   to use
   as the catalog administrator,
   choose the user name,
   and then choose **Add permissions**.
   Otherwise,
   create a user as follows:
   1. Choose **Add user**.
   2. For **User name**,
      type `ServiceCatalogAdmin`.
   3. Select **Programmatic access** and **AWS Management Console access**.
   4. Choose **Next: Permissions**.

3. Choose **Attach existing policies directly**.
4. Choose **Create policy**,
   and then do the following:
   1. Choose the **JSON** tab.
   2. Copy the following example policy, and paste it
      in **Policy Document**:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "ec2:CreateKeyPair",
                   "iam:AddRoleToInstanceProfile",
                   "iam:AddUserToGroup",
                   "iam:AttachGroupPolicy",
                   "iam:CreateAccessKey",
                   "iam:CreateGroup",
                   "iam:CreateInstanceProfile",
                   "iam:CreateLoginProfile",
                   "iam:CreateRole",
                   "iam:CreateUser",
                   "iam:Get*",
                   "iam:List*",
                   "iam:PutRolePolicy",
                   "iam:UpdateAssumeRolePolicy"
               ],
               "Resource": [
                   "*"
               ]
           }
       ]
   }
   ```

   3. Choose **Next: Tags**.
   4. (Optional) Choose **Add tag**
      to associate a key-value pair
      with the resource.
      You can add a maximum
      of 50 tags.

   ###### Note

   Tags are key-value pairs
   that you can add
   to resources.
   This helps identify, organize, and search
   for resources.
   For more information,
   see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md")
   in the _AWS General Reference Reference Guide_. 5. Choose **Next: Review**. 6. For **Policy Name**,
   type `ServiceCatalogAdmin-AdditionalPermissions`.

   ###### Important

   You must grant administrators Amazon S3 permissions
   to access templates
   that AWS Service Catalog stores
   in Amazon S3.
   For more information,
   see [User Policy Examples](../../../AmazonS3/latest/userguide/example-policies-s3.md "../../../AmazonS3/latest/userguide/example-policies-s3.md")
   in the _Amazon Simple Storage Service User Guide_. 7. Choose **Create Policy**.

5. Return to the browser window with the permissions page and choose **Refresh**.
6. In the search field, type `ServiceCatalog` to filter the policy list.
7. Select the checkboxes for the **`AWSServiceCatalogAdminFullAccess`** and
   **`ServiceCatalogAdmin-AdditionalPermissions`** policies,
   and then choose **Next: Review**.
8. If you are updating a user, choose **Add permissions**.

If you are creating a user, choose **Create user**. You can download or copy
the credentials and then choose **Close**. 9. To sign in as the catalog administrator, use your account-specific URL. To find this URL, choose
**Dashboard** in the navigation pane and choose **Copy Link**.
Paste the link in your browser, and use the name and password of the IAM user you created or updated in this procedure.

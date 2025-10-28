# Step 5: Create launch roles

In this step, you will create an IAM role (launch role) specifying the permissions
that the Terraform provisioning engine and AWS Service Catalog can assume when an end user
launches a HashiCorp Terraform product.

The IAM role (launch role) that you later assign to your simple Amazon S3 bucket
Terraform product as a launch constraint must have
the following permissions:

- Access to the underlying AWS resources for your Terraform product.
  In this tutorial, this includes access to the `s3:CreateBucket*`,
  `s3:DeleteBucket*`, `s3:Get*`, `s3:List*`,
  and `s3:PutBucketTagging` Amazon S3 operations.
- Read access to the Amazon S3 template in a AWS Service Catalog-owned Amazon S3 bucket
- Access to the `CreateGroup`, `ListGroupResources`, `DeleteGroup`,
  and `Tag` resource group operations. These operations enable AWS Service Catalog to manage
  resource groups and tags

######

To create a launch role in the AWS Service Catalog administrator account

1. While logged in to the AWS Service Catalog administrator account, follow the instructions to [Create new policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _IAM User guide_.
2. Create a **policy** for your simple Amazon S3 bucket Terraform product.
   This policy must be created before you create the launch role, and
   consists of the following permissions:
   - `s3`— Allows AWS Service Catalog full permissions to list, read, write, provision,
     and tag the Amazon S3 product.
   - `s3`— Allows access to Amazon S3 buckets owned by AWS Service Catalog. To deploy the product,
     AWS Service Catalog requires access to provisioning artifacts.
   - `resourcegroups`—
     Allows AWS Service Catalog to create, list, delete, and tag AWS Resource Groups.
   - `tag`—
     Allows AWS Service Catalog tagging permissions.

###### Note

Depending on the underlying resources that you want to deploy,
you may need to modify the example JSON policy.

Paste the following JSON policy document:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "s3:ExistingObjectTag/servicecatalog:provisioning": "true"
 }
 }
 },
 {
 "Action": [
 "s3:CreateBucket*",
 "s3:DeleteBucket*",
 "s3:Get*",
 "s3:List*",
 "s3:PutBucketTagging"
 ],
 "Resource": "arn:aws:s3:::*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "resource-groups:CreateGroup",
 "resource-groups:ListGroupResources",
 "resource-groups:DeleteGroup",
 "resource-groups:Tag"
 ],
 "Resource": "*",
 "Effect": "Allow"
 },
 {
 "Action": [
 "tag:GetResources",
 "tag:GetTagKeys",
 "tag:GetTagValues",
 "tag:TagResources",
 "tag:UntagResources"
 ],
 "Resource": "*",
 "Effect": "Allow"
 }
 ]
}`

```

3. 1. Choose **Next**, **Tags**.
   2. Choose **Next,**
      **Review**.
   3. In the **Review policy** page, for the **Name**,
      enter `S3ResourceCreationAndArtifactAccessPolicy`.
   4. Choose **Create policy**.
4. In the navigation pane, choose **Roles**, and then choose
   **Create role**.
5. For **Select trusted entity**, choose **Custom trust policy** and then enter the following JSON policy:
6. Choose **Next**.
7. In the **Policies** list, select the
   `S3ResourceCreationAndArtifactAccessPolicy` you just created.
8. Choose **Next**.
9. For **Role name**, enter `SCLaunch-S3product`.

###### Important

Launch role names **must** begin with "SCLaunch" followed by the desired
role name. 10. Choose **Create role**.

###### Important

After creating the launch role in your AWS Service Catalog administrator account, you must also create an identical launch role in the AWS Service Catalog end
user account. The role in the end user account must have the same name and include the same policy as the
role in the administrator account.

######

To create a launch role in the AWS Service Catalog end user account

1. Log in as the administrator to the end user account, and then follow the instructions to [Create new policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the _IAM User guide_.
2. Repeat steps 2-10 from _To create a launch role in the AWS Service Catalog administrator account_ above.

###### Note

When creating a launch role in the AWS Service Catalog end user account, ensure
you use the same administrator `AccountId` in the custom trust policy.

Now that you have created a launch role in both the administrator and end user accounts, you can
add a launch constraint to the product.

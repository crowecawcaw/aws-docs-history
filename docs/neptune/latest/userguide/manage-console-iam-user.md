# Creating an IAM user with permissions for Neptune

To access the Neptune console to create and manage a Neptune DB cluster, you
need to create an IAM user with all the necessary permissions.

The first step is to create a service-linked role policy for Neptune:

## Create a service-linked role policy for Amazon Neptune

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.
3. On the **Policies** page, select **Create Policy**.
4. On the **Create policy** page, select the **JSON** tab
   and copy in the following service-linked role policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "iam:CreateServiceLinkedRole",
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/aws-service-role/rds.amazonaws.com/AWSServiceRoleForRDS",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName":"rds.amazonaws.com"
 }
 }
 }
 ]
}`

```

5. Select **Next: Tags**, and on the **Add tags**
   page select **Next: Review**.
6. On the **Review policy** page, name the new policy
   "NeptuneServiceLinked".

For more information about service-linked roles, see [Using service-linked roles for Amazon Neptune](security-iam-service-linked-roles.md "security-iam-service-linked-roles.md").

## Create a new IAM user with all necessary permissions

Next, create the new IAM user with the appropriate managed policies attached
that will grant the permissions you'll need, along with the service-linked role policy
that you have created (here named `NeptuneServiceLinked`):

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane on the left, choose **Users**, and on the
    **Users** page, choose **Add users**.
3.  On the **Add user** page, enter a name for the new IAM user,
    choose **Access key - Programatic access** for the AWS credential type,
    and choose **Next: Permissions**.
4.  On the **Set permissions** page, in the **Filter
    policies** box, type "Neptune". Now select the following from the policies
    that are listed:
    - **NeptuneFullAccess**
    - **NeptuneConsoleFullAccess**
    - **NeptuneServiceLinked** (assuming that is what
      you named the service-linked role policy that you created earlier).

5.  Next type "VPC" in the **Filter policies** box in
    place of "Neptune". Select **AmazonVPCFullAccess** from the
    policies that are listed.
6.  Select **Next: Tags**, and in the **Add tags**
    page, select **Next: Review**.
7.  In the **Review** page, check that all of the following
    policies are now attached to your new user:

        * **NeptuneFullAccess**
        * **NeptuneConsoleFullAccess**
        * **NeptuneServiceLinked**
        * **AmazonVPCFullAccess**

    Then, select **Create User**.

8.  Finally, download and save the new user's access key ID and secret access key.

To interoperate on other services such as Amazon Simple Storage Service (Amazon S3), you will need to add
more permissions and trust relationships.

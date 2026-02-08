# Configure permissions for Amazon Keyspaces automatic scaling

To get started, confirm that the principal has the appropriate permissions to create and manage automatic scaling settings. In AWS Identity and Access Management (IAM),
the AWS managed policy `AmazonKeyspacesFullAccess` is required to manage Amazon Keyspaces scaling policies.

###### Important

`application-autoscaling:*` permissions are required to disable automatic
scaling on a table. You must turn off auto scaling for a table before you can delete it.

To set up an IAM user or role for Amazon Keyspaces console access and Amazon Keyspaces automatic scaling, add the
following policy.

###### To attach the `AmazonKeyspacesFullAccess` policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the IAM console dashboard, choose **Users**, and then
   choose your IAM user or role from the list.
3. On the **Summary** page, choose **Add
   permissions**.
4. Choose **Attach existing policies directly**.
5. From the list of policies, choose **AmazonKeyspacesFullAccess**,
   and then choose **Next: Review**.
6. Choose **Add permissions**.

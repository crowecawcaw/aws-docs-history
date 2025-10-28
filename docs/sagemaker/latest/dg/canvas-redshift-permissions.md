# Grant Users Permissions to Import Amazon Redshift

Data

Your users might have datasets stored in Amazon Redshift. Before users can import data from Amazon Redshift into
SageMaker Canvas, you must add the `AmazonRedshiftFullAccess` managed policy to the IAM
execution role that you've used for the user profile and add Amazon Redshift as a service principal to
the role's trust policy. You must also associate the IAM execution role with your Amazon Redshift
cluster. Complete the procedures in the following sections to give your users the required
permissions to import Amazon Redshift data.

## Add Amazon Redshift permissions to your IAM

role

You must grant Amazon Redshift permissions to the IAM role specified in your user profile.

To add the `AmazonRedshiftFullAccess` policy to the user's IAM role, do the
following.

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**.
3. In the search box, search for the user's IAM role by name and select it.
4. On the page for the user's role, under **Permissions**, choose
   **Add permissions**.
5. Choose **Attach policies**.
6. Search for the `AmazonRedshiftFullAccess` managed policy and select
   it.
7. Choose **Attach policies** to attach the policy to the role.

After attaching the policy, the role’s **Permissions** section should
now include `AmazonRedshiftFullAccess`.

To add Amazon Redshift as a service principal to the IAM role, do the following.

1. On the same page for the IAM role, under **Trust relationships**,
   choose **Edit trust policy**.
2. In the **Edit trust policy** editor, update the trust policy to add
   Amazon Redshift as a service principal. An IAM role that allows Amazon Redshift to access other AWS
   services on your behalf has a trust relationship as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

3. After editing the trust policy, choose **Update policy**.

You should now have an IAM role that has the policy
`AmazonRedshiftFullAccess` attached to it and a trust relationship established
with Amazon Redshift, giving users permission to import Amazon Redshift data into SageMaker Canvas. For more information
about AWS managed policies, see [Managed policies and
inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") in the _IAM User Guide_.

## Associate the IAM role with your

Amazon Redshift cluster

In the settings for your Amazon Redshift cluster, you must associate the IAM role that you
granted permissions to in the preceding section.

To associate an IAM role with your cluster, do the following.

1. Sign in to the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, and then choose the
   name of the cluster that you want to update.
3. In the **Actions** dropdown menu, choose **Manage IAM
   roles**. The **Cluster permissions** page appears.
4. For **Available IAM roles**, enter either the ARN or the name of
   the IAM role, or choose the IAM role from the list.
5. Choose **Associate IAM role** to add it to the list of
   **Associated IAM roles**.
6. Choose **Save changes** to associate the IAM role with the
   cluster.

Amazon Redshift modifies the cluster to complete the change, and the IAM role to which you
previously granted Amazon Redshift permissions is now associated with your Amazon Redshift cluster. Your users now
have the required permissions to import Amazon Redshift data into SageMaker Canvas.

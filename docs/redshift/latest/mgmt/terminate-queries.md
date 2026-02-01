Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Ending a running query

You can also use the **Queries** page to end a query that is
currently in progress.

###### Note

The ability to terminate queries and loads in the Amazon Redshift console requires specific
permission. If you want users to be able to terminate queries and loads, make sure
to add the `redshift:CancelQuerySession` action to your AWS Identity and Access Management (IAM)
policy. This requirement applies whether you select the **Amazon Redshift Read
Only** AWS managed policy or create a custom policy in IAM. Users who
have the **Amazon Redshift Full Access** policy already have the necessary
permission to terminate queries and loads. For more information about actions in IAM
policies for Amazon Redshift, see [Managing access to
resources](redshift-iam-access-control-overview.md#redshift-iam-accesscontrol-managingaccess "redshift-iam-access-control-overview.md#redshift-iam-accesscontrol-managingaccess").

###### To end a running query

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Queries and loads** to
   display the list of queries for your account.
3. Choose the running query that you want to end in the list, and then choose
   **Terminate query**.

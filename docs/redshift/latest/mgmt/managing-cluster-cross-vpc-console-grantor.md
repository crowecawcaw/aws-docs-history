Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Granting access to a

VPC

If the VPC that you want to access your cluster or workgroup is in another AWS
account, make sure to authorize it from the owner's (grantor's) account.

###### To allow a VPC in another AWS account to have access to your cluster or

workgroup

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**. For
   Amazon Redshift Serverless, choose **Serverless dashboard**.
3. For a cluster that you want to allow access to, view the details by choosing
   the cluster name. Choose the **Properties** tab of the cluster.

The **Granted accounts** section displays the accounts and
corresponding VPCs that have access to your cluster. For an Amazon Redshift Serverless
workgroup, choose the workgroup. **Granted accounts** are
available under the **Data access** tab. 4. Choose **Grant access** to display a form to enter
**Grantee information** to add an account. 5. For **AWS account ID**, enter the ID of the account you are
granting access. You can grant access to specific VPCs or all VPCs in the
specified account. 6. Choose **Grant access** to grant access.

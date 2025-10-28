Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Renaming a cluster that has

a custom domain assigned

###### Note

This series of steps doesn't apply to an Amazon Redshift Serverless workgroup. You can't
change the workgroup name.

In order to rename a cluster that has a custom domain name, the
`acm:DescribeCertificate` IAM permission is required.

1. Go to the Amazon Redshift console and choose the cluster whose name you want to change.
   Choose **Edit** to edit the cluster properties.
2. Edit the **Cluster identifier**. You can also change other
   properties for the cluster. Then choose **Save
   changes**.
3. After the cluster is renamed, you have to update the DNS record to change the
   CNAME entry for the custom domain to point to the updated Amazon Redshift endpoint.

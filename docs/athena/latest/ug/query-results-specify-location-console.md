# Specify a query result

location using the Athena console

Before you can run a query, a query result bucket location in Amazon S3 must be
specified, or you must use a workgroup that has specified a bucket and whose
configuration overrides client settings.

###### To specify a client-side setting query result location using the Athena

console

1. [Switch](switching-workgroups.md "switching-workgroups.md") to the workgroup for which you want to specify a query
   results location. The name of the default workgroup is
   **primary**.
2. From the navigation bar, choose **Settings**.
3. From the navigation bar, choose **Manage**.
4. For **Manage settings**, do one of the following:
   - In the **Location of query result** box, enter
     the path to the bucket that you created in Amazon S3 for your query
     results. Prefix the path with `s3://`.
   - Choose **Browse S3**, choose the Amazon S3 bucket that
     you created for your current Region, and then choose
     **Choose**.

###### Note

If you are using a workgroup that specifies a query result location
for all users of the workgroup, the option to change the query result
location is unavailable. 5. (Optional) Choose **View lifecycle configuration** to
view and configure the [Amazon S3
lifecycle rules](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") on your query results bucket. The Amazon S3 lifecycle
rules that you create can be either expiration rules or transition rules.
Expiration rules automatically delete query results after a certain amount
of time. Transition rules move them to another Amazon S3 storage tier. For more
information, see [Setting lifecycle configuration on a bucket](../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md "../../../AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.md") in the
Amazon Simple Storage Service User Guide. 6. (Optional) For **Expected bucket owner**, enter the ID of
the AWS account that you expect to be the owner of the output location
bucket. This is an added security measure. If the account ID of the bucket
owner does not match the ID that you specify here, attempts to output to the
bucket will fail. For in-depth information, see [Verifying bucket ownership with bucket owner
condition](../../../AmazonS3/latest/userguide/bucket-owner-condition.md "../../../AmazonS3/latest/userguide/bucket-owner-condition.md") in the _Amazon S3 User Guide_.

###### Note

The expected bucket owner setting applies only to the Amazon S3
output location that you specify for Athena query results. It does not
apply to other Amazon S3 locations like data source locations
in external Amazon S3 buckets, `CTAS` and
`INSERT INTO` destination table
locations, `UNLOAD` statement output
locations, operations to spill buckets for federated
queries, or `SELECT` queries run against a
table in another account. 7. (Optional) Choose **Encrypt query results** if you want
to encrypt the query results stored in Amazon S3. For more information about
encryption in Athena, see [Encryption at rest](encryption.md "encryption.md"). 8. (Optional) Choose **Assign bucket owner full control over query
results** to grant full control access over query results to
the bucket owner when [ACLs are
enabled](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") for the query result bucket. For example, if your query
result location is owned by another account, you can grant ownership and
full control over your query results to the other account. For more
information, see [Controlling
ownership of objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the
_Amazon S3 User Guide_. 9. Choose **Save**.

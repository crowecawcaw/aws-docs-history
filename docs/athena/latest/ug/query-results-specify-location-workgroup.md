# Specify a query result

location using a workgroup

You specify the query result location in a workgroup configuration using the
AWS Management Console, the AWS CLI, or the Athena API.

When using the AWS CLI, specify the query result location using the
`OutputLocation` parameter of the `--configuration` option
when you run the [`aws athena
 create-work-group`](../../../cli/latest/reference/athena/create-work-group.md "../../../cli/latest/reference/athena/create-work-group.md") or [`aws athena
 update-work-group`](../../../cli/latest/reference/athena/update-work-group.md "../../../cli/latest/reference/athena/update-work-group.md") command.

###### To specify the query result location for a workgroup using the Athena

console

1. If the console navigation pane is not visible, choose the expansion menu
   on the left.

![Choose the expansion menu.](images/nav-pane-expansion.png) 2. In the navigation pane, choose **Workgroups**. 3. In the list of workgroups, choose the link of the workgroup that you want
to edit. 4. Choose **Edit**. 5. For **Query result location and encryption**, do one of
the following:

    * In the **Location of query result** box, enter
     the path to a bucket in Amazon S3 for your query results. Prefix the path
     with `s3://`.
    * Choose **Browse S3**, choose the Amazon S3 bucket for
     your current Region that you want to use, and then choose
     **Choose**.

6. (Optional) For **Expected bucket owner**, enter the ID of
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
full control over your query results to the other account.

If the bucket's S3 Object Ownership setting is **Bucket owner preferred**, the bucket owner also owns all query
result objects written from this workgroup. For example, if an external
account's workgroup enables this option and sets its query result location
to your account's Amazon S3 bucket which has an S3 Object Ownership setting of
**Bucket owner preferred**, you own and
have full control access over the external workgroup's query results.

Selecting this option when the query result bucket's S3 Object Ownership
setting is **Bucket owner enforced** has no
effect. For more information, see [Controlling
ownership of objects and disabling ACLs for your bucket](../../../AmazonS3/latest/userguide/about-object-ownership.md "../../../AmazonS3/latest/userguide/about-object-ownership.md") in the
_Amazon S3 User Guide_. 9. If you want to require all users of the workgroup to use the query results
location that you specified, scroll down to the
**Settings** section and select **Override
client-side settings**. 10. Choose **Save changes**.

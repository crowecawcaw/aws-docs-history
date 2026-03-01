# Configure cross-account AWS Glue access in Athena for Spark

This topic shows how consumer account `666666666666` and owner
account `999999999999` can be configured for cross-account AWS Glue
access. When the accounts are configured, the consumer account can run queries from Athena
for Spark on the owner's AWS Glue databases and tables.

## Step 1: In AWS Glue, provide access to consumer roles

In AWS Glue, the owner creates a policy that provides the consumer's roles access to the
owner's AWS Glue data catalog.

###### To add a AWS Glue policy that allows a consumer role access to the owner's data catalog

1. Using the catalog owner's account, sign in to the AWS Management Console.
2. Open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
3. In the navigation pane, expand **Data Catalog**, and then choose
   **Catalog settings**.
4. On the **Data catalog settings** page, in the
   **Permissions** section, add a policy like the following.
   This policy provides roles for the consumer account
   `666666666666` access to the data catalog in the
   owner account `999999999999`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Cataloguers",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`666666666666`:role/Admin",
 "arn:aws:iam::`666666666666`:role/AWSAthenaSparkExecutionRole"
 ]
 },
 "Action": "glue:*",
 "Resource": [
 "arn:aws:glue:us-west-2:`999999999999`:catalog",
 "arn:aws:glue:us-west-2:`999999999999`:database/*",
 "arn:aws:glue:us-west-2:`999999999999`:table/*"
 ]
 }
 ]
}`

```

## Step 2: Configure the consumer account for access

In the consumer account, create a policy to allow access to the owner's AWS Glue Data Catalog,
databases, and tables, and attach the policy to a role. The following example uses
consumer account `666666666666`.

###### To create a AWS Glue policy for access to the owner's AWS Glue Data Catalog

1. Using the consumer account, sign into the AWS Management Console.
2. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
3. In the navigation pane, expand **Access management**, and
   then choose **Policies**.
4. Choose **Create policy**.
5. On the **Specify permissions** page, choose
   **JSON**.
6. In the **Policy editor**, enter a JSON statement like the
   following that allows AWS Glue actions on the owner account's data catalog.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "glue:*",
 "Resource": [
 "arn:aws:glue:us-east-1:`999999999999`:catalog",
 "arn:aws:glue:us-east-1:`999999999999`:database/*",
 "arn:aws:glue:us-east-1:`999999999999`:table/*"
 ]
 }
 ]
}`

```

7. Choose **Next**.
8. On the **Review and create** page, for **Policy
   name**, enter a name for the policy.
9. Choose **Create policy**.

Next, you use IAM console in the consumer account to attach the policy that you just
created to the IAM role or roles that the consumer account will use to access the
owner's data catalog.

###### To attach the AWS Glue policy to the roles in the consumer account

1. In the consumer account IAM console navigation pane, choose
   **Roles**.
2. On the **Roles** page, find the role that you want to attach
   the policy to.
3. Choose **Add permissions**, and then choose **Attach
   policies**.
4. Find the policy that you just created.
5. Select the check box for the policy, and then choose **Add
   permissions**.
6. Repeat the steps to add the policy to other roles that you want to use.

## Step 3: Configure a session and create a query

In Athena Spark, in the requester account, using the role specified, create a session
to test access by [creating
a notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook "notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook") or [editing a
current session](notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details "notebooks-spark-getting-started.md#notebooks-spark-getting-started-editing-session-details"). When you [configure the session
properties](notebooks-spark-custom-jar-cfg.md#notebooks-spark-custom-jar-cfg-console "notebooks-spark-custom-jar-cfg.md#notebooks-spark-custom-jar-cfg-console"), specify one of the following:

- The AWS Glue catalog separator – With this
  approach, you include the owner account ID in your queries. Use this method if
  you are going to use the session to query data catalogs from different
  owners.
- The AWS Glue catalog ID – With this
  approach, you query the database directly. This method is more convenient if you
  are going to use the session to query only a single owner's data catalog.

When you edit the session properties, add the following:

```
{
    "spark.hadoop.aws.glue.catalog.separator": "/"
}
```

When you run a query in a cell, use syntax like that in the following example.
Note that in the `FROM` clause, the catalog ID and separator are
required before the database name.

```
df = spark.sql('SELECT requestip, uri, method, status FROM ``999999999999`/mydatabase`.cloudfront_logs LIMIT 5')
df.show()
```

When you edit the session properties, enter the following property. Replace
`999999999999` with the owner account ID.

```
{
    "spark.hadoop.hive.metastore.glue.catalogid": "`999999999999`"
}
```

When you run a query in a cell, use syntax like the following. Note that in
the `FROM` clause, the catalog ID and separator are not required
before the database name.

```
df = spark.sql('SELECT * FROM mydatabase.cloudfront_logs LIMIT 10')
df.show()
```

## Additional resources

[Configure cross-account access to AWS Glue data catalogs](security-iam-cross-account-glue-catalog-access.md "security-iam-cross-account-glue-catalog-access.md")

[Managing cross-account permissions using both AWS Glue and Lake Formation](../../../lake-formation/latest/dg/hybrid-cross-account.md "../../../lake-formation/latest/dg/hybrid-cross-account.md") in the
_AWS Lake Formation Developer Guide_.

[Configure cross-account access to a shared AWS Glue Data Catalog using Amazon Athena](../../../prescriptive-guidance/latest/patterns/configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena.md "../../../prescriptive-guidance/latest/patterns/configure-cross-account-access-to-a-shared-aws-glue-data-catalog-using-amazon-athena.md") in
_AWS Prescriptive Guidance Patterns_.

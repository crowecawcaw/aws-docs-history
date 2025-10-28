# Loading report data to other resources

You can upload Cost and Usage Reports to Amazon Redshift and Amazon Quick Suite to analyze your AWS cost and
usage.

###### Topics

- [Loading report data to Amazon Quick Suite](#cur-query-other-qs "#cur-query-other-qs")
- [Loading report data to Amazon Redshift](#cur-query-other-rs "#cur-query-other-rs")

## Loading report data to Amazon Quick Suite

You can upload your Cost and Usage Reports into Amazon Quick Suite.

For more information about uploading to Quick Suite, see [Creating a Data Set Using Amazon S3
Files](../../../quicksight/latest/user/create-a-data-set-s3.md "../../../quicksight/latest/user/create-a-data-set-s3.md") in the _Quick Suite User Guide_.

## Loading report data to Amazon Redshift

This section shows how you can upload AWS CUR to Amazon Redshift to analyze your AWS costs and
usage.

###### Important

Amazon Redshift columns aren't case sensitive and has stricter character limitations than
user-defined tags. To prevent conflicts between Amazon Redshift and user-defined tags, AWS replaces
your tags with the tags `userTag0`, `userTag1`,
`userTag2`, etc. After you create an Amazon Redshift table and upload your report into
it, you can create an Amazon Redshift table that maps the AWS-defined tags to your user-defined tags.
The tag table allows you to look up your original tags.

For example, if you have the tags `OWNER` and `Owner`, Amazon Redshift
doesn't allow you to create a table with two columns named "owner". Instead, you create a
report table with the columns `userTag0` and `userTag1` instead of
`OWNER` and `Owner`, and then create a table with the columns
`remappedUserTag` and `userTag`. The `remappedUserTag`
column stores the AWS-defined tags `userTag0` and `userTag1`, and
the `userTag` column stores your original tags, `OWNER` and
`Owner`

AWS provides the commands to create your Amazon Redshift table, upload your report, create your
tag table, and insert all of the tag rows into your tag table. The commands are provided to
you in the `RedshiftCommands.sql` file that is stored alongside your manifest
file in S3, and in the **Redshift file**
**Helper file** in the Billing and Cost Management console. AWS also provides a RedshiftManifest
file, which controls which report the commands in the RedshiftCommand file uploads. Deleting
or removing the RedshiftManifest file breaks the copy command in the RedshiftCommands
file.

###### To find the `RedshiftCommands.sql` file in the Billing and Cost Management console

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy Pages**,
   choose **Cost and Usage Reports**.
3. Choose the report that you want to upload to Amazon Redshift.
4. Next to **You have enabled viewing reports in the following
   service(s):**, choose **Amazon Redshift**.
5. Copy the commands from the dialog box and paste them into your SQL client.

The following procedure assumes familiarity with databases and Amazon Redshift.

###### To upload an Cost and Usage Reports to Amazon Redshift

1. Create an Amazon Redshift cluster.

For more information, see [Creating a
Cluster](../../../redshift/latest/mgmt/managing-clusters-console.md#create-cluster "../../../redshift/latest/mgmt/managing-clusters-console.md#create-cluster") in the _Amazon Redshift Management Guide_. 2. Sign in to the AWS Management Console and open the Amazon S3 console at
[https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"). 3. Navigate to the Amazon S3 location where you store your AWS CUR. 4. Open the `RedshiftCommands.sql` file.

The file contains customized commands to create an Amazon Redshift table, upload the AWS CUR from
Amazon S3, and create a tag table that allows user-defined tags to be imported into
Amazon Redshift. 5. In the `copy` command, replace
`<AWS_ROLE>` with the ARN of an IAM role that has
permissions to access the Amazon S3 bucket where you store your AWS CUR. 6. Replace `<S3_BUCKET_REGION>` with the Region your
Amazon S3 bucket is in. For example, `us-east-1`. 7. Use a SQL client to connect to the cluster.

For more information, see [Accessing
Amazon Redshift Clusters and Databases](../../../redshift/latest/mgmt/using-rs-tools.md "../../../redshift/latest/mgmt/using-rs-tools.md") in the
_Amazon Redshift Management Guide_. 8. Copy the SQL commands from the `RedshiftCommands.sql` file to your SQL
client in the following order:

    * create table - This command creates an Amazon Redshift table with a schema customized to
     match your report.
    * copy - This command uses the provided IAM role to upload the AWS CUR files from S3
     to Amazon Redshift.
    * create tag table - This command creates a table that allows you to map
     AWS-defined tags to your user-defined tags.
    * insert - These commands insert the user-defined tags into the tag table.

9. After you have copied all of the data from your AWS CUR into Amazon Redshift, you can query the
   data using SQL. For more information about querying data in Amazon Redshift, see [Amazon Redshift SQL](../../../redshift/latest/dg/c_redshift-sql.md "../../../redshift/latest/dg/c_redshift-sql.md") in the
   _Amazon Redshift Database Developer Guide_.

###### Note

The number of columns in Cost and Usage Reports can change from month to month, such as when a
new cost allocation tag is created or a service adds a new product attribute. We recommend
that you copy the data from your AWS CUR into a new table every month, and then copy the
columns that interest you into a separate month-by-month table.

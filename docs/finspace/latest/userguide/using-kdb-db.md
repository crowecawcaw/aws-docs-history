After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managing kdb databases

The following sections provide a detailed overview of the operations that you can
perform by using a Managed kdb database.

## Creating a kdb database

###### To create a kdb database

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Databases**
   tab.
5. Choose **Create database**.
6. On the **Create database** page, enter a unique name for
   the database.
7. (Optional) Enter a description for your database.
8. (Optional) Add a new tag to assign it to your kdb database. For more
   information, see [AWS tags](create-an-amazon-finspace-environment.md#aws-tags "create-an-amazon-finspace-environment.md#aws-tags").

###### Note

You can only add up to 50 tags to your database. 9. Choose **Create database**. The environment details page
opens and the table under **Databases** lists the newly
created database.

You can choose the database name from the list to view its details in
database details page.

## Managing data in a kdb database

The Managed kdb Insights database allows you to add, update, or delete a set of
files. When you create a database, there is no data loaded in it. You must add data
to the database through changesets. A changeset represents a versioned set of changes
that are applied to a database.

### Creating an Amazon S3 bucket policy

Before you can ingest data into your database, you must have a valid Amazon S3
bucket IAM policy in place to allow FinSpace to access the data you will ingest into
it. The following is an example of such a policy.

In the following example, replace each `*user input
 placeholder*` with your own values. Replace
`*555555555555*` with the AWS account where you created your
Managed kdb Insights environment.

###### Example — Sample Amazon S3 bucket policy

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "FinSpaceServiceAccess",
 "Statement": [{
 "Effect": "Allow",
 "Principal": {
 "Service": "finspace.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:GetObjectTagging"
 ],
 "Resource": "arn:aws:s3:::managed-kdb-data/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "555555555555"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "finspace.amazonaws.com"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::managed-kdb-data",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "555555555555"
 }
 }
 }
 ]
}`

```

### Creating a new changeset

You can add, update, and delete data in a database by creating a new changeset.
You can either use
the console or the [CreateKxChangeset](../management-api/API_CreateKxChangeset.md "../management-api/API_CreateKxChangeset.md") API to create a changeset. To add a data to your database, create a changeset by providing the changeset type
as `PUT`, database path, and S3 URI path.

To update data in a database, you need to create another changeset with the
same database path you chose while adding the data. To delete data in a database,
create a new changeset with changeset type as `DELETE`.

###### Note

You should only add data in the correct kdb file format that follows a valid
kdb path structure. Other file formats and structures are not supported when
accessed from a FinSpace Managed kdb cluster. You can learn more about valid kdb
path structures [here](https://code.kx.com/q/database/ "https://code.kx.com/q/database/").

###### To create a changeset from the console

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the
   environment.
4. On the environment details page, choose **Databases**
   tab. The table under this tab displays a list of databases.
5. Choose a database name to view its details.
6. On the database details page, choose the **Changesets**
   tab.
7. Choose **Create changeset**.
8. On the **Create changeset** page, select one of the
   following types of changeset.
   - _PUT_ – Adds or updates
     files in a database.
   - _DELETE_ – Deletes files in
     a database. This option is not available when creating the changeset
     for the first time.

9. For **Database path**, specify a path within the
   database directory where you want to add data. If the data already exists at
   this path, it will be updated.
10. For **S3 URI** provide the source path of the file to
    add data.
11. Choose **Create changeset**. The database details page
    opens where you can see the status of the changeset in the changeset
    table.

You can choose the changeset ID to view details of a changeset.

## Updating a kdb database

###### To update the metadata of a kdb database

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose **Databases**
   tab.
5. From the list of databases, choose the one that you want to update. The
   database details page opens.
6. On the database details page, choose **Edit**.
7. Edit the database description.
8. Choose **Update database**.

## Viewing kdb database details

###### To view and get details of a kdb database

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose **Databases** tab.
   The table under this tab displays a list of databases.
5. Choose a database name to view its details. The database details page opens
   where you can view details about the database. You can also add and view
   changesets and tags associated with this database.

## Deleting a kdb database

###### Note

This action is irreversible. Deleting a kdb database will delete all of its
contents.

###### To delete a kdb database

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. Choose **Kdb environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose the **Databases**
   tab.
5. From the list of databases, choose the one that you want to delete. The
   database details page opens.
6. On the database details page, choose **Delete**.
7. On the confirmation dialog box, enter _confirm_.
8. Choose **Delete**.

# Using the Aurora query editor

The Aurora query editor lets you run SQL statements on your Aurora DB cluster
through the AWS Management Console. You can run SQL queries, data manipulation (DML) statements,
and data definition (DDL) statements. Using the console interface lets you perform
database maintenance, produce reports, and conduct SQL experiments. You can avoid
setting up the network configuration to connect to your DB cluster from a
separate client system such as an EC2 instance or a laptop computer.

The query editor requires an Aurora DB cluster with RDS Data API (Data API) enabled.
For information about DB clusters that support Data API and how to enable it, see
[Using the Amazon RDS Data API](data-api.md "data-api.md").
The SQL that you can run is subject to the Data API limitations. For more information, see [Limitations for the Amazon RDS Data API](data-api.md "data-api.md").

## Availability of the query editor

The query editor is available for Aurora DB clusters using Aurora MySQL and
Aurora PostgreSQL engine versions that support Data API, and in the AWS Regions where
Data API is available. For more information, see [Supported Regions and Aurora DB engines for RDS Data API](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

## Authorizing access to the query editor

A user must be authorized to run queries in the query editor. You can authorize a
user to run queries in the query editor by adding the
`AmazonRDSDataFullAccess` policy, a predefined AWS Identity and Access Management (IAM)
policy, to that user.

###### Note

Make sure to use the same user name and password when you create the IAM user as you did for the database user, such as
the administrative user name and password. For more information, see [Creating an IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the
_AWS Identity and Access Management User Guide_.

You can also create an IAM policy that grants access to the query editor. After you create the policy,
add it to each user that requires access to the query editor.

The following policy provides the minimum required permissions for a user to access the
query editor.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QueryEditor0",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:PutResourcePolicy",
 "secretsmanager:PutSecretValue",
 "secretsmanager:DeleteSecret",
 "secretsmanager:DescribeSecret",
 "secretsmanager:TagResource"
 ],
 "Resource": "arn:aws:secretsmanager:*:*:secret:rds-db-credentials/*"
 },
 {
 "Sid": "QueryEditor1",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetRandomPassword",
 "tag:GetResources",
 "secretsmanager:CreateSecret",
 "secretsmanager:ListSecrets",
 "dbqms:CreateFavoriteQuery",
 "dbqms:DescribeFavoriteQueries",
 "dbqms:UpdateFavoriteQuery",
 "dbqms:DeleteFavoriteQueries",
 "dbqms:GetQueryString",
 "dbqms:CreateQueryHistory",
 "dbqms:UpdateQueryHistory",
 "dbqms:DeleteQueryHistory",
 "dbqms:DescribeQueryHistory",
 "rds-data:BatchExecuteStatement",
 "rds-data:BeginTransaction",
 "rds-data:CommitTransaction",
 "rds-data:ExecuteStatement",
 "rds-data:RollbackTransaction"
 ],
 "Resource": "*"
 }
 ]
}`

```

For information about creating an IAM policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md")
in the _AWS Identity and Access Management User Guide_.

For information about adding an IAM policy to a user, see [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md")
in the _AWS Identity and Access Management User Guide_.

## Running queries in the query editor

You can run SQL statements on an Aurora DB cluster in the query editor. The SQL
that you can run is subject to the Data API limitations. For more information, see
[Limitations for the Amazon RDS Data API](data-api.md "data-api.md").

###### To run a query in the query editor

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the upper-right corner of the AWS Management Console, choose the AWS Region in which you
   created the Aurora DB clusters that you want to query.
3. In the navigation pane, choose **Databases**.
4. Choose the Aurora DB cluster that you want to run SQL queries on.
5. For **Actions**, choose **Query**. If you
   haven't connected to the database before, the **Connect to
   database** page opens.

![Query editor Connect to database page](images/query-editor-connect.png) 6. Enter the following information:

    1. For **Database instance or cluster**, choose the Aurora DB cluster
     that you want to run SQL queries on.
    2. For **Database username**, choose the user name of
     the database user to connect with, or choose **Add new
     database credentials**. If you choose **Add new
     database credentials**, enter the user name for the new
     database credentials in **Enter database
     username**.
    3. For **Enter database password**, enter the password for the database
     user that you chose.
    4. In the last box, enter the name of the database or schema that you want to use for
     the Aurora DB cluster.
    5. Choose **Connect to database**.


    ###### Note

    If your connection is successful, your connection and
     authentication information are stored in AWS Secrets Manager. You don't
     need to enter the connection information again.

7. In the query editor, enter the SQL query that you want to run on the
   database.

![Query editor with a SQL statement in the text area](images/query-editor.png)

Each SQL statement can commit automatically, or you can run SQL statements in a script as part of a transaction.
To control this behavior, choose the gear icon above the query window.

![Gear icon in Query editor](images/query-editor-gear.png)

The **Query Editor Settings** window appears.

![Query Editor Settings](images/query-editor-settings.png)

If you choose **Auto-commit**, every SQL statement commits automatically. If you choose **Transaction**,
you can run a group of statements in a script. Statements are automatically committed at the end of the script unless explicitly committed
or rolled back before then. Also, you can choose to stop a running script if an error occurs by enabling **Stop on error**.

###### Note

In a group of statements, data definition language (DDL) statements can cause previous data manipulation language (DML) statements to commit.
You can also include `COMMIT` and `ROLLBACK` statements in a group of statements in a script.

After you make your choices in the **Query Editor Settings** window, choose **Save**. 8. Choose **Run** or press Ctrl+Enter, and the query editor
displays the results of your query.

After running the query, save it to **Saved queries** by
choosing **Save**.

Export the query results to spreadsheet format by choosing
**Export to csv**.

You can find, edit, and rerun previous queries. To do so, choose the **Recent**
tab or the **Saved queries** tab, choose the query text, and then choose **Run**.

To change the database, choose **Change database**.

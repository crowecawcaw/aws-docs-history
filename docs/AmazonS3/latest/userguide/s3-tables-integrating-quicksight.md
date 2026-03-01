# Visualizing table data with Quick

Quick is a fast business analytics service to build visualizations, perform ad hoc
analysis, and quickly get business insights from your data. Quick seamlessly discovers
AWS data sources, enables organizations to scale to hundreds of thousands of users, and
delivers fast and responsive query performance by using the Quick Super-fast, Parallel,
In-Memory, Calculation Engine (SPICE). For more information, see [What is Quick?](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") in the _Quick
user guide_.

After you [Integrate your table buckets with
AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md"), you can create data sets from your tables and work with
them in Quick using SPICE or direct SQL queries from your query engine. Quick supports
Athena as a data source for S3 tables.

## Configure permissions for Quick to access tables

Before working with S3 table data in Quick you must grant permissions to the Quick service role, the Quick admin user, and grant Lake Formation permissions on the tables you want to access.

###### Grant permissions to the Quick service role

When set up Quick for the first time in your account, AWS creates a service role that allows Quick to access data sources in other AWS services, such as Athena or Amazon Redshift. The default role name is `aws-quicksight-service-role-v0`.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles** and select the Quick service role. The default name is `aws-quicksight-service-role-v0`
3. Choose **Add permissions** and then **Create inline policy**.
4. Select **JSON** to open the JSON policy editor, then add the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "glue:GetCatalog",
 "Resource": "*"
 }
 ]
}`

```

5. Choose **Next**, enter a **Policy name** and then **Create policy**.

###### To configure permissions for the Quick admin user

1. Run the following AWS CLI command to find the ARN of your Quick admin user.

```
aws quicksight list-users --aws-account-id `111122223333` --namespace `default` --region `region`
```

2. Grant Lake Formation permissions to this ARN. For details, see [Managing access to a table or database with Lake Formation](grant-permissions-tables.md "grant-permissions-tables.md").

## Using table data in Quick

You can connect to table data using Athena as a data source.

###### Prerequisites

- [Integrate your table buckets with
  AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
  - [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md").
  - [Create a table](s3-tables-create.md "s3-tables-create.md").
  - [Configure permissions for Quick to access tables](#quicksight-permissions-tables "#quicksight-permissions-tables").

- [Sign up for Quick](../../../quicksight/latest/user/signing-up.md "../../../quicksight/latest/user/signing-up.md").

1. Sign in to your Quick account at [https://quicksight.aws.amazon.com/](https://quicksight.aws.amazon.com/. "https://quicksight.aws.amazon.com/.")
2. In the dashboard, choose **New analysis**.
3. Choose **New dataset**.
4. Select **Athena**.
5. Enter a **Data source name**, then choose **Create data source**.
6. Choose Use custom SQL. You will not be able to select your table from the **Choose your table** pane.
7. Enter an Athena SQL query that captures the columns you want to visualize, then choose **Confirm query**. For example, use the following query to select all columns:

```
SELECT * FROM "s3tablescatalog/`table-bucket-name`".`namespace`.`table-name`

```

8. Choose **Visualize** to analyze data and start building dashboards. For more information, see [Visualizing data in Quick](../../../quicksight/latest/user/working-with-visuals.md "../../../quicksight/latest/user/working-with-visuals.md") and [Exploring interactive dashboards in Quick](../../../quicksight/latest/user/using-dashboards.md "../../../quicksight/latest/user/using-dashboards.md")

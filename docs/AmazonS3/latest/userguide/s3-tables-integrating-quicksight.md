

# Visualizing table data with Quick
<a name="s3-tables-integrating-quicksight"></a>

Quick is a fast business analytics service to build visualizations, perform ad hoc analysis, and quickly get business insights from your data. Quick seamlessly discovers AWS data sources, enables organizations to scale to hundreds of thousands of users, and delivers fast and responsive query performance by using the Quick Super-fast, Parallel, In-Memory, Calculation Engine (SPICE). For more information, see [What is Quick?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) in the *Quick user guide*.

After you [Integrate your table buckets with AWS analytics services](s3-tables-integrating-aws.md), you can create data sets from your tables and work with them in Quick using SPICE or direct SQL queries from your query engine. Quick supports Athena as a data source for S3 tables.

## Configure permissions for Quick to access tables
<a name="quicksight-permissions-tables"></a>

Before working with S3 table data in Quick you must grant permissions to the Quick service role and the Quick admin user permissions on the tables you want to access. Additionally, if you use AWS Lake Formation, you also need to grant Lake Formation permissions to your Quick admin user on those tables you want to access.

**Grant permissions to the Quick service role**

When set up Quick for the first time in your account, AWS creates a service role that allows Quick to access data sources in other AWS services, such as Athena or Amazon Redshift. The default role name is `aws-quicksight-service-role-v0`.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Roles** and select the Quick service role. The default name is `aws-quicksight-service-role-v0`

1. Choose **Add permissions** and then **Create inline policy**.

1. Select **JSON** to open the JSON policy editor, then add the following policy.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "VisualEditor0",
         "Effect": "Allow",
         "Action": "glue:GetCatalog",
         "Resource": "*"
       }
     ]
   }
   ```

------

1. Choose **Next**, enter a **Policy name** and then **Create policy**.

**To configure Lake Formation permissions for the Quick admin user**

1. Run the following AWS CLI command to find the ARN of your Quick admin user.

   ```
   aws quicksight list-users --aws-account-id {{111122223333}} --namespace {{default}} --region {{region}}
   ```

1. Grant Lake Formation permissions to this ARN. For details, see [Managing access to a table or database with Lake Formation](grant-permissions-tables.md).

## Using table data in Quick
<a name="quicksight-connect-tables"></a>

You can connect to table data using Athena as a data source.

**Prerequisites**
+ [Integrate your table buckets with AWS analytics services](s3-tables-integrating-aws.md).
  + [Create a namespace](s3-tables-namespace-create.md).
  + [Create a table](s3-tables-create.md).
  + [Configure permissions for Quick to access tables](#quicksight-permissions-tables).
+ [Sign up for Quick](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html).

1. Sign in to your Quick account at [ https://quicksight.aws.amazon.com/](https://quicksight.aws.amazon.com/.)

1. In the dashboard, choose **New analysis**.

1. Choose **New dataset**.

1. Select **Athena**.

1. Enter a **Data source name**, then choose **Create data source**.

1. Choose Use custom SQL. You will not be able to select your table from the **Choose your table** pane. 

1. Enter an Athena SQL query that captures the columns you want to visualize, then choose **Confirm query**. For example, use the following query to select all columns:

   ```
   SELECT * FROM "s3tablescatalog/{{table-bucket-name}}".{{namespace}}.{{table-name}}
   ```

1. Choose **Visualize** to analyze data and start building dashboards. For more information, see [Visualizing data in Quick ](https://docs.aws.amazon.com/quicksight/latest/user/working-with-visuals.html) and [Exploring interactive dashboards in Quick ](https://docs.aws.amazon.com/quicksight/latest/user/using-dashboards.html)
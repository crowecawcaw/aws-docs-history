# Accessing Amazon S3 tables using the AWS Glue Iceberg REST endpoint

Once your S3 table buckets are integrated with the AWS Glue Data Catalog you can use the AWS Glue Iceberg REST endpoint to connect to your S3 tables from Apache Iceberg-compatible clients, such as PyIceberg or Spark. The AWS Glue Iceberg REST endpoint implements the [Iceberg REST Catalog Open API specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml "https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml") which provides a standardized interface for interacting with Iceberg tables. To access S3 tables using the endpoint you need to configure permissions through a combination of IAM policies and AWS Lake Formation grants. The following sections explain how to set up access, including creating the necessary IAM role, defining the required policies, and establishing Lake Formation permissions for both database and table-level access. 

For an end to end walkthrough using PyIceberg, see [Access data in Amazon S3 Tables using PyIceberg through the AWS Glue Iceberg REST endpoint](https://aws.amazon.com/blogs/storage/access-data-in-amazon-s3-tables-using-pyiceberg-through-the-aws-glue-iceberg-rest-endpoint/ "https://aws.amazon.com/blogs/storage/access-data-in-amazon-s3-tables-using-pyiceberg-through-the-aws-glue-iceberg-rest-endpoint/").


###### Prerequisites


* [Integrate your table buckets with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md")
* [Create a table namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md")
* [Have access to a data lake administrator account](https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin "https://docs.aws.amazon.com/lake-formation/latest/dg/initial-lf-config.html#create-data-lake-admin")

## Create an IAM role for your client


To access tables through AWS Glue endpoints, you need to create an IAM role with permissions to AWS Glue and Lake Formation actions. This procedure explains how to create this role and configure its permissions.


1. Open the IAM console at
 [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policies**.
3. Choose **Create a policy**, and choose **JSON** in policy editor.
4. Add the following inline policy that grants permissions to access AWS Glue and Lake Formation actions:



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "glue:GetCatalog",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:GetTable",
 "glue:GetTables",
 "glue:CreateTable",
 "glue:UpdateTable"
 ],
 "Resource": [
 "arn:aws:glue:us-east-1:111122223333:catalog",
 "arn:aws:glue:us-east-1:111122223333:catalog/s3tablescatalog",
 "arn:aws:glue:us-east-1:111122223333:catalog/s3tablescatalog/amzn-s3-demo-table-bucket",
 "arn:aws:glue:us-east-1:111122223333:table/s3tablescatalog/amzn-s3-demo-table-bucket/`<namespace>`/*",
 "arn:aws:glue:us-east-1:111122223333:database/s3tablescatalog/amzn-s3-demo-table-bucket/`<namespace>`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 }
 ]
}`

```
5. After you create the policy, create an IAM role and choose **Custom trust policy** as the **Trusted entity type**.
6. Enter the following for the **Custom trust policy**.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`Admin_role`"
 },
 "Action": "sts:AssumeRole",
 "Condition": {}
 }
 ]
}`

```

## Define access in Lake Formation


Lake Formation provides fine-grained access control for your data lake tables. When you integrated your S3 bucket with the AWS Glue Data Catalog, your tables were automatically registered as resources in Lake Formation. To access these tables, you must grant specific Lake Formation permissions to your IAM identity, in addition to its IAM policy permissions.


The following steps explain how to apply Lake Formation access controls to allow your Iceberg client to connect to your tables. You must sign in as a data lake administrator to apply these permissions.


### Allow external engines to access table data


In Lake Formation, you must enable full table access for external engines to access data. This allows third-party applications to get temporary credentials from Lake Formation when using an IAM role that has full permissions on the requested table.


Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), and sign in as a data lake administrator.
2. In the navigation pane under **Administration**, choose **Application integration settings**.
3. Select **Allow external engines to access data in Amazon S3 locations with full table access**. Then choose **Save**.

### Grant Lake Formation permissions on your table resources


Next, grant Lake Formation permissions to the IAM role you created for your Iceberg-compatible client. These permissions will allow the role to create and manage tables in your namespace. You need to provide both database and table-level permissions. For more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").


## Set up your environment to use the endpoint


After you have setup the IAM role with the permissions required for table access you can use it to run Iceberg clients from your local machine by configuring the AWS CLI with your role, using the following command:



```
aws sts assume-role --role-arn "arn:aws:iam::`<accountid>`:role/`<glue-irc-role>`" --role-session-name `<glue-irc-role>`
```

To access tables through the AWS Glue REST endpoint, you need to initialize a catalog in your Iceberg-compatible client. This initialization requires specifying custom properties, including sigv4 properties, the endpoint URI and the warehouse location. Specify these properties as follows:



* Sigv4 properties - Sigv4 must be enabled, the signing name is `glue`
* Warehouse location - This is your table bucket, specified in this format: ``<accountid>`:s3tablescatalog/`<table-bucket-name>``
* Endpoint URI - Refer to the AWS Glue service endpoints reference guide for the region-specific endpoint

The following example shows how to initialize a pyIceberg catalog.



```
rest_catalog = load_catalog(
        `s3tablescatalog`,
**{
"type": "rest",
"warehouse": "`<accountid>`:s3tablescatalog/`<table-bucket-name>`",
"uri": "https://glue.`<region>`.amazonaws.com/iceberg",
"rest.sigv4-enabled": "true",
"rest.signing-name": "glue",
"rest.signing-region": region
        }
)
```

For additional information about the AWS Glue Iceberg REST endpoint implementation, see [Connecting to the Data Catalog using AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html "https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html") in the *AWS Glue User Guide*.

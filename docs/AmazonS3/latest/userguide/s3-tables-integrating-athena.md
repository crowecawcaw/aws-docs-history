# Querying Amazon S3 tables with Athena

Amazon Athena is an interactive query service that you can use to analyze data directly in Amazon S3 by using
 standard SQL. For more information, see [What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html "https://docs.aws.amazon.com/athena/latest/ug/what-is.html") in the *Amazon Athena User Guide*.

After you integrate your table buckets with AWS analytics services, you can run Data Definition
 Language (DDL), Data Manipulation Language (DML), and Data Query Language (DQL) queries on S3 tables by
 using Athena. For more information about how to query tables in a table bucket, see [Register S3 Table
 bucket catalogs](https://docs.aws.amazon.com/athena/latest/ug/gdc-register-s3-table-bucket-cat.html "https://docs.aws.amazon.com/athena/latest/ug/gdc-register-s3-table-bucket-cat.html") in the *Amazon Athena User Guide*.

You can also run queries in Athena from the Amazon S3 console. 

###### Important

When creating tables, make sure that you use all lowercase letters in your table names and table
 definitions. For example, make sure that your column names are all lowercase. If your table name or
 table definition contains capital letters, the table isn't supported by AWS Lake Formation or the AWS Glue Data Catalog. In
 this case, your table won't be visible to AWS analytics services such as Amazon Athena, even if your table
 buckets are integrated with AWS analytics services. 

If your table definition contains capital letters, you receive the following error message when
 running a `SELECT` query in Athena: **`"GENERIC_INTERNAL_ERROR: Get table request
 failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation Resource -
 Invalid table or column names."`**

The following procedure uses the Amazon S3 console to access the Athena query editor so that you can
 query a table with Amazon Athena. 

###### Note

Before performing the following steps, make sure that you've integrated your table buckets with
 AWS analytics services in this Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics
 services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").

###### To query a table

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Table buckets**.
3. On the **Table buckets** page, choose the bucket that contains the table that
 you want to query.
4. On the bucket details page, choose the option button next to the name of the table that you
 want to query.
5. Choose **Query table with Athena**.
6. The Amazon Athena console opens and the Athena query editor appears with a sample
 `SELECT` query loaded for you. Modify this query as needed for your use case.


In the query editor, the **Catalog** field should be populated with
 **s3tablescatalog/** followed by the name of your table
 bucket, for example, **s3tablescatalog/`amzn-s3-demo-bucket`**. The
 **Database** field should be populated with the namespace where your table is
 stored. 


###### Note

If you don't see these values in the **Catalog** and
 **Database** fields, make sure that you've integrated your table buckets with
 AWS analytics services in this Region. For more information, see [Integrating Amazon S3 Tables with AWS analytics
 services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").
7. To run the query, choose **Run**.


###### Note



	* If you receive the error **`"Insufficient permissions to execute the query.
	 Principal does not have any privilege on specified resource"`** when you try to
	 run a query in Athena, you must be granted the necessary Lake Formation permissions on the table. For
	 more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").
	* If you receive the error **`"Iceberg cannot access the requested
	 resource"`** when you try to run the query, go to the AWS Lake Formation console and make
	 sure that you've granted yourself permissions on the table bucket catalog and database
	 (namespace) that you created. Don't specify a table when granting these permissions. For
	 more information, see [Granting Lake Formation permission on a table or database](grant-permissions-tables.md#grant-lf-table "grant-permissions-tables.md#grant-lf-table").
	* If you receive the following error message when running a `SELECT` query in
	 Athena, this message is caused by having capital letters in your table name or your column
	 names in your table definition: **`"GENERIC_INTERNAL_ERROR: Get table request
	 failed: com.amazonaws.services.glue.model.ValidationException: Unsupported Federation
	 Resource - Invalid table or column names."`** Make sure that your table and
	 column names are all lowercase.

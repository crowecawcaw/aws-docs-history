

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Query a database
<a name="query-databases"></a>

To query databases hosted by your Amazon Redshift cluster, you have two options:
+ Connect to your cluster and run queries on the AWS Management Console with the query editor. 

  If you use the query editor on the Amazon Redshift console, you don't have to download and set up a SQL client application. 
+ Connect to your cluster through a SQL client tool, such as SQL Workbench/J. 

  Amazon Redshift supports SQL client tools connecting through Java Database Connectivity (JDBC) and Open Database Connectivity (ODBC). Amazon Redshift doesn't provide or install any SQL client tools or libraries, so you must install them on your client computer or Amazon EC2 instance to use them. You can use most SQL client tools that support JDBC or ODBC drivers.

**Note**  
 When you write stored procedures, we recommend a best practice for securing sensitive values:   
 Don't hard code any sensitive information in stored procedure logic. For example, don't assign a user password in a CREATE USER statement in the body of a stored procedure. This poses a security risk, because hard-coded values can be recorded as schema metadata in catalog tables. Instead, pass sensitive values, such as passwords, as arguments to the stored procedure, by means of parameters.   
For more information about stored procedures, see [CREATE PROCEDURE](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_PROCEDURE.html) and [Creating stored procedures in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/stored-procedure-overview.html). For more information about catalog tables, see [System catalog tables](https://docs.aws.amazon.com/redshift/latest/dg/c_intro_catalog_views.html).
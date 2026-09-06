

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Set the application name connection property
<a name="discovering-metadata-application-name"></a>

When you connect to Amazon Redshift, set the optional application name driver property. This property identifies which application or tool established each connection, which makes it easier to monitor, audit, and troubleshoot your Amazon Redshift environment.

The application name that you provide appears in the `application_name` column of `SYS_CONNECTION_LOG`. You can use it to do the following:
+ **Track connection sources**. Identify which applications, services, or tools connect to your cluster.
+ **Troubleshoot performance**. Correlate queries with the originating application to isolate performance issues.
+ **Audit access**. Understand application-level usage patterns across your data warehouse.

The following table shows how to set the application name for each Amazon Redshift driver.


| Driver | Property | Example | 
| --- | --- | --- | 
| JDBC | ApplicationName | jdbc:redshift://{{endpoint}}:{{port}}/{{database}}?ApplicationName=my-etl-pipeline | 
| ODBC | ApplicationName | Set ApplicationName=my-bi-tool in the DSN or connection string. | 
| Python | application\_name | redshift\_connector.connect(..., application\_name='my-data-catalog') | 

For more information about the application name property for each driver, see the following:
+ JDBC: [ApplicationName](https://docs.aws.amazon.com/redshift/latest/mgmt/jdbc20-configuration-options.html#jdbc20-applicationname-option)
+ ODBC: [ApplicationName](https://docs.aws.amazon.com/redshift/latest/mgmt/odbc20-configuration-options.html#odbc20-application_name-option)
+ Python: [application\_name](https://docs.aws.amazon.com/redshift/latest/mgmt/python-configuration-options.html#python-application_name-option)

**Note**  
Use a descriptive, consistent naming convention for application names, such as `{{team}}-{{service}}-{{environment}}` (for example, `quicksight-analytics-dashboard-prod`). This approach makes it easier to filter and analyze `SYS_CONNECTION_LOG` data.
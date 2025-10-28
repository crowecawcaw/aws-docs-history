Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query performance tuning

Amazon Redshift uses queries based on structured query language (SQL) to interact with data and
objects in the system. Data manipulation language (DML) is the subset of SQL that you use to
view, add, change, and delete data. Data definition language (DDL) is the subset of SQL that
you use to add, change, and delete database objects such as tables and views.

Once your system is set up, you typically work with DML the most, especially the [SELECT](r_SELECT_synopsis.md "r_SELECT_synopsis.md") command for retrieving and
viewing data. To write effective data retrieval queries in Amazon Redshift, become familiar with
SELECT and apply the tips outlined in [Amazon Redshift best practices for designing
tables](c_designing-tables-best-practices.md "c_designing-tables-best-practices.md") to maximize query efficiency.

To understand how Amazon Redshift processes queries, use the [Query processing](c-query-processing.md "c-query-processing.md") and [Query analysis and improvement](c-query-tuning.md "c-query-tuning.md") sections. Then you can apply this information in
combination with diagnostic tools to identify and remove issues in query performance.

To identify and address some of the most common and most serious issues you are likely to
encounter with Amazon Redshift queries, use the [Query troubleshooting](queries-troubleshooting.md "queries-troubleshooting.md") section.

###### Topics

- [Query processing](c-query-processing.md "c-query-processing.md")
- [Query analysis and improvement](c-query-tuning.md "c-query-tuning.md")
- [Query troubleshooting](queries-troubleshooting.md "queries-troubleshooting.md")

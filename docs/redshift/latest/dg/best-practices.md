Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift best practices

Following, you can find best practices for planning a proof of concept, designing tables, loading data into tables, and
writing queries for Amazon Redshift, and also a discussion of working with Amazon Redshift Advisor.

Amazon Redshift is not the same as other SQL database systems. To fully realize the benefits of
the Amazon Redshift architecture, you must specifically design, build, and load your tables to use
massively parallel processing, columnar data storage, and columnar data compression. If your
data loading and query execution times are longer than you expect, or longer than you want,
you might be overlooking key information.

If you are an experienced SQL database developer, we strongly recommend that you review
this topic before you begin developing your Amazon Redshift data warehouse.

If you are new to developing SQL databases, this topic is not the best place to start. We
recommend that you begin by reading
[Run commands to define and use a database in your data warehouse](../gsg/database-tasks.md "../gsg/database-tasks.md") in the
_Amazon Redshift Getting Started Guide_,
and trying the examples yourself.

In this topic, you can find an overview of the most important development principles, along
with specific tips, examples, and best practices for implementing those principles. No single
practice can apply to every application. Evaluate all of your options before finishing a
database design. For more information, see [Automatic table optimization](t_Creating_tables.md "t_Creating_tables.md"), [Loading data in Amazon Redshift](t_Loading_data.md "t_Loading_data.md"), [Query performance tuning](c-optimizing-query-performance.md "c-optimizing-query-performance.md"), and the reference chapters.

###### Topics

- [Conduct a proof of concept (POC) for Amazon Redshift](proof-of-concept-playbook.md "proof-of-concept-playbook.md")
- [Amazon Redshift best practices for designing
  tables](c_designing-tables-best-practices.md "c_designing-tables-best-practices.md")
- [Amazon Redshift best practices for loading
  data](c_loading-data-best-practices.md "c_loading-data-best-practices.md")
- [Amazon Redshift best practices for designing
  queries](c_designing-queries-best-practices.md "c_designing-queries-best-practices.md")
- [Follow recommendations from Amazon Redshift Advisor](advisor.md "advisor.md")

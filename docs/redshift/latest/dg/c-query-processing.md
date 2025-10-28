Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Query processing

Amazon Redshift routes a submitted SQL query through the parser and optimizer to develop a
query plan. The execution engine then translates the query plan into code and sends that
code to the compute nodes for execution.

###### Topics

- [Query planning and execution workflow](c-query-planning.md "c-query-planning.md")
- [Creating and interpreting a query plan](c-the-query-plan.md "c-the-query-plan.md")
- [Reviewing query plan steps](reviewing-query-plan-steps.md "reviewing-query-plan-steps.md")
- [Factors affecting query performance](c-query-performance.md "c-query-performance.md")

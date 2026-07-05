Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Query processing

Amazon Redshift routes a submitted SQL query through the parser and optimizer to develop a
query plan. The execution engine then translates the query plan into code and sends that
code to the compute nodes for execution.

###### Topics

- [Query planning and execution workflow](c-query-planning.md "c-query-planning.md")
- [Creating and interpreting a query plan](c-the-query-plan.md "c-the-query-plan.md")
- [Reviewing query plan steps](reviewing-query-plan-steps.md "reviewing-query-plan-steps.md")
- [Factors affecting query performance](c-query-performance.md "c-query-performance.md")

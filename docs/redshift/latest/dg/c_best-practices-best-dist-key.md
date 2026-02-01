Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Choose the best distribution

style

When you run a query, the query optimizer redistributes the rows to the compute
nodes as needed to perform any joins and aggregations. The goal in selecting a table
distribution style is to minimize the impact of the redistribution step by locating the
data where it needs to be before the query is run.

###### Note

When you use automatic table optimization, you don't need to choose the distribution style of your table.
For more information, see [Automatic table optimization](t_Creating_tables.md "t_Creating_tables.md").

Some suggestions for the best approach follow:

1. Distribute the fact table and one dimension table on
   their common columns.

Your fact table can have only one distribution key. Any tables that join on
another key aren't collocated with the fact table. Choose one dimension to
collocate based on how frequently it is joined and the size of the joining rows.
Designate both the dimension table's primary key and the fact table's
corresponding foreign key as the DISTKEY. 2. Choose the largest dimension based on the size of the
filtered dataset.

Only the rows that are used in the join must be distributed, so consider the
size of the dataset after filtering, not the size of the table. 3. Choose a column with high cardinality in the filtered
result set.

If you distribute a sales table on a date column, for example, you should
probably get fairly even data distribution, unless most of your sales are
seasonal. However, if you commonly use a range-restricted predicate to filter for
a narrow date period, most of the filtered rows occur on a limited set of slices
and the query workload is skewed. 4. Change some dimension tables to use ALL
distribution.

If a dimension table cannot be collocated with the fact table or other
important joining tables, you can improve query performance significantly by
distributing the entire table to all of the nodes. Using ALL distribution
multiplies storage space requirements and increases load times and maintenance
operations, so you should weigh all factors before choosing ALL
distribution.
To have Amazon Redshift choose the appropriate distribution style, specify `AUTO` for
the distribution style.

For more information about choosing distribution styles, see [Data distribution for query optimization](t_Distributing_data.md "t_Distributing_data.md").

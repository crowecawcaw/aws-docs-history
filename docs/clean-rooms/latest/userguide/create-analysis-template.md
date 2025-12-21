# Analysis templates in AWS Clean Rooms

Analysis templates work with the [Custom analysis rule in AWS Clean Rooms](analysis-rules-custom.md "analysis-rules-custom.md"). With an analysis template, you can define parameters
to help you reuse the same query. AWS Clean Rooms supports a subset of parameterization with literal
values.

Analysis templates are collaboration-specific. For each collaboration, members can only see
the queries in that collaboration. If you plan to use differential privacy in a collaboration,
you should make sure that your analysis templates are compatible with the [general-purpose query structure](analysis-rules-custom.md#dp-query-structure-syntax "analysis-rules-custom.md#dp-query-structure-syntax") of AWS Clean Rooms
Differential Privacy.

You can create an analysis template in two ways: using SQL code or using Python code for
Spark.

###### Topics

- [SQL analysis templates](sql-analysis-templates.md "sql-analysis-templates.md")
- [PySpark analysis templates](pyspark-analysis-templates.md "pyspark-analysis-templates.md")
- [Troubleshooting PySpark analysis
  templates](troubleshooting-pyspark-analysis-templates.md "troubleshooting-pyspark-analysis-templates.md")

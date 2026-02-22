# Query timeout when using Athena

with Amazon Quick Sight

If your query times out, you can try these options to resolve your problem.

If the failure was generated while working on an analysis, remember that the
Amazon Quick Sight timeout for generating any visual is two minutes. If you're using a custom
SQL query, you can simplify your query to optimize running time.

If you are in direct query mode (not using SPICE), you can try
importing your data to SPICE. However, if your query exceeds the
Athena 30-minute timeout, you might get another timeout while importing data into
SPICE. For the most current information on Athena limits, see
[Amazon Athena Limits](../../../general/latest/gr/aws_service_limits.md#amazon-athena-limits "../../../general/latest/gr/aws_service_limits.md#amazon-athena-limits") in the _AWS General Reference_.

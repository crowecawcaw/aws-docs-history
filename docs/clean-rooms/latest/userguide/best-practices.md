# Best practices for data collaborations in AWS Clean Rooms

This topic describes the best practices for conducting data collaborations in
AWS Clean Rooms.

AWS Clean Rooms follows the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/"). AWS Clean Rooms offers [analysis rules](analysis-rules.md "analysis-rules.md") that you can configure to strengthen your ability to protect sensitive
data in a collaboration. The analysis rules that you configure in AWS Clean Rooms will enforce the
restrictions (query controls and query output controls) that you have configured. You are
responsible for determining the restrictions and configuring analysis rules accordingly.

Data collaborations might involve more than just your use of AWS Clean Rooms. To help you maximize
the benefit of data collaborations, we recommend that you perform the following best practices
with your use of AWS Clean Rooms and specifically with analysis rules.

###### Topics

- [Best practices with AWS Clean Rooms](#best-practices-with-clean-rooms "#best-practices-with-clean-rooms")
- [Best practices for using analysis rules in
  AWS Clean Rooms](#best-practices-for-analysis-rules "#best-practices-for-analysis-rules")

## Best practices with AWS Clean Rooms

You're responsible for assessing the risk of each data collaboration and comparing it to
your privacy requirements such as external and internal compliance programs and policies. We
recommend that you take additional actions with your use of AWS Clean Rooms. These actions might help
further manage risks and help guard against third-party attempts to re-identify your data (for
example, differencing attacks or side-channel attacks).

For example, consider conducting due diligence on your other collaborators and enter into
legal agreements with them _before_ engaging in a collaboration.
To monitor the use of your data, also consider adopting other audit mechanisms with your use of
AWS Clean Rooms.

## Best practices for using analysis rules in

AWS Clean Rooms

Analysis rules in AWS Clean Rooms allow you to restrict the queries that can be run by setting
query controls on a configured table. For example, you can set a query control for how a
configured table can be joined and which columns can be selected. You can also restrict the query
output through setting query result controls such as aggregation thresholds on output rows. The
service rejects any query and removes rows that don’t comply with the analysis rules set by
members on their configured tables in the query.

We recommend the following _10 best practices_ for using
analysis rules on your configured table:

- Create separate configured tables for separate query use cases (for example, audience
  planning or attribution). You can create multiple configured tables with the same underlying
  AWS Glue table.
- Specify columns in the analysis rule (for example, dimension columns, list columns, join
  columns) that are necessary for queries in a collaboration. This might help mitigate the risk
  of differencing attacks or enabling other members to reverse engineer your data. Use the
  **allowlist columns** feature to note other columns that you might want to
  make queryable in the future. To customize the columns that can be used for a certain
  collaboration, create additional configured tables with the same underlying AWS Glue table.
- Specify the functions in the analysis rule that are necessary for analysis in the
  collaboration. This can help mitigate risk from rare function errors that can present
  information on an individual data point. To customize the functions that can be used for a
  certain collaboration, create additional configured tables with the same underlying AWS Glue
  table.
- Add aggregation constraints on any columns whose values at a row-level are sensitive. This
  includes columns in your configured table that also exist in other collaboration members’
  tables and analysis rules as an aggregation constraint.
  This
  also includes columns in your configured table that aren't queryable, that is, columns that are
  in your configured table but are not in the analysis
  rule. Aggregation constraints can help mitigate
  risk from correlating query results with data outside the collaboration.
- Create test collaborations and analysis rules to test restrictions created with specified
  analysis rules.
- Review collaborator configured tables and members’ analysis rules on configured tables to
  check that they match what was agreed upon for the collaboration. This can help mitigate risk
  from other members engineering their own data to run queries that weren't agreed upon.
- Review the example query provided (console only) that is enabled on your configured table
  after you set up the analysis rule.

###### Note

In addition to the provided example query, other queries are possible based on the
analysis rule and other collaboration member tables and analysis rules.

- You can add or update an analysis rule for a configured table in a collaboration. When you
  do, review all the collaborations where the configured table is associated and its resulting
  impact. This helps make sure that no collaborations use obsolete analysis rules.
- Review the queries run in the collaboration to check that the queries match the use cases
  or queries that were agreed upon for the collaboration. (The queries are available in the query
  logs when the **Query logging** feature is turned on.) This can help mitigate
  risk from members running analysis that was not agreed upon and potential attacks such as side
  channel attacks.
- Review the configured table columns used in collaboration members’ analysis rules and in
  queries to check that they match what was agreed upon in the collaboration. (The queries are
  available in the query logs when that feature is turned on.) This can help mitigate risk from
  other members engineering their own data to do queries that weren't agreed upon.

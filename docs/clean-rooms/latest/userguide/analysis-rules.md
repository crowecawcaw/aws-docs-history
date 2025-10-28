# Analysis rules in AWS Clean Rooms

As part of enabling a table to use in AWS Clean Rooms for collaboration analysis, the collaboration
member must configure an _analysis rule_.

An analysis rule is a privacy-enhancing control that each data owner sets up on a configured
table. An analysis rule determines how the configured table can be analyzed.

The analysis rule is an account-level control on the configured table (an account-level
resource) and is enforced in any collaboration where the configured table is associated. If there
is no analysis rule configured, the configured table can be associated to collaborations but it
can’t be queried. Queries can only reference configured tables with the same analysis rule type.

To configure an analysis rule, you first select a type of analysis and then specify the
analysis rule. For both steps, you should consider the use case you want to enable and how you
want to protect your underlying data.

AWS Clean Rooms enforces the more restrictive controls across all configured tables referenced in a
query.

The following examples illustrate the restrictive controls.

###### Example Restrictive control: Output constraint

- Collaborator A has an output constraint on the identiﬁer column of 100.
- Collaborator B has an output constraint on the identiﬁer column of 150.

An aggregation query that references both conﬁgured tables requires at least 150 distinct
values of identiﬁer within an output row for it to be displayed in the query output. The query
output doesn't indicate that results are removed because of the output constraint.

###### Example Restrictive control: Analysis template not approved

- Collaborator A has allowed an analysis template with a query that references configured
  tables from Collaborator A and Collaborator B in their custom analysis rule.
- Collaborator B hasn't allowed the analysis template.

Because Collaborator B hasn't allowed the analysis template, the member who can query
can’t run that analysis template.

## Analysis rule types

There are three types of analysis rules: [aggregation](analysis-rules-aggregation.md "analysis-rules-aggregation.md"), [list](analysis-rules-list.md "analysis-rules-list.md") and [custom](analysis-rules-custom.md "analysis-rules-custom.md"). The following tables compare the analysis rule
types. Each type has a separate section that describes specifying the analysis rule.

###### Note

There is an analysis rule type called the ID mapping table analysis rule. However, this
analysis rule is managed by AWS Clean Rooms and can’t be modified. For more information, see [ID mapping table analysis rule](analysis-rules-id-mapping-table.md "analysis-rules-id-mapping-table.md").

The following sections describe supported use cases and controls for each analysis rule
type.

### Supported use cases

The following tables show a comparison summary of the supported use cases for each analysis
rule type.

| Use case                                           | [Aggregation](analysis-rules-aggregation.md "analysis-rules-aggregation.md")                                                                                                                                                                                                                                                                                                                                                                     | [List](analysis-rules-list.md "analysis-rules-list.md")                                                                                                                   | [Custom](analysis-rules-custom.md "analysis-rules-custom.md")                                                                           |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Supported analyses**                             | Queries that aggregate statistics using COUNT, SUM, and AVG functions along optional dimensions                                                                                                                                                                                                                                                                                                                                                  | Queries that output row-level lists of the overlap between multiple tables                                                                                                | Any custom analysis as long as the analysis template or the analysis creator have been reviewed and allowed                             |
| **Common use cases**                               | Segment analysis, measurement, attribution                                                                                                                                                                                                                                                                                                                                                                                                       | Enrichment, segment building                                                                                                                                              | First-touch attribution, incremental analyses, audience discovery                                                                       |
| **SQL constructs**                                 | <br>• [JOIN statements](analysis-rules-aggregation.md#join-controls "analysis-rules-aggregation.md#join-controls"): INNER JOIN <br>• [Aggregate functions](analysis-rules-aggregation.md#agg-functions "analysis-rules-aggregation.md#agg-functions"): COUNT/COUNT DISTINCT, SUM/SUM DISTINCT, and AVG <br>• [Scalar functions](analysis-rules-aggregation.md#scalar-functions "analysis-rules-aggregation.md#scalar-functions"): Limited subset | <br>• [JOIN statements](analysis-rules-list.md#list-controls-join-controls "analysis-rules-list.md#list-controls-join-controls"): INNER JOIN <br>• Scalar functions: None | Majority of SQL functions and SQL constructs available with the SELECT command                                                          |
| **Subqueries and common table expressions (CTEs)** | No                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                                                                                                                                                                        | Yes                                                                                                                                     |
| **Analysis templates**                             | No                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                                                                                                                                                                        | Yes                                                                                                                                     | ### Supported controls The following tables show a comparison summary of how each analysis rule type protects your underlying data.                                                                                                                                                                                                                                                              |
| Control                                            | [Aggregation](analysis-rules-aggregation.md "analysis-rules-aggregation.md")                                                                                                                                                                                                                                                                                                                                                                     | [List](analysis-rules-list.md "analysis-rules-list.md")                                                                                                                   | [Custom](analysis-rules-custom.md "analysis-rules-custom.md")                                                                           |
| ---                                                | ---                                                                                                                                                                                                                                                                                                                                                                                                                                              | ---                                                                                                                                                                       | ---                                                                                                                                     |
| **Control mechanism**                              | Control how data in the table can be used in a query*(For example, allow COUNT and SUM of column hashed_email.)*                                                                                                                                                                                                                                                                                                                                 | Control how data in the table can be used in a query*(For example, allow use of column hashed_email only for joining.)*                                                   | Control what queries are allowed to run on the table*(For example, allow only queries defined in analysis templates "Custom query 1".)* |
| **Built-in privacy enhancing techniques**          | <br>• Blind match <br>• Aggregation required <br>• Min aggregation threshold >= <br>• 2 Pre-defined query structure                                                                                                                                                                                                                                                                                                                              | <br>• Blind match <br>• Overlap required <br>• Pre-defined query structure <br>• Allowed additional analyses                                                              | <br>• Differential privacy <br>• Disallowed output columns                                                                              |
| **Review query before it can be run**              | No                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                                                                                                                                                                        | Yes, using analysis templates                                                                                                           | For more information about the analysis rules that are available in AWS Clean Rooms, see the following topics. <br>• [Aggregation analysis rule](analysis-rules-aggregation.md "analysis-rules-aggregation.md") <br>• [List analysis rule](analysis-rules-list.md "analysis-rules-list.md") <br>• [Custom analysis rule in AWS Clean Rooms](analysis-rules-custom.md "analysis-rules-custom.md") |

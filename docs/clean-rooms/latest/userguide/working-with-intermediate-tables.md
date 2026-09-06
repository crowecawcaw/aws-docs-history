

# Intermediate tables in AWS Clean Rooms
<a name="working-with-intermediate-tables"></a>

An *intermediate table* is a collaboration-scoped resource in AWS Clean Rooms that caches analysis results within a collaboration for reuse in subsequent analyses.

Intermediate tables are created by the analysis runner who owns and manages them. The data is stored in AWS managed storage and is not exported outside the collaboration.

Before you can use an intermediate table in an analysis, you must first populate it. Then, attach a Custom analysis rule to it. The table must have a status of `POPULATE_SUCCESS` before it can be referenced in any analysis. You can reference intermediate tables by name in SQL queries and PySpark jobs, just like configured tables.

**Note**  
Storage for intermediate tables is billed at standard rates until the table is deleted.

A *base table* is any configured table, ID mapping table, or other intermediate table that is used in the analysis to populate an intermediate table.

**Deferred enforcement**

AWS Clean Rooms uses *deferred enforcement* for certain privacy controls on intermediate tables. AWS Clean Rooms does not evaluate deferred controls when you create or populate the intermediate table. Instead, AWS Clean Rooms enforces them at analysis time, when the intermediate table is referenced in a subsequent analysis.

Intermediate tables have the following classification types, which determine how deferred controls are applied:
+ **First-party** – All base tables used to populate the intermediate table are owned by the creator. The creator has full control over the analysis rule configuration.
+ **Multi-party** – Base tables come from different data providers. The creator can only make inherited controls more restrictive, not less.

The intermediate table inherits deferred controls from the base tables used to populate it. When you populate an intermediate table, AWS Clean Rooms captures the deferred controls from each base table's analysis rule. It then applies the most restrictive combination to the intermediate table.

The following table describes the deferred controls for intermediate tables.


| Deferred control | Description | 
| --- | --- | 
| Allowed result receivers | Specifies which collaboration members can receive the results of an analysis that references the intermediate table. Inherited as the intersection of all base tables' allowed result receivers. | 
| Disallowed output columns | Specifies columns that cannot appear in the output of an analysis. Inherited as the union of all base tables' disallowed output columns. | 
| Allowed additional analyses | Specifies whether the results of an analysis can be used as input to additional analyses. Inherited as the most restrictive value from the base tables. | 
| Additional analyses | Controls whether the intermediate table can be used in additional analyses beyond the initial analysis. Inherited as the most restrictive value from the base tables. | 

**Intermediate table statuses**

The following table describes the status lifecycle for an intermediate table.


| Status | Description | 
| --- | --- | 
| CREATED | The intermediate table resource exists but has no materialized data. | 
| POPULATE\_STARTED | A populate operation is in progress. | 
| POPULATE\_SUCCESS | Data has been successfully materialized in the intermediate table. | 
| POPULATE\_FAILED | The populate operation did not complete successfully. | 
| DISALLOWED\_BY\_DATA\_PROVIDER | A data provider has disallowed the intermediate table. The table can no longer be used in analyses until the data provider re-allows it. | 
| BASE\_TABLE\_REMOVED | One or more base tables used to populate the intermediate table have been removed from the collaboration. The intermediate table can no longer be used in analyses. | 
| RETENTION\_PERIOD\_EXPIRED | The intermediate table version has expired based on the configured retention period. All stored data has been cleaned up and the table must be repopulated in order to be used again. The default retention is 30 days. | 

**Budgets with intermediate tables**

You can configure access budgets and differential privacy budgets on intermediate tables, the same as configured tables.

**Access budgets**

AWS Clean Rooms decrements access budgets for the intermediate table and all base tables referenced in the analysis (including transitive dependencies for nested intermediate tables) at the following times:
+ **Creation or refresh** – Budgets are decremented because the populate operation executes an analysis against base tables.
+ **Usage** – Budgets are decremented because the intermediate table contains base table data. Every access to that data, even if cached, counts as a use of the base table for privacy tracking.

**Differential privacy budgets**

AWS Clean Rooms handles differential privacy budgets for intermediate tables as follows:
+ **Creation or refresh** – If base tables have differential privacy enabled, their differential privacy budgets are decremented. AWS Clean Rooms injects noise at this time. The analysis that populates the intermediate table must follow all restrictions for queries with differential privacy enabled.
+ **Usage** – If you configured differential privacy for the intermediate table, the epsilon for the collaboration's single budget owner is decremented. This applies regardless of who owns the intermediate table. If no budget exists, the analysis is rejected.

**Note**  
Differential privacy on intermediate tables treats the data in an intermediate table as a fresh dataset. AWS Clean Rooms injects noise based on the number of users in the intermediate table itself. If you amplify the number of users through a transformation when populating the intermediate table, the effect of that transformation on the original user population will not be tracked.

**Topics**
+ [Creating an intermediate table](create-intermediate-table.md)
+ [Populating an intermediate table](populate-intermediate-table.md)
+ [Configuring an analysis rule for an intermediate table](intermediate-table-analysis-rule.md)
+ [Deleting an intermediate table](delete-intermediate-table.md)
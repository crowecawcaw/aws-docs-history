# View execution plans for SQL queries

You can use the Athena query editor to see graphical representations of how your query will
be run. When you enter a query in the editor and choose the **Explain**
option, Athena uses an [EXPLAIN](athena-explain-statement.md "athena-explain-statement.md") SQL statement on your query to
create two corresponding graphs: a distributed execution plan and a logical execution plan.
You can use these graphs to analyze, troubleshoot, and improve the efficiency of your
queries.

###### To view execution plans for a query

1. Enter your query in the Athena query editor, and then choose
   **Explain**.

![Choose Explain in the Athena query editor.](images/query-plans-1.png)

The **Distributed plan** tab shows you the execution plan for
your query in a distributed environment. A distributed plan has processing fragments
or _stages_. Each stage has a zero-based index
number and is processed by one or more nodes. Data can be exchanged between
nodes.

![Sample query distributed plan graph.](images/query-plans-2.png) 2. To navigate the graph, use the following options:

    * To zoom in or out, scroll the mouse, or use the magnifying icons.
    * To adjust the graph to fit the screen, choose the **Zoom to
     fit** icon.
    * To move the graph around, drag the mouse pointer.

3. To see details for a stage, choose the stage.

![Choose a stage to see details for the stage.](images/query-plans-3.png) 4. To see the stage details full width, choose the expand icon at the top right of
the details pane. 5. To see more detail, expand one or more items in the operator tree. For information
about distributed plan fragments, see [EXPLAIN statement output types](athena-explain-statement-understanding.md#athena-explain-statement-understanding-explain-plan-types "athena-explain-statement-understanding.md#athena-explain-statement-understanding-explain-plan-types").

![Expanded operator tree for a stage in a distributed query plan.](images/query-plans-4.png)

###### Important

Currently, some partition filters may not be visible in the nested operator
tree graph even though Athena does apply them to your query. To verify the effect
of such filters, run [EXPLAIN](athena-explain-statement.md#athena-explain-statement-syntax-athena-engine-version-2 "athena-explain-statement.md#athena-explain-statement-syntax-athena-engine-version-2") or [EXPLAIN ANALYZE](athena-explain-statement.md#athena-explain-analyze-statement "athena-explain-statement.md#athena-explain-analyze-statement") on
your query and view the results. 6. Choose the **Logical plan** tab. The graph shows the logical plan
for running your query. For information about operational terms, see [Understand Athena EXPLAIN statement results](athena-explain-statement-understanding.md "athena-explain-statement-understanding.md").

![Graph of a logical query plan in Athena.](images/query-plans-5.png) 7. To export a plan as an SVG or PNG image, or as JSON text, choose
**Export**.

## Additional resources

For more information, see the following resources.

[Using EXPLAIN and EXPLAIN ANALYZE in Athena](athena-explain-statement.md "athena-explain-statement.md")

[Understand Athena EXPLAIN statement results](athena-explain-statement-understanding.md "athena-explain-statement-understanding.md")

[View statistics and execution details for completed queries](query-stats.md "query-stats.md")

Visual query execution analysis in Amazon Athena (AWS YouTube channel)

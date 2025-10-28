# Edit data flow steps

In Amazon SageMaker Canvas, you can edit individual steps in your data flows to transform your dataset
without having to create a new data flow. The following page covers how to edit join and
concatenate steps, as well as data source steps.

## Edit join and concatenate

steps

Within your data flows, you have the flexibility to edit your join and concatenate
steps. You can make necessary adjustments to your data processing workflow, ensuring
that your data is properly combined and transformed without having to redo your entire
data flow.

To edit a join or concatenate step in your data flow, do the following:

1. Open your data flow.
2. Choose the plus icon (**+**) next to the join or concatenate
   node that you want to edit.
3. From the context menu, choose **Edit**.
4. A side panel opens where you can edit the details of your join or
   concatenation. Modify your step fields, such as the type of join. To swap out a
   data node and select a different one to join or concatenate, choose the delete
   icon next to the node and then, in the data flow view, select the new node that
   you want to include in your transformation.

###### Note

When swapping out a node during the editing process, you can only select
steps that occur before the join or concatenate operation. You can swap
either the left or right node, but you can only swap one node at a time.
Additionally, you cannot select a source node as a replacement. 5. Choose **Preview** to view the result of the combining operation. 6. Choose **Update** to save your changes.

Your data flow should now be updated.

## Edit or replace a data source

step

You might need to make changes to your data source or dataset without deleting the
transforms and data flow steps applied to your original data. Within Data Wrangler, you can edit
or replace your data source configuration while keeping the steps of your data flow.
When editing a data source, you can change the import settings, such as the sampling
size or method and any advanced settings. You can also add more files with the same
schema, or for query-based data sources such as Amazon Athena, you can edit the query. When
replacing a data source, you have the option to select a different dataset, or even
import the data from a different data source altogether, as long as the schema of the
new data matches the original data.

To edit a data source configuration, do the following:

1. In the Canvas application, go to the **Data Wrangler**
   page.
2. Choose your data flow to view it.
3. In the **Data flow** tab that shows your data flow steps,
   find the **Source** node that you want to edit.
4. Choose the ellipsis icon next to the **Source** node.
5. From the context menu, choose **Edit**.
6. For Amazon S3 data sources and local upload, you have the option to select or
   upload more files with the same schema as your original data. For query-based
   data sources such as Amazon Athena, you can remove and select different tables in
   the visual query builder, or you can edit the SQL query directly. When you're
   done, choose **Next**.
7. For the **Import settings**, make any desired changes.
8. When you're done, choose **Save changes**.

Your data source should now be updated.

To replace a data source, do the following:

1. In the Canvas application, go to the **Data Wrangler**
   page.
2. Choose your data flow to view it.
3. In the **Data flow** tab that shows your data flow steps,
   find the **Source** node that you want to edit.
4. Choose the ellipsis icon next to the **Source** node.
5. From the context menu, choose **Replace**.
6. Go through the [create a data flow
   experience](canvas-data-flow.md "canvas-data-flow.md") to select another data source and data.
7. When you’ve selected your data and are ready to update the source node, choose
   **Save**.

You should now see the **Source** node updated in your data
flow.

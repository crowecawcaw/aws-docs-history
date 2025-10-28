# Lookup transform

Use this transform to add matching columns by looking them up on another catalog
table.

###### To add a Lookup transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Lookup**.
4. Select the diagram to add the node to your visual ETL job.
5. Connect the transform node to a data source node.
6. Select the node on the diagram to view details about the transform.
7. Under **Catalog**, select the catalog to use for lookup.
8. Under **Database**, select a database.
9. Under **Table**, select a table.
10. Under **Lookup key columns to match**, enter columns in the lookup
    table, separated by commas.
11. Under **Lookup columns to take**, enter columns in the lookup table
    to add to the data when a match is found.

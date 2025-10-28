# Derived column transform

The Derived Column transform allows you to define a new column based on a math formula
or SQL expression in which you can use other columns in the data, as well as constants and
literals. For instance, to derive a “percentage” column from the columns "success" and
"count", you can enter the SQL expression: "success \* 100 / count || '%'".

Example result:

| success | count | percentage |
| ------- | ----- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 14      | 100   | 14%        |
| 6       | 20    | 3%         |
| 3       | 40    | 7.5%       | ###### To add a Derived Column transform: 1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio. 2. Choose the plus icon to open the **Add nodes** menu. 3. Under **Transforms**, choose **Derived Column**. 4. Select the diagram to add the node to your visual ETL job. 5. Select the node on the diagram to view details about the transform. 6. Under **Name of derived column**, enter the name of a new column that will be generated. 7. Under **Column expression**, enter a SQL expression to define the new column based on existing columns. |

# Concatenate columns transform

The Concatenate transform allows you to build a new string column using the values of
other columns with an optional spacer. For example, if we define a concatenated column
“date” as the concatenation of “year”, “month” and “day” (in that order) with “-” as the
spacer, we would get:

| day | month | year | date       |
| --- | ----- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01  | 01    | 2020 | 2020-01-01 |
| 02  | 01    | 2020 | 2020-01-02 |
| 03  | 01    | 2020 | 2020-01-02 |
| 04  | 01    | 2020 | 2020-01-02 | ###### To add a Concatenate Columns transform: 1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio. 2. Choose the plus icon to open the **Add nodes** menu. 3. Under **Transforms**, choose **Concatenate Columns**. 4. Select the diagram to add the node to your visual ETL job. 5. Select the node on the diagram to view details about the transform. 6. Under **Concatenated column**, enter the name of a new column that will be generated. 7. Under **Columns**, select the input columns. 8. (Optional) Under **Spacer**, enter a string to place between concatenated fields. 9. (Optional) Under **Null value**, enter the string to use when a column value is null. |

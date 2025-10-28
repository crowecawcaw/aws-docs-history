# Regex extract transform

Use this transform to extract new columns from a string column with JSON data.

###### To add a Regex Extract transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Regex
   Extract**.
4. Select the diagram to add the node to your visual ETL job.
5. Select the node on the diagram to view details about the transform.
6. Under **Column to extract from**, choose a column from the data
   source you connected to the transform.
7. Under **Regular expression**, enter a regular expression to apply
   on the column. If there are multiple columns, the expression must have a number of
   groups equal to the number of columns.
8. Under **Extracted column**, enter the name of the column to contain
   the extracted regex.

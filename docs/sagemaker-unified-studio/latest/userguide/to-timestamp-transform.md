# To timestamp transform

You can use the transform To Timestamp to change the data type of a numeric or string
column into timestamp, so that it can be stored with that data type or applied to other
transforms that require a timestamp.

###### To add a To Timestamp transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **To
   Timestamp**.
4. Select the diagram to add the node to your visual ETL job.
5. Select the node on the diagram to view details about the transform.
6. Under **Column to convert**, select the column that you want to
   convert.
7. Under **Time format**, define how to parse the column selected by
   choosing the format.

If the value is a number, it can be expressed in seconds (Unix/Python timestamp),
milliseconds, or microseconds.

If the value is a formatted string, choose the "iso" type. The string needs to
conform to one of the variants of the ISO format, for example:
“2022-11-02T14:40:59.915Z“.

If you don’t know the type at this point or different rows use different types, then
you can choose ”autodetect“ and the system will make its best guess, with a small
performance cost. 8. Under **Column name**, enter a name for a new column that will be
generated for the timestamps. If a column name is not specified, the existing column
will be replaced instead of generating a new column.

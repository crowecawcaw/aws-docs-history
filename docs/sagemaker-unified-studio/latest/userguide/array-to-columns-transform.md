# Array to columns transform

The Array To Columns transform allows you extract some or all the elements of a column
of type array into new columns. The transform will fill the new columns as much as possible
if the array has enough values to extract, optionally taking the elements in the positions
specified.

For instance, if you have an array column “subnet”, which was the result of applying the
“Split String” transform on a ip v4 subnet, you can extract the first and forth positions
into new columns “first_octect” and “forth_octect”. The output of the transform in this
example would be (notice the last two rows have shorter arrays than expected):

| subnet              | first_octect | fourth_octect |
| ------------------- | ------------ | ------------- |
| [54, 240, 197, 238] | 54           | 238           |
| [192, 168, 0, 1]    | 192          | 1             |
| [192, 168]          | 192          |               |
| []                  |              |               |

###### To add an Array to Columns transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Array to
   Columns**.
4. Select the diagram to add the node to your visual ETL job.
5. Select the node on the diagram to view details about the transform.
6. Under **Array type column**, choose the column of type array from
   which the new columns are extracted.
7. Under **Output columns**, enter names for the output
   columns.
8. (Optional) Under **Array indexes to use**, enter numbers to
   indicate which columns to include.

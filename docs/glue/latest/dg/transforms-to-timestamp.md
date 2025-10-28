# Convert a column to timestamp type

You can use the transform _To timestamp_ to change the data type of a numeric or string column into timestamp,
so that it can be stored with that data type or applied to other transforms that require a timestamp.

###### To add a _To timestamp_ transform node in your job diagram

1. Open the Resource panel and then choose **To timestamp** to add a new
   transform to your job diagram. The node selected at the time of adding the node will be its parent.
2. (Optional) On the **Node properties** tab, you can enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. On the **Transform** tab, enter the name of the column to be converted.
4. On the **Transform** tab, define how to parse the column selected by choosing the type.

If the value is a number, it can be expressed in seconds (Unix/Python timestamp), milliseconds or microseconds, choose the corresponding option.

If the value is a formatted string, choose the "iso" type, the string needs to conform to one of the variants of the ISO format, for example: “2022-11-02T14:40:59.915Z“.

If you don’t know the type at this point or different rows use different types, then you can choose ”autodetect“ and the system will make its best guess, with a small performance cost. 5. (Optional) On the **Transform** tab, instead of converting the selected column, you can create a new one and keep the original by entering a name for the new column.

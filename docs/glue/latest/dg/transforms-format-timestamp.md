# Convert a timestamp column to a formatted string

Format a timestamp column into a string based on a pattern. You can use _Format timestamp_ to get date and time as a string with the desired format.
You can define the format using [Spark date syntax](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html "https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html")
as well as most of the [Python date codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes").

For example, if you want your date string to be formatted like “2023-01-01 00:00”,
you can define such format using the Spark syntax as “yyyy-MM-dd HH:mm” or the equivalent Python date codes as “%Y-%m-%d %H:%M”

###### To add a _Format timestamp_ transform node in your job diagram

1. Open the Resource panel and then choose **Format timestamp** to add a new
   transform to your job diagram. The node selected at the time of adding the node will be its parent.
2. (Optional) On the **Node properties** tab, you can enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. On the **Transform** tab, enter the name of the column to be converted.
4. On the **Transform** tab, enter the **Timestamp format** pattern to use,
   expressed using [Spark date syntax](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html "https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html")
   or [Python date codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes "https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes").
5. (Optional) On the **Transform** tab, instead of converting the selected column,
   you can create a new one and keep the original by entering a name for the new column.

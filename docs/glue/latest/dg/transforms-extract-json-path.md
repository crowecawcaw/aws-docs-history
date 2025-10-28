# Extracting a JSON path

This transform extracts new columns from a JSON string column. This transform is useful when you only need a few data elements and don't want to import the entire JSON content into the table schema.

###### To add an Extract JSON Path transform node to your job diagram

1. Open the Resource panel, and then choose **Extract JSON Path** to add a new
   transform to your job diagram. The node selected at the time of adding the node will be its parent.
2. In the node properties panel, you can enter a name for the node in
   the job diagram. If a node parent isn't already selected, choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. On the **Transform** tab, select the column containing the JSON string. Enter one of more JSON path expressions separated by commas, each one referencing how to extract a value out of the JSON array or object. For instance, if the JSON column contained an objects with properties "prop_1" and "prop2" you could extract both specifying their names "prop_1, prop_2".

If the JSON field has special characters, for instance to extract the property from this JSON `{"a. a": 1}` you could use the path `$['a. a']`. The exception is the comma because it is reserved to separate paths. Then enter the corresponding column names for each path, separated by commas. 4. (Optional) On the **Transform** tab, you can check to drop the JSON column once extracted, this makes sense when you don't need the rest of the JSON data once you have extracted the parts you need.

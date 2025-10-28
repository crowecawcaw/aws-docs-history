# Parsing a string column containing JSON data

This transform parses a string column containing JSON data and convert it to a struct or an array column, depending if the JSON is an object or an array, respectively. Optionally you can keep both the parsed and original column.

The JSON schema can be provided or inferred (in the case of JSON objects), with optional sampling.

###### To add a Parse JSON Column transform node to your job diagram

1. Open the Resource panel, and then choose **Parse JSON Column** to add a new
   transform to your job diagram. The node selected at the time of adding the node will be its parent.
2. In the node properties panel, you can enter a name for the node in
   the job diagram. If a node parent isn't already selected, choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. On the **Transform** tab, select the column containing the JSON string.
4. (Optional) On the **Transform** tab, enter the schema that the JSON data follows using SQL syntax, for instance: "field1 STRING, field2 INT" in the case of an object or "ARRAY<STRING>" in the case of an array.

If the case of an array the schema is required but in the case of an object, if the schema is not specified it will be inferred using the data. To reduce the impact of inferring the schema (especially on a large dataset), you can avoid reading the whole data twice by entering a **Ratio of samples to use to infer schema**. If the value is lower than 1, the corresponding ratio of random samples is used to infer the schema. If the data is reliable and the object is consistent between rows, you can use a small ratio such as 0.1 to improve performance. 5. (Optional) On the **Transform** tab, you can enter a new column name if you want to keep both the original string column and the parsed column.

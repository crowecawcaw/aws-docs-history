# Removing null rows

This transform removes from the dataset rows that have all columns as null. In addition, you can extend this criteria to include empty fields, so as to keep rows where at least one column is non empty.

###### To add a Remove Null Rows transform node to your job diagram

1. Open the Resource panel, and then choose **Remove Null Rows** to add a new
   transform to your job diagram. The node selected at the time of adding the node will be its parent.
2. In the node properties panel, you can enter a name for the node in
   the job diagram. If a node parent isn't already selected, choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. (Optional) On the **Transform** tab, check the **Extended** option if you want to require rows not just to not be null but also not empty, this way empty strings, arrays or maps will be considered nulls for the purpose of this transform.

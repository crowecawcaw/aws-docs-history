# Add an identifier column

Assign a numeric _Identifier_ for each row in the dataset.

###### To add an _Identifier_ transform node in your job diagram

1. Open the Resource panel and then choose **Identifier** to add a new
   transform to your job diagram. The node selected at the time of adding the node will be its parent.
2. (Optional) On the **Node properties** tab, you can enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. (Optional) On the **Transform** tab, you can customize the name of the new column. By default, it will be named "id".
4. (Optional) If the job processes and stores data incrementally, you want to avoid the same ids to be reused between job runs.

On the **Transform** tab, mark the **unique** checkbox option. It will include the job timestamp in the identifier, making it unique between multiple runs.
To allow for the larger number, the column instead of type long will be a decimal.

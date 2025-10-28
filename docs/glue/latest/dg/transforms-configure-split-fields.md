# Using SplitFields to split a dataset

into two

The _SplitFields_ transform allows you to choose some of the data
property keys in the input dataset and put them into one dataset and the unselected keys
into a separate dataset. The output from this transform is a collection of
`DynamicFrames`.

###### Note

You must use a _SelectFromCollection_ transform to convert the
collection of `DynamicFrames` into a single `DynamicFrame` before
you can send the output to a target location.

The _SplitFields_ transform is case sensitive. Add an
_ApplyMapping_ transform as a parent node if you need case-insensitive
property key names.

###### To add a SplitFields transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **SplitFields** to add a new
   transform to your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab.
4. Choose which property keys you want to put into the first dataset. The keys that you
   do not choose are placed in the second dataset.
5. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here.
6. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.
7. Configure a _SelectFromCollection_ transform node to process the
   resulting datasets.

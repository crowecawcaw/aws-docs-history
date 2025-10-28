# Using SelectFields to remove most data

property keys

You can create a subset of data property keys from the dataset using the
_SelectFields_ transform. You indicate which data property keys you
want to keep and the rest are removed from the dataset.

###### Note

The _SelectFields_ transform is case sensitive. Use
_ApplyMapping_ if you need a case-insensitive way to select
fields.

###### To add a SelectFields transform node to your job diagram

1. (Optional) Open the Resource panel, and then choose **SelectFields** to add a new
   transform to your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent is not already selected, choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab in the node details
   panel.
4. Under the heading **SelectFields**, choose the data property keys
   in the dataset that you want to keep. Any data property keys not selected are dropped
   from the dataset.

You can also choose the check box next to the column heading
**Field** to automatically choose all the data property keys in the
dataset. Then you can deselect individual data property keys to remove them from the
dataset. 5. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here. 6. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

# Using DropFields to keep most data

property keys

You can create a subset of data property keys from the dataset using the
_DropFields_ transform. You indicate which data property keys you want
to remove from the dataset and the rest of the keys are retained.

###### Note

The _DropFields_ transform is case sensitive. Use
_Change Schema_ if you need a case-insensitive way to select
fields.

###### To add a DropFields transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **DropFields** to add a new
   transform to your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab in the node details
   panel.
4. Under the heading **DropFields**, choose the data property keys to
   drop from the data source.

You can also choose the check box next to the column heading
**Field** to automatically choose all the data property keys in the
dataset. Then you can deselect individual data property keys so they are retained in the
dataset. 5. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here. 6. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

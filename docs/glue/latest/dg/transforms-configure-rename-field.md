# Renaming a field in the dataset

You can use the _RenameField_ transform to change the name for an
individual property key in the dataset.

###### Note

The _RenameField_ transform is case sensitive. Use
_ApplyMapping_ if you need a case-insensitive transform.

###### Tip

If you use the _Change Schema_ transform, you can rename multiple
data property keys in the dataset with a single transform.

###### To add a RenameField transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **RenameField** to add a new
   transform to your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab.
4. Under the heading **Data field**, choose a property key from the
   source data and then enter a new name in the **New field name** field.
5. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here.
6. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

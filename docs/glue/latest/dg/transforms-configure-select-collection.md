# Using SelectFromCollection to

choose which dataset to keep

Use the _SelectFromCollection_ transform to convert a collection of
`DynamicFrames` into a single `DynamicFrame`.

###### To add a SelectFromCollection transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **SelectFromCollection** to add a
   new transform to your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent is not already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab.
4. Under the heading **Frame index**, choose the array index number
   that corresponds to the `DynamicFrame` you want to select from the collection
   of `DynamicFrames`.

For example, if the parent node for this transform is a
_SplitFields_ transform, on the
**Output schema** tab of that node you can see the schema for
each `DynamicFrame`. If you want to keep the `DynamicFrame`
associated with the schema for **Output 2**, you would select
`1` for the value of **Frame index**, which is
the second value in the list.

Only the `DynamicFrame` that you choose is included in the output. 5. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here. 6. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

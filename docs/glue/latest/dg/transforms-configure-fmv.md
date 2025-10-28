# Find and fill missing values in a dataset

You can use the _FillMissingValues_ transform to locate records in
the dataset that have missing values and add a new field with a value determined by
imputation. The input data set is used to train the machine learning (ML) model that
determines what the missing value should be. If you use incremental data sets, then each
incremental set is used as the training data for the ML model, so the results might not be
as accurate.

###### To use a FillMissingValues transform node in your job diagram

1. (Optional) Open the Resource panel and then choose **FillMissingValues** to add
   a new transform to your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent isn't already selected, choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab.
4. For **Data field**, choose the column or field name from the source
   data that you want to analyze for missing values.
5. (Optional) In the **New field name** field, enter a name for the
   field added to each record that will hold the estimated replacement value for the
   analyzed field. If the analyzed field doesn't have a missing value, the value in the
   analyzed field is copied into the new field.

If you don't specify a name for the new field, the default name is the name of the
analyzed column with `_filled` appended. For example, if you enter
`Age` for **Data field** and don't specify a
value for **New field name**, a new field named
`Age_filled` is added to each record. 6. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here. 7. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

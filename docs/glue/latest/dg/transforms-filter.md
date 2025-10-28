# Filtering keys within a dataset

Use the _Filter_ transform to create a new dataset by filtering
records from the input dataset based on a regular expression. Rows that don't satisfy the
filter condition are removed from the output.

- For string data types, you can filter rows where the key value matches a specified
  string.
- For numeric data types, you can filter rows by comparing the key value to a
  specified value using the comparison operators `<`, `>`,
  `=`, `!=`, `<=`, and `>=`.
  If you specify multiple filter conditions, the results are combined using an
  `AND` operator by default, but you can choose `OR` instead.

The _Filter_ transform is case sensitive. Add an
_ApplyMapping_ transform as a parent node if you need case-insensitive
property key names.

###### To add a Filter transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **Filter** to add a new transform to
   your job diagram, if needed.
2. On the **Node properties** tab, enter a name for the node in
   the job diagram. If a node parent isn't already selected, then choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab.
4. Choose either **Global AND** or **Global OR**.
   This determines how multiple filter conditions are combined. All conditions are combined
   using either `AND` or `OR` operations. If you have only a single
   filter conditions, then you can choose either one.
5. Choose the **Add condition** button in the **Filter
   condition** section to add a filter condition.

In the **Key** field, choose a property key name from the dataset.
In the **Operation** field, choose the comparison operator. In the
**Value** field, enter the comparison value. Here are some examples
of filter conditions:

    * `year >= 2018`
    * `State matches 'CA*'`

When you filter on string values, make sure that the comparison value uses a regular
expression format that matches the script language selected in the job properties
(Python or Scala). 6. Add additional filter conditions, as needed. 7. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here. 8. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

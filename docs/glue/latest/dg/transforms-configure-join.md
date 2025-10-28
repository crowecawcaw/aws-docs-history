# Joining datasets

The _Join_ transform allows you to combine two datasets into one. You
specify the key names in the schema of each dataset to
compare. The output `DynamicFrame` contains rows where keys meet the join
condition. The rows in each dataset that meet the join condition are combined into a single
row in the output `DynamicFrame` that contains all the columns found in either
dataset.

###### To add a Join transform node to your job diagram

1. If there is only one data source available, you must add a new data source node to
   the job diagram.
2. Choose one of the source nodes for the join. Open the Resource panel
   and then choose **Join** to add a new transform to your job
   diagram.
3. On the **Node properties** tab, enter a name for the node in
   the job diagram.
4. In the **Node properties** tab, under the heading
   **Node parents**, add a parent node so that there are two datasets
   providing inputs for the join. The parent can be a data source node or a transform node.

###### Note

A join can have only two parent nodes. 5. Choose the **Transform** tab.

If you see a message indicating that there are conflicting key names, you can
either:

    * Choose **Resolve it** to automatically add an
     *ApplyMapping* transform node to your job diagram. The
     ApplyMapping node adds a prefix to any keys in the dataset that have the same name
     as a key in the other dataset. For example, if you use the default value of
     `right`, then any keys in the right dataset that have the
     same name as a key in the left dataset will be renamed to `(right)*key
     name*`.
    * Manually add a transform node earlier in the job diagram to remove or rename the
     conflicting keys.

6. Choose the type of join in the **Join type** list.
   - **Inner join**: Returns a row with columns from both datasets
     for every match based on the join condition. Rows that don't satisfy the join
     condition aren't returned.
   - **Left join**: All rows from the left dataset and only the rows
     from the right dataset that satisfy the join condition.
   - **Right join**: All rows from the right dataset and only the
     rows from the left dataset that satisfy the join condition.
   - **Outer join**: All rows from both datasets.
   - **Left semi join**: All rows from the left dataset that have a
     match in the right dataset based on the join condition.
   - **Left anti join**: All rows in the left dataset that don't
     have a match in the right dataset based on join condition.

7. On the **Transform** tab, under the heading
   **Join conditions**, choose **Add condition**.
   Choose a property key from each dataset to compare.
   Property keys on the left side of the comparison operator are referred to as the left
   dataset and property keys on the right are referred to as the right dataset.

For more complex join conditions, you can add additional matching keys by choosing
**Add condition** more than once. If you accidentally add a
condition, you can choose the delete icon (
![An outline of a trash can](images/delete-icon-black.png)
) to remove it. 8. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here. 9. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.
For an example of the join output schema, consider a join between two datasets with the
following property keys:

```
Left: {id, dept, hire_date, salary, employment_status}
Right: {id, first_name, last_name, hire_date, title}
```

The join is configured to match on the `id` and `hire_date` keys
using the `=` comparison operator.

Because both datasets contain `id` and `hire_date` keys, you chose
**Resolve it** to automatically add the prefix
`right` to the keys in the right dataset.

The keys in the output schema would be:

```
{id, dept, hire_date, salary, employment_status,
(right)id, first_name, last_name, (right)hire_date, title}
```

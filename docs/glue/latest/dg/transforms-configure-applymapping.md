# Using Change Schema to remap data

property keys

A _Change Schema_ transform remaps the source data property keys into
the desired configured for the target data. In a Change Schema transform node, you
can:

- Change the name of multiple data property keys.
- Change the data type of the data property keys, if the new data type is supported
  and there is a transformation path between the two data types.
- Choose a subset of data property keys by indicating which data property keys you
  want to drop.
  You can also add additional _Change Schema_ nodes to the job diagram as
  needed – for example, to modify additional data sources or following a
  _Join_ transform.

##

Using Change Schema with decimal datatype

When using the **Change Schema** transform with decimal datatype, the **Change Schema**
transform modifies the precision to the default value of (10,2). To modify this and set the precision for your use case, you
can use the **SQL Query** transform and cast the columns with a specific precision.

For example, if you have an input column named "DecimalCol" of type Decimal, and you want to remap it to an output
column named "OutputDecimalCol" with a specific precision of (18,6), you would:

1. Add a subsequent **SQL Query** transform after the **Change Schema**
   transform.
2. In the **SQL Query** transform, use an SQL query to cast the remapped column to the desired
   precision. The SQL query would look like this:

```
SELECT col1, col2, CAST(DecimalCol AS DECIMAL(18,6)) AS OutputDecimalCol
FROM __THIS__
```

In the above SQL query:

    * `col1` and `col2` are other columns in your data that you want to pass through without modification.
    * `DecimalCol` is the original column name from the input data.
    * `CAST(DecimalCol AS DECIMAL(18,6))` casts the `DecimalCol` to a Decimal type with a precision of 18 digits and 6
     decimal places.
    * `AS OutputDecimalCol` renames the casted column to `OutputDecimalCol`.

By using the **SQL Query** transform, you can override the default precision set by the
**Change Schema** transform and explicitly cast the Decimal columns to the desired precision.
This approach allows you to leverage the **Change Schema** transform for renaming and
restructuring your data while handling the precision requirements for Decimal columns through the subsequent
**SQL Query** transformation.

## Adding a Change Schema transform to your job

###### Note

The **Change Schema** transform is not case-sensitive.

###### To add a Change Schema transform node to your job diagram

1. (Optional) Open the Resource panel and then choose **Change Schema**
   to add a new transform to your job diagram, if needed.
2. In the node properties panel, enter a name for the node in
   the job diagram. If a node parent isn't already selected, choose a node from the
   **Node parents** list to use as the input source for the
   transform.
3. Choose the **Transform** tab in the node properties panel.
4. Modify the input schema:
   - To rename a data property key, enter the new name of the key in the
     **Target key** field.
   - To change the data type for a data property key, choose the new data type for
     the key from the **Data type** list.
   - To remove a data property key from the target schema, choose the
     **Drop** check box for that key.

5. (Optional) After configuring the transform node properties, you can view the modified schema for your data by choosing the **Output schema** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. If you have not specified an IAM role on the **Job details** tab, you are prompted to enter an IAM role here.
6. (Optional) After configuring the node properties and transform properties, you can preview the modified dataset by choosing the **Data preview** tab in the node details panel. The first time you choose this tab for any node in your job, you are prompted to provide an IAM role to access the data. There is a cost associated with using this feature, and billing starts as soon as you provide an IAM role.

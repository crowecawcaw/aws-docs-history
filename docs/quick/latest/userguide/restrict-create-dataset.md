

# Restricting others from creating new datasets from your dataset
<a name="restrict-create-dataset"></a>

When you create a dataset in Amazon Quick, you can prevent others from using it as a source for other datasets. You can specify if others can use it to create any datasets at all. Or you can specify the type of datasets others can or can't create from your dataset, such as direct query datasets or SPICE datasets.

Use the following procedure to learn how to restrict others from creating new datasets from your dataset.

**To restrict others from creating new datasets from your dataset**

1. From the Quick start page, choose **Data** in the pane at left.

1. Choose **Create** then choose the dataset that you want to restrict creating new datasets from.

1. On the page that opens for that dataset, choose **Edit dataset**.

1. On the data preparation page that opens, choose **Manage** at upper right, and then choose **Properties**.

1. In the **Dataset properties** pane that opens, choose from the following options:
   + To restrict anyone from creating any type of new datasets from this dataset, turn off **Allow new datasets to be created from this one**.

     The toggle is blue when creating new datasets is allowed. It's gray when creating new datasets isn't allowed.
   + To restrict others from creating direct query datasets, clear **Allow direct query**.
   + To restrict others from creating SPICE copies of your dataset, clear **Allow SPICE copies**.

     For more information about SPICE datasets, see [Importing data into SPICE](spice.md).

1. Close the pane.